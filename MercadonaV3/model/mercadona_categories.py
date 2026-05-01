import time
import json
import os
import traceback
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

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
        postal_input.send_keys(postal_code + Keys.ENTER)
        print("📮 Code postal saisi + ENTER")

        WebDriverWait(driver, 20).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, 'input[aria-label="Código postal"]'))
        )
        print("✅ Catalogue chargé avec succès")
    except Exception as e:
        print(f"❌ Erreur initiale : {type(e).__name__}")
        driver.quit()
        exit(1)

class MercadonaCategoriesExtractor:
    def __init__(self, driver):
        self.driver = driver
        self.target_categories_es = {
            "aceite, especias y salsas",
            "agua y refrescos",
            "aperitivos",
            "arroz, legumbres y pasta",
            "azúcar, caramelos y chocolate",
            "bebé",
            "bodega",
            "cacao, café e infusiones",
            "carne",
            "cereales y galletas",
            "charcutería y quesos",
            "congelados",
            "conservas, caldos y cremas",
            "fruta y verdura",
            "huevos, leche y mantequilla",
            "marisco y pescado",
            "mascotas",
            "panadería y pastelería",
            "pizzas y platos preparados",
            "postres y yogures",
            "zumos"
        }

    def get_categories(self) -> dict:
        self.driver.get("https://tienda.mercadona.es/categories")
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.category-menu'))
        )

        for _ in range(10):
            self.driver.execute_script("window.scrollBy(0, 200);")
            time.sleep(0.2)

        menu = self.driver.find_element(By.CSS_SELECTOR, 'ul.category-menu')
        items = menu.find_elements(By.CSS_SELECTOR, 'li.category-menu__item')

        categories = []
        for index in range(len(items)):
            try:
                menu = self.driver.find_element(By.CSS_SELECTOR, 'ul.category-menu')
                items = menu.find_elements(By.CSS_SELECTOR, 'li.category-menu__item')
                item = items[index]

                self.driver.execute_script("arguments[0].scrollIntoView(true);", item)
                time.sleep(0.4)

                button = item.find_element(By.CSS_SELECTOR, 'button')
                label_elem = button.find_element(By.CSS_SELECTOR, 'label.subhead1-r')
                label_es = label_elem.text.strip()

                if label_es.lower() not in {cat.lower() for cat in self.target_categories_es}:
                    continue

                self.driver.execute_script("arguments[0].click();", button)
                time.sleep(1.5)

                subs = []
                try:
                    sub_ul = item.find_element(By.CSS_SELECTOR, 'ul')
                    sub_items = sub_ul.find_elements(By.CSS_SELECTOR, 'li.category-item')

                    for sub_index in range(len(sub_items)):
                        try:
                            menu = self.driver.find_element(By.CSS_SELECTOR, 'ul.category-menu')
                            items = menu.find_elements(By.CSS_SELECTOR, 'li.category-menu__item')
                            item = items[index]
                            sub_ul = item.find_element(By.CSS_SELECTOR, 'ul')
                            sub_items = sub_ul.find_elements(By.CSS_SELECTOR, 'li.category-item')

                            btn = sub_items[sub_index].find_element(By.CSS_SELECTOR, 'button.category-item__link')
                            sub_label = btn.text.strip()

                            self.driver.execute_script("arguments[0].click();", btn)
                            time.sleep(1.5)

                            current_url = self.driver.current_url
                            match = re.search(r'/categories/(\d+)', current_url)
                            sub_id = match.group(1) if match else f"{index}-{sub_index}"

                            subs.append({
                                "id": sub_id,
                                "label": sub_label
                                
                            })

                            self.driver.back()
                            time.sleep(1.5)
                        except Exception as e:
                            print(f"⚠️ Erreur sous-catégorie {sub_index}: {e}")
                except:
                    pass

                if subs:
                    categories.append({
                        "id": subs[0]['id'],
                        "label": label_es,
                        "subs": subs
                    })
            except Exception as e:
                print(f"⚠️ Erreur pour une catégorie : {e}")
                traceback.print_exc()

        print(f"✅ Total catégories enregistrées : {len(categories)}")
        return {
            'id': '0',
            'label': 'mercadona_categories_es',
            'subs': categories
        }

    def save_to_file(self, data: dict, path: str):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"📁 JSON sauvegardé : {path}")

if __name__ == '__main__':
    postal_code = "28001"
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options)
    try:
        handle_initial_popup(driver, postal_code)
        extractor = MercadonaCategoriesExtractor(driver)
        categories = extractor.get_categories()
        output_path = 'C:/PFE_ONRTECH/Project_PFE/VN_parsers2/src/countries/spain/MercadonaV3/model/categories_mercadona.json'
        extractor.save_to_file(categories, output_path)
    finally:
        driver.quit()
