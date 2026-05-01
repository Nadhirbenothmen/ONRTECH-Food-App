import json
import os

def map_spanish_nutrition(name: str) -> str:
    """Convertit un nom nutritionnel espagnol vers une clé normalisée"""
    name = name.lower()
    if "valor energético" in name and "kj" in name:
        return "energy_kj"
    if "valor energético" in name and "kcal" in name:
        return "energy_kcal"
    if "grasas" == name:
        return "fat"
    if "saturadas" in name:
        return "saturated_fat"
    if "hidratos de carbono" in name:
        return "carbohydrates"
    if "azúcares" in name:
        return "sugars"
    if "proteínas" in name:
        return "proteins"
    if "sal" in name:
        return "salt"
    if "por" in name:
        return "por"
    return name.replace(" ", "_")

def parse_nutriscore_to_dict(text):
    """Transforme le bloc de texte brut en dictionnaire nutrition_facts"""
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    facts = {}
    i = 0
    while i < len(lines) - 1:
        key_raw = lines[i]
        val = lines[i + 1]
        key = map_spanish_nutrition(key_raw)
        facts[key] = val
        i += 2
    return facts

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if isinstance(data, dict):
            products = [data]
        elif isinstance(data, list):
            products = data
        else:
            print(f"❌ Format non reconnu dans {file_path}.")
            return

        for product in products:
            for evo in product.get("evolutions", []):
                if "nutriscore" in evo:
                    raw = evo.pop("nutriscore")
                    nutrition_facts = parse_nutriscore_to_dict(raw)
                    evo["nutrition_facts"] = nutrition_facts

        # Sauvegarde fichier corrigé
        folder, filename = os.path.split(file_path)
        new_filename = "corrige_" + filename
        output_path = os.path.join(folder, new_filename)

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(products if isinstance(data, list) else products[0], f, indent=4, ensure_ascii=False)

        print(f"✅ Fichier corrigé : {output_path}")

    except Exception as e:
        print(f"❌ Erreur avec {file_path}:")

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

