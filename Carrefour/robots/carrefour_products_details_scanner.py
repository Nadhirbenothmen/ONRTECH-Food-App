# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Jan 28, 2019

@author: marwen
"""

import json
import os
from pathlib import Path
import re
import sys
from datetime import datetime
from typing import List, Literal, Optional

import dacite
import dacite.exceptions
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

from src.countries.france.carrefour.model.product_carrefour import EvolutionCarrefour, OfferCarrefour, ProductCarrefour
from src.countries.france.carrefour.model.product_content_carrefour import NutritionCarrefour, ProductContentCarrefour
from src.countries.france.carrefour.robots import URL_BASE_CARREFOUR, webdriverInstance  # NOQA
from src.countries.france.carrefour.robots.carrefour_static_ailes import get_static_aisles_from_user_cmdargs  # NOQA
from src.model.custom_tree import CustomTree
from src.model.product import (
    Category,
    CustomerReviews,
    Desc,
    Evolution,
    Label,
    LangDesc,
    Nutrition,
    Offer,
    Origin,
    Product,
    get_latest_parsed_products,
)
from src.model.product_content import convert_format_product
from src.model.static_category_aisle import StaticAisle
from src.utils.appium_utils import get_attribute_from_element, wait_el, wait_el_click, wait_el_text, wait_els  # NOQA
from src.utils.ean_country_checker import get_country_code_from_country_name_in_french_lang, get_country_code_from_ean
from src.utils.my_utils import all_attrs_are_none_or_zero, convert_to_float, custom_dump, dump_json_then_write_it_to_file, find_all_substrings_in_text, write_output_to_file


class ScannerProductDetails:
    def __init__(self):
        self.total_products_number = 0
        self.first_access = True

    def get_url_response_via_curl(self, product: dict) -> dict | None:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:129.0) Gecko/20100101 Firefox/129.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
            'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'cross-site',
            'Connection': 'keep-alive',
            'Cookie': '__cf_bm=uUn1ktvpMx9PNPB8ZrRThJR.Mp3MH8D_IdrjK1qlv2s-1722954135-1.0.1.1-0z_tYFgbBd7gdOxCo8fQ.9PJWW3EMMRoCR6OU06vLVIAnBHx8KFsM7XTynMUFmKlBkfDz3VHjIqGT8cZmo3aKQ; tc_cj_v2=%5Ecl_%5Dny%5B%5D%5D_mmZZZZZZKQLLSONNJKMRSZZZ%5D; tc_cj_v2_cmp=; tc_cj_v2_med=; tc_ts=75; pageCounterCrfOne=2; carrefour_counter=1722954401797%7C18147653384229%7Cp0%7Ce0%7Cv1%7Cc248.01%7CServerSide; tc_ab=1; FRONTONE_ONLINE=1725546138; FRONTONE_SESSION_ID=ac9277aca2e9b4b6938a00f0125a48f6dc5839d6; CAID=202408061525451233509379; FRONTONE_SESSID=cu2krftfk7p4ln5jiuqaebcsld; WID=2cc4b813-43a1-4a10-b95c-e0b3aaa4025f; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Aug+06+2024+15%3A26%3A41+GMT%2B0100+(heure+normale+d%E2%80%99Europe+centrale)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=85312a91-0a2c-4fe3-b411-252d150e9f6a&interactionCount=1&landingPath=NotLandingPage&groups=C0048%3A1%2CC0001%3A1%2CC0040%3A0%2CC0032%3A0%2CC0025%3A0%2CC0020%3A0%2CC0037%3A0%2CC0039%3A0%2CC0036%3A0%2CC0041%3A0%2CC0042%3A0%2CC0044%3A0%2CC0043%3A0%2CC0045%3A0%2CC0046%3A0%2CC0049%3A0%2CC0047%3A0%2CC0023%3A0%2CC0056%3A0%2CC0038%3A0%2CC0082%3A0%2CC0026%3A0%2CC0177%3A0%2CC0113%3A0%2CC0089%3A0%2CC0092%3A0%2CC0190%3A0%2CC0166%3A0%2CC0222%3A0%2CC0223%3A0%2CC0231%3A0%2CC0004%3A0%2CC0022%3A0%2CC0054%3A0%2CC0179%3A0%2CC0146%3A0%2CC0052%3A0%2CC0034%3A0%2CC0063%3A0%2CC0157%3A0%2CC0003%3A0%2CC0212%3A0%2CC0081%3A0%2CC0051%3A0%2CC0136%3A0%2CC0135%3A0%2CC0007%3A0%2CV2STACK42%3A0; aaaaaaaaa944fac35b02f4d9a99619247b88ad463_cs_nt=ODI5NDc5NTUtMGE1NC00MzlkLTg5OWMtMzNiZjRhYWUzNmEw; OptanonAlertBoxClosed=2024-08-06T14:26:41.288Z; eupubconsent-v2=CQC7X5gQC7X5gAcABBENBAFwAAAAAAAAAChQAAAAAAChIAYAygF5gTAHQAwBlALzAmAOAAgSEJQAQF5lIAYAygF5gTAA.YAAAAAAAAAAA; OneTrustGroupsConsent=%2CC0048%2CC0001%2C'
        }

        product_link = URL_BASE_CARREFOUR + product["links"]["self"]
        print(f"product_link: {product_link}")
        try:
            response = requests.get(product_link, headers=headers)
            response.raise_for_status()
            json_data = response.json()
            write_output_to_file(data=json_data, file_name="marwen_curl",
                                 path_includes_in_file_name=True, include_seconds_in_date=False, extension='.json')
            return json_data
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP error occurred while retrieving details for link: {
                  product_link}: {errh}")
        except requests.exceptions.RequestException as err:
            print(f"Error occurred while retrieving details for link: {
                  product_link}: {err}")
        return None

    def parse_product_details_only_if_no_available(self, driver: webdriver, product: dict) -> Product | None:
        details = product.get("details", None)
        print(f"{details is None or details == {}
                 }: the details exist for product: {product["title"]}")
        if not details or details == {}:
            # parse again product details then return
            product_details = self.parse_product_details(driver, product)
            return product_details
        return details

    def parse_product_details(self, driver: webdriver, product: Product, should_merge_evolutions=False) -> Product | None:
        if not isinstance(product, Product):
            return None
        product_link = product.lang_desc.fr.links.links_self
        product_link = URL_BASE_CARREFOUR + \
            product_link if URL_BASE_CARREFOUR not in product_link else product_link

        try:
            driver.get(product_link)
            if self.first_access:
                # should click on cookies panel just the first time the driver is launched
                wait_el_click(
                    driver, By.ID, "onetrust-reject-all-handler", timeout=5)
                self.first_access = False

            start_parsing_date = datetime.now()
            # get categories
            categories = self.get_categories(driver)

            product.updated_at = datetime.now().isoformat(timespec="minutes")

            product_desc = None
            evolution_availability_el = wait_el(
                driver, By.ID, "tag-unavailable")
            evolution_availability = evolution_availability_el is None
            # check first if there is a badge list
            label, french_origin = self.get_label_and_origin(driver)

            # nutriscore
            evolution_nutriscore = self.get_nutriscore(driver)

            # images:
            images_urls = self.get_images(driver)

            partial_origin: Optional[str] = None
            all_evolutions: List[Evolution] = None
            evolution_certification: Optional[str] = None
            evolution_ingredients: Optional[str] = None
            evolution_nutrition: Optional[NutritionCarrefour] = None
            customerReviews: Optional[CustomerReviews] = None
            offers = None
            price_per_packaging = None
            weight_per_packaging = None
            packaging_format = None
            price_per_unit_without_weight = None
            on_discount = None
            freshness_days = None
            unit_of_mesure = None
            packaging_measure_unit = None
            # get Description by clicking on  button
            secondary_details_el = wait_el(
                driver, By.CSS_SELECTOR, "#product-characteristics > div")
            if secondary_details_el:
                # Déscription
                secondary_details_desc = wait_el(
                    secondary_details_el, By.CSS_SELECTOR, "#product-characteristics-description")
                if secondary_details_desc:
                    product_desc = wait_el_text(
                        secondary_details_desc, By.CSS_SELECTOR, "div:nth-child(2) > div")
                    if find_all_substrings_in_text(ProductContentCarrefour.FRENCH_PRESENCE, product_desc) is not None:
                        partial_origin = "FR"

                # characteristics-composition
                secondary_details_characteristics_el = wait_el(
                    secondary_details_el, By.CSS_SELECTOR, "#product-characteristics-composition", 1)
                if secondary_details_characteristics_el:
                    # Certification
                    secondary_details_certification = wait_el(
                        secondary_details_characteristics_el, By.CSS_SELECTOR, ".allergobox-details")
                    evolution_certification = 'ConsoTrust-AllergoBox' if secondary_details_certification else None

                    # Nutritions
                    evolution_nutrition = self.get_nutrition(
                        secondary_details_el)

                    product_title_desktop = wait_el(
                        driver, By.ID, 'product-title-desktop', timeout=0.5)
                    if product_title_desktop:
                        title = wait_el_text(
                            product_title_desktop, By.CSS_SELECTOR, ".product-title__title")
                        packaging_format = wait_el_text(
                            product_title_desktop, By.CSS_SELECTOR, ".product-title__packaging")
                        price_per_unit = wait_el_text(
                            product_title_desktop, By.CSS_SELECTOR, ".product-title__per-unit-label")
                        unit_of_mesure, matter, price_per_unit_without_weight = ProductContentCarrefour.get_packaging_info(
                            price_per_unit)
                    (packaging_measure_unit, weight_per_packaging) = convert_format_product(
                        packaging_format)

                    data_service_el = wait_el(
                        driver, By.ID, "data-service-crf-1")
                    if data_service_el:
                        price_per_packaging_part1 = wait_el_text(data_service_el, By.CSS_SELECTOR,
                                                                 ".product-price__amounts p:nth-of-type(1)")
                        price_per_packaging_part2 = wait_el_text(data_service_el, By.CSS_SELECTOR,
                                                                 ".product-price__amounts p:nth-of-type(2)")
                        price_per_packaging_str = f"{
                            price_per_packaging_part1}" + f"{price_per_packaging_part2}"

                        price_per_packaging = convert_to_float(price_per_packaging_str.replace(
                            ',', '.')) if price_per_packaging_str else None
                        print(f"price_per_packaging: {
                              price_per_packaging}, price_per_packaging_part1: {price_per_packaging_part1}, price_per_packaging_part2: {price_per_packaging_part2}, price_per_packaging_str: {price_per_packaging_str}")

                        offer_desc = wait_el_text(
                            data_service_el, By.CSS_SELECTOR, '[data-testid="promotion-label"]')
                        offers = [OfferCarrefour.extractInfo(
                            offer_desc)] if offer_desc else None

                    # on discount
                    on_discount = self.get_on_discount(driver)
                    # freshness days:
                    freshness_days = self.get_freshness_days(driver)
                    # reviews
                    customerReviews = self.get_reviews(driver)
                    # ingredients
                    evolution_ingredients = wait_el_text(
                        secondary_details_el, By.CSS_SELECTOR, "div[data-testid='product-composition-ingredients'] > div:nth-child(2) > div")

                    print(f"title: {title}, packaging_format: {packaging_format}, unit_of_mesure: {unit_of_mesure}, matter: {matter}, price_per_unit_without_weight: {
                          price_per_unit_without_weight}, price_per_packaging: {price_per_packaging}, offer: {offers}, on_discount: {on_discount}")
            new_evolution = EvolutionCarrefour(format=packaging_format, availability=evolution_availability, price_per_unit=price_per_unit_without_weight,
                                               price_per_packaging=price_per_packaging, nutriscore=evolution_nutriscore, certification=evolution_certification, nutrition=evolution_nutrition,
                                               ingredients=evolution_ingredients, allergens=None, reviews=customerReviews,
                                               on_discount=on_discount, weight_per_packaging=weight_per_packaging, offers=offers)
            if should_merge_evolutions:
                all_evolutions = Evolution.merge_evolutions(
                    new_evolution, product.evolutions, EvolutionCarrefour.is_deep_equal)
            else:
                all_evolutions = [new_evolution]

            print(f"ell evols length: {
                  len(all_evolutions) if all_evolutions else 0}")
            explicit_origin = wait_el_text(
                driver, By.CSS_SELECTOR, "#product-origin .product-origin__content p")
            explicit_origin = explicit_origin if explicit_origin else french_origin
            origin = Origin(ean=get_country_code_from_ean(ean=product.ean), explicit=get_country_code_from_country_name_in_french_lang(explicit_origin),
                            partial=partial_origin)

            product.origin = None if all_attrs_are_none_or_zero(
                origin) else origin
            product.freshness = freshness_days
            product.categories = categories
            product.evolutions = all_evolutions
            product.label = None if all_attrs_are_none_or_zero(
                label) else label
            product.lang_desc.fr.desc = product_desc
            product.lang_desc.fr.images = images_urls if images_urls and len(
                images_urls) > 0 else None
            product.mesure_unit_for_price_per_unit = unit_of_mesure
            product.mesure_unit_for_packaging = packaging_measure_unit

            product.parsing_duration = (
                datetime.now() - start_parsing_date).seconds
            print("returning product...")
            return product

        except requests.Timeout:
            print(f"Timeout occurred for requested page: {product_link}")
            return None if all_attrs_are_none_or_zero(product) else product
        except dacite.DaciteError as e:
            print(f'product_link: {product_link}, WrongTypeError:{e}')
            sys.exit()
        except KeyboardInterrupt:
            sys.exit()
        except (UnboundLocalError, AttributeError) as e:
            print(f'product_title:{product.title}, UnboundLocalError:{e}')
            sys.exit()
        except:
            print("global except error:", sys.exc_info())
            return None if all_attrs_are_none_or_zero(product) else product

    def get_on_discount(self, driver) -> (Literal[True] | None):
        on_discount_el = wait_el(
            driver, By.CSS_SELECTOR, 'div.product-price.product-price--promo.product-price--size-xl.product-price--inline-amounts')
        on_discount = True if on_discount_el else None
        return on_discount

    def get_freshness_days(self, driver) -> (float | None):
        freshness_el_text = wait_el_text(
            driver, By.CSS_SELECTOR, "#data-produit-image .freshness-badge", 0.5)
        freshness_days = None if freshness_el_text else ProductContentCarrefour.get_freshness_days(
            freshness_el_text)
        freshness_days = float(freshness_days) if freshness_days else None
        return freshness_days

    def get_categories(self, driver) -> List[Category] | None:
        categories: Optional[List[Category]] = None
        # last_aisle_el_text = wait_el_text(
        #     driver, By.CSS_SELECTOR, "#data-filariane > ol > li:nth-last-child(2) > a > span")
        last_aisle_el = wait_el(
            driver, By.CSS_SELECTOR, "nav.plp-banner-marketplace__breadcrumbs > ol > li:nth-last-child(2)")
        last_aisle_el_text = wait_el_text(
            last_aisle_el, By.CSS_SELECTOR, "a:nth-of-type(2)")

        if last_aisle_el_text:
            print(f"last_aisle_id_el valid: {last_aisle_el_text}")
            file_uri = self.get_categories_json_file_uri()
            aisles = CustomTree.aisles_ancestors_fetcher(
                last_aisle_el_text, file_uri=file_uri)
            if aisles:
                categories = [Category(id=int(aisle.id), label=aisle.label)
                              for aisle in aisles]
            print(f"res aisles: {custom_dump(aisles)}")
        return categories

    def get_categories_json_file_uri() -> Optional[str]:
        script_path = Path(__file__).resolve()  # Get full path of the script
        script_folder = script_path.parent      # Get the folder containing the script
        parent_folder = script_folder.parent    # Remove the last folder
        model_folder = os.path.join(parent_folder, 'model')  # add model folder
        model_file = os.path.join(
            model_folder, 'categories_carrefour.json')  # add file name
        print(f"script_path: {script_path}, script_folder:{
              script_folder}, parent_folder:{parent_folder}, model_file:{model_file}")
        return model_file or "src/countries/france/carrefour/model/categories_carrefour.json"

    def get_images(self, driver) -> Optional[List[str]]:
        images_urls: List[str] = []
        images = wait_els(driver, By.CSS_SELECTOR,
                          'div.pdp-hero__thumbs.pdp-hero__thumbs--top-left img')
        if images:
            for image in images or []:
                image_id = get_attribute_from_element(image, 'src') or None
                if image_id:
                    image_url = image_id.replace(
                        "p_43x43", "p_540x540") or None
                    images_urls.append(image_url)
        else:
            image = wait_el(driver, By.CSS_SELECTOR, '#data-produit-image img')
            image_url = get_attribute_from_element(image, 'src') or None
            if image_url:
                images_urls.append(image_url)
        return images_urls

    def get_nutrition(self, driver: webdriver) -> Optional[NutritionCarrefour]:
        nutritional_details_table_els = wait_els(
            driver, By.CLASS_NAME, 'nutritional-fact')
        if nutritional_details_table_els:
            nutrition_dict = {}
            for nutritional_details_table_row_els in nutritional_details_table_els:
                nutrition_name = wait_el_text(
                    nutritional_details_table_row_els, By.CSS_SELECTOR, "th > span")
                nutrition_value = wait_el_text(
                    nutritional_details_table_row_els, By.CSS_SELECTOR, "td > span")
                nutrition_dict[nutrition_name] = nutrition_value
            nutrition_dict = NutritionCarrefour.compute_nutrition_values_per_100_g_or_ml(
                nutrition_dict)

            evolution_nutrition = NutritionCarrefour(
            ).convert_dict_to_nutrition_object(nutrition_dict)
            return evolution_nutrition
        return None

    def get_reviews(self, driver: webdriver) -> Optional[CustomerReviews]:
        reviews_section_el = wait_el(
            driver, By.CSS_SELECTOR, '#pdp-customers-reviews')
        if reviews_section_el:
            reviews_average = wait_el_text(
                reviews_section_el, By.CSS_SELECTOR, 'p.rating-summary__average')
            reviews_count = wait_el_text(
                reviews_section_el, By.CSS_SELECTOR, 'p.rating-summary__count')
            reviews_average = reviews_average.replace(
                " sur 5", "") if reviews_average else None
            reviews_average = convert_to_float(reviews_average.replace(
                ',', '.')) if reviews_average else None
            reviews_count = reviews_count.replace(
                " avis", "") if reviews_count else None
            reviews_count = int(
                reviews_count) if reviews_count else None
            customerReviews = CustomerReviews(
                average=reviews_average, count=reviews_count) if reviews_average else None
            return customerReviews
        return None

    def get_nutriscore(self, driver: webdriver):
        nutrition_score_el = wait_el(
            driver, By.CSS_SELECTOR, "img.image.product-badge__icon__img[alt='Nutri-Score']")
        nutriscore = get_attribute_from_element(
            nutrition_score_el, "src", 'nutrition')
        evolution_nutriscore = nutriscore[-5] if nutriscore and len(
            nutriscore) > 5 else None

        return evolution_nutriscore

    def get_label_and_origin(self, driver: webdriver) -> tuple[Label | None, str | None]:
        if not driver:
            return None
        label = Label()
        french_origin = None
        badge_list_el = wait_el(
            driver, By.CSS_SELECTOR, "ul.product-badges-list")
        if badge_list_el:
            nutrition_fat_free = wait_el(
                badge_list_el, By.CSS_SELECTOR, 'li[data-flag-id="flag.common.fatfree"]')
            nutrition_added_sugar_free = wait_el(
                badge_list_el, By.CSS_SELECTOR, 'li[data-flag-id="flag.common.addedsugarfree"]')
            nutrition_gluten_free = wait_el(
                badge_list_el, By.CSS_SELECTOR, 'li[data-flag-id="flag.common.glutenfree"]')
            nutrition_ogm_free = wait_el(
                badge_list_el, By.CSS_SELECTOR, 'li[data-flag-id="flag.common.gmofree"]')
            nutrition_for_pregnant = wait_el(
                badge_list_el, By.CSS_SELECTOR, 'li[data-flag-id="flag.common.avoidifpregnant"]')
            nutrition_for_vegetarian = wait_el(
                badge_list_el, By.CSS_SELECTOR, 'li[data-flag-id="flag.common.fruitslegumesfr"]')
            nutrition_bio = wait_el(
                badge_list_el, By.CSS_SELECTOR, 'li[data-flag-id="flag.common.organic"]')
            nutrition_frozen = wait_el(
                badge_list_el, By.CSS_SELECTOR, 'li[data-flag-id="flag.common.frozen"]')
            nutrition_fr_greengrocery = wait_el(
                badge_list_el, By.CSS_SELECTOR, 'li[data-flag-id="flag.common.fruitslegumesfr"]')
            nutrition_regional_greengrocery = nutrition_fr_greengrocery if nutrition_fr_greengrocery is not None else wait_el(
                badge_list_el, By.CSS_SELECTOR, 'li[data-flag-id="flag.common.regional"]')
            frenchpoultrymeat = wait_el(
                badge_list_el, By.CSS_SELECTOR, 'li[data-flag-id="flag.common.frenchpoultrymeat"]')
            label.fat_free = True if nutrition_fat_free else None
            label.sugar_added_free = True if nutrition_added_sugar_free else None
            label.gluten_free = True if nutrition_gluten_free else None
            label.pregnancy_unsafe = True if nutrition_for_pregnant else None
            label.bio = True if nutrition_bio else None
            label.vegetarian = True if nutrition_for_vegetarian else None
            label.frozen = True if nutrition_frozen else None
            label.fr_greengrocery = True if nutrition_fr_greengrocery is not None or nutrition_regional_greengrocery is not None else None
            label.gmo_free = True if nutrition_ogm_free else None

            french_origin = nutrition_fr_greengrocery or nutrition_regional_greengrocery or frenchpoultrymeat
            french_origin = "france" if french_origin else None
        return label, french_origin


'''
This class goals:
Scan for products details from a file containing products
which are with some or without details.
run it by executing:
/Users/marwenrhayem/Projects/mrh/LaNoria_backoffice/.venv/bin/python3 /Users/marwenrhayem/Projects/mrh/LaNoria_backoffice/src/robots/france/carrefour/scanner_product_details.py src/robots/france/carrefour/products/categorie_cremerie/cremerie_desserts_compotes_detailed_24_02_14_00.07.json  parse_product_details_only_if_no_available

1st args (required): reserved to the script.
2nd args (required): the input file containing a list of products
3nd args (optional): is either 
    1- "parse_product_details_only_if_no_available":
    2- "parse_product_details": if we would like to override existing details
'''
if __name__ == "__main__":
    print("my main")
    # Get the arguments list
    cmdargs = sys.argv

    # Print it
    print(f"The total numbers of args passed to the script: {
          len(cmdargs)}, Args list: + {cmdargs}")

    scannerProductDetails = ScannerProductDetails()
    aisles: List[StaticAisle] = get_static_aisles_from_user_cmdargs(
        cmdargs=cmdargs)
    print(f"aisles: {len(aisles)}")
    if not aisles:
        print("empty aisles")
        sys.exit()
    for aisle1 in aisles:
        aisle: StaticAisle = aisle1
        products: List[ProductCarrefour] = []
        products_detailed: List[Product] = []
        file_uri = aisle.original_file_uri
        should_merge_evolutions = False
        if "get_latest_parsed_products" in cmdargs:
            products = get_latest_parsed_products(aisle=aisle)
        else:
            json_file = open(file_uri, encoding='utf-8')
            products = json.load(json_file)
        should_merge_evolutions = "merge_evolutions" in cmdargs
        products_count = len(products or [])
        start_parsing_date_aisle = datetime.now()
        for index, product in enumerate(products or []):
            product = dacite.from_dict(
                data_class=Product, data=product, config=dacite.Config(strict=True))
            aisle_parsing_duration = (
                datetime.now() - start_parsing_date_aisle).seconds
            print(f'time ellapsed parsing aisle:{aisle_parsing_duration}s aisle_name: {
                    aisle.name}, product N: {index}/{len(products)}, url: {product.lang_desc.fr.links.links_self}')
            if all_attrs_are_none_or_zero(product):
                continue
            # access to product details and add them into the product "details" key
            # if len(cmdargs) == 3 and cmdargs[2] == "parse_product_details_only_if_no_available":
            if "parse_product_details_only_if_no_available" in cmdargs:
                product_with_details = scannerProductDetails.parse_product_details_only_if_no_available(
                    webdriverInstance, product)
            else:
                product_with_details = scannerProductDetails.parse_product_details(
                    webdriverInstance, product)

            if product_with_details:
                products_detailed.append(product_with_details)

        dump_json_then_write_it_to_file(file_uri.replace(
            ".json", "_detailed"), products_detailed)




else:
    print(
        "this was imported by:" + __name__)
