import os
import re
import json

def parse_weight_from_format(format_str: str):
    """Extrait le poids total ou le nombre d’unités depuis le champ format."""
    if not format_str:
        return None

    format_str = format_str.lower().strip()
    format_str = format_str.replace("cáspulas", "capsulas")

    # Cas type "pack 6x22,5 g" ou "4×100 ml"
    match = re.search(r"(\d+)\s*[x×]\s*(\d+(?:[.,]\d+)?)\s*(g|gr|gramos|kg|ml|cl|l|litros?)", format_str)
    if match:
        count = int(match.group(1))
        unit_weight = float(match.group(2).replace(",", "."))
        unit = match.group(3).strip()
    else:
        # Cas simple comme "18,4 g" ou "caja 27,5 g"
        matches = re.findall(r"(\d+(?:[.,]\d+)?)\s*(g|gr|gramos|kg|ml|cl|l|litros?)", format_str)
        if matches:
            count = 1
            unit_weight = float(matches[-1][0].replace(",", "."))  # prend le dernier nombre avant l’unité
            unit = matches[-1][1].strip()

        else:
            # Cas unités (capsules, sobres, etc.)
            match = re.search(
                r"(\d+)\s*(capsulas|cápsulas|comprimidos|viales|uds?|ud\.?|unid\.?|unidad(?:es)?|sobres?|monodosis|bolsitas?|pastillas)",
                format_str
            )
            if match:
                return float(match.group(1))

            if re.fullmatch(r"(unidad|ud|ud\.|unid\.)", format_str):
                return 1.0

            # Cas "docena"
            match = re.search(r"(\d+)?\s*docena(?:s)?", format_str)
            if match:
                n = int(match.group(1)) if match.group(1) else 1
                return float(n * 12)

            # Cas "frasco 12"
            match = re.search(r"frasco\s*(\d+)$", format_str)
            if match:
                return float(match.group(1))

            # Cas "200 + 50 g"
            match = re.search(r"(\d+)\s*\+\s*\d+%?\s*g", format_str)
            if match:
                return float(match.group(1))

            if any(word in format_str for word in ["al peso", "al corte", "compra mínima", "aprox", "bandeja", "manojo"]):
                return None

            return None

    # Conversion en grammes / ml
    if unit in ["g", "gr", "gramo", "gramos"]:
        return count * unit_weight
    elif unit == "kg":
        return count * unit_weight * 1000
    elif unit == "ml":
        return count * unit_weight
    elif unit == "cl":
        return count * unit_weight * 10
    elif unit in ["l", "litro", "litros"]:
        return count * unit_weight * 1000

    return None



def compute_price_per_unit(weight_per_packaging, price_per_packaging, format_str):
    """Calcule le prix unitaire en €/kg, €/L ou €/pièce selon le format."""
    if not weight_per_packaging or not price_per_packaging:
        return None

    fmt = format_str.lower() if format_str else ""

    # Cas poids → toujours convertir en kg
    if any(u in fmt for u in ["g", "kg", "gramo", "gramos"]):
        kg = weight_per_packaging / 1000.0
        return round(price_per_packaging / kg, 2) if kg > 0 else None

    # Cas volume → toujours convertir en L
    if any(u in fmt for u in ["ml", "cl", "l", "litro", "litros"]):
        litres = weight_per_packaging / 1000.0
        return round(price_per_packaging / litres, 2) if litres > 0 else None

    # Cas unités (capsules, sobres, etc.)
    if re.search(r"(capsulas|cápsulas|comprimidos|viales|uds?|ud\.?|unid\.?|unidad(?:es)?|sobres?|monodosis|bolsitas?|pastillas|docena)", fmt):
        return round(price_per_packaging / weight_per_packaging, 2)

    # Fallback générique : assume grammes → kg
    kg = weight_per_packaging / 1000.0
    return round(price_per_packaging / kg, 2) if kg > 0 else None


def compute_nutriscore(nutrition: dict) -> str:
    """Calcule le Nutri-Score (A-E) depuis un dict nutrition (sel en mg)."""
    if not nutrition or not isinstance(nutrition, dict):
        return "N/A"

    try:
        energies = nutrition.get("energies", {})
        kcal = energies.get("kcal", 0) or 0
        kj = energies.get("kj", kcal * 4.184) if kcal else energies.get("kj", 0)

        minerals = nutrition.get("minerals", {})
        # ⚠️ salt en mg → conversion en grammes
        salt_mg = minerals.get("salt", 0) or 0
        salt = salt_mg / 1000.0  

        fats = nutrition.get("fats", {})
        saturates = fats.get("saturates", 0) or 0

        carbs = nutrition.get("carbohydrates", {})
        sugars = carbs.get("sugars", carbs.get("of_which_sugars", 0)) or 0

        proteins = nutrition.get("proteins", {}).get("proteins", 0) or 0
        fibers = carbs.get("dietary_fiber", 0) or 0

        # === Points négatifs (A) ===
        pts_energy = 0
        if kj > 3350: pts_energy = 10
        elif kj > 3015: pts_energy = 9
        elif kj > 2680: pts_energy = 8
        elif kj > 2345: pts_energy = 7
        elif kj > 2010: pts_energy = 6
        elif kj > 1675: pts_energy = 5
        elif kj > 1340: pts_energy = 4
        elif kj > 1005: pts_energy = 3
        elif kj > 670: pts_energy = 2
        elif kj > 335: pts_energy = 1

        pts_sugar = 0
        if sugars > 45: pts_sugar = 10
        elif sugars > 40: pts_sugar = 9
        elif sugars > 36: pts_sugar = 8
        elif sugars > 31: pts_sugar = 7
        elif sugars > 27: pts_sugar = 6
        elif sugars > 22.5: pts_sugar = 5
        elif sugars > 18: pts_sugar = 4
        elif sugars > 13.5: pts_sugar = 3
        elif sugars > 9: pts_sugar = 2
        elif sugars > 4.5: pts_sugar = 1

        pts_satfat = 0
        if saturates > 10: pts_satfat = 10
        elif saturates > 9: pts_satfat = 9
        elif saturates > 8: pts_satfat = 8
        elif saturates > 7: pts_satfat = 7
        elif saturates > 6: pts_satfat = 6
        elif saturates > 5: pts_satfat = 5
        elif saturates > 4: pts_satfat = 4
        elif saturates > 3: pts_satfat = 3
        elif saturates > 2: pts_satfat = 2
        elif saturates > 1: pts_satfat = 1

        pts_salt = 0
        if salt > 4.5: pts_salt = 10
        elif salt > 4: pts_salt = 9
        elif salt > 3.5: pts_salt = 8
        elif salt > 3: pts_salt = 7
        elif salt > 2.5: pts_salt = 6
        elif salt > 2: pts_salt = 5
        elif salt > 1.5: pts_salt = 4
        elif salt > 1: pts_salt = 3
        elif salt > 0.5: pts_salt = 2
        elif salt > 0.12: pts_salt = 1

        neg_points = pts_energy + pts_sugar + pts_satfat + pts_salt

        # === Points positifs (C) ===
        pts_fiber = 0
        if fibers > 4.7: pts_fiber = 5
        elif fibers > 3.7: pts_fiber = 4
        elif fibers > 2.8: pts_fiber = 3
        elif fibers > 1.9: pts_fiber = 2
        elif fibers > 0.9: pts_fiber = 1

        pts_prot = 0
        if proteins > 8: pts_prot = 5
        elif proteins > 6.4: pts_prot = 4
        elif proteins > 4.8: pts_prot = 3
        elif proteins > 3.2: pts_prot = 2
        elif proteins > 1.6: pts_prot = 1

        pos_points = pts_fiber + pts_prot

        # === Score final ===
        score = neg_points - pos_points

        # === Conversion score → lettre ===
        if score <= -1: return "A"
        elif score <= 2: return "B"
        elif score <= 10: return "C"
        elif score <= 18: return "D"
        else: return "E"

    except Exception:
        return "N/A"

def extract_brand_from_title(title: str) -> str:
    """
    Détecte la marque dans le titre.
    - Si des mots en majuscules sont trouvés → retourne la dernière occurence.
    - Sinon → retourne "EROSKI" par défaut.
    """
    if not title:
        return "EROSKI"

    # Cherche tous les groupes en majuscules (y compris accents, 2 lettres minimum)
    candidates = re.findall(r"\b([A-ZÁÉÍÓÚÑÜ]{2,}(?:\s+[A-ZÁÉÍÓÚÑÜ]{2,})*)\b", title)

    if candidates:
        return candidates[-1].strip()

    return "EROSKI"


def enrich_file_with_weight(fichier):
    updated = 0
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            data = json.load(f)

        modified = False
        products = data if isinstance(data, list) else [data]

        for product in products:
            # === Correction brand ===
            title_full = product.get("title") or product.get("lang_desc", {}).get("es", {}).get("title", "")
            if title_full:
                old_brand = product.get("brand")
                new_brand = extract_brand_from_title(title_full)
                if new_brand != old_brand:
                    product["brand"] = new_brand
                    modified = True
                    print(f"🏷️ Brand corrigée : {old_brand} → {new_brand} (EAN={product.get('ean')})")

            evolutions = product.get("evolutions", [])
            for evo in evolutions:
                if not isinstance(evo, dict):
                    continue

                fmt = evo.get("format")
                # === Correction format si trop générique ===
                if fmt and re.fullmatch(r"\d+(?:[.,]\d+)?\s*(g|kg|ml|cl|l|litros?)", fmt.strip()):
                    match = re.search(r"(caja|bolsa|pack|botella|sobre|lata|frasco|bandeja).*?\d+(?:[.,]\d+)?\s*(g|kg|ml|cl|l|litros?)",
                                      title_full.lower())
                    if match:
                        new_fmt = match.group(0)
                        if new_fmt != fmt.lower():
                            evo["format"] = new_fmt
                            modified = True
                            print(f"📦 Format corrigé : {fmt} → {new_fmt} (EAN={product.get('ean')})")
                            fmt = new_fmt  # mettre à jour la variable locale

                current_weight = evo.get("weight_per_packaging")
                parsed_weight = parse_weight_from_format(fmt or title_full)
                # Mettre à jour le weight_per_packaging si calculé et différent
                if parsed_weight and (current_weight in [None, 0] or abs(current_weight - parsed_weight) > 0.01):
                    evo["weight_per_packaging"] = parsed_weight
                    modified = True
                    print(f"⚖️ Corrigé weight_per_packaging = {parsed_weight} (ancien={current_weight}, fmt={fmt})")


                price_pack = evo.get("price_per_packaging")

                print(f"\n🔎 EAN={product.get('ean')} | format={repr(fmt)} | actuel={current_weight} | calculé={parsed_weight}")

                # Cas 1 : poids détecté + prix dispo
                if price_pack not in [None, "", 0]:
                    price_unit = compute_price_per_unit(parsed_weight, price_pack, fmt)
                    if price_unit:
                        current_price_unit = evo.get("price_per_unit")
                        if current_price_unit in [None, "", 0] or abs(current_price_unit - price_unit) > 0.01:
                            evo["price_per_unit"] = price_unit   # ✅ met directement à jour
                            modified = True
                            print(f"💰 Corrigé price_per_unit = {price_unit} (ancien={current_price_unit}, fmt={fmt})")


                # Cas 2 : pas de poids exploitable → fallback = price_per_packaging
                elif price_pack not in [None, "", 0]:
                    new_evo = {}
                    for k, v in evo.items():
                        new_evo[k] = v
                        if k == "price_per_packaging":
                            new_evo["price_per_unit"] = round(price_pack, 2)
                    evo.clear()
                    evo.update(new_evo)

                    print(f"💰 Ajout fallback price_per_unit = {price_pack} (pas de poids détecté, fmt={fmt})")
                    modified = True

            # === Déterminer l'unité de mesure au niveau produit ===
            title = product.get("title", "").lower()
            fmt_all = " ".join([str(evo.get("format", "")).lower() for evo in evolutions])

            mesure_unit_for_packaging = None
            mesure_unit_for_price_per_unit = None

            if re.search(r"\b(ml|cl|l)\b", fmt_all):
                mesure_unit_for_packaging = "ml"
                mesure_unit_for_price_per_unit = "l"

            elif re.search(r"\b(kg|g|gramo|gramos)\b", fmt_all):
                mesure_unit_for_packaging = "g"
                mesure_unit_for_price_per_unit = "kg"

            elif re.search(r"(\d+\s*)?(uds?|ud\.?|unid\.?|unidad(?:es)?|comprimidos?|capsulas?|cápsulas?|sobres?|monodosis)", title, re.IGNORECASE) \
                or re.search(r"(\d+\s*)?(uds?|ud\.?|unid\.?|unidad(?:es)?|comprimidos?|capsulas?|cápsulas?|sobres?|monodosis)", fmt_all, re.IGNORECASE):
                mesure_unit_for_packaging = "piece"
                mesure_unit_for_price_per_unit = "piece"

            elif "frasco" in title or "frasco" in fmt_all:
                mesure_unit_for_packaging = "g"
                mesure_unit_for_price_per_unit = "kg"

            elif "manojo" in title or "manojo" in fmt_all:
                mesure_unit_for_packaging = "piece"
                mesure_unit_for_price_per_unit = "piece"

            elif any(word in title for word in ["al peso", "al corte", "aprox", "cuña"]) \
                or any(word in fmt_all for word in ["al peso", "al corte", "aprox", "cuña"]):
                mesure_unit_for_packaging = "piece"
                mesure_unit_for_price_per_unit = "piece"

            elif re.search(r"\b(docena|docenas)\b", title) or re.search(r"\b(docena|docenas)\b", fmt_all):
                mesure_unit_for_packaging = "piece"
                mesure_unit_for_price_per_unit = "piece"

            # === Ajouter matter + unités ===
            if mesure_unit_for_packaging and mesure_unit_for_price_per_unit:
                if mesure_unit_for_packaging == "ml":
                    matter = "LIQUID"
                elif mesure_unit_for_packaging == "g":
                    matter = "SUBSTANCE"
                elif mesure_unit_for_packaging == "piece":
                    matter = "PIECE"
                else:
                    matter = None

                new_product = {}
                for k, v in product.items():
                    if k == "origin":
                        new_product["origin"] = v
                        if matter:
                            new_product["matter"] = matter
                    elif k == "label":
                        new_product["mesure_unit_for_packaging"] = mesure_unit_for_packaging
                        new_product["mesure_unit_for_price_per_unit"] = mesure_unit_for_price_per_unit
                        new_product["label"] = v
                    else:
                        new_product[k] = v

                product.clear()
                product.update(new_product)
                modified = True
                print(f"📐 Ajout unités: packaging={mesure_unit_for_packaging}, "
                      f"price_per_unit={mesure_unit_for_price_per_unit}, matter={matter}")

                # === Ajout Nutri-Score ===
                for evo in evolutions:
                    ns = evo.get("nutri_Score")
                    if ns in [None, "", "N/A", "unknow", "_"]:
                        ns_calc = compute_nutriscore(evo.get("nutrition", {}))
                        if ns_calc and ns_calc not in ["N/A", None]:
                            evo["nutri_Score"] = ns_calc
                            print(f"🥗 Nutri-Score ajouté pour {product.get('ean')} = {ns_calc}")
                            modified = True

        # === Sauvegarde si modifications ===
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
