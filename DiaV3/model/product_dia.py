import sys
import re
import json
import random
import datetime

from turtle import update
from typing import Dict, Optional , List , override

from src.countries.spain.DiaV3.model.product_content_dia import ProductContentDia

sys.path.append('src')
from pydantic.dataclasses import dataclass
from src.model.product import Category, CustomerReviews, Desc, Evolution, Freshness, Label, LangDesc, Market, Nutrition, Offer, Origin, Product
from src.countries.spain.DiaV3.model.product_content_dia import ProductContentDia 
from src.model.my_model import from_dict_to_objects
from src.utils.ean_country_checker import get_country_code_from_country_name_in_french_lang, get_country_code_from_ean
from src.utils.my_utils import find_all_substrings_in_text, is_any_string_in_string_list, is_substring_in_list
from src.countries.spain.DiaV3.model.product_content_dia import ProductContentDia


ALLERGENS = [
    "cacahuete", "apio", "crustáceos", "cangrejo", "gamba", "cigala", "langosta", "langostino",
    "avena", "trigo", "espelta", "kamut y sus cepas híbridas", "cebada", "centeno",
    "frutos de cáscara", "almendra", "avellana", "nuez", "nuez de brasil",
    "anacardo", "nuez de macadamia", "nuez de pecán", "nuez de queensland", "pistacho",
    "leche", "altramuces", "huevo", "pescado", "lactosa" , "gluten",
    "caracol de mar", "calamar", "caracol", "ostra", "mejillón", "almeja", "vieira", "pulpo",
    "mostaza", "sésamo", "soja", "sulfitos"
]



@dataclass
class LabelDia(Label):
    bio: Optional[bool] = None
    frozen: Optional[bool] = None
    halal: Optional[bool] = None
    fr_greengrocery: Optional[bool] = None
    gluten_free:Optional[bool] = None
    pregnant: Optional[bool] = None
    vegan: Optional[bool] = None
    vegetarian: Optional[bool] = None
    sugar: Optional[bool] = None
    lactose: Optional[bool] = None
    fat_free: Optional[bool] = None
    gmo_free: Optional[bool] = None
    sugar_added_free: Optional[bool] = None
    cooled: Optional[bool] = None
    preservative: Optional[bool] = None
    additive: Optional[bool] = None
    dye: Optional[bool] = None

    @classmethod
    def from_dict_to_object(cls, product: dict):
        title = (product.get("title") or "").lower()
        details = product.get("details") or {}

        # Champs texte à analyser (avec fallback vide)
        details_desc = (details.get("desc") or "").lower()
        details_ingredients = (details.get("ingredients") or "").lower()
        details_info_text = (details.get("product_info_text") or "").lower()
        details_other = (details.get("other_information") or "").lower()

        # Récupération directe
        details_bio = details.get("ecologico")
        details_frozen = details.get("congelado")
        details_halal = details.get("halal")
        details_fr_greengrocery = details.get("fr_greengrocery")
        details_gluten = details.get("gluten")
        details_pregnant = details.get("embarazadas")
        details_vegan = details.get("vegano")
        details_vegetarian = details.get("vegetariano")
        details_sugar = details.get("azucar")
        details_lactose = details.get("lactosa")
        details_fat = details.get("grase")
        details_gmo = details.get("ogm")
        details_preservative = details.get("conservante")
        details_additive = details.get("aditivo")
        details_dye = details.get("colorante")
        details_cooled = details.get("cooled")
        details_sugar_free = details.get("sin azucar")
        details_sugar_added_free = details.get("sugar_added_free")

        # Texte total combiné
        text_all = " ".join([title, details_desc, details_ingredients, details_info_text, details_other])

        # Analyse textuelle intelligente
        if details_lactose is None:
            if find_all_substrings_in_text(ProductContentDia.LACTOSE_ABSENCE, text_all):
                details_lactose = False
            elif find_all_substrings_in_text(ProductContentDia.LACTOSE_PRESENCE, text_all):
                details_lactose = True

        if details_vegan is None and find_all_substrings_in_text(ProductContentDia.VEGAN_PRESENCE, text_all):
            details_vegan = True

        if details_halal is None and find_all_substrings_in_text(ProductContentDia.HALAL_PRESENCE, text_all):
            details_halal = True

        if details_bio is None and find_all_substrings_in_text(ProductContentDia.BIO_PRESENCE, text_all):
            details_bio = True

        if details_fat is None and find_all_substrings_in_text(ProductContentDia.FAT_ABSENCE, text_all):
            details_fat = False

        if details_gmo is None and find_all_substrings_in_text(ProductContentDia.GMO_ABSENCE, text_all):
            details_gmo = False

        if details_additive is None and find_all_substrings_in_text(ProductContentDia.ADDITIVE_ABSENCE, text_all):
            details_additive = False

        if details_dye is None and find_all_substrings_in_text(ProductContentDia.DYE_ABSENCE, text_all):
            details_dye = False

        if details_preservative is None and find_all_substrings_in_text(ProductContentDia.PRESERVATIVE_ABSENCE, text_all):
            details_preservative = False

        if details_gluten is None:
            if find_all_substrings_in_text(ProductContentDia.GLUTEN_ABSENCE, text_all):
                details_gluten = True
            elif find_all_substrings_in_text(ProductContentDia.GLUTEN_PRESENCE, text_all):
                details_gluten = False

        if details_sugar_free is None and find_all_substrings_in_text(ProductContentDia.SUGAR_ABSENCE, text_all):
            details_sugar_free = True

        return cls(
            bio=details_bio,
            frozen=details_frozen,
            halal=details_halal,
            fr_greengrocery=details_fr_greengrocery,
            gluten_free=details_gluten,
            pregnant=details_pregnant,
            vegan=details_vegan,
            vegetarian=details_vegetarian,
            sugar_free=details_sugar_free,
            lactose=details_lactose,
            fat_free=details_fat,
            gmo_free=details_gmo,
            sugar_added_free=details_sugar_added_free,
            cooled=details_cooled,
            preservative=details_preservative,
            additive=details_additive,
            dye=details_dye
        )

class EvolutionDia(Evolution):
    @override
    @classmethod
    def is_medium_equal(cls, l: 'Evolution', r: 'Evolution') -> bool | None:
        '''
        Custom medium equality comparison based on the infos available on products list
        '''
        if not l or not r:
            print("is_medium_equal 1")
            return None
        if l.parsing_date == r.parsing_date:
            print("is_medium_equal 2")
            return True
        elif not cls.is_shallow_equal(l=l, r=r):
            print("is_medium_equal 3")
            return False  
        elif set(l.offers or []) == set(r.offers or []) and l.nutriscore == r.nutriscore and l.reviews == r.reviews:
            print("is_medium_equal 4")
            return True
        else:
            print("is_medium_equal 5")
            return False

    @override
    @classmethod
    def from_dict_to_object(cls, evol: dict):
        if isinstance(evol, dict):
            evol_date = evol.get("date")
            evol_format = evol.get("format")
            evol_availabilty = evol.get("availabilty")
            evol_pricePerUnit = evol.get("pricePerUnit")
            evol_price = evol.get("price")
            evol_nutriscore = evol.get("nutriscore")
            evol_certification = evol.get("certification")

            evol_nutrition = evol.get("nutrition")  # dict
            Nutrition.convert_dict_to_nutrition_Object(nutritions=evol_nutrition)
            evol_ingredients = evol.get("ingredients")  # dict
            evol_allergens = evol.get("allergens")  # dict
            evol_customerReviews = evol.get("customerReviews")  # dict
            customerReviews = CustomerReviews.from_dict_to_object(evol_customerReviews)

            on_discount = evol.get("on_discount", False)

            evol = EvolutionDia(parsing_date=evol_date, format=evol_format, availability=evol_availabilty, price_per_unit=evol_pricePerUnit,
                                      price=evol_price, nutriscore=evol_nutriscore, certification=evol_certification, nutrition=evol_nutrition,
                                      ingredients=evol_ingredients, allergens=evol_allergens, reviews=customerReviews,
                                      on_discount=on_discount)
            return evol
        return None
@dataclass
class MarketDia(Market):
    name: str = "DIA"
    country: str = "ES"
    address: str = "Madrid"
    

    @classmethod
    def from_dict_to_object(cls, product: dict):
        return cls(
            name=product.get("market") or "DIA",
            country=product.get("market_country") or "ES",
            address=product.get("market_address") or "Madrid"
        )

@dataclass
class ProductDia(Product):
    @classmethod
    def from_dict_to_object(cls, product: Dict) -> 'ProductDia':
        ean = product.get("ean")
        business_type = product.get("business_type")
        origin = Origin(
            ean=get_country_code_from_ean(ean),
            explicit=get_country_code_from_country_name_in_french_lang(product.get("origin")),
            partial=product.get("partial_origin")
        )

        unit_of_mesure = product.get("unit_of_mesure")
        created_at = product.get("created_at")
        updated_at = product.get("updated_at")

        market_data = product.get("market") or {}
        market = MarketDia(
        name=market_data.get("name"),
        country=market_data.get("country"),
        address=market_data.get("address")
)
        categories = product.get("categories")  # list
        categories: list[Category] = from_dict_to_objects(Category, categories)

        lang_desc = product.get("lang_desc")  # dict
        lang_desc = LangDesc.from_dict_to_object(lang_desc=lang_desc)

        label = LabelDia.from_dict_to_object(product=product)

        evolutions = product.get("evolution")  # list
        evolutions = from_dict_to_objects(Evolution, evolutions)
        
        product = ProductDia(ean=ean, origin=origin, unit_of_mesure=unit_of_mesure,
                                   created_at=created_at, updated_at=updated_at, market=market, categories=categories,
                                   lang_desc=lang_desc, evolutions=evolutions, label=label)

        return product

