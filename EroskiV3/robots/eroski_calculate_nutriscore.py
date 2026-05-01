import os
import json
import sys

# Ajoutez le chemin racine pour importer votre module
sys.path.append("src")
sys.path.append("./")

# Import direct de la fonction Nutri-score depuis votre module
from src.countries.spain.EroskiV3.model.product_content_eroski import ProductContentEroski

def process_file(filepath: str):
    
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Gérer un dict unique ou une liste de dicts
        products = data if isinstance(data, list) else [data]

        for product in products:
            evolutions = product.get("evolutions", [])
            if not evolutions or not isinstance(evolutions[0], dict):
                continue

            evo = evolutions[0]

            # Calcul du Nutri-score
            nutrition = evo.get("nutrition")
            nutriscore = (
                ProductContentEroski.calculate_nutriscore_from_nested(nutrition)
                if nutrition
                else "N/A"
            )

            # Reconstruction de l'évolution sans allergènes
            new_evo = {}
            for key, value in evo.items():
                if key == "nutrition":
                    new_evo["nutriscore"] = nutriscore
                    new_evo["nutrition"] = value
                else:
                    new_evo[key] = value

            product["evolutions"][0] = new_evo

        # Écrase le fichier original avec indentation pour lisibilité
        out = products if isinstance(data, list) else products[0]
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(out, f, indent=4, ensure_ascii=False)

        print(f"✅ Fichier mis à jour : {filepath}")

    except Exception as e:
        print(f"❌ Erreur dans {filepath} : {e}")

def main():
    path = input("📂 Entrez le chemin du fichier ou dossier à traiter : ").strip()

    if os.path.isfile(path) and path.endswith(".json"):
        process_file(path)
    elif os.path.isdir(path):
        for dirpath, _, filenames in os.walk(path):
            for fname in filenames:
                if "iAdetailed" in fname and fname.endswith(".json"):
                    process_file(os.path.join(dirpath, fname))
    else:
        print("❌ Chemin invalide.")

if __name__ == "__main__":
    main()
