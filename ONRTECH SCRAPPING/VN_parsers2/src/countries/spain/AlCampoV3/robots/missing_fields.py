#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import sys
import re

# --- Fonctions utilitaires ---
def is_partial_null_nutrition(nutrition: dict) -> bool:
    """Détecte une nutrition partiellement remplie (beaucoup de None explicites)."""
    if not nutrition or not isinstance(nutrition, dict):
        return False
    flat_vals = []
    def collect_vals(d):
        for v in d.values():
            if isinstance(v, dict):
                collect_vals(v)
            else:
                flat_vals.append(v)
    collect_vals(nutrition)
    non_null = [v for v in flat_vals if v is not None]
    nulls = [v for v in flat_vals if v is None]
    return len(non_null) > 0 and len(nulls) >= len(non_null)

def is_illogical_ingredients(ingredients: str) -> bool:
    if not ingredients or not isinstance(ingredients, str):
        return True
    ing = ingredients.strip().lower()
    if len(ing) < 5:
        return True
    if re.fullmatch(r"[\d\s.,;:]+", ing):
        return True
    if ing.count("ingrédient") > 2:
        return True
    return False

def is_illogical_ingredients_clean(ingredients_clean: str) -> bool:
    """Détecte si ingredients_clean est illogique (vide, trop court, format ou bruit)."""
    if not ingredients_clean or not isinstance(ingredients_clean, str):
        return True
    ing = ingredients_clean.strip().lower()
    if len(ing) < 5:
        return True
    if re.fullmatch(r"[\d\s.,;:]+", ing):
        return True
    if any(word in ing for word in ["lata", "pack", "ud", "unidad", "sobre", "caja"]):
        return True
    return False

def is_illogical_nutrition(nutrition: dict) -> bool:
    if not nutrition or not isinstance(nutrition, dict):
        return True
    if all(v in [None, 0, ""] or (isinstance(v, dict) and len(v) == 0) for v in nutrition.values()):
        return True
    energies = nutrition.get("energies", {})
    if isinstance(energies, dict):
        kcal = energies.get("kcal")
        if isinstance(kcal, (int, float)) and kcal > 10000:
            return True
    return False

def is_illogical_brand(brand: str) -> bool:
    if not brand or not isinstance(brand, str):
        return True
    b = brand.strip()
    if len(b) < 2:
        return True
    if re.match(r"^\d", b):
        return True
    if re.fullmatch(r"[0-9%+\s]+", b):
        return True
    if re.search(r"\+\s*\d+\s*(mes|meses|m)", b, re.IGNORECASE):
        return True
    for bad in ["0%", "sin", "azúcar", "azúcares", "instantáneo", "añadidos"]:
        if bad.lower() in b.lower():
            return True
    return False

def looks_like_format_instead_of_ingredients(val: str) -> bool:
    """Détecte si la valeur est un format pur (g/ml/ud), pas une vraie liste d'ingrédients."""
    if not val or not isinstance(val, str):
        return False
    txt = val.lower().strip()

    patterns = [
        r"^\d+\s*(g|gr|gr\.|kg|ml|cl|l|litro?s?|litre?s?)\.?$",      # ex: "190 g", "220 ml", "500 gr", "1 litro", "2 litres"
        r"^\d+\s*(ud|uds|unidad(?:es)?)\s*\d+\s*(g|gr|gr\.|kg|ml|cl|l|litro?s?|litre?s?)$", 
        # ex: "10 ud 50 g", "10 uds 200 ml", "12 unidades 1 litro"
        r"\b\d+[.,]?\d*\s*(g|gr|gr\.|kg)\s*(de|x)\s*cápsula",       # ex: "7 gr de café x cápsula"
        r"^\d+\s*(uds?|capsulas?|cápsulas?)\b",                     # ex: "16 uds.", "10 cápsulas"
        r"^(gramos?|grams?|gr|gr\.|litro?s?|litre?s?)$",            # ex: "gramos", "litros", "litre"
        r"^\d+\s*(grams?|gramos?|gr|gr\.|kg|ml|cl|l|litro?s?|litre?s?|liter?s?)$",
        # ex: "500 gramos", "1 litro", "2 litres"
    ]
    return any(re.search(p, txt) for p in patterns)


def looks_like_ean(val: str) -> bool:
    """Détecte si une valeur ressemble à un code EAN (8 à 14 chiffres)."""
    if not val or not isinstance(val, str):
        return False
    return bool(re.fullmatch(r"\d{8,14}", val.strip()))

# --- Fonction principale ---
def count_missing_fields(root_path, txt_output="missing_fields_report.txt"):
    total_products = 0
    # Compteurs de manquants
    missing_format = missing_weight = missing_price = 0
    missing_unit_packaging = missing_unit_price = 0
    missing_matter = missing_origin = missing_brand = 0
    missing_nutrition = missing_ingredients = missing_ingredients_ia = 0
    missing_nutriscore = 0
    # Compteurs illogiques
    illogical_ingredients = illogical_ingredients_clean = illogical_nutrition = illogical_brand = 0
    # Cas spéciaux
    ingredients_as_format = ingredients_as_ean = 0
    ingredients_clean_as_format = ingredients_clean_as_ean = 0
    ingredients_ia_as_format = ingredients_ia_mymemory_warning = 0
    # Détails
    missing_details, illogical_details, special_details = [], [], []

    # 🔧 Correction : accepte fichier ou dossier
    files_to_process = []
    if os.path.isfile(root_path):
        if "iAdetailed" in os.path.basename(root_path) and ".json" in os.path.basename(root_path):
            files_to_process.append(root_path)
    else:
        for dp, _, files in os.walk(root_path):
            for fn in files:
                if "iAdetailed" in fn and ".json" in fn:
                    files_to_process.append(os.path.join(dp, fn))

    # --- Parcours des fichiers à traiter ---
    for full_path in files_to_process:
        try:
            with open(full_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            products = data if isinstance(data, list) else [data]

            for product in products:
                total_products += 1
                evolutions = product.get("evolutions", [])
                rel_path = os.path.relpath(full_path, root_path if os.path.isdir(root_path) else os.path.dirname(root_path))
                ean = product.get("ean", "❓")
                title = (
                    product.get("title")
                    or product.get("lang_desc", {}).get("fr", {}).get("title")
                    or product.get("lang_desc", {}).get("es", {}).get("title")
                    or "❓"
                )

                # Vérif brand
                if product.get("brand") in [None, "", "0", 0]:
                    missing_brand += 1
                    missing_details.append((rel_path, ean, title, "brand", None))
                else:
                    brand_val = product.get("brand")
                    if is_illogical_brand(brand_val):
                        illogical_brand += 1
                        illogical_details.append((ean, rel_path, title, "brand", brand_val))

                # Vérif autres champs simples
                if product.get("matter") in [None, "", "0", 0]:
                    missing_matter += 1
                if not product.get("origin"):
                    missing_origin += 1
                if product.get("mesure_unit_for_packaging") in [None, "", "0", 0]:
                    missing_unit_packaging += 1
                if product.get("mesure_unit_for_price_per_unit") in [None, "", "0", 0]:
                    missing_unit_price += 1

                # Boucle sur evolutions
                if isinstance(evolutions, list):
                    has_format = has_weight = has_price = has_nutrition = False
                    has_ingredients = has_ingredients_ia = False
                    for evo in evolutions:
                        if not isinstance(evo, dict):
                            continue
                        fmt = evo.get("format")
                        weight = evo.get("weight_per_packaging")
                        price = evo.get("price_per_unit")
                        nutrition = evo.get("nutrition")
                        ingredients = evo.get("ingredients")
                        ingredients_clean = evo.get("ingredients_clean")
                        ingredients_ia = evo.get("ingredients_ia")
                        nutri_Score = evo.get("nutri_Score")

                        if fmt: has_format = True
                        if weight not in [None, "", 0]: has_weight = True
                        if price not in [None, "", 0]: has_price = True
                        if nutrition and isinstance(nutrition, dict) and len(nutrition) > 0: has_nutrition = True
                        if ingredients and isinstance(ingredients, str) and ingredients.strip(): has_ingredients = True
                        if ingredients_ia and isinstance(ingredients_ia, list) and len(ingredients_ia) > 0: has_ingredients_ia = True

                        # --- Manquants ---
                        if weight in [None, "", 0]:
                            missing_weight += 1
                            missing_details.append((rel_path, ean, title, "weight_per_packaging", weight))

                        if price in [None, "", 0]:
                            missing_price += 1
                            missing_details.append((rel_path, ean, title, "price_per_unit", price))

                        if not nutrition:
                            missing_nutrition += 1
                            missing_details.append((rel_path, ean, title, "nutrition", nutrition))

                        if not ingredients:
                            missing_ingredients += 1
                            missing_details.append((rel_path, ean, title, "ingredients", ingredients))

                        if not ingredients_ia:
                            missing_ingredients_ia += 1
                            missing_details.append((rel_path, ean, title, "ingredients_ia", ingredients_ia))

                        if nutri_Score in [None, "", "N/A", "n/a", "NA", "na", "UNKNOWN", "_"]:
                            missing_nutriscore += 1
                            missing_details.append((rel_path, ean, title, "nutri_Score", nutri_Score))

                        # --- Illogiques ---
                        if is_illogical_ingredients(ingredients):
                            illogical_ingredients += 1
                            illogical_details.append((ean, rel_path, title, "ingredients", ingredients))

                        if is_illogical_ingredients_clean(ingredients_clean):
                            illogical_ingredients_clean += 1
                            illogical_details.append((ean, rel_path, title, "ingredients_clean", ingredients_clean))

                        if is_illogical_nutrition(nutrition):
                            illogical_nutrition += 1
                            illogical_details.append((ean, rel_path, title, "nutrition", nutrition))

                        if nutrition and is_partial_null_nutrition(nutrition):
                            illogical_nutrition += 1
                            illogical_details.append((ean, rel_path, title, "nutrition_partial", nutrition))

                        # --- Cas spéciaux ingredients ---
                        if isinstance(ingredients, str):
                            if looks_like_format_instead_of_ingredients(ingredients):
                                ingredients_as_format += 1
                                special_details.append((ean, rel_path, title, "ingredients_as_format", ingredients))
                            elif looks_like_ean(ingredients):
                                ingredients_as_ean += 1
                                special_details.append((ean, rel_path, title, "ingredients_as_ean", ingredients))
                        if isinstance(ingredients_clean, str):
                            if looks_like_format_instead_of_ingredients(ingredients_clean):
                                ingredients_clean_as_format += 1
                                special_details.append((ean, rel_path, title, "ingredients_clean_as_format", ingredients_clean))
                            elif looks_like_ean(ingredients_clean):
                                ingredients_clean_as_ean += 1
                                special_details.append((ean, rel_path, title, "ingredients_clean_as_ean", ingredients_clean))
                        if isinstance(ingredients_ia, list):
                            count_formats = 0
                            for ingr in ingredients_ia:
                                if isinstance(ingr, str) and looks_like_format_instead_of_ingredients(ingr):
                                    count_formats += 1
                                    special_details.append((ean, rel_path, title, "ingredients_ia_as_format", ingr))
                                elif isinstance(ingr, str) and "mymemory warning" in ingr.lower():
                                    ingredients_ia_mymemory_warning += 1
                                    special_details.append((ean, rel_path, title, "ingredients_ia_mymemory", ingr))
                            if count_formats > 0:
                                ingredients_ia_as_format += count_formats

                    if not has_format:
                        missing_format += 1
        except Exception as e:
            print(f"⚠️ Erreur lecture {full_path} : {e}")

    # --- Résumé console ---
    print("📊 Résultats globaux :")
    print(f"   ➤ Produits totaux : {total_products}")
    print(f"   ➤ Missing brand : {missing_brand}")
    print(f"   ➤ Missing format : {missing_format}")
    print(f"   ➤ Missing weight : {missing_weight}")
    print(f"   ➤ Missing price : {missing_price}")
    print(f"   ➤ Missing unit packaging : {missing_unit_packaging}")
    print(f"   ➤ Missing unit price : {missing_unit_price}")
    print(f"   ➤ Missing matter : {missing_matter}")
    print(f"   ➤ Missing origin : {missing_origin}")
    print(f"   ➤ Missing nutrition : {missing_nutrition}")
    print(f"   ➤ Missing ingredients : {missing_ingredients}")
    print(f"   ➤ Missing ingredients_ia : {missing_ingredients_ia}")
    print(f"   ➤ Missing nutri_Score : {missing_nutriscore}")
    print(f"   ➤ Illogical ingredients : {illogical_ingredients}")
    print(f"   ➤ Illogical ingredients_clean : {illogical_ingredients_clean}")
    print(f"   ➤ Illogical nutrition : {illogical_nutrition}")
    print(f"   ➤ Illogical brand : {illogical_brand}")
    print(f"   ➤ Ingredients as format : {ingredients_as_format}")
    print(f"   ➤ Ingredients as EAN : {ingredients_as_ean}")
    print(f"   ➤ Ingredients_clean as format : {ingredients_clean_as_format}")
    print(f"   ➤ Ingredients_clean as EAN : {ingredients_clean_as_ean}")
    print(f"   ➤ Ingredients_ia as format : {ingredients_ia_as_format}")
    print(f"   ➤ Ingredients_ia with Mymemory warning : {ingredients_ia_mymemory_warning}")

    # --- Aperçu console ---
    if missing_details:
        print("\n❌ Aperçu des 100 premiers produits avec champs manquants :")
        for file_path, ean, title, champ, fmt in missing_details[:100]:
            print(f"   - {ean} | {title} | fichier: {file_path} | manque={champ} | format={fmt}")
        if len(missing_details) > 100:
            print(f"   ... et {len(missing_details) - 100} autres (voir {txt_output})")

    if illogical_details:
        print("\n❌ Aperçu des 100 premiers produits illogiques :")
        for ean, file_path, title, champ, val in illogical_details[:100]:
            print(f"   - {ean} | {title} | fichier: {file_path} | champ={champ} | valeur={val}")
        if len(illogical_details) > 100:
            print(f"   ... et {len(illogical_details) - 100} autres (voir {txt_output})")

    if special_details:
        print("\n❌ Aperçu des 100 premiers cas spéciaux (ingredients/clean = format ou EAN) :")
        for ean, file_path, title, champ, val in special_details[:100]:
            print(f"   - {ean} | {title} | fichier: {file_path} | champ={champ} | valeur={val}")
        if len(special_details) > 100:
            print(f"   ... et {len(special_details) - 100} autres (voir {txt_output})")


     # --- Sauvegarde TXT ---
    with open(txt_output, "w", encoding="utf-8") as out:
        out.write("📊 Résultats globaux :\n")
        out.write(f"   ➤ Produits totaux : {total_products}\n")
        out.write(f"   ➤ Missing brand : {missing_brand}\n")
        out.write(f"   ➤ Missing format : {missing_format}\n")
        out.write(f"   ➤ Missing weight : {missing_weight}\n")
        out.write(f"   ➤ Missing price : {missing_price}\n")
        out.write(f"   ➤ Missing unit packaging : {missing_unit_packaging}\n")
        out.write(f"   ➤ Missing unit price : {missing_unit_price}\n")
        out.write(f"   ➤ Missing matter : {missing_matter}\n")
        out.write(f"   ➤ Missing origin : {missing_origin}\n")
        out.write(f"   ➤ Missing nutrition : {missing_nutrition}\n")
        out.write(f"   ➤ Missing ingredients : {missing_ingredients}\n")
        out.write(f"   ➤ Missing ingredients_ia : {missing_ingredients_ia}\n")
        out.write(f"   ➤ Missing nutri_Score : {missing_nutriscore}\n")
        out.write(f"   ➤ Illogical ingredients : {illogical_ingredients}\n")
        out.write(f"   ➤ Illogical ingredients_clean : {illogical_ingredients_clean}\n")
        out.write(f"   ➤ Illogical nutrition : {illogical_nutrition}\n")
        out.write(f"   ➤ Illogical brand : {illogical_brand}\n")
        out.write(f"   ➤ Ingredients as format : {ingredients_as_format}\n")
        out.write(f"   ➤ Ingredients as EAN : {ingredients_as_ean}\n")
        out.write(f"   ➤ Ingredients_clean as format : {ingredients_clean_as_format}\n")
        out.write(f"   ➤ Ingredients_clean as EAN : {ingredients_clean_as_ean}\n")
        out.write(f"   ➤ Ingredients_ia as format : {ingredients_ia_as_format}\n")
        out.write(f"   ➤ Ingredients_ia with Mymemory warning : {ingredients_ia_mymemory_warning}\n")

        

        out.write("\n--- Manquants ---\n")
        for file_path, ean, title, champ, fmt in missing_details:
            out.write(f"{ean} | {title} | fichier:{file_path} | manque={champ} | format={fmt}\n")

        out.write("\n--- Illogiques ---\n")
        for ean, file_path, title, champ, val in illogical_details:
            out.write(f"{ean} | {title} | fichier:{file_path} | champ={champ} | valeur={val}\n")

        out.write("\n--- Cas spéciaux (format/EAN) ---\n")
        for ean, file_path, title, champ, val in special_details:
            out.write(f"{ean} | {title} | fichier:{file_path} | champ={champ} | valeur={val}\n")

    print(f"\n📂 Rapport TXT complet : {txt_output}")


if __name__ == "__main__":
    dossier = sys.argv[1] if len(sys.argv) > 1 else input("📂 Entrez le chemin du dossier à analyser : ").strip()
    if not os.path.exists(dossier):
        print("❌ Chemin invalide.")
        sys.exit(1)
    count_missing_fields(dossier)
