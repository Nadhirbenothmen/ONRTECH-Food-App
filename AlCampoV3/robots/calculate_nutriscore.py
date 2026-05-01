#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import os
import sys
import json
import re

# Permet d’importer vos modules depuis src/
sys.path.append(os.path.abspath("src"))
sys.path.append(os.path.abspath("."))

from src.countries.spain.AlCampoV3.model.product_content_alcampo import ProductContentAlcampo

# Regex pour détecter le format (ex: "4 uds", "250 ml", "1 kg", "pack de 6", etc.)
FORMAT_REGEX = re.compile(
    r"(\d+(?:[.,]\d+)?\s*(?:uds?|unidades?|g|kg|ml|l|cl|pack(?:s)?|sobres?|u))",
    re.IGNORECASE
)

def extract_format_from_title(title: str) -> str | None:
    """
    Extrait le format depuis un titre de produit en se basant sur FORMAT_REGEX.
    Retourne la première occurrence ou None si pas trouvé.
    """
    if not title:
        return None
    match = FORMAT_REGEX.search(title)
    return match.group(1).strip() if match else None


def process_file(filepath: str):
    """
    Ouvre un fichier iAdetailed JSON, recalcule/injecte nutriscore si nécessaire,
    nettoie ingredients_ia pour n’y garder que des strings,
    extrait et ajoute le champ 'format' dans les évolutions juste après 'parsing_date',
    et écrase le fichier en mettant à jour les produits.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Impossible de lire {filepath}: {e}")
        return 0, 0

    products = data if isinstance(data, list) else [data]
    missing = 0

    for prod in products:
        evo = prod.setdefault("evolutions", [{}])[0]

        # --- Nettoyage de ingredients_ia : on ne garde que la chaîne du nom ---
        ia_vals = evo.get("ingredients_ia", [])
        clean_ia = []
        for item in ia_vals:
            if isinstance(item, dict) and "name" in item:
                clean_ia.append(item["name"])
            elif isinstance(item, str):
                clean_ia.append(item)
        evo["ingredients_ia"] = clean_ia

        # --- Vérification et ajout du format juste après 'parsing_date' ---
        if "parsing_date" in evo:  # Vérification si 'parsing_date' existe
            title = (
                prod.get("lang_desc", {}).get("es", {}).get("title")
                or prod.get("label")
                or ""
            )
            fmt = extract_format_from_title(title)
            if fmt:
                # On crée un ordre spécifique : ajouter "format" juste après "parsing_date"
                evo_ordered = {
                    "parsing_date": evo["parsing_date"],
                    "format": fmt,
                }
                # On ajoute les autres champs après "parsing_date" et "format"
                for key, value in evo.items():
                    if key not in ["parsing_date", "format"]:
                        evo_ordered[key] = value
                # Réassigner l'ordre à l'élément de l'évolution
                evo.clear()
                evo.update(evo_ordered)

                print(f"🔖 {os.path.basename(filepath)}: format extrait et ajouté juste après 'parsing_date' → {fmt}")
            else:
                print(f"⚠️ {os.path.basename(filepath)}: Aucun format trouvé dans le titre.")

        # --- Recalcul / injection NutriScore si manquant ou 'N/A' ---
        score = evo.get("nutriscore")
        if score is None or score == "N/A":
            nutrition = evo.get("nutrition")
            new_score = None
            if nutrition:
                try:
                    new_score = ProductContentAlcampo.calculate_nutriscore_from_nested(nutrition)
                except Exception as e:
                    print(f"⚠️ Erreur calcul nutriscore {prod.get('id','?')}: {e}")
            evo["nutriscore"] = new_score
            if new_score is not None:
                print(f"✅ {os.path.basename(filepath)}: nutriscore injecté → {new_score}")
            else:
                missing += 1

    # Réécriture uniquement si nécessaire
    try:
        out = products if isinstance(data, list) else products[0]
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"❌ Impossible d’écrire {filepath}: {e}")

    total = len(products)
    print(f"{os.path.basename(filepath)} → manquants: {missing}/{total}")
    return missing, total

def process_directory_or_file(path: str):
    """
    Traite un fichier ou un dossier. Si c'est un fichier, on le traite directement.
    Si c'est un dossier, on parcourt tous les fichiers dedans.
    """
    total_missing = 0
    total_products = 0

    if os.path.isdir(path):
        # Si c'est un dossier, on parcourt tous les fichiers
        for dirpath, _, files in os.walk(path):
            for fname in files:
                if fname.endswith(".json") and "iAdetailed" in fname:
                    fullpath = os.path.join(dirpath, fname)
                    print(f"[INFO] Traitement de {fullpath}")
                    m, t = process_file(fullpath)
                    total_missing += m
                    total_products += t
    elif os.path.isfile(path):
        # Si c'est un fichier, on le traite directement
        print(f"[INFO] Traitement de {path}")
        m, t = process_file(path)
        total_missing += m
        total_products += t
    else:
        print("❌ Ce n'est pas un fichier ou un dossier valide.")
        return

    print("\n=== RÉCAP GLOBAL ===")
    print(f"Produits totaux :       {total_products}")
    print(f"Nutri-scores manquants : {total_missing}")
    if total_products:
        pct = total_missing / total_products * 100
        print(f"Taux d’absents :        {pct:.2f}%")


def main():
    path = input("📂 Entrez le chemin d'un fichier ou d'un dossier à traiter (iAdetailed only): ").strip()
    process_directory_or_file(path)


if __name__ == "__main__":
    main()
