#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json

# --- Normalisation du sel ---
def normalize_salt(nutrition: dict) -> float:
    raw_salt = nutrition.get("minerals", {}).get("salt", 0) or 0
    if raw_salt < 1:  
        salt_mg = raw_salt * 1000  # g → mg
    else:
        salt_mg = raw_salt         # déjà en mg
    return salt_mg / 1000.0  # mg → g


# --- Fonction de calcul du Nutri-Score ---
def compute_nutriscore(nutrition: dict) -> str:
    if not nutrition:
        return "N/A"

    kj = nutrition.get("energies", {}).get("kj", 0) or 0
    sugars = nutrition.get("carbohydrates", {}).get("of_which_sugars", 0) or 0
    sat_fats = nutrition.get("fats", {}).get("saturates", 0) or 0
    fiber = nutrition.get("carbohydrates", {}).get("dietary_fiber", 0) or 0
    proteins = nutrition.get("proteins", {}).get("proteins", 0) or 0
    salt = normalize_salt(nutrition)

    # --- Points négatifs ---
    points_energy = (
        0 if kj <= 335 else
        1 if kj <= 670 else
        2 if kj <= 1005 else
        3 if kj <= 1340 else
        4 if kj <= 1675 else
        5 if kj <= 2010 else
        6 if kj <= 2345 else
        7 if kj <= 2680 else
        8 if kj <= 3015 else
        9 if kj <= 3350 else 10
    )

    points_sugar = (
        0 if sugars <= 4.5 else
        1 if sugars <= 9 else
        2 if sugars <= 13.5 else
        3 if sugars <= 18 else
        4 if sugars <= 22.5 else
        5 if sugars <= 27 else
        6 if sugars <= 31 else
        7 if sugars <= 36 else
        8 if sugars <= 40 else
        9 if sugars <= 45 else 10
    )

    points_satfat = (
        0 if sat_fats <= 1 else
        1 if sat_fats <= 2 else
        2 if sat_fats <= 3 else
        3 if sat_fats <= 4 else
        4 if sat_fats <= 5 else
        5 if sat_fats <= 6 else
        6 if sat_fats <= 7 else
        7 if sat_fats <= 8 else
        8 if sat_fats <= 9 else
        9 if sat_fats <= 10 else 10
    )

    points_salt = (
        0 if salt <= 0.09 else
        1 if salt <= 0.18 else
        2 if salt <= 0.27 else
        3 if salt <= 0.36 else
        4 if salt <= 0.45 else
        5 if salt <= 0.54 else
        6 if salt <= 0.63 else
        7 if salt <= 0.72 else
        8 if salt <= 0.81 else
        9 if salt <= 0.9 else 10
    )

    negative = points_energy + points_sugar + points_satfat + points_salt

    # --- Points positifs ---
    points_fiber = (
        0 if fiber <= 0.9 else
        1 if fiber <= 1.9 else
        2 if fiber <= 2.8 else
        3 if fiber <= 3.7 else
        4 if fiber <= 4.7 else 5
    )

    points_protein = (
        0 if proteins <= 1.6 else
        1 if proteins <= 3.2 else
        2 if proteins <= 4.8 else
        3 if proteins <= 6.4 else
        4 if proteins <= 8.0 else 5
    )

    positive = points_fiber + points_protein

    score = negative - positive

    if score <= -1:
        return "A"
    elif score <= 2:
        return "B"
    elif score <= 10:
        return "C"
    elif score <= 18:
        return "D"
    else:
        return "E"


# --- Mise à jour d’un fichier ---
def update_nutriscore_in_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    modified = False
    for product in data if isinstance(data, list) else [data]:
        evolutions = product.get("evolutions", [])
        for evo in evolutions:
            if evo.get("nutri_Score") in [None, "", "N/A", "UNKNOWN"]:
                nutri = evo.get("nutrition")
                evo["nutri_Score"] = compute_nutriscore(nutri)
                modified = True

    if modified:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"✅ Nutri-Score mis à jour dans {path}")
    else:
        print(f"⏩ Aucun changement dans {path}")


# --- Traitement dossier récursif ---
def process_folder(folder: str):
    for root, _, files in os.walk(folder):
        for fname in files:
            if "iAdetailed" in fname and fname.endswith(".json"):
                update_nutriscore_in_file(os.path.join(root, fname))


if __name__ == "__main__":
    chemin = input("👉 Entrez le chemin d’un fichier JSON ou d’un dossier : ").strip()

    if os.path.isfile(chemin) and "iAdetailed" in chemin and chemin.endswith(".json"):
        update_nutriscore_in_file(chemin)
    elif os.path.isdir(chemin):
        process_folder(chemin)
    else:
        print("⚠️ Veuillez entrer un fichier JSON valide (iAdetailed) ou un dossier contenant des fichiers iAdetailed.json.")
