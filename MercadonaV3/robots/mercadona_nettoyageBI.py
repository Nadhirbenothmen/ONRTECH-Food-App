#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from pathlib import Path
import sys
import json
import re
from datetime import datetime
from googletrans import Translator  # Remplacez par votre service de traduction


IAD_FILE_PAT = re.compile(
    r'^(?P<root>.+?\.json)(?:_(?P<rawts>\d{2}(?:_\d{2}){4}|\d{4}(?:_\d{2}){4}))?_iAdetailed'
    r'(?:_(?P<iadts>\d{2}(?:_\d{2}){4}|\d{4}(?:_\d{2}){4}))?\.json$',
    re.I
)

def _parse_root_and_ts(fname: str):
    m = IAD_FILE_PAT.match(fname)
    if not m:
        return None, None
    root  = m.group("root")
    iadts = m.group("iadts")
    dt = None
    if iadts:
        # essaie plusieurs formats: année-devant, année 2 chiffres, ou jour-devant (ton rename)
        for fmt in ("%Y_%m_%d_%H_%M", "%y_%m_%d_%H_%M", "%d_%m_%H_%M_%S"):
            try:
                dt = datetime.strptime(iadts, fmt)
                break
            except:
                pass
    return root, dt

# --- Configuration / Regex / Stopwords ---
UNIT_PATTERN = re.compile(r'\b\d+(?:[\.,]\d+)?\s?(?:g|kg|l|ml)\b', re.IGNORECASE)
STOPWORDS = {
    'papilla','preparado','lácteo','hero','solo','peques','puleva',
    'meses','mes','de','del','la','el','un','una','0%','%','añadidos',
    'azúcares','sin','gluten'
}
UNITS = {'g','kg','ml','l','piece'}
translator = Translator()

# --- Cache de traduction ---
CACHE_FILE = Path('mercadona_translation_cache.json') if 'Path' in globals() else None
try:
    if CACHE_FILE and CACHE_FILE.exists():
        with open(CACHE_FILE, 'r', encoding='utf-8') as cf:
            TRANSLATION_CACHE = json.load(cf)
    else:
        TRANSLATION_CACHE = {}
except Exception:
    TRANSLATION_CACHE = {}


def normalize(s: str) -> str:
    return re.sub(r'[^a-z0-9]+','', s.lower())

def is_only_format(ing: str, fmt: str) -> bool:
    raw = ing.strip().replace(' de ',' ')
    if normalize(raw) == normalize(fmt.strip()):
        return True
    if raw.lower() == fmt.strip().lower():
        return True
    low = ing.lower()
    if UNIT_PATTERN.search(low):
        cleaned = UNIT_PATTERN.sub('', re.sub(r'[()\[\]]','', low)).strip()
        return cleaned == '' or cleaned.isnumeric()
    return False


def extract_base_ingredients(title: str) -> list[str]:
    parts = re.split(r'\bcon\b', title, flags=re.IGNORECASE)
    seg = parts[1] if len(parts) > 1 else parts[0]
    seg = re.split(r'\d+', seg)[0]
    toks = re.split(r'[\,y]', seg)
    out = []
    for t in toks:
        for w in re.findall(r"[A-Za-zÁÉÍÓÚáéíóúñÑ]+", t.lower()):
            if w not in STOPWORDS and w not in UNITS:
                out.append(w)
    return list(dict.fromkeys(out))


def translate_list(es_list: list[str]) -> list[str]:
    out = []
    for w in es_list:
        # utiliser cache
        if w in TRANSLATION_CACHE:
            out.append(TRANSLATION_CACHE[w])
        else:
            try:
                tr = translator.translate(w, src='es', dest='en').text.lower().strip()
            except Exception:
                tr = w
            TRANSLATION_CACHE[w] = tr
            out.append(tr)
    return out


def get_es_title(prod: dict) -> str:
    return prod.get('lang_desc', {}).get('es', {}).get('title', '') or ''


def process_file(path: str) -> tuple[int, list[str]]:
    now = datetime.now()
    # Charger JSON
    with open(path, encoding='utf-8') as f:
        data = json.load(f)

    # Supprimer updated_at sans created_at
    def strip_updated(obj):
        if isinstance(obj, dict):
            if 'created_at' not in obj:
                obj.pop('updated_at', None)
            for v in obj.values(): strip_updated(v)
        elif isinstance(obj, list):
            for item in obj: strip_updated(item)
    strip_updated(data)

    only_eans = []
    prods = data if isinstance(data, list) else [data]
    for prod in prods:
        title = get_es_title(prod)
        for evo in prod.get('evolutions', []):
            ing = evo.get('ingredients', '')
            fmt = evo.get('format', '')
            if is_only_format(ing, fmt):
                only_eans.append(prod.get('ean', ''))
                base = extract_base_ingredients(title)
                text_es = ", ".join(base)
                evo['ingredients'] = text_es
                evo['ingredients_clean'] = text_es
                evo['ingredients_ia'] = translate_list(base)

    # Écraser fichier et mettre à jour horodatage
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    ts = now.timestamp()
    os.utime(path, (ts, ts))

    # Sauvegarder cache
    if CACHE_FILE:
        with open(CACHE_FILE, 'w', encoding='utf-8') as cf:
            json.dump(TRANSLATION_CACHE, cf, ensure_ascii=False, indent=2)

    # Renommer fichier avec timestamp
    stamp = now.strftime("%d_%m_%H_%M_%S")
    dirname, filename = os.path.split(path)
    new_filename = re.sub(r'\d{2}_\d{2}_\d{2}_\d{2}_\d{2}', stamp, filename)
    new_path = os.path.join(dirname, new_filename)
    os.rename(path, new_path)

    print(f"🔄 {filename} → {new_filename} (mtime {now})")
    return len(only_eans), only_eans


def find_iadetailed_files(root: str) -> list[str]:
    out = []
    for dp, _, fns in os.walk(root):
        for fn in fns:
            if fn.lower().endswith('.json') and 'iadetailed' in fn.lower():
                out.append(os.path.join(dp, fn))
    return out


def main():
    inp = input("📂 Chemin fichier ou dossier : ").strip()
    if not os.path.exists(inp):
        print("❌ Chemin invalide."); sys.exit(1)
    if os.path.isfile(inp):
        files = [inp] if 'iadetailed' in os.path.basename(inp).lower() else []
    else:
        latest_by_root = {}  # "Baby_food.json" -> (has_ts:int, dt:datetime, full_path)
        for dp, _, fns in os.walk(inp):
            for fn in fns:
                low = fn.lower()
                if not (low.endswith('.json') and 'iadetailed' in low):
                    continue
                root, dt = _parse_root_and_ts(fn)
                if not root:
                    continue
                full = os.path.join(dp, fn)
                has_ts = 1 if dt is not None else 0
                if dt is None:
                    dt = datetime.fromtimestamp(os.path.getmtime(full))  # fallback: mtime
                prev = latest_by_root.get(root)
                if prev is None or (has_ts, dt) > (prev[0], prev[1]):
                    latest_by_root[root] = (has_ts, dt, full)
        files = [t[2] for t in latest_by_root.values()]

    if not files:
        print("⚠️ Aucun JSON iAdetailed trouvé."); sys.exit(0)
    total, all_eans = 0, []
    for p in files:
        cnt, eans = process_file(p)
        total += cnt; all_eans.extend(eans)
    unique = sorted(set(all_eans))
    print(f"\nTotal produits only-format : {total}")
    print(f"Produits uniques         : {len(unique)}")
    if unique:
        print("EANs :")
        for e in unique: print(" -", e)

if __name__ == '__main__':
    main()
