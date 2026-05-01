# Importations des modules standards
import json
import logging
import os
import re
import sys
import time
import dataclasses
from enum import Enum
from typing import List, Optional
from datetime import datetime
from pathlib import Path
from dataclasses import asdict, is_dataclass
from bs4 import BeautifulSoup
# Bibliothèques tierces
import dacite
import requests
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException , NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

# Imports locaux
# Configuration des chemins d'accès
sys.path.append('src')  # Ajoute le dossier src au PATH
sys.path.append('./')   # Ajoute le dossier courant au PATH
from src.countries.spain.DiaV3.model import categories_dia
from src.countries.spain.DiaV3.robots import static_data_V3, webdriverInstance
from src.countries.spain.DiaV3.model.product_dia import ALLERGENS, MarketDia , LabelDia 
from src.countries.spain.DiaV3.model.product_content_dia import ProductContentDia, NutritionContentDia, NutritionDia,Nutrition
from src.utils.ean_country_checker import extract_origin_structure_from_address  
from src.model.product import (Origin)

from src.model.product import (
    Desc, Evolution, LangDesc, Links, Product, Offer,
    get_latest_parsed_products, get_product_by_ean
)
from src.model.static_category_aisle import StaticAisle
from src.utils.appium_utils import (
    get_attribute_from_element, get_text_from_element,
    setup_logging, wait_el, wait_el_click, wait_el_text, wait_els
)
from src.utils.my_utils import convert_to_float, dump_json_then_write_it_to_file

BASE_PRODUCTS_PATH = os.path.join(os.path.dirname(__file__), "products")



def create_driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    return driver

def get_categories_json_file_uri() -> Optional[str]:
    """
    Retourne le chemin absolu vers le fichier categories_dia.json.
    Utilise la position du script pour construire dynamiquement le chemin.
    """
    script_path = Path(__file__).resolve()           # Chemin complet du script actuel
    script_folder = script_path.parent               # Dossier contenant ce script
    parent_folder = script_folder.parent             # src/countries/spain/DiaV3/
    model_folder = os.path.join(parent_folder, 'model')  # .../model
    model_file = os.path.join(model_folder, 'categories_dia.json')  # .../categories_dia.json
    print(f"[DEBUG] 📄 categories_dia.json path → {model_file}")
    return model_file


def find_category_for_url(categories_data: dict, product_url_or_aisle: str) -> Optional[List[dict]]:
    for main_cat in categories_data.get("subs", []):
        for sub in main_cat.get("subs", []):
            if sub.get("id") and sub["id"] in product_url_or_aisle:
                return [
                    {"id": int(main_cat["id"].replace("L", "")), "label": main_cat["label"]},
                    {"id": int(sub["id"].replace("L", "")), "label": sub["label"]}
                ]
    return None

def extract_offer_from_product_element(product_el) -> Optional[List[Offer]]:
    try:
        offer_text = None

        # 🥇 Titre promotionnel (ex : "2 UDS SÓLO 4 EUROS")
        try:
            title_el = product_el.find_element(By.CSS_SELECTOR, 'p[data-test-id="product-special-offer-promotion-title"]')
            offer_text = title_el.text.strip()
            print(f"[DEBUG] Titre promotionnel trouvé : {offer_text}")
        except Exception:
            pass

        # 🥈 Fallback : Pourcentage de remise (ex : "20% dto.")
        if not offer_text:
            try:
                discount_el = product_el.find_element(By.CSS_SELECTOR, 'p[data-test-id="product-special-offer-discount-percentage-discount"]')
                offer_text = discount_el.text.strip()
                print(f"[DEBUG] Pourcentage promotionnel trouvé : {offer_text}")
            except Exception as e:
                print(f"[DEBUG] Aucun pourcentage promo trouvé ")

        # 🔍 Détection de quantité
        quantity_match = re.search(r"(\d+)[ªº]?\s*(ud|uds|unidad)", offer_text.lower()) if offer_text else None
        required_quantity = int(quantity_match.group(1)) if quantity_match else 0

        if offer_text:
            offer = Offer(
                id=None,
                description=LangDesc(es=Desc(desc=offer_text)),
                requiredProductQuantity=required_quantity
            )
            print(f"[DEBUG] 🎁 Offre détectée : {offer_text} | Quantité requise : {required_quantity}")
            return [offer]
        else:
            print("[INFO] Aucune offre promotionnelle détectée pour ce produit.")
            return None

    except Exception as e:
        print(f"[ERROR] Erreur dans l'extraction d'offre ")
        return None

def extract_all_product_images_with_carousel(driver):
    images = set()
    previous_image_count = 0

    try:
        while True:
            image_els = driver.find_elements(By.CSS_SELECTOR, 'div[data-test-id="product-images-images-section"] img')
            for img_el in image_els:
                src = img_el.get_attribute("src")
                if src:
                    if src.startswith("/"):
                        src = f"https://www.dia.es{src}"
                    images.add(src)

            # Vérifie s’il y a une nouvelle image après clic
            if len(images) == previous_image_count:
                break  # aucune nouvelle image → fin
            previous_image_count = len(images)

            # Essaie de cliquer
            try:
                next_arrow = WebDriverWait(driver, 2).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[data-test-id="arrow-button"]'))
                )
                driver.execute_script("arguments[0].click();", next_arrow)
                time.sleep(0.4)
            except:
                break

    except Exception as e:
        print(f"❌ Erreur carrousel : {e}")

    return list(images)

# 🍪 Cookies uniquement

def handle_initial_popup(driver):
    #Gère la popup initiale : accepte les cookies via Onetrust
    wait = WebDriverWait(driver, 10)
    try:
        time.sleep(2)  # Laisse le temps au popup de s'afficher
        accept_btn = wait.until(
            EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
        )

        if accept_btn.is_displayed() and accept_btn.is_enabled():
            driver.execute_script("arguments[0].click();", accept_btn)
            print("✅ Cookies acceptés (via ID onetrust-accept-btn-handler)")
        else:
            print("⚠️ Bouton cookie détecté mais non cliquable.")
    except Exception as e:
        print(f"ℹ️ Aucun popup cookies détecté ou déjà accepté : ")

def smart_scroll(driver, pause=1.5, max_scrolls=20):
    """
    Scrolle progressivement vers le bas en s'assurant de faire apparaître de nouveaux produits.
    """
    last_height = 0
    for i in range(max_scrolls):
        driver.execute_script("window.scrollBy(0, 800);")  # Scroll progressif
        time.sleep(pause)
        new_height = driver.execute_script("return document.documentElement.scrollTop")
        products = driver.find_elements(By.CSS_SELECTOR, 'li[data-test-id="product-card-list-item"]')
        print(f"[Scroll {i+1}] Produits visibles : {len(products)}")

        # Vérifie s'il y a plus de produits visibles
        if new_height == last_height and len(products) >= 60:
            print("🛑 Fin du scroll détectée.")
            break
        last_height = new_height

    time.sleep(2)

class DiaAislesProductsScanner:
    
    def __init__(self):
        self.total_products_number = 0
        self.first_access = True

    # Fonction de détection de changement dans les évolutions
    def detect_change(self, old_evolution: Evolution, new_evolution: Evolution) -> bool:
        def nutrition_to_dict(nut):
            return nut.__dict__ if nut else {}
        def offers_to_set(offers):
            return set(offers or [])

        return any([
            old_evolution.price_per_packaging != new_evolution.price_per_packaging,
            old_evolution.price_per_unit != new_evolution.price_per_unit,
            old_evolution.format != new_evolution.format,
            old_evolution.weight_per_packaging != new_evolution.weight_per_packaging,
            old_evolution.ingredients != new_evolution.ingredients,
            old_evolution.allergens != new_evolution.allergens,
            old_evolution.nutri_Score != new_evolution.nutri_Score,
            old_evolution.certification != new_evolution.certification,
            nutrition_to_dict(old_evolution.nutrition) != nutrition_to_dict(new_evolution.nutrition),
            offers_to_set(old_evolution.offers) != offers_to_set(new_evolution.offers),
        ])

    def parse_products(self, driver: webdriver, aisle: StaticAisle, parse_only_ean_title_url_price: bool,
                   parse_only_first_x_products: Optional[int] = None,
                   parse_only_from_index: Optional[int] = None,
                   latest_parsed_products: List[Product] = [],
                   categories_data: dict = None) -> List[Product]:

        aisle_url = aisle.url
        try:
            print(f"aisle_url: {aisle_url}")
            driver.get(aisle.url)
            handle_initial_popup(driver)
            smart_scroll(driver)
            time.sleep(2)  # Attendre que la page se charge complètement

            products: List[Product] = []
            skipped_count = 0
            products_els2 = wait_els(driver, By.CSS_SELECTOR, 'li[data-test-id="product-card-list-item"]', timeout=5)
            print("Nombre de produits détectés :", len(products_els2))

            for index, product_el in enumerate(products_els2 or []):
                try:
                    start_parsing_date = datetime.now()
                    if parse_only_from_index and parse_only_from_index > index:
                        continue

                    product_title = None
                    product_url = None
                    product_id = None

                    # 🧭 Scroll ciblé
                    try:
                        driver.execute_script("arguments[0].scrollIntoView();", product_el)
                        time.sleep(0.3)
                    except:
                        pass

                    offers = extract_offer_from_product_element(product_el)


                    # 🔗 URL & Titre
                    try:
                        link_el = WebDriverWait(product_el, 5).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.search-product-card__product-link'))
                        )
                        product_url = link_el.get_attribute("href")
                        retries = 0
                        while product_url == "about:blank" and retries < 5:
                            time.sleep(0.5)
                            product_url = link_el.get_attribute("href")
                            retries += 1
                        if not product_url or product_url == "about:blank":
                            print(f"[{index}] ⛔ Lien about:blank persistant, produit ignoré.")
                            skipped_count += 1
                            continue
                        if product_url.startswith("/"):
                            product_url = f"https://www.dia.es{product_url}"
                        title_el = link_el.find_element(By.CSS_SELECTOR, 'p.search-product-card__product-name')
                        product_title = title_el.text.strip()
                    except Exception as e:
                        print(f"[{index}] ⚠️ Erreur extraction titre/URL : {e}")
                        skipped_count += 1
                        continue

                    # 🔢 ID
                    try:
                        match = re.search(r'/p/([A-Za-z0-9]+)', product_url)
                        if match:
                            product_id = match.group(1)
                            print(f"[{index}] ✅ ID extrait depuis URL: {product_id}")
                        else:
                            print(f"[{index}] ⚠️ Aucun ID trouvé dans l’URL: {product_url}")
                    except Exception as e:
                        print(f"[{index}] ❌ Erreur extraction ID : {e}")

                    # 💶 Prix
                    price_per_unit_raw = None
                    try:
                        price_el = wait_el(product_el, By.CSS_SELECTOR, 'p.search-product-card__active-price')
                        price_per_unit_raw = price_el.text.strip()
                    except Exception as e:
                        print(f"[{index}] ⚠️ Erreur extraction prix : {e}")

                    price_per_unit = price_per_packaging = None
                    price_per_unit_display = price_per_packaging_display = None
                    if price_per_unit_raw:
                        try:
                            price_per_pack_str = price_per_unit_raw.replace('€', '').replace(',', '.').strip()
                            price_per_unit = convert_to_float(price_per_pack_str)
                            price_per_packaging = price_per_unit
                            price_per_unit_display = f"{price_per_unit:.2f} €"
                            price_per_packaging_display = f"{price_per_packaging:.2f} €"
                        except:
                            print(f"[{index}] ⚠️ Erreur conversion prix : '{price_per_unit_raw}'")

                    print(f"[{index}] Title: {product_title} | Price per unit: {price_per_unit_raw} | URL: {product_url}")
                    if not product_title or not product_title.strip():
                        print(f"⛔ Skipping product — title is missing:\n→ product_url: {product_url}, product_title: {product_title}")
                        skipped_count += 1
                        continue

                    # 🚀 Aller à la fiche produit
                    full_title = price_detail = quantity = ingredients = nutritional_information = storage_conditions = country_of_origin = None
                    images = []
                    energy = None
                    mode_emploi = manufacturer_name = manufacturer_address = None

                    try:
                        driver.execute_script("window.open(arguments[0]);", product_url)
                        driver.switch_to.window(driver.window_handles[-1])
                        time.sleep(1)
                        driver.get(product_url)
                        time.sleep(2)

                        images = extract_all_product_images_with_carousel(driver)

                        # 🏋️ Poids
                        weight = None
                        weight_unit = None

                        try:
                            title_el = WebDriverWait(driver, 5).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, 'h1[data-test-id="product-title"]'))
                            )
                            full_title = title_el.text.strip().lower()

                            def convert_to_grams_or_ml(value: float, unit: str) -> tuple[float, str]:
                                conversions = {
                                    'kg': (1000.0, 'g'),
                                    'g': (1.0, 'g'),
                                    'l': (1000.0, 'ml'),
                                    'ml': (1.0, 'ml'),
                                    'cl': (10.0, 'ml')
                                }
                                factor, normalized_unit = conversions.get(unit, (1.0, 'g'))  # fallback 'g'
                                return value * factor, normalized_unit

                            # Cas format "pack 6 x 125 g"
                            match = re.search(r'(\d+)\s*[xX×]\s*(\d+(?:[.,]?\d*)?)\s*(g|kg|ml|cl|l)\b', full_title)
                            if match:
                                quantity = int(match.group(1))
                                unit_value = float(match.group(2).replace(',', '.'))
                                unit = match.group(3)
                                total_weight, weight_unit = convert_to_grams_or_ml(unit_value, unit)
                                weight = total_weight * quantity
                            else:
                                # Cas simple "1 l", "500 g", etc.
                                match = re.search(r'(\d+(?:[.,]?\d*)?)\s*(g|kg|ml|cl|l)\b', full_title)
                                if match:
                                    value = float(match.group(1).replace(',', '.'))
                                    unit = match.group(2)
                                    weight, weight_unit = convert_to_grams_or_ml(value, unit)
                                else:
                                    # Cas spécial "20 unidades", "10 uds", "1 ud", etc.
                                    match = re.search(r'(\d+)\s*(unidades|unidad|uds?|pieces?|pièces?)\b', full_title)
                                    if match:
                                        weight = float(match.group(1))
                                        weight_unit = "piece"

                        except Exception as e:
                            print(f"[⚠️] Erreur lors de l'extraction du poids : {e}")
                            weight = None
                            weight_unit = None






                        # 💶 Prix/poids pack
                        price_packaging = weight_packaging = None
                        try:
                            price_unit_el = WebDriverWait(driver, 5).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, 'p[data-test-id="buy-box-price-per-unit"]'))
                            )
                            text = price_unit_el.text.strip()
                            match = re.search(r'\(?([\d,]+)\s*€\s*/\s*([A-Z]+)\)?', text, re.IGNORECASE)
                            if match:
                                price_str = match.group(1).replace(",", ".")
                                unit_str = match.group(2).upper()
                                price_packaging = f"{float(price_str):.2f} €"
                                weight_packaging = f"1 {unit_str}"
                        except:
                            pass

                        # 📝 Résumé
                        try:
                            summary_el = WebDriverWait(driver, 5).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, 'p[data-test-id="product-summary-description"]'))
                            )
                            product_summary = summary_el.text.strip()
                        except:
                            product_summary = None

                        # 🧪 Nutrition
                        try:
                            nutrition_root = WebDriverWait(driver, 5).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-test-id="nutritional-info"]'))
                            )

                            items = wait_els(nutrition_root,By.CSS_SELECTOR, 'li.nutritional-values__items')
                            nutritional_info = {}

                            for item in items:
                                try:
                                    label_el = wait_el(item,By.CSS_SELECTOR, 'p[data-test-id="nutritional-list-title"]')
                                    amount_el = wait_el(item,By.CSS_SELECTOR, 'p[data-test-id="nutritional-list-amount"]')

                                    label = label_el.text.strip()
                                    amount = amount_el.text.strip()

                                    nutritional_info[label] = amount

                                    # Sous-valeurs : ex. "de los cuales azúcares"
                                    try:
                                        sub_items = wait_els(item,By.CSS_SELECTOR, 'li.nutritional-types__items')
                                        for sub in sub_items:
                                            sub_label_el = wait_el(sub,By.CSS_SELECTOR, 'p[data-test-id="nutritional-item-title"]')
                                            sub_amount_el = wait_el(sub,By.CSS_SELECTOR, 'p[data-test-id="nutritional-item-amount"]')

                                            sub_label = sub_label_el.text.strip()
                                            sub_amount = sub_amount_el.text.strip()
                                            nutritional_info[sub_label] = sub_amount
                                    except:
                                        pass

                                except:
                                    continue

                            if not nutritional_info:
                                nutritional_info = None
                            else:
                                # 🔋 Ajout de l'énergie kj et kcal depuis les blocs séparés
                                try:
                                    energy_section = WebDriverWait(driver, 5).until(
                                        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-test-id="nutritional-info-energy"]'))
                                    )
                                    energy_text = energy_section.text.strip().lower()

                                    kj_match = re.search(r'(\d+(?:[.,]?\d*)?)\s*kj', energy_text)
                                    kcal_match = re.search(r'(\d+(?:[.,]?\d*)?)\s*kcal', energy_text)

                                    kj = float(kj_match.group(1).replace(',', '.')) if kj_match else None
                                    kcal = float(kcal_match.group(1).replace(',', '.')) if kcal_match else None

                                    if kj is not None or kcal is not None:
                                        nutritional_info["energy"] = {
                                            "kj": kj,
                                            "kcal": kcal
                                        }
                                        print(f"[DEBUG] Énergie détectée → kj: {kj}, kcal: {kcal}")
                                except Exception as e:
                                    print(f"[DEBUG] Aucun bloc énergie détecté : {e}")
                        except:
                            nutritional_info = None


                        #INGREDIENTS:

                        try:
                            ingredients = None

                            # 🔎 Récupère tous les titres <h2> contenant "Ingredientes"
                            h2_els = WebDriverWait(driver, 5).until(
                                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'h2'))
                            )

                            for h2 in h2_els:
                                try:
                                    title = h2.text.strip().lower()
                                    if "ingrediente" in title:
                                        # 🧭 Le bloc de texte se trouve dans le frère suivant (div.text-section__text)
                                        parent = h2.find_element(By.XPATH, 'following-sibling::div[contains(@class, "text-section__text")]')

                                        # 🥇 Cas avec <p>
                                        paragraphs = parent.find_elements(By.TAG_NAME, 'p')
                                        if paragraphs:
                                            ingredients = ' '.join(p.text.strip() for p in paragraphs if p.text.strip())
                                        else:
                                            # 🥈 Fallback : innerHTML si pas de texte brut
                                            raw_html = parent.get_attribute("innerHTML")
                                            soup = BeautifulSoup(raw_html, "html.parser")
                                            ingredients = soup.get_text(separator=" ", strip=True)
                                        break
                                except Exception as e:
                                    continue  # ignore erreurs pour les h2 sans structure attendue

                            if not ingredients:
                                print("[⚠️] Aucun ingrédient trouvé via les <h2>.")

                        except Exception as e:
                            print(f"[❌] Erreur globale extraction ingrédients ")
                            ingredients = None


                        allergens_found = ProductContentDia.detect_allergens(ingredients, ALLERGENS)
                        print(f"[{index}] ⚠️ Allergènes détectés : {allergens_found}")

                        # 🧊 Mode emploi & conservation
                        try:
                            instruction_els = wait_els(driver, By.CSS_SELECTOR, "p.instructions-info__items-text")
                            if len(instruction_els) >= 1:
                                mode_emploi = instruction_els[0].text.strip()
                            if len(instruction_els) >= 2:
                                storage_conditions = instruction_els[1].text.strip()
                        except:
                            storage_conditions = None
                            mode_emploi = None

                        # 🏭 Fabricant
                        try:
                            manufacturer_name = wait_el(driver, By.CSS_SELECTOR, "p.manufacturer-info__name").text.strip()
                            manufacturer_address = wait_el(driver, By.CSS_SELECTOR, "p.manufacturer-info__address").text.strip()
                        except:
                            manufacturer_name = manufacturer_address = None

                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])

                    except Exception as e:
                        print(f"[{index}] ⚠️ Erreur détails produit : {e}")
                        try:
                            driver.close()
                            driver.switch_to.window(driver.window_handles[0])
                        except:
                            pass

                    #Integre_Section
                    try:
                        sections = wait_els(driver, By.CSS_SELECTOR, 'div.text-section[data-test-id="text-section"]')
                        interes_text = None

                        for section in sections:
                            try:
                                title_el = wait_el(section,By.CSS_SELECTOR, 'h2[data-test-id="text-section-title"]')
                                title_text = title_el.text.strip().lower()

                                if "información de interés" in title_text:
                                    content_el = wait_el(section,By.CSS_SELECTOR, 'div[data-test-id="text-section-text"]')
                                    interes_text = content_el.text.strip()
                                    break  # on arrête à la première occurrence trouvée
                            except:
                                continue  # ignore les erreurs et continue la boucle

                    except Exception as e:
                        interes_text = None

                    # Affichage ou retour
                    print(f"[INFO] Información de interés: {interes_text}")

                    #Certfication
                    try:
                        content_el = driver.find_element(By.CSS_SELECTOR, 'div[data-test-id="text-section-text"]')
                        text = content_el.text.strip()
                        
                        # Initialisation de la certification
                        certification = None

                        if "certicar" in text.lower():
                            # Extrait tout ce qui vient après "Certificado por:"
                            match = re.search(r'certificado por:\s*(.*)', text, re.IGNORECASE)
                            if match:
                                certification = match.group(1).strip()
                            else:
                                certification = "Certicar CP/NCI/"
                        else:
                            certification = "Certicar CP/NCI/"
                    except:
                        certification = "Certicar CP/NCI/"

                    # Affichage ou retour
                    print(f"[CERTIFICATION] → {certification}")

                    # ✅ Nettoyage + conversion nutrition
                    nutrition_object = None
                    nutriscore = "N/A"  # valeur par défaut

                    try:
                        if nutritional_info:
                            cleaned_nutritional_info = {}
                            for k, v in nutritional_info.items():
                                try:
                                    if isinstance(v, dict):
                                        # Pour "energy" déjà formaté
                                        cleaned_nutritional_info[k] = v
                                        continue

                                    if isinstance(v, str):
                                        v = v.replace(",", ".").replace("\xa0", " ")
                                        v = re.sub(r"(?<=\d)(?=[a-zA-Zµ])", " ", v).strip()
                                        parts = v.split()
                                        if len(parts) == 1:
                                            value_str, unit = parts[0], "g"  # unité par défaut
                                        else:
                                            value_str, unit = parts[0], parts[1]
                                        cleaned_nutritional_info[k] = f"{value_str} {unit}"
                                    else:
                                        cleaned_nutritional_info[k] = str(v)

                                except Exception:
                                    print(f"⚠️ Erreur nettoyage nutrition pour '{k}': {v}")

                            # Conversion finale en dataclass NutritionDia
                            try:
                                nutrition_object = NutritionDia.convert_dict_to_nutrition_object(cleaned_nutritional_info)
                            except Exception:
                                print(f"❌ Erreur lors de la conversion en objet Nutrition")
                                nutrition_object = None

                            # ——— ICI : calcul du Nutri-score ———
                            if nutrition_object:
                                # asdict transforme le dataclass + sous-dataclasses en dict de primitives
                                nutri_input = asdict(nutrition_object)
                                nutri_input = ProductContentDia.enrich_nested_nutrition (nutri_input)
                                nutriscore = ProductContentDia.calculate_nutriscore_from_nested(nutri_input)
                            else:
                                nutriscore = "N/A"

                    except Exception as e:
                        print(f"❌ Erreur bloc nutrition global: {e}")
                        nutrition_object = None
                        nutriscore = "N/A"

                    origin = None
                    try:
                        if manufacturer_address:
                            origin_data = extract_origin_structure_from_address(manufacturer_address)
                            if origin_data and isinstance(origin_data, dict):
                                ean_list = origin_data.get("ean")
                                if isinstance(ean_list, list) and all(isinstance(code, str) for code in ean_list):
                                    origin = {"ean": ean_list}
                    except Exception as e:
                        print(f"[{index}] ⚠️ Erreur extraction origin depuis adresse fabricant ")
                        origin = None

                    # ✅ Ajout fallback si rien trouvé
                    if origin is None:
                        origin = {"ean": ["ES"]}


                    try:
                        info_el = product_el.find_element(By.CSS_SELECTOR, 'p[data-test-id="search-product-card-info"]')
                        product_info_text = info_el.text.strip()
                    except NoSuchElementException:
                        product_info_text = None

                    print(f"[{index}] Info produit: {product_info_text}")

                     # 🧱 Création objet produit
                    link = Links(links_self=product_url)
                    lang_desc = LangDesc(es=Desc(title=product_title, links=link, images=images, desc=product_summary))
                    mesure_unit_for_price_per_unit, matter, product_pricing_unit = ProductContentDia.get_packaging_info(
                    text if 'text' in locals() else None)
                    formats = ProductContentDia.extract_full_format_from_title(full_title)

                    # Vérification de l'ancienne évolution (si elle existe)
                    if latest_parsed_products:
                        old_evolution = latest_parsed_products[0].evolutions[-1]  # Dernière évolution du produit précédent
                    else:
                        old_evolution = None

                    # Calcul de `created_at` et `updated_at`
                    created_at = datetime.now().strftime("%Y-%m-%dT%H:%M")
                    updated_at = created_at  # Initialement égal à `created_at`   
                    new_evolution = Evolution(
                        format=formats,
                        price_per_packaging=price_per_pack_str,
                        weight_per_packaging=weight,
                        price_per_unit=price_str,
                        nutrition=nutrition_object,
                        ingredients=ingredients,
                        allergens=allergens_found,
                        nutri_Score=nutriscore,
                        certification=certification,
                        offers=offers,
                        
                    )
                    # Mettre à jour `updated_at` seulement si une évolution a eu lieu
                    if old_evolution and self.detect_change(old_evolution, new_evolution):
                        updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M")

                     # 🔒 Forcer la lisibilité JSON pour `matter`
                    if matter is None:
                        matter = "OTHER"
                    elif isinstance(matter, Enum):
                        matter = matter.name

                    #Brand
                    brand = ProductContentDia.extract_brand_from_title(product_title)

                    # 🔒 Initialiser un LabelDia vide pour éviter UnboundLocalError
                    final_label = LabelDia()

                    try:
                        # 📄 Préparer l'entrée pour l'analyse textuelle
                        label_input_dict = {
                            "title": product_title,
                            "details": {
                                "desc": product_summary,
                                "ingredients": ingredients,
                                "other_information": interes_text,
                                "product_info_text": product_info_text
                                
                            }
                        }

                        # 🔍 Analyse textuelle
                        try:
                            label_textual = LabelDia.from_dict_to_object(label_input_dict)
                        except Exception:
                            label_textual = LabelDia()

                        # ✅ Affecter le label extrait
                        final_label = label_textual

                    except Exception as e:
                        print(f"[{index}] ⚠️ Erreur lors de l'extraction des labels textuels : {e}")
                        final_label = LabelDia()  # Fallback sûr

                    # 📦 Construction du dictionnaire complet (y compris False et None)
                    label_dict = {}
                    for key in LabelDia.__annotations__.keys():
                        value = getattr(final_label, key, None)
                        if isinstance(value, bool):
                            label_dict[key] = value  # inclut True ou False
                        

                    print(f"[{index}] 🏷️ Labels (complet) : {json.dumps(label_dict, ensure_ascii=False)}")

                    # ✅ Parsing_duration ici
                    end_parsing_date = datetime.now()
                    parsing_duration = (end_parsing_date - start_parsing_date).seconds

                    categories = find_category_for_url(categories_data, aisle_url)
                    if index == 0:
                        print(f"\n📂 Catégorie hiérarchique utilisée pour ce rayon ({aisle.name}):")
                        print(json.dumps(categories, indent=4, ensure_ascii=False))
                    
                    product = Product(ean=product_id, lang_desc=lang_desc, brand=brand, market=MarketDia(), matter=matter or "OTHER",
                                      mesure_unit_for_price_per_unit=mesure_unit_for_price_per_unit,mesure_unit_for_packaging=weight_unit,
                                      label=label_dict,parsing_duration=parsing_duration,created_at=created_at, updated_at=updated_at,origin=origin,
                                      categories=categories,
                                      )
                    
                    product.evolutions = [new_evolution]
                    products.append(product)

                    if parse_only_first_x_products and len(products) >= parse_only_first_x_products:
                        break

                    time.sleep(0.25)

                except Exception as e:
                    print(f"[{index}] ❌ Erreur inattendue lors de l'analyse du produit : {e}")
                    import traceback
                    traceback.print_exc()
                    skipped_count += 1
                    try:
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                    except:
                        pass
                    continue


            print(f"✅ {len(products)} produits extraits avec succès | ⛔ {skipped_count} ignorés")
            return products

        except Exception as e:
            print(f"❌ Erreur lors de l'analyse des produits : ")
            return []


#Boucle principale
if __name__ == "__main__":
    driver = create_driver()
    print("my main")
    cmdargs = sys.argv
    print(f"The total numbers of args passed to the script: {len(cmdargs)}, Args list: {cmdargs}")

     # ✅ Charger le JSON des catégories DIA
    json_path = get_categories_json_file_uri()
    print(f"✅ Chemin du fichier JSON des catégories DIA : {json_path}")
    with open(json_path, "r", encoding="utf-8") as f:
        categories_data = json.load(f)


    if len(cmdargs) > 1:
        dia = DiaAislesProductsScanner()

        # ✅ Obtenir la classe parser dynamiquement
        parser_name = cmdargs[1]
        parser_class = getattr(static_data_V3, parser_name)


        # ✅ Obtenir les rayons depuis la classe parser
        aisles: List[StaticAisle] = parser_class.aisles
        print(f"aisles: {len(aisles)}")

        if len(aisles) == 0:
            print("empty aisles")
            sys.exit()

        # Filtrage d’un seul rayon via son identifiant (ex: SALADS_AND_PREPARED_VEGETABLES)
        only_one_aisle = None
        if "--only_one_aisle" in cmdargs:
            idx = cmdargs.index("--only_one_aisle")
            only_one_aisle = cmdargs[idx + 1]
            print(f"➡️ Filtrage activé sur un seul rayon : {only_one_aisle}")

        # 📦 Chemin dossier basé sur parser_class
        category_folder_path = os.path.normpath(parser_class.category_path())
        os.makedirs(category_folder_path, exist_ok=True)
        print(f"[DEBUG] category_folder_path: {category_folder_path}")

        # 🔄 Traiter chaque rayon
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

            print(f"aisle.name: {aisle.name}, aisle.url: {aisle.url}, latest_parsed_products count: {len(latest_parsed_products)}")

            # 🗂️ Nom du fichier .json (ex: "Pasta_and_noodles.json")
            aisle_filename = aisle.name.replace("&", "and").replace(" ", "_") + ".json"
            aisle_uri = os.path.join(category_folder_path, aisle_filename)

            # 🔧 Options parsing
            parse_only_ean_title_url_price = "parse_only_ean_title_url_price" in cmdargs
            parse_only_first_x_products = None
            if "parse_only_first_x_products" in cmdargs:
                index = cmdargs.index("parse_only_first_x_products")
                parse_only_first_x_products = int(cmdargs[index + 1])

            parse_only_from_index = None

            # 🚀 Scraping
            new_products = dia.parse_products(
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
                    """Convertit une dataclass (récursive) en dict, en supprimant les champs None."""
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

                    if "categories" in prod_dict:
                        for cat in prod_dict["categories"]:
                            if isinstance(cat["id"], int):
                                cat["id"] = f"L{cat['id']}"  # Appliquer "L" à tous

                    output.append(prod_dict)
                return output


            final_products = remap_category_ids(new_products)
            dump_json_then_write_it_to_file(aisle_uri, final_products)


        if len (cmdargs ) <= 1:
            print("wrong args number")
            sys.exit()
