import time
import json
import re
import os
import traceback
import unicodedata
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def normalize(text):
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8').strip().lower()


class EroskiCategoriesExtractor:
    def __init__(self, driver):
        self.driver = driver
        self.allowed_labels = {
            "alimentación",
            "frescos",
            "dulces y desayuno",
            "bebidas",
            "congelados",
            "bebé"
        }

    def accept_cookies(self):
        try:
            btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            self.driver.execute_script("arguments[0].click();", btn)
            print("✅ Cookies acceptés")
        except:
            print("⚠️ Cookies déjà acceptés ou non trouvés")

    def extract_category_id_from_url(self, url):
        match = re.search(r'/supermercado/(\d+)-', url)
        return match.group(1) if match else None

    def extract_subcategories_from_category(self, category_url):
        self.driver.get(category_url)
        time.sleep(2)

        subcategories = []
        try:
            items = self.driver.find_elements(By.CSS_SELECTOR, 'ul.m__list_category__list > li')
            for li in items:
                try:
                    a_tag = li.find_element(By.CSS_SELECTOR, 'a')
                    href = a_tag.get_attribute("href")
                    label = li.find_element(By.CSS_SELECTOR, 'h2.m__list_category__name').text.strip()
                    class_attr = li.get_attribute("class")
                    match = re.search(r'category-(\d+)', class_attr)
                    sub_id = match.group(1) if match else None

                    # 👉 Filtrage spécial pour Bebé
                    if "/2060327-bebe/" in category_url:
                        allowed_baby_urls = {
                            "https://supermercado.eroski.es/es/supermercado/2060327-bebe/2060352-leche-y-aguas/",
                            "https://supermercado.eroski.es/es/supermercado/2060327-bebe/2060383-postres-y-meriendas/",
                            "https://supermercado.eroski.es/es/supermercado/2060327-bebe/5000310-productos-ecologicos/",
                            "https://supermercado.eroski.es/es/supermercado/2060327-bebe/2060361-tarritos-potitos-papillas-y-otros-alimentos/",
                        }
                        if href not in allowed_baby_urls:
                            continue

                    if label and sub_id:
                        subcategories.append({
                            "id": sub_id,
                            "label": label,
                            "subs": []
                        })
                except Exception as e:
                    print(f"⚠️ Erreur dans sous-catégorie spéciale : {e}")
        except Exception as e:
            print(f"⚠️ Impossible de charger les sous-catégories : {e}")
            traceback.print_exc()

        return subcategories


    def get_filtered_categories(self):
        self.driver.get("https://supermercado.eroski.es/es")
        self.accept_cookies()
        time.sleep(2)

        try:
            # 👉 Sélecteur mis à jour pour capter les bons liens <a>
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a.not_clickable[href*="/supermercado/"]'))
            )
            links = self.driver.find_elements(By.CSS_SELECTOR, 'a.not_clickable[href*="/supermercado/"]')
            print(f"🔍 Total de liens détectés : {len(links)}")
        except Exception as e:
            print(f"❌ Menu non chargé ou introuvable : {e}")
            links = []

        normalized_allowed = {normalize(lbl) for lbl in self.allowed_labels}
        raw_categories = []
        congelados_entry = None

        link_data = []
        for link in links:
            try:
                href = link.get_attribute("href")
                label = ""
                try:
                    label = link.get_attribute("innerText").strip()
                    if not label:
                        label = link.get_attribute("aria-label") or ""
                    label = label.strip()
                except:
                    pass
                link_data.append((href, label))
            except Exception as e:
                print(f"⚠️ Erreur lors de la préparation du lien : {e}")


        for idx, (href, label) in enumerate(link_data):
            try:
                if not href:
                    continue

                normalized_label = normalize(label)
                cat_id = self.extract_category_id_from_url(href) or f"category-{idx}"

                if normalized_label not in normalized_allowed:
                    continue

                print(f"✅ Catégorie gardée : {label} - {href}")
                subcats = self.extract_subcategories_from_category(href)

                raw_categories.append({
                    "id": cat_id,
                    "label": label,
                    "subs": subcats
                })

            except Exception as e:
                print(f"⚠️ Erreur dans la boucle principale : {e}")
                traceback.print_exc()

        if congelados_entry:
            print("✅ Catégorie 'Congelados' ajoutée en dernière position")
            raw_categories.append(congelados_entry)

        result = {
            "id": "0",
            "label": "eroski_categories",
            "subs": raw_categories
        }

        print(f"\n📦 Total catégories extraites : {len(raw_categories)}")
        print("📚 Catégories extraites :")
        for cat in raw_categories:
            print(f" - {cat['label']}")

        output_path = 'C:/PFE_ONRTECH/Project_PFE/VN_parsers2/src/countries/spain/EroskiV3/model/categories_eroski2.json'
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4)

        print(f"\n📁 JSON sauvegardé : {output_path}")


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        extractor = EroskiCategoriesExtractor(driver)
        extractor.get_filtered_categories()
    finally:
        driver.quit()