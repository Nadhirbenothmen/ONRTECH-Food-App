#!/usr/bin/env python
from concurrent.futures import ThreadPoolExecutor, as_completed
import glob
import json
import sys
import os
import re
from typing import List

import dacite
import tqdm
import requests
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
sys.path.append('src')
sys.path.append('./')

from src.model.product import Evolution, Product
from src.countries.spain.EroskiV3.model.product_content_eroski import ProductContentEroski
from src.utils.my_utils import (
    extract_file_name, extract_folder_path,
    get_files_with_substring_ordered_by_mtime,
    keep_text_after, remove_extra_dots,
    remove_keyword_if_first, remove_keywords_and_empty_texts,
    remove_substrings_and_clean, rephrase_text_if_parenthesis_exists,
    write_output_to_file
)
from src.countries.spain.EroskiV3.robots.static_data_V3 import get_static_aisles_from_user_cmdargs
from src.model.static_category_aisle import StaticAisle
from src.model.product_content import iA_keywords_to_remove

# --- API OpenAI ---
api_key = os.getenv('OPENAI_API_KEY')
print(f"api_key: {api_key}")
client = OpenAI(api_key=api_key)

# --- Cache IA ---
CACHE_FILE = "eroskiGPT_cache_ingredients.json"
def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

gpt_cache = load_cache()

# --- Nettoyage et post-traitements ---
def remove_parentheses(text: str) -> str:
    return re.sub(r'\([^)]*\)', '', text)

def clean_redundant(text: str) -> str:
    parts = [p.strip() for p in text.split(",")]
    seen = set()
    return ", ".join([p for p in parts if p and not (p in seen or seen.add(p))])

def clean_ingredients_list(ingredients: List[str]) -> List[str]:
    cleaned = []
    for ing in ingredients:
        ing = ing.strip().lower()
        ing = re.sub(r'\([^)]*\)', '', ing)
        ing = re.sub(r'[^a-záéíóúñüç ]+', '', ing)
        ing = ing.strip()
        if ing and ing not in cleaned and len(ing) > 2:
            cleaned.append(ing)
    return cleaned

def filter_garbage_ingredients(ingredients: List[str]) -> List[str]:
    return [
        ing for ing in ingredients
        if len(ing) > 2
        and not re.fullmatch(r"[a-z]{1,2}", ing)
        and "translated" not in ing
        and not re.match(r'^[a-z]$', ing)
    ]

def postprocess_ingredients_ia(ingredients: List[str]) -> List[str]:
    GARBAGE = {
        "", "s", "as", "b", "a", "c", "k",
        "result", "translated", "extracted", "base", "ingredient",
        "ingredients", "duplicates", "have been removed", "contains", "output",
        "a delicious task", "we get", "translated to english", "cleaned",
        "here are the base ingredient names in spanish"
    }

    GARBAGE_PHRASES = [
        "for any codes", "remove the letter codes", "and noningredient words",
        "codes eg", "no changes", "not an ingredient", "ignore", "note this",
        "step is not necessary", "commaseparated", "heres the updated list",
        "so its ignored", "this can be considered a processing step"
    ]

    VERB_TOKENS = ["remove", "kept", "left", "remain", "we ", "are ", "was ", "will "]

    def deduplicate_words_in_string(s: str) -> str:
        words = s.split()
        seen = set()
        return ' '.join([w for w in words if not (w in seen or seen.add(w))])

    cleaned = set()
    for ing in ingredients:
        ing = ing.strip().lower()

        # Supprimer parenthèses et crochets
        ing = re.sub(r"[\[\](){}]", "", ing)
        ing = re.sub(r"\s{2,}", " ", ing).strip()

        if ing in GARBAGE:
            continue

        if any(phrase in ing for phrase in GARBAGE_PHRASES):
            continue

        if any(v in ing for v in VERB_TOKENS):
            continue

        # Supprimer codes type "b1", "d3", etc.
        if re.match(r"^[a-z]{1,2}\d{1,2}$", ing):
            continue

        # Supprimer fragments trop courts non alphabétiques
        if len(ing) <= 2 and not ing.isalpha():
            continue

        # Supprimer lignes trop longues (trop explicatives)
        if len(ing.split()) > 4:
            continue

        ing = deduplicate_words_in_string(ing)
        cleaned.add(ing)

    return sorted(cleaned)


def expand_parenthesis_variants(text: str) -> str:
    pattern = re.compile(r'([^,()]+?)\s*\(([^)]+)\)')
    def repl(m):
        prefix = m.group(1).strip()
        parts = re.split(r',\s*| y\s*', m.group(2))
        return ', '.join(f"{prefix} {p.strip()}" for p in parts)
    prev = None
    while prev != text:
        prev = text
        text = re.sub(pattern, repl, text)
    return text

def flatten_square_brackets(text: str) -> str:
    """
    Aplati les crochets en gardant leur contenu avec une virgule séparée,
    sans supprimer ce qui est avant ou après.
    """
    return re.sub(r'\[([^\[\]]+)\]', r', \1', text)

def clean_ingredients(text: str, ingredients_clean_es: str = None) -> List[str]:
    if not text or not isinstance(text, str):
        return []
    if text in gpt_cache:
        return gpt_cache[text]

    prompt = (
        "You are a food science expert.\n"
        "Your task is to clean and translate a list of food ingredients written in Spanish.\n"
        "Follow these strict rules:\n"
        "1. Remove anything in parentheses or brackets (e.g., (contains milk), [G (Girasol)]).\n"
        "2. Extract only core ingredient names (e.g., remove codes like B1, D3 or generic words like 'ingredients', 'may contain').\n"
        "3. Translate the extracted ingredients to English (e.g., 'leche' becomes 'milk').\n"
        "4. Keep only food ingredient names — no steps, no comments, no explanations.\n"
        "5. Do not repeat any ingredient.\n"
        "6. Return only a clean comma-separated list of ingredient names, nothing else.\n"
        "7. Final output format example: milk, water, sugar, cornstarch, banana\n\n"
        f"Spanish ingredient list:\n{text}\n\n"
        "Cleaned and translated ingredients:"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a food science expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        
        content = response.choices[0].message.content
        print(f"💬 GPT-4o response:\n{content}")
        lines = content.replace("\u2022", "-").split("\n")
        raw = []

        # Motifs à ignorer (artefacts typiques des LLM)
        junk_patterns = [
            r"^so .*", r"^after .*", r"^remove .*", r"^none needed", r"^since .*",
            r"^we .*", r"^this .*", r"^from .*", r"^the .*", r"^milk fermented .*",
            r"^there .*", r"^not a .*", r"^i am .*", r"^kept .*", r"^as there .*",
            r"^so its .*", r"^leaving us .*", r"^step .*", r"^cleaned .*",
            r"^codes", r"^translated", r"^fermented is not .*", r"^protein",
            r"^based on .*", r".*noningredient.*", r"^commaseparated.*"
        ]

        for line in lines:
            line = line.strip("-• ").strip()
            if any(re.search(pattern, line.lower()) for pattern in junk_patterns):
                continue
            if "," in line:
                raw.extend([x.strip() for x in line.split(",") if x.strip()])
            elif re.match(r"^[A-Za-záéíóúñüç\s\-]{3,}$", line):
                raw.append(line)

        # Nettoyage & unicité
        result = list(dict.fromkeys([ing.strip().lower() for ing in raw if len(ing.strip()) > 2]))

        # Traductions manuelles connues
        manual_translations = {
            "espesante": "thickener",
            "almidón de maíz": "cornstarch",
            "almidón": "starch",
            "hidróxido potásico": "potassium hydroxide",
            "proteínas": "proteins",
            "fermentos lácteos": "lactic cultures",
            "leche": "milk",
            "agua": "water",
            "azúcar": "sugar"
        }
        result = [manual_translations.get(ing, ing) for ing in result]

        # Supprimer ceux déjà dans ingredients_clean_es
        if ingredients_clean_es:
            spanish = [tok.strip().lower() for tok in ingredients_clean_es.split(",")]
            result = [ing for ing in result if ing not in spanish]

        # Postprocessing
        result = postprocess_ingredients_ia(result)
        result = clean_ingredients_list(result)
        result = filter_garbage_ingredients(result)

        # Mise en cache
        gpt_cache[text] = result
        save_cache(gpt_cache)
        return result

    except Exception as e:
        print(f"⚠️ GPT-4o API error: {e}")
        return []

def process_product(product: dict) -> Product:
    """
    1. Convertit le dict JSON en dataclass Product (validation dacite).
    2. Parcourt chaque Evolution :
       - si ingredients_ia déjà présent, skip.
       - sinon, construit ingredients_clean et appel IA.
    3. Retourne le Product mis à jour.
    """
    product = dacite.from_dict(data_class=Product, data=product, config=dacite.Config(strict=True))
    evolsV2: List[Evolution] = []

    for evol in product.evolutions or []:
        if evol.ingredients_ia:
            evolsV2.append(evol)
            continue

        if evol.ingredients and len(evol.ingredients) > 2:
            # Pré-nettoyage texte brut
            ingredients = evol.ingredients.replace("\n", ",").strip().lower()
            ingredients = keep_text_after(ingredients, "ingredients:")
            ingredients = keep_text_after(ingredients, "ingredientes:")
            ingredients = remove_keyword_if_first(ingredients, ": ")
            ingredients = ingredients.replace("&", ", ").replace(" y", ",").strip()
            # 🔄 Étapes de nettoyage robustes
            ingredients = remove_substrings_and_clean(ingredients, substrings=ProductContentEroski.INGREDIENTS_SUBSTRINGS)
            ingredients = flatten_square_brackets(ingredients)
            ingredients = remove_parentheses(ingredients)
            ingredients = clean_redundant(ingredients)

            evol.ingredients_clean = remove_extra_dots(ingredients)

            # Appel IA et filtre final
            ingredients_ia = clean_ingredients(evol.ingredients_clean , ingredients_clean_es=evol.ingredients_clean)
            ingredients_ia = remove_keywords_and_empty_texts(ingredients_ia, iA_keywords_to_remove)
            evol.ingredients_ia = ingredients_ia

        evolsV2.append(evol)

    product.evolutions = evolsV2
    return product

if __name__ == "__main__":
    print("🟢 Lancement script IA GPT ingrédients")

    aisles: List[StaticAisle] = []
    cmdargs = sys.argv

    if len(cmdargs) > 1:
        user_input = cmdargs[1]

        # ✅ Si l'utilisateur passe un fichier JSON brut
        if os.path.isfile(user_input) and user_input.endswith(".json"):
            print(f"📄 Fichier unique fourni : {user_input}")
            aisles.append(StaticAisle(
                name=os.path.basename(user_input).replace(".json", ""),
                code="auto",
                original_file_uri=user_input,
                created_from_file=True
            ))

        # ✅ Si l'utilisateur passe un dossier
        elif os.path.isdir(user_input):
            print(f"📁 Dossier fourni : {user_input}")
            folder_to_use = user_input
        else:
            print("❌ Argument invalide. Spécifie un fichier .json ou un dossier valide.")
            sys.exit(1)
    else:
        folder_to_use = "src/countries/spain/EroskiV3/robots/products/"
        print("📁 Aucun argument fourni, utilisation du dossier par défaut.")

    # 📦 Si dossier utilisé, parcourir les fichiers récursivement
    if not aisles:
        all_json_files = glob.glob(os.path.join(folder_to_use, "**", "*.json"), recursive=True)
        raw_files = [
            f for f in all_json_files
            if (
                "_HFdetailed" not in f
                and "_Ollamadetailed" not in f
                and "_GPTdetailed" not in f
                and "_iAdetailed" not in f
                and re.search(r"_\d{2}_\d{2}_\d{2}", os.path.basename(f))  # ex: _25_07_26
            )
        ]

        files_by_base = {}
        for f in raw_files:
            filename = os.path.basename(f)
            base = filename.split(".json")[0].split("_25_")[0]
            if base not in files_by_base:
                files_by_base[base] = []
            files_by_base[base].append(f)

        for base, files in files_by_base.items():
            latest_file = max(files, key=os.path.getmtime)
            print(f"🕒 Dernière version de '{base}' détectée : {latest_file}")
            aisles.append(StaticAisle(
                name=os.path.basename(latest_file).replace(".json", ""),
                code="auto",
                original_file_uri=latest_file,
                created_from_file=True
            ))

    if not aisles:
        print("❌ Aucun fichier brut JSON valide détecté.")
        sys.exit()

    # --- Traitement IA de chaque fichier sélectionné ---
    for aisle in aisles:
        print(f"📂 Traitement fichier : {aisle.original_file_uri}")
        file = aisle.original_file_uri

        with open(file, encoding='utf-8') as f:
            products = json.load(f)

        productsV3: List[Product] = []
        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = [executor.submit(process_product, p) for p in products]
            for future in tqdm.tqdm(as_completed(futures), total=len(futures), desc=f"[{aisle.name}] Produits"):
                productsV3.append(future.result())

        print(f"🧪 {len(productsV3)} produits traités")

        base_name = os.path.basename(file).replace(".json", "")
        cleaned_file_path = os.path.join(os.path.dirname(file), f"{base_name}_GPTdetailed.json")
        print(f"💾 Sauvegarde vers : {cleaned_file_path}")

        json_object = json.dumps(
            productsV3,
            default=lambda o: {k: v for k, v in o.__dict__.items() if v is not None},
            indent=4,
            ensure_ascii=False
        )

        write_output_to_file(
            data=json_object,
            file_name=cleaned_file_path,
            path_includes_in_file_name=True,
            include_seconds_in_date=False,
            extension='.json'
        )
    # 🔒 Sauvegarde du cache
    print("💾 Sauvegarde du cache IA...")
    save_cache(gpt_cache)