from datetime import datetime
import os
import json
import sys
import re
# --- Garder uniquement la dernière version iAdetailed ---
IAD_FILE_PAT = re.compile(
    r'^(?P<root>.+?\.json)(?:_(?P<rawts>\d{2}(?:_\d{2}){4}|\d{4}(?:_\d{2}){4}))?_iAdetailed'
    r'(?:_(?P<iadts>\d{2}(?:_\d{2}){4}|\d{4}(?:_\d{2}){4}))?\.json$',
    re.I
)

# Ajoute le chemin racine si besoin
sys.path.append ("src")
sys.path.append ("./")


from src.countries.spain.MercadonaV3.model.product_mercadona import ALLERGENS

def _parse_iadetailed_root_and_ts(fname: str):
    m = IAD_FILE_PAT.match(fname)
    if not m:
        return None, None
    root = m.group("root")  # ex: "Baby_food.json"
    iadts = m.group("iadts")
    dt = None
    if iadts:
        for fmt in ("%Y_%m_%d_%H_%M", "%y_%m_%d_%H_%M"):
            try:
                dt = datetime.strptime(iadts, fmt)
                break
            except:
                pass
    return root, dt

def detect_allergens(ingredients_text, ingredients_clean_text):
    allergens_found = set()
    haystack = (ingredients_text or "") + " " + (ingredients_clean_text or "")
    haystack_lower = haystack.lower()

    for allergen in ALLERGENS:
        if allergen.lower() in haystack_lower:
            allergens_found.add(allergen)

    return sorted(allergens_found)

def calculate_nutriscore_from_nested(nutrition):
    try:
        energy = nutrition.get("energies", {}).get("kj", 0)
        sugar = nutrition.get("carbohydrates", {}).get("of_which_sugars", 0)
        sat_fat = nutrition.get("fats", {}).get("saturates", 0)
        fiber = nutrition.get("fiber", 0)
        protein = nutrition.get("proteins", {}).get("proteins", 0)
        salt = nutrition.get("salt", 0)
        fruits_percent = nutrition.get("fruits_percentage", 0)

        pts_energy = min(energy // 335, 10)
        pts_sugar = min(sugar // 4.5, 10)
        pts_sat_fat = min(sat_fat // 1, 10)
        sodium = salt * 400
        pts_sodium = min(sodium // 90, 10)

        neg = pts_energy + pts_sugar + pts_sat_fat + pts_sodium
        pts_fiber = min(fiber // 0.9, 5)
        pts_protein = min(protein // 1.6, 5)

        pts_fruits = 0
        if fruits_percent >= 80:
            pts_fruits = 5
        elif fruits_percent >= 60:
            pts_fruits = 2
        elif fruits_percent >= 40:
            pts_fruits = 1

        pos = pts_fiber + pts_protein + pts_fruits
        score = neg - pos

        if score <= -1: return "A"
        elif score <= 2: return "B"
        elif score <= 10: return "C"
        elif score <= 18: return "D"
        else: return "E"
    except:
        return "N/A"

def process_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, dict):
            products = [data]
        else:
            products = data

        for product in products:
            evolutions = product.get("evolutions", [])
            if evolutions and isinstance(evolutions[0], dict):
                evo = evolutions[0]

                # Nutriscore
                nutrition = evo.get("nutrition")
                nutriscore = calculate_nutriscore_from_nested(nutrition) if nutrition else "N/A"

                # Allergens
                ingredients = evo.get("ingredients", "")
                ingredients_clean = evo.get("ingredients_clean", "")
                allergens = detect_allergens(ingredients, ingredients_clean)

                # Reconstruction
                new_evo = {}
                for key, value in evo.items():
                    if key == "ingredients_ia":
                        new_evo[key] = value
                        new_evo["allergens"] = allergens
                    elif key == "nutrition":
                        new_evo["nutri_Score"] = nutriscore
                        new_evo[key] = value
                    else:
                        new_evo[key] = value

                evolutions[0] = new_evo

        # ⚠️ ÉCRASE le fichier original
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(products if isinstance(data, list) else products[0], f, indent=4, ensure_ascii=False)

        print(f"✅ Fichier mis à jour : {filepath}")

    except Exception as e:
        print(f"❌ Erreur dans {filepath} : {e}")

def main():
    path = input("📂 Entrez le chemin du fichier ou dossier à traiter : ").strip()

    if os.path.isfile(path) and path.endswith(".json"):
        process_file(path)

    elif os.path.isdir(path):
        for dirpath, _, filenames in os.walk(path):
            latest_by_root = {}  # root.json -> (datetime, full_path)
            for fname in filenames:
                low = fname.lower()
                if not (low.endswith(".json") and "iadetailed" in low):
                    continue
                root, dt = _parse_iadetailed_root_and_ts(fname)
                if not root:
                    continue
                full = os.path.join(dirpath, fname)
                if dt is None:
                    dt = datetime.fromtimestamp(os.path.getmtime(full))  # fallback: mtime
                if root not in latest_by_root or dt > latest_by_root[root][0]:
                    latest_by_root[root] = (dt, full)

            # Ne traiter que la DERNIÈRE version iAdetailed par racine
            for _, (_, full) in latest_by_root.items():
                process_file(full)

    else:
        print("❌ Chemin invalide.")

if __name__ == "__main__":
    main()
