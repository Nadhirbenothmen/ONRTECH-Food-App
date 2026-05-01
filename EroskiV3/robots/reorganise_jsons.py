#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Uniformise la structure des fichiers *_iAdetailed.json
dans un ou plusieurs dossiers / fichiers passés en argument.
Compatible avec JSON racine = dict ou list de produits.
"""

import os
import sys
import json
from collections import OrderedDict

# --- Modèle cible pour evolution (ordre + valeurs par défaut) ---
EVOLUTION_TEMPLATE = OrderedDict([
    ("parsing_date", None),
    ("format", None),
    ("availability", None),
    ("nutri_Score", None),
    ("nutrition", OrderedDict([
        ("energies", OrderedDict([
            ("kj", None),
            ("kcal", None),
        ])),
        ("minerals", OrderedDict([
            ("salt", None),
            ("calcium", None),
        ])),
        ("fats", OrderedDict([
            ("fats", None),
            ("saturates", None),
        ])),
        ("proteins", OrderedDict([
            ("proteins", None),
        ])),
        ("carbohydrates", OrderedDict([
            ("carbohydrates", None),
            ("of_which_sugars", None),
            ("dietary_fiber", None),
        ])),
    ])),
    ("ingredients", None),
    ("ingredients_clean", None),
    ("ingredients_ia", []),
    ("allergens", []),
    ("reviews", OrderedDict([
        ("average", 0.0),
        ("count", 0),
    ])),
    ("weight_per_packaging", None),
    ("price_per_packaging", None),
    ("price_per_unit", None),
])

# --- Normalisation d'une evolution ---
def normalize_evolution(evo: dict) -> OrderedDict:
    normalized = OrderedDict()
    for key, default in EVOLUTION_TEMPLATE.items():
        if isinstance(default, OrderedDict):
            sub = evo.get(key, {})
            normalized[key] = OrderedDict()
            for subk, subdefault in default.items():
                normalized[key][subk] = sub.get(subk, subdefault)
        else:
            normalized[key] = evo.get(key, default)

    # --- Nettoyage spécial pour ingredients_ia ---
    if isinstance(normalized.get("ingredients_ia"), list):
        cleaned = []
        seen = set()
        for ing in normalized["ingredients_ia"]:
            if not ing:
                continue
            ing_str = str(ing).strip()
            # on supprime toute phrase contenant "mymemory warning"
            if "mymemory warning" in ing_str.lower():
                print(f"⚠️ Suppression d'une entrée MyMemory Warning : {ing_str[:60]}...")
                continue
            # éviter les doublons (insensible à la casse)
            if ing_str.lower() in seen:
                print(f"🔁 Doublon supprimé : {ing_str}")
                continue
            seen.add(ing_str.lower())
            cleaned.append(ing_str)
        normalized["ingredients_ia"] = cleaned

    return normalized

# --- Normalisation d'un produit (dict) ---
def normalize_product(product: dict) -> dict:
    if "evolutions" in product and isinstance(product["evolutions"], list):
        old_count = len(product["evolutions"])
        product["evolutions"] = [normalize_evolution(e) for e in product["evolutions"]]
        print(f"✅ {old_count} evolution(s) normalisée(s) pour produit EAN {product.get('ean')}")
    return product

# --- Traitement d'un fichier JSON ---
def process_file(path: str):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, list):  # cas racine = liste de produits
            data = [normalize_product(prod) for prod in data]
        elif isinstance(data, dict):  # cas racine = un seul produit
            data = normalize_product(data)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    except Exception as e:
        print(f"❌ Erreur {path} : {e}")

# --- Gestion des chemins ---
def process_path(path: str):
    if os.path.isfile(path) and "iAdetailed.json" in path:
        process_file(path)
    elif os.path.isdir(path):
        for root, _, files in os.walk(path):
            for file in files:
                if "iAdetailed.json" in file:
                    process_file(os.path.join(root, file))

def main():
    # Demande manuelle si aucun argument
    if len(sys.argv) > 1:
        paths = sys.argv[1:]
    else:
        user_input = input("👉 Entrez le chemin du fichier ou dossier à traiter : ").strip()
        paths = [user_input]

    for p in paths:
        process_path(p)

if __name__ == "__main__":
    main()
