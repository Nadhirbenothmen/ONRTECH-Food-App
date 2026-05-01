#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import time
import re
from datetime import datetime, timezone
import copy
import requests
import json5
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import urllib.parse
from collections import OrderedDict
from deep_translator import GoogleTranslator

# --- CONSTANTES ---
OLLAMA_URL     = "http://localhost:11434/api/generate"
OFF_SEARCH_URL = "https://world.openfoodfacts.org/cgi/search.pl"
CACHE_FILE     = "alcampo_cache_enrichment.json"
LOG_FILE       = "alcampo_enrichment.log"
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

def log_warning(msg: str):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(msg + "\n")
    print(msg)

enrichment_cache = load_cache()

# --- UTILES ---
def simplify_title_for_off(title: str) -> str:
    """Nettoie un titre produit pour améliorer la recherche OFF"""
    if not title:
        return ""
    text = title.lower()
    blacklist = ["pack", "caja", "lata", "botella", "bolsa", "bandeja",
                 "uds", "ud", "unidades", "unidad", "sobre", "capsulas"]
    for word in blacklist:
        text = re.sub(rf"\b{word}\b", " ", text)
    text = re.sub(r"\b\d+\s*(g|kg|ml|cl|l|litros?)\b", " ", text)
    text = re.sub(r"\b\d+\s*[x×]\s*\d+\s*(g|kg|ml|cl|l)\b", " ", text)
    text = re.sub(r"\b\d+\s*(uds?|unidades?)\b", " ", text)
    text = re.sub(r"\b\d+\b", " ", text)
    return re.sub(r"\s+", " ", text).strip()

def normalize_nutrition(raw):
    return OrderedDict([
        ("energies", OrderedDict([
            ("kj", float(raw.get("kj", 0))),
            ("kcal", float(raw.get("kcal", 0)))
        ])),
        ("minerals", OrderedDict([
            ("salt", float(raw.get("salt", 0)))
        ])),
        ("fats", OrderedDict([
            ("fats", float(raw.get("lípidos", 0))),
            ("saturates", float(raw.get("grasas_saturadas", 0)))
        ])),
        ("proteins", OrderedDict([
            ("proteins", float(raw.get("proteínas", 0)))
        ])),
        ("carbohydrates", OrderedDict([
            ("carbohydrates", float(raw.get("glucidos", 0))),
            ("of_which_sugars", float(raw.get("azúcares", 0))),
            ("dietary_fiber", float(raw.get("dietary_fiber", 0)))
        ]))
    ])

# --- TRADUCTION ---
def translate_to_english(items):
    translated = []
    for i in items:
        try:
            translated.append(GoogleTranslator(source="es", target="en").translate(i))
        except:
            translated.append(i)
    return translated

# --- FETCH OFF ---
def fetch_nutrition_off(query, weight_g):
    query = simplify_title_for_off(query)
    cache_key = f"{query.strip().lower()}|{weight_g}|nutrition"
    if cache_key in enrichment_cache:
        return enrichment_cache[cache_key]

    params = {"search_terms": query, "search_simple": 1, "action": "process", "json": 1}
    try:
        resp = requests.get(OFF_SEARCH_URL, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
    except:
        return {}
    if not data.get("products"):
        return {}

    prod = data["products"][0]
    nutr = prod.get("nutriments", {})
    factor = weight_g / 100.0
    result = {
        "kj": nutr.get("energy-kj_100g", 0) * factor,
        "kcal": nutr.get("energy-kcal_100g", 0) * factor,
        "proteínas": nutr.get("proteins_100g", 0) * factor,
        "glucidos": nutr.get("carbohydrates_100g", 0) * factor,
        "azúcares": nutr.get("sugars_100g", 0) * factor,
        "lípidos": nutr.get("fat_100g", 0) * factor,
        "grasas_saturadas": nutr.get("saturated-fat_100g", 0) * factor,
        "salt": nutr.get("salt_100g", 0) * factor * 1000,
        "dietary_fiber": nutr.get("fiber_100g", 0) * factor,
        "nutriscore": prod.get("nutriscore_grade", "").upper()
    }

    enrichment_cache[cache_key] = result
    save_cache(enrichment_cache)
    return result

def fetch_ingredients_off(title):
    params = {"search_terms": title, "search_simple": 1, "action": "process",
              "json": 1, "fields": "ingredients_text,ingredients_text_en"}
    try:
        resp = requests.get(OFF_SEARCH_URL, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
    except:
        return None
    prods = data.get("products") or []
    if not prods:
        return None
    prod = prods[0]
    ingr_es = prod.get("ingredients_text", "")
    ingr_en = prod.get("ingredients_text_en", "")
    items = [i.strip() for i in (ingr_es or ingr_en).split(",") if i.strip()]
    return {
        "ingredients": ingr_es or ingr_en,          # espagnol
        "ingredients_clean": (ingr_es or ingr_en),  # espagnol
        "ingredients_ia": translate_to_english(items)  # anglais
    }

# --- IA ---
def enrich_title_with_ollama(title, ingredients, weight,
                             models=("mistral", "llama3"), retries=3):
    cache_key = f"{title.strip().lower()}|{weight}"
    if cache_key in enrichment_cache:
        return enrichment_cache[cache_key]

    prompt = f"""
Dado el título del producto: "{title}", genera un objeto JSON con:
{{
  "ingredients": string,                // original en español
  "ingredients_clean": string,          // limpio en español
  "ingredients_ia": lista[string]       // traducido al inglés
}}
Solo responde con el JSON.
""".strip()

    for model in models:
        for _ in range(retries):
            try:
                resp = requests.post(OLLAMA_URL, json={
                    "model": model, "prompt": prompt, "stream": False,
                    "options": {"temperature": 0.3, "num_predict": 300}
                }, timeout=60)
                resp.raise_for_status()
                text = resp.json().get("response", "").strip()
                if "{" in text:
                    frag = text[text.find("{"):text.rfind("}")+1]
                    try:
                        out = json.loads(frag)
                    except:
                        out = json5.loads(frag)

                    required_keys = {"ingredients", "ingredients_clean", "ingredients_ia"}
                    if not required_keys.issubset(out.keys()):
                        log_warning(f"⚠️ Réponse IA incomplète pour « {title} » : {out}")
                        return None

                    enrichment_cache[cache_key] = out
                    save_cache(enrichment_cache)
                    return out

            except:
                time.sleep(1)
    return None

def predict_ingredients_from_title(title, models=("mistral", "llama3"), retries=2):
    """
    Utilise l'IA pour prédire des ingrédients de base à partir du titre du produit.
    Retourne un dict {ingredients, ingredients_clean, ingredients_ia}.
    """
    cache_key = f"{title.strip().lower()}|predict_title"
    if cache_key in enrichment_cache:
        return enrichment_cache[cache_key]

    prompt = f"""
Eres un sistema experto en alimentación.
A partir solo del título del producto: "{title}",
predice una lista razonable de ingredientes típicos.

Devuelve un objeto JSON con:
{{
  "ingredients": "texto en español con los ingredientes",
  "ingredients_clean": "versión simplificada en español, sin porcentajes ni frases técnicas",
  "ingredients_ia": ["traducción en inglés, en lista clara"]
}}
Responde solo con JSON válido.
""".strip()

    for model in models:
        for _ in range(retries):
            try:
                resp = requests.post(OLLAMA_URL, json={
                    "model": model, "prompt": prompt, "stream": False,
                    "options": {"temperature": 0.5, "num_predict": 250}
                }, timeout=60)
                resp.raise_for_status()
                text = resp.json().get("response", "").strip()
                if "{" in text:
                    frag = text[text.find("{"): text.rfind("}")+1]
                    try:
                        out = json.loads(frag)
                    except:
                        out = json5.loads(frag)

                    if isinstance(out, dict) and "ingredients" in out:
                        enrichment_cache[cache_key] = out
                        save_cache(enrichment_cache)
                        return out
            except:
                time.sleep(1)

    return None


def enrich_nutrition_with_ollama(title, ingredients_ia, weight,
                                 models=("mistral", "llama3"), retries=2):
    prompt = f"""
Dado el producto: "{title}" con estos ingredientes: {ingredients_ia},
genera un objeto JSON con el perfil nutricional aproximado por {weight} g.
Todos los valores deben ser float (números con decimales):

{{
  "kj": float,
  "kcal": float,
  "proteínas": float,
  "glucidos": float,
  "azúcares": float,
  "lípidos": float,
  "grasas_saturadas": float,
  "salt": float,
  "dietary_fiber": float
}}
Solo responde con el JSON.
""".strip()

    for model in models:
        for _ in range(retries):
            try:
                resp = requests.post(OLLAMA_URL, json={
                    "model": model, "prompt": prompt, "stream": False,
                    "options": {"temperature": 0.3, "num_predict": 300}
                }, timeout=60)
                resp.raise_for_status()
                text = resp.json().get("response", "").strip()
                if "{" in text:
                    frag = text[text.find("{"):text.rfind("}")+1]
                    try:
                        out = json.loads(frag)
                    except:
                        out = json5.loads(frag)
                    if isinstance(out, dict):
                        return {k: float(v) if v not in (None, "", "null") else 0.0 for k, v in out.items()}
            except:
                time.sleep(1)
    return None

# --- HELPERS ---
def extract_title_from_url(url):
    if not url: return None
    parts = urllib.parse.urlparse(url).path.strip("/").split("/")
    return parts[-1].replace("-", " ").capitalize()

def needs_nutrition(prod):
    evo = prod.get("evolutions", [{}])[0]
    nutr = evo.get("nutrition", {})
    # Si aucun champ nutrition → enrichissement
    if not nutr or not isinstance(nutr, dict):
        return True
    # Sinon on garde les valeurs existantes (même si certaines = 0 ou sel < 1)
    return False

def is_placeholder_ingredients(val: str) -> bool:
    """
    Détecte si un champ ingredients est vide ou un placeholder.
    """
    if not val:
        return True
    val_low = val.strip().lower()
    return (
        "no se especificaron" in val_low
        or "aucun" in val_low
        or val_low in ("n/a", "none", "-", "null")
    )


def postprocess_ingredients(evo):
    raw_ing = evo.get("ingredients", "")
    if not raw_ing:
        return evo

    # Nettoyage basique
    clean = raw_ing
    clean = re.sub(r"contiene\s+[^\.,;]+", "", clean, flags=re.IGNORECASE)
    clean = re.sub(r"colorante[s]?:", "colorante", clean, flags=re.IGNORECASE)
    clean = re.sub(r"conservante[s]?:", "conservante", clean, flags=re.IGNORECASE)

    # Découpage en liste
    parts = [p.strip(" .") for p in clean.split(",") if p.strip()]
    clean = ", ".join(parts)

    # Remplacer ingredients_clean s’il est vide ou placeholder
    if (not evo.get("ingredients_clean") or 
        "no se especificaron" in evo.get("ingredients_clean", "").lower()):
        evo["ingredients_clean"] = clean

    # Remplir ingredients_ia s’il est vide
    if not evo.get("ingredients_ia"):
        evo["ingredients_ia"] = translate_to_english(parts)

    return evo


# --- TEMPLATE POUR ORDONNANCER LES CHAMPS ---
EVOLUTION_TEMPLATE = OrderedDict([
    ("parsing_date", None),
    ("format", None),
    ("availability", None),
    ("nutri_Score", None),
    ("certification", None),
    ("nutrition", OrderedDict([
        ("energies", OrderedDict([
            ("kj", None),
            ("kcal", None),
        ])),
        ("minerals", OrderedDict([
            ("salt", None),
        ])),
        ("fats", OrderedDict([
            ("fats", None),
            ("saturates", None),
        ])),
        ("proteins", OrderedDict([
            ("proteins", None),
        ])),
        ("carbohydrates", OrderedDict([
            ("carbohydrates", None),
            ("of_which_sugars", None),
            ("dietary_fiber", None),
        ])),
    ])),
    ("ingredients", None),
    ("ingredients_clean", None),
    ("ingredients_ia", []),
    ("allergens", []),
    ("weight_per_packaging", None),
    ("price_per_packaging", None),
    ("price_per_unit", None),
    ("offers", []),
])

def reorder_evolution(evo: dict) -> OrderedDict:
    result = OrderedDict()
    for key, default in EVOLUTION_TEMPLATE.items():
        if key == "offers":
            # ⚡ On n'ajoute "offers" que si présent
            if "offers" in evo:
                result[key] = evo["offers"]
        elif key == "nutrition":
            nutr = evo.get("nutrition", {})
            nutr_ordered = OrderedDict()
            for subkey, subdefault in EVOLUTION_TEMPLATE["nutrition"].items():
                subdict = nutr.get(subkey, {})
                sub_ordered = OrderedDict()
                for sk in subdefault.keys():
                    sub_ordered[sk] = subdict.get(sk, None)
                nutr_ordered[subkey] = sub_ordered
            result[key] = nutr_ordered
        else:
            result[key] = evo.get(key, default)
    return result


# --- ENRICH PRODUCT ---
def enrich_product(prod):
    p   = copy.deepcopy(prod)
    evo = p.setdefault("evolutions", [{}])[0]

    title = (prod.get("lang_desc", {}).get("es", {}).get("title")
             or evo.get("format")
             or extract_title_from_url(prod.get("lang_desc", {}).get("es", {}).get("links", {}).get("links_self", "")))
    if not title:
        return p

    # --- Enrichissement ingrédients ---
    if "ingredients" in evo and evo.get("ingredients") and not is_placeholder_ingredients(evo["ingredients"]):
        # ingredients existe vraiment -> on complète seulement les autres
        if not evo.get("ingredients_clean") or not evo.get("ingredients_ia"):
            print(f"\n🍴 [{title}] Complément ingredients_clean / ingredients_ia")
            enriched = enrich_title_with_ollama(title, evo["ingredients"], evo.get("weight_per_packaging", 100))
            if enriched:
                evo["ingredients_clean"] = enriched.get("ingredients_clean", evo.get("ingredients_clean"))
                evo["ingredients_ia"] = enriched.get("ingredients_ia", evo.get("ingredients_ia", []))
                print(f"✅ [{title}] Complété ingredients_clean/ia")
            else:
                off_ing = fetch_ingredients_off(title)
                if off_ing:
                    evo["ingredients_clean"] = off_ing.get("ingredients_clean", evo.get("ingredients_clean"))
                    evo["ingredients_ia"] = off_ing.get("ingredients_ia", evo.get("ingredients_ia", []))
                    print(f"✅ [{title}] Complété ingredients_clean/ia (OFF)")
                else:
                    log_warning(f"⚠️ Impossible de compléter ingredients_clean/ia pour « {title} »")
    else:
        # ingredients absent OU placeholder -> prédire les 3
        print(f"\n🍴 [{title}] Prédiction complète ingrédients")
        enriched = enrich_title_with_ollama(title, "", evo.get("weight_per_packaging", 100))
        if enriched:
            evo["ingredients"] = enriched.get("ingredients")
            evo["ingredients_clean"] = enriched.get("ingredients_clean")
            evo["ingredients_ia"] = enriched.get("ingredients_ia", [])
            print(f"✅ [{title}] Ingrédients prédits")
            print("   ➤ ingredients:", evo["ingredients"])
            print("   ➤ clean      :", evo["ingredients_clean"])
            print("   ➤ IA (en)    :", evo["ingredients_ia"])
        else:
            off_ing = fetch_ingredients_off(title)
            if off_ing:
                evo.update(off_ing)
                print(f"✅ [{title}] Ingrédients prédits (OFF)")
            else:
                predicted = predict_ingredients_from_title(title)
                if predicted:
                    evo["ingredients"] = predicted.get("ingredients", "")
                    evo["ingredients_clean"] = predicted.get("ingredients_clean", "")
                    evo["ingredients_ia"] = predicted.get("ingredients_ia", [])
                    print(f"✅ [{title}] Ingrédients prédits (fallback titre)")
                else:
                    log_warning(f"⚠️ Aucun ingrédient trouvé pour « {title} »")

    
    # --- Post-traitement local pour nettoyer et traduire si besoin ---
    evo = postprocess_ingredients(evo)
    # --- Enrichissement nutrition ---
    if needs_nutrition(prod):
        print(f"\n🥗 [{title}] Nutrition AVANT: {evo.get('nutrition')}")
        weight = evo.get("weight_per_packaging", 100)
        off_nut = fetch_nutrition_off(title, weight)
        if off_nut:
            evo["nutrition"] = normalize_nutrition(off_nut)
            if off_nut.get("nutriscore"):
                evo["nutri_Score"] = off_nut["nutriscore"]
            print(f"✅ [{title}] Nutrition APRÈS (OFF): {evo['nutrition']}")
        else:
            ia_nut = enrich_nutrition_with_ollama(title, evo.get("ingredients_ia", []), weight)
            if ia_nut:
                evo["nutrition"] = normalize_nutrition(ia_nut)
                print(f"✅ [{title}] Nutrition APRÈS (IA): {evo['nutrition']}")
            else:
                log_warning(f"⚠️ Aucune nutrition trouvée ni prédite pour « {title} »")

    # 🔄 Réordonner les champs avant retour
    p["evolutions"][0] = reorder_evolution(evo)
    return p


# --- PROCESS FILES ---
def process_file(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    prods = data if isinstance(data, list) else [data]

    enriched_count = 0
    results = []
    for prod in tqdm(prods, desc=os.path.basename(path)):
        new = enrich_product(prod)
        if new != prod: enriched_count += 1
        results.append(new)

    out = results if isinstance(data, list) else results[0]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=4)

    dirn, orig_fn = os.path.split(path)
    now = datetime.now().strftime("%y_%m_%d_%H_%M")
    new_fn = re.sub(r"(\d{2}_\d{2}_\d{2}_\d{2}_\d{2})(?=\.json$)", now, orig_fn)
    os.replace(path, os.path.join(dirn, new_fn))

    return enriched_count, len(prods)

def main():
    root = sys.argv[1] if len(sys.argv) > 1 else input("Dossier iAdetailed: ").strip()
    total_enriched = 0
    total_scanned  = 0

    open(LOG_FILE, "w").close()  # vider le log

    for dirpath, _, files in os.walk(root):
        for fn in files:
            if fn.lower().endswith(".json") and "iadetailed" in fn.lower():
                enriched_count, count = process_file(os.path.join(dirpath, fn))
                total_enriched += enriched_count
                total_scanned  += count

    print(f"\n=== RÉSUMÉ ===\nProduits totaux  : {total_scanned}\nProduits enrichis: {total_enriched}\n")
    print(f"📄 Logs enregistrés dans {LOG_FILE}")

if __name__ == "__main__":
    main()
