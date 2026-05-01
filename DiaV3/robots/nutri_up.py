#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json

# --- Config ---
PETS_DIR = "src/countries/spain/diaV3/robots/products/Pets"  # <-- adapte le chemin à ton projet

def update_nutriscore_in_file(file_path: str):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Erreur lecture {file_path}: {e}")
        return

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
        except Exception as e:
            print(f"❌ Erreur écriture {file_path}: {e}")


def process_directory(folder: str):
    updated_files = 0
    for root, _, files in os.walk(folder):
        for name in files:
            if name.endswith(".json"):
                update_nutriscore_in_file(os.path.join(root, name))
                updated_files += 1
    print(f"\n🎯 Terminé : {updated_files} fichiers JSON modifiés.")


if __name__ == "__main__":
    process_directory(PETS_DIR)
    print("🐾 Nutri-Score des produits animaux remplacé par 'N/A' (mise à jour des originaux)")
