#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import re
from pathlib import Path
from datetime import datetime
from googletrans import Translator

# --- Cache des traductions ---
CACHE_FILE = Path('dia_translation_cache.json')
try:
    with CACHE_FILE.open('r', encoding='utf-8') as cf:
        TRANSLATION_CACHE = json.load(cf)
except FileNotFoundError:
    TRANSLATION_CACHE = {}

# Ordre des clés souhaité pour chaque produit
PRODUCT_KEY_ORDER = [
    "ean", "brand", "business_type", "categories", "origin", "matter",
    "market", "lang_desc", "evolutions", "mesure_unit_for_packaging",
    "mesure_unit_for_price_per_unit", "label", "created_at", "updated_at",
    "parsing_duration"
]
# Ordre des clés souhaité pour chaque évolution
EVOLUTION_KEY_ORDER = [
    "parsing_date", "format", "availability", "certification",
    "nutriscore", "nutrition", "ingredients", "ingredients_clean",
    "ingredients_ia", "allergens", "weight_per_packaging",
    "price_per_packaging", "price_per_unit"
]

# Initialisation du traducteur pour espagnol -> anglais
translator = Translator()

# --- Fonctions d'extraction et d'unité ---
def extract_format_from_title(title):
    paren = re.search(r"\(([^)]+)\)", title)
    if paren:
        return paren.group(1).strip()
    vol = re.search(r"\b\d+(?:[\.,]\d+)?\s*(?:kg|g|l|ml|cl)\b", title, re.IGNORECASE)
    if vol:
        return vol.group(0).strip()
    pack = re.search(r"\b\d+\s*[xX]\s*\d+(?:[\.,]\d+)?\s*(?:kg|g|l|ml|cl)?\b", title, re.IGNORECASE)
    if pack:
        return pack.group(0).strip()
    return ""

# --- Application des unités selon 'matter' ---
def apply_matter_units(evo):
    matter = evo.get("matter", "").upper()
    if matter == "SUBSTANCE":
        evo["mesure_unit_for_packaging"] = "g"
        evo["mesure_unit_for_price_per_unit"] = "kg"
    elif matter == "LIQUID":
        evo["mesure_unit_for_packaging"] = "ml"
        evo["mesure_unit_for_price_per_unit"] = "l"
    elif matter == "PIECE":
        evo["mesure_unit_for_packaging"] = "piece"
        evo["mesure_unit_for_price_per_unit"] = "piece"
    else:
        evo["mesure_unit_for_packaging"] = "OTHER"
        evo["mesure_unit_for_price_per_unit"] = "OTHER"

# --- Nettoyage et traduction des ingrédients ---
def refine_ingredients(evo):
    raw = evo.get("ingredients", "")

    # 1) Extraire tout contenu entre parenthèses sans pourcentage
    parenth = re.findall(r"\(([^)]*?)(?<!%)\)", raw)

    # 2) Supprimer uniquement les parenthèses contenant un pourcentage
    text = re.sub(r"\([^)]*%[^)]*\)", "", raw)
    # 3) Retirer toutes les parenthèses restantes
    text = re.sub(r"[()]", "", text)

    # 4) Découper sur les virgules
    parts = [p.strip().lower() for p in text.split(",")]
    candidates = parenth + parts

    # 5) Filtrer vides, chiffres, stopwords, ne garder que lettres/espaces/tirets
    stopwords = {
        "ingredientes","puede","contener","y","de","con","en",
        "la","el","los","las","del","al","que","etc",
        "zumo","vitamina","c","agua","aceite","polvo","formula",
        "puré","fruta","a","partir","proporción","variable"
    }
    es_list = []
    for w in candidates:
        w = w.strip()
        if not w or re.search(r"\d", w) or w in stopwords:
            continue
        if not re.fullmatch(r"[a-záéíóúüñ\s-]+", w):
            continue
        es_list.append(w)

    # 6) Déduplication en conservant l'ordre
    unique_es = []
    for ing in es_list:
        if ing not in unique_es:
            unique_es.append(ing)
    evo["ingredients_clean"] = ", ".join(unique_es)

    # 7) Traduction anglaise via cache
    unique_en = []
    for ing in unique_es:
        tr = TRANSLATION_CACHE.get(ing)
        if not tr:
            try:
                tr = translator.translate(ing, src='es', dest='en').text.lower().strip()
            except Exception:
                tr = ing
            TRANSLATION_CACHE[ing] = tr
        if tr not in unique_en:
            unique_en.append(tr)
    evo["ingredients_ia"] = unique_en

# --- Suppression des unités 'OTHER' ---
def remove_other_units(data):
    for obj in data:
        if obj.get("mesure_unit_for_packaging") == "OTHER": obj.pop("mesure_unit_for_packaging", None)
        if obj.get("mesure_unit_for_price_per_unit") == "OTHER": obj.pop("mesure_unit_for_price_per_unit", None)
        for evo in obj.get("evolutions", []):
            if evo.get("mesure_unit_for_packaging") == "OTHER": evo.pop("mesure_unit_for_packaging", None)
            if evo.get("mesure_unit_for_price_per_unit") == "OTHER": evo.pop("mesure_unit_for_price_per_unit", None)

# --- Réordonnage des clés ---
def reorder_obj(obj, key_order):
    ordered = {}
    for k in key_order:
        if k in obj: ordered[k] = obj[k]
    for k,v in obj.items():
        if k not in ordered: ordered[k] = v
    return ordered

# --- Analyse et mise à jour des évolutions ---
def analyse_and_update(data):
    total_evos=0; missing_fmt=0; missing_fmt_eans=set()
    for obj in data:
        ean=obj.get("ean","<sans-ean>")
        for evo in obj.get("evolutions",[]):
            total_evos+=1
            if not evo.get("format"):
                fmt=extract_format_from_title(evo.get("title",""))
                if fmt: evo["format"]=fmt
                else: missing_fmt+=1; missing_fmt_eans.add(ean)
            apply_matter_units(evo)
            refine_ingredients(evo)
    remove_other_units(data)
    return total_evos, missing_fmt, missing_fmt_eans

# --- Vérification du nutriscore ---
def check_nutriscore(data):
    missing_nutri = 0; missing_nutri_eans = set()
    for obj in data:
        ean = obj.get("ean", "<sans-ean>")
        for evo in obj.get("evolutions", []):
            if not evo.get("nutriscore"):
                missing_nutri += 1; missing_nutri_eans.add(ean)
    return missing_nutri, missing_nutri_eans

# --- Traitement de chaque fichier ---
def process_file(path):
    path = Path(path)
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except Exception as e:
        print(f"Erreur lecture {path} : {e}"); return
    if not isinstance(data, list):
        print(f"{path} n’est pas une liste JSON."); return
    total_evos, missing_fmt, fmt_eans = analyse_and_update(data)
    missing_nutri, nutri_eans = check_nutriscore(data)
    for obj in data:
        obj['evolutions'] = [reorder_obj(e, EVOLUTION_KEY_ORDER) for e in obj.get('evolutions', [])]
    data = [reorder_obj(obj, PRODUCT_KEY_ORDER) for obj in data]
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    base = re.sub(r'_[0-9]{8}_[0-9]{6}$', '', path.stem)
    new_path = path.with_name(f"{base}_{ts}.json")
    try:
        new_path.write_text(json.dumps(data, ensure_ascii=False, indent=4), encoding='utf-8')
        path.unlink(); print(f"Fichier écrit sous : {new_path.name} (ancien supprimé)")
    except Exception as e:
        print(f"Erreur écriture/cleanup : {e}"); return
    # Sauvegarde du cache
    with CACHE_FILE.open('w', encoding='utf-8') as cf:
        json.dump(TRANSLATION_CACHE, cf, ensure_ascii=False, indent=2)
    print(f"\n=== Bilan pour {new_path.name} ===")
    print(f"Évolutions examinées                  : {total_evos}")
    print(f"Formats manquants                     : {missing_fmt}")
    if fmt_eans:
        print("EANs sans format détecté :")
        for code in sorted(fmt_eans): print(f"  - {code}")
    print(f"Nutriscore manquants                  : {missing_nutri}")
    if nutri_eans:
        print("EANs sans nutriscore dans évolutions :")
        for code in sorted(nutri_eans): print(f"  - {code}")

# --- Point d'entrée ---
if __name__ == "__main__":
    cible = input("Entrez le chemin du fichier JSON ou du dossier : ").strip()
    if os.path.isfile(cible) and cible.lower().endswith('.json') and 'iadetailed' in cible.lower():
        process_file(cible)
    elif os.path.isdir(cible):
        found = False
        for root, _, files in os.walk(cible):
            for nom in files:
                if nom.lower().endswith('.json') and 'iadetailed' in nom.lower(): process_file(os.path.join(root, nom)); found = True
        if not found:
            print(f"Aucun .json 'iadetailed' trouvé sous {cible}")
    else:
        print(f"Chemin invalide : {cible}")
