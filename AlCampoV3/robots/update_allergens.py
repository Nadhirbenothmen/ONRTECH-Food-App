#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import re

# --- Liste d'allergènes ---
ALLERGENS = {
    "cacahuete": ["cacahuete", "cacahuète", "peanut"],
    "apio": ["apio", "céleri", "celery"],
    "crustáceos": ["crustáceos", "crustacés", "crustaceans"],
    "cangrejo": ["cangrejo", "crabe", "crab"],
    "gamba": ["gamba", "crevette", "shrimp"],
    "cigala": ["cigala", "langoustine", "scampi"],
    "langosta": ["langosta", "homard", "lobster"],
    "langostino": ["langostino", "grosse crevette", "prawn"],

    "avena": ["avena", "avoine", "oat"],
    "trigo": ["trigo", "blé", "wheat"],
    "espelta": ["espelta", "épeautre", "spelt"],
    "kamut y sus cepas híbridas": ["kamut y sus cepas híbridas", "kamut", "kamut wheat"],
    "cebada": ["cebada", "orge", "barley"],
    "centeno": ["centeno", "seigle", "rye"],

    "frutos de cáscara": ["frutos de cáscara", "fruits à coque", "tree nuts"],
    "almendra": ["almendra", "amande", "almond"],
    "avellana": ["avellana", "noisette", "hazelnut"],
    "nuez": ["nuez", "noix", "walnut"],
    "nuez de brasil": ["nuez de brasil", "noix du brésil", "brazil nut"],
    "anacardo": ["anacardo", "noix de cajou", "cashew"],
    "nuez de macadamia": ["nuez de macadamia", "noix de macadamia", "macadamia nut"],
    "nuez de pecán": ["nuez de pecán", "noix de pécan", "pecan"],
    "nuez de queensland": ["nuez de queensland", "noix de queensland", "queensland nut"],
    "pistacho": ["pistacho", "pistache", "pistachio"],

    "leche": ["leche", "lait", "milk"],
    "altramuces": ["altramuces", "lupin"],
    "huevo": ["huevo", "œuf", "egg"],
    "pescado": ["pescado", "poisson", "fish"],
    "lactosa": ["lactosa", "lactose"],
    "gluten": ["gluten"],

    "caracol de mar (búzio)": ["caracol de mar (búzio)", "bigorneau", "whelk"],
    "calamar": ["calamar", "calamar", "squid"],
    "caracol": ["caracol", "escargot", "snail"],
    "ostra": ["ostra", "huître", "oyster"],
    "mejillón": ["mejillón", "moule", "mussel"],
    "almeja": ["almeja", "palourde", "clam"],
    "vieira": ["vieira", "coquille saint-jacques", "scallop"],
    "pulpo": ["pulpo", "poulpe", "octopus"],

    "mostaza": ["mostaza", "moutarde", "mustard"],
    "sésamo": ["sésamo", "sésame", "sesame"],
    "soja": ["soja", "soya", "soy"],
    "sulfitos": ["sulfitos", "sulfites"],

    "lupin": ["lupin", "lupin", "lupine"],
    "celery": ["celery", "céleri", "apio"],  # déjà couvert par "apio", mais laissé pour compatibilité
}


# Prépare les regex insensibles à la casse
ALLERGENS_PATTERNS = [(a, re.compile(rf"\b{re.escape(a)}\b", re.IGNORECASE)) for a in ALLERGENS]

def detect_allergens(*texts: str):
    found = set()
    for text in texts:
        if not text or not isinstance(text, str):
            continue
        t = text.lower()
        for es_allergen, variants in ALLERGENS.items():
            for v in variants:
                if re.search(rf"\b{re.escape(v.lower())}\b", t, re.IGNORECASE):
                    found.add(es_allergen)  # stocké en espagnol
                    break
    return sorted(found)



def update_file(file_path: str):
    """Met à jour le champ allergens dans un fichier JSON produit."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Erreur lecture {file_path}: {e}")
        return

    changed = False

    def process_product(prod):
        nonlocal changed
        # Extraire title/desc de toutes les langues
        titles_descs = []
        if isinstance(prod.get("lang_desc"), dict):
            for _, d in prod["lang_desc"].items():
                if isinstance(d, dict):
                    titles_descs.append(d.get("title", ""))
                    titles_descs.append(d.get("desc", ""))

        if "evolutions" in prod:
            for evo in prod["evolutions"]:
                ing = evo.get("ingredients", "")
                allergens = detect_allergens(ing, *titles_descs)
                if allergens:
                    if evo.get("allergens") != allergens:
                        evo["allergens"] = allergens
                        changed = True

    if isinstance(data, list):
        for p in data:
            process_product(p)
    elif isinstance(data, dict):
        process_product(data)

    if changed:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"✅ Allergènes mis à jour dans {file_path}")
    else:
        print(f"ℹ️ Aucun changement dans {file_path}")


if __name__ == "__main__":
    path = input("📂 Entrez le chemin d’un dossier ou d’un fichier JSON : ").strip()

    if os.path.isdir(path):
        for root, _, files in os.walk(path):
            for fname in files:
                if fname.endswith(".json") and "iAdetailed" in fname:
                    update_file(os.path.join(root, fname))
    elif os.path.isfile(path):
        if path.endswith(".json") and "iAdetailed" in os.path.basename(path):
            update_file(path)
        else:
            print("⚠️ Le fichier doit être un .json contenant 'iAdetailed' dans son nom.")
    else:
        print("❌ Chemin invalide")
