#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import re
import unicodedata
from rapidfuzz import process, fuzz

# --- Constantes ---
CACHE_FILE = "title_to_ingredients_cache.json"
FUZZY_THRESHOLD = 75  # seuil de similarité (0-100)

# --- Normaliser un titre ---
def normalize_title(title: str) -> str:
    if not title:
        return ""
    title = title.lower().strip()
    title = ''.join(
        c for c in unicodedata.normalize('NFD', title)
        if unicodedata.category(c) != 'Mn'
    )
    title = re.sub(r'[^a-z0-9\s]', '', title)
    title = re.sub(r'\s+', ' ', title)
    return title

# --- Charger cache avec titres normalisés ---
def load_cache():
    if not os.path.exists(CACHE_FILE):
        print(f"⚠️ Cache introuvable : {CACHE_FILE}")
        return {}
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        raw = json.load(f)

    norm_cache = {}
    for k, v in raw.items():
        norm_cache[normalize_title(k)] = v
    return norm_cache

cache = load_cache()
cache_keys = list(cache.keys())

# --- Vérifier valeur vide ---
def is_empty(val):
    return val is None or val == "" or val == [] or val == {}

# --- Vérifier valeur illogique ---
def is_illogical(val):
    if not val:
        return True
    if isinstance(val, str):
        val = [val]

    bad_patterns = [
        r"\b\d+\s?(g|kg|mg|ml|cl|l|lt|liter|litre|liters)\b",
        r"\bpack\b", r"\bbox\b", r"\bbrick\b", r"\bweight\b",
        r"\bbottle\b", r"\bcan\b", r"\bjar\b", r"\bbag\b",
        r"\bbotella\b", r"\blata\b", r"\btarro\b", r"\bbolsa\b",
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

# --- Récupérer le titre (depuis lang_desc.es) ---
def get_best_title(prod: dict) -> str:
    if "lang_desc" in prod and isinstance(prod["lang_desc"], dict):
        es = prod["lang_desc"].get("es", {})
        if isinstance(es, dict) and es.get("title"):
            return es["title"]
    return ""

# --- Trouver correspondance (exact ou fuzzy) ---
def find_in_cache(title: str):
    norm_title = normalize_title(title)
    if norm_title in cache:
        return cache[norm_title]

    # fuzzy search si pas trouvé
    match, score, _ = process.extractOne(
        norm_title, cache_keys, scorer=fuzz.token_sort_ratio
    )
    if match and score >= FUZZY_THRESHOLD:
        print(f"🔎 Fuzzy match: '{title}' ≈ '{match}' (score {score})")
        return cache[match]

    return None

# --- Enrichir un produit ---
def enrich_product(prod, cache):
    changed = False
    title = get_best_title(prod).strip()
    if not title:
        return False

    cached = find_in_cache(title)
    if not cached:
        return False

    # ⚠️ evolutions est une liste
    evolutions = prod.get("evolutions", [])
    if not isinstance(evolutions, list) or not evolutions:
        return False

    evol = evolutions[0]  # on enrichit la première évolution

    # Vérifie et met à jour ingredients
    cur_ing = evol.get("ingredients")
    if (is_empty(cur_ing) or is_illogical(cur_ing)) and "ingredients" in cached:
        evol["ingredients"] = cached["ingredients"]
        changed = True

    # Vérifie et met à jour ingredients_clean
    cur_ing_clean = evol.get("ingredients_clean")
    if (is_empty(cur_ing_clean) or is_illogical(cur_ing_clean)) and "ingredients_clean" in cached:
        evol["ingredients_clean"] = cached["ingredients_clean"]
        changed = True

    # Vérifie et met à jour ingredients_ia
    cur_ing_ia = evol.get("ingredients_ia")
    if (is_empty(cur_ing_ia) or is_illogical(cur_ing_ia)) and "ingredients_ia" in cached:
        evol["ingredients_ia"] = cached["ingredients_ia"]
        changed = True

    if changed:
        print(f"✅ Enrichi: {title[:60]}...")

    prod["evolutions"][0] = evol
    return changed

# --- Traiter un fichier ---
def enrich_file(path, cache):
    changed = False
    with open(path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f"❌ Erreur JSON {path}: {e}")
            return False

    if isinstance(data, list):
        for p in data:
            if enrich_product(p, cache):
                changed = True
    elif isinstance(data, dict):
        if enrich_product(data, cache):
            changed = True

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    return changed

# --- Parcourir un dossier récursivement ---
def enrich_directory(directory, cache):
    updated_files = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json") and "iAdetailed" in file:
                path = os.path.join(root, file)
                if enrich_file(path, cache):
                    updated_files += 1
    return updated_files

# --- Main ---
def main():
    target = input("👉 Entrez le chemin d'un fichier ou dossier à traiter : ").strip()

    if os.path.isfile(target):
        if target.endswith(".json") and "iAdetailed" in target:
            if enrich_file(target, cache):
                print(f"✅ {target} mis à jour")
            else:
                print(f"ℹ️ Pas de mise à jour pour {target}")
        else:
            print(f"⏭️ Ignoré (pas un fichier iAdetailed) : {target}")

    elif os.path.isdir(target):
        updated_files = enrich_directory(target, cache)
        print(f"✅ {updated_files} fichiers iAdetailed mis à jour dans {target}")

    else:
        print(f"❌ Chemin introuvable: {target}")

if __name__ == "__main__":
    main()
