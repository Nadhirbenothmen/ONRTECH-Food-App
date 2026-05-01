import json
import os
import re

def normalize_key(name: str) -> str:
    name = name.strip().lower()
    name = name.replace("á", "a").replace("é", "e").replace("í", "i") \
               .replace("ó", "o").replace("ú", "u").replace("ñ", "n")

    translations = {
        "grasas": "fat",
        "acidos grasos saturados": "saturated_fat",
        "hidratos de carbono": "carbohydrates",
        "azucares": "sugars",
        "proteinas": "proteins",
        "sal": "salt",
        "fibra alimentaria": "fibra_alimentaria",
        "acido folico": "acido_folico",
        "biotina": "biotina",
        "calcio": "calcio",
        "hierro": "hierro",
        "potasio": "potasio",
        "magnesio": "magnesio",
        "manganeso": "manganeso",
        "niacina": "niacina",
        "fosforo": "fosforo",
        "acido pantotenico": "acido_pantotenico",
        "riboflavinas": "riboflavinas",
        "tiamina": "tiamina",
        "zinc": "zinc",
    }

    for key in translations:
        if key in name:
            return translations[key]

    name = re.sub(r"[^a-z0-9]+", "_", name)
    return name.strip("_")

def normalize_value(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"(\d+),(\d+)", r"\1.\2", value)  # ex: 3,5 → 3.5

    # Remplacer les unités longues par abréviations
    replacements = {
        r"kilocalor[ií]a(s)?(\s+it.*)?": "kcal",
        r"calor[ií]a(s)?(\s+it.*)?": "kcal",
        r"kilojulio(s)?": "kj",
        r"gramo(s)?": "g",
        r"miligramos?": "mg",
        r"microgramos?": "µg"
    }

    for pattern, repl in replacements.items():
        value = re.sub(pattern, repl, value, flags=re.IGNORECASE)

    # Extraire valeur propre : nombre + unité
    match = re.search(r"(\d+(?:\.\d+)?)\s*(kcal|kj|g|mg|µg)", value)
    if match:
        return f"{match.group(1)} {match.group(2)}"

    return value

def parse_nutriscore_to_dict(text: str) -> dict:
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    facts = {}

    for line in lines:
        if re.search(r"cantidad\s+100\s+gramos", line.lower()):
            continue  # Ignore "Cantidad 100 gramos"

        match = re.match(r"(.+?)\s+([\d,\.]+\s*[\wµ]+.*)", line)
        if not match:
            continue

        key_raw = match.group(1).strip().lower()
        val_raw = match.group(2).strip().lower()

        # Forcer energy_kcal ou energy_kj selon la valeur
        if "kilojulio" in val_raw or "kj" in val_raw:
            key = "energy_kj"
        elif "kcal" in val_raw or "caloria" in val_raw or "caloría" in val_raw:
            key = "energy_kcal"
        else:
            key = normalize_key(key_raw)

        val = normalize_value(val_raw)
        facts[key] = val

    return facts

def process_file(file_path: str):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        products = [data] if isinstance(data, dict) else data if isinstance(data, list) else None
        if not products:
            print(f"❌ Format non reconnu dans {file_path}.")
            return

        for product in products:
            for evo in product.get("evolutions", []):
                if "nutriscore" in evo:
                    raw = evo.pop("nutriscore")
                    evo["nutrition_facts"] = parse_nutriscore_to_dict(raw)

        folder, filename = os.path.split(file_path)
        output_path = os.path.join(folder, "corrige_" + filename)

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(products if isinstance(data, list) else products[0], f, indent=4, ensure_ascii=False)

        print(f"✅ Fichier corrigé : {output_path}")

    except Exception as e:
        print(f"❌ Erreur avec {file_path}: {e}")

def main():
    folder = input("Entrez le chemin du dossier contenant les fichiers à corriger : ").strip()
    if not os.path.isdir(folder):
        print(f"❌ Dossier non trouvé : {folder}")
        return

    for dirpath, _, filenames in os.walk(folder):
        for file in filenames:
            if file.endswith(".json"):
                process_file(os.path.join(dirpath, file))

    print("\n✅ Tous les fichiers ont été traités.")

if __name__ == "__main__":
    main()
