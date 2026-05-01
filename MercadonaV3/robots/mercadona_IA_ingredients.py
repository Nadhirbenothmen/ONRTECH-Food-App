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
from deep_translator import GoogleTranslator

sys.path.append('./')
sys.path.append('src')

OLLAMA_URL = "http://localhost:11434/api/generate"
OFF_SEARCH_URL = "https://world.openfoodfacts.org/cgi/search.pl"
CACHE_FILE = "mercadona_cache_enrichment.json"

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

enrichment_cache = load_cache()

def clean_units(text):
    if not isinstance(text, str):
        return text
    return re.sub(r"(\d+)\s?(mg|g|IU|%)", r"\1", text)

def normalize_nutrition(raw):
    return {
        "energies": {"kj": float(raw.get("kj", 0)), "kcal": float(raw.get("kcal", 0))},
        "vitamins": {
            "vitamin_a": float(raw.get("vitamina_a", 0)),
            "vitamin_c": float(raw.get("vitamina_c", 0)),
            "vitamin_d": float(raw.get("vitamina_d", 0))
        },
        "minerals": {
            "calcium": float(raw.get("calcio", 0)),
            "iron": float(raw.get("hierro", 0)),
            "zinc": float(raw.get("zinc", 0)),
            "iodine": float(raw.get("yodo", 0))
        },
        "fats": {"fats": float(raw.get("lípidos", 0)), "saturates": float(raw.get("grasas_saturadas", 0))},
        "proteins": {"proteins": float(raw.get("proteínas", 0))},
        "carbohydrates": {"carbohydrates": float(raw.get("glucidos", 0)),
                           "of_which_sugars": float(raw.get("azúcares", 0))}
    }

def fetch_nutrition_off(query, weight_g):
    params = {"search_terms": query, "search_simple": 1, "action": "process", "json": 1}
    resp = requests.get(OFF_SEARCH_URL, params=params, timeout=30)
    if resp.status_code != 200:
        return None
    data = resp.json()
    if not data.get("products"):
        return None
    prod = data["products"][0]
    nutr = prod.get("nutriments", {})
    factor = weight_g / 100.0
    return {
        "kj": nutr.get("energy-kj_100g", 0) * factor,
        "kcal": nutr.get("energy-kcal_100g", 0) * factor,
        "proteínas": nutr.get("proteins_100g", 0) * factor,
        "glucidos": nutr.get("carbohydrates_100g", 0) * factor,
        "azúcares": nutr.get("sugars_100g", 0) * factor,
        "lípidos": nutr.get("fat_100g", 0) * factor,
        "grasas_saturadas": nutr.get("saturated-fat_100g", 0) * factor,
        "calcio": nutr.get("calcium_100g", 0) * factor,
        "hierro": nutr.get("iron_100g", 0) * factor,
        "zinc": nutr.get("zinc_100g", 0) * factor,
        "yodo": nutr.get("iodine_100g", 0) * factor,
        "vitamina_a": nutr.get("vitamin-a_100g", 0) * factor,
        "vitamina_c": nutr.get("vitamin-c_100g", 0) * factor,
        "vitamina_d": nutr.get("vitamin-d_100g", 0) * factor
    }

def enrich_title_with_ollama(title: str, ingredients: str, weight: float = 235.0, model: str = "mistral", retries=3):
    cache_key = f"{title.strip().lower()}|{weight}"
    if cache_key in enrichment_cache:
        return enrichment_cache[cache_key]

    prompt = f"""
    Dado el título del producto: \"{title}\", genera un objeto JSON con los siguientes campos:

    {{
      "ingredients": string,
      "ingredients_clean": string,
      "ingredients_ia": lista[string],
      "nutrition": {{ kj: float, kcal: float, proteínas: float, glucidos: float, azucares: float, lípidos: float, grasas_saturadas: float, calcio: float, hierro: float, zinc: float, yodo: float, vitamina_a: float, vitamina_c: float, vitamina_d: float }}
    }}

    Solo responde con el JSON.
    """.strip()

    enriched = None
    for attempt in range(1, retries + 1):
        try:
            resp = requests.post(
                OLLAMA_URL,
                json={"model": model, "prompt": prompt, "stream": False, "options": {"temperature": 0.5, "num_predict": 500}},
                timeout=60
            )
            resp.raise_for_status()
            enriched = resp.json().get("response", "").strip()
            break
        except Exception as e:
            print(f"[WARNING] Ollama attempt {attempt}/{retries} failed: {e}")
            time.sleep(1)

    if not enriched:
        if model != "llama3":
            return enrich_title_with_ollama(title, ingredients, weight, model="llama3", retries=2)
        print("[ERROR] Ollama enrich returned empty")
        enriched = '{}'

    try:
        enriched_obj = json.loads(enriched)
    except json.JSONDecodeError:
        try:
            enriched_obj = json5.loads(enriched)
        except Exception as e:
            print(f"[ERROR] Failed JSON5 parse: {e}")
            enriched_obj = {}

    nut = enriched_obj.get("nutrition", {})
    for k, v in nut.items():
        try:
            nut[k] = float(clean_units(v))
        except Exception:
            nut[k] = 0.0
    enriched_obj["nutrition"] = nut

    try:
        translated_ia = [GoogleTranslator(source='auto', target='en').translate(ingr) for ingr in enriched_obj.get("ingredients_ia", [])]
    except Exception as e:
        print(f"[WARNING] Translation failed: {e}")
        translated_ia = enriched_obj.get("ingredients_ia", [])

    enriched_obj["ingredients_ia"] = translated_ia

    try:
        ingredients_clean_es = ", ".join([GoogleTranslator(source='en', target='es').translate(ing) for ing in translated_ia])
    except Exception as e:
        print(f"[WARNING] Reverse translation failed: {e}")
        ingredients_clean_es = ""

    enriched_obj["ingredients_clean_es"] = ingredients_clean_es

    # Save to cache
    enrichment_cache[cache_key] = enriched_obj
    save_cache(enrichment_cache)

    return enriched_obj

def extract_title_from_url(url):
    if not url:
        return None
    parsed_url = urllib.parse.urlparse(url)
    path_parts = parsed_url.path.strip('/').split('/')
    if len(path_parts) >= 3:
        return path_parts[-1].replace('-', ' ').capitalize()
    return None

def enrich_product(product, model, filepath=None):
    result = copy.deepcopy(product)
    evo_orig = product.get("evolutions", [{}])[0]
    orig_ing = evo_orig.get("ingredients", "")
    lang_desc_es = result.get("lang_desc", {}).get("es", {})
    title = lang_desc_es.get("title") or extract_title_from_url(lang_desc_es.get("links", {}).get("links_self"))
    if not title:
        print(f"[WARNING] Produit {product.get('ean', 'unknown')} sans titre, enrichissement sauté.")
        return result
    enriched = enrich_title_with_ollama(title, orig_ing, evo_orig.get("weight_per_packaging", 100), model=model)
    nut = enriched.get("nutrition", {})
    if all(v == 0 or v is None for v in nut.values()):
        off = fetch_nutrition_off(title, evo_orig.get("weight_per_packaging", 100))
        if off:
            enriched["nutrition"] = off
    result["evolutions"] = [
        {
        "parsing_date": evo_orig.get("parsing_date"),
        "format": evo_orig.get("format"),
        "availability": evo_orig.get("availability"),
        "nutrition": normalize_nutrition(enriched.get("nutrition", {})),
        "ingredients": enriched.get("ingredients", orig_ing),
        "ingredients_clean": enriched.get("ingredients_clean_es", orig_ing),
        "ingredients_ia": enriched.get("ingredients_ia", []),
        "weight_per_packaging": evo_orig.get("weight_per_packaging"),
        "price_per_packaging": evo_orig.get("price_per_packaging"),
        "price_per_unit": evo_orig.get("price_per_unit")
    }
]
    result["updated_at"] = datetime.now(timezone.utc).astimezone(datetime.strptime("+0100", "%z").tzinfo).isoformat()
    if "parsing_duration" in product:
        result["parsing_duration"] = product["parsing_duration"]
    else:
        result["parsing_duration"] = int(time.time() - os.path.getmtime(filepath))
    return result

def process_file(filepath, model="mistral", max_threads=4):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    products = data if isinstance(data, list) else [data]
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        results = list(tqdm(executor.map(lambda p: enrich_product(p, model, filepath), products), total=len(products)))
    base = os.path.splitext(os.path.basename(filepath))[0]
    ts = datetime.now(timezone.utc).astimezone(datetime.strptime("+0100", "%z").tzinfo).strftime("%y_%m_%d_%H_%M")
    out_path = os.path.join(os.path.dirname(filepath), f"{base}_iAdetailed_{ts}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
    print(f"[OK] Saved → {out_path}")
# --- Helpers pour ne garder que la dernière version “brute” ---
EXCLUDE_PAT = re.compile(r'(iAdetailed|ingredients_extracted|HFdetailed|Ollamadetailed|GPTdetailed)', re.I)
TS_PATTERNS = [
    (re.compile(r'^(?P<base>.+?\.json)_(?P<ts>\d{4}(?:_\d{2}){4})\.json$', re.I), "%Y_%m_%d_%H_%M"),  # 2025_07_24_10_24
    (re.compile(r'^(?P<base>.+?\.json)_(?P<ts>\d{2}(?:_\d{2}){4})\.json$', re.I), "%y_%m_%d_%H_%M"),  # 25_07_24_10_24
]

def _is_raw_candidate(filename: str) -> bool:
    return filename.lower().endswith(".json") and not EXCLUDE_PAT.search(filename)

def _split_base_and_ts(filename: str):
    for pat, fmt in TS_PATTERNS:
        m = pat.match(filename)
        if m:
            base = m.group("base")
            ts = m.group("ts")
            try:
                dt = datetime.strptime(ts, fmt)
                return base, dt
            except ValueError:
                pass
    # Pas de timestamp → on retournera la mtime plus bas
    return filename, None

def process_directory(directory_path, model="mistral", max_threads=4):
    for root, _, files in os.walk(directory_path):
        latest_by_base = {}  # base.json -> (datetime, filename)
        for file in files:
            if not _is_raw_candidate(file):
                continue
            base, dt = _split_base_and_ts(file)
            full_path = os.path.join(root, file)
            if dt is None:
                dt = datetime.fromtimestamp(os.path.getmtime(full_path))
            if base not in latest_by_base or dt > latest_by_base[base][0]:
                latest_by_base[base] = (dt, file)

        # Traiter seulement la dernière version brute par base
        for base, (_, fname) in latest_by_base.items():
            full_path = os.path.join(root, fname)
            print(f"\n[INFO] Processing LATEST raw for {base}: {full_path}")
            process_file(full_path, model=model, max_threads=max_threads)

if __name__ == "__main__":
    input_paths = input("Path(s) to .json file(s) or directory(ies) (separated by comma): ").strip()
    model = input("Model (mistral/llama3) [llama3]: ").strip() or "llama3"
    try:
        threads = int(input("Threads: ").strip() or 4)
    except:
        threads = 4

    paths = [p.strip() for p in input_paths.split(",") if p.strip()]
    
    for path in paths:
        if os.path.isfile(path):
            print(f"\n📄 Processing file: {path}")
            process_file(path, model=model, max_threads=threads)
        elif os.path.isdir(path):
            print(f"\n📁 Processing directory: {path}")
            process_directory(path, model=model, max_threads=threads)
        else:
            print(f"⚠️ Invalid path: {path}")
