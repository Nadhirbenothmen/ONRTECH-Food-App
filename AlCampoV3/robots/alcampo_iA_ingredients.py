import json
import sys
import os
import glob
import re
import dacite
import requests
import tqdm
from typing import List
from concurrent.futures import ThreadPoolExecutor, as_completed



# --- Imports internes pour le traitement des produits ---
sys.path.append('src')
sys.path.append('./')
from src.model.product import Evolution, Product
from src.countries.spain.AlCampoV3.model.product_content_alcampo import ProductContentAlcampo
from src.utils.my_utils import (
    keep_text_after, remove_extra_dots, remove_keyword_if_first,
    remove_keywords_and_empty_texts, remove_substrings_and_clean,
    rephrase_text_if_parenthesis_exists, write_output_to_file, 
)
from src.model.static_category_aisle import StaticAisle
from src.model.product_content import iA_keywords_to_remove

# --- Cache persistant des résultats IA pour éviter les appels répétitifs ---
CACHE_FILE = "alcampo_cache_ingredients.json"
def load_cache():
    """Charge le cache depuis disque (ou renvoie {} si pas de fichier)."""
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    """Sauvegarde le cache en JSON indenté pour la relecture."""
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

ingredients_cache = load_cache()


# --- Fonctions de nettoyage local avant ET après appel IA ---

def remove_parentheses(text: str) -> str:
    """Supprime tout ce qui est entre parenthèses."""
    return re.sub(r'\([^)]*\)', '', text)

def clean_redundant(text: str) -> str:
    """Enlève les doublons consécutifs après découpage par virgule."""
    parts = [p.strip() for p in text.split(",")]
    seen = set()
    return ", ".join([p for p in parts if p and not (p in seen or seen.add(p))])

def clean_ingredients_list(ingredients: List[str]) -> List[str]:
    """
    Standardise chaque ingrédient : 
    - minuscules, 
    - enlève parenthèses et caractères non-alfanumériques
    - filtre les chaînes trop courtes ou vides
    """
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
    """Supprime les restes non pertinents : codes, mots ultra courts, 'translated', etc."""
    return [
        ing for ing in ingredients
        if len(ing) > 2
        and not re.fullmatch(r"[a-z]{1,2}", ing)
        and "translated" not in ing
        and not re.match(r'^[a-z]$', ing)
    ]

def postprocess_ingredients_ia(ingredients: List[str]) -> List[str]:
    """
    Filtre final : 
    - retire les termes explicitement listés dans GARBAGE
    - retire les occurrences de 'extract' et 'duplicate'
    - renvoie trié
    """
    GARBAGE = {
        "", "s", "as", "b", "a", "c", "k",
        "result", "translated", "extracted", "base", "ingredient",
        "ingredients", "duplicates", "have been removed", "contains", "output",
        "a delicious task", "we get", "translated to english", "cleaned",
        "here are the base ingredient names in spanish"
    }

    cleaned = set()
    for ing in ingredients:
        ing = ing.strip().lower()
        ing = re.sub(r"[^a-z\u00e1\u00e9\u00ed\u00f3\u00fa\u00f1\u00fc\u00e7 -]", "", ing)

        if ing in GARBAGE or "extract" in ing or "duplicate" in ing:
            continue
        cleaned.add(ing)

    return sorted(cleaned)


# --- Fonction principale d’appel IA et parsing de la réponse ---

def clean_ingredients(text, ingredients_clean_es=None):
    if not text or not isinstance(text, str):
        return []
    if text in ingredients_cache:
        return ingredients_cache[text]

    prompt = (
        "You are a food science expert. "
        "Given the following ingredient list in Spanish, perform the following steps:\n"
        "1. Ignore anything inside parentheses.\n"
        "2. Extract only base ingredient names.\n"
        "3. Translate them to English.\n"
        "4. Remove duplicates, vitamin codes (e.g., B1, D3), and non-ingredient words.\n"
        "Return a **comma-separated list only** of ingredient names — no explanations, no titles, no headers.\n"
        f"Ingredients: {text}\n\n"
        "Cleaned and Translated Ingredients:"
    )

    try:
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        })
        content = response.json().get("response", "")
        print(f"💬 IA Response:\n{content}")  # DEBUG

        # 1) Split lines & strip
        lines = content.replace("•", "-").replace("*", "-").split("\n")
        raw = []

        # 2) Nouvelle liste de junk phrases
        junk_phrases = [
            "a delicious task", "here are", "we get",
            "translate", "ignore", "duplicate",
            "cleaned", "output", "moved", "nothing",
            "based on", "perform", "specified", "steps"
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

        # 3) Nettoyages existants
        result = clean_ingredients_list(raw)
        result = filter_garbage_ingredients(result)
        result = postprocess_ingredients_ia(result)

        # 4) Filtrer les tokens espagnols s’ils sont passés
        if ingredients_clean_es:
            spanish_tokens = [tok.strip().lower() for tok in ingredients_clean_es.split(",")]
            result = [ing for ing in result if ing.lower() not in spanish_tokens]

        # 5) Cache + retour
        ingredients_cache[text] = result
        save_cache(ingredients_cache)
        return result

    except Exception as e:
        print(f"\u26a0\ufe0f LLM error: {e}")
        return []



# --- Fonction de transformation d’un produit complet --- 

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
            ingredients = remove_substrings_and_clean(ingredients, substrings=ProductContentAlcampo.INGREDIENTS_SUBSTRINGS)
            ingredients = rephrase_text_if_parenthesis_exists(ingredients)
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



# --- Script principal ---
if __name__ == "__main__":
    print("\U0001F7E2 Lancement script IA ingrédients")
    cmdargs = sys.argv
    aisles: List[StaticAisle] = []

    for arg in cmdargs[1:]:
        if os.path.isdir(arg):
            # Parcours récursif de tous les .json
            json_files = glob.glob(os.path.join(arg, "**", "*.json"), recursive=True)
            for file in json_files:
                aisles.append(StaticAisle(
                    name=os.path.basename(file).replace(".json", ""),
                    code="auto",
                    original_file_uri=file,
                    created_from_file=True
                ))
        elif arg.endswith(".json") and os.path.isfile(arg):
            aisles.append(StaticAisle(
                name=os.path.basename(arg).replace(".json", ""),
                code="manual",
                original_file_uri=arg,
                created_from_file=True
            ))

    if not aisles:
        print("\u274c Aucun fichier JSON valide ou dossier fourni.")
        sys.exit()

    for aisle in aisles:
        print(f"\U0001F4C2 Traitement fichier : {aisle.original_file_uri}")
        file = aisle.original_file_uri

        with open(file, encoding='utf-8') as f:
            products = json.load(f)

        productsV2: List[Product] = []
        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = [executor.submit(process_product, p) for p in products]
            for future in tqdm(as_completed(futures), total=len(futures), desc=f"[{aisle.name}] Produits"):
                productsV2.append(future.result())

        print(f"\U0001F9EA {len(productsV2)} produits traités")
        cleaned_file_path = file.replace(".json", "_iAdetailed.json")
        print(f"\U0001F4BE Sauvegarde vers : {cleaned_file_path}")

        json_object = json.dumps(
            productsV2,
            default=lambda o: {k: v for k, v in o.__dict__.items() if v is not None},
            indent=4,
            ensure_ascii=False
        )

        write_output_to_file(
            data=json_object,
            file_name=os.path.join(os.path.dirname(file), os.path.basename(cleaned_file_path)),
            path_includes_in_file_name=True,
            include_seconds_in_date=False,
            extension='.json'
        )
    else:
        print("wrong args number")
        sys.exit()