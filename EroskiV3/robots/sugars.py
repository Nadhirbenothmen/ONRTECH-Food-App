#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
from typing import Any, Dict
from collections import OrderedDict

def transform_evolution(evolution: Dict[str, Any]) -> Dict[str, Any]:
    """Applique les règles de transformation sur un bloc evolution."""
    nutrition = evolution.get("nutrition", {})

    # ---- 1. Remplacer les null par 0.0 ----
    def replace_nulls(d: Dict[str, Any]):
        for k, v in d.items():
            if isinstance(v, dict):
                replace_nulls(v)
            else:
                if v is None:
                    d[k] = 0.0
    replace_nulls(nutrition)

    # ---- 2. Renommer sugars -> of_which_sugars ----
    carbs = nutrition.get("carbohydrates", {})
    if "sugars" in carbs:
        carbs["of_which_sugars"] = carbs.pop("sugars")

    # Réordonner explicitement carbohydrates
    if isinstance(carbs, dict):
        ordered_carbs = OrderedDict()
        if "carbohydrates" in carbs:
            ordered_carbs["carbohydrates"] = carbs["carbohydrates"]
        if "of_which_sugars" in carbs:
            ordered_carbs["of_which_sugars"] = carbs["of_which_sugars"]
        if "dietary_fiber" in carbs:
            ordered_carbs["dietary_fiber"] = carbs["dietary_fiber"]
        nutrition["carbohydrates"] = ordered_carbs

    # ---- 3. Ajuster minerals ----
    minerals = nutrition.get("minerals", {})
    if "salt" in minerals and isinstance(minerals["salt"], (int, float)):
        if minerals["salt"] < 9:
            minerals["salt"] = minerals["salt"] * 1000

    if "calcium" in minerals and isinstance(minerals["calcium"], (int, float)):
        if minerals["calcium"] < 2:
            minerals["calcium"] = minerals["calcium"] * 1000

    return evolution

def process_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    # JSON racine = dict avec evolutions
    if isinstance(data, dict) and "evolutions" in data:
        data["evolutions"] = [transform_evolution(evo) for evo in data["evolutions"]]

    # JSON racine = liste de produits
    elif isinstance(data, list):
        for product in data:
            if "evolutions" in product:
                product["evolutions"] = [transform_evolution(evo) for evo in product["evolutions"]]

    # Sauvegarde (on écrase le fichier)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"✅ Fichier mis à jour : {filepath}")

if __name__ == "__main__":
    path = input("👉 Entrez le chemin d'un fichier ou dossier à traiter : ").strip()

    if os.path.isdir(path):
        for root, _, files in os.walk(path):
            for fname in files:
                if fname.endswith(".json"):
                    process_file(os.path.join(root, fname))
    elif os.path.isfile(path) and path.endswith(".json"):
        process_file(path)
    else:
        print("❌ Chemin invalide. Donnez un fichier .json ou un dossier contenant des .json.")
