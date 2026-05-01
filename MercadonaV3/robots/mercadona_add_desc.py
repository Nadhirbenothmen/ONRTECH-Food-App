#!/usr/bin/env python3
# fix_predict_desc_iadetailed.py
import os
import sys
import json
import re
from typing import Any, Dict, Tuple, List

# ---------- Utils fichiers ----------
def collect_json_files(path: str) -> List[str]:
    path = os.path.abspath(path)
    files = []
    if os.path.isfile(path):
        if path.lower().endswith(".json"):
            files.append(path)
    else:
        for root, _, fns in os.walk(path):
            for fn in fns:
                if fn.lower().endswith(".json"):
                    files.append(os.path.join(root, fn))
    # Ne garder que les iAdetailed
    return [f for f in files if "iadetailed" in os.path.basename(f).lower()]

# ---------- Normalisation & détection "desc triviale" ----------
_WS = re.compile(r"\s+")
_NONWORD = re.compile(r"[^\wáéíóúüñç]+", flags=re.IGNORECASE)

def _simplify(s: str) -> str:
    s = (s or "").strip().lower()
    s = _NONWORD.sub(" ", s)
    s = _WS.sub(" ", s).strip()
    return s

def is_trivial_desc(title: str, desc: str) -> bool:
    """
    Considère trivial si desc est vide OU égale au titre (avec/ sans ponctuation),
    ou commence par le titre (cas "Title. Algo" très rare).
    """
    if not isinstance(desc, str) or not desc.strip():
        return True
    if not isinstance(title, str) or not title.strip():
        return False
    st = _simplify(title)
    sd = _simplify(desc)
    return sd == st or sd.startswith(st + " ")

# ---------- Générateur de description ES ----------
def suggest_es_desc(title: str) -> str:
    """
    Génère une description espagnole courte et naturelle, SANS inventer d’ingrédients.
    Règles simples basées sur mots-clés; fallback générique.
    """
    t = (title or "").strip()
    base = t[0].upper() + t[1:] if t else ""

    low = t.lower()

    # Animaux
    if "periquito" in low or "periquitos" in low or "canario" in low or "canarios" in low or "aves" in low:
        return "Mezcla equilibrada para periquitos, ideal para la nutrición diaria y el cuidado del plumaje."

    if "gato" in low or "gatos" in low:
        return "Alimento completo para gatos con nutrientes esenciales para su día a día."

    if "perro" in low or "perros" in low:
        return "Alimento completo para perros que contribuye a su energía y bienestar diarios."

    # Bebés
    if "papilla" in low or "potito" in low or "tarrito" in low or "+ meses" in low or "meses" in low:
        m = re.search(r"(\+?\d+)\s*mes", low)
        if m:
            n = m.group(1).lstrip("+")
            return f"Papilla adecuada a partir de {n} meses, con textura suave para una alimentación diaria equilibrada."
        return "Papilla para bebés, con textura suave y pensada para una alimentación diaria equilibrada."

    # Pastas / fideos
    if any(w in low for w in ["fideo", "fideos", "espagueti", "espaguetis", "macarron", "macarrones", "pasta"]):
        if "cabello de ángel" in low or "cabello de angel" in low:
            return "Pasta tipo cabello de ángel, fina y versátil, ideal para sopas y preparaciones ligeras."
        return "Pasta de uso cotidiano, versátil para numerosas recetas."

    # Aceites / condimentos (générique sans présumer la variété)
    if any(w in low for w in ["aceite", "vinagre", "sal", "especia", "especias"]):
        return "Producto básico de cocina, práctico para realzar el sabor de tus recetas diarias."

    # Snacks / galletas / cereales (très générique)
    if any(w in low for w in ["galleta", "galletas", "cereal", "cereales", "snack", "aperitivo"]):
        return "Opción práctica para el día a día, perfecta para picar entre horas o acompañar desayunos."

    # Bebidas (générique)
    if any(w in low for w in ["zumo", "jugo", "bebida", "refresco", "agua", "té", "te ", "café", "cafe "]):
        return "Bebida pensada para el consumo diario, refrescante y fácil de combinar en cualquier momento."

    # Lácteos (générique)
    if any(w in low for w in ["leche", "yogur", "yogurt", "queso", "mantequilla"]):
        return "Producto lácteo de uso cotidiano, ideal para desayunos y meriendas."

    # Fallback ultra-sûr
    if base:
        return f"{base}. Ideal para el uso diario."
    return "Producto de uso cotidiano, práctico y fácil de incorporar a la rutina."

# ---------- Insertion 'desc' juste après 'title' ----------
def _insert_after_title(es: Dict[str, Any], desc: str) -> None:
    if "title" in es:
        new_es = {}
        inserted = False
        for k, v in es.items():
            new_es[k] = v
            if k == "title" and not inserted:
                new_es["desc"] = desc
                inserted = True
        if not inserted:
            new_es["desc"] = desc
        es.clear()
        es.update(new_es)
    else:
        es["desc"] = desc

def _normalize_desc_from_title(title: str) -> str:
    desc = (title or "").strip()
    if desc:
        desc = desc[0].upper() + desc[1:]
    if desc and desc[-1] not in ".!?":
        desc += "."
    return desc

# ---------- Cœur: ajout / réparation / remplacement ----------
def ensure_desc_in_lang_desc(product: Dict[str, Any]) -> Tuple[bool, bool]:
    """
    - Ajoute lang_desc.es.desc si absent (avec suggestion naturelle).
    - Remplace desc trivial (== titre) par une suggestion naturelle.
    - Répare l'imbrication erronée es.lang_desc -> es.desc.
    Retourne (changed, repaired_bug).
    """
    changed = False
    repaired = False

    lang_desc = product.get("lang_desc")
    if not isinstance(lang_desc, dict):
        return (False, False)

    es = lang_desc.get("es")
    if not isinstance(es, dict):
        es = {}
        lang_desc["es"] = es
        changed = True

    # Réparer l'imbrication
    nested = es.get("lang_desc")
    if isinstance(nested, dict):
        inner_es = nested.get("es")
        if isinstance(inner_es, dict):
            inner_desc = inner_es.get("desc")
            if isinstance(inner_desc, str) and inner_desc.strip() and not es.get("desc"):
                es["desc"] = inner_desc
                changed = True
        del es["lang_desc"]
        repaired = True

    # Si 'desc' existe mais trivial -> remplacer par meilleur texte
    current_desc = es.get("desc")
    # Chercher un titre
    title_candidates = [
        es.get("title"),
        product.get("title"),
        product.get("product_title"),
        product.get("name"),
    ]
    title = next((t for t in title_candidates if isinstance(t, str) and t.strip()), "")

    if isinstance(current_desc, str) and current_desc.strip():
        if title and is_trivial_desc(title, current_desc):
            new_desc = suggest_es_desc(title)
            if new_desc != current_desc:
                _insert_after_title(es, new_desc)
                changed = True
        return (changed, repaired)

    # Sinon pas de desc -> créer
    if title:
        # On génère direct une phrase naturelle
        new_desc = suggest_es_desc(title)
        _insert_after_title(es, new_desc)
        changed = True
    else:
        # Si aucun title, fallback minimal
        _insert_after_title(es, "Producto de uso cotidiano, práctico y fácil de incorporar a la rutina.")
        changed = True

    return (changed, repaired)

# ---------- Parcours JSON (évite de retraiter 'lang_desc') ----------
def process_object(obj: Any) -> Tuple[int, int, int]:
    changed_count = 0
    repaired_count = 0
    if isinstance(obj, dict):
        if "lang_desc" in obj and isinstance(obj["lang_desc"], dict):
            changed, repaired = ensure_desc_in_lang_desc(obj)
            if changed:
                changed_count += 1
            if repaired:
                repaired_count += 1
        for k, v in list(obj.items()):
            if k == "lang_desc":
                continue
            _, ch, rp = process_object(v)
            changed_count += ch
            repaired_count += rp
    elif isinstance(obj, list):
        for it in obj:
            _, ch, rp = process_object(it)
            changed_count += ch
            repaired_count += rp
    return (0, changed_count, repaired_count)

def process_file(fp: str) -> Tuple[int, int]:
    try:
        with open(fp, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"⚠️  Lecture JSON échouée: {fp} -> {e}")
        return (0, 0)

    _, changed_products, repaired_products = process_object(data)

    if changed_products or repaired_products:
        try:
            with open(fp, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"❌ Écriture échouée: {fp} -> {e}")
            return (0, 0)

    return (changed_products, repaired_products)

def main():
    if len(sys.argv) != 2:
        print("Usage:\n  python fix_predict_desc_iadetailed.py <chemin_fichier_ou_dossier>")
        sys.exit(1)

    target = sys.argv[1]
    files = collect_json_files(target)
    if not files:
        print("Aucun fichier JSON iAdetailed trouvé.")
        sys.exit(0)

    total_files = 0
    total_changed = 0
    total_repaired = 0

    for fp in files:
        changed, repaired = process_file(fp)
        total_files += 1
        total_changed += changed
        total_repaired += repaired
        print(f"• {os.path.relpath(fp)} → desc mises à jour/ajoutées: {changed}, réparations bug: {repaired}")

    print("\n=== RÉSUMÉ ===")
    print(f"Fichiers traités : {total_files}")
    print(f"Produits avec desc maj/ajout : {total_changed}")
    print(f"Produits réparés (imbrication lang_desc supprimée) : {total_repaired}")

if __name__ == "__main__":
    main()
