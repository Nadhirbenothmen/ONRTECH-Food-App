import sys
import re
import json
import random
import datetime

from turtle import update
from typing import Dict, Optional , List , override

sys.path.append('src')
from pydantic.dataclasses import dataclass
from src.model.product import Category, CustomerReviews, Desc, Evolution, Freshness, Label, LangDesc, Market, Nutrition, Offer, Origin, Product
from src.countries.spain.EroskiV3.model.product_content_eroski import ProductContentEroski 
from src.model.my_model import from_dict_to_objects
from src.utils.ean_country_checker import get_country_code_from_country_name_in_french_lang, get_country_code_from_ean
from src.utils.my_utils import find_all_substrings_in_text, is_any_string_in_string_list, is_substring_in_list


ALLERGENS = [
    "Cacahuete", "Apio", "Crustáceos", "Cangrejo", "Gamba", "Cigala", "Langosta", "Langostino",
    "Avena", "Trigo", "Espelta", "Kamut y sus cepas híbridas", "Cebada", "Centeno",
    "Frutos de cáscara", "Almendra", "Avellana", "Nuez", "Nuez de Brasil",
    "Anacardo", "Nuez de macadamia", "Nuez de pecán", "Nuez de Queensland", "Pistacho",
    "Leche", "Altramuces", "Huevo", "Pescado", "lactosa" , "gluten",
    "Caracol de mar (Búzio)", "Calamar", "Caracol", "Ostra", "Mejillón", "Almeja", "Vieira", "Pulpo",
    "Mostaza", "Sésamo", "Soja", "Sulfitos"
]


@dataclass
class LabelEroski(Label):
    bio: Optional[bool] = None
    frozen: Optional[bool] = None
    halal: Optional[bool] = None
    es_greengrocery: Optional[bool] = None
    gluten_free:Optional[bool] = None
    pregnant: Optional[bool] = None
    vegan: Optional[bool] = None
    vegetarian: Optional[bool] = None
    sugar_free: Optional[bool] = None
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
        title = product.get("title")
        details = product.get("details") or {}

        # Récupération directe
        details_bio = details.get("ecologico")
        details_frozen = details.get("congelado")
        details_halal = details.get("halal")
        details_es_greengrocery = details.get("es_greengrocery")
        details_gluten = details.get("gluten")
        details_pregnant = details.get("embarazadas")
        details_vegan = details.get("vegano")
        details_vegetarian = details.get("vegetariano")
        details_sugar_free = details.get("sin azucar")
        details_lactose = details.get("lactasa")
        details_fat = details.get("grase")
        details_gmo = details.get("ogm")
        details_preservative = details.get("conservante")
        details_additive = details.get("aditivo")
        details_dye = details.get("colorante")
        details_cooled = details.get("cooled")
        details_sugar_added_free = details.get("sugar_added_free")

        # Champs texte à analyser
        details_desc = details.get("desc", "")
        details_ingredients = details.get("ingredients", "")
        

        # Analyse textuelle sécurisée
        # Lactose
        if details_lactose is None and find_all_substrings_in_text(ProductContentEroski.LACTOSE_PRESENCE, details_desc, title, details_ingredients):
            details_lactose = True
        elif details_lactose is None and find_all_substrings_in_text(ProductContentEroski.LACTOSE_ABSENCE, details_desc, title, details_ingredients):
            details_lactose = False
        

        # Vegan
        if details_vegan is None and find_all_substrings_in_text(ProductContentEroski.VEGAN_PRESENCE, details_desc, title, details_ingredients):
            details_vegan = True

        # Halal
        if details_halal is None and find_all_substrings_in_text(ProductContentEroski.HALAL_PRESENCE, details_desc, title, details_ingredients):
            details_halal = True

        # Bio
        if details_bio is None and find_all_substrings_in_text(ProductContentEroski.BIO_PRESENCE, details_desc, title, details_ingredients):
            details_bio = True

        # Fat
        if details_fat is None and find_all_substrings_in_text(ProductContentEroski.FAT_ABSENCE, details_desc, title, details_ingredients):
            details_fat = False

        # GMO
        if details_gmo is None and find_all_substrings_in_text(ProductContentEroski.GMO_ABSENCE, details_desc, title, details_ingredients):
            details_gmo = False

        # Additives
        if details_additive is None and find_all_substrings_in_text(ProductContentEroski.ADDITIVE_ABSENCE, details_desc, title, details_ingredients):
            details_additive = False

        # Dyes
        if details_dye is None and find_all_substrings_in_text(ProductContentEroski.DYE_ABSENCE, details_desc, title, details_ingredients):
            details_dye = False

        # Preservatives
        if details_preservative is None and find_all_substrings_in_text(ProductContentEroski.PRESERVATIVE_ABSENCE, details_desc, title, details_ingredients):
            details_preservative = False

        # Gluten (absence avant présence)
        if details_gluten is None and find_all_substrings_in_text(ProductContentEroski.GLUTEN_ABSENCE, details_desc, title, details_ingredients):
            details_gluten = True
        elif details_gluten is None and find_all_substrings_in_text(ProductContentEroski.GLUTEN_PRESENCE, details_desc, title, details_ingredients):
            details_gluten = False

        # Sugar
        if details_sugar_free is None and find_all_substrings_in_text(ProductContentEroski.SUGAR_ABSENCE, details_desc, title, details_ingredients):
            details_sugar_free = False


        return cls(
            bio=details_bio,
            frozen=details_frozen,
            halal=details_halal,
            es_greengrocery=details_es_greengrocery,
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
            dye=details_dye,
        )

class EvolutionEroski(Evolution):
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

            evol = EvolutionEroski(parsing_date=evol_date, format=evol_format, availability=evol_availabilty, price_per_unit=evol_pricePerUnit,
                                      price=evol_price, nutriscore=evol_nutriscore, certification=evol_certification, nutrition=evol_nutrition,
                                      ingredients=evol_ingredients, allergens=evol_allergens, reviews=customerReviews,
                                      on_discount=on_discount)
            return evol
        return None

@dataclass
class MarketEroski(Market):
    name: str = "EROSKI"
    country: str = "ES"
    address: str = "Biscaye"

    @classmethod
    def from_dict_to_object(cls, product: dict):
        return cls(
            name=product.get("market") or "ALCAMPO",
            country=product.get("market_country") or "ES" ,
            address=product.get("market_address") or "Biscaye" 
        )

@dataclass
class ProductEroski(Product):
    @classmethod
    def from_dict_to_object(cls, product: Dict) -> 'ProductEroski':
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
        market = MarketEroski(
        name=market_data.get("name"),
        country=market_data.get("country"),
        address=market_data.get("address")
)
        categories = product.get("categories")  # list
        categories: list[Category] = from_dict_to_objects(Category, categories)

        lang_desc = product.get("lang_desc")  # dict
        lang_desc = LangDesc.from_dict_to_object(lang_desc=lang_desc)

        label = LabelEroski.from_dict_to_object(product=product)

        evolutions = product.get("evolution")  # list
        evolutions = from_dict_to_objects(Evolution, evolutions)
        
        product = ProductEroski(ean=ean, origin=origin, unit_of_mesure=unit_of_mesure,
                                   created_at=created_at, updated_at=updated_at, market=market, categories=categories,
                                   lang_desc=lang_desc, evolutions=evolutions, label=label)

        return product

