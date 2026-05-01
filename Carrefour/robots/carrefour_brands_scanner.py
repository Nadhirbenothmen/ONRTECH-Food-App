# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Jan 28, 2019

@author: marwen
"""
from src.utils.my_utils import dump_json_then_write_it_to_file, write_output_to_file
from src.utils.appium_utils import setup_logging, wait_el, wait_el_click, wait_els
from src.model.my_model import ProductAisle, ProductCategory
from src.countries.france.carrefour.robots import carrefour_static_ailes, webdriverInstance
from selenium.webdriver.common.by import By
from selenium import webdriver
import requests
import datetime
import json
import logging
import os
from pathlib import Path
import sys
import time
from typing import List

sys.path.append('src')

poll_frequency = 10
class ScannerProductBrands:
    def __init__(self):
        self.first_access = True

    def parse_brands(self, driver: webdriver, aisle_url: str) -> List[str] | None:
        try:
            print(f"***gonna parse product_url: {aisle_url}")
            brands_names: List[str] = []
            driver.get(aisle_url)
            if self.first_access:
                # should click on cookies panel just the first time the driver is launched
                wait_el_click(
                    driver=driver, by=By.ID, element="onetrust-reject-all-handler", timeout=2, poll_frequency=poll_frequency)
                self.first_access = False

            start_parsing_date = datetime.datetime.now()
            # check if product is available:
            brands_filter_el = wait_el(
                driver=driver, by=By.ID, element='data_facet_marque', timeout=20, poll_frequency=poll_frequency)
            print(f"brands_filter1 valid: {brands_filter_el is not None}")
            if brands_filter_el is None:
                return None
            wait_el_click(driver=brands_filter_el, by=By.CSS_SELECTOR, element='button', timeout=1, poll_frequency=poll_frequency)

            brands_els = wait_els(
                driver=brands_filter_el, by=By.CSS_SELECTOR, element='div > div > label > span', poll_frequency=poll_frequency)
            print(f"brands_els brands_els: {len(brands_els)}")
            for brand_el in brands_els:
                name = brand_el.get_attribute(
                    "innerHTML") if brand_el is not None else None
                print(f"name: {name}")
                brands_names.append(name.strip())
            end_parsing_date = datetime.datetime.now()
            parsing_duration = str(
                (end_parsing_date - start_parsing_date).seconds)
            print(f"parsing_duration: {parsing_duration}")
            return brands_names

        except requests.Timeout:
            logging.error("Timeout occurred for requested page: " + str(aisle_url))
            return None
        except:
            print("global except error:", sys.exc_info())
            if brands_names:
                return brands_names


if __name__ == "__main__":
    sections: List[ProductCategory] = []
    all_brands: List[ProductAisle] = []
    scannerProductBrands = ScannerProductBrands()
    for carrefour_section in carrefour_static_ailes.carrefour_categories_with_uris:
        print(f"Section url: {carrefour_section.url}, Section name: {carrefour_section.name}")
        aisles: List[ProductCategory] = carrefour_section.aisles
        aisles_v2: List[ProductCategory] = []
        for carrefour_aisle in [a for a in aisles if a.url]:
            print(f"Aisle name: {carrefour_aisle.name}, Aisle url: {carrefour_aisle.url}")

            brands: List[str] | None = scannerProductBrands.parse_brands(
                webdriverInstance, carrefour_aisle.url)

            if not brands:
                logging.error("no brands found for aisles:" + carrefour_aisle.url)
                continue
            all_brands.append(brands)
            carrefour_aisle.brands = brands
            aisles_v2.append(carrefour_aisle)
        carrefour_section.aisles = aisles_v2
        sections.append(carrefour_section)

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'brands'))
    file_path = os.path.join(path, "brands")
    dump_json_then_write_it_to_file(file_path, sections)

else:
    print(
        "this was imported by:" + __name__)
