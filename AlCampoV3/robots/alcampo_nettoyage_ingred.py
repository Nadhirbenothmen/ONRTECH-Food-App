import os
import json
import re
from collections import OrderedDict

def nettoyer_ingredients(text):
    if not text:
        return ""

    text = text.lower()

    # Supprimer le préfixe "ingredientes:"
    text = re.sub(r"^ingredientes\s*:\s*", "", text)

    # Supprimer les pourcentages et mentions techniques (ex: % M.G., % en gras)
    text = re.sub(r"\(?\d+[\d\s,.]*\s*%[^,)]*\)?", "", text)

    # Supprimer les additifs (ex: E-472c)
    text = re.sub(r"\be[-–—]?\s?\d+[a-z]*", "", text)

    # Supprimer les noms scientifiques trop techniques (ex: fosfato tricálcico) uniquement dans les sous-listes
    text = re.sub(r"\(([^()]*?(fosfato|sulfato|cloruro|pirofosfato|yodato|carbonato)[^()]*)\)", "", text)

    # Supprimer mentions type "puede contener..."
    text = re.sub(r"¿?puede contener.*", "", text)

    # Nettoyage final ponctuation
    text = text.replace(";", "")
    text = text.replace(" .", ".").replace(".", "")
    text = re.sub(r"\s{2,}", " ", text).strip()

    # Nettoyage parenthèses vides
    text = re.sub(r"\(\s*\)", "", text)

    # Nettoyage des virgules orphelines
    text = re.sub(r",\s*,", ", ", text)
    text = re.sub(r",\s*$", "", text)

    return text


# 📥 Saisie du dossier à traiter
input_folder = input("📂 Entrez le chemin du dossier contenant les fichiers JSON : ").strip()

if not os.path.isdir(input_folder):
    print(f"❌ Le dossier '{input_folder}' n'existe pas.")
    exit(1)

# 🔁 Traitement des fichiers .json
for filename in os.listdir(input_folder):
    if filename.endswith(".json") and "_cleaned" not in filename:
        input_path = os.path.join(input_folder, filename)
        output_filename = filename.replace(".json", "_cleaned.json")
        output_path = os.path.join(input_folder, output_filename)

        try:
            with open(input_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            for product in data:
                new_evolutions = []
                for evo in product.get("evolutions", []):
                    cleaned = nettoyer_ingredients(evo.get("ingredients", ""))
                    new_evo = OrderedDict()

                    for key, value in evo.items():
                        if key == "allergens":
                            # ➕ Insertion avant "allergens"
                            new_evo["ingredients_clean"] = cleaned
                        new_evo[key] = value

                    new_evolutions.append(new_evo)

                product["evolutions"] = new_evolutions

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

            print(f"✅ Fichier nettoyé : {output_filename}")
        except Exception as e:
            print(f"⚠️ Erreur dans {filename} : {e}")
