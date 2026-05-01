#Correct Ersoki 
from dataclasses import asdict
import json
from operator import index
import os
from pathlib import Path
import re
import sys
import time
from turtle import up
from typing import List, Optional
import unicodedata

from numpy import average
import pycountry
import requests
from geotext import GeoText
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

from sympy import product

# Local imports
sys.path.append('src')
sys.path.append('./')
from src.countries.spain.DiaV3.model.product_dia import ALLERGENS
from src.utils.appium_utils import get_attribute_from_element, get_text_from_element, wait_el, wait_els
from src.countries.spain.EroskiV3.robots import static_data_V3, webdriverInstance
from src.countries.spain.EroskiV3.model.product_eroski import ProductEroski, MarketEroski,LabelEroski
from src.countries.spain.EroskiV3.model.product_content_eroski import NutritionEroski, ProductContentEroski,NutritionContentEroski
from src.model.product import (
    Category, Desc, Evolution, LangDesc, Links, Product, CustomerReviews,Offer,
    get_latest_parsed_products
)
from src.model.static_category_aisle import StaticAisle
from src.utils.my_utils import convert_to_float, dump_json_then_write_it_to_file

def get_categories_json_file_uri() -> Optional[str]:
    """
    Retourne le chemin absolu vers le fichier categories_dia.json.
    Utilise la position du script pour construire dynamiquement le chemin.
    """
    script_path = Path(__file__).resolve()           # Chemin complet du script actuel
    script_folder = script_path.parent               # Dossier contenant ce script
    parent_folder = script_folder.parent             # .../spain/EroskiV3/robots
    model_folder = os.path.join(parent_folder, 'model')  # .../model
    model_file = os.path.join(model_folder, 'categories_eroski_final.json')  # .../categories_eroski_final.json
    print(f"[DEBUG] 📄 categories_eroski_final.json path → {model_file}")
    return model_file


def find_category_hierarchy(categories_data: dict, category_id: str) -> Optional[dict]:
    """
    Recherche récursive d'une catégorie par ID et retourne
    l'arbre complet imbriqué depuis ce nœud,
    en garantissant toujours la clef 'subs' (liste).
    """
    def recursive_search(subs):
        for cat in subs:
            # Si c'est la feuille recherchée, on renvoie son id, son label
            # et sa liste de sous-catégories (vide si absente)
            if str(cat["id"]) == category_id:
                return {
                    "id": cat["id"],
                    "label": cat["label"],
                    "subs": cat.get("subs", [])
                }
            # Sinon, on descend dans ses enfants
            if "subs" in cat:
                result = recursive_search(cat["subs"])
                if result:
                    # On remonte en gardant la branche menant à la feuille
                    return {
                        "id": cat["id"],
                        "label": cat["label"],
                        "subs": [result]
                    }
        return None

    # On lance la recherche depuis la racine
    return recursive_search(categories_data.get("subs", []))



def find_category_for_url(categories_data: dict, product_url_or_aisle: str) -> Optional[List[dict]]:
    print(f"[DEBUG] URL à analyser pour catégorie : {product_url_or_aisle}")
    ids = re.findall(r'/(\d+)-', product_url_or_aisle)
    if not ids:
        print("[WARN] Aucun ID catégorie trouvé dans l'URL.")
        return None
    category_id = ids[-1]
    print(f"[DEBUG] ID catégorie extrait : {category_id}")
    hierarchy_tree = find_category_hierarchy(categories_data, category_id)
    if not hierarchy_tree:
        print(f"[WARN] ID catégorie {category_id} non trouvé dans categories_data.")
    return [hierarchy_tree] if hierarchy_tree else None

#OFFER

def extract_offer_as_object(driver) -> Optional[List[Offer]]:
    try:
        offer_el = wait_el(driver, By.CSS_SELECTOR, 'span.partner-price')
        offer_text = offer_el.text.strip().replace('\n', ' ')

        # Détection de quantité comme "2ª unidad", sinon 0 par défaut
        quantity_match = re.search(r"(\d+)[ªº]?\s*unidad", offer_text, re.IGNORECASE)
        required_quantity = int(quantity_match.group(1)) if quantity_match else 0

        if offer_text and any(c.isdigit() for c in offer_text):
            print(f"[DEBUG] Offre détectée : {offer_text} | Quantité requise : {required_quantity}")
            offer = Offer(
                id=None,
                description=LangDesc(es=Desc(desc=offer_text)),
                requiredProductQuantity=required_quantity
            )
            return [offer]
        else:
            print(f"[INFO] Offre ignorée car vide ou invalide : '{offer_text}'")
            return None
    except Exception:
        print("[INFO] Aucune offre promotionnelle détectée.")
        return None

#ORIGIN

# 🔁 Traduction manuelle de l'espagnol vers l'anglais
SPANISH_TO_ENGLISH_COUNTRY = {
    "francia": "France",
    "alemania": "Germany",
    "italia": "Italy",
    "portugal": "Portugal",
    "españa": "Spain",
    "espana": "Spain",
    "reino unido": "United Kingdom",
    "estados unidos": "United States",
    "paises bajos": "Netherlands",
    "suiza": "Switzerland",
    "belgica": "Belgium"
}

def normalize_country_name(name: str) -> str:
    nfkd_form = unicodedata.normalize('NFKD', name)
    return nfkd_form.encode('ASCII', 'ignore').decode('ASCII').lower().strip()

def get_country_code_from_country_name(raw_name: str) -> Optional[str]:
    name = normalize_country_name(raw_name)
    translated = SPANISH_TO_ENGLISH_COUNTRY.get(name, name)
    try:
        country = pycountry.countries.lookup(translated)
        return country.alpha_2
    except LookupError:
        print(f"[WARN] Aucun code ISO pour pays : {raw_name} (normalisé : {name})")
        return None

def extract_origin_structure_from_page(driver) -> dict:
    # 1️⃣ Extraction via "País de origen"
    try:
        country_blocks = driver.find_elements(By.CSS_SELECTOR, "div.feature-country")
        for block in country_blocks:
            try:
                title = block.find_element(By.CSS_SELECTOR, "span.title").text.strip().lower()
                if "país de origen" in title:
                    raw_country = block.find_element(By.CSS_SELECTOR, "p.text").text.strip()
                    print(f"[DEBUG] País de origen trouvé (corrigé) : {raw_country}")
                    iso = get_country_code_from_country_name(raw_country)
                    if iso:
                        print(f"[DEBUG] Code ISO détecté : {iso}")
                        return {"ean": [iso]}
            except Exception:
                continue
        print("[INFO] Champ 'País de origen' introuvable ou vide, fallback vers adresse")
    except Exception as e:
        print(f"[ERROR] Erreur recherche 'País de origen' : {e}")

    # 2️⃣ Fallback via bloc adresse fabricant
    try:
        p_elements = wait_els(driver, By.CSS_SELECTOR, "p.text")
        for idx, p in enumerate(p_elements):
            try:
                strong = wait_el(p, By.TAG_NAME, "strong").text.strip().lower()
                if "dirección" in strong or "direccion" in strong:
                    if idx + 1 < len(p_elements):
                        raw_address = p_elements[idx + 1].text.strip().lower()
                        print(f"[DEBUG] Adresse détectée : {raw_address}")

                        # 🎯 Code postal espagnol
                        match = re.search(r"\b(0[1-9]|[1-4][0-9]|5[0-2])\d{3}\b", raw_address)
                        if match:
                            print(f"[DEBUG] Code postal espagnol détecté : {match.group(0)} → ES")
                            return {"ean": ["ES"]}

                        # 🎯 Ville espagnole
                        known_cities = ["barcelona", "madrid", "coruña", "valencia", "arroniz", "siero"]
                        if any(city in raw_address for city in known_cities):
                            print("[DEBUG] Ville espagnole détectée → ES")
                            return {"ean": ["ES"]}

                        # 🎯 Nom de pays détecté dans l’adresse
                        for country in pycountry.countries:
                            if normalize_country_name(country.name) in raw_address:
                                print(f"[DEBUG] Pays détecté depuis adresse : {country.name} → {country.alpha_2}")
                                return {"ean": [country.alpha_2]}
            except:
                continue
    except Exception as e:
        print(f"[ERROR] Fallback adresse échoué : {e}")

    # 3️⃣ Par défaut, fallback générique
    return {"ean": ["ES"]}


def parse_weight_from_format(format_str: str):
    """Extrait le poids total ou le nombre d’unités depuis le champ format."""
    if not format_str:
        return None

    format_str = format_str.lower().strip()
    format_str = format_str.replace("cáspulas", "cápsulas")

    # Cas type "pack 6x22,5 cl", "4×100 g"
    match = re.search(r"(\d+)\s*[x×]\s*(\d+(?:[.,]\d+)?)\s*(g|gr|gramos|kg|ml|cl|l|litro|litros)", format_str)
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
                r"(\d+)\s*(capsulas|cápsulas|comprimidos|viales|uds?|ud\.?|unid\.?|unidad(?:es)?|sobres?|monodosis|bolsitas?|pastillas)",
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


class EroskiAislesProductsScanner:
    def __init__(self):
        self.total_products_number = 0

    @staticmethod
    def evolution_has_changed(old_evolution: Evolution, new_evolution: Evolution) -> bool:
        def nutrition_to_dict(nutrition):
            return nutrition.__dict__ if nutrition else None

        def offers_to_set(offers):
            return set(offers or [])

        return any([
            old_evolution.price_per_packaging != new_evolution.price_per_packaging,
            old_evolution.price_per_unit != new_evolution.price_per_unit,
            old_evolution.format != new_evolution.format,
            old_evolution.weight_per_packaging != new_evolution.weight_per_packaging,
            old_evolution.ingredients != new_evolution.ingredients,
            old_evolution.allergens != new_evolution.allergens,
            old_evolution.nutriscore != new_evolution.nutriscore,
            old_evolution.certification != new_evolution.certification,
            nutrition_to_dict(old_evolution.nutrition) != nutrition_to_dict(new_evolution.nutrition),
            offers_to_set(old_evolution.offers) != offers_to_set(new_evolution.offers),
        ])


    def scroll_and_load_all_products(self, driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        print("✅ Tous les produits ont été chargés.")

    def parse_products(self, driver: webdriver.Chrome, aisle: StaticAisle, parse_only_ean_title_url_price: bool,
                       parse_only_first_x_products: Optional[int] = None,
                       parse_only_from_index: Optional[int] = None,
                       latest_parsed_products: List[Product] = [],
                       categories_data: dict = None) -> List[Product]:
        
        aisle_url = aisle.url

        try:
            print(f"aisle_url: {aisle.url}")
            driver.get(aisle.url)
            time.sleep(2)
            try:
                accept_btn = driver.find_element(By.ID, "onetrust-accept-btn-handler")
                if accept_btn.is_displayed():
                    driver.execute_script("arguments[0].click();", accept_btn)
                    print("✅ Cookies acceptés")
            except: pass

            self.scroll_and_load_all_products(driver)

            products: List[Product] = []
            products_els = wait_els(driver, By.CSS_SELECTOR, 'div.col.border-0.product-item-lineal.item-type-1')
            print("Nombre de produits détectés :", len(products_els))

            original_window = driver.current_window_handle

            count_skipped = 0

            # récupère l’arbre imbriqué pour le rayon
            tree_for_aisle = find_category_for_url(categories_data, aisle_url) or []

            # aplatit cet arbre en une liste de dicts {"id","label"}
            flat_aisle = []
            def _flatten(nodes):
                for n in nodes:
                    flat_aisle.append({"id": n["id"], "label": n["label"]})
                    _flatten(n.get("subs", []))
            _flatten(tree_for_aisle)

            # crée les instances Category
            aisle_categories = [Category(id=c["id"], label=c["label"]) for c in flat_aisle]

            print(f"\n📂 Catégories aplaties pour le rayon ({aisle.name}):")
            for cat in aisle_categories:
                print(f"  - {cat.id} : {cat.label}")
            

            for index, product_el in enumerate(products_els):
                start_parsing_date = datetime.now()
                if parse_only_from_index and parse_only_from_index > index:
                    continue

                product_title = None
                product_url = None
                try:
                    title_el = wait_el(product_el, By.CSS_SELECTOR, 'h2.product-title a')
                    product_title = title_el.text.strip()
                    if not product_title:
                        product_title = title_el.get_attribute("textContent") or ""
                        product_title = product_title.strip()

                    product_url = title_el.get_attribute('href')
                    if product_url and not product_url.startswith("http"):
                        product_url = "https://supermercado.eroski.es" + product_url

                    product_id = None
                    if product_url:
                        match = re.search(r'/productdetail/(\d+)-', product_url)
                        if match:
                            product_id = match.group(1)
                except Exception as e:
                    print(f"[{index}] ⚠️ Erreur titre/URL : {e}")
                    continue



                try:
                    price_el = wait_el(product_el, By.CSS_SELECTOR, 'span.price-offer-now')
                    price_text = price_el.text.strip().replace('€', '').replace(',', '.').strip()
                    price_per_packaging = convert_to_float(price_text)
                    price_display = f"{price_per_packaging:.2f} €"
                except:
                    price_per_packaging = None
                    price_display = None

                print(f"[{index}] {product_title} | {price_display} | {product_url}")
                # 🔍 Construire l'arbre complet jusqu'à la catégorie de CE produit
                hierarchy_for_product = find_category_for_url(categories_data, product_url) or []
                if index == 0:
                    print("📂 Catégorie (produit) :")
                    print(json.dumps(hierarchy_for_product, indent=4, ensure_ascii=False))

                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[-1])
                driver.get(product_url)
                time.sleep(0.7)

                #Formats

                try:
                    full_title = wait_el(driver, By.CSS_SELECTOR, "h1.description-title").text

                    if ',' in full_title:
                        formats = full_title.split(',')[-1].strip()
                    else:
                        # Contenants + pack + poids/volume
                        pattern = re.compile(
                            r'(?:botella|lata|frasco|bote|caja|paquete|sobre|bandeja|tarro)\s*[a-zA-Z]*\s*\d+[.,]?\d*\s*(?:g|kg|ml|cl|l|unid|uds|monodosis)|'
                            r'(?:pack\s*\d*\s*(?:x\s*\d+)?\s*(?:g|kg|ml|cl|l|uds|unid))|'
                            r'(?:\d+\s*[x×]\s*\d+[.,]?\d*\s*(?:g|kg|ml|cl|l))|'
                            r'(?:compra mínima\s*\d+[.,]?\d*\s*(?:g|kg|ml|cl|l))',
                            re.IGNORECASE
                        )
                        match = pattern.search(full_title)
                        formats = match.group(0).strip() if match else None

                except:
                    formats = None
                                
                # weight_per_packaging

                weight_pack = None
                weight_per_packaging = None
                mesure_unit_for_packaging = None
                mesure_unit_for_price_per_unit = None

                try:
                    full_title = wait_el(driver, By.CSS_SELECTOR, "h1.description-title").text.strip()
                    match = re.search(r"(\d+[.,]?\d*)\s*(ml|g|l|litro|kg)", full_title, re.IGNORECASE)

                    if match:
                        value = float(match.group(1).replace(",", ".").strip())
                        unit = match.group(2).lower()

                        if unit == "ml":
                            weight_per_packaging = value
                            mesure_unit_for_packaging = "ml"
                            mesure_unit_for_price_per_unit = "l"

                        elif unit == "g":
                            weight_per_packaging = value
                            mesure_unit_for_packaging = "g"
                            mesure_unit_for_price_per_unit = "kg"

                        elif unit in ["l", "litro"]:
                            weight_per_packaging = value * 1000  # l → ml
                            mesure_unit_for_packaging = "ml"
                            mesure_unit_for_price_per_unit = "l"

                        elif unit == "kg":
                            weight_per_packaging = value * 1000  # kg → g
                            mesure_unit_for_packaging = "g"
                            mesure_unit_for_price_per_unit = "kg"

                    print(f"[{index}] ⚖️ Poids : {weight_per_packaging} {mesure_unit_for_packaging} | Prix/unité : {mesure_unit_for_price_per_unit}")

                except Exception as e:
                    print(f"[{index}] ❌ Impossible d'extraire le poids unitaire ")
                # 🔁 Fallback depuis le champ format si poids non fiable ou absent

                if (not weight_pack or weight_pack < 200) and formats:
                    weight_fallback = parse_weight_from_format(formats)
                    if weight_fallback:
                        weight_pack = weight_fallback
                        print(f"[{index}] 🧪 Fallback poids via format : {formats} → {weight_pack}")
                        if "ml" in formats.lower():
                            mesure_unit_for_packaging = "ml"
                        elif "g" in formats.lower() or "gramo" in formats.lower():
                            mesure_unit_for_packaging = "g"
                        elif "l" in formats.lower() or "litro" in formats.lower():
                            mesure_unit_for_packaging = "ml"
                        elif "kg" in formats.lower():
                            mesure_unit_for_packaging = "g"

                # 🔁 Déduction unité pour prix unitaire
                if mesure_unit_for_packaging == "ml":
                    mesure_unit_for_price_per_unit = "l"
                elif mesure_unit_for_packaging == "g":
                    mesure_unit_for_price_per_unit = "kg"

                # ⚖️ Extraction du prix unitaire depuis <p class="quantity-text">
                price_per_unit = None
                price_unit_text = None

                try:
                    qty_el = driver.find_element(By.CSS_SELECTOR, "p.quantity-text")
                    price_unit_text = qty_el.text.strip()  # ex: "1 KILO A 17,18 €"

                    # Normalisation : remplacer virgule et espaces insécables
                    cleaned_text = price_unit_text.replace(",", ".").replace("\xa0", " ").upper()

                    # Regex pour capter le nombre avant le €
                    match = re.search(r"([\d.]+)\s*€", cleaned_text)
                    if match:
                        price_per_unit = float(match.group(1))
                        print(f"[{index}] ✅ Prix unitaire extrait : {price_per_unit} ({price_unit_text})")
                except Exception:
                    # 🔁 fallback direct si la balise n'est pas trouvée
                    price_per_unit = price_per_packaging
                    print(f"[{index}] ℹ️ Fallback → price_per_unit = price_per_packaging ({price_per_unit})")


                """# ✅ Appel correct à get_packaging_info()
                mesure_unit_for_price_per_unit, matter, product_pricing_unit = ProductContentEroski.get_packaging_info(price_unit_text)
                print(f"[{index}] 📦 Unité de prix : {mesure_unit_for_price_per_unit}, matter: {matter}, pricing_unit: {product_pricing_unit}")"""


                #Ingredients

                try:
                    # Recherche du bloc contenant le span avec "Ingredientes"
                    ingredient_block = driver.find_element(By.XPATH, '//div[span[text()="Ingredientes"]]/p')
                    ingredients = ingredient_block.text.strip()
                except:
                    ingredients = None


                allergens_found = ProductContentEroski.detect_allergens(ingredients, ALLERGENS)
                print(f"[{index}] ⚠️ Allergènes détectés : {allergens_found}")

                #nutritional_info

                try:
                    nutritional_info = wait_el(driver,By.CSS_SELECTOR, "ul.list").text
                except:
                    nutritional_info = None

                #Storage conditions

                try:
                    storage_conditions = wait_el(driver,By.CSS_SELECTOR, "div.feature-text-preservation").text
                except:
                    storage_conditions = None

                #Country of origin

                try:
                    country_of_origin = wait_el(driver,By.CSS_SELECTOR, "div.feature-country p.text").text
                except:
                    country_of_origin = None

                #Mode d'emploi

                try:
                    mode_emploi = wait_el(driver,By.XPATH, '//span[text()="Modo de empleo"]/following-sibling::p[@class="text"]').text
                except:
                    mode_emploi = None

                #Fabricant

                try:
                    fabricante_block = wait_el(driver,By.XPATH, '//span[text()="Fabricante"]/parent::div')
                    raw_elements = wait_els(fabricante_block, By.CSS_SELECTOR, "p.text")
                    valid_texts = [el.text.strip() for el in raw_elements if el.text.strip() and not el.find_elements(By.XPATH, ".//*")]
                    manufacturer_name = valid_texts[0] if len(valid_texts) > 0 else None
                    manufacturer_address = valid_texts[1] if len(valid_texts) > 1 else None
                except:
                    manufacturer_name = None
                    manufacturer_address = None

                #Images

                images = []
                try:
                    image_els = driver.find_elements(By.CSS_SELECTOR, "div.product-thumbnails img")
                    for img_el in image_els:
                        img_url = img_el.get_attribute("data-bigimage")
                        if img_url and img_url.startswith("http"):
                            images.append(img_url)
                    if not images:
                        single_img = driver.find_element( By.CSS_SELECTOR, "img.product-big-image")
                        img_url = single_img.get_attribute("data-bigimage") or single_img.get_attribute("src")
                        if img_url:
                            images.append(img_url)
                except:
                    images = None

                #Reviews

                customer_rating = None
                customer_reviews_count = None
                review_url = None

                try:
                    # Bloc des étoiles affiché en haut
                    starbar = wait_el(driver, By.CSS_SELECTOR, "div.starbar")
                    full_stars = len(starbar.find_elements(By.CSS_SELECTOR, "div.star.checked"))
                    half_stars = len(starbar.find_elements(By.CSS_SELECTOR, "div.star.half-checked"))
                    customer_rating = full_stars + 0.5 * half_stars

                    reviews_text = starbar.text.strip()
                    reviews_match = re.search(r"(\d+)$", reviews_text)
                    if reviews_match:
                        customer_reviews_count = int(reviews_match.group(1))

                    print(f"[{index}] ⭐ Note client : {customer_rating} / {customer_reviews_count} avis")
                except Exception as e:
                    print(f"[{index}] ⚠️ Erreur avis visibles : {e}")

                # ✅ Vérifie que le bloc d'avis existe réellement dans le HTML
                try:
                    driver.find_element(By.ID, "ratingsZone")
                    review_url = product_url + "#ratingsZone"
                    print(f"[{index}] 🔗 Lien vers la section avis : {review_url}")
                except:
                    review_url = None
                    print(f"[{index}] ℹ️ Section #ratingsZone absente")

                
                nutrition_object = None
                nutriscore = "N/A"

                try:
                    if nutritional_info and isinstance(nutritional_info, str):
                        lines = nutritional_info.strip().split("\n")
                        cleaned_nutritional_info = {}

                        for line in lines:
                            line = line.strip()
                            match = re.match(r"^(.+?)\s+([\d.,]+)\s*([a-zA-Zµ%]*)", line)
                            if not match:
                                print(f"[WARN] Ligne ignorée (non parsable) : {line}")
                                continue

                            key = match.group(1).strip()
                            value_num = match.group(2).replace(",", ".").replace("\xa0", " ").strip()
                            unit = match.group(3).lower().strip() if match.group(3) else ""

                            # 🔹 Garder valeur + unité ensemble (ex: "0.09 g", "95 mg")
                            cleaned_value = f"{value_num} {unit}".strip()

                            # 🔹 Normaliser certaines clés
                            if key.lower() in ("ácidos grasos saturados", "grasas saturadas"):
                                key = "Grasas saturadas"

                            # 🔹 Cas particulier énergie
                            kl = key.lower()
                            if kl == "energía":
                                if "kcal" in unit or "kilocaloría" in line.lower():
                                    cleaned_nutritional_info["Energía (kcal)"] = cleaned_value
                                if "kj" in unit or "kilojulio" in line.lower():
                                    cleaned_nutritional_info["Energía (kJ)"] = cleaned_value
                                continue

                            # 🔹 Fallback énergie (si autre clé mais unité kcal/kj)
                            if "kcal" in unit or "kilocaloría" in line.lower():
                                key = "Energía (kcal)"
                            elif "kj" in unit or "kilojulio" in line.lower():
                                key = "Energía (kJ)"

                            cleaned_nutritional_info[key] = cleaned_value


                        # DEBUG affichage
                        print("[DEBUG] Données nutrition nettoyées :")
                        print(json.dumps(cleaned_nutritional_info, indent=4, ensure_ascii=False))

                        # Calcul Nutri-Score si infos valides
                        if cleaned_nutritional_info:
                            try:
                                nutriscore = ProductContentEroski.calculate_nutriscore_from_nested(cleaned_nutritional_info)
                                print(f"[{index}] 🥗 Nutri-Score calculé : {nutriscore}")
                            except Exception as e:
                                print(f"[{index}] ❌ Erreur calcul Nutri-Score : {e}")
                                nutriscore = "N/A"

                            # Conversion typée
                            try:
                                nutrition_object = NutritionEroski.convert_dict_to_nutrition_object(cleaned_nutritional_info)
                            except Exception as e:
                                print(f"[{index}] ❌ Erreur conversion Nutrition: {e}")
                                nutrition_object = None
                        else:
                            print(f"[{index}] ⚠️ Aucune donnée nutritionnelle utilisable trouvée.")
                    else:
                        print(f"[{index}] ⚠️ Données nutritionnelles absentes ou non valides.")
                except Exception as e:
                    print(f"[{index}] ❌ Erreur globale bloc nutrition : {e}")
                    nutrition_object = None
                    nutriscore = "N/A"

                # Labels
                
                final_label = LabelEroski()
                try:
                    label_input_dict = {
                        "title": product_title,
                        "details": {
                            "ingredients": ingredients,
                        }
                    }
                    try:
                        label_textual = LabelEroski.from_dict_to_object(label_input_dict)
                    except Exception:
                        label_textual = LabelEroski()
                    final_label = label_textual
                except Exception as e:
                    print(f"[{index}] ⚠️ Erreur lors de l'extraction des labels textuels : {e}")
                    final_label = LabelEroski()

                # Assure que label_dict est toujours défini
                label_dict = {}
                for key in LabelEroski.__annotations__.keys():
                    value = getattr(final_label, key, None)
                    if isinstance(value, bool):
                            label_dict[key] = value  # inclut True ou False

                print(f"[{index}] 🏷️ Labels (complet) : {json.dumps(label_dict, ensure_ascii=False)}")



                link = Links(links_self=product_url, reviews=review_url)
                lang_desc = LangDesc(es=Desc(title=product_title, links=link, images=images))
                reviews = CustomerReviews(average=customer_rating, count=customer_reviews_count)

                if not weight_pack and formats:
                    weight_pack = parse_weight_from_format(formats)

                offers = extract_offer_as_object(driver)

                # Vérification de l'ancienne évolution (si elle existe)
                if latest_parsed_products:
                    old_evolution = latest_parsed_products[0].evolutions[-1]  # Dernière évolution du produit précédent
                else:
                    old_evolution = None

                # Calcul de created_at et updated_at
                created_at = datetime.now().strftime("%Y-%m-%dT%H:%M")
                updated_at = created_at  # Initialement égal à created_at
                new_evolution = Evolution(price_per_packaging=price_per_packaging,
                                      price_per_unit=price_per_unit,
                                      format=formats,
                                      weight_per_packaging=weight_pack,
                                      ingredients=ingredients,
                                      allergens=allergens_found,
                                      nutri_Score=nutriscore,
                                      nutrition=nutrition_object,
                                      reviews=reviews,
                                      offers=offers)

                # Mettre à jour updated_at seulement si une évolution a eu lieu
                if old_evolution and self.evolution_has_changed(old_evolution, new_evolution):
                    updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M")
                
                unit, matter, product_price_unit = ProductContentEroski.get_packaging_info(mesure_unit_for_packaging)
                marque = ProductContentEroski.extract_brand_from_title(driver, index)
                origin = extract_origin_structure_from_page(driver)

                # ✅ Parsing_duration ici
                end_parsing_date = datetime.now()
                parsing_duration = (end_parsing_date - start_parsing_date).seconds 

                """# juste après avoir calculé hierarchy_for_aisle
                print("DEBUG ➡️ categories going into Product:")
                print(json.dumps(hierarchy_for_aisle, indent=4, ensure_ascii=False))"""
                
                product = Product(ean=product_id, lang_desc=lang_desc, brand=marque,
                                  market=MarketEroski(),mesure_unit_for_price_per_unit=mesure_unit_for_price_per_unit,mesure_unit_for_packaging=mesure_unit_for_packaging,
                                  matter = matter , label= label_dict, origin=origin,parsing_duration=parsing_duration,
                                  created_at=created_at,updated_at=updated_at,categories= aisle_categories,
                                  )
                
                # juste après avoir construit product
                print("DEBUG ➡️ product.categories brut:")
                print(product.categories)   # liste d'instances Category

                print("DEBUG ➡️ product.categories converti en dicts:")
                print([asdict(cat) for cat in product.categories])

                product.evolutions = [new_evolution]
                products.append(product)


                driver.close()
                driver.switch_to.window(original_window)

                if parse_only_first_x_products and len(products) >= parse_only_first_x_products:
                    break

                time.sleep(0.1)

            print(f"✅ Extraction terminée : {len(products)} produits enregistrés, {count_skipped} ❌ ignorés.")

            return products

        except Exception as e:
            print(f"❌ Erreur analyse produits : {e}")
            return []

if __name__ == "__main__":
    print("my main")
    cmdargs = sys.argv
    print(f"The total numbers of args passed to the script: {len(cmdargs)}, Args list: {cmdargs}")

    # ✅ Charger le JSON des catégories DIA
    json_path = get_categories_json_file_uri()
    print(f"✅ Chemin du fichier JSON des catégories Mercadona : {json_path}")
    with open(json_path, "r", encoding="utf-8") as f:
        categories_data = json.load(f)

    if len(cmdargs) > 1:
        eroski = EroskiAislesProductsScanner()
        parser_name = cmdargs[1]
        parser_class = getattr(static_data_V3, parser_name)
        aisles: List[StaticAisle] = parser_class.aisles
        print(f"aisles: {len(aisles)}")

        if not aisles:
            print("empty aisles")
            sys.exit()

        # Filtrage d’un seul rayon via son identifiant (ex: SALADS_AND_PREPARED_VEGETABLES)
        only_one_aisle = None
        if "--only_one_aisle" in cmdargs:
            idx = cmdargs.index("--only_one_aisle")
            only_one_aisle = cmdargs[idx + 1]
            print(f"➡️ Filtrage activé sur un seul rayon : {only_one_aisle}")

        category_folder_path = os.path.normpath(parser_class.category_path())
        os.makedirs(category_folder_path, exist_ok=True)

        for aisle_code, aisle in parser_class.__dict__.items():
            if not isinstance(aisle, StaticAisle) or not aisle.url:
                continue

            if only_one_aisle and aisle_code != only_one_aisle:
                print(f"⏭️ Rayon ignoré (filtrage actif) : {aisle.name}")
                continue

            print(f"➡️ Rayon traité : {aisle.name} (code: {aisle_code})")
            latest_parsed_products: List[Product] = []
            if "get_latest_parsed_products" in cmdargs:
                latest_parsed_products = get_latest_parsed_products(aisle=aisle)

            now = datetime.now().strftime("%d_%m_%y_%H_%M_%S")
            base = aisle.name.replace("&", "and").replace(" ", "_")
            aisle_filename = f"{base}_{now}.json"

            aisle_uri = os.path.join(category_folder_path, aisle_filename)


            parse_only_ean_title_url_price = "parse_only_ean_title_url_price" in cmdargs
            parse_only_first_x_products = None
            if "parse_only_first_x_products" in cmdargs:
                index = cmdargs.index("parse_only_first_x_products")
                parse_only_first_x_products = int(cmdargs[index + 1])
            parse_only_from_index = None

            new_products = eroski.parse_products(
                webdriverInstance,
                aisle,
                parse_only_ean_title_url_price,
                parse_only_first_x_products,
                parse_only_from_index,
                latest_parsed_products,
                categories_data
            )

            # 💾 Sauvegarde du fichier JSON
            # ✅ Préparation finale du fichier avec ID des catégories remappées en "Lxxx"
            def prune_none(obj):
                if isinstance(obj, dict):
                    return { k: prune_none(v) for k, v in obj.items() if v is not None }
                if isinstance(obj, list):
                    return [prune_none(v) for v in obj]
                return obj

            # --- Génération finale du JSON sans les None, en conservant intact la hiérarchie subs ---
            output = []
            for p in new_products:
                d = asdict(p)
                # on ne recalcule plus raw_hierarchy : on réutilise p.categories qui est déjà plat
                d["categories"] = d["categories"]
                cleaned = prune_none(d)
                output.append(cleaned)

            with open(aisle_uri, "w", encoding="utf-8") as f:
                json.dump(output, f, indent=4, ensure_ascii=False)


            print(f"✅ Fichier écrit : {aisle_uri} ({len(output)} produits)")
    else:
        print("wrong args number")
        sys.exit()