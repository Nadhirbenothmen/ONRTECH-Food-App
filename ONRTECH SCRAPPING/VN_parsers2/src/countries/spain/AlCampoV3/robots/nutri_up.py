#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json

# --- Config ---
BASE_PETS_DIR = "src/countries/spain/AlCampoV3/robots/products"  # chemin racine
PETS_FOLDERS = [
    "Pets_Birds_food",
    "Pets_Cats_food",
    "Pets_Dog_food",
    "Pets_Fish_food",
    "Pets_Rabbits_food"
]

def update_nutriscore_in_file(file_path: str):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Erreur lecture {file_path}: {e}")
        return False

    changed = False

    def process_product(prod):
        nonlocal changed
        if isinstance(prod, dict) and "evolutions" in prod:
            for evo in prod["evolutions"]:
                if "nutri_Score" in evo and evo["nutri_Score"] != "N/A":
                    evo["nutri_Score"] = "N/A"
                    changed = True

    if isinstance(data, list):
        for p in data:
            process_product(p)
    elif isinstance(data, dict):
        process_product(data)

    if changed:
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"✅ Mis à jour : {file_path}")
            return True
        except Exception as e:
            print(f"❌ Erreur écriture {file_path}: {e}")
    return False


def process_directory(folder: str):
    updated_files = 0
    for root, _, files in os.walk(folder):
        for name in files:
            if name.endswith(".json"):
                if update_nutriscore_in_file(os.path.join(root, name)):
                    updated_files += 1
    print(f"\n🎯 Terminé dans {folder} : {updated_files} fichiers JSON modifiés.")


if __name__ == "__main__":
    total_updated = 0
    for folder in PETS_FOLDERS:
        path = os.path.join(BASE_PETS_DIR, folder)
        if os.path.exists(path):
            process_directory(path)
        else:
            print(f"⚠️ Dossier introuvable : {path}")
    print("🐾 Nutri-Score des produits animaux remplacé par 'N/A' (mise à jour terminée)")
