from pathlib import Path
import json
import sys
import re

def extract_brand_from_title(title: str) -> str:
    words = title.strip().split()
    brand_words = []
    for word in words:
        if word.isupper():
            brand_words.append(word)
        else:
            break
    return " ".join(brand_words).strip()

def extract_full_format_from_title(title: str) -> str | None:
    title = title.lower()
    title = title.replace("×", "x").replace("*", "x").replace(",", ".").replace("·", " ").strip()

    # Corriger "malla3kg", "bandeja8uds", etc.
    title = re.sub(r'([a-záéíóúñü]+)(\d+)([a-záéíóúñü]+)', r'\1 \2 \3', title)
    title = re.sub(r'([a-záéíóúñü]+)(\d+)', r'\1 \2', title)
    title = re.sub(r'(\d+)([a-záéíóúñü]+)', r'\1 \2', title)

    patterns = [
        # ✅ Prioritaire : "pack de 6 unidades de 20 g"
        r'\bpack de\s*\d+\s*(?:uds\.?|unidades?)\s*de\s*\d+[.,]?\d*\s*(?:g|gr|gramos|kg|ml|cl|l)\b',

        # Autres formats combinés
        r'\b\d+\s*(?:uds\.?|unidades?)\s*[.,]?\s*\d+[.,]?\d*\s*(?:g|gr|gramos|kg|ml|cl|l)\b',
        r'\b\d+\s*(?:ud\.?|uds\.?|unidades?)\s+\d+[.,]?\d*\s*(?:g|gr|gramos|kg|ml|cl|l)\b',
        r'\b\d+\s*(?:uds\.?|unidades?)\s+\d+[.,]?\d*\s*(?:g|gr\.?|gramos|kg|ml|cl|l)\b',

        r'\b\d+\s*(?:uds\.?|unidades?)\b',
        r'\bpack de\s*\d+\s+(?:latas|botellas|bricks|tarros)\s+(?:de\s*)?\d+[.,]?\d*\s*(?:g|gr|gramos|kg|ml|cl|l)\b',
        r'\bpack\s+\d+\s*(?:uds\.?|unidades?)\s*x\s*\d+[.,]?\d*\s*(?:g|gr|gramos|kg|ml|cl|l)\b',
        r'\bpack\s+\d+\s+(?:latas|botellas|bricks|tarros)\s*x\s*\d+[.,]?\d*\s*(?:g|gr|gramos|kg|ml|cl|l)\b',
        r'\b\d+\s+(?:latas|botellas|bricks|tarros)\s*x\s*\d+[.,]?\d*\s*(?:g|gr|gramos|kg|ml|cl|l)\b',
        r'\b(?:botella|lata|brick|brik|tarro|paquete|pack)\s*(?:de\s*)?\d+[.,]?\d*\s*(?:g|gr|gramos|kg|ml|cl|l)\b',
        r'\b\d+\s*(?:uds\.?|unidades?)\s+\d+[.,]?\d*\s*(?:g|gr|gramos|kg|ml|cl|l)\b',
        r'\b\d+\s*(?:uds\.?|unidades?)\s*x\s*\d+[.,]?\d*\s*(?:g|gr|gramos|kg|ml|cl|l)\b',
        r'\b\d+\s*x\s*\d+[.,]?\d*\s*(?:g|gr|gramos|kg|ml|cl|l)\b',
        r'\b(?:bolsa|cup|brik|botella|lata|tarro|paquete|pack|bandeja|tarrina|malla)\s*(?:de\s*)?\d+[.,]?\d*\s*(?:g|gr|gramos|kg|ml|cl|l)\b',
        r'\b\d+[.,]?\d*\s*(?:g|gr|gramos|kg|ml|cl|l)\b.*?(?:pack|paquete|lot[e]?)\s*de\s*\d+\s*(?:uds\.?|unidades?)',
        r'\b\d+[.,]?\d*\s*(?:g|gr|gramos|kg|ml|cl|l)\b',
]


    matches = []
    seen = set()

    for pattern in patterns:
        for match in re.finditer(pattern, title):
            val = match.group(0).strip()
            if val not in seen:
                seen.add(val)
                matches.append(val)
        if matches:
            break  # 🛑 On s'arrête au premier pattern qui matche

    return " ".join(matches) if matches else None




def calculate_nutriscore_from_nested(nutrition: dict) -> str:
    try:
        energy_kj = nutrition.get("energies", {}).get("kj", 0)
        carbs = nutrition.get("carbohydrates", {})
        sugars_g = carbs.get("of_which_sugars") or carbs.get("sugars") or 0
        satfat_g = nutrition.get("fats", {}).get("saturates", 0)
        fiber_g = carbs.get("fiber") or carbs.get("dietary_fiber") or 0
        protein_g = nutrition.get("proteins", {}).get("proteins", 0)
        salt_mg = nutrition.get("minerals", {}).get("salt", 0)
        fruits_percentage = nutrition.get("fruits_percentage", 0)

        def to_float(v): return float(str(v).replace(",", ".").split()[0]) if isinstance(v, str) else float(v or 0)

        energy_kj = to_float(energy_kj)
        sugars_g = to_float(sugars_g)
        satfat_g = to_float(satfat_g)
        fiber_g = to_float(fiber_g)
        protein_g = to_float(protein_g)
        salt_mg = to_float(salt_mg)
        fruits_percentage = to_float(fruits_percentage)

        pts_energy = min(int(energy_kj / 335), 10)
        pts_sugar = min(int(sugars_g / 4.5), 10)
        pts_satfat = min(int(satfat_g / 1), 10)
        pts_salt = min(int((salt_mg / 1000.0) / 0.09), 10)
        neg = pts_energy + pts_sugar + pts_satfat + pts_salt

        pts_fiber = min(int(fiber_g / 0.9), 5)
        pts_protein = min(int(protein_g / 1.6), 5)
        if fruits_percentage >= 80:
            pts_fruits = 5
        elif fruits_percentage >= 60:
            pts_fruits = 2
        elif fruits_percentage >= 40:
            pts_fruits = 1
        else:
            pts_fruits = 0
        pos = pts_fiber + pts_protein + pts_fruits

        score = neg - pos

        if score <= -1: return "A"
        elif score <= 2: return "B"
        elif score <= 10: return "C"
        elif score <= 18: return "D"
        else: return "E"
    except Exception as e:
        print(f"❌ NutriScore exception: {e}")
        return "N/A"

def update_json_file(filepath: Path):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        modified = False

        for product in data:
            title = product.get("lang_desc", {}).get("es", {}).get("title", "")
            current_brand = product.get("brand", "").strip().upper()

            # 🚫 Si la marque AUCHAN est détectée dans le champ brand ou dans le titre → remplacer
            if current_brand == "AUCHAN" or "AUCHAN" in title.upper():
                if current_brand != "PRODUCTO ALCAMPO":
                    print(f"🔁 Brand remplacé (AUCHAN détecté) → 'PRODUCTO ALCAMPO' dans : {title}")
                    product["brand"] = "PRODUCTO ALCAMPO"
                    modified = True
                continue  # Skip brand extraction, we've forced it

            # ✅ Si la marque est vide ou absente → fallback par défaut
            if not current_brand:
                print(f"⚠️ Marque absente → défaut : 'PRODUCTO ALCAMPO' dans : {title}")
                product["brand"] = "PRODUCTO ALCAMPO"
                modified = True
                continue

            # 🧠 Sinon, extraire depuis le titre
            if title:
                extracted_brand = extract_brand_from_title(title)
                if extracted_brand and extracted_brand != current_brand:
                    print(f"✅ Brand extrait : {extracted_brand} → remplacé ancien : {current_brand}")
                    product["brand"] = extracted_brand
                    modified = True





            evolutions = product.get("evolutions", [])
            for evo in evolutions:
                # Nutri-Score
                nutrition = evo.get("nutrition")
                if nutrition:
                    new_score = calculate_nutriscore_from_nested(nutrition)
                    evo["nutri_Score"] = new_score
                    modified = True

                # Format
                if title:
                    extracted_format = extract_full_format_from_title(title)
                    if extracted_format:
                        current_format = evo.get("format")
                        print(f"\n[🔎 Titre] {title}")
                        print(f"[➡️ Format extrait] {extracted_format}")
                        print(f"[📦 Format actuel]  {current_format}")

                        if current_format != extracted_format:
                            print(f"🔁 Mise à jour du format : '{current_format}' → '{extracted_format}'")

                            # Supprimer ancien format
                            evo.pop("format", None)

                            # Reconstruction avec format après parsing_date
                            new_evo = {}
                            inserted = False

                            for key, value in evo.items():
                                new_evo[key] = value
                                if key == "parsing_date":
                                    new_evo["format"] = extracted_format
                                    inserted = True

                            if not inserted:
                                # Si pas de parsing_date, mettre format au début
                                new_evo = {"format": extracted_format, **new_evo}

                            evo.clear()
                            evo.update(new_evo)
                            modified = True


        if modified:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"✅ Mis à jour : {filepath}")
        else:
            print(f"ℹ️ Aucune modification : {filepath}")

    except Exception as e:
        print(f"❌ Erreur fichier {filepath}: {e}")

def process_input(path: str):
    path_obj = Path(path)
    if path_obj.is_file() and path_obj.suffix == ".json":
        update_json_file(path_obj)
    elif path_obj.is_dir():
        json_files = list(path_obj.rglob("*.json"))
        print(f"🔍 {len(json_files)} fichiers trouvés dans {path}")
        for file in json_files:
            update_json_file(file)
    else:
        print(f"❌ Chemin invalide : {path}")

# --- Entrée depuis le terminal ---
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("❌ Usage : python update_products.py <chemin/fichier.json|dossier>")
        sys.exit(1)

    input_path = sys.argv[1]
    process_input(input_path)
