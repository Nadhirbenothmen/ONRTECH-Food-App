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

# Import Mongo loader
from src.countries.spain.EroskiV3.db.eroski_uploader import get_all_products_from_mongodb_by_category_with_ia_ingredient

# --- Cache IA ---
CACHE_FILE = "eroski_cache_ingredients.json"
def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

ingredients_cache = load_cache()

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
    cleaned = set()
    for ing in ingredients:
        ing = ing.strip().lower()
        if ing in GARBAGE or "extract" in ing or "duplicate" in ing:
            continue
        if len(ing) <= 1:
            continue
        cleaned.add(ing)
    return sorted(cleaned)


def clean_ingredients(text: str, ingredients_clean_es: str = None) -> List[str]:
    if not text or not isinstance(text, str):
        return []
    if text in ingredients_cache:
        return ingredients_cache[text]

    prompt = (
        "You are a food science expert. Given the following ingredient list in Spanish, perform the following steps:\n"
        "1. Ignore anything inside parentheses.\n"
        "2. Extract only base ingredient names.\n"
        "3. Translate them to English.\n"
        "4. For any codes in square brackets (e.g. [G (Girasol), N (Nabina)]), remove the letter codes but keep the full names in Spanish.\n"
        "5. Remove duplicates, vitamin codes (e.g., B1, D3), and non-ingredient words.\n"
        "Return a comma-separated list only of ingredient names — no explanations.\n"
        f"Ingredients: {text}\nCleaned and Translated Ingredients:"
    )
    try:
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        })
        content = response.json().get("response", "")
        # Parsing
        lines = content.replace("•", "-").split("\n")
        raw = []
        junk = ["a delicious task","here are","we get","translate","ignore","duplicate","cleaned","output"]
        for line in lines:
            line = line.strip("-• ").strip()
            if any(kw in line.lower() for kw in junk):
                continue
            if "," in line:
                raw.extend([x.strip() for x in line.split(",") if x.strip()])
            elif re.match(r"^[A-Za-záéíóúñüç\s\-]{3,}$", line):
                raw.append(line)

        result = clean_ingredients_list(raw)
        result = filter_garbage_ingredients(result)
        result = postprocess_ingredients_ia(result)
        if ingredients_clean_es:
            spanish = [tok.strip().lower() for tok in ingredients_clean_es.split(",")]
            result = [ing for ing in result if ing not in spanish]

        ingredients_cache[text] = result
        save_cache(ingredients_cache)
        return result
    except Exception as e:
        print(f"⚠️ LLM error: {e}")
        return []


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


def get_most_common_category_id(products: list) -> int:
    from collections import Counter
    cats = [c['id'] for p in products for c in p.get('categories', [])]
    return Counter(cats).most_common(1)[0][0]


if __name__ == "__main__":
    print("🚀 Lancement script IA ingrédients Eroski")
    cmdargs = sys.argv
    if len(cmdargs) < 2:
        print("❌ Usage: python eroski_ia.py <aisle_code|file|folder> [--by_category <id>] [--get_latest_parsed_products]")
        sys.exit(1)

    aisles: List[StaticAisle] = get_static_aisles_from_user_cmdargs(cmdargs=cmdargs)
    if not aisles:
        print("❌ Aucune allée trouvée.")
        sys.exit(1)

    mongo_products: List[Product] = []
    if "--by_category" in cmdargs:
        i = cmdargs.index("--by_category")
        try:
            cid = int(cmdargs[i+1])
            mongo_products = get_all_products_from_mongodb_by_category_with_ia_ingredient(category_id=cid)
        except:
            print("❌ --by_category doit être suivi d'un ID valide.")
            sys.exit(1)

    for aisle in aisles:
        print(f"📂 Allée : {aisle.name}")
        if not aisle.created_from_file:
            folder = extract_folder_path(aisle.original_file_uri)
            base = extract_file_name(aisle.original_file_uri)
            files = get_files_with_substring_ordered_by_mtime(folder, f"{base.lower()}_detailed")
            files = files[:1]
        else:
            files = [aisle.original_file_uri]

        if "--get_latest_parsed_products" in cmdargs:
            files = [files[0]]

        last_cat = None
        for file in files:
            print(f"  • Fichier : {file}")
            with open(file, encoding='utf-8') as f:
                raw_list = json.load(f)

            if not mongo_products:
                cat = get_most_common_category_id(raw_list)
                if cat != last_cat:
                    mongo_products = get_all_products_from_mongodb_by_category_with_ia_ingredient(category_id=cat)
                    last_cat = cat

            enriched: List[Product] = []
            existing_eans = {p.ean for p in mongo_products}
            for raw in raw_list:
                prod = dacite.from_dict(Product, raw, config=dacite.Config(strict=True))
                if prod.ean in existing_eans:
                    enriched.append(prod)
                    continue
                new_evols: List[Evolution] = []
                for evol in prod.evolutions or []:
                    if evol.ingredients and len(evol.ingredients) > 2:
                        txt = evol.ingredients.replace("\n", ",").strip().lower()
                        txt = keep_text_after(txt, "ingredients:")
                        txt = keep_text_after(txt, "ingredientes:")
                        txt = remove_keyword_if_first(txt, ": ")
                        txt = txt.replace("&", ", ").replace(" y", ",").strip()
                        txt = remove_substrings_and_clean(txt, ProductContentEroski.INGREDIENTS_SUBSTRINGS)
                        txt = rephrase_text_if_parenthesis_exists(txt)
                        txt = expand_parenthesis_variants(txt)
                        txt = remove_parentheses(txt)
                        txt = clean_redundant(txt)
                        evol.ingredients_clean = remove_extra_dots(txt)

                        ings = clean_ingredients(evol.ingredients_clean, evol.ingredients_clean)
                        evol.ingredients_ia = remove_keywords_and_empty_texts(ings, iA_keywords_to_remove)

                    new_evols.append(evol)
                prod.evolutions = new_evols
                enriched.append(prod)

            out = file.replace(".json", "_iAdetailed.json")
            json_str = json.dumps(
                enriched,
                default=lambda o: {k:v for k,v in o.__dict__.items() if v is not None},
                indent=4, ensure_ascii=False
            )
            write_output_to_file(
                data=json_str,
                file_name=out,
                path_includes_in_file_name=True,
                include_seconds_in_date=False,
                extension='.json'
            )
            print(f"  ✅ Sauvegardé : {out}")