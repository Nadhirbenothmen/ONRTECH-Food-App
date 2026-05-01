import os
import sys
import json
import re
from datetime import datetime
from pathlib import Path
import unicodedata
from urllib.parse import urlparse, urlunparse, parse_qsl, urlencode
from typing import Optional
from dotenv import load_dotenv
from openai import OpenAI

sys.path.append('src')
sys.path.append('./')
from src.countries.spain.MercadonaV3.model.product_content_mercadona import ProductContentMercadona
from src.countries.spain.MercadonaV3.model.product_mercadona import LabelMercadona
from src.countries.spain.MercadonaV3.model.product_mercadona import ALLERGENS

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"   # coupe les logs TF Lite
os.environ["GLOG_minloglevel"] = "2"       # baisse la verbosité glog/absl
# ====== Config & client ======
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ====== Helpers ======
def strip_code_fences(s: str) -> str:
    if not isinstance(s, str):
        return ""
    s = s.strip()
    if s.startswith("```"):
        s = s.strip("`")
        s = s.replace("json", "", 1).strip()
    s = s.replace("```json", "").replace("```", "").strip()
    return s

def set_imgix_params(url: str, **params) -> str:
    """Réécrit une URL imgix avec des query params custom."""
    try:
        p = urlparse(url)
        q = dict(parse_qsl(p.query))
        q.update({k: v for k, v in params.items() if v is not None})
        new_q = urlencode(q, doseq=True)
        return urlunparse((p.scheme, p.netloc, p.path, p.params, new_q, p.fragment))
    except Exception:
        return url

def build_img_candidates(url: str) -> list[str]:
    candidates = []
    if not isinstance(url, str) or not url:
        return candidates

    # Versions HD en priorité
    candidates.append(set_imgix_params(url, w=2000, h=2000, dpr=2, fit="max", auto="compress,format"))
    candidates.append(set_imgix_params(url, w=1600, dpr=2, fit="max", auto="compress,format"))
    candidates.append(set_imgix_params(url, w=1200, dpr=2, fit="max", auto="compress,format"))

    base = url.split("?", 1)[0]
    candidates.append(base)
    candidates.append(url)

    out, seen = [], set()
    for u in candidates:
        if u and u not in seen:
            seen.add(u)
            out.append(u)
    return out

def call_gpt_vision_json(image_url: str, prompt: str, model: str = "gpt-4o-mini") -> dict:
    """Appel Chat Completions (vision) qui renvoie un JSON parsé."""
    resp = client.chat.completions.create(
        model=model,
        messages=[{
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": image_url}},
            ],
        }],
        temperature=0,
        response_format={"type": "json_object"},
    )
    raw = resp.choices[0].message.content or ""
    return json.loads(strip_code_fences(raw))

def to_float(x) -> float:
    if x is None: return 0.0
    if isinstance(x, (int, float)): return float(x)
    s = str(x).strip().replace(",", ".")
    # retire unités communes (avec et sans espace)
    for u in ["kJ","kcal","g","mg","ml","%","/100g",
              "por 100g","por 100 g","per 100g","per 100 g"]:
        s = s.replace(u, "")
    s = s.strip()
    try:
        return float(s)
    except:
        import re as _re
        m = _re.search(r"[-+]?\d*\.?\d+", s)
        return float(m.group(0)) if m else 0.0

def any_value(d: dict) -> bool:
    return any(to_float(v) != 0.0 for v in d.values()) if d else False

def grams_to_mg(x) -> float:
    """Convertit des grammes vers milligrammes (arrondi 2 déc.)."""
    return round(to_float(x) * 1000.0, 2)

def normalize_nutrition(nut_flat: dict) -> dict:
    """
    Transforme le format plat {kj,kcal,fats,saturates,carbohydrates,sugars,proteins,salt}
    → structure imbriquée. Les minéraux sont en mg (ici: 'salt' converti g→mg).
    """
    return {
        "energies": {
            "kj": to_float(nut_flat.get("kj")),
            "kcal": to_float(nut_flat.get("kcal")),
        },
        "minerals": {
            "salt": grams_to_mg(nut_flat.get("salt")),


        },
        "fats": {
            "fats": to_float(nut_flat.get("fats")),
            "saturates": to_float(nut_flat.get("saturates")),
        },
        "proteins": {
            "proteins": to_float(nut_flat.get("proteins")),
        },
        "carbohydrates": {
            "carbohydrates": to_float(nut_flat.get("carbohydrates")),
            "of_which_sugars": to_float(nut_flat.get("sugars")),
            "dietary_fiber": to_float(nut_flat.get("fiber")),
        },
    }

def deep_merge_fill(dst: dict, src: dict) -> dict:
    """Fusionne src → dst sans écraser les valeurs existantes non nulles."""
    if not isinstance(dst, dict):
        dst = {}
    for k, v in src.items():
        if isinstance(v, dict):
            dst[k] = deep_merge_fill(dst.get(k, {}), v)
        else:
            if k not in dst or to_float(dst.get(k)) == 0.0:
                dst[k] = v
    return dst

# ====== Ingrédients: nettoyage ======
def clean_ingredients(raw: str) -> str:
    """
    - Supprime 'Ingredientes:' (ou variantes)
    - Supprime pourcentages (ex: 40%, 0.5 %)
    - Supprime contenu entre () et {} (ex: (14%), (harina...), {…})
    - Uniformise tous les séparateurs en virgules, espaces propres
    """
    if not isinstance(raw, str):
        return ""
    s = raw.strip()

    # 1) Supprimer le préfixe "Ingredientes:" / "Ingredient:"
    s = re.sub(r"^\s*ingredientes?\s*:\s*", "", s, flags=re.IGNORECASE)

    # 2) Supprimer les pourcentages
    s = re.sub(r"\b\d+[.,]?\d*\s*%", "", s)

    # 3) Supprimer le contenu entre parenthèses et accolades
    s = re.sub(r"\([^)]*\)", "", s)
    s = re.sub(r"\{[^}]*\}", "", s)

    # 4) Uniformiser séparateurs → virgules (points/points-virgules)
    s = s.replace(";", ",").replace("·", ",").replace("•", ",").replace(".", ",")

    s = re.sub(r'(?i)\s+y\s+', ', ', s)

    # 5) Nettoyer espaces autour des virgules
    s = re.sub(r"\s*,\s*", ", ", s)

    # 6) Supprimer doubles virgules et espaces multiples
    s = re.sub(r",\s*,", ",", s)
    s = re.sub(r"\s+", " ", s)

    # 7) Retirer virgules/espaces superflus en bouts
    s = s.strip(" ,;.")

    return s

DESIRED_EVO_ORDER = [
    "parsing_date",
    "format",
    "availability",
    "nutri_Score",
    "nutrition",
    "ingredients",
    "ingredients_clean",
    "ingredients_ia",
    "allergens",
    "weight_per_packaging",
    "price_per_packaging",
    "price_per_unit",
]

def enforce_evolution_order(product: dict):
    evols = product.get("evolutions")
    if not (isinstance(evols, list) and evols and isinstance(evols[0], dict)):
        return

    evo = evols[0]

    # ---- Normalisation/ordre de nutrition (EN CONSERVANT minerals) ----
    ordered_nutrition = None
    if isinstance(evo.get("nutrition"), dict):
        nut = dict(evo["nutrition"])  # copie
        energies = nut.get("energies") or {}
        fats = nut.get("fats") or {}
        proteins = nut.get("proteins") or {}
        carbohydrates = nut.get("carbohydrates") or {}
        minerals = nut.get("minerals")  # <-- on garde tel quel si présent

        # fiber -> dietary_fiber
        if isinstance(carbohydrates, dict):
            if "dietary_fiber" not in carbohydrates and "fiber" in carbohydrates:
                carbohydrates["dietary_fiber"] = carbohydrates.pop("fiber")

        ordered_nutrition = {
        "energies": {
            "kj": to_float(energies.get("kj")),
            "kcal": to_float(energies.get("kcal")),
        },
        }

        # minerals directement sous energies
        if isinstance(minerals, dict) and minerals:
            ordered_minerals = {k: to_float(v) for k, v in minerals.items()}
            ordered_nutrition["minerals"] = ordered_minerals

        # puis le reste
        ordered_nutrition.update({
            "fats": {
                "fats": to_float(fats.get("fats")),
                "saturates": to_float(fats.get("saturates")),
            },
            "proteins": {
                "proteins": to_float(proteins.get("proteins")),
            },
            "carbohydrates": {
                "carbohydrates": to_float(carbohydrates.get("carbohydrates")),
                "of_which_sugars": to_float(carbohydrates.get("sugars")),
                "dietary_fiber": to_float(carbohydrates.get("dietary_fiber")),
            },
        })


    # Valeurs dans l’ordre souhaité
    values_in_order = {
        "parsing_date": evo.get("parsing_date"),
        "format": evo.get("format"),
        "availability": evo.get("availability"),
        "nutri_Score": evo.get("nutri_Score"),
        "nutrition": ordered_nutrition if ordered_nutrition is not None else evo.get("nutrition"),
        "ingredients": evo.get("ingredients"),
        "ingredients_clean": evo.get("ingredients_clean"),
        "ingredients_ia": evo.get("ingredients_ia"),
        "allergens": evo.get("allergens"),  # ✅ sera forcé plus bas
        "weight_per_packaging": evo.get("weight_per_packaging"),
        "price_per_packaging": evo.get("price_per_packaging"),
        "price_per_unit": evo.get("price_per_unit"),
    }

    new_evo = {}
    for k in DESIRED_EVO_ORDER:
        if k in ("ingredients_ia", "allergens"):  # ✅ forcer présence même vide
            val = values_in_order[k]
            new_evo[k] = val if val is not None else []
        else:
            if values_in_order[k] is not None:
                new_evo[k] = values_in_order[k]

    # Conserver toute autre clé en fin (si tu veux les garder)
    for k, v in evo.items():
        if k not in new_evo:
            new_evo[k] = v

    evols[0] = new_evo


# ====== Extraction: ingrédients ======
def extract_ingredients_from_image(image_url: str, model: str = "gpt-4o-mini", debug_file: Optional[Path] = None):
    """
    Extrait UNIQUEMENT la phrase/liste qui commence par 'Ingredientes:' (ES/PT),
    pas les textes marketing.
    """
    prompt = (
        "Lee SOLO la lista oficial de ingredientes del etiquetado. "
        "Ignora recuadros de receta o marketing. "
        "Devuelve un JSON ESTRICTO:\n"
        "{\n"
        '  "ingredients": "texto EXACTO que aparece a partir de la palabra Ingredientes o Ingredientes: '
        'y hasta el final del bloque. Si no aparece Ingredientes, devuelve cadena vacía."\n'
        "}\n"
        "Reglas:\n"
        "- No inventes. No traduzcas. Mantén puntuación y porcentajes.\n"
    )

    candidates = build_img_candidates(image_url)
    last_error = None
    for idx, url in enumerate(candidates, start=1):
        try:
            data = call_gpt_vision_json(url, prompt, model=model)
            ing_text = (data.get("ingredients") or "").strip()
            if ing_text:
                ing_norm = ing_text
                # Corrections OCR courantes
                repl = {"murcielago": "merluza", "murciélago": "merluza", "merluzo": "merluza"}
                low = ing_norm.lower()
                for k, v in repl.items():
                    if k in low:
                        ing_norm = re.sub(k, v, ing_norm, flags=re.IGNORECASE)
                print(f"✅ Ingrédients extraits depuis: {url}")
                return ing_norm
        except Exception as e:
            last_error = e
            if debug_file:
                try:
                    with open(debug_file, "a", encoding="utf-8") as dbg:
                        dbg.write(f"\n[ING DEBUG] URL #{idx}: {url}\n[ERR] {repr(e)}\n")
                except Exception:
                    pass
    if last_error:
        print(f"[ERREUR] Extraction ingrédients image échouée: {last_error}")
    return ""

# ====== Extraction: nutrition ======
def extract_nutrition_from_image(image_url: str, model: str = "gpt-4o-mini", debug_file: Optional[Path] = None) -> dict:
    """
    Lit UNIQUEMENT la colonne 'Por 100 g' (ou 'Per 100 g').
    """
    prompt = (
        "Lee la TABLA NUTRICIONAL y devuelve SOLO la columna 'Por 100 g' (o 'Per 100 g'). "
        "Devuelve JSON ESTRICTO con números en decimal punto, máx. 2 decimales, sin redondeos agresivos:\n"
        "{\n"
        '  "kj": number,\n'
        '  "kcal": number,\n'
        '  "fats": number,\n'
        '  "saturates": number,\n'
        '  "carbohydrates": number,\n'
        '  "of_which_sugars": number,\n'
        '  "fiber": number,\n'
        '  "proteins": number,\n'
        '  "salt": number\n'
        "}\n"
        "Si ves 0,08 g, escribe 0.08. Si falta un valor, escribe 0."
    )

    candidates = build_img_candidates(image_url)
    last_error = None
    for idx, url in enumerate(candidates, start=1):
        try:
            data = call_gpt_vision_json(url, prompt, model=model)
            out = {k: round(to_float(data.get(k)), 2) for k in
                   ["kj","kcal","fats","saturates","carbohydrates","of_which_sugars","fiber","proteins","salt"]}

            # Coherence check: carbs >= sugars
            if out["of_which_sugars"] > out["carbohydrates"] and out["carbohydrates"] > 0:
                out["carbohydrates"], out["of_which_sugars"] = out["of_which_sugars"], out["carbohydrates"]

            if any_value(out):
                print(f"✅ Nutrition extraite depuis: {url}")
                return out
        except Exception as e:
            last_error = e
            if debug_file:
                try:
                    with open(debug_file, "a", encoding="utf-8") as dbg:
                        dbg.write(f"\n[NUT DEBUG] URL #{idx}: {url}\n[ERR] {repr(e)}\n")
                except Exception:
                    pass
    if last_error:
        print(f"[ERREUR] Extraction nutrition image échouée: {last_error}")
    return {}

# ====== Mercadona-specific ======
def get_ingredients_image_from_product(product: dict) -> Optional[str]:
    """Mercadona: lang_desc.es.images = liste. Essaie [1] (étiquette), sinon [0]."""
    try:
        images_list = product.get("lang_desc", {}).get("es", {}).get("images", [])
        if len(images_list) > 1:
            return images_list[1]
        elif images_list:
            return images_list[0]
    except Exception:
        pass
    return None

def put_ingredients_under_evolution(product: dict, ingredients_text: str):
    """Place 'ingredients' sous evolutions[0]['ingredients'] et nettoie racine."""
    if not ingredients_text:
        return
    evols = product.get("evolutions")
    if not (isinstance(evols, list) and len(evols) > 0 and isinstance(evols[0], dict)):
        product["evolutions"] = [{}]
        evols = product["evolutions"]
    evols[0]["ingredients"] = ingredients_text
    if "ingredients_list" in product:
        del product["ingredients_list"]
    if "ingredients" in product:
        del product["ingredients"]

def put_ingredients_clean_under_evolution(product: dict, ingredients_clean: str):
    """Place 'ingredients_clean' sous evolutions[0], sous 'ingredients'."""
    if not ingredients_clean:
        return
    evols = product.get("evolutions")
    if not (isinstance(evols, list) and evols and isinstance(evols[0], dict)):
        product["evolutions"] = [{}]
        evols = product["evolutions"]

    evo = evols[0]
    evo["ingredients_clean"] = ingredients_clean

    # Nettoyage: plus de ingredients_clean à la racine
    if "ingredients_clean" in product:
        del product["ingredients_clean"]

#Ingredients_ia
def call_gpt_json_text(prompt: str, model: str = "gpt-4o-mini") -> dict:
    """Appel Chat Completions (TEXTE) qui renvoie un JSON parsé."""
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        response_format={"type": "json_object"},
    )
    raw = resp.choices[0].message.content or ""
    return json.loads(strip_code_fences(raw))

def postprocess_ingredients_ia(items: list[str]) -> list[str]:
    """Nettoyage simple + dédoublonnage pour ingredients_ia."""
    seen = set()
    out = []
    for it in items or []:
        if not isinstance(it, str):
            continue
        t = it.strip().strip(" ,;.-").lower()
        # ignorer vides
        if not t:
            continue
        # dédoublonnage en gardant l'ordre
        if t not in seen:
            seen.add(t)
            out.append(t)
    return out


def generate_ingredients_ia(ingredients_text: str, model: str = "gpt-4o-mini") -> list[str]:
    """
    À partir de la chaîne d'ingrédients (ES), produit une liste d'ingrédients de base EN.
    - Traduit vers l’anglais.
    - Garde UNIQUEMENT les ingrédients (matières premières): ex. 'apple', 'wheat flour', 'sunflower oil', 'sugar', 'salt'.
    - Exclut additifs/technos/claims: colorants, arômes, conservateurs, acidifiants, épaississants, édulcorants, E-xxx, vitamines, minéraux, 'acidity regulator', etc.
    - Pas de pourcentages, pas d’unités, pas d’allergènes en gras; pas de phrases; liste simple.
    JSON strict: {"ingredients_ia": ["...", "..."]}
    """
    if not isinstance(ingredients_text, str) or not ingredients_text.strip():
        return []

    prompt = f"""
Eres un asistente de datos. Te doy la lista de ingredientes ORIGINAL en español (texto plano).
Devuélveme SOLO los ingredientes base, traducidos a INGLÉS, como lista JSON estricta:

REQUISITOS
- No cantidades, no porcentajes, no unidades.
- No aditivos ni términos técnicos (ej.: emulsifier(s), stabilizer(s), preservative(s), acidity regulator(s), color(s), flavour(s)/flavor(s), sweetener(s), thickener(s), E-xxx, vitamins, minerals).
- No claims/avisos (ej.: "sin azúcares añadidos").
- Usa nombres genéricos en inglés (ej.: "wheat flour", "sunflower oil", "skimmed milk", "apple", "sugar", "salt").
- Singular/plural natural (no importa mientras sea claro). Sin frases, solo ítems.
- Salida JSON **estricta**:

{{
  "ingredients_ia": ["...","..."]
}}

TEXTO ORIGINAL (ES):
{ingredients_text}
"""
    try:
        data = call_gpt_json_text(prompt, model=model)
        items = data.get("ingredients_ia") or []
        return postprocess_ingredients_ia(items)
    except Exception:
        return []

def put_ingredients_ia_under_evolution(product: dict, ingredients_ia: list[str]):
    """Place 'ingredients_ia' sous evolutions[0], juste après 'ingredients_clean'."""
    if not ingredients_ia:
        return
    evols = product.get("evolutions")
    if not (isinstance(evols, list) and evols and isinstance(evols[0], dict)):
        product["evolutions"] = [{}]
        evols = product["evolutions"]

    evo = evols[0]
    ingredients = evo.get("ingredients")
    ingredients_clean = evo.get("ingredients_clean")
    allergens = evo.get("allergens")

    # Reconstruire dans l'ordre voulu
    new_evo = {}
    if ingredients is not None:
        new_evo["ingredients"] = ingredients
    if ingredients_clean is not None:
        new_evo["ingredients_clean"] = ingredients_clean
    new_evo["ingredients_ia"] = ingredients_ia
    if allergens is not None:
        new_evo["allergens"] = allergens

    # Rattacher le reste
    for k, v in evo.items():
        if k not in ("ingredients", "ingredients_clean", "ingredients_ia", "allergens"):
            new_evo[k] = v

    evols[0] = new_evo


#description
def extract_desc_from_image(image_url: str, model: str = "gpt-4o-mini", debug_file: Optional[Path] = None) -> str:
    """
    Extrae solo los MENSAJES CORTOS tipo reclamos/avisos del envase (no ingredientes ni tabla).
    Ejemplos: "Sin azúcares añadidos", "Contiene azúcares naturalmente presentes",
    "El contenido de sal obedece exclusivamente al sodio presente de forma natural en el alimento".
    Devuelve una sola línea en español, concatenando frases con punto.
    """
    prompt = (
        "Lee SOLO los mensajes cortos de reclamo o aviso del envase (no ingredientes ni tabla nutricional). "
        "Ejemplos: 'Sin azúcares añadidos', 'Contiene azúcares naturalmente presentes', "
        "'El contenido de sal obedece exclusivamente al sodio presente de forma natural en el alimento'. "
        "Devuelve JSON ESTRICTO:\n"
        "{\n"
        '  "desc": "frases tal cual aparecen, unidas en UNA sola línea; separa ideas con punto. Si no hay, devuelve vacío."\n'
        "}\n"
        "No inventes. No traduzcas."
    )

    candidates = build_img_candidates(image_url)
    last_error = None
    for idx, url in enumerate(candidates, start=1):
        try:
            data = call_gpt_vision_json(url, prompt, model=model)
            desc = (data.get("desc") or "").strip().strip(".")
            # normaliza espacios y deja frases separadas por punto
            desc = re.sub(r"\s+", " ", desc)
            if desc:
                print(f"✅ Descripción extraída desde: {url}")
                return desc
        except Exception as e:
            last_error = e
            if debug_file:
                try:
                    with open(debug_file, "a", encoding="utf-8") as dbg:
                        dbg.write(f"\n[DESC DEBUG] URL #{idx}: {url}\n[ERR] {repr(e)}\n")
                except Exception:
                    pass
    if last_error:
        print(f"[INFO] No se pudo extraer descripción: {last_error}")
    return ""

def put_desc_under_title(product: dict, desc_text: str):
    if not desc_text:
        return
    lang_desc = product.setdefault("lang_desc", {})
    es_obj = lang_desc.setdefault("es", {})

    # Sauvegarder title, images et links s'ils existent
    title = es_obj.get("title", "")
    images = es_obj.get("images", [])
    links = es_obj.get("links", {})

    # Reconstruire l'objet dans l'ordre voulu
    es_obj.clear()
    es_obj["title"] = title
    es_obj["desc"] = desc_text
    if images:
        es_obj["images"] = images
    if links:
        es_obj["links"] = links

def put_allergens_under_evolution(product: dict, allergens: list[str]):
    """Place 'allergens' sous evolutions[0], après ingredients_ia si présent, sinon après ingredients_clean.
       Toujours créer la clé, même si la liste est vide."""
    # ✅ même si allergens est vide, on garde []
    allergens = list(allergens or [])

    evols = product.get("evolutions")
    if not (isinstance(evols, list) and evols and isinstance(evols[0], dict)):
        product["evolutions"] = [{}]
        evols = product["evolutions"]

    evo = evols[0]
    ingredients = evo.get("ingredients")
    ingredients_clean = evo.get("ingredients_clean")
    ingredients_ia = evo.get("ingredients_ia")

    new_evo = {}
    if ingredients is not None:
        new_evo["ingredients"] = ingredients
    if ingredients_clean is not None:
        new_evo["ingredients_clean"] = ingredients_clean
    if ingredients_ia is not None:
        new_evo["ingredients_ia"] = ingredients_ia

    # ✅ on écrit toujours allergens (même vide)
    new_evo["allergens"] = allergens

    for k, v in evo.items():
        if k not in ("ingredients", "ingredients_clean", "ingredients_ia", "allergens"):
            new_evo[k] = v

    evols[0] = new_evo

    if "allergens" in product:
        del product["allergens"]



def _strip_accents(s: str) -> str:
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def _normalize_text(s: str) -> str:
    s = _strip_accents((s or "").lower())
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def detect_allergens(ingredients_text: str, allergens_list=None) -> list[str]:
    """Retourne une liste unique d’allergènes détectés (ordre de la liste source)."""
    if not isinstance(ingredients_text, str):
        return []
    allergens_list = allergens_list or ALLERGENS
    norm_text = _normalize_text(ingredients_text)

    found, seen = [], set()
    for raw_term in allergens_list:
        term = _normalize_text(raw_term)
        if not term:
            continue

        parts = term.split()
        last = parts[-1]
        # autoriser pluriel simple/es sur le dernier mot
        last_plural = fr"(?:{re.escape(last)}(?:s|es)?)"
        if len(parts) > 1:
            head = r"\b" + r"\s+".join(re.escape(p) for p in parts[:-1]) + r"\s+"
            pattern = head + last_plural + r"\b"
        else:
            pattern = r"\b" + last_plural + r"\b"

        if re.search(pattern, norm_text):
            key = raw_term.lower()
            if key not in seen:
                seen.add(key)
                found.append(raw_term)  # conserve l’étiquette d’origine

    return found

# ====== File processing ======
def process_json_file(filepath: str, model: str = "gpt-4o-mini"):
    debug_path = Path(filepath).with_suffix(".ingredients_debug.log")

    with open(filepath, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print(f"[ERREUR] Fichier JSON invalide : {filepath}")
            return

    is_list = isinstance(data, list)
    products = data if is_list else [data]

    for product in products:
        orig_url = get_ingredients_image_from_product(product)
        if not orig_url:
            print(f"[INFO] Pas d'image ingrédients trouvée pour : {product.get('ean', '???')}")
            continue

        # Image HD
        candidates = build_img_candidates(orig_url)
        image_url_hd = candidates[0] if candidates else orig_url
        print(f"📷 Extraction depuis (HD) : {image_url_hd}")

        # --- Ingrédients ---
        ing_text = extract_ingredients_from_image(image_url_hd, model=model, debug_file=debug_path)
        if ing_text:
            ingredients_clean = clean_ingredients(ing_text)
            allergens = detect_allergens(ingredients_clean or ing_text, ALLERGENS)
            print(f"[{product.get('ean','???')}] 🥕 Ingrédients : {ing_text}")
            print(f"[{product.get('ean','???')}] 🧹 Ingrédients clean : {ingredients_clean}")
            print(f"[{product.get('ean','???')}] ⚠️ Allergènes détectés : {allergens if allergens else 'aucun'}")

            put_ingredients_under_evolution(product, ing_text)
            put_ingredients_clean_under_evolution(product, ingredients_clean)
            # ⬇️ Générer ingredients_ia en EN à partir du texte original (plus riche)
            ingredients_ia = generate_ingredients_ia(ing_text, model=model)
            put_ingredients_ia_under_evolution(product, ingredients_ia)
            put_allergens_under_evolution(product, allergens)
        else:
            print(f"[{product.get('ean','???')}] [INFO] Ingrédients non extraits (même en HD).")

        

        # --- Desc desde imagen (claims/avisos cortos) ---
        desc_text = extract_desc_from_image(image_url_hd, model=model, debug_file=debug_path)
        if not desc_text:
            # Si no salió del HD, intenta también la otra imagen base por si la descripción está allí
            try_other = None
            images_list = product.get("lang_desc", {}).get("es", {}).get("images", [])
            if images_list:
                # si HD venía de [1], intenta [0]; si venía de [0], intenta [1]
                try_other = images_list[0] if len(images_list) > 1 and image_url_hd.startswith(images_list[1].split("?")[0]) else (images_list[1] if len(images_list) > 1 else None)
            if try_other:
                alt_candidates = build_img_candidates(try_other)
                if alt_candidates:
                    desc_text = extract_desc_from_image(alt_candidates[0], model=model, debug_file=debug_path)

        if desc_text:
            put_desc_under_title(product, desc_text)
            print(f"[{product.get('ean','???')}] 📝 Desc: {desc_text}")
        else:
            print(f"[{product.get('ean','???')}] [INFO] Desc no encontrada en imágenes.")

        # --- Label (détection depuis ingrédients + desc) ---
        try:
            # 1) Texte ingrédients
            ing_for_labels = ""
            evols = product.get("evolutions")
            if isinstance(evols, list) and evols and isinstance(evols[0], dict):
                ing_for_labels = (
                    evols[0].get("ingredients") or
                    evols[0].get("ingredients_clean") or
                    ""
                )
            if not ing_for_labels:
                # fallback rétro-compat si anciens fichiers
                ing_for_labels = product.get("ingredients") or product.get("ingredients_clean") or ""


            # 2) Texte desc (claims courts sous lang_desc.es.desc)
            desc_for_labels = (
                product.get("lang_desc", {})
                    .get("es", {})
                    .get("desc", "")
                    .strip()
            )

            def labels_from_text(text: str) -> dict:
                if not text:
                    return {}
                # on passe le texte via le champ title attendu par LabelMercadona
                tmp = dict(product)
                tmp["title"] = text
                try:
                    obj = LabelMercadona.from_dict_to_object(tmp)
                    return {k: v for k, v in obj.__dict__.items() if isinstance(v, bool)}
                except Exception:
                    return {}

            labels_ing = labels_from_text(ing_for_labels)
            labels_desc = labels_from_text(desc_for_labels)

            # 3) Fusion: priorité à True (OR logique). On n’écrase pas True par False.
            merged = dict(product.get("label") or {})
            for k, v in labels_ing.items():
                if v is True or k not in merged or merged[k] is None:
                    merged[k] = v
            for k, v in labels_desc.items():
                if v is True or k not in merged or merged[k] is None:
                    merged[k] = v

            # 4) Ne garder que bool
            product["label"] = {k: v for k, v in merged.items() if isinstance(v, bool)}

            print(f"[{product.get('ean','???')}] 🏷️ Label maj (ing+desc): {product['label']}")

        except Exception as e:
            print(f"[{product.get('ean','???')}] ⚠️ Label non calculé: {e}")


        # --- Nutrition ---
        nut_flat = extract_nutrition_from_image(image_url_hd, model=model, debug_file=debug_path)
        if nut_flat:
            print(f"[{product.get('ean','???')}] 📊 Nutrition (100g): {nut_flat}")
            nut_norm = normalize_nutrition(nut_flat)

            evols = product.get("evolutions")
            if not (isinstance(evols, list) and len(evols) > 0 and isinstance(evols[0], dict)):
                product["evolutions"] = [{}]
                evols = product["evolutions"]

            existing = evols[0].get("nutrition", {})
            if not isinstance(existing, dict):
                existing = {}
            evols[0]["nutrition"] = deep_merge_fill(existing, nut_norm)
            ns_letter = ProductContentMercadona.calculate_nutriscore_from_nested(evols[0]["nutrition"])
            evols[0]["nutri_Score"] = ns_letter
            # nettoyage au cas où il aurait été écrit en dessous par le passé
            if isinstance(evols[0].get("nutrition"), dict):
                evols[0]["nutrition"].pop("nutri_Score", None)

            print(f"[{product.get('ean','???')}] 🅽 NutriScore: {ns_letter}")
        else:
            print(f"[{product.get('ean','???')}] [INFO] Nutrition et Nutriscore non extraite.")
        enforce_evolution_order(product)

    ts = datetime.now().strftime("%Y_%m_%d_%H_%M")
    out_path = Path(filepath).with_name(f"{Path(filepath).stem}_ingredients_extracted_{ts}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(products if is_list else products[0], f, ensure_ascii=False, indent=4)
    print(f"✅ Sauvegardé → {out_path}")

# --- Sélection du dernier fichier brut par base ---
RX_4Y = re.compile(r"_([0-9]{4})_([0-9]{2})_([0-9]{2})_([0-9]{2})_([0-9]{2})(?:_([0-9]{2}))?\.json$", re.I)
RX_2Y = re.compile(r"_([0-9]{2})_([0-9]{2})_([0-9]{2})_([0-9]{2})_([0-9]{2})(?:_([0-9]{2}))?\.json$", re.I)

def parse_ts(name: str) -> datetime | None:
    m = RX_4Y.search(name)
    if m:
        y, mo, d, h, mi, s = m.groups()
        return datetime(int(y), int(mo), int(d), int(h), int(mi), int(s or "00"))
    m = RX_2Y.search(name)
    if m:
        yy, mo, d, h, mi, s = m.groups()
        y = 2000 + int(yy)
        return datetime(y, int(mo), int(d), int(h), int(mi), int(s or "00"))
    return None

def pick_latest_raw_files(root: str) -> list[Path]:
    """
    - Ignore les fichiers 'iadetailed'
    - Prend uniquement les <base>.json_<timestamp>.json
    - Regroupe par base et garde le plus récent
    """
    groups: dict[str, tuple[Path, datetime]] = {}
    for f in Path(root).rglob("*.json"):
        name = f.name
        if "iadetailed" in name.lower():
            continue
        if ".json_" not in name:
            continue
        ts = parse_ts(name)
        if not ts:
            continue
        base_key = name.split(".json_")[0] + ".json"
        cur = groups.get(base_key)
        if (cur is None) or (ts > cur[1]):
            groups[base_key] = (f, ts)
    return [p for (p, _) in groups.values()]

def process_path(path: str, model: str = "gpt-4o-mini"):
    p = Path(path)
    if p.is_file() and p.suffix.lower() == ".json":
        if "iadetailed" in p.name.lower():
            print(f"[INFO] Ignoré (iadetailed): {p}")
            return
        process_json_file(str(p), model=model)
    elif p.is_dir():
        latest_files = pick_latest_raw_files(str(p))
        if not latest_files:
            print("[INFO] Aucun fichier brut (dernier timestamp) trouvé.")
            return
        for json_file in latest_files:
            print(f"➡️  Sélectionné (dernier brut): {json_file}")
            process_json_file(str(json_file), model=model)
    else:
        print(f"[ERREUR] Chemin invalide : {path}")

# ====== Main ======
if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Utilisation : python mercadona_ingredients.py <fichier_ou_dossier> [model]")
        sys.exit(1)

    input_path = sys.argv[1]
    model = sys.argv[2] if len(sys.argv) == 3 else "gpt-4o-mini"
    process_path(input_path, model=model)
