#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os

def clean_node(node):
    """
    Copie un nœud en :
      - gardant toujours 'id' et 'label'
      - reconstruisant récursivement 'subs' si non vide
      - supprimant la clé 'subs' si la liste résultante est vide
    """
    cleaned = {
        "id": node["id"],
        "label": node["label"]
    }

    children = [clean_node(child) for child in node.get("subs", [])]
    if children:
        # nœud intermédiaire : on remet la liste de enfants
        cleaned["subs"] = children
    # sinon, on n'ajoute pas la clé "subs" -> niveau feuille

    return cleaned

def main():
    input_path = input("Chemin vers le JSON d'entrée : ").strip()
    if not os.path.isfile(input_path):
        print(f"❌ Le fichier '{input_path}' n’existe pas.")
        return

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # on nettoie tout l’arbre
    result = clean_node(data)

    base, ext = os.path.splitext(input_path)
    output_path = f"{base}_final.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    print(f"✅ JSON sans 'subs': [] écrit dans : {output_path}")

if __name__ == "__main__":
    main()
