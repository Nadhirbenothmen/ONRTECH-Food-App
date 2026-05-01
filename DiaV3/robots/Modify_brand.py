import os
import json
import re

def extract_brand_from_title(title: str) -> str:
    PACKAGING_KEYWORDS = {
        "pack", "botella", "brik", "bandeja", "caja", "lata", "bolsa",
        "unidad", "x", "g", "kg", "ml", "cl", "l", "ud", "tabletas", "package"
    }
    IGNORED_WORDS = {"de", "dia", "marca", "el", "la", "los", "las"}

    if not title:
        return "Dia"

    words = re.split(r"[,\s]+", title.strip())
    words = [w for w in words if w]

    for i in range(len(words) - 1, 0, -1):
        w1 = words[i]
        w0 = words[i - 1]
        lw1 = w1.lower()
        lw0 = w0.lower()

        if lw1 in PACKAGING_KEYWORDS or lw1 in IGNORED_WORDS:
            continue

        if lw0 not in PACKAGING_KEYWORDS and lw0 not in IGNORED_WORDS:
            if w0[0].isupper() and w1[0].isupper():
                return f"{w0} {w1}"

    for word in reversed(words):
        if word and word.lower() not in PACKAGING_KEYWORDS | IGNORED_WORDS and word[0].isupper():
            return word

    return "Dia"


def process_json_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if isinstance(data, dict):
            products = [data]
            is_list = False
        elif isinstance(data, list):
            products = data
            is_list = True
        else:
            print(f"⚠️ Format non supporté dans : {filepath}")
            return

        for i in range(len(products)):
            original = products[i]
            title = original.get("lang_desc", {}).get("es", {}).get("title", "")
            brand_value = extract_brand_from_title(title) if title else "Dia"

            # Reconstruit le dictionnaire avec brand placé juste après ean
            new_product = {}
            for key, value in original.items():
                if key == "brand":
                    continue  # Supprime l'ancien
                new_product[key] = value
                if key == "ean":
                    new_product["brand"] = brand_value

            products[i] = new_product

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(products if is_list else products[0], f, indent=4, ensure_ascii=False)

        print(f"✅ Écrasé : {filepath}")

    except Exception as e:
        print(f"❌ Erreur fichier {filepath} : {e}")


def main():
    folder = input("📂 Entrez le chemin du dossier contenant les JSON : ").strip()

    if not os.path.isdir(folder):
        print(f"❌ Le dossier '{folder}' est introuvable.")
        return

    json_files = [f for f in os.listdir(folder) if f.endswith(".json")]

    if not json_files:
        print("⚠️ Aucun fichier JSON trouvé dans ce dossier.")
        return

    for filename in json_files:
        filepath = os.path.join(folder, filename)
        process_json_file(filepath)

    print("\n🎉 Tous les fichiers ont été mis à jour avec le champ 'brand'.")


if __name__ == "__main__":
    
    main()
