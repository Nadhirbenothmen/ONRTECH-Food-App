
import json
import os

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

        for product in products:
            extre_data = product.get("extre_data", {})
            nutrition_facts = extre_data.pop("nutrition_facts", None)  # Retirer nutrition_facts proprement

            if nutrition_facts is not None:
                # Toujours déplacer nutrition_facts (même vide)
                if "evolutions" not in product or not product["evolutions"]:
                    product["evolutions"] = [{}]
                product["evolutions"][0]["nutrition_facts"] = nutrition_facts

        # Nouveau fichier corrigé
        folder, filename = os.path.split(file_path)
        new_filename = "corrige_" + filename
        output_path = os.path.join(folder, new_filename)

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data if isinstance(data, list) else data, f, indent=4, ensure_ascii=False)

        print(f"✅ Corrigé : {output_path}")

    except Exception as e:
        print(f"❌ Erreur avec {file_path}: {e}")

def main():
    folder_to_process = input("Entrez le chemin du dossier contenant les JSON à corriger (ex: products/Baby_Infant_nutrition) : ").strip()

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
