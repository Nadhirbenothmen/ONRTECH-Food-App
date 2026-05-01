#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import re
import requests
from tqdm import tqdm

# --- CONFIG ---
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"   # ou "mistral"

# Permet de passer les fichiers en argument
INPUT_FILES = sys.argv[1:] if len(sys.argv) > 1 else [
    "products_with_ingredients_ia_as_format.json",
    "products_with_ingredients_ia_format_full.json",
    "products_with_ingredients_ia_final.json",
    "products_missing_ingredients_ia.json",
    "products_missings_ingredients_ia.json",
    "products_missing_or_empty_ingredients_ia.json",
    "products_with_ingredients_as_format.json",
    "products_without_ingredients_as_format.json",
    "products_ean_equals_all_fields.json",
    "products_with_empty_ingredients_and_clean.json",
    "products_with_ingredients_dot_full.json",
    "products_with_ingredients_final.json",
    "products_with_ingredients_clean_as_format_cleaned.json",
    "products_with_ingredients_as_format_fin.json"
]

OUTPUT_FILE = "missing_ingredients_predicted_final_cleaned_alcampo_fin.json"
CACHE_FILE = "title_to_ingredients_cache_ing_final_cleaned_alcampo_fin.json"

PROMPT_TEMPLATE = """
Eres un experto en nutrición.
A partir del título del producto, predice sus ingredientes.

Instrucciones importantes:
- Responde SOLO en JSON válido.
- No uses porcentajes ni explicaciones.
- Usa siempre exactamente estas claves:
  "ingredients" (cadena en ESPAÑOL),
  "ingredients_clean" (cadena simplificada en ESPAÑOL),
  "ingredients_ia" (lista en INGLÉS).
- Si no hay información precisa, usa una estimación simple.
  Ejemplos:
  - Whisky: "Agua, cebada malteada"
  - Vino: "Uvas"
  - Agua mineral: "Agua mineral"
  - Estuche, bolsa, accesorios: "N/A"

Ejemplo de respuesta correcta:
{{
  "ingredients": "Agua, cebada malteada",
  "ingredients_clean": "Agua, cebada malteada",
  "ingredients_ia": ["Water", "Malted barley"]
}}

Título del producto: "{title}"
"""


# --- UTILS ---
def force_json_decode(val):
    """Essaie de décoder récursivement si c'est un JSON string."""
    if isinstance(val, str):
        try:
            parsed = json.loads(val)
            return force_json_decode(parsed)
        except Exception:
            return val
    if isinstance(val, list):
        return [force_json_decode(v) for v in val]
    if isinstance(val, dict):
        return {k: force_json_decode(v) for k, v in val.items()}
    return val

# --- GESTION DE CACHE ---
def load_cache():
    if not os.path.exists(CACHE_FILE):
        return {}

    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    corrected = {}
    fixed_count = 0
    removed_count = 0

    for title, pred in data.items():
        decoded = force_json_decode(pred)

        # re-nettoyage champ par champ
        if isinstance(decoded, dict):
            decoded_fixed = {
                "ingredients": force_json_decode(decoded.get("ingredients", "")),
                "ingredients_clean": force_json_decode(decoded.get("ingredients_clean", "")),
                "ingredients_ia": force_json_decode(decoded.get("ingredients_ia", [])),
            }
        else:
            decoded_fixed = decoded

        if decoded_fixed != pred:
            fixed_count += 1

        if not is_valid_prediction(decoded_fixed):
            removed_count += 1
            continue

        corrected[title] = decoded_fixed

    # 🔹 Réécriture du cache corrigé
    with open(CACHE_FILE, "w", encoding="utf-8") as fw:
        json.dump(corrected, fw, ensure_ascii=False, indent=4, sort_keys=True)

    print(f"🧹 Cache nettoyé : {len(corrected)} entrées (corrigées: {fixed_count}, supprimées: {removed_count}) → {CACHE_FILE}")
    return corrected



def save_cache(cache):
    """Sauvegarde en forçant le nettoyage avant d’écrire"""
    cleaned = {k: force_json_decode(v) for k, v in cache.items()}
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cleaned, f, ensure_ascii=False, indent=4, sort_keys=True)
    print(f"💾 Cache sauvegardé ({len(cleaned)} titres) → {CACHE_FILE}")


def is_valid_prediction(pred: dict) -> bool:
    if not pred:
        return False
    if not isinstance(pred, dict):
        return False

    ingredients = str(pred.get("ingredients", "")).strip()
    ingredients_clean = str(pred.get("ingredients_clean", "")).strip()
    ingredients_ia = pred.get("ingredients_ia", [])

    # cas: liste vide ou [""] → invalide
    if isinstance(ingredients_ia, list):
        ingredients_ia = [x for x in ingredients_ia if str(x).strip()]

    return bool(ingredients or ingredients_clean or ingredients_ia)


def is_missing_ingredients_ia(val) -> bool:
    if not val:
        return True
    if isinstance(val, str) and not val.strip():
        return True
    if isinstance(val, list) and all((not x or str(x).strip().lower() in {"", "null", "none"}) for x in val):
        return True
    return False

def is_illogical_ingredients(val) -> bool:
    if not val:
        return True
    if isinstance(val, str):
        val = [val]

    bad_patterns = [
        r"\b\d+\s?(g|kg|mg|ml|cl|l|lt|liter|litre|liters)\b",
        r"\bpack\b", r"\bbox\b", r"\bbrick\b", r"\bweight\b",
        r"\bbottle\b", r"\bcan\b", r"\bjar\b", r"\bbag\b",
        r"\bbotella\b", r"\blata\b", r"\btarro\b", r"\bbolsa\b",
        r"\b\d+x\b",
        r"\buds?\b", r"\bunid(?:ad(?:es)?)?\b",
        r"\b\d+\s*units?\b"
    ]

    for ing in val:
        ing_low = str(ing).lower()
        if len(ing_low) <= 2:
            return True
        for pat in bad_patterns:
            if re.search(pat, ing_low):
                return True
    return False

def is_format_instead_of_ingredients(val) -> bool:
    if not val:
        return False
    if isinstance(val, str):
        patterns = [
            r"\d+\s?(g|kg|mg|ml|cl|l|lt)",
            r"\buds?\b", r"\bunidad(es)?\b",
            r"\bcapsulas?\b", r"\bsobres?\b",
            r"\bpack\b", r"\b\d+\s*x\b"
        ]
        for pat in patterns:
            if re.search(pat, val.lower()):
                return True
    return False

# --- POST-TRAITEMENT ---
def clean_prediction(pred: dict) -> dict:
    pred = force_json_decode(pred)

    ingredients = pred.get("ingredients", "")
    ingredients_clean = pred.get("ingredients_clean", "")
    ingredients_ia = pred.get("ingredients_ia", [])

    if not isinstance(ingredients, str):
        ingredients = str(ingredients)
    if not isinstance(ingredients_clean, str):
        ingredients_clean = str(ingredients_clean)
    if isinstance(ingredients_ia, str):
        ingredients_ia = [i.strip() for i in ingredients_ia.split(",") if i.strip()]
    if not isinstance(ingredients_ia, list):
        ingredients_ia = [str(ingredients_ia)]

    cleaned_ia = []
    seen = set()
    ignore_words = {"additives", "vitamins", "minerals", "preservatives"}
    for ing in ingredients_ia:
        ing = ing.strip()
        if not ing:
            continue
        key = ing.lower()
        if key in seen:
            continue
        seen.add(key)
        if any(w in key for w in ignore_words):
            continue
        ing = ing[0].upper() + ing[1:] if len(ing) > 1 else ing.upper()
        cleaned_ia.append(ing)

    return {
        "ingredients": ingredients.strip(),
        "ingredients_clean": ingredients_clean.strip(),
        "ingredients_ia": cleaned_ia
    }

# --- IA ---
def query_ollama(title: str) -> dict:
    prompt = PROMPT_TEMPLATE.format(title=title)
    resp = requests.post(OLLAMA_URL, json={"model": MODEL, "prompt": prompt}, stream=True)
    resp.raise_for_status()
    text = ""
    for line in resp.iter_lines():
        if not line:
            continue
        try:
            data = json.loads(line.decode("utf-8"))
            text += data.get("response", "")
        except:
            continue
    text = text.strip()

    try:
        parsed = json.loads(text)
    except:
        parsed = {"ingredients": text, "ingredients_clean": text, "ingredients_ia": [text]}

    # Nettoie la prédiction
    prediction = clean_prediction(parsed)

    # --- Fallback si toujours vide ---
    if not is_valid_prediction(prediction):
        low = title.lower()
        if "whisky" in low:
            prediction = {
                "ingredients": "Agua, cebada malteada",
                "ingredients_clean": "Agua, cebada malteada",
                "ingredients_ia": ["Water", "Malted barley"]
            }
        elif "vino" in low:
            prediction = {
                "ingredients": "Uvas",
                "ingredients_clean": "Uvas",
                "ingredients_ia": ["Grapes"]
            }
        elif "agua" in low:
            prediction = {
                "ingredients": "Agua mineral",
                "ingredients_clean": "Agua mineral",
                "ingredients_ia": ["Mineral water"]
            }
        else:
            prediction = {
                "ingredients": "N/A",
                "ingredients_clean": "N/A",
                "ingredients_ia": ["N/A"]
            }

    return prediction


# --- MAIN ---
def main():
    cache = load_cache()

    # Fusionne tous les produits des INPUT_FILES
    products = []
    from_as_format = 0
    for fpath in INPUT_FILES:
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    products.extend(data)
                    if "products_with_ingredients_ia_as_format" in fpath:
                        from_as_format += len(data)
                except Exception as e:
                    print(f"⚠️ Erreur lecture {fpath} : {e}")

    count_recalc = 0
    count_cache = 0
    count_skip = 0

    enriched = []
    for p in tqdm(products, desc="Prediction IA"):
        title = p.get("title", "").strip()
        ingredients_ia = p.get("ingredients_ia")

        if (is_missing_ingredients_ia(ingredients_ia) or 
            is_illogical_ingredients(ingredients_ia) or 
            is_format_instead_of_ingredients(ingredients_ia)) and title:

            # Vérifie le cache uniquement si valide
            if title in cache and is_valid_prediction(cache[title]):
                prediction = cache[title]
                count_cache += 1
                status = "cache"
            else:
                prediction = query_ollama(title)

                # Vérifie si la prédiction est vraiment utile
                if is_valid_prediction(prediction):
                    cache[title] = prediction
                    save_cache(cache)
                    status = "IA recalculée"
                    count_recalc += 1
                else:
                    # Ne pas sauvegarder si vide
                    status = "IA vide (non sauvegardée)"
                    count_recalc += 1


            cleaned = force_json_decode({
                "ean": p.get("ean"),
                "title": title,
                **prediction
            })
            enriched.append(cleaned)
            print(f"🔄 {title[:40]}... → {status}")

        else:
            cleaned = force_json_decode({
                "ean": p.get("ean"),
                "title": title,
                "ingredients": p.get("ingredients"),
                "ingredients_clean": p.get("ingredients_clean"),
                "ingredients_ia": p.get("ingredients_ia"),
            })
            enriched.append(cleaned)
            count_skip += 1
            print(f"⏩ {title[:40]}... → skip (déjà correct)")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(enriched, f, ensure_ascii=False, indent=4)

    print(f"✅ Fichier généré : {OUTPUT_FILE}")
    save_cache(cache)

    # --- Résumé final ---
    uniques = len({p.get("title", "").strip() for p in products})
    print("\nRésumé :")
    print(f"- {uniques} produits uniques")
    print(f"- dont {from_as_format} venaient de products_with_ingredients_ia_as_format.json")
    print(f"- {count_recalc} recalculés IA")
    print(f"- {count_cache} pris du cache")
    print(f"- {count_skip} skip (corrects)")

if __name__ == "__main__":
    main()
