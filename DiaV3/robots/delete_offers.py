#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json

# --- Config ---
ROOT_DIR = "src/countries/spain/DiaV3/robots/products"  # <-- adapte ton chemin

def clean_offers_in_file(file_path: str):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Erreur lecture {file_path}: {e}")
        return

    changed = False

    def process_product(prod):
        nonlocal changed
        if not isinstance(prod, dict):
            return

        # Supprimer offers au niveau racine
        if "offers" in prod and (prod["offers"] in [None, []]):
            prod.pop("offers")
            changed = True

        # Supprimer offers dans evolutions
        if "evolutions" in prod and isinstance(prod["evolutions"], list):
            for evo in prod["evolutions"]:
                if isinstance(evo, dict) and "offers" in evo and (evo["offers"] in [None, []]):
                    evo.pop("offers")
                    changed = True

    # Liste de produits ou produit unique
    if isinstance(data, list):
        for p in data:
            process_product(p)
    elif isinstance(data, dict):
        process_product(data)

    if changed:
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"✅ Nettoyé : {file_path}")
        except Exception as e:
            print(f"❌ Erreur écriture {file_path}: {e}")


def process_directory(folder: str):
    total = 0
    for root, _, files in os.walk(folder):
        for name in files:
            if name.endswith(".json"):
                file_path = os.path.join(root, name)
                clean_offers_in_file(file_path)
                total += 1
    print(f"\n🎯 Terminé : {total} fichiers JSON analysés.")


if __name__ == "__main__":
    process_directory(ROOT_DIR)
