#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import asdict, is_dataclass
from datetime import datetime 
import os
from pathlib import Path
import sys
import time
import re
import json
from typing import List, Optional

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException

sys.path.append('src')
sys.path.append('./')

from src.countries.spain.MercadonaV3.robots import static_data_V3
from src.countries.spain.MercadonaV3.model.product_mercadona import ProductMercadona,  LabelMercadona , MarketMercadona
from src.countries.spain.MercadonaV3.model.product_content_mercadona import ProductContentMercadona , NutritionContentMercadona , NutritionMercadona 
from src.model.product import Desc, Evolution, LangDesc, Links, Product, get_latest_parsed_products
from src.model.static_category_aisle import StaticAisle
from src.utils.appium_utils import get_attribute_from_element, get_text_from_element, wait_el, wait_els
from src.utils.my_utils import convert_to_float, dump_json_then_write_it_to_file


def get_categories_json_file_uri() -> Optional[str]:
    """
    Retourne le chemin absolu vers le fichier categories_dia.json.
    Utilise la position du script pour construire dynamiquement le chemin.
    """
    script_path = Path(__file__).resolve()           # Chemin complet du script actuel
    script_folder = script_path.parent               # Dossier contenant ce script
    parent_folder = script_folder.parent             # Chemin du dossier parent (src/countries/spain/MercadonaV3/robots)
    model_folder = os.path.join(parent_folder, 'model')  # .../model
    model_file = os.path.join(model_folder, 'categories_mercadona.json')  # .../categories_dia.json
    print(f"[DEBUG] 📄 categories_mercadona.json path → {model_file}")
    return model_file


def find_category_for_url(categories_data: dict, product_url_or_aisle: str) -> Optional[List[dict]]:
    # Extraire le dernier segment numérique de l’URL (ex: "147" depuis ".../categories/147")
    match = re.search(r'/categories/(\d+)', product_url_or_aisle)
    if not match:
        return None

    category_id = match.group(1)

    for main_cat in categories_data.get("subs", []):
        for sub in main_cat.get("subs", []):
            if str(sub.get("id")) == category_id:
                return [
                    {"id": str(main_cat["id"]), "label": main_cat["label"]},
                    {"id": str(sub["id"]), "label": sub["label"]}
                ]
    return None


def handle_initial_popup(driver, postal_code="28001"):
    driver.get("https://tienda.mercadona.es")
    wait = WebDriverWait(driver, 30)
    try:
        try:
            accept_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Aceptar')]")))
            accept_button.click()
            print("✅ Cookies acceptés")
        except:
            print("ℹ️ Pas de bouton cookies ou déjà accepté.")

        postal_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-label="Código postal"]')))
        postal_input.clear()
        postal_input.send_keys(postal_code)

        for _ in range(6):
            try:
                continuar_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="postal-code-checker-button"]')
                if continuar_button.is_enabled():
                    continuar_button.click()
                    print("➡️ Bouton CONTINUAR cliqué.")
                    break
            except:
                time.sleep(5)

        WebDriverWait(driver, 20).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, 'input[aria-label="Código postal"]'))
        )
        print("✅ Catalogue chargé avec succès")
    except Exception as e:
        print(f"❌ Erreur initiale : {type(e).__name__}")
        driver.quit()
        sys.exit(1)


def get_product_title(driver, timeout=6) -> str:
    try:
        h1_el = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h1.title2-b.private-product-detail__description"))
        )
        return h1_el.text.strip()
    except:
        return None
    
def format_origin(ean_country_code: Optional[str]) -> dict:
    """
    Format l'origine du produit dans la structure attendue :
    {
        "origin": {
            "ean": ["ES"]
        }
    }
    """
    if ean_country_code:
        return {"ean": [ean_country_code.upper()]}
    else:
        return {"ean": []}


def scroll_to_bottom(driver, pause_time=1.5, max_tries=10):
    last_height = driver.execute_script("return document.body.scrollHeight")
    tries = 0
    while tries < max_tries:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            tries += 1
        else:
            tries = 0
            last_height = new_height


class MercadonaAislesProductsScanner:

    def extract_packaging_info(self, format_text: str) -> tuple[str | None, float | None]:
        """
        Retourne : (unité normalisée ('g' ou 'ml'), poids total en grammes ou millilitres)
        """
        if not format_text:
            return (None, None)

        format_text = format_text.lower().replace(",", ".").strip()

        # Cas multi-unité : ex. "3 mini bricks x 330 ml"
        match_multi = re.search(r'(\d+)[^\d]{0,20}[xX×][^\d]{0,20}([\d.]+)\s*(ml|l|cl|g|kg)', format_text)
        if match_multi:
            count = int(match_multi.group(1))
            value = float(match_multi.group(2))
            unit = match_multi.group(3)
        else:
            # Cas simple : 250g, 1.5 L, etc.
            match_single = re.search(r'([\d.]+)\s*(ml|l|cl|g|kg)', format_text)
            if not match_single:
                return (None, None)
            count = 1
            value = float(match_single.group(1))
            unit = match_single.group(2)

        total = value * count

        # Normalisation vers "g" ou "ml" uniquement
        if unit == "kg":
            total *= 1000
            normalized_unit = "g"
        elif unit == "l":
            total *= 1000
            normalized_unit = "ml"
        elif unit == "cl":
            total *= 10
            normalized_unit = "ml"
        elif unit == "g":
            normalized_unit = "g"
        elif unit == "ml":
            normalized_unit = "ml"
        else:
            return (None, None)

        return (normalized_unit, total)
    
        # Fonction de détection de changement dans les évolutions
    @staticmethod
    def detect_change(old_evolution: Evolution, new_evolution: Evolution) -> bool:
        return (
            old_evolution.price_per_packaging != new_evolution.price_per_packaging or
            old_evolution.price_per_unit != new_evolution.price_per_unit or
            old_evolution.format != new_evolution.format or
            old_evolution.weight_per_packaging != new_evolution.weight_per_packaging
        )
    
    def parse_products(self, driver: webdriver.Chrome, aisle: StaticAisle, parse_only_ean_title_url_price: bool,
                       parse_only_first_x_products: Optional[int] = None,
                       parse_only_from_index: Optional[int] = None,
                       latest_parsed_products: List[Product] = [],
                       categories_data: dict = None) -> List[Product]:
        
        aisle_url = aisle.url
        driver.get(aisle.url)
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "section[data-testid='section']")))
        scroll_to_bottom(driver)

        products: List[Product] = []
        count_skipped = 0

        start_parsing_date = datetime.now()
        
        product_els = wait_els(driver, By.CSS_SELECTOR, 'div.product-cell')

        print("Nombre de produits détectés :", len(product_els))
       
        for index, product_el in enumerate(product_els):
                if parse_only_from_index and index < parse_only_from_index:
                    continue

                try:
                    btn_el = wait_el(product_el, By.CSS_SELECTOR, 'button[data-testid="open-product-detail"]')
                    driver.execute_script("arguments[0].click();", btn_el)
                    time.sleep(1.5)

                    product_title = get_product_title(driver)
                    
                    product_url = driver.current_url
                    product_id = re.search(r'/product/(\d+)', product_url).group(1) if "/product/" in product_url else None

                    # 📸 images
                    image_urls = []
                    try:
                        thumbs = WebDriverWait(driver, 5).until(
                            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.product-gallery-thumbnails img[src*="imgix.net"]'))
                        )
                        image_urls = [img.get_attribute('src') for img in thumbs if img.get_attribute('src')]
                    except:
                        pass

                    # 💶 price per unit
                    price_weight_text = None
                    price_per_unit = None
                    try:
                        spans = driver.find_elements(By.CSS_SELECTOR, 'span.headline1-r')
                        for span in spans:
                            txt = span.text.strip()
                            match = re.search(r'([\d,.]+)\s*€/[a-zA-Z]', txt)
                            if match:
                                price_per_unit = float(match.group(1).replace('.', '').replace(',', '.'))
                                price_weight_text = txt
                                break
                    except:
                        pass

                    driver.back()
                    time.sleep(1)

                except Exception as e:
                    print(f"❌ Erreur produit : {e}")
                    count_skipped += 1
                    continue

                # 💶 price pack
                try:
                    price_el = wait_el(product_el, By.CSS_SELECTOR, 'p.product-price__unit-price')
                    price_raw = get_text_from_element(price_el, 'price_per_unit')
                    price_per_packaging = convert_to_float(price_raw.replace('€', '').replace(',', '.')) if price_raw else None
                except:
                    price_per_packaging = price_raw = None

                # 📦 format
                try:
                    format_el = wait_el(product_el, By.CSS_SELECTOR, 'div.product-format__size--cell')
                    format_size = get_text_from_element(format_el, 'format')  
                except:
                    format_size = None

                #Weight_per_packaging

                mesure_unit_for_packaging, weight_per_packaging = self.extract_packaging_info(format_size)

                # 🧲 unité
                try:
                    unit_el = wait_el(product_el, By.CSS_SELECTOR, 'p.product-price__extra-price')
                    unit = get_text_from_element(unit_el, 'unit')
                except:
                    unit = None

                print(f"[{index}] Title: {product_title} | ID: {product_id} | URL: {product_url} | Price: {price_raw} | Format: {format_size} | Weight: {weight_per_packaging}g | price_per_unit: {price_per_unit}")



                # ✅ création objet
                link = Links(links_self=product_url)
                lang_desc = LangDesc(es=Desc(title=product_title, links=link, images=image_urls))

                try:
                    mesure_unit_for_price_per_unit, matter, product_pricing_unit = ProductContentMercadona.get_packaging_info(price_weight_text)
                except:
                    mesure_unit_for_price_per_unit = matter = product_pricing_unit = None

                # 🔒 Initialiser un LabelMercadona vide pour éviter UnboundLocalError
                final_label = LabelMercadona()

                try:
                    # 📄 Préparer l'entrée pour l'analyse textuelle
                    label_input_dict = {
                        "title": product_title.lower().strip()
                    }

                    

                    # 🔍 Analyse textuelle
                    try:
                        label_textual = LabelMercadona.from_dict_to_object(label_input_dict)
                    except Exception:
                        label_textual = LabelMercadona()

                    # ✅ Affecter le label extrait
                    final_label = label_textual

                except Exception as e:
                    print(f"[{index}] ⚠️ Erreur lors de l'extraction des labels textuels : {e}")
                    final_label = LabelMercadona()  # Fallback sûr

                # 📦 Construction du dictionnaire complet (y compris False et None)
                label_dict = {}
                for key in LabelMercadona.__annotations__.keys():
                    value = getattr(final_label, key, None)
                    if isinstance(value, bool):  # Inclut uniquement True ou False
                        label_dict[key] = value

                print(f"[{index}] 🏷️ Labels (complet) : {json.dumps(label_dict, ensure_ascii=False)}")

                #Parsing_duration
                end_parsing_date = datetime.now()
                parsing_duration = (end_parsing_date - start_parsing_date).seconds

                # Calcul de `created_at` et `updated_at`
                created_at = datetime.now().strftime("%Y-%m-%dT%H:%M")
                updated_at = created_at  # Initialement égal à `created_at`
                
                new_evolution = Evolution(price_per_packaging=price_per_packaging, format=format_size, price_per_unit=price_per_unit,
                                        weight_per_packaging=weight_per_packaging, )
                
                # Mettre à jour `updated_at` seulement si une évolution a eu lieu
                evolutions = []
                if latest_parsed_products:
                    old_evolution = latest_parsed_products[0].evolutions[-1]
                    evolutions.append(old_evolution)
                    if self.detect_change(old_evolution, new_evolution):
                        updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M")
                        evolutions.append(new_evolution)
                else:
                    evolutions = [new_evolution]
                
                brand = ProductContentMercadona.extract_brand_from_title(product_title)
                country_code = "ES"
                origin= format_origin(country_code)

                categories = find_category_for_url(categories_data, aisle_url)

                if index == 0:
                    print(f"\n📂 Catégorie hiérarchique utilisée pour ce rayon ({aisle.name}):")
                    print(json.dumps(categories, indent=4, ensure_ascii=False))

                
                product = Product(ean=product_id, lang_desc=lang_desc,market=MarketMercadona(), brand=brand,mesure_unit_for_price_per_unit=mesure_unit_for_price_per_unit,
                                  matter=matter, mesure_unit_for_packaging=mesure_unit_for_packaging, parsing_duration=parsing_duration,created_at=created_at,
                                  updated_at=updated_at,origin=origin,categories=categories,label= label_dict)
                product.evolutions = evolutions
                products.append(product)

                if parse_only_first_x_products and len(products) >= parse_only_first_x_products:
                    return products
        
        print(f"✅ Extraction terminée : {len(products)} produits enregistrés, {count_skipped} ❌ ignorés.")
        return products


# ▶️ Boucle principale

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
        mercadona = MercadonaAislesProductsScanner()
        parser_name = cmdargs[1]
        parser_class = getattr(static_data_V3, parser_name)
        aisles: List[StaticAisle] = parser_class.aisles

          # ✅ Obtenir les rayons depuis la classe parser
        aisles: List[StaticAisle] = parser_class.aisles
        print(f"aisles: {len(aisles)}")

        if len(aisles) == 0:
            print("empty aisles")
            sys.exit()
        
        # Filtrage d’un seul rayon via son identifiant
        only_one_aisle = None
        if "--only_one_aisle" in cmdargs:
            idx = cmdargs.index("--only_one_aisle")
            only_one_aisle = cmdargs[idx + 1]
            print(f"➡️ Filtrage activé sur un seul rayon : {only_one_aisle}")
            
        postal_code = "28001"
        if "postal_code" in cmdargs:
            index = cmdargs.index("postal_code")
            postal_code = cmdargs[index + 1]

        category_folder_path = os.path.normpath(parser_class.category_path())
        os.makedirs(category_folder_path, exist_ok=True)

        # 🔧 Lancement du navigateur Chrome
        options = Options()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)

        try:
            # 🔐 Étape initiale : cookies + code postal
            handle_initial_popup(driver, postal_code)

            # 📥 Traitement de chaque allée
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

                aisle_filename = aisle.name.replace("&", "and").replace(" ", "_") + ".json"
                aisle_uri = os.path.join(category_folder_path, aisle_filename)

                parse_only_ean_title_url_price = "parse_only_ean_title_url_price" in cmdargs
                parse_only_first_x_products = None
                if "parse_only_first_x_products" in cmdargs:
                    index = cmdargs.index("parse_only_first_x_products")
                    parse_only_first_x_products = int(cmdargs[index + 1])

                parse_only_from_index = None

                new_products = mercadona.parse_products(
                    driver,
                    aisle,
                    parse_only_ean_title_url_price,
                    parse_only_first_x_products,
                    parse_only_from_index,
                    latest_parsed_products,
                    categories_data
                )

                # 💾 Sauvegarde du fichier JSON
                # ✅ Préparation finale du fichier avec ID des catégories remappées en "Lxxx"
                def remap_category_ids(products: List[Product]) -> List[dict]:
                    def clean_dict(obj):
                        if isinstance(obj, list):
                            return [clean_dict(item) for item in obj if item is not None]
                        elif is_dataclass(obj):
                            return {k: clean_dict(v) for k, v in asdict(obj).items() if v is not None}
                        elif isinstance(obj, dict):
                            return {k: clean_dict(v) for k, v in obj.items() if v is not None}
                        else:
                            return obj

                    output = []
                    for p in products:
                        prod_dict = clean_dict(p)

                        # ❌ Ne pas ajouter "subs", juste garder les catégories brutes si elles existent
                        # ✅ Et ne rien faire sinon
                        output.append(prod_dict)

                    return output

                final_products = remap_category_ids(new_products)

                dump_json_then_write_it_to_file(aisle_uri, final_products)

        finally:
            try:
                driver.quit()
                print("🛑 Navigateur fermé proprement.")
            except:
                pass
    else:
        print("wrong args number")
        sys.exit()