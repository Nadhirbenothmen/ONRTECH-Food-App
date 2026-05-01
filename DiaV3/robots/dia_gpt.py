from concurrent.futures import ThreadPoolExecutor, as_completed
import glob
import json
import sys
import os
import re
from typing import List
import dacite
import tqdm

from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

sys.path.append('src')
sys.path.append('./')

from src.model.product import Evolution, Product
from src.countries.spain.DiaV3.model.product_content_dia import ProductContentDia
from src.utils.my_utils import (
    extract_file_name, extract_folder_path, get_files_with_substring_ordered_by_mtime,
    keep_text_after, remove_extra_dots, remove_keyword_if_first,
    remove_keywords_and_empty_texts, remove_substrings_and_clean,
    rephrase_text_if_parenthesis_exists, write_output_to_file
)
from src.countries.spain.DiaV3.robots.static_data_V3 import get_static_aisles_from_user_cmdargs
from src.model.static_category_aisle import StaticAisle
from src.model.product_content import iA_keywords_to_remove

# --- API OpenAI ---
api_key = os.getenv('OPENAI_API_KEY')
print(f"api_key: {api_key}")
client = OpenAI(api_key=api_key)

# --- Système de cache IA ---
CACHE_FILE = "diaGPT_cache_ingredients.json"

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_cache(cache: dict):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=4)

gpt_cache = load_cache()


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

def clean_ingredients_for_analysis(raw_text: str) -> str:
    """
    Nettoie un champ 'ingredients' pour analyse :
    - Supprime parenthèses, crochets et leur contenu
    - Retire les additifs, stabilisants, mots techniques
    - Supprime les expressions comme 'a partir de', 'sin gluten', etc.
    - Garde seulement les ingrédients de base, séparés par virgule
    """
    if not isinstance(raw_text, str):
        return ""

    text = raw_text.lower()

    # 1. Supprimer tout ce qui est entre (), [] ou {}
    text = re.sub(r"\([^)]*\)", "", text)
    text = re.sub(r"\[[^]]*\]", "", text)
    text = re.sub(r"\{[^}]*\}", "", text)

    # 2. Supprimer les mots techniques ou inutiles
    garbage_keywords = [
        r"emulgente[s]?", r"estabilizante[s]?", r"vitaminas?", r"sales minerales?",
        r"aromas?", r"lecitina[s]?", r"colorante[s]?", r"antioxidante[s]?", r"acidulante[s]?",
        r"espesante[s]?", r"edulcorante[s]?", r"corrector(?:es)? de acidez",
        r"e-\d+", r"e\d+", r"aditivos?", r"conservante[s]?", r"traz(?:as)? de", r"puede contener"
    ]
    for kw in garbage_keywords:
        text = re.sub(rf"\b{kw}\b", "", text)

    # ✅ 3. Supprimer les expressions explicatives non utiles
    explanatory_phrases = [
        r"\ba partir de\b",
        r"\ben proporción variable\b",
        r"\bsin gluten\b",
        r"\bsin azúcares? añadidos?\b",
        r"\bde origen ecológico\b",
        r"\bprocedente[s]? de\b",
        r"\bconcentrado\b",
        r"\badaptado a las necesidades.*?\b",
        r"\bsin.*?\b"
    ]
    for phrase in explanatory_phrases:
        text = re.sub(phrase, "", text)

    # 4. Nettoyage ponctuation → remplacer & ou " y " par virgule
    text = text.replace("&", ",").replace(" y ", ",").replace(";", ",").replace(":", ",")

    # 5. Supprimer parenthèses restantes accidentelles
    text = text.replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "")

    # 6. Séparer et nettoyer
    parts = [p.strip() for p in text.split(",") if p.strip() and len(p.strip()) > 2]

    # 7. Supprimer doublons
    seen = set()
    unique_parts = []
    for p in parts:
        if p not in seen:
            unique_parts.append(p)
            seen.add(p)

    result = ", ".join(unique_parts)

    # ✅ Correction manuelle spécifique
    result = result.replace("proteínas de suero leche", "proteínas de suero de leche")

    return result


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

    # ✅ Corrections spécifiques connues d'erreurs fréquentes d'IA
    corrections = {
        "-fucosyllactose": "2'-fucosyllactose",
        "-tocopherol": "alpha-tocopherol",
        "-caseinate": "sodium caseinate",
        "-carotene": "beta-carotene",
        "-palmitate": "vitamin a palmitate",
        "‘": "'", "’": "'", "“": '"', "”": '"'
    }

    cleaned = set()

    for ing in ingredients:
        ing = ing.strip().lower()

        # ✅ Appliquer toutes les corrections connues
        for wrong, right in corrections.items():
            ing = ing.replace(wrong, right)

        # ✅ Nettoyage caractères autorisés
        ing = re.sub(r"[^a-z\u00e1\u00e9\u00ed\u00f3\u00fa\u00f1\u00fc\u00e7 \-']", "", ing)

        # ✅ Supprimer les guillemets simples en trop autour
        ing = ing.strip("'").strip('"')

        # ✅ Filtrage final
        if ing in GARBAGE or "extract" in ing or "duplicate" in ing:
            continue

        cleaned.add(ing)

    return sorted(cleaned)


def clean_ingredients(text, ingredients_clean_es=None):
    if not text or not isinstance(text, str):
        return []

    text_key = text.strip().lower()
    if text_key in gpt_cache:
        print("✅ Résultat récupéré depuis le cache.")
        return gpt_cache[text_key]

    prompt = (
        "You are a food science expert. "
        "Given the following ingredient list in Spanish, perform the following steps:\n"
        "1. Ignore anything inside parentheses.\n"
        "2. Extract only base ingredient names.\n"
        "3. Translate them to English.\n"
        "4. For any codes in square brackets (e.g. [G (Girasol), N (Nabina)]), remove the letter codes but keep the full names in Spanish.\n"
        "5. Remove duplicates, vitamin codes (e.g., B1, D3), and non-ingredient words.\n"
        "Return a **comma-separated list only** of ingredient names — no explanations, no titles, no headers.\n"
        f"Ingredients: {text}\n\n"
        "Cleaned and Translated Ingredients:"
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

        lines = content.replace("•", "-").replace("*", "-").split("\n")
        raw = []

        junk_phrases = [
            "a delicious task", "here are", "we get", "translate", "ignore", "duplicate",
            "cleaned", "output", "moved", "nothing", "based on", "perform", "specified", "steps"
        ]

        for line in lines:
            line = line.strip("-• ").strip()
            low = line.lower()
            if any(kw in low for kw in junk_phrases):
                continue
            if "," in line:
                raw.extend([x.strip() for x in line.split(",") if x.strip()])
            elif re.match(r"^[A-Za-záéíóúñüç\s\-]{3,}$", line):
                raw.append(line)

        result = clean_ingredients_list(raw)
        raw_string = ", ".join(raw)
        result = clean_ingredients_for_analysis(raw_string).split(", ")
        result = filter_garbage_ingredients(result)
        result = postprocess_ingredients_ia(result)

        if ingredients_clean_es:
            spanish_tokens = [tok.strip().lower() for tok in ingredients_clean_es.split(",")]
            result = [ing for ing in result if ing.lower() not in spanish_tokens]

        gpt_cache[text_key] = result
        return result

    except Exception as e:
        print(f"⚠️ GPT-4o API error: {e}")
        return []

def process_product(product: dict) -> Product:
    product = dacite.from_dict(data_class=Product, data=product, config=dacite.Config(strict=True))
    if product.evolutions is None:
        product.evolutions = []

    evolsV2: List[Evolution] = []

    for evol in product.evolutions:
        if evol.ingredients and len(evol.ingredients) > 2:
            print(f"ean without ia_ingredients: {product.ean}")
            ingredients = evol.ingredients
            ingredients = ingredients.replace("&", ", ").replace(" y", ",").strip()
            ingredients = remove_substrings_and_clean(ingredients, substrings=ProductContentDia.INGREDIENTS_SUBSTRINGS)
            ingredients = rephrase_text_if_parenthesis_exists(ingredients)
            evol.ingredients_clean = clean_ingredients_for_analysis(evol.ingredients)


            ingredients_ia = clean_ingredients(evol.ingredients_clean)
            ingredients_ia = remove_keywords_and_empty_texts(texts=ingredients_ia, keywords=iA_keywords_to_remove) if ingredients_ia else None
            evol.ingredients_ia = ingredients_ia

            print(f"[DEBUG] {product.ean} - ingredients_clean: {evol.ingredients_clean}")
            print(f"[DEBUG] {product.ean} - ingredients_ia: {evol.ingredients_ia}")

        evolsV2.append(evol)

    product.evolutions = evolsV2
    return product


# --- Script principal ---
if __name__ == "__main__":
    print("🟢 Lancement script IA GPT ingrédients")
    aisles: List[StaticAisle] = []
    cmdargs = sys.argv

    if len(cmdargs) > 1:
        user_input = cmdargs[1]
        if os.path.isfile(user_input) and user_input.endswith(".json"):
            print(f"📄 Fichier unique fourni : {user_input}")
            aisles.append(StaticAisle(
                name=os.path.basename(user_input).replace(".json", ""),
                code="auto",
                original_file_uri=user_input,
                created_from_file=True
            ))
        elif os.path.isdir(user_input):
            print(f"📁 Dossier fourni : {user_input}")
            folder_to_use = user_input
        else:
            print("❌ Argument invalide.")
            sys.exit(1)
    else:
        folder_to_use = "src/countries/spain/DiaV3/robots/products/"
        print("📁 Aucun argument fourni, dossier par défaut.")

    if not aisles:
        all_json_files = glob.glob(os.path.join(folder_to_use, "**", "*.json"), recursive=True)
        raw_files = [f for f in all_json_files if "_HFdetailed" not in f and "_Ollamadetailed" not in f and "_GPTdetailed" not in f and "_iAdetailed" not in f]
        files_by_base = {}
        for f in raw_files:
            filename = os.path.basename(f)
            base = filename.split(".json")[0].split("_25_")[0]
            files_by_base.setdefault(base, []).append(f)
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
        print("❌ Aucun fichier détecté.")
        sys.exit()

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

        base_name = os.path.basename(file).replace(".json", "")
        cleaned_file_path = os.path.join(os.path.dirname(file), f"{base_name}_iAdetailed.json")
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
