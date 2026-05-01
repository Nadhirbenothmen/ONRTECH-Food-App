#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Prédit ingredients (espagnol), ingredients_clean (espagnol) et
ingredients_ia (liste en anglais) à partir du title (via Ollama local).
Avec système de cache, détection des champs illogiques et post-traitement robuste.
Gère plusieurs fichiers INPUT (ex: missing_ingredients_ia_v2.json +
products_with_ingredients_ia_as_format.json).
"""

import os
import sys
import json
import re
import requests
from tqdm import tqdm

# --- CONFIG ---
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"   # ou "mistral"

# Permet de passer les fichiers en argument
INPUT_FILES = sys.argv[1:] if len(sys.argv) > 1 else [
    "products_with_ingredients_ia.json",
    "products_missing_ingredients_ia.json",
    "products_with_illogical_ingredients.json"
]

OUTPUT_FILE = "missing_ingredients_predicted_dia.json"
CACHE_FILE = "title_to_ingredients_cache_dia.json"

PROMPT_TEMPLATE = """
Eres un experto en nutrición.
A partir del título del producto, predice sus ingredientes:

1. "ingredients" → versión bruta en ESPAÑOL (como en el envase).
2. "ingredients_clean" → versión limpia y simplificada en ESPAÑOL.
3. "ingredients_ia" → lista en INGLÉS (cada ingrediente separado en una lista JSON).

Responde SOLO en JSON estricto, sin texto adicional.
Ejemplo:
{{
  "ingredients": "Leche entera, fermentos lácticos",
  "ingredients_clean": "Leche entera, fermentos",
  "ingredients_ia": ["Whole milk", "Lactic ferments"]
}}

Título del producto: "{title}"
"""

# --- GESTION DE CACHE ---
def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=4)
    print(f"💾 Cache sauvegardé ({len(cache)} titres) → {CACHE_FILE}")

# --- UTILS ---
def try_json_load(value):
    if isinstance(value, str) and value.strip().startswith("{"):
        try:
            return json.loads(value)
        except:
            return value
    return value

def is_missing_ingredients_ia(val) -> bool:
    if not val:
        return True
    if isinstance(val, str) and not val.strip():
        return True
    if isinstance(val, list) and all((not x or str(x).strip().lower() in {"", "null", "none"}) for x in val):
        return True
    return False

def is_illogical_ingredients(val) -> bool:
    if not val:
        return True
    if isinstance(val, str):
        val = [val]

    bad_patterns = [
        # unités
        r"\b\d+\s?(g|kg|mg|ml|cl|l|lt|liter|litre|liters)\b",
        # formats FR/ES
        r"\bpack\b", r"\bbotella\b", r"\blata\b", r"\btarro\b", r"\bbolsa\b",
        # formats EN
        r"\bbox\b", r"\bbrick\b", r"\bweight\b", r"\bbottle\b", r"\bcan\b", r"\bjar\b", r"\bbag\b",
        # multi x
        r"\b\d+x\b"
    ]

    for ing in val:
        ing_low = str(ing).lower()
        if len(ing_low) <= 2:
            return True
        for pat in bad_patterns:
            if re.search(pat, ing_low):
                return True
    return False

# --- POST-TRAITEMENT ---
def clean_prediction(pred: dict) -> dict:
    if isinstance(pred, str):
        pred = try_json_load(pred)
        if isinstance(pred, str):
            return {
                "ingredients": pred,
                "ingredients_clean": pred,
                "ingredients_ia": [pred]
            }
    ingredients = try_json_load(pred.get("ingredients", ""))
    ingredients_clean = try_json_load(pred.get("ingredients_clean", ""))
    ingredients_ia = try_json_load(pred.get("ingredients_ia", []))

    if not isinstance(ingredients, str):
        ingredients = str(ingredients)
    if not isinstance(ingredients_clean, str):
        ingredients_clean = str(ingredients_clean)
    if isinstance(ingredients_ia, str):
        ingredients_ia = [i.strip() for i in ingredients_ia.split(",") if i.strip()]
    if not isinstance(ingredients_ia, list):
        ingredients_ia = [str(ingredients_ia)]

    cleaned_ia = []
    seen = set()
    ignore_words = {"additives", "vitamins", "minerals", "preservatives"}
    for ing in ingredients_ia:
        ing = ing.strip()
        if not ing:
            continue
        key = ing.lower()
        if key in seen:
            continue
        seen.add(key)
        if any(w in key for w in ignore_words):
            continue
        ing = ing[0].upper() + ing[1:] if len(ing) > 1 else ing.upper()
        cleaned_ia.append(ing)

    return {
        "ingredients": ingredients.strip(),
        "ingredients_clean": ingredients_clean.strip(),
        "ingredients_ia": cleaned_ia
    }

# --- IA ---
def query_ollama(title: str) -> dict:
    prompt = PROMPT_TEMPLATE.format(title=title)
    resp = requests.post(OLLAMA_URL, json={"model": MODEL, "prompt": prompt}, stream=True)
    resp.raise_for_status()
    text = ""
    for line in resp.iter_lines():
        if not line:
            continue
        try:
            data = json.loads(line.decode("utf-8"))
            text += data.get("response", "")
        except:
            continue
    text = text.strip()
    try:
        parsed = json.loads(text)
    except:
        parsed = {"ingredients": text, "ingredients_clean": text, "ingredients_ia": [text]}
    return clean_prediction(parsed)

# --- MAIN ---
def main():
    cache = load_cache()

    # Fusionne tous les produits des INPUT_FILES
    products = []
    from_as_format = 0
    for fpath in INPUT_FILES:
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    products.extend(data)
                    if "products_with_ingredients_ia_as_format" in fpath:
                        from_as_format += len(data)
                except Exception as e:
                    print(f"⚠️ Erreur lecture {fpath} : {e}")

    count_recalc = 0
    count_cache = 0
    count_skip = 0

    enriched = []
    for p in tqdm(products, desc="Prediction IA"):
        title = p.get("title", "").strip()
        ingredients_ia = p.get("ingredients_ia")

        if (is_missing_ingredients_ia(ingredients_ia) or is_illogical_ingredients(ingredients_ia)) and title:
            if title in cache and not is_illogical_ingredients(ingredients_ia):
                prediction = cache[title]
                status = "cache"
                count_cache += 1
            else:
                prediction = query_ollama(title)
                cache[title] = prediction
                save_cache(cache)
                status = "IA recalculée"
                count_recalc += 1
            enriched.append({
                "ean": p.get("ean"),
                "title": p.get("title"),
                "ingredients": prediction.get("ingredients"),
                "ingredients_clean": prediction.get("ingredients_clean"),
                "ingredients_ia": prediction.get("ingredients_ia"),
            })
            print(f"🔄 {title[:40]}... → {status}")
        else:
            enriched.append({
                "ean": p.get("ean"),
                "title": p.get("title"),
                "ingredients": p.get("ingredients"),
                "ingredients_clean": p.get("ingredients_clean"),
                "ingredients_ia": p.get("ingredients_ia"),
            })
            count_skip += 1
            print(f"⏩ {title[:40]}... → skip (déjà correct)")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(enriched, f, ensure_ascii=False, indent=4)

    print(f"✅ Fichier généré : {OUTPUT_FILE}")
    save_cache(cache)

    # --- Résumé final ---
    uniques = len({p.get("title", "").strip() for p in products})
    print("\nRésumé :")
    print(f"- {uniques} produits uniques")
    print(f"- dont {from_as_format} venaient de products_with_ingredients_ia_as_format.json")
    print(f"- {count_recalc} recalculés IA")
    print(f"- {count_cache} pris du cache")
    print(f"- {count_skip} skip (corrects)")

if __name__ == "__main__":
    main()
