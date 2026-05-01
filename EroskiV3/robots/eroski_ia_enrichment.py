#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import time
import re
from datetime import datetime
import copy
import requests
import json5
from tqdm import tqdm
import urllib.parse
from collections import OrderedDict

def normalize_nutrition_keys(nut: dict) -> dict:
    """Corrige les clés mal orthographiées, supprime doublons et nettoie la nutrition IA."""
    if not nut or not isinstance(nut, dict):
        return {}

    # Cas particulier: JSON imbriqué sous le titre du produit
    if len(nut) == 1 and isinstance(next(iter(nut.values())), dict):
        nut = next(iter(nut.values()))

    mapping = {
        "proteiins": "proteins",
        "proteeins": "proteins",
        "protein": "proteins",
        "carbohydratees": "carbohydrates",
        "carbohydrattes": "carbohydrates",
        "carbohydratess": "carbohydrates",
        "nutrients": "nutrition",
        "energi": "energies",
        "energy": "energies",
        "fatss": "fats",
        "magnesio": "magnesium",   # IA renvoie parfois ça
    }

    normalized = {}
    for k, v in nut.items():
        nk = mapping.get(k.lower(), k)

        # Corrige doublon "{{...}}" → "{...}"
        if isinstance(v, str) and v.strip().startswith("{{"):
            try:
                v = json.loads(v.strip("{}"))
            except:
                v = {}

        # Appliquer récursivement
        if isinstance(v, dict):
            normalized[nk] = normalize_nutrition_keys(v)
        else:
            normalized[nk] = v

    # Supprimer les minéraux non gérés sauf salt et calcium
    if "minerals" in normalized and isinstance(normalized["minerals"], dict):
        allowed = {"salt", "calcium"}
        normalized["minerals"] = {k: v for k, v in normalized["minerals"].items() if k in allowed}

    return normalized



# --- CONSTANTES ---
OLLAMA_URL     = "http://localhost:11434/api/generate"
OFF_SEARCH_URL = "https://world.openfoodfacts.org/cgi/search.pl"
CACHE_FILE     = "eroski_cache_enrichment.json"
MAX_IA_TRIES   = 3

# --- GESTION DE CACHE ---
def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=4)
    print(f"💾 Cache sauvegardé : {CACHE_FILE} ({len(cache)} entrées)")

enrichment_cache = load_cache()

# --- UTILES ---
def is_invalid_ingredients_list(lst):
    if not lst or not isinstance(lst, list):
        return True
    joined = " ".join(lst).lower()
    if re.fullmatch(r"[0-9xgml\s]+", joined):  # ex: "2 190g"
        return True
    return False

def is_only_quantity(text: str) -> bool:
    return bool(text and re.fullmatch(r"[\d\sxX×,.]+(g|gr|ml|cl|l|kg)?", text.strip().lower()))

def enforce_valid_ingredients(evo):
    ing = evo.get("ingredients", "")
    clean = evo.get("ingredients_clean", "")
    if is_only_quantity(ing) or is_only_quantity(clean):
        evo["ingredients"] = ""
        evo["ingredients_clean"] = ""
        evo["ingredients_ia"] = []

def clean_ingredients_text(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r"\(.*?\)|\[.*?\]|\{.*?\}", "", text)   # enlever ()
    text = re.sub(r"\d+\s*%", "", text)                   # enlever %
    text = re.sub(r"\s+y\s+", ", ", text, flags=re.IGNORECASE)  # remplacer y par ,
    text = re.sub(r"\s*,\s*", ", ", text)                 # espaces autour des virgules
    text = re.sub(r"\s+", " ", text)                      # espaces multiples
    return text.strip(" ,")

def translate_ingredients_to_en(clean_text: str) -> list:
    if not clean_text:
        return []

    prompt = f"""
Traduisez cette liste d'ingrédients espagnols en anglais.
Retournez uniquement une liste JSON d'ingrédients en anglais, sans texte supplémentaire.

Espagnol:
{clean_text}

Format attendu:
["Ingredient1", "Ingredient2", ...]
"""
    try:
        resp = requests.post(OLLAMA_URL, json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": 0.2, "num_predict": 256}
        }, timeout=60)
        resp.raise_for_status()
        text = resp.json().get("response", "").strip()

        if "[" in text and "]" in text:
            frag = text[text.find("["):text.rfind("]")+1]
            return json.loads(frag)

    except Exception as e:
        print(f"⚠️ Traduction IA échouée: {e}")

    # fallback : séparer par virgules et capitaliser
    return [x.strip().capitalize() for x in clean_text.split(",") if x.strip()]

# --- FORMATAGE NUTRITION ---
def safe_get_float(nut, key, subkey=None):
    try:
        val = nut.get(key, 0)
        # Si c’est déjà un float/int, on le garde
        if isinstance(val, (int, float, str)):
            return round(float(val), 1)
        # Si c’est un dict, on prend le subkey
        if isinstance(val, dict) and subkey:
            return round(float(val.get(subkey, 0)), 1)
        return 0.0
    except:
        return 0.0

def sanitize_json(text: str) -> str:
    """
    Nettoie la réponse IA pour obtenir un JSON valide.
    - Extrait uniquement le bloc {...}
    - Supprime les unités (mg, g, kj, kcal, %)
    - Corrige les nombres mal formatés (1,000 → 1000)
    - Uniformise les guillemets
    """
    if "{" not in text or "}" not in text:
        return "{}"

    frag = text[text.find("{"):text.rfind("}")+1]

    # Supprime les unités comme "mg", "g", "kj", "kcal", "%"
    frag = re.sub(r"(\d+(?:[.,]\d+)?)\s*(mg|g|kj|kcal|%)", r"\1", frag, flags=re.IGNORECASE)

    # Corrige les séparateurs de milliers 1,000 → 1000
    frag = re.sub(r"(\d),(\d{3})(\D)", r"\1\2\3", frag)

    # Supprime les doubles virgules ou virgules finales
    frag = re.sub(r",\s*}", "}", frag)
    frag = re.sub(r",\s*]", "]", frag)

    # Corrige Nutri-Score
    frag = frag.replace("Nutri-Score", "nutri_Score")

    # Uniformise les quotes
    frag = frag.replace("’", "'").replace("“", '"').replace("”", '"')

    return frag

def normalize_numbers(d):
    """Convertit tous les entiers/str numériques en float"""
    if isinstance(d, dict):
        return {k: normalize_numbers(v) for k, v in d.items()}
    elif isinstance(d, list):
        return [normalize_numbers(x) for x in d]
    else:
        try:
            return float(d)
        except (ValueError, TypeError):
            return d

def format_nutrition(nut):
    return OrderedDict([
        ("energies", OrderedDict([
            ("kj", safe_get_float(nut, "kj")),
            ("kcal", safe_get_float(nut, "kcal"))
        ])),
        ("minerals", OrderedDict([
            ("salt", safe_get_float(nut, "salt")),
            ("calcium", safe_get_float(nut, "calcium"))
        ])),
        ("fats", OrderedDict([
            ("fats", safe_get_float(nut, "lípidos", "fats") or safe_get_float(nut, "fats")),
            ("saturates", safe_get_float(nut, "grasas_saturadas", "saturates") or safe_get_float(nut, "saturates"))
        ])),
        ("proteins", OrderedDict([
            ("proteins", safe_get_float(nut, "proteínas", "proteins") or safe_get_float(nut, "proteins"))
        ])),
        ("carbohydrates", OrderedDict([
            ("carbohydrates", safe_get_float(nut, "glucidos", "carbohydrates") or safe_get_float(nut, "carbohydrates")),
            ("of_which_sugars", safe_get_float(nut, "azúcares", "of_which_sugars") or safe_get_float(nut, "of_which_sugars")),
            ("dietary_fiber", safe_get_float(nut, "fiber", "dietary_fiber") or safe_get_float(nut, "dietary_fiber"))
        ]))
    ])

def is_empty_nutrition(nutr: dict) -> bool:
    """
    Vérifie si la nutrition est absente ou trop incomplète.
    Considère comme vide si :
      - tous les champs sont vides/0
      - ou si moins de 3 champs ont une valeur numérique > 0
    """
    if not nutr or not isinstance(nutr, dict):
        return True

    total_fields = 0
    non_empty_fields = 0

    for k, v in nutr.items():
        if isinstance(v, dict):
            for sk, sub in v.items():
                total_fields += 1
                try:
                    if sub is not None and float(sub) > 0:
                        non_empty_fields += 1
                except:
                    continue
        else:
            total_fields += 1
            try:
                if v is not None and float(v) > 0:
                    non_empty_fields += 1
            except:
                continue

    # ⚠️ Trop incomplet : moins de 3 valeurs valides => considéré vide
    if non_empty_fields < 3:
        print(f"⚠️ Nutrition incomplète détectée ({non_empty_fields}/{total_fields}) : {nutr}")
        return True

    return False

# --- PREDICTION NUTRITION IA ---
def enrich_product_nutrition(evolution: dict, title: str, ingredients: str) -> dict:
    nutr = evolution.get("nutrition", {})

    # 🔎 Vérifier si déjà en cache
    cache_key = f"nutrition::{title.strip().lower()}"
    if cache_key in enrichment_cache:
        evolution["nutrition"] = enrichment_cache[cache_key]
        print(f"💾 Nutrition récupérée du cache pour: {title}")
        return evolution

    if not is_empty_nutrition(nutr):
        return evolution

    print(f"⚠️ Nutrition vide détectée: {nutr}")

    prompt = f"""
Tu es un générateur JSON strict.
Donne uniquement un objet JSON (pas de texte, pas de phrases).
Produit: "{title}"
Ingrédients: "{ingredients}"

Format strict :
{{
  "energies": {{"kj": float, "kcal": float}},
  "minerals": {{"salt": float, "calcium": float}},
  "fats": {{"fats": float, "saturates": float}},
  "proteins": {{"proteins": float}},
  "carbohydrates": {{"carbohydrates": float, "of_which_sugars": float, "dietary_fiber": float}},
  "nutri_Score": "A" | "B" | "C" | "D" | "E"
}}
""".strip()

    try:
        resp = requests.post(OLLAMA_URL, json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": 0.3, "num_predict": 300}
        }, timeout=90)
        resp.raise_for_status()
        text = resp.json().get("response", "").strip()

        frag = sanitize_json(text)

        try:
            nutrition_pred = json.loads(frag)
        except json.JSONDecodeError:
            print("⚠️ JSON invalide, tentative avec json5 …")
            nutrition_pred = json5.loads(frag)

        # ✅ conversion en float
        nutrition_pred = normalize_numbers(nutrition_pred)

        if not nutrition_pred or is_empty_nutrition(nutrition_pred):
            print("⚠️ IA n’a rien retourné d’utile, nutrition ignorée")
            return evolution

        # ✅ Met à jour l'objet produit
        evolution["nutrition"] = nutrition_pred

        # ✅ Sauvegarde dans le cache
        enrichment_cache[cache_key] = nutrition_pred
        save_cache(enrichment_cache)

        print("✅ Nutrition enrichie et sauvegardée en cache:", json.dumps(nutrition_pred, ensure_ascii=False))

    except Exception as e:
        print(f"❌ Erreur enrichissement nutrition: {e}")

    return evolution

# --- ENRICHISSEMENT IA (INGRÉDIENTS) ---
def enrich_title_with_ollama(title, retries=3, models=("mistral","llama3")):
    cache_key = title.strip().lower()
    if cache_key in enrichment_cache:
        return enrichment_cache[cache_key]
    prompt = f"""
Dado el título del producto: "{title}", genera un objeto JSON con:
{{
  "ingredients": string,
  "ingredients_clean": string,
  "ingredients_ia": lista[string]
}}
Solo responde con el JSON.
""".strip()
    for model in models:
        for _ in range(retries):
            try:
                resp = requests.post(OLLAMA_URL, json={
                    "model": model,
                    "prompt": prompt,
                    "stream": False,
                    "options": {"temperature": 0.3, "num_predict": 300}
                }, timeout=60)
                resp.raise_for_status()
                text = resp.json().get("response", "").strip()
                if "{" in text:
                    frag = text[text.find("{"):text.rfind("}")+1]
                    out = json.loads(frag)
                    if out.get("ingredients"):
                        clean = clean_ingredients_text(out.get("ingredients_clean") or out["ingredients"])
                        ia = translate_ingredients_to_en(clean)
                        out["ingredients_clean"] = clean
                        out["ingredients_ia"] = ia
                        enrichment_cache[cache_key] = out
                        save_cache(enrichment_cache)
                        return out
            except:
                time.sleep(1)
    return None

# --- FETCH OFF ---
def fetch_nutrition_off(query, weight_g):
    try:
        resp = requests.get(OFF_SEARCH_URL, params={
            "search_terms": query, "search_simple": 1, "action": "process", "json": 1
        }, timeout=30)
        resp.raise_for_status()
        data = resp.json()
    except:
        return {}
    if not data.get("products"):
        return {}
    nutr = data["products"][0].get("nutriments", {})
    factor = weight_g / 100.0
    return {
        "kj": nutr.get("energy-kj_100g", 0)*factor,
        "kcal": nutr.get("energy-kcal_100g", 0)*factor,
        "proteínas": nutr.get("proteins_100g", 0)*factor,
        "glucidos": nutr.get("carbohydrates_100g", 0)*factor,
        "azúcares": nutr.get("sugars_100g", 0)*factor,
        "lípidos": nutr.get("fat_100g", 0)*factor,
        "grasas_saturadas": nutr.get("saturated-fat_100g", 0)*factor,
        "salt": nutr.get("salt_100g", 0)*factor * 1000,      # mg
        "calcium": nutr.get("calcium_100g", 0)*factor * 1000, # mg
        "fiber": nutr.get("fiber_100g", 0)*factor,
        "nutriscore": data["products"][0].get("nutriscore_grade","").upper()
    }

def fetch_ingredients_off(title):
    try:
        resp = requests.get(OFF_SEARCH_URL, params={
            "search_terms": title,"search_simple":1,"action":"process","json":1,
            "fields":"ingredients_text,ingredients_text_en"
        }, timeout=30)
        resp.raise_for_status()
        data = resp.json()
    except:
        return None
    prods = data.get("products") or []
    if not prods:
        return None
    ingr_es = prods[0].get("ingredients_text", "")
    clean = clean_ingredients_text(ingr_es)
    return {
        "ingredients": ingr_es,
        "ingredients_clean": clean,
        "ingredients_ia": translate_ingredients_to_en(clean)
    }

# --- NEEDS ING ---
def needs_ing(prod):
    evo = prod.get("evolutions", [{}])[0]
    ing = evo.get("ingredients", "")
    clean = evo.get("ingredients_clean", "")
    ia = evo.get("ingredients_ia", [])

    # --- Cas 1 : ingredients_ia contient du texte MyMemory Warning
    if isinstance(ia, list):
        joined = " ".join(ia).lower()
        if "mymemory warning" in joined or "available free translations" in joined:
            return True
    elif isinstance(ia, str):
        if "mymemory warning" in ia.lower():
            return True

    # --- Cas 2 : champs vides ou incohérents
    if not (ing and clean and isinstance(ia, list) and any(x.strip() for x in ia)):
        return True
    if is_invalid_ingredients_list(ia):
        return True
    if is_only_quantity(ing) or is_only_quantity(clean):
        return True

    return False



# --- HEURISTIQUE SIMPLE ---
HEURISTIC_NUTRITION = {
    "agua": {"kj": 0, "kcal": 0, "proteins": 0, "fats": 0, "saturates": 0, "carbohydrates": 0, "of_which_sugars": 0, "fiber": 0, "salt": 0, "calcium": 0, "nutri_Score": "A"},
    "leche": {"kj": 260, "kcal": 62, "proteins": 3.2, "fats": 3.5, "saturates": 2, "carbohydrates": 4.8, "of_which_sugars": 4.8, "fiber": 0, "salt": 0.1, "calcium": 120, "nutri_Score": "B"},
    "yogur": {"kj": 250, "kcal": 60, "proteins": 3.5, "fats": 3, "saturates": 2, "carbohydrates": 4.5, "of_which_sugars": 4.5, "fiber": 0, "salt": 0.1, "calcium": 120, "nutri_Score": "B"},
    "galleta": {"kj": 2100, "kcal": 500, "proteins": 6, "fats": 24, "saturates": 12, "carbohydrates": 65, "of_which_sugars": 25, "fiber": 3, "salt": 0.6, "calcium": 20, "nutri_Score": "D"},
    "zumo": {"kj": 180, "kcal": 42, "proteins": 0.5, "fats": 0.1, "saturates": 0, "carbohydrates": 10, "of_which_sugars": 9, "fiber": 0.2, "salt": 0, "calcium": 5, "nutri_Score": "B"},
    "vino": {"kj": 280, "kcal": 70, "proteins": 0, "fats": 0, "saturates": 0, "carbohydrates": 2, "of_which_sugars": 2, "fiber": 0, "salt": 0, "calcium": 0, "nutri_Score": "E"},
    "pollo": {"kj": 670, "kcal": 160, "proteins": 20, "fats": 8, "saturates": 2, "carbohydrates": 0, "of_which_sugars": 0, "fiber": 0, "salt": 0.2, "calcium": 15, "nutri_Score": "A"},
    "pescado": {"kj": 820, "kcal": 196, "proteins": 22, "fats": 11, "saturates": 3, "carbohydrates": 0, "of_which_sugars": 0, "fiber": 0, "salt": 0.3, "calcium": 20, "nutri_Score": "A"},
    "manzana": {"kj": 215, "kcal": 52, "proteins": 0.3, "fats": 0.2, "saturates": 0, "carbohydrates": 14, "of_which_sugars": 12, "fiber": 2, "salt": 0, "calcium": 6, "nutri_Score": "A"},
    "plátano": {"kj": 371, "kcal": 89, "proteins": 1.1, "fats": 0.3, "saturates": 0.1, "carbohydrates": 23, "of_which_sugars": 12, "fiber": 2.6, "salt": 0, "calcium": 5, "nutri_Score": "B"},
}

def heuristic_nutrition(title: str):
    t = title.lower()
    for key, values in HEURISTIC_NUTRITION.items():
        if key in t:
            print(f"🟡 Nutrition estimée par heuristique pour: {title}")
            return format_nutrition(values), values.get("nutri_Score", "N/A")
    return None, None

def purge_invalid_ingredients(evo):
    """Supprime ingredients_ia s'il contient un warning MyMemory."""
    ia = evo.get("ingredients_ia", [])
    if isinstance(ia, list):
        if any("mymemory warning" in (x or "").lower() for x in ia):
            print(f"🗑️ Suppression ancienne valeur ingredients_ia = {ia}")
            evo["ingredients_ia"] = []
    elif isinstance(ia, str):
        if "mymemory warning" in ia.lower():
            print(f"🗑️ Suppression ancienne valeur ingredients_ia = {ia}")
            evo["ingredients_ia"] = []
    return evo

def clean_ingredients_ia_list(evo):
    """Supprime les éléments invalides (MyMemory warnings) de ingredients_ia"""
    ia = evo.get("ingredients_ia", [])
    if isinstance(ia, list):
        filtered = [x for x in ia if not any(
            bad in x.lower() for bad in ["mymemory warning", "available free translations"]
        )]
        if len(filtered) != len(ia):
            print(f"🗑️ Nettoyage ingredients_ia : {ia}  →  {filtered}")
        evo["ingredients_ia"] = filtered
    elif isinstance(ia, str) and "mymemory warning" in ia.lower():
        print(f"🗑️ Nettoyage ingredients_ia : {ia} → []")
        evo["ingredients_ia"] = []
    return evo

def is_illogical_ingredients_list(ia_list):
    """
    Détecte si ingredients_ia est utilisé comme 'format' ou quantité.
    Exemples: '190g', '6x200ml', 'botella 1.5l'
    """
    if not ia_list or not isinstance(ia_list, list):
        return True

    for ing in ia_list:
        if not ing or not isinstance(ing, str):
            return True
        txt = ing.strip().lower()

        # Cas: trop court ou juste chiffres + unité
        if re.fullmatch(r"[\dxX×.,\s]+(g|gr|ml|cl|l|kg|unidad|pack)?", txt):
            return True
        # Cas: contient "pack", "botella", "lata" etc.
        if any(word in txt for word in ["pack", "botella", "lata", "sachet", "unidad"]):
            return True
    return False

# --- ENRICH PRODUCT ---
def enrich_product(prod):
    p = copy.deepcopy(prod)
    evo = p.setdefault("evolutions", [{}])[0]

    title = prod.get("lang_desc", {}).get("es", {}).get("title", "")
    ing = evo.get("ingredients", "")
    clean = evo.get("ingredients_clean", "")
    ia = evo.get("ingredients_ia", [])

    # --- 1) Purge si Memory Warning
    if isinstance(ia, list) and any("mymemory warning" in (x or "").lower() for x in ia):
        print(f"\n⚠️ Produit avec Memory Warning détecté: {title}")
        evo["ingredients_ia"] = []
    elif isinstance(ia, str) and "mymemory warning" in ia.lower():
        print(f"\n⚠️ Produit avec Memory Warning détecté: {title}")
        evo["ingredients_ia"] = []

    # --- 2) Générer ingredients depuis le titre si vide
    if not ing and title:
        enriched = enrich_title_with_ollama(title)
        if enriched:
            evo["ingredients"] = enriched.get("ingredients", "")
            evo["ingredients_clean"] = clean_ingredients_text(
                enriched.get("ingredients_clean") or enriched.get("ingredients", "")
            )
            evo["ingredients_ia"] = enriched.get("ingredients_ia") or translate_ingredients_to_en(evo["ingredients_clean"])
            print(f"🤖 Ingrédients prédits depuis le titre: {evo['ingredients_ia']}")
        else:
            off_ing = fetch_ingredients_off(title)
            if off_ing:
                evo.update(off_ing)
                print(f"🌍 Ingrédients importés depuis OFF: {evo['ingredients_ia']}")


    # --- 3) Nettoyer ingredients → ingredients_clean
    if not clean and evo.get("ingredients"):
        evo["ingredients_clean"] = clean_ingredients_text(evo["ingredients"])
        print(f"🧹 ingredients_clean nettoyés: {evo['ingredients_clean']}")

    # --- 4) Détection des ingrédients illogiques (formats/quantités)
    def is_illogical_ingredients_list(ia_list):
        if not ia_list or not isinstance(ia_list, list):
            return True
        for ing in ia_list:
            if not ing or not isinstance(ing, str):
                return True
            txt = ing.strip().lower()
            # Juste chiffres + unité
            if re.fullmatch(r"[\dxX×.,\s]+(g|gr|mg|ml|cl|l|kg|unidad|pack)?", txt):
                return True
            # Contient mots de format/emballage
            if any(word in txt for word in ["pack", "botella", "lata", "sachet", "unidad", "envase"]):
                return True
        return False

    if is_illogical_ingredients_list(evo.get("ingredients_ia", [])):
        print(f"⚠️ ingredients_ia illogique détecté pour: {title} → {evo.get('ingredients_ia')}")
        evo["ingredients_ia"] = []

    # --- 5) Reconstruire ingredients_ia si vide ou invalide
    ia = evo.get("ingredients_ia", [])
    if not ia or not isinstance(ia, list) or not any(x.strip() for x in ia):
        if evo.get("ingredients_clean"):  # priorité à ingredients_clean
            evo["ingredients_ia"] = translate_ingredients_to_en(evo["ingredients_clean"])
            print(f"✅ ingredients_ia généré depuis ingredients_clean: {evo['ingredients_ia']}")
        elif evo.get("ingredients"):
            evo["ingredients_clean"] = clean_ingredients_text(evo["ingredients"])
            evo["ingredients_ia"] = translate_ingredients_to_en(evo["ingredients_clean"])
            print(f"✅ ingredients_ia généré depuis ingredients: {evo['ingredients_ia']}")
        elif title:  # fallback sur le titre
            enriched = enrich_title_with_ollama(title)
            if enriched:
                evo["ingredients"] = enriched["ingredients"]
                evo["ingredients_clean"] = clean_ingredients_text(
                    enriched.get("ingredients_clean") or enriched["ingredients"]
                )
                evo["ingredients_ia"] = translate_ingredients_to_en(evo["ingredients_clean"])
                print(f"✅ ingredients_ia généré depuis le titre: {evo['ingredients_ia']}")
            else:
                off_ing = fetch_ingredients_off(title)
                if off_ing:
                    evo.update(off_ing)
                    print(f"🌍 ingredients_ia importé depuis OFF: {evo['ingredients_ia']}")

    # --- 6) Nettoyage final
    clean_ingredients_ia_list(evo)
    enforce_valid_ingredients(evo)

    # --- 7) Nutrition (inchangé)
    nutr = normalize_nutrition_keys(evo.get("nutrition", {}))

    # Cas particulier: faux objet {"carbohydrates": {}} → considéré vide
    if nutr == {"carbohydrates": {}}:
        nutr = {}
    if is_empty_nutrition(nutr):
        weight = evo.get("weight_per_packaging", 100)
        off_nut = fetch_nutrition_off(title, weight)

        if off_nut and not is_empty_nutrition(off_nut):
            print(f"🌍 Nutrition mise à jour depuis OFF pour: {title}")
            evo["nutrition"] = format_nutrition(off_nut)
            if off_nut.get("nutriscore"):
                evo["nutri_Score"] = off_nut["nutriscore"]

        else:
            evo = enrich_product_nutrition(evo, title, evo.get("ingredients", ""))
            if is_empty_nutrition(normalize_nutrition_keys(evo.get("nutrition", {}))):
                heur, score = heuristic_nutrition(title)

                if heur:
                    evo["nutrition"] = heur
                    evo["nutri_Score"] = score

    return p


# --- PROCESS FILE ---
def process_file(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    prods = data if isinstance(data, list) else [data]
    enriched_count = 0
    results = []
    for prod in tqdm(prods, desc=os.path.basename(path)):
        new = enrich_product(prod)  # enrichit systématiquement (ingredients_ia + nutrition)
        enriched_count += 1
        results.append(new)

    out = results if isinstance(data, list) else results[0]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=4)
    return enriched_count, len(prods)

# --- MAIN ---
def main():
    root = sys.argv[1] if len(sys.argv) > 1 else input("Dossier iAdetailed: ").strip()
    total_enriched,total_scanned=0,0
    enriched_products=[]
    for dirpath,_,files in os.walk(root):
        for fn in files:
            if fn.lower().endswith(".json") and "iadetailed" in fn.lower():
                full=os.path.join(dirpath,fn)
                enriched_count,count=process_file(full)
                total_enriched+=enriched_count; total_scanned+=count
                if enriched_count>0:
                    with open(full,"r",encoding="utf-8") as f: data=json.load(f)
                    prods=data if isinstance(data,list) else [data]
                    for prod in prods:
                        evo=prod.get("evolutions",[{}])[0]
                        if needs_ing(prod) or is_empty_nutrition(normalize_nutrition_keys(evo.get("nutrition", {}))):
                            ean = prod.get("ean") or ",".join(prod.get("origin",{}).get("ean",[]))
                            enriched_products.append((full,ean))
    print(f"\n=== RÉSUMÉ ===\nProduits totaux  : {total_scanned}\nProduits enrichis: {total_enriched}\n")
    if enriched_products:
        print("\n📋 Produits enrichis (chemin + EAN):")
        for i,(path,ean) in enumerate(enriched_products[:20],start=1):
            print(f"{i:02d}. {path} | EAN: {ean}")
        if len(enriched_products)>20:
            with open("enriched_products.txt","w",encoding="utf-8") as f:
                for path,ean in enriched_products[20:]:
                    f.write(f"{path} | EAN: {ean}\n")
            print("\n⚠️ Plus de 20 produits enrichis. Voir enriched_products.txt")

if __name__=="__main__":
    main()
