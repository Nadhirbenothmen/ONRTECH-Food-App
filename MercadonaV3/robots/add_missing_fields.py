import os
import re
import json

def parse_weight_from_format(format_str: str):
    """Extrait le poids total ou le nombre d’unités depuis le champ format."""
    if not format_str:
        return None

    format_str = format_str.lower().strip()
    format_str = format_str.replace("cáspulas", "cápsulas")

    # Cas spécial : "12 láminas (20 g)" → retourne 20 g (pas 240 g)
    match = re.search(r"\(\s*(\d+(?:[.,]\d+)?)\s*(g|gr|gramos|kg|ml|cl|l|litro|litros)(?:[^)]*escurrido|[^)]*neto)?\s*\)", format_str)
    if match:
        unit_weight = float(match.group(1).replace(",", "."))
        unit = match.group(2).strip()
        if unit in ["g", "gr", "gramo", "gramos"]:
            return unit_weight
        elif unit == "kg":
            return unit_weight * 1000
        elif unit in ["ml"]:
            return unit_weight
        elif unit in ["cl", "centilitro", "centilitros"]:
            return unit_weight * 10
        elif unit in ["l", "litro", "litros"]:
            return unit_weight * 1000
        return unit_weight

    # Cas type "pack 6x22,5 cl", "4×100 g"
    match = re.search(
        r"(?:pack|paquete|paquetes|caja|cajas|caixa|brick|bricks|mini|botellas?|latas?|sobres?|bolsas?)?\s*"
        r"(\d+)\s*(?:[a-zA-Z]*\s*)*[x×]\s*(\d+(?:[.,]\d+)?)\s*"
        r"(g|gr|gramos|kg|ml|cl|l|litro|litros)",
        format_str
    )
    if match:
        count = int(match.group(1))
        unit_weight = float(match.group(2).replace(",", "."))
        unit = match.group(3).strip()
    else:
        match = re.search(r"(\d+(?:[.,]\d+)?)\s*(g|gr|gramos|kg|ml|cl|l|litro|litros)", format_str)
        if match:
            count = 1
            unit_weight = float(match.group(1).replace(",", "."))
            unit = match.group(2).strip()
        else:
            match = re.search(
                r"(\d+)\s*(capsulas|cápsulas|comprimidos|viales|uds?|ud\.?|unid\.?|unidad(?:es)?|sobres?|monodosis|bolsitas?|pastillas|velas)",
                format_str
            )
            if match:
                return float(match.group(1))
            if re.fullmatch(r"(unidad|ud|ud\.|unid\.)", format_str):
                return 1.0
            match = re.search(r"(\d+)?\s*docena(?:s)?", format_str)
            if match:
                n = int(match.group(1)) if match.group(1) else 1
                return float(n * 12)
            match = re.search(r"frasco\s*(\d+)$", format_str)
            if match:
                return float(match.group(1))
            match = re.search(r"(\d+)\s*\+\s*\d+%?\s*g", format_str)
            if match:
                return float(match.group(1))
            if any(word in format_str for word in ["al peso", "al corte", "compra mínima", "aprox", "bandeja", "manojo"]):
                return None
            return None

    if unit in ["g", "gr", "gramo", "gramos"]:
        return count * unit_weight
    elif unit == "kg":
        return count * unit_weight * 1000
    elif unit in ["ml"]:
        return count * unit_weight
    elif unit in ["cl", "centilitro", "centilitros"]:
        return count * unit_weight * 10
    elif unit in ["l", "litro", "litros"]:
        return count * unit_weight * 1000

    return None

def compute_price_per_unit(weight_per_packaging, price_per_packaging, format_str):
    """Calcule le prix unitaire au kg, L ou pièce (corrigé pour capsules avec poids)."""
    if not weight_per_packaging or not price_per_packaging:
        return None

    fmt = format_str.lower() if format_str else ""

    if re.search(r"(g|gr|gramo|gramos|kg|ml|cl|l|litro|litros)", fmt):
        kg_or_litre = float(weight_per_packaging) / 1000.0
        if kg_or_litre > 0:
            return round(price_per_packaging / kg_or_litre, 2)

    if re.search(r"(capsulas|cápsulas|comprimidos|uds?|unid\.?|unidad(?:es)?|sobres?|monodosis|bolsitas?|pastillas|docena)", fmt):
        return round(price_per_packaging / float(weight_per_packaging), 2)

    kg = float(weight_per_packaging) / 1000.0
    if kg > 0:
        return round(price_per_packaging / kg, 2)

    return None

def extract_brand_from_title(title: str) -> str:
    if not title:
        return None

    title_clean = title.strip()
    title_clean = re.sub(r"\+\s*\d+\s*(mes(es)?|m)", "", title_clean, flags=re.IGNORECASE).strip()

    special_brands = ["Hacendado", "Puleva", "Président", "Nestlé", "Danone"]
    for sp in special_brands:
        if sp.lower() in title_clean.lower():
            return sp

    if "hacendado" in title_clean.lower():
        return "Hacendado"
    if "1897" in title_clean:
        return "Doble Malta"
    if "1906" in title_clean:
        return "1906"
    if "especial steinburg" in title_clean.lower():
        return "Especial Steinburg"
    if "coto de imaz" in title_clean.lower():
        return "Coto de Imaz"
    if "la mancha" in title_clean.lower():
        match = re.search(r"La Mancha\s+([A-ZÁÉÍÓÚÑ][\wáéíóúñ]+)", title_clean)
        if match:
            return f"La Mancha {match.group(1)}"
    if "queso de cabra" in title_clean.lower():
        return "Queso de Cabra"

    match = re.search(r"([A-ZÁÉÍÓÚÑ][\wáéíóúñ]+)\s*&\s*([A-ZÁÉÍÓÚÑ][\wáéíóúñ]+)", title_clean)
    if match:
        return f"{match.group(1)} & {match.group(2)}"

    words = title_clean.split()
    generic = {"café", "cacao", "papilla", "leche", "tónica", "agua", "bitter",
               "mineral", "cerveza", "cava", "brut", "vino", "pan", "integral", "trigo", "queso", "huevos"}

    candidates = [w for w in words if w and w[0].isupper() and w.lower() not in generic]

    if len(words) > 1 and candidates and candidates[0] == words[0]:
        candidates = candidates[1:]

    candidates = [w for w in candidates if w.upper() not in {"L", "M", "XL", "XXL", "S","B"}]

    if candidates:
        if len(candidates) >= 2:
            return " ".join(candidates[-2:])
        return candidates[-1]

    return "MERCADONA"

def is_animal_feed(title: str) -> bool:
    """Détecte si c’est un aliment pour animaux (petfood)."""
    t = title.lower()
    keywords = [
        "pienso", "mascota", "perro", "gato", "chien", "chat",
        "dog", "cat", "alimento animal", "alimentación animal",
        "croquetas", "petfood"
    ]
    return any(word in t for word in keywords)

def enrich_file_with_weight(fichier):
    updated = 0
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            data = json.load(f)

        modified = False
        products = data if isinstance(data, list) else [data]

        for product in products:
            title = product.get("title") or product.get("lang_desc", {}).get("es", {}).get("title", "")
            extracted_brand = extract_brand_from_title(title)
            old_brand = product.get("brand")

            if extracted_brand:
                if not old_brand or old_brand.strip().lower() != extracted_brand.lower():
                    product["brand"] = extracted_brand
                    modified = True
                    print(f"🏷️ Brand mis à jour : {old_brand} → {extracted_brand}")
            else:
                if not old_brand or old_brand.strip() == "":
                    product["brand"] = "MERCADONA"
                    modified = True
                    print(f"🏷️ Brand par défaut ajouté : MERCADONA")

            evolutions = product.get("evolutions", [])
            for evo in evolutions:
                if isinstance(evo, dict):
                    fmt = evo.get("format")
                    current_weight = evo.get("weight_per_packaging")
                    parsed_weight = parse_weight_from_format(fmt)
                    price_pack = evo.get("price_per_packaging")

                    if parsed_weight is not None:
                        evo["weight_per_packaging"] = parsed_weight
                        modified = True

                    print(f"\n🔎 EAN={product.get('ean')} | format={repr(fmt)} | actuel={current_weight} | calculé={parsed_weight}")

                    if price_pack not in [None, "", 0] and parsed_weight:
                        price_unit = compute_price_per_unit(parsed_weight, price_pack, fmt)
                        if price_unit:
                            evo["price_per_unit"] = price_unit
                            modified = True
                            print(f"💰 FORCÉ : price_per_unit recalculé = {price_unit}")
                    elif price_pack not in [None, "", 0]:
                        evo["price_per_unit"] = round(price_pack, 2)
                        modified = True
                        print(f"💰 Ajout forcé fallback price_per_unit = {price_pack}")

                    # 🔹 Nettoyage nutrition
                    nutrition = evo.get("nutrition")
                    if isinstance(nutrition, dict):
                        # supprimer vitamins
                        if "vitamins" in nutrition:
                            del nutrition["vitamins"]
                            modified = True
                            print(f"🧹 Champ 'vitamins' supprimé pour EAN={product.get('ean')}")
                        # garder seulement salt et calcium dans minerals
                        if "minerals" in nutrition and isinstance(nutrition["minerals"], dict):
                            nutrition["minerals"] = {k: v for k, v in nutrition["minerals"].items() if k in ["salt", "calcium"]}
                            modified = True
                            print(f"🧹 Nettoyage minerals (salt + calcium seulement) pour EAN={product.get('ean')}")

                    # 🔹 Aliment pour animaux → Nutri_Score = N/A
                    if is_animal_feed(title):
                        if evo.get("nutri_Score") != "N/A":
                            evo["nutri_Score"] = "N/A"
                            modified = True
                            print(f"🐾 Aliment animal détecté, Nutri_Score → N/A (EAN={product.get('ean')})")

        if modified:
            with open(fichier, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            updated += 1

    except Exception as e:
        print(f"⚠️ Erreur {fichier} : {e}")

    return updated

if __name__ == "__main__":
    chemin = input("📂 Chemin du fichier ou dossier JSON à enrichir : ").strip()
    if not os.path.exists(chemin):
        print("❌ Chemin invalide.")
    else:
        total_updated = 0
        if os.path.isfile(chemin):
            total_updated += enrich_file_with_weight(chemin)
        else:
            for root, _, files in os.walk(chemin):
                for file in files:
                    if file.endswith(".json"):
                        full_path = os.path.join(root, file)
                        total_updated += enrich_file_with_weight(full_path)

        print(f"\n📊 Mise à jour terminée. Fichiers modifiés : {total_updated}")
