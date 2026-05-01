import sys
import time
import json
import re
import traceback
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_el(driver, by, value, timeout=10):
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
    except Exception as e:
        print(f"❌ Impossible de trouver l’élément ({by}, {value}) dans les {timeout}s.")
        raise e

CATEGORIES_TO_KEEP = {
    "Air_Fryer", "Baby", "Beers_Wines_And_Spirits", "Biscuits_Bruns_And_Cereals",
    "Breads_Flours_And_Doughs", "Butchery", "Canned_Food_Broths_And_Creams",
    "Charcuterie_And_Cheeses", "Chips_Pickles_And_Nuts", "Coffee_Cocoa_And_Infusions",
    "Fish_Smoked_Fish_And_Seafood", "Frozen_Food", "Fruits", "Milk_Eggs_And_Butter",
    "Oil_Sauces_And_Spicess", "Pets", "Pizzas_And_Prepared_Dishes",
    "Rice_Pasta_And_Pulses", "Sugar_Chocolates_And_Candies", "Vegetables",
    "Water_Soft_Drinks_And_Juices", "Yoghurts_And_Desserts"
}

CATEGORY_LABEL_MAPPING = {
    "Freidora de aire - Airfryer": "Air_Fryer",
    "Bebé": "Baby",
    "Cervezas, vinos y bebidas con alcohol": "Beers_Wines_And_Spirits",
    "Galletas, bollos y cereales": "Biscuits_Bruns_And_Cereals",
    "Panes, harinas y masas": "Breads_Flours_And_Doughs",
    "Carnicería": "Butchery",
    "Conservas, caldos y cremas": "Canned_Food_Broths_And_Creams",
    "Charcutería y quesos": "Charcuterie_And_Cheeses",
    "Patatas fritas, encurtidos y frutos secos": "Chips_Pickles_And_Nuts",
    "Café, cacao e infusiones": "Coffee_Cocoa_And_Infusions",
    "Pescados, mariscos y ahumados": "Fish_Smoked_Fish_And_Seafood",
    "Congelados": "Frozen_Food",
    "Frutas": "Fruits",
    "Leche, huevos y mantequilla": "Milk_Eggs_And_Butter",
    "Aceites, salsas y especias": "Oil_Sauces_And_Spicess",
    "Mascotas": "Pets",
    "Pizzas y platos preparados": "Pizzas_And_Prepared_Dishes",
    "Arroz, pastas y legumbres": "Rice_Pasta_And_Pulses",
    "Azúcar, chocolates y caramelos": "Sugar_Chocolates_And_Candies",
    "Verduras": "Vegetables",
    "Agua, refrescos y zumos": "Water_Soft_Drinks_And_Juices",
    "Yogures y postres": "Yoghurts_And_Desserts"
}

class DiaCategoriesExtractor:
    def __init__(self, driver):
        self.driver = driver

    def accept_cookies(self):
        try:
            btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
            )
            self.driver.execute_script("arguments[0].click();", btn)
            print("✅ Cookies acceptés")
        except Exception as e:
            print(f"⚠️ Cookies déjà acceptés ou bouton introuvable : {e}")

    def extract_category_id_from_url(self, url):
        match = re.search(r'/c/([^/]+)', url)
        return match.group(1) if match else None

    def extract_subcategories_from_category_page(self, url):
        self.driver.get(url)
        time.sleep(2)
        subcategories = []

        try:
            ul = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'ul[data-test-id="sub-categories-list"]'))
            )
            sub_items = ul.find_elements(By.CSS_SELECTOR, 'div[data-test-id="sub-category-item"]')
            for sub in sub_items:
                try:
                    a_tag = sub.find_element(By.CSS_SELECTOR, 'a[data-test-id="sub-category-item-link"]')
                    label = a_tag.find_element(By.CSS_SELECTOR, 'span[data-test-id="sub-category-item-title"]').text.strip()
                    href = a_tag.get_attribute("href")
                    sub_id = self.extract_category_id_from_url(href)
                    if not label.lower().startswith("todo "):
                        subcategories.append({
                            "id": sub_id or "unknown",
                            "label": label
                        })

                except Exception as sub_err:
                    print(f"⚠️ Erreur sur une sous-catégorie : {sub_err}")
        except Exception:
            print("⚠️ Aucun bloc de sous-catégories détecté")

        return subcategories

    def parse_categories(self, rayon_url="https://www.dia.es/"):
        try:
            self.driver.get(rayon_url)
            self.accept_cookies()

            print("⏳ Ouverture du menu de navigation...")
            btn = wait_el(self.driver, By.CSS_SELECTOR, 'button[data-test-id="desktop-category-button"]')
            self.driver.execute_script("arguments[0].click();", btn)
            print("✅ Menu des catégories ouvert.")

            ul = wait_el(self.driver, By.CSS_SELECTOR, 'ul[data-test-id="categories-list"]')
            li_elements = ul.find_elements(By.CSS_SELECTOR, 'li[data-test-id="categories-list-element"]')
            print(f"🔍 Nombre total de catégories trouvées : {len(li_elements)}")

            categories = []

            for idx in range(len(li_elements)):
                try:
                    # Recharger les éléments `li` à chaque itération
                    ul = wait_el(self.driver, By.CSS_SELECTOR, 'ul[data-test-id="categories-list"]')
                    li_elements = ul.find_elements(By.CSS_SELECTOR, 'li[data-test-id="categories-list-element"]')
                    li = li_elements[idx]

                    a_tag = li.find_element(By.CSS_SELECTOR, 'a[data-test-id="category-item-link"]')
                    title = li.find_element(By.CSS_SELECTOR, 'span[data-test-id="category-item-title"]').text.strip()
                    url = a_tag.get_attribute("href")
                    cat_id = self.extract_category_id_from_url(url) or f"category-{idx}"

                    mapped_label = CATEGORY_LABEL_MAPPING.get(title)
                    if not mapped_label or mapped_label not in CATEGORIES_TO_KEEP:
                        print(f"⏩ Catégorie ignorée : {title}")
                        continue

                    print(f"\n🔸 Catégorie gardée : {title} - ID: {cat_id}")
                    subcats = self.extract_subcategories_from_category_page(url)

                    categories.append({
                        "id": cat_id,
                        "label": title,
                        "subs": subcats
                    })

                    # Revenir à la page d’accueil pour continuer la boucle
                    self.driver.get(rayon_url)
                    time.sleep(1)
                    btn = wait_el(self.driver, By.CSS_SELECTOR, 'button[data-test-id="desktop-category-button"]')
                    self.driver.execute_script("arguments[0].click();", btn)

                except Exception as e:
                    print(f"[ERROR] Problème sur la catégorie {idx + 1}: {e}")
                    traceback.print_exc()

            result = {
                "id": "0",
                "label": "dia_categories",
                "subs": categories
            }

            output_path = 'C:/PFE_ONRTECH/Project_PFE/VN_parsers2/src/countries/spain/DiaV3/model/categories_dia.json'
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=4)

            print(f"✅ Fichier JSON sauvegardé : {output_path}")

        except Exception as e:
            print(f"[FATAL ERROR] {e}")
            traceback.print_exc()

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    extractor = DiaCategoriesExtractor(driver)
    extractor.parse_categories()
    driver.quit()
