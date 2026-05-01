#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json

def clean_nutrition(obj):
    """Supprime le champ nutrition si = {'carbohydrates': {}} dans evolutions."""
    if isinstance(obj, dict):
        # Cas "evolutions" = liste
        if "evolutions" in obj and isinstance(obj["evolutions"], list):
            for evo in obj["evolutions"]:
                if isinstance(evo, dict) and evo.get("nutrition") == {"carbohydrates": {}}:
                    del evo["nutrition"]

        # Parcours récursif des sous-objets
        for v in obj.values():
            clean_nutrition(v)

    elif isinstance(obj, list):
        for item in obj:
            clean_nutrition(item)


def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"❌ Erreur JSON dans {filepath}: {e}")
            return

    clean_nutrition(data)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"✅ Nettoyé: {filepath}")


if __name__ == "__main__":
    path = input("👉 Entrez le chemin du fichier ou dossier JSON à nettoyer : ").strip()

    if os.path.isfile(path):
        process_file(path)
    elif os.path.isdir(path):
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(".json"):
                    process_file(os.path.join(root, file))
    else:
        print(f"❌ Chemin introuvable: {path}")
