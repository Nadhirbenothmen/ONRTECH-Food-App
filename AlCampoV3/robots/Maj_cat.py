import json
import sys
from pathlib import Path
from collections import OrderedDict

# 📥 Demander le dossier principal
input_dir = input("📂 Entrez le chemin du dossier contenant les fichiers JSON (inclut les sous-dossiers) : ").strip()
root_folder = Path(input_dir)

# 🔁 Explorer récursivement tous les fichiers .json
for file in root_folder.rglob("*.json"):
    try:
        with open(file, "r", encoding="utf-8") as f:
            products = json.load(f)
    except Exception as e:
        print(f"❌ Erreur lecture {file.name}: {e}")
        continue

    if not isinstance(products, list):
        print(f"⚠️ Fichier ignoré (pas une liste de produits): {file.name}")
        continue

    # ✅ Vérification : au moins un produit a une catégorie
    base_categories = any(
        isinstance(product, dict) and product.get("categories") for product in products
    )
    if not base_categories:
        print(f"⛔ Aucune catégorie trouvée dans : {file.name}")
        continue

    updated_products = []

    for product in products:
        if not isinstance(product, dict):
            continue

        # 🧠 Réorganiser les clés pour placer `categories` juste après `business_type`
        new_product = OrderedDict()
        for key, value in product.items():
            new_product[key] = value
            if key == "business_type":
                # 🛠 Insérer 'categories' après 'business_type' s'il existe
                if "categories" in product:
                    new_product["categories"] = product["categories"]
        # 📌 Si 'categories' n'a jamais été ajouté, mais présent dans le produit
        if "categories" in product and "categories" not in new_product:
            new_product["categories"] = product["categories"]

        updated_products.append(new_product)

    # 💾 Réécriture du fichier JSON original
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(updated_products, f, ensure_ascii=False, indent=4)
        print(f"✅ Fichier mis à jour : {file}")
    except Exception as e:
        print(f"❌ Erreur écriture {file.name} : {e}")
