#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import re
import time
from datetime import datetime
from collections import OrderedDict
from pathlib import Path
from googletrans import Translator  # utilisation d'un service de traduction

translator = Translator()

# --- Cache de traduction ---
CACHE_FILE = Path('eroski_translation_cache.json')
try:
    with CACHE_FILE.open('r', encoding='utf-8') as cf:
        TRANSLATION_CACHE = json.load(cf)
except Exception:
    TRANSLATION_CACHE = {}


def save_cache():
    try:
        with CACHE_FILE.open('w', encoding='utf-8') as cf:
            json.dump(TRANSLATION_CACHE, cf, ensure_ascii=False, indent=2)
    except Exception:
        pass


def extract_format_from_title(title):
    """
    Tente d'extraire un format depuis le titre, en cherchant différents motifs de format.
    """
    patterns = [
        r"(pack\s*\d+x?\d*\s*(?:g|ml|cl))",
        r"(doypack\s*\d+\s*(?:g|ml|cl))",
        r"(bolsita\s*\d+\s*(?:g|ml|cl))",
        r"(sachet\s*\d+\s*(?:g|ml|cl))",
        r"(bote\s*\d+\s*(?:g|ml|cl))",
        r"(lata\s*\d+\s*(?:g|ml|cl))",
        r"(botella\s*\d+\s*(?:g|ml|cl))",
        r"(\d+\s*(?:g|ml|cl))"
    ]
    lower = title.lower()
    for pat in patterns:
        m = re.search(pat, lower)
        if m:
            return m.group(1)
    if "," in title:
        return title.rsplit(",", 1)[1].strip()
    return None


def fill_missing_formats(data):
    updated = []
    for obj in data:
        ean = obj.get("ean", "<sans-ean>")
        title = obj.get("lang_desc", {}).get("es", {}).get("title", "")
        suggestion = extract_format_from_title(title)
        for evo in obj.get("evolutions", []):
            if not evo.get("format") and suggestion:
                evo["format"] = suggestion
                updated.append(ean)
    return updated


def clean_ingredients_fields(data):
    """
    Nettoie les champs ingredients_clean et ingredients_ia en ne gardant que des ingrédients de base
    et traduit les ingrédients IA en anglais via le traducteur avec cache.
    """
    stopwords = set([
        "ingredientes", "puede", "contener", "y", "de", "con", "en",
        "la", "el", "los", "las", "del", "al", "que", "etc",
        "zumo", "vitamina", "c", "agua", "aceite", "polvo", "formula",
        "puré", "fruta", "a", "partir", "proporción", "variable"
    ])
    for obj in data:
        for evo in obj.get("evolutions", []):
            # nettoyage ingredients_clean
            raw = evo.get("ingredients_clean", "")
            parts = re.split(r"[\[\],()]+", raw)
            words = []
            for part in parts:
                w = part.strip().lower()
                if not w or w in stopwords or re.search(r"\d", w):
                    continue
                for token in w.split():
                    tk = token.strip().lower().strip(':')
                    if tk and tk not in stopwords:
                        words.append(tk)
            unique_clean = []
            for w in words:
                if w not in unique_clean:
                    unique_clean.append(w)
            evo["ingredients_clean"] = ", ".join(unique_clean)

            # nettoyage et traduction ingredients_ia
            ia_list = evo.get("ingredients_ia", [])
            cleaned_ia = []
            for item in ia_list:
                w = item.strip().lower()
                if re.match(r'^[a-záéíóúüñ]+$', w) and w not in stopwords:
                    if w in TRANSLATION_CACHE:
                        tr_text = TRANSLATION_CACHE[w]
                    else:
                        try:
                            tr_text = translator.translate(w, src='es', dest='en').text.lower().strip()
                        except Exception:
                            tr_text = w
                        TRANSLATION_CACHE[w] = tr_text
                    if tr_text not in cleaned_ia:
                        cleaned_ia.append(tr_text)
            evo["ingredients_ia"] = cleaned_ia
    # sauvegarde cache après nettoyage
    save_cache()


def reorder_evolutions(data):
    evo_order = [
        "parsing_date", "format", "availability", "nutriscore", "nutrition",
        "ingredients", "ingredients_clean", "ingredients_ia", "allergens",
        "reviews", "weight_per_packaging", "price_per_packaging", "price_per_unit"
    ]
    for obj in data:
        new_list = []
        for evo in obj.get("evolutions", []):
            ordered = OrderedDict()
            for key in evo_order:
                if key in evo:
                    ordered[key] = evo[key]
            for k, v in evo.items():
                if k not in ordered:
                    ordered[k] = v
            new_list.append(ordered)
        obj["evolutions"] = new_list


def set_measure_units(data):
    for obj in data:
        raw = obj.get("matter")
        matter = raw.upper() if isinstance(raw, str) and raw.strip() else "OTHER"
        if matter == "SUBSTANCE":
            obj["mesure_unit_for_packaging"] = "g"
            obj["mesure_unit_for_price_per_unit"] = "kg"
        elif matter == "LIQUID":
            obj["mesure_unit_for_packaging"] = "ml"
            obj["mesure_unit_for_price_per_unit"] = "l"
        elif matter == "PIECE":
            obj["mesure_unit_for_packaging"] = "piece"
            obj["mesure_unit_for_price_per_unit"] = "piece"
        else:
            obj["mesure_unit_for_packaging"] = "-"
            obj["mesure_unit_for_price_per_unit"] = "-"


def reorder_product_keys(data):
    desired_order = [
        "ean", "brand", "business_type", "categories", "origin", "matter",
        "market", "lang_desc", "evolutions",
        "mesure_unit_for_packaging", "mesure_unit_for_price_per_unit",
        "label", "created_at", "updated_at", "parsing_duration"
    ]
    new_data = []
    for obj in data:
        ordered = OrderedDict()
        for key in desired_order:
            if key in obj:
                ordered[key] = obj[key]
        for k, v in obj.items():
            if k not in ordered:
                ordered[k] = v
        new_data.append(ordered)
    return new_data


def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not isinstance(data, list):
        print(f"{path} n’est pas une liste JSON.")
        return

    modified_eans = fill_missing_formats(data)
    clean_ingredients_fields(data)
    reorder_evolutions(data)
    set_measure_units(data)
    data = reorder_product_keys(data)

    dirname = os.path.dirname(path)
    stem, ext = os.path.splitext(os.path.basename(path))
    clean_stem = re.sub(r'(_\d{8}_\d{6})$', '', stem)
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_filename = f"{clean_stem}_{now}{ext}"
    new_path = os.path.join(dirname, new_filename)

    with open(new_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    os.remove(path)

    print(f"\nFichier mis à jour : {new_path}")
    if modified_eans:
        print("Formats complétés pour les EAN suivants :")
        for e in sorted(set(modified_eans)):
            print(f"  - {e}")
    else:
        print("Nettoyage et réordonnancement effectués pour tous les produits.")


def main():
    chemin = input("Entrez le chemin du fichier JSON ou du dossier : ").strip()
    if os.path.isfile(chemin):
        if "iadetailed" in os.path.basename(chemin).lower():
            process_file(chemin)
        else:
            print(f"Le fichier '{chemin}' n'est pas un fichier iAdetailed. Ignoré.")
    elif os.path.isdir(chemin):
        found = False
        for root, _, files in os.walk(chemin):
            for f in files:
                if f.lower().endswith('.json') and 'iadetailed' in f.lower():
                    found = True
                    process_file(os.path.join(root, f))
        if not found:
            print("Aucun fichier .json iAdetailed trouvé dans", chemin)
    else:
        print("Chemin invalide :", chemin)

if __name__ == "__main__":
    main()