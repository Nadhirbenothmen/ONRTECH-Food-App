import os
import json
import time
import re
from datetime import datetime
import requests
import json5
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List

from src.countries.spain.MercadonaV3.model.product_content_mercadona import ProductContentMercadona
OLLAMA_URL = "http://localhost:11434/api/generate"

# === Label Rules ===


def clean_units(text):
    if not isinstance(text, str):
        return text
    return re.sub(r"(\d+)\s?(mg|g|IU|%)", r"\1", text)


def predict_labels_from_title_and_ingredients(title: str, ingredients: str) -> dict:
    content = (title + " " + ingredients).lower()
    def match_any(keywords):
        return any(kw.lower() in content for kw in keywords)

    return {
        "bio": match_any(ProductContentMercadona.BIO_PRESENCE),
        "vegan": match_any(ProductContentMercadona.VEGAN_PRESENCE),
        "gluten_free": match_any(ProductContentMercadona.GLUTEN_ABSENCE),
        "lactose": match_any(ProductContentMercadona.LACTOSE_ABSENCE),
        "sugar_free": match_any(ProductContentMercadona.SUGAR_ABSENCE),
        "fat_free": match_any(ProductContentMercadona.FAT_ABSENCE),
        "gmo_free": match_any(ProductContentMercadona.GMO_ABSENCE),
        "additive": match_any(ProductContentMercadona.ADDITIVE_ABSENCE),
        "dye": match_any(ProductContentMercadona.DYE_ABSENCE),
        "preservative": match_any(ProductContentMercadona.PRESERVATIVE_ABSENCE),
        "halal": match_any(ProductContentMercadona.HALAL_PRESENCE),
    }


def enrich_title_with_ollama(title: str, weight: float = 235.0, model: str = "mistral", retries=3):
    prompt = f"""
Dado el título del producto: \"{title}\", genera un objeto JSON con los siguientes campos:

{{
  "desc": string,
  "ingredients": string,
  "ingredients_clean": lista[string],
  "ingredients_ia": lista[string],
  "nutrition": {{
    "kcal": float,
    "proteínas": float,
    "glucidos": float,
    "azúcares": float,
    "lípidos": float,
    "grasas_saturadas": float,
    "calcio": float,
    "hierro": float,
    "zinc": float,
    "yodo": float,
    "vitamina_a": float,
    "vitamina_c": float,
    "vitamina_d": float
  }}
}}

Solo responde con el JSON. No expliques nada.
    """.strip()

    for attempt in range(1, retries + 1):
        try:
            response = requests.post(
                OLLAMA_URL,
                json={
                    "model": model,
                    "prompt": prompt,
                    "stream": False,
                    "options": {"temperature": 0.7, "num_predict": 300}
                },
                timeout=60
            )
            response.raise_for_status()
            output = response.json()["response"]

            start = output.find("{")
            end = output.rfind("}") + 1
            json_str = output[start:end].strip()

            if not json_str:
                raise ValueError("Empty response from model")

            try:
                enriched = json.loads(json_str)
            except json.JSONDecodeError:
                enriched = json5.loads(json_str)

            enriched["nutrition"] = {
                k: clean_units(v) for k, v in enriched.get("nutrition", {}).items()
            }
            return enriched

        except Exception as e:
            print(f"[WARNING] Error attempt {attempt}/{retries}: {e}")
            time.sleep(1)

    if model != "llama3":
        print("[RETRY] Switching to fallback model llama3...")
        return enrich_title_with_ollama(title, weight, model="llama3", retries=2)

    return {"error": "API failed after multiple retries"}


def normalize_carrefour_format(product):
    evo = product.get("evolutions", [{}])[0]
    nutrition_raw = evo.pop("nutrition", {})
    nutrition = {
        "energies": {
            "kj": 0,
            "kcal": float(nutrition_raw.get("kcal", 0))
        },
        "vitamins": {
            "vitamin_a": float(nutrition_raw.get("vitamina_a", 0)),
            "vitamin_c": float(nutrition_raw.get("vitamina_c", 0)),
            "vitamin_d": float(nutrition_raw.get("vitamina_d", 0))
        },
        "minerals": {
            "calcium": float(nutrition_raw.get("calcio", 0)),
            "iron": float(nutrition_raw.get("hierro", 0)),
            "zinc": float(nutrition_raw.get("zinc", 0)),
            "iodine": float(nutrition_raw.get("yodo", 0))
        },
        "fats": {
            "fats": float(nutrition_raw.get("lípidos", 0)),
            "saturates": float(nutrition_raw.get("grasas_saturadas", 0))
        },
        "proteins": {
            "proteins": float(nutrition_raw.get("proteínas", 0))
        },
        "carbohydrates": {
            "carbohydrates": float(nutrition_raw.get("glucidos", 0)),
            "of_which_sugars": float(nutrition_raw.get("azúcares", 0))
        }
    }
    product["updated_at"] = datetime.utcnow().isoformat()
    evo["nutrition"] = nutrition
    return product


def enrich_product(product, model):
    title = product.get("lang_desc", {}).get("es", {}).get("title")
    weight = product.get("evolutions", [{}])[0].get("weight_per_packaging", 235)

    if not title:
        return product

    enrichment = enrich_title_with_ollama(title, weight, model=model)
    if "error" in enrichment:
        print(f"[ERROR] Enrichment failed: {enrichment['error']} → {title}")
        return product

    evo = product.get("evolutions", [{}])[0]
    ingredients = enrichment.get("ingredients", "")

    evo.update({
        "ingredients": ingredients,
        "ingredients_clean": enrichment.get("ingredients_clean"),
        "ingredients_ia": enrichment.get("ingredients_ia", []),
        "nutrition": enrichment.get("nutrition", {})
    })

    product["label"] = predict_labels_from_title_and_ingredients(title, ingredients)
    product["lang_desc"]["es"]["desc"] = enrichment.get("desc", "")
    product = normalize_carrefour_format(product)
    return product


def process_file(filepath, model="llama3", max_threads=4):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    products = data if isinstance(data, list) else [data]

    print(f"[INFO] Enrichissement de {len(products)} produits en parallèle avec {max_threads} threads")
    results = []

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        future_to_product = {executor.submit(enrich_product, p, model): p for p in products}
        for future in tqdm(as_completed(future_to_product), total=len(products), desc="[WAITING] Enrichissement"):
            enriched = future.result()
            results.append(enriched)

    out_path = filepath.replace(".json", "_enriched.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results if isinstance(data, list) else results[0], f, indent=4, ensure_ascii=False)
    print(f"[OK] Fichier enrichi sauvegardé : {out_path}")


if __name__ == "__main__":
    try:
        path = input("[*] Entrez le chemin du fichier ou dossier à traiter : ").strip()
        model = input("[*] Modèle à utiliser (mistral / llama3) [par défaut : mistral] : ").strip() or "mistral"
        threads = int(input("[*] Nombre de threads (ex : 4) [par défaut : 4] : ").strip() or 4)
    except Exception as e:
        print(f"[ERROR] Mauvaise saisie : {e}")
        exit(1)

    if os.path.isfile(path):
        process_file(path, model=model, max_threads=threads)
    else:
        print("[ERROR] Chemin de fichier invalide.")
