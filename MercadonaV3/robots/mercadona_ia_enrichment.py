#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import time
import re
from datetime import datetime, timezone
import copy
import requests
import json5
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import urllib.parse
from collections import OrderedDict
from deep_translator import GoogleTranslator

IAD_FILE_PAT = re.compile(
    r'^(?P<root>.+?\.json)'                       # ex: Baby_food.json
    r'(?:_(?P<rawts>\d{2}(?:_\d{2}){4}|\d{4}(?:_\d{2}){4}))?'  # timestamp “brut” optionnel
    r'_iAdetailed'
    r'(?:_(?P<iadts>\d{4}(?:_\d{2}){4}|\d{2}(?:_\d{2}){4}))?'  # timestamp final optionnel
    r'\.json$', re.I
)

def _parse_root_and_ts(fname: str):
    m = IAD_FILE_PAT.match(fname)
    if not m:
        return None, None
    root  = m.group("root")
    iadts = m.group("iadts")
    dt = None
    if iadts:
        for fmt in ("%Y_%m_%d_%H_%M", "%y_%m_%d_%H_%M"):
            try:
                dt = datetime.strptime(iadts, fmt)
                break
            except:
                pass
    return root, dt

# --- CONSTANTES ---
OLLAMA_URL     = "http://localhost:11434/api/generate"
OFF_SEARCH_URL = "https://world.openfoodfacts.org/cgi/search.pl"
CACHE_FILE     = "mercadona_cache_enrichment.json"
MAX_IA_TRIES   = 3

# --- GESTION DE CACHE ---
def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=4)

enrichment_cache = load_cache()

# --- UTILES ---
def clean_units(text):
    if not isinstance(text, str):
        return text
    return re.sub(r"(\d+)\s?(mg|g|IU|%)", r"\1", text)

def normalize_nutrition(raw):
    return OrderedDict([
        ("energies", OrderedDict([("kj", float(raw.get("kj", 0))), ("kcal", float(raw.get("kcal", 0)))])),
        ("minerals", OrderedDict([("salt", float(raw.get("salt", 0)))])),
        ("fats",     OrderedDict([("fats", float(raw.get("lípidos", 0))), ("saturates", float(raw.get("grasas_saturadas", 0)))])),
        ("proteins", OrderedDict([("proteins", float(raw.get("proteínas", 0)))])),
        ("carbohydrates", OrderedDict([("carbohydrates", float(raw.get("glucidos", 0))), ("of_which_sugars", float(raw.get("azúcares", 0)))]))
    ])

def fetch_nutrition_off(query, weight_g):
    params = {"search_terms": query, "search_simple": 1, "action": "process", "json": 1}
    try:
        resp = requests.get(OFF_SEARCH_URL, params=params, timeout=30)
        resp.raise_for_status()
    except:
        return {}
    data = resp.json()
    if not data.get("products"):
        return {}
    prod = data["products"][0]
    nutr = prod.get("nutriments", {})
    factor = weight_g / 100.0
    return {
        "kj": nutr.get("energy-kj_100g", 0)*factor,
        "kcal": nutr.get("energy-kcal_100g", 0)*factor,
        "proteínas": nutr.get("proteins_100g", 0)*factor,
        "glucidos": nutr.get("carbohydrates_100g", 0)*factor,
        "azúcares": nutr.get("sugars_100g", 0)*factor,
        "lípidos": nutr.get("fat_100g", 0)*factor,
        "grasas_saturadas": nutr.get("saturated-fat_100g", 0)*factor,
        "salt": nutr.get("salt_100g", 0)*factor,
     
        "nutriscore": prod.get("nutriscore_grade","").upper()
    }
def fetch_ingredients_off(title):
    """
    Recherche le premier produit OFF correspondant à 'title'
    et renvoie un dict { ingredients, ingredients_clean, ingredients_ia }
    ou None si introuvable.
    """
    params = {
        "search_terms": title,
        "search_simple": 1,
        "action": "process",
        "json": 1,
        "fields": "ingredients_text,ingredients_text_en"
    }
    try:
        resp = requests.get(OFF_SEARCH_URL, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
    except:
        return None

    prods = data.get("products") or []
    if not prods:
        return None

    prod = prods[0]
    # ON PREND LE TEXTE BRUT D'INGRÉDIENTS
    ingr_es = prod.get("ingredients_text", "")   
    ingr_en = prod.get("ingredients_text_en", "") 

    # Nettoyage minimal : on sépare par virgule
    if ingr_en:
        items = [i.strip() for i in ingr_en.split(",") if i.strip()]
    else:
        items = [i.strip() for i in ingr_es.split(",") if i.strip()]

    return {
        "ingredients": ingr_es or ingr_en,
        "ingredients_clean": (ingr_en or ingr_es),
        "ingredients_ia": items
    }


# --- ENRICHISSEMENT IA ---
def enrich_title_with_ollama(title, ingredients, weight,
                             models=("mistral", "llama3"),
                             retries=3):
    cache_key = f"{title.strip().lower()}|{weight}"
    if cache_key in enrichment_cache:
        return enrichment_cache[cache_key]

    prompt = f"""
Dado el título del producto: "{title}", genera un objeto JSON con:
{{
  "ingredients": string,
  "ingredients_clean": string,
  "ingredients_ia": lista[string]
}}
Solo responde con el JSON.
""".strip()

    for model in models:
        for _ in range(retries):
            try:
                resp = requests.post(OLLAMA_URL, json={
                    "model": model,
                    "prompt": prompt,
                    "stream": False,
                    "options": {"temperature": 0.3, "num_predict": 300}
                }, timeout=60)
                resp.raise_for_status()
                text = resp.json().get("response", "").strip()
                if "{" in text:
                    frag = text[text.find("{"):text.rfind("}")+1]
                    try:
                        out = json.loads(frag)
                    except:
                        out = json5.loads(frag)
                    if out.get("ingredients") and isinstance(out.get("ingredients_ia"), list):
                        enrichment_cache[cache_key] = out
                        save_cache(enrichment_cache)
                        return out
            except:
                time.sleep(1)

    # Aucun modèle n'a renvoyé un JSON exploitable
    return None


def extract_title_from_url(url):
    if not url: return None
    parts = urllib.parse.urlparse(url).path.strip("/").split("/")
    return parts[-1].replace("-", " ").capitalize()

def needs_ing(prod):
    evo = prod.get("evolutions",[{}])[0]
    ing = evo.get("ingredients","")
    clean = evo.get("ingredients_clean","")
    ia = evo.get("ingredients_ia",[])
    return not (ing and clean and isinstance(ia,list) and any(x.strip() for x in ia))

# --- ENRICHISSEMENT PRODUIT ---
def enrich_product(prod):
    p   = copy.deepcopy(prod)
    evo = p.setdefault("evolutions", [{}])[0]

    # récupération du titre
    title = (
        evo.get("format")
        or extract_title_from_url(prod.get("lang_desc", {})
                                  .get("es", {})
                                  .get("links", {})
                                  .get("links_self", ""))
    )
    if not title:
        return p

    if needs_ing(prod):
        # 1) tentative IA
        enriched = enrich_title_with_ollama(
            title,
            evo.get("ingredients", ""),
            evo.get("weight_per_packaging", 100)
        )

        if enriched:
            evo["ingredients"]       = enriched["ingredients"]
            evo["ingredients_clean"] = enriched["ingredients_clean"]
            evo["ingredients_ia"]    = enriched["ingredients_ia"]
        else:
            # 2) fallback OFF
            off_ing = fetch_ingredients_off(title)
            if off_ing:
                evo["ingredients"]       = off_ing["ingredients"]
                evo["ingredients_clean"] = off_ing["ingredients_clean"]
                evo["ingredients_ia"]    = off_ing["ingredients_ia"]
            else:
                print(f"⚠️ Aucun ingrédient trouvé pour « {title} »")

    return p



# --- TRAITEMENT FICHIERS / RÉPERTOIRES ---
def process_file(path):
    # 1) Chargement
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    prods = data if isinstance(data, list) else [data]

    # 2) Enrichissement
    enriched_count = 0
    results = []
    for prod in tqdm(prods, desc=os.path.basename(path)):
        if needs_ing(prod):
            new = enrich_product(prod)
            enriched_count += 1
        else:
            new = prod
        results.append(new)

    # 3) Réécriture du contenu
    out = results if isinstance(data, list) else results[0]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=4)

    # 4) Renommage du fichier : on remplace le dernier timestamp par celui du run
    dirn, orig_fn = os.path.split(path)
    now = datetime.now().strftime("%y_%m_%d_%H_%M")
    # trouve le dernier motif 00_00_00_00_00 avant .json et remplace
    new_fn = re.sub(
        r"(\d{2}_\d{2}_\d{2}_\d{2}_\d{2})(?=\.json$)",
        now,
        orig_fn
    )
    new_path = os.path.join(dirn, new_fn)
    os.replace(path, new_path)

    # 5) Retourne enrichis et total
    return enriched_count, len(prods)

def main():
    root = sys.argv[1] if len(sys.argv) > 1 else input("Dossier iAdetailed: ").strip()
    total_enriched = 0
    total_scanned  = 0

    latest_by_root = {}  # root.json -> (has_ts:int, dt:datetime, full_path)
    for dirpath, _, files in os.walk(root):
        for fn in files:
            low = fn.lower()
            if not (low.endswith(".json") and "iadetailed" in low):
                continue
            base, dt = _parse_root_and_ts(fn)
            if not base:
                continue
            full = os.path.join(dirpath, fn)
            has_ts = 1 if dt is not None else 0
            if dt is None:
                dt = datetime.fromtimestamp(os.path.getmtime(full))  # fallback mtime
            if base not in latest_by_root or (has_ts, dt) > latest_by_root[base][:2]:
                latest_by_root[base] = (has_ts, dt, full)

    # Traiter uniquement le plus récent par base
    for _, (_, _, full) in latest_by_root.items():
        enriched_count, count = process_file(full)
        total_enriched += enriched_count
        total_scanned  += count
    print(
        "\n=== RÉSUMÉ ===\n"
        f"Produits totaux  : {total_scanned}\n"
        f"Produits enrichis: {total_enriched}\n"    )

if __name__ == "__main__":
    main()


