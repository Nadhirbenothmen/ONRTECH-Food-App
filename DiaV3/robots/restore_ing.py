import os
import json

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def restore_fields(brut_path, enriched_path):
    brut_data = load_json(brut_path)
    enriched_data = load_json(enriched_path)

    brut_list = brut_data if isinstance(brut_data, list) else [brut_data]
    enriched_list = enriched_data if isinstance(enriched_data, list) else [enriched_data]

    # Map EAN -> ingrédients du brut
    brut_map = {}
    for b in brut_list:
        ean = b.get("ean")
        evo = (b.get("evolutions") or [{}])[0]
        if ean:
            brut_map[ean] = evo.get("ingredients")

    modified = False
    restored_count = 0
    skipped_count = 0

    for e in enriched_list:
        ean = e.get("ean")
        if ean in brut_map:
            evo = e.setdefault("evolutions", [{}])[0]

            new_ing = brut_map[ean]
            if new_ing is not None and evo.get("ingredients") != new_ing:
                print(f"{os.path.basename(enriched_path)} | EAN {ean}: ingredients restaurés")
                evo["ingredients"] = new_ing
                modified = True
                restored_count += 1
        else:
            print(f"⚠ Aucun produit brut trouvé pour EAN {ean} dans {os.path.basename(enriched_path)}")
            skipped_count += 1

    if modified:
        save_json(enriched_path, enriched_data)
        print(f"✔ Fichier mis à jour: {enriched_path}")
    else:
        print(f"✅ Aucun changement pour {os.path.basename(enriched_path)}")

    return restored_count, skipped_count


def find_matching_file(given_file, folder):
    """Trouve le fichier pair (brut <-> iAdetailed) basé sur la base commune du nom."""
    fname = os.path.basename(given_file)

    if "iadetailed" in fname.lower():
        # Cas enrichi → chercher brut
        base = fname.split("_iAdetailed")[0]
        for f in os.listdir(folder):
            if f.startswith(base) and "iadetailed" not in f.lower():
                return os.path.join(folder, f), given_file

    else:
        # Cas brut → chercher enrichi
        base = fname.replace(".json", "")
        for f in os.listdir(folder):
            if f.startswith(base) and "iadetailed" in f.lower():
                return given_file, os.path.join(folder, f)

    return None, None


if __name__ == "__main__":
    target = input("👉 Entrez le chemin d’un fichier JSON ou d’un dossier: ").strip()

    total_restored = 0
    total_skipped = 0

    if os.path.isdir(target):
        for dirpath, _, files in os.walk(target):
            for f in files:
                if f.endswith(".json") and "iadetailed" in f.lower():
                    enriched_path = os.path.join(dirpath, f)
                    brut_path, enriched = find_matching_file(enriched_path, dirpath)
                    if brut_path and os.path.isfile(brut_path):
                        r, s = restore_fields(brut_path, enriched)
                        total_restored += r
                        total_skipped += s
                    else:
                        print(f"⚠ Pas de brut trouvé pour {f}")

    elif os.path.isfile(target):
        folder = os.path.dirname(target)
        brut, enriched = find_matching_file(target, folder)
        if brut and enriched and os.path.isfile(brut) and os.path.isfile(enriched):
            r, s = restore_fields(brut, enriched)
            total_restored += r
            total_skipped += s
        else:
            print(f"⚠ Impossible de trouver le fichier correspondant pour {target}")

    else:
        print("⚠ Merci de donner un chemin valide (fichier ou dossier)")

    print("\n📊 Rapport final:")
    print(f"   Ingrédients restaurés : {total_restored}")
    print(f"   Produits ignorés : {total_skipped}")
