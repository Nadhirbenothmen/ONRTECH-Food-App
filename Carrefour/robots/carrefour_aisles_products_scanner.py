# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Jan 28, 2019

@author: marwen
"""
import json
import logging
import os
import re
import sys
import time
from typing import List, Optional

import dacite
import requests
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.countries.france.carrefour.model.product_carrefour import EvolutionCarrefour, MarketCarrefour, OfferCarrefour, ProductCarrefour
from src.countries.france.carrefour.model.product_content_carrefour import ProductContentCarrefour
from src.countries.france.carrefour.robots import carrefour_static_ailes, webdriverInstance
from src.model.my_model import ProductBrand
from src.model.product import (
    CustomerReviews,
    Desc,
    Evolution,
    LangDesc,
    Links,
    Offer,
    Product,
    get_latest_parsed_products,
    get_product_by_ean,
)
from src.model.product_content import convert_format_product
from src.model.static_category_aisle import StaticAisle
from src.utils.appium_utils import (
    get_attribute_from_element,
    get_text_from_element,
    setup_logging,
    wait_el,
    wait_el_click,
    wait_el_text,
    wait_els,
)
from src.utils.my_utils import convert_to_float, dump_json_then_write_it_to_file, match_all_numbers, write_output_to_file

sys.path.append('src')

# sys.path.append('C:\Users\ASUS\Desktop\StagePFE\LaNoria_backoffice')
sys.path.append('./')

"""
sys.path.append('./')
sys.path.insert(1, 'src/model/')
sys.path.insert(1, 'src/model.my_model')
sys.path.insert(
    1, '/Users/marwenrhayem/Projects/mrh/LaNoria_backoffice2/src/model/')
sys.path.insert(
    1, '/Users/marwenrhayem/Projects/mrh/LaNoria_backoffice2/src/model')
sys.path.append('../..')
"""


class CarrefourAislesProductsScanner:
    def __init__(self):
        self.total_products_number = 0
        self.first_access = True
        self.brands = [ProductBrand]

    def parse_products(self, driver: webdriver, aisle: StaticAisle, parse_only_ean_title_url_price: bool, parse_only_first_x_products=Optional[int], parse_only_from_index=Optional[int], latest_parsed_products: List[ProductCarrefour] = []) -> List[Product]:
        aisle_url = aisle.url
        try:
            print(f"aisle_url: {aisle_url}")
            driver.get(aisle_url)
            products: List[Product] = []
            nb_parsed_results = 0
            consulted_products_total = 0
            if self.first_access:
                # should click on cookies panel just the first time the driver is launched
                wait_el_click(driver, By.ID, "onetrust-reject-all-handler", 5)
                self.brands = self.parse_brands(driver)
                self.first_access = False
            # get promotion count for promotion page:
            promotion_count = wait_el_text(
                driver, By.CSS_SELECTOR, 'div.search-results-count.search-results-count--promotion p')
            print(f'promotion_count: {promotion_count}')
            if not promotion_count:
                nb_result = wait_el_text(
                    driver, By.XPATH, '//*[@id="data-voir-plus"]/p')
                if not nb_result:
                    print(f"the aisle may no longer exist? : {
                          nb_result is None}")
                    return []
                consulted_products = [int(s)
                                      for s in nb_result.split() if s.isdigit()]
                consulted_products_total = consulted_products[1] if len(
                    consulted_products) > 0 else 0

                products_els: List[WebElement] = []
                # products_els = driver.find_elements(By.XPATH, '//*[@id="data-plp_produits"]/li/article')
                consulted_products_total = parse_only_first_x_products or consulted_products_total
                while nb_parsed_results < consulted_products_total and (nb_parsed_results) < 2200:
                    products_els = wait_els(
                        driver, By.XPATH, '//*[@id="data-plp_produits"]/li/article', 220)
                    nb_parsed_results = len(
                        products_els) if products_els else nb_parsed_results
                    time.sleep(1.5)
                    button_voirplus_still_exist = wait_el(
                        driver, By.XPATH, '//*[@id="data-voir-plus"]/div[2]/button', 5)
                    print(f"new nb_result: {nb_parsed_results}, consulted_products_total:{
                          consulted_products_total}, button_voirplus_still_exist: {button_voirplus_still_exist is not None}")

                    if button_voirplus_still_exist:
                        wait_el_click(driver, By.XPATH,
                                      '//*[@id="data-voir-plus"]/div[2]/button', 5)
                    else:
                        print(f"total nb_result: {nb_parsed_results}, consulted_products_total: {
                              consulted_products_total}")
                        break
            else:
                promotion_count = promotion_count.replace(" promotions", "")
                products_els2 = wait_els(
                    driver, By.CSS_SELECTOR, '#data-plp_produits article')
                print(f"products_els2 count: {
                      len(products_els2) if products_els2 else None} for total:{promotion_count}")
                # and len(products_els2) < 2500):
                while int(promotion_count) > len(products_els2):
                    # Locate the specific div using a selector (in this case, by ID)
                    # Replace with the actual ID of the div
                    footer_element = wait_el(
                        driver, By.CSS_SELECTOR, '#data-voir-plus')
                    # Scroll the page until the div is in view
                    driver.execute_script(
                        "arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", footer_element)
                    time.sleep(2)
                    products_els2 = wait_els(
                        driver, By.CSS_SELECTOR, '#data-plp_produits article')
                    print(f"while products_els2 count: {
                          len(products_els2) if products_els2 else None} for total:{int(promotion_count)}")

            products_els2 = wait_els(
                driver, By.CSS_SELECTOR, '#data-plp_produits article')
            nb_parsed_products = 0
            for index in range(len(products_els2 or [])):
                nb_parsed_products += 1
                if parse_only_from_index and parse_only_from_index > index:
                    print(f"parse_only_from_index: {
                          parse_only_from_index}, index: {index}")
                    continue
                product_el = products_els2[index]
                product_id = get_attribute_from_element(
                    product_el, 'id', "product_id")
                if isinstance(product_id, StaleElementReferenceException):
                    products_els2 = wait_els(
                        driver, By.CSS_SELECTOR, '#data-plp_produits article')
                    product_el = products_els2[index]
                    product_id = get_attribute_from_element(
                        product_el, 'id', "product_id")
                price_per_packaging_part1 = wait_el_text(
                    product_el, By.CSS_SELECTOR, 'p.product-price__content.c-text.c-text--size-m.c-text--style-subtitle.c-text--bold')
                # product-price__content c-text c-text--size-s c-text--style-p c-text--bold c-text--spacing-default
                price_per_packaging_part2 = wait_el_text(
                    product_el, By.CSS_SELECTOR, 'p.product-price__content.c-text.c-text--size-s.c-text--style-p.c-text--bold')
                # price = price.replace(',', '.') if price else None

                price_per_packaging_str = f"{
                    price_per_packaging_part1}" + f"{price_per_packaging_part2}"

                price_per_packaging = convert_to_float(price_per_packaging_str.replace(
                    ',', '.')) if price_per_packaging_str else None
                print(f"price_per_packaging: {
                    price_per_packaging}, price_per_packaging_part1: {price_per_packaging_part1}, price_per_packaging_part2: {price_per_packaging_part2}, price_per_packaging_str: {price_per_packaging_str}")

                price_per_packaging = convert_to_float(
                    price_per_packaging) if price_per_packaging else None
                # ds-product-card__perunitlabel pl-text pl-text--size-m pl-text--style-caption
                price_per_unit = wait_el_text(
                    product_el, By.CSS_SELECTOR, 'p.ds-product-card__perunitlabel.pl-text.pl-text--size-m.pl-text--style-caption')
                # in case of StaleElementReferenceException,
                # we should save the current_index,
                # get the root drive, and execute again products_els2 = wait_els(driver, By.CSS_SELECTOR, '#data-plp_produits article')
                # current_index[]
                # check if product_id exists in latest parsed products:
                # if yes then return its product
                product_already_parsed = get_product_by_ean(
                    product_id, latest_parsed_products)
                print(f"product_id: {product_id}, product_already_parsed: {
                      product_already_parsed is not None}, {"skip it!" if product_already_parsed else "parse it!"}")
                if product_already_parsed:
                    try:
                        product_already_parsed = dacite.from_dict(
                            data_class=Product, data=product_already_parsed, config=dacite.Config(strict=True))
                    except dacite.UnexpectedDataError as e:
                        print(f"Unexpected data found: {e}")
                        return product_already_parsed
                        # raise  # Re-raise the error after logging or inspecting the data
                    # create new evolutions containing only prices:
                    latest_evolution = Evolution.latest_evolution(
                        product_already_parsed.evolutions)
                    print(f"latest_evolution: {latest_evolution}, price_per_packaging: {
                          price_per_packaging}")
                    # Compare the current product details with the most recent one.
                    if latest_evolution and latest_evolution.price_per_unit == price_per_unit:
                        # If the details haven’t changed, insert only a timestamp
                        evolution = Evolution()
                        product_already_parsed.evolutions.append(evolution)
                        products.append(product_already_parsed)
                        continue
                    # else:
                    #     # If the details have changed or evolution list is empty, insert a new evolution
                    #     evolution = Evolution(price_per_packaging=price_per_packaging, price_per_unit=price_per_unit)
                    #     product_already_parsed.evolutions = (product_already_parsed.evolutions or []).append(evolution)
                    #     products.append(product_already_parsed)
                    #     continue
                product_card_el = wait_el(
                    product_el, By.CLASS_NAME, 'product-card-image')
                product_url_el = wait_el(
                    product_el, By.CSS_SELECTOR, 'a')
                product_url = get_attribute_from_element(
                    product_url_el, "href", 'product_url') if product_card_el else None
                product_title = wait_el_text(
                    product_url_el, By.CSS_SELECTOR, 'h3') if product_card_el else None

                if not product_id or "sponsor" in product_id or not product_url or not product_title:
                    print(f"skipt this product:\nproduct_id: {product_id}, product_url: {
                          product_url}, product_title: {product_title}")
                    continue
                print(f"price_per_packaging:{
                      price_per_packaging}, price_per_unit: {price_per_unit}")
                print(f"product_id: {product_id}, product_url: {product_url}, parsing product: {
                      nb_parsed_products}/{nb_parsed_results}, aisle: {aisle.name}")
                if parse_only_ean_title_url_price:
                    link = Links(reviews=None, links_self=product_url)
                    lang_desc = LangDesc(
                        fr=Desc(title=product_title, links=link))
                    evolution = Evolution(
                        price_per_packaging=price_per_packaging, price_per_unit=price_per_unit)
                    product = ProductCarrefour(
                        ean=product_id, lang_desc=lang_desc)
                    product.evolutions = [evolution]
                    products.append(product)
                    time.sleep(0.25)
                    continue

                # packaging format:
                format_layout__infos_el = wait_el(
                    product_el, By.CSS_SELECTOR, 'div.main-layout__infos > div')
                packaging_format2 = get_text_from_element(
                    format_layout__infos_el)
                packaging_format = get_attribute_from_element(
                    format_layout__infos_el, 'aria-label')
                (base_weigth_unit, poids_total) = convert_format_product(
                    packaging_format)
                (base_weigth_unit2, poids_total2) = convert_format_product(
                    packaging_format2)
                mesure_unit_for_packaging = base_weigth_unit or base_weigth_unit2
                weight_per_packaging = poids_total or poids_total2
                if not packaging_format:
                    packaging_format = packaging_format2
                    packaging_format2 = None

                # offers
                offers = self.get_offers(product_el)
                print("step 3")

                freshness_el_text = wait_el_text(
                    product_el, By.CSS_SELECTOR, ".freshness-badge", 0.5)
                freshness_days = None if not freshness_el_text else ProductContentCarrefour.get_freshness_days(
                    freshness_el_text)
                freshness_days = int(
                    freshness_days) if freshness_days else None

                nutriscore_el = wait_el(
                    product_el, By.CSS_SELECTOR, ".product-badge--flag-nutriscore", 0.5)
                nutriscore_val = None if not nutriscore_el else get_attribute_from_element(
                    nutriscore_el, "nutriscore", 'nutriscore_val')
                print(f"product_el is valid1: {
                      product_el is not None}, nutriscore_val: {nutriscore_val}")
                product_img = self.get_image(product_el)
                print(f"product_img: {product_img}")
                product_title_packaging = wait_el_text(
                    product_el, By.XPATH, '//*[@class="pl-text pl-text--size-m pl-text--style-caption"]')

                print(f"product_title_packaging: {product_title_packaging}, price: {
                      price_per_packaging}, price_per_unit: {price_per_unit}")

                # reviews_section
                # reviews_number = self.get_reviews_infos_V2(product_el)
                reviews_url, reviews_number, reviews_average = self.get_reviews_infos(
                    product_el)
                reviews_average = convert_to_float(
                    reviews_average) if reviews_average else None

                reviews = CustomerReviews(
                    count=int(reviews_number) or None, average=reviews_average or None) if reviews_number else None
                link = Links(reviews=reviews_url, links_self=product_url)
                lang_desc = LangDesc(
                    fr=Desc(title=product_title, images=[product_img], links=link))

                product_brand = ProductContentCarrefour.get_brand_from_title(
                    product_title)

                mesure_unit_for_price_per_unit, matter, product_pricing_unit = ProductContentCarrefour.get_packaging_info(
                    price_per_unit)
                new_evolution = EvolutionCarrefour(nutriscore=nutriscore_val, availability=True,
                                                   price_per_packaging=price_per_packaging, price_per_unit=product_pricing_unit,
                                                   reviews=reviews, offers=offers, format=packaging_format, format2=packaging_format2,
                                                   weight_per_packaging=weight_per_packaging)
                all_evolutions = Evolution.merge_evolutions(
                    new_evolution=new_evolution, old_evolutions=product_already_parsed.evolutions if product_already_parsed else None, equality_func=EvolutionCarrefour.is_medium_equal)

                product = Product(ean=product_id, brand=product_brand, categories=None,
                                  origin=None, mesure_unit_for_packaging=mesure_unit_for_packaging, mesure_unit_for_price_per_unit=mesure_unit_for_price_per_unit, matter=matter,
                                  freshness=freshness_days, lang_desc=lang_desc, market=MarketCarrefour(),
                                  evolutions=all_evolutions, label=None)
                products.append(product)

                if parse_only_first_x_products and len(products) > parse_only_first_x_products:
                    print(f"parse_only_first_x_products: {
                          parse_only_first_x_products} reached")
                    break
            return products
        except requests.Timeout:
            print(f"Timeout occurred for requested page: {
                  aisle_url} for aisle: {aisle.name}")
            return products
        except:
            print(f"global except error for aisle: {
                  aisle.name}, error: {sys.exc_info()}")
            return products

    def get_image(self, product_el) -> str | None:
        product_img_el = wait_el(
            product_el, By.CSS_SELECTOR, 'div.product-card-image img')
        product_img = product_img_el.get_attribute(
            "src") if product_img_el else ""
        product_img2 = product_img_el.get_attribute(
            "data-src") if product_img_el else ""
        product_img = product_img if product_img else product_img2
        return product_img

    def get_offers(self, product_el) -> list[Offer] | None:
        offers_els = wait_els(product_el, By.CSS_SELECTOR,
                              '.c-text.c-text--size-s.c-text--style-caption.c-text--bold.promotion-label-refonte__text.promotion-label-refonte__label') or []
        offers_text = [get_text_from_element(
            offer_el) for offer_el in offers_els]
        offer_desc = ', '.join(offers_text) or None
        # add regex to extract the requiredProductQuantity:
        offers = [OfferCarrefour.extractInfo(
            offer_desc)] if offer_desc else None
        return offers

    def get_reviews_infos(self, product_el) -> tuple[str | None, str | None, int]:
        reviews_section_el = wait_el(
            product_el, By.CSS_SELECTOR, 'div.main-layout__rating a')
        if not reviews_section_el:
            return (None, None, None)
        rating_text = get_attribute_from_element(
            reviews_section_el, 'aria-label', "aria-label")
        reviews_url = get_attribute_from_element(
            reviews_section_el, 'href', "href")
        # text = "1 avis pour une note moyenne de 4 sur 5"
        # Use regex to find all numbers in the text
        matches = match_all_numbers(rating_text)
        reviews_number = matches[0] if len(matches) >= 3 else None
        reviews_average = matches[1] if len(matches) >= 3 else None
        print(f"rating_text: {rating_text}, get_reviews_infos: {
              matches}")  # Output: ['1', '4', '5']
        return reviews_url, reviews_number, reviews_average

    def parse_brands(self, driver) -> List[ProductBrand]:
        wait_el_click(driver, By.CSS_SELECTOR, '#data_facet_marque > button')

        brand_els = wait_els(
            driver, By.CSS_SELECTOR, '#data_facet_marque span.filters-checkbox__option__label')

        brands = []
        if not brand_els:
            return brands
        for brand_el in brand_els:
            brand_name = brand_el.get_attribute("innerHTML")
            print(f"brand_name: {brand_name}")
            brand = ProductBrand("0", brand_name)
            # brand = {"name": brand_name}
            brands.append(brand)
        return brands


if __name__ == "__main__":
    print("my main")
    # Get the arguments list
    cmdargs = sys.argv

    # Print it
    print(f"The total numbers of args passed to the script: {
          len(cmdargs)}, Args list: {cmdargs}")
    # first arg section, second arg aisle
    if len(cmdargs) > 1:  # in (1, 2):
        carrefour = CarrefourAislesProductsScanner()
        aisles: List[StaticAisle] = carrefour_static_ailes.get_static_aisles_from_user_cmdargs(
            cmdargs=cmdargs)
        print(f"aisles: {len(aisles)}")
        if len(aisles) == 0:
            print("empty aisles")
            sys.exit()
        for aisle in (a for a in aisles if a.url):
            latest_parsed_products: List[ProductCarrefour] = []
            if "get_latest_parsed_products" in cmdargs:
                latest_parsed_products = get_latest_parsed_products(
                    aisle=aisle)
            print(f"aisle.name: {aisle.name}, aisle.url: {
                  aisle.url}, latest_parsed_products count: {len(latest_parsed_products)}")

            aisle_uri = aisle.original_file_uri.replace(
                ".json", "")
            parse_only_ean_title_url_price = False
            parse_only_first_x_products = None
            if "parse_only_ean_title_url_price" in cmdargs:
                parse_only_ean_title_url_price = True
            if "parse_only_first_x_products" in cmdargs:
                index = cmdargs.index("parse_only_first_x_products")
                parse_only_first_x_products = int(cmdargs[index + 1])

            parse_only_from_index = None
            new_products = carrefour.parse_products(
                webdriverInstance, aisle, parse_only_ean_title_url_price, parse_only_first_x_products, parse_only_from_index, latest_parsed_products)

            dump_json_then_write_it_to_file(aisle_uri, new_products)
    else:
        print("wrong args number")
        sys.exit()
