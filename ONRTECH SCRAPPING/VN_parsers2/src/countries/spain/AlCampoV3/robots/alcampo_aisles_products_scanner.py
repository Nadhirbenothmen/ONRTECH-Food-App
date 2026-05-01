# -*- coding: utf-8 -*-Acampo id url title price unit pack 
#!/usr/bin/env python

from dataclasses import asdict, is_dataclass
import datetime
import json
import os
from pathlib import Path
import re
import sys
import time
from tracemalloc import start
from typing import List, Optional, Dict

from numpy import average, imag
from enum import Enum
from datetime import datetime, timedelta
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
sys.path.append('src')
sys.path.append('./')
from utils.appium_utils import wait_el_text, wait_els,wait_el

# Local imports
from src.countries.spain.AlCampoV3.model.product_alcampo import ALLERGENS, MarketAlcampo , ProductAlcampo, LabelAlcampo
from src.countries.spain.AlCampoV3.model.product_content_alcampo import NutritionAlcampo, ProductContentAlcampo, NutritionContentAlcampo
from src.model.my_model import ProductType
from src.countries.spain.AlCampoV3.robots.static_dataV3 import get_static_aisles_from_user_cmdargs
from src.countries.spain.AlCampoV3.robots import static_dataV3, webdriverInstance
from src.model.product import (
    Category,CustomerReviews, Desc, Evolution, LangDesc, Links, NutritionFacts, Product, CustomerReviews,Origin,Label,Nutrition,Offer,
    get_latest_parsed_products
)
from src.model.static_category_aisle import StaticAisle
from src.utils.my_utils import all_attrs_are_none_or_zero, convert_to_float, custom_dump, dump_json_then_write_it_to_file, find_all_substrings_in_text, write_output_to_file
from src.model.product_content import convert_format_product 
from src.utils.ean_country_checker import get_country_code_from_country_name_in_french_lang, get_country_code_from_ean


def get_categories_json_file_uri() -> Optional[str]:
    """
    Retourne le chemin absolu vers le fichier categories_dia.json.
    Utilise la position du script pour construire dynamiquement le chemin.
    """
    script_path = Path(__file__).resolve()           # Chemin complet du script actuel
    script_folder = script_path.parent               # Dossier contenant ce script
    parent_folder = script_folder.parent             # src/countries/spain/AlcampoV3/
    model_folder = os.path.join(parent_folder, 'model')  # .../model
    model_file = os.path.join(model_folder, 'alcampo_categories.json')  # .../categories_alcampo.json
    print(f"[DEBUG] 📄 categories_alcampo.json path → {model_file}")
    return model_file


def find_deepest_category_path(categories: list, product_url_or_aisle: str, path=None):
    if path is None:
        path = []
    candidates = []

    for cat in categories:
        current_path = path + [{"id": cat["id"], "label": cat["label"]}]
        if cat.get("id") and cat["id"] in product_url_or_aisle:
            # On creuse plus loin si possible
            if "subs" in cat:
                deeper_path = find_deepest_category_path(cat["subs"], product_url_or_aisle, current_path)
                if deeper_path:
                    candidates.append(deeper_path)
                else:
                    candidates.append(current_path)
            else:
                candidates.append(current_path)
        else:
            if "subs" in cat:
                deeper_path = find_deepest_category_path(cat["subs"], product_url_or_aisle, current_path)
                if deeper_path:
                    candidates.append(deeper_path)

    if not candidates:
        return None

    # On choisit la candidate dont le dernier id est la plus longue (plus spécifique)
    def specificity(path):
        # Dernier id dans le chemin
        return len(path[-1]["id"])

    best_path = max(candidates, key=specificity)
    return best_path


def find_category_for_url(categories_data: dict, product_url_or_aisle: str) -> Optional[List[dict]]:
    return find_deepest_category_path(categories_data.get("subs", []), product_url_or_aisle)
            
def convert_categories_raw_to_typed(categories_raw: Optional[List[dict]]) -> Optional[List[Category]]:
    if not categories_raw:
        return None
    result = []
    for cat in categories_raw:
        cat_id = str(cat.get('id', ''))  # Garder l'ID tel quel en chaîne (ex: "OC2112")
        label = cat.get('label', '')
        result.append(Category(id=cat_id, label=label))
    return result

def extract_offer_as_object(driver) -> Optional[List[Offer]]:
    try:
        # Sélecteur CSS spécifique aux offres promotionnelles Alcampo
        offer_el = wait_el(driver, By.CSS_SELECTOR, 'span._text--promotion_cn5lb_31')
        offer_text = offer_el.text.strip().replace('\n', ' ')

        # 🔎 Détection de quantité nécessaire, ex : "2ª unidad"
        quantity_match = re.search(r"(\d+)[ªº]?\s*unidad", offer_text, re.IGNORECASE)
        required_quantity = int(quantity_match.group(1)) if quantity_match else 0

        if offer_text and any(c.isdigit() for c in offer_text):
            print(f"[DEBUG] 🎁 Offre détectée : {offer_text} | Quantité requise : {required_quantity}")
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

            
def get_product_images(driver):
    images = set()

    # 1) Tenter de récupérer le carousel (image thumbnails)
    try:
        carousel = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="tablist"]'))
        )
        thumbs = carousel.find_elements(By.CSS_SELECTOR, 'button[role="tab"] img')
        for img in thumbs:
            src = img.get_attribute('src') or img.get_attribute('data-src')
            if src:
                images.add(src.split('?')[0])

        # Si c'est paginé, cliquer "siguiente" autant que possible
        while True:
            next_btn = driver.find_elements(By.CSS_SELECTOR,
                'button[aria-label*="siguiente"], button[aria-label*="next"]'
            )
            if not next_btn or not next_btn[0].is_displayed():
                break
            driver.execute_script("arguments[0].click();", next_btn[0])
            time.sleep(0.3)
            # reprendre les vignettes
            thumbs = carousel.find_elements(By.CSS_SELECTOR, 'button[role="tab"] img')
            for img in thumbs:
                src = img.get_attribute('src') or img.get_attribute('data-src')
                if src:
                    images.add(src.split('?')[0])

    except TimeoutException:
        # 2) Fallback global : toutes les <img> dont le src contient "500x500"
        all_imgs = driver.find_elements(By.CSS_SELECTOR, 'img[src*="500x500"]')
        for img in all_imgs:
            src = img.get_attribute('src')
            if src:
                images.add(src.split('?')[0])

    except Exception as e:
        print(f"⚠️ Erreur extraction images: {e}")

    return list(images)



BASE_PRODUCTS_PATH = os.path.join(os.path.dirname(__file__), "products")

class AlcampoAislesProductsScanner:
    def __init__(self):
        self.total_products_number = 0


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

    def close_location_popup(self, driver: webdriver):
        try:
            # Fermer via bouton 'X' si disponible
            close_buttons = wait_els(driver, By.CSS_SELECTOR, 'div[class*="modal"] button[aria-label="Cerrar"]')
            for btn in close_buttons:
                if btn.is_displayed():
                    driver.execute_script("arguments[0].click();", btn)
                    print("✅ Popup fermé via bouton 'X'")
                    return

            # Ou fermer via texte spécifique
            popup_text_el = wait_els(driver, By.XPATH, "//div[contains(text(), 'Dinos dónde y cuándo quieres recibir tu compra')]")
            if popup_text_el:
                close_icon = wait_el(driver, By.CSS_SELECTOR, 'button[aria-label="Cerrar"]')
                driver.execute_script("arguments[0].click();", close_icon)
                print("✅ Popup de localisation fermé via texte détecté")
        except Exception as e:
            print(f"ℹ️ Aucun popup de localisation fermé ou non détecté : ")

    # Fonction de détection de changement dans les évolutions
    @staticmethod
    def detect_change(old_evolution: Evolution, new_evolution: Evolution) -> bool:
        
        def offers_to_set(offers):
            return set(offers or [])
        return (
            old_evolution.price_per_packaging != new_evolution.price_per_packaging or
            old_evolution.format != new_evolution.format or
            old_evolution.price_per_unit != new_evolution.price_per_unit or
            old_evolution.weight_per_packaging != new_evolution.weight_per_packaging or
            old_evolution.ingredients != new_evolution.ingredients or
            old_evolution.allergens != new_evolution.allergens or
            old_evolution.nutri_Score != new_evolution.nutri_Score or
            old_evolution.certification != new_evolution.certification or
            (old_evolution.reviews.__dict__ if old_evolution.reviews else None) != (new_evolution.reviews.__dict__ if new_evolution.reviews else None) or
            offers_to_set(old_evolution.offers) != offers_to_set(new_evolution.offers) or
            (old_evolution.nutrition.__dict__ if old_evolution.nutrition else None) != (new_evolution.nutrition.__dict__ if new_evolution.nutrition else None)

        )
    
    
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
            except Exception:
                pass

            self.scroll_and_load_all_products(driver)

            products: List[Product] = []
            products_els = wait_els(driver, By.CSS_SELECTOR, 'div.product-card-container' , timeout = 10) or []
            total = len(products_els)
            print("Nombre de produits détectés :", total)

            original_window = driver.current_window_handle

            count_skipped = 0

            start_parsing_date = datetime.now()

            for index in range(total):
                if parse_only_from_index and parse_only_from_index > index:
                    continue
                try:   
                    products_els = wait_els(driver, By.CSS_SELECTOR, 'div.product-card-container')
                    product_el = products_els[index]

                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", product_el)
                    time.sleep(0.5)

                    try:
                        a_tag = wait_el(product_el, By.XPATH, './/a[contains(@href, "/products/")]')
                        if a_tag:
                            product_url = a_tag.get_attribute("href")
                            print(f"🔗 URL Produit {index+1}: {product_url}")
                        else:
                            print(f"⚠️ [Produit {index+1}] Élément <a> introuvable dans la carte produit.")
                            continue
                    except Exception as e:
                        print(f"⚠️ [Produit {index+1}] Exception lors de la recherche du lien produit ")
                        continue


                    try:
                        title_el = wait_el(product_el, By.XPATH, './/h3')
                        product_title = title_el.text.strip()
                        print(f"[{index}] 🏷️ Titre : {product_title}")
                    except NoSuchElementException:
                        product_title = ""
                        print(f"[{index}] ⚠️ Titre non trouvé")

                    product_id = product_url.split("/")[-1].split("?")[0] if product_url else None


                    #Extraction du prix

                    try:
                        price_el = wait_el(product_el,By.CSS_SELECTOR, 'span[data-test="fop-price"]')
                        price_text = price_el.text.strip().replace('€', '').replace(',', '.').strip()
                        price_per_packaging = convert_to_float(price_text)
                        price_display = f"{price_per_packaging:.2f} €"
                    except:
                        price_per_packaging = None
                        price_display = None

                    print(f"[{index}]  {price_display} ")

                    # Extraction du poids et prix par quantité
                    formats = ProductContentAlcampo.extract_full_format_from_title(product_title)


                    weight_per_unit = None
                    weight_value = None
                    unit = None

                    # 2) Tentative d’extraction depuis le sélecteur fop-size (s’il existe)
                    try:
                        weight_el = wait_el(product_el, By.CSS_SELECTOR, 'div[data-test="fop-size"] span')
                        weight_per_unit = weight_el.text.strip()  # ex. "750ml", "1kg", "(6,46 € Unidad)"
                        print(f"[{index}] Poids extrait brut (fop-size) : {weight_per_unit}")

                        # Si le texte contient "€", on considère que ce n'est pas un poids, mais un prix par unité
                        if "€" in weight_per_unit:
                            print(f"[{index}] Texte contenant '€' → on ignore fop-size comme poids.")
                            # weight_value et unit restent à None, on passera au fallback
                        else:
                            # On applique une regex stricte pour récupérer "nombre + unité" (g, kg, ml, cl, l)
                            m1 = re.match(r"^(\d+(?:[.,]\d+)?)[\s]*(g|kg|ml|cl|l)\b", weight_per_unit.lower())
                            if m1:
                                raw_number = m1.group(1).replace(",", ".")
                                parsed_number = float(raw_number) if "." in raw_number else int(raw_number)
                                parsed_unit = m1.group(2)

                                # Conversion automatique selon l'unité récupérée
                                if parsed_unit == "g":
                                    weight_value = parsed_number
                                    unit = "g"
                                elif parsed_unit == "kg":
                                    weight_value = parsed_number * 1000
                                    unit = "g"
                                elif parsed_unit == "ml":
                                    weight_value = parsed_number
                                    unit = "ml"
                                elif parsed_unit == "cl":
                                    weight_value = parsed_number * 10
                                    unit = "ml"
                                elif parsed_unit == "l":
                                    weight_value = parsed_number * 1000
                                    unit = "ml"

                                print(f"[{index}] Poids normalisé (fop-size) : {weight_value} {unit}")
                            else:
                                print(f"[{index}] Format de 'fop-size' non reconnu : '{weight_per_unit}'")
                                weight_value = None
                                unit = None

                    except NoSuchElementException:
                        # Aucun fop-size trouvé → on passera au fallback
                        weight_per_unit = None
                        weight_value = None
                        unit = None
                        print(f"[{index}] Aucun élément 'fop-size' trouvé.")
                    except Exception as e:
                        weight_per_unit = None
                        weight_value = None
                        unit = None
                        print(f"[{index}] Erreur lors de l'extraction fop-size : {e}")

                    # 3) Si pas de poids valide, fallback sur le titre (formats)
                    if weight_value is None and formats:
                        # Exemples attendus dans formats: "75 cl", "1 kg", "500 g", "0,75 l"
                        fmt = formats.strip().lower()  # ex. "75 cl", "0,75 l"
                        m2 = re.match(r"^(\d+(?:[.,]\d+)?)[\s]*(g|kg|ml|cl|l)\b", fmt)
                        if m2:
                            raw2 = m2.group(1).replace(",", ".")
                            parsed2 = float(raw2) if "." in raw2 else int(raw2)
                            unit2 = m2.group(2)

                            if unit2 == "g":
                                weight_value = parsed2
                                unit = "g"
                            elif unit2 == "kg":
                                weight_value = parsed2 * 1000
                                unit = "g"
                            elif unit2 == "ml":
                                weight_value = parsed2
                                unit = "ml"
                            elif unit2 == "cl":
                                weight_value = parsed2 * 10
                                unit = "ml"
                            elif unit2 == "l":
                                weight_value = parsed2 * 1000
                                unit = "ml"

                            print(f"[{index}] Poids normalisé (fallback titre) : {weight_value} {unit}")
                        else:
                            print(f"[{index}] Aucun poids extrait depuis 'formats' ('{formats}').")

                    # À ce stade, weight_value et unit sont soit valides, soit None
                    print(f"[{index}] → weight_per_packaging final = {weight_value}, unit = {unit}")


                    #Extraction du prix par unité

                    try:
                        price_weight_el = wait_el(product_el, By.CSS_SELECTOR, 'span[data-test="fop-price-per-unit"]')
                        price_weight_text = price_weight_el.text.strip()  # Exemple : "3,19 € por kilogramo"

                        # Extraire le prix et la mesure avec une regex
                        match = re.search(r'([\d.,]+)\s?€\s?por\s?(\w+)', price_weight_text)
                        if match:
                            # On convertit la partie numérique en float
                            price_per_unit = float(match.group(1).replace(',', '.'))
                            weight_per_pack = match.group(2)
                            print(f"[{index}] Prix par unité (extrait) : {price_per_unit} €, poids par unité : {weight_per_pack}")
                        else:
                            price_per_unit = None
                            weight_per_pack = None
                            print(f"[{index}] Aucun prix/poids trouvé dans '{price_weight_text}'.")
                    except Exception as e:
                        price_per_unit = None
                        weight_per_pack = None
                        print(f"[{index}] Erreur lors de l'extraction du prix/poids : {e}")

                    # → Fallback : si price_per_unit est None, on reprend price_per_packaging
                    if price_per_unit is None and price_per_packaging is not None:
                        price_per_unit = price_per_packaging
                        print(f"[{index}] Fallback : price_per_unit non trouvé, on prend price_per_packaging ({price_per_packaging} €)")

                    # À partir d'ici, price_per_unit est toujours défini (ou None si price_per_packaging l'était aussi)
                    print(f"[{index}] FINAL → price_per_packaging = {price_per_packaging}, price_per_unit = {price_per_unit}")

                    # Ouverture d'un nouvel onglet pour extraction détaillée (EAN, prix, etc.)
                    driver.execute_script(f"window.open('{product_url}', '_blank');")
                    driver.switch_to.window(driver.window_handles[-1])
                    driver.get(product_url)
                    time.sleep(0.7)

                    images = get_product_images(driver)

                    """formats = ProductContentAlcampo.extract_full_format_from_title(product_title)"""
                   
                    # Extraction des ingrédients
                    # ✅ Extraction des ingrédients
                    try:
                        ingredients = None

                        # Chercher tous les conteneurs de section (comme <div class="sc-fmzyuX">)
                        section_divs = wait_els(driver, By.CSS_SELECTOR, "div.sc-fmzyuX")

                        for div in section_divs:
                            try:
                                h4 = div.find_element(By.TAG_NAME, "h4")
                                if "Ingrediente" in h4.text.strip():
                                    # On prend le premier paragraphe <p> dans la même div
                                    p = div.find_element(By.TAG_NAME, "p")
                                    ingredients = p.text.strip()
                                    break
                            except Exception:
                                continue

                        if ingredients:
                            print(f"[{index}] 🧬 Ingrédients : {ingredients}")
                        else:
                            ingredients = None
                            print(f"[{index}] ⚠️ Aucun ingrédient trouvé.")
                    except Exception as e:
                        ingredients = None
                        print(f"[{index}] ❌ Erreur lors de l'extraction des ingrédients ")


                    allergens_found = ProductContentAlcampo.detect_allergens(ingredients, ALLERGENS)
                    print(f"[{index}] ⚠️ Allergènes détectés : {allergens_found}")
                    
                    # ✅ Extraction des détails du produit (robuste)
                    try:
                        product_details = None

                        # Trouver toutes les sections contenant <h2> avec "Detalles del producto"
                        detail_containers = driver.find_elements(By.CSS_SELECTOR, 'div._box_1qlpx_1')

                        for container in detail_containers:
                            try:
                                h2 = container.find_element(By.TAG_NAME, "h2")
                                if "Detalles del producto" in h2.text.strip():
                                    # Trouver la div sc-fmzyuX à l’intérieur
                                    detail_div = container.find_element(By.CSS_SELECTOR, "div.sc-fmzyuX")

                                    # Si la div contient des <p>, on les concatène
                                    paragraphs = detail_div.find_elements(By.TAG_NAME, "p")
                                    if paragraphs:
                                        product_details = "\n".join(p.text.strip() for p in paragraphs if p.text.strip())
                                    else:
                                        # Sinon, on prend tout le texte brut
                                        product_details = detail_div.text.strip()
                                    break
                            except Exception:
                                continue

                        # 🟡 Fallback : si aucun détail trouvé → utiliser le titre sans format
                        if not product_details and product_title:
                            cleaned_title = product_title.strip()

                            # Supprimer formats simples (ex: "35 g", "1.5 l", "250 ml")
                            cleaned_title = re.sub(r"\s*\d+[.,]?\d*\s*(g|gr|gramos|kg|ml|cl|l)\.?$", "", cleaned_title, flags=re.IGNORECASE)

                            # Supprimer formats multipack simples (ex: "2x125 g", "3 x 250 ml")
                            cleaned_title = re.sub(r"\s*\d+\s*[x×]\s*\d+[.,]?\d*\s*(g|gr|gramos|kg|ml|cl|l)\.?$", "", cleaned_title, flags=re.IGNORECASE)

                            # Supprimer formats pack (ex: "pack 6 botellas de 1.5 l", "pack de 4 unidades de 33 cl")
                            cleaned_title = re.sub(
                                r"\s*pack\s*(de\s*)?\d+\s*(botellas?|unidades?|uds?\.?)\s*(de\s*)?\d+[.,]?\d*\s*(g|gr|gramos|kg|ml|cl|l)\.?$",
                                "",
                                cleaned_title,
                                flags=re.IGNORECASE
                            )

                            # Nettoyer espaces finaux et ajouter un point
                            cleaned_title = cleaned_title.strip().rstrip(".") + "."

                            product_details = cleaned_title
                            print(f"[{index}] ⚠️ Aucun détail produit trouvé. Utilisation du titre nettoyé comme fallback : {product_details}")

                        elif product_details:
                            print(f"[{index}] 🧾 Détails produit : {product_details}")
                        else:
                            print(f"[{index}] ⚠️ Aucun détail produit trouvé et pas de titre disponible.")

                    except Exception as e:
                        product_details = None
                        print(f"[{index}] ❌ Erreur lors de l'extraction des détails produit ")




                  
                    # Extraction du mode d'emploi (usage/stockage)
                    try:
                        usage_instructions = None
                        # Cherche le h2 avec le texte "Almacenamiento y uso"
                        h2s = wait_els(driver, By.XPATH, "//h2[contains(text(), 'Almacenamiento y uso')]")
                        for h2 in h2s:
                            # Prend la div suivante (sibling)
                            next_divs = wait_els(h2, By.XPATH, "following-sibling::div")
                            for div in next_divs:
                                text = div.text.strip()
                                if text:
                                    usage_instructions = text
                                    break
                            if usage_instructions:
                                break
                        print(f"[{index}] Mode d'emploi : {usage_instructions}")
                    except Exception:
                        usage_instructions = None
                        print(f"[{index}] Mode d'emploi non trouvé.")
                    
                    # Extraction de la marque
                    try:
                        marque = None
                        marca_h2 = wait_el(driver, By.XPATH, "//h2[text()='Marca']")
                        if marca_h2:
                            parent_div = wait_el(marca_h2, By.XPATH, "./..")
                            brand_div = wait_el(parent_div, By.XPATH, ".//div[contains(@class, 'sc-fmzyuX')]")
                            if brand_div:
                                marque = brand_div.text.strip()
                    except Exception as e:
                        marque = None
                        print(f"[{index}] ⚠️ Marque non trouvée ou erreur : {e}")

                    # Fallback sur le premier mot du titre
                    if not marque and product_title:
                        marque = product_title.split()[0].strip()

                    # Fallback final si rien trouvé
                    if not marque:
                        marque = "PRODUCTO ALCAMPO"

                    print(f"[{index}] ✅ Marque extraite : {marque}")



                    # Extraction des caractéristiques (tableau sous "Características")
                    try:
                        Caractéristiques= {}
                        caracteristicas_header = wait_els(driver, By.XPATH, "//h2[contains(text(), 'Características')]")
                        if caracteristicas_header:
                            table_el = wait_el(caracteristicas_header[0], By.XPATH, "following-sibling::div//table")
                            rows = wait_els(table_el, By.TAG_NAME, "tr")
                            for row in rows:
                                cells = wait_els(row, By.TAG_NAME, "td")
                                if len(cells) >= 2:
                                    key = cells[0].text.strip()
                                    value = cells[1].text.strip()
                                    Caractéristiques[key] = value
                        print(f"[{index}] 🧾 Caractéristiques : {json.dumps(Caractéristiques, ensure_ascii=False)}")
                    except Exception as e:
                        Caractéristiques = None
                        print(f"[{index}] Caractéristiques non trouvées : ")

                    # 🏳️ Extraction du pays d'origine (depuis Caractéristiques)
                    origin_country_name = None
                    origin_code = None
                    origin_ean_list = []

                    if Caractéristiques:
                        origin_country_name = Caractéristiques.get("País de origen") or Caractéristiques.get("País de Origen")

                    # Si le pays n'est pas trouvé, utiliser "Espagne" par défaut
                    if not origin_country_name:
                        origin_country_name = "España"

                    origin_code = get_country_code_from_country_name_in_french_lang(origin_country_name)
                    if not origin_code:
                        origin_code = "ES"  # Forcer ES si aucun code trouvé
                    origin_ean_list = [origin_code]

                    # Exemple complet : extraction et fusion des labels
                    try:
                        # Extraction des labels SVG et origine (fonction à adapter selon ton code)
                        label_svg, spanish_origin = ProductContentAlcampo.get_label_and_origin(driver)
                    except Exception:
                        label_svg, spanish_origin = None, None

                    label_input_dict = {
                        "title": product_title,
                        "details": {
                            "desc": product_details,
                            "ingredients": ingredients,
                            **(Caractéristiques if Caractéristiques else {})
                        }
                    }

                    try:
                        # Extraction des labels textuels via analyse des textes
                        label_textual = LabelAlcampo.from_dict_to_object(label_input_dict)
                    except Exception:
                        label_textual = LabelAlcampo()

                    # Fusion des labels : priorité au SVG si présent, sinon textuel
                    final_label = LabelAlcampo()
                    for key in LabelAlcampo.__annotations__.keys():
                        svg_value = getattr(label_svg, key, None) if label_svg else None
                        textual_value = getattr(label_textual, key, None)
                        setattr(final_label, key, svg_value if svg_value is not None else textual_value)

                    # Récupérer un dict complet avec toutes les clés définies dans LabelAlcampo
                    label_dict_complete = {k: getattr(final_label, k, None) for k in LabelAlcampo.__annotations__.keys()}

                    # Filtrer uniquement les labels booléens True/False (ignorer None)
                    label_dict_filtered = {k: v for k, v in label_dict_complete.items() if isinstance(v, bool)}

                    print(f"[{index}] 🏷️ Labels détectés : {json.dumps(label_dict_filtered, ensure_ascii=False)}")

                    # Extraction du lien vers les avis clients
                    try:
                        review_link_el = wait_el(driver, By.CSS_SELECTOR, 'a[href="#reviews-title"]')
                        review_link = review_link_el.get_attribute("href")
                        print(f"[{index}] 🔗 Lien vers les avis : {review_link}")
                    except NoSuchElementException:
                        review_link = None
                        print(f"[{index}] ❌ Lien vers les avis non trouvé.")

                    # 🔹 Extraction des étoiles et avis
                    try:
                        # Scroll vers la section des avis pour déclencher le chargement
                        try:
                            reviews_title = wait_el(driver, By.ID, "reviews-title")
                            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", reviews_title)
                            WebDriverWait(driver, 3).until(
                                EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'de 5 de')]"))
                            )
                            time.sleep(1.0)  # petit délai pour stabiliser
                        except Exception as e:
                            print(f"[{index}] ⚠️ Scroll vers la section avis échoué : {e}")

                        note = 0.0
                        review_count = 0

                        # 🧠 Extraction depuis le texte brut (ex: "Puntuación, 5.0 de 5 de 2 opiniones.")
                        try:
                            avis_spans = wait_els(driver, By.XPATH, "//span[contains(text(), 'de 5 de')]")
                            for span in avis_spans:
                                avis_text = span.text.strip()
                                print(f"[{index}] Texte brut d'avis : {avis_text}")
                                match = re.search(r'(\d+(?:[.,]\d+)?) de 5 de (\d+)', avis_text)
                                if match:
                                    note = float(match.group(1).replace(",", "."))
                                    review_count = int(match.group(2))
                                    break
                        except Exception as e:
                            print(f"[{index}] ⚠️ Erreur parsing note/avis : {e}")

                        # ⭐ Fallback si `note` toujours 0 mais présence d’étoiles SVG
                        if note == 0.0:
                            try:
                                filled_stars = wait_els(driver, By.CSS_SELECTOR, 'svg[data-icon="icon__reviews_filled"]')
                                half_stars = wait_els(driver, By.CSS_SELECTOR, 'svg[data-icon="icon__reviews_half"]')
                                rating = len(filled_stars) + (0.5 if len(half_stars) > 0 else 0)
                                note = rating
                            except:
                                pass  # on garde note = 0.0

                        print(f"[{index}] ⭐ Note : {note} / 5, Avis : {review_count}")

                    except Exception as e:
                        note = 0.0
                        review_count = 0
                        print(f"[{index}] ❌ Erreur globale d'extraction des avis : {e}")

                    # Extraction des données nutritionnelles
                    try:
                        nutrition_facts = {}
                        excluded_keys = ["Valores medios por:", "Valores medios por", "Valor por", "Valores por", "Por 100g"]
                        nutrition_header = wait_els(driver, By.XPATH, "//h2[contains(text(), 'Datos nutricionales')]")

                        if nutrition_header:
                            table_el = wait_el(nutrition_header[0], By.XPATH, "following-sibling::div//table")
                            rows = wait_els(table_el, By.TAG_NAME, "tr")

                            for row in rows:
                                try:
                                    cells = wait_els(row, By.XPATH, "./td | ./th")
                                    cells_text = [c.text.strip() for c in cells if c.text.strip()]

                                    if len(cells_text) == 1:
                                        titre = cells_text[0]
                                        if "valor" in titre.lower() or "valores medios" in titre.lower():
                                            nutrition_facts["header"] = titre
                                    elif len(cells_text) >= 2:
                                        key = cells_text[0]
                                        value = cells_text[1]
                                        if any(key.lower().startswith(k.lower()) for k in excluded_keys):
                                            print(f"[{index}] ⏭️ Ligne ignorée : {key} = {value}")
                                            continue
                                        if key and value:
                                            nutrition_facts[key] = value
                                except Exception as e:
                                    print(f"[{index}] ⚠️ Ligne ignorée (erreur parsing) : {e}")
                                    continue

                        
                        if nutrition_facts:
                            print(f"[{index}] 🍎 Données nutritionnelles brutes : {json.dumps(nutrition_facts, ensure_ascii=False)}")
                            # Supprimer la clé "header" si présente
                            nutrition_facts.pop("header", None)
                            try:
                                # Conversion en objet Nutrition
                                nutrition = NutritionAlcampo.convert_dict_to_nutrition_object(nutrition_facts)
                                print(f"[{index}] ✅ Objet Nutrition : {nutrition}")
                                # ▶ Calcul du Nutri-Score à partir du dict brut
                                nutri_score = ProductContentAlcampo.calculate_nutriscore_from_nested(asdict(nutrition) if nutrition else {})
                                print(f"[{index}] 🥇 Nutri-Score calculé : {nutri_score}")
                            except Exception as e:
                                print(f"[{index}] ❌ Erreur de conversion en Nutrition : {e}")
                                nutrition = None
                                nutri_score = "N/A"
                        else:
                            print(f"[{index}] ⚠️ Données nutritionnelles vides.")
                            nutrition = None
                            nutri_score = "N/A"
                    except Exception as e:
                        nutrition = None
                        nutri_score = "N/A"
                        print(f"[{index}] ❌ Erreur d'extraction des données nutritionnelles : {e}")


                    # Extraction de la certification écologique
                    def extract_certification(driver):
                        certification_value = None  # Initialisation de la certification à None par défaut

                        try:
                            # Attendre que l'élément "Eco::Etiqueta ecológica de la UE::" soit visible
                            certification_label = WebDriverWait(driver, 2).until(
                                EC.visibility_of_element_located((By.XPATH, "//td[contains(text(), 'Eco::Etiqueta ecológica de la UE::')]"))
                            )

                            # Extraire le texte de la cellule contenant "Eco::Etiqueta ecológica de la UE::"
                            certification_text = certification_label.text.strip()  # Cela devrait renvoyer "Eco::Etiqueta ecológica de la UE::"
                            
                            # Extraire uniquement la partie après "Eco::" si présente
                            if certification_text:
                                certification_value = certification_text.split("::")[1].strip() if "::" in certification_text else None

                        except Exception as e:
                            # Gérer l'exception si l'élément n'est pas trouvé ou si une erreur se produit
                            print(f"Erreur lors de l'extraction de la certification : ")
                            certification_value = "Etiqueta ecológica de la UE"  # Si l'élément est absent ou une erreur se produit, mettre la certification à None

                        # Afficher la certification extraite ou None
                        print(f"Certification écologique : {certification_value}")
                        
                        return certification_value


                    link = Links(links_self=product_url, reviews=review_link)
                    lang_desc = LangDesc(es=Desc(links=link , images=images  , title=product_title , desc = product_details))
                    reviews = CustomerReviews(average=note, count=review_count)
                    mesure_unit_for_price_per_unit, matter, product_pricing_unit = ProductContentAlcampo.get_packaging_info(
                    price_weight_text if 'price_weight_text' in locals() else None)

                    certification_value = extract_certification(driver)
                    offers = extract_offer_as_object (driver)
      
                     # 🔒 Forcer la lisibilité JSON pour `matter`
                    if matter is None:
                        matter = "OTHER"
                    elif isinstance(matter, Enum):
                        matter = matter.name

                    #Parsing_duration
                    end_parsing_date = datetime.now()
                    parsing_duration = (end_parsing_date - start_parsing_date).seconds

                    # Vérification de l'ancienne évolution (si elle existe)
                    if latest_parsed_products:
                        old_evolution = latest_parsed_products[0].evolutions[-1]  # Dernière évolution du produit précédent
                    else:
                        old_evolution = None

                    # Calcul de `created_at` et `updated_at`
                    created_at = datetime.now().strftime("%Y-%m-%dT%H:%M")
                    updated_at = created_at  # Initialement égal à `created_at`
                    
                     # Créer une nouvelle évolution à partir des nouvelles valeurs
                    new_evolution = Evolution(price_per_packaging=price_per_packaging,
                                            format=formats,
                                            price_per_unit=price_per_unit,
                                            weight_per_packaging=weight_value,
                                            ingredients=ingredients,
                                            allergens= allergens_found,
                                            reviews=reviews,
                                            nutrition=nutrition,
                                            nutri_Score=nutri_score,
                                            certification=certification_value,
                                            offers=offers)
                    # Mettre à jour `updated_at` seulement si une évolution a eu lieu
                    if old_evolution and self.detect_change(old_evolution, new_evolution):
                        updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M")
                    
                    origin = {"ean":origin_ean_list}

                    categories_raw = find_deepest_category_path(categories_data.get("subs", []), aisle_url) if categories_data else None
                    # Convertir ici en liste d'objets Category avec int id
                    categories = convert_categories_raw_to_typed(categories_raw)
                    product = Product(ean=product_id,lang_desc=lang_desc ,brand=marque , market= MarketAlcampo(), matter=matter or "OTHER",origin=origin,
                                      mesure_unit_for_price_per_unit=mesure_unit_for_price_per_unit,mesure_unit_for_packaging=unit,label=label_dict_filtered,
                                      parsing_duration= parsing_duration,created_at=created_at, updated_at=updated_at, categories=categories,)
                    
                    product.evolutions = [new_evolution]
                    
                    products.append(product)
                
                except Exception as e:
                    print(f"⛔️ Produit {index+1} ignoré suite à une erreur : {e}")
                    count_skipped += 1
                    try:
                        if len(driver.window_handles) > 1:
                            driver.close()
                            driver.switch_to.window(driver.window_handles[0])
                    except Exception as e:
                        print(f"⚠️ Erreur lors de la fermeture de l'onglet (erreur produit) : {e}")
                    continue


                try:
                    if len(driver.window_handles) > 1:
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                except Exception as e:
                    print(f"⚠️ Erreur lors de la fermeture de l'onglet (fin produit) : {e}")


                if parse_only_first_x_products and len(products) >= parse_only_first_x_products:
                    break

                time.sleep(0.1)

            print(f"✅ Extraction terminée : {len(products)} produits enregistrés, {count_skipped} ❌ ignorés.")

            return products

        except Exception as e:
            print(f"❌ Erreur analyse produits : {e}")
            return []

        

#BOUCLE PRINCIPALAE

if __name__ == "__main__":
    print("my main")
    cmdargs = sys.argv
    print(f"The total numbers of args passed to the script: {len(cmdargs)}, Args list: {cmdargs}")

    # ✅ Charger le JSON des catégories DIA
    json_path = get_categories_json_file_uri()
    print(f"✅ Chemin du fichier JSON des catégories Alcampo : {json_path}")
    with open(json_path, "r", encoding="utf-8") as f:
        categories_data = json.load(f)

    if len(cmdargs) > 1:
        alcampo = AlcampoAislesProductsScanner()
        parser_name = cmdargs[1]
        parser_class = getattr(static_dataV3, parser_name)
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

            aisle_filename = aisle.name.replace("&", "and").replace(" ", "_") + ".json"
            aisle_uri = os.path.join(category_folder_path, aisle_filename)

            parse_only_ean_title_url_price = "parse_only_ean_title_url_price" in cmdargs
            parse_only_first_x_products = None
            if "parse_only_first_x_products" in cmdargs:
                index = cmdargs.index("parse_only_first_x_products")
                parse_only_first_x_products = int(cmdargs[index + 1])
            parse_only_from_index = None

            new_products = alcampo.parse_products(
                webdriverInstance,
                aisle,
                parse_only_ean_title_url_price,
                parse_only_first_x_products,
                parse_only_from_index,
                latest_parsed_products,
                categories_data
            )
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

                    # Convertir la liste categories en liste de dicts
                    if p.categories:
                        prod_dict["categories"] = [asdict(cat) for cat in p.categories]

                    output.append(prod_dict)
                return output

            final_products = remap_category_ids(new_products)

            dump_json_then_write_it_to_file(aisle_uri, final_products)
    else:
        print("wrong args number")
        sys.exit()

