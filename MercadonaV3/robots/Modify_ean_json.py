import json
import os
from collections import OrderedDict

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Gestion liste ou objet unique
        if isinstance(data, dict):
            products = [data]
        elif isinstance(data, list):
            products = data
        else:
            print(f"❌ Format non reconnu dans {file_path}.")
            return

        new_products = []

        for product in products:
            if "id" in product:
                product["ean"] = product.pop("id")  # Remplacer id par ean

            # Créer un OrderedDict pour forcer l'ordre : ean en premier
            ordered_product = OrderedDict()
            if "ean" in product:
                ordered_product["ean"] = product["ean"]
            for key, value in product.items():
                if key != "ean":  # Le reste après
                    ordered_product[key] = value

            new_products.append(ordered_product)

        # Nouveau fichier corrigé
        folder, filename = os.path.split(file_path)
        new_filename = "corrige_" + filename
        output_path = os.path.join(folder, new_filename)

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(new_products if isinstance(data, list) else new_products[0], f, indent=4, ensure_ascii=False)

        print(f"✅ Corrigé : {output_path}")

    except Exception as e:
        print(f"❌ Erreur avec {file_path}: {e}")

def main():
    folder_to_process = input("Entrez le chemin du dossier contenant les JSON à corriger : ").strip()

    if not os.path.isdir(folder_to_process):
        print(f"❌ Le dossier '{folder_to_process}' n'existe pas.")
        return

    for dirpath, dirnames, filenames in os.walk(folder_to_process):
        for filename in filenames:
            if filename.endswith(".json"):
                file_path = os.path.join(dirpath, filename)
                process_file(file_path)

    print("\n✅ Correction terminée pour tous les fichiers du dossier.")

if __name__ == "__main__":
    main()
