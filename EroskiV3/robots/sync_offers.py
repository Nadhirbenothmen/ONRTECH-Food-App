#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json

def sync_offers(brut_path: str):
    folder = os.path.dirname(brut_path)
    base = os.path.basename(brut_path).replace(".json", "")

    # chercher le fichier iAdetailed correspondant (peut avoir un suffixe timestamp)
    candidates = [f for f in os.listdir(folder) if f.startswith(base + "_iAdetailed")]
    if not candidates:
        print(f"⚠️ Aucun iAdetailed trouvé pour {brut_path}")
        return

    detailed_path = os.path.join(folder, candidates[0])

    # charger brut et iAdetailed
    with open(brut_path, "r", encoding="utf-8") as f:
        brut = json.load(f)
    with open(detailed_path, "r", encoding="utf-8") as f:
        detailed = json.load(f)

    def inject_offers(brut_data, detailed_data):
        # cas produit unique
        if isinstance(brut_data, dict) and isinstance(detailed_data, dict):
            if brut_data.get("ean") == detailed_data.get("ean"):
                for evo_b, evo_d in zip(brut_data.get("evolutions", []),
                                        detailed_data.get("evolutions", [])):
                    if "offers" in evo_b:
                        evo_d["offers"] = evo_b["offers"]
                        print(f"📦 offers copié pour produit EAN {brut_data.get('ean')}")

        # cas liste de produits
        elif isinstance(brut_data, list) and isinstance(detailed_data, list):
            brut_index = {p.get("ean"): p for p in brut_data}
            for det in detailed_data:
                ean = det.get("ean")
                if ean in brut_index:
                    evo_brut = brut_index[ean].get("evolutions", [])
                    evo_det = det.get("evolutions", [])
                    for evo_b, evo_d in zip(evo_brut, evo_det):
                        if "offers" in evo_b:
                            evo_d["offers"] = evo_b["offers"]
                            print(f"📦 offers copié pour produit EAN {ean}")

    inject_offers(brut, detailed)

    # sauver le iAdetailed mis à jour
    with open(detailed_path, "w", encoding="utf-8") as f:
        json.dump(detailed, f, indent=4, ensure_ascii=False)

    print(f"✅ offers synchronisés depuis {brut_path} → {detailed_path}")


def process_folder(folder: str):
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".json") and "iAdetailed" not in file:
                brut_path = os.path.join(root, file)
                sync_offers(brut_path)


def main():
    path = input("👉 Entrez le chemin d'un fichier brut (.json) ou d'un dossier : ").strip()
    if os.path.isfile(path):
        sync_offers(path)
    elif os.path.isdir(path):
        process_folder(path)
    else:
        print("❌ Chemin invalide ou fichier introuvable")


if __name__ == "__main__":
    main()
