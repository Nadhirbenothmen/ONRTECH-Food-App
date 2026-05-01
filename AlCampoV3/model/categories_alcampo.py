#Sub
import sys
import time
import json
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

# Ajouter le chemin vers vos modules
sys.path.append('src')
sys.path.append('./')

from src.utils.appium_utils import (
    wait_el,
    wait_els,
    wait_el_click
)

class AlcampoCategoriesExtractor:
    def __init__(self, driver):
        self.driver = driver
        self.total_categories_number = 0
        self.target_labels = {
            "frescos",
            "leche, huevos, lácteos, yogures y bebidas vegetales",
            "alimentación",
            "desayuno y merienda",
            "congelados",
            "comida preparada",
            "bebidas",
            "supermercado ecológico",
            "sin gluten / sin lactosa, nutrición deportiva y funcional",
            "veganos",
            "bebé",
            "mascotas"
        }

    def accept_cookies(self):
        try:
            wait_el_click(self.driver, By.ID, "onetrust-accept-btn-handler", timeout=2)
            print("✅ Cookies acceptés")
        except Exception:
            print("⚠️ Bouton cookies non trouvé ou déjà accepté")

    def open_menu(self):
        wait_el_click(self.driver, By.XPATH, "//span[text()='Menú']", timeout=2)
        wait_el(self.driver, By.ID, "nav-menu-pane-0", timeout=2)

    def extract_category_id_from_full_url(self, url: str) -> str:
        m = re.search(r'/([^/?#]+)(?:\?|$)', url or '')
        return m.group(1) if m else None

    def extract_subcategories(self, category_url):
        subs = []
        try:
            self.driver.get(f"{category_url}&source=navigation")
            time.sleep(2)

            anchors_lvl2_raw = wait_els(self.driver, By.CSS_SELECTOR, "a[data-test='root-category-link']", timeout=2) or []
            hrefs_lvl2 = [(a.text.strip(), a.get_attribute('href')) for a in anchors_lvl2_raw]

            for label_lvl2, href_lvl2 in hrefs_lvl2:
                if not href_lvl2:
                    continue
                if href_lvl2.startswith('/'):
                    href_lvl2 = f"https://www.compraonline.alcampo.es{href_lvl2}"
                id_lvl2 = self.extract_category_id_from_full_url(href_lvl2)
                if not id_lvl2:
                    continue

                subs_lvl3 = []
                try:
                    self.driver.get(href_lvl2)
                    time.sleep(2)

                    anchors_lvl3 = wait_els(self.driver, By.CSS_SELECTOR, "ul.sc-xdgqhu-1 a[data-test='root-category-link']", timeout=5) or []
                    for a3 in anchors_lvl3:
                        try:
                            label_lvl3 = a3.text.strip()
                            href_lvl3 = a3.get_attribute('href') or ''
                            if href_lvl3.startswith('/'):
                                href_lvl3 = f"https://www.compraonline.alcampo.es{href_lvl3}"
                            id_lvl3 = self.extract_category_id_from_full_url(href_lvl3)
                            if id_lvl3:
                                subs_lvl3.append({
                                    "id": id_lvl3,
                                    "label": label_lvl3
                                    
                                })
                        except:
                            continue  # ignorer erreurs individuelles

                except Exception as e:
                    print(f"⚠️ Pas de niveau 3 pour {label_lvl2} : {e}")

                subs.append({
                    "id": id_lvl2,
                    "label": label_lvl2,
                    "subs": subs_lvl3
                })

        except Exception as e:
            print(f"⚠️ Erreur dans extract_subcategories: {e}")
        return subs


    def extract_category_id_from_url(self, url: str) -> str:
        m = re.search(r'/categories/[^/]+/([^/?#]+)', url or '')
        return m.group(1) if m else None

    def parse_categories(self):
        root_url = "https://www.compraonline.alcampo.es/"
        self.driver.get(root_url)
        self.accept_cookies()
        time.sleep(1)
        self.open_menu()

        panel = wait_el(self.driver, By.ID, 'nav-menu-pane-0', timeout=2)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", panel)
        time.sleep(0.5)

        anchors = wait_els(panel, By.CSS_SELECTOR, "li[role='menuitem'] > a[data-test]", timeout=2) or []

        category_infos = []
        for a in anchors:
            try:
                raw_label = a.get_attribute('data-test') or ''
                label = raw_label.strip()
                if label.lower() not in self.target_labels:
                    continue
                href = a.get_attribute('href') or ''
                href = href.strip()
                if href.startswith('/'):
                    href = f"https://www.compraonline.alcampo.es{href}"
                cat_id = self.extract_category_id_from_url(href)
                if not cat_id:
                    continue
                category_infos.append((label, href, cat_id))
            except Exception as e:
                print(f"⚠️ Erreur lecture lien principal : {e}")
                continue

        categories = []
        for label, href, cat_id in category_infos:
            print(f"🔍 Catégorie: {label} - {href} - {cat_id}")
            subs = self.extract_subcategories(href)
            categories.append({"id": cat_id, "label": label, "subs": subs})
            self.total_categories_number += 1

        data = {"id": "0", "label": "alcampo_categories", "subs": categories}
        output_file = 'C:/PFE_ONRTECH/Project_PFE/VN_parsers2/src/countries/spain/AlCampoV3/model/alcampo_categories.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"✅ Extraction terminée : {self.total_categories_number} catégories, avec sous-catégories, dans {output_file}")

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    try:
        parser = AlcampoCategoriesExtractor(driver)
        parser.parse_categories()
    finally:
        driver.quit()
