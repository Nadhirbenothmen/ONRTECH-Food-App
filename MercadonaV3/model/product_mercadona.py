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
from src.countries.spain.MercadonaV3.model.product_content_mercadona import ProductContentMercadona 
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
class LabelMercadona(Label):
    bio: Optional[bool] = None
    frozen: Optional[bool] = None
    halal: Optional[bool] = None
    fr_greengrocery: Optional[bool] = None
    gluten_free: Optional[bool] = None
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
        title = product.get("title", "").lower()

        # Récupération directe (si un jour tu ajoutes details réels)
        details = product.get("details") or {}
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
        details_fat = details.get("grasa")  # corrigé typo: "grase" → "grasa"
        details_gmo = details.get("ogm")
        details_preservative = details.get("conservante")
        details_additive = details.get("aditivo")
        details_dye = details.get("colorante")
        details_cooled = details.get("cooled")
        details_sugar_added_free = details.get("sugar_added_free")

        # Analyse uniquement sur le `title`
        def match(patterns):
            return find_all_substrings_in_text(patterns, title)

        if details_lactose is None:
            if match(ProductContentMercadona.LACTOSE_ABSENCE):
                details_lactose = False
            elif match(ProductContentMercadona.LACTOSE_PRESENCE):
                details_lactose = True

        if details_vegan is None and match(ProductContentMercadona.VEGAN_PRESENCE):
            details_vegan = True

        if details_halal is None and match(ProductContentMercadona.HALAL_PRESENCE):
            details_halal = True

        if details_bio is None and match(ProductContentMercadona.BIO_PRESENCE):
            details_bio = True

        if details_fat is None and match(ProductContentMercadona.FAT_ABSENCE):
            details_fat = True

        if details_gmo is None and match(ProductContentMercadona.GMO_ABSENCE):
            details_gmo = True

        if details_additive is None and match(ProductContentMercadona.ADDITIVE_ABSENCE):
            details_additive = False

        if details_dye is None and match(ProductContentMercadona.DYE_ABSENCE):
            details_dye = False

        if details_preservative is None and match(ProductContentMercadona.PRESERVATIVE_ABSENCE):
            details_preservative = False

        if details_gluten is None:
            if match(ProductContentMercadona.GLUTEN_ABSENCE):
                details_gluten = True
            elif match(ProductContentMercadona.GLUTEN_PRESENCE):
                details_gluten = False

        if details_sugar is None and match(ProductContentMercadona.SUGAR_ABSENCE):
            details_sugar = True

        return cls(
            bio=details_bio,
            frozen=details_frozen,
            halal=details_halal,
            fr_greengrocery=details_fr_greengrocery,
            gluten_free=details_gluten,
            pregnant=details_pregnant,
            vegan=details_vegan,
            vegetarian=details_vegetarian,
            sugar_free=details_sugar,
            lactose=details_lactose,
            fat_free=details_fat,
            gmo_free=details_gmo,
            sugar_added_free=details_sugar_added_free,
            cooled=details_cooled,
            preservative=details_preservative,
            additive=details_additive,
            dye=details_dye
        )

class EvolutionMercadona(Evolution):
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

            evol = EvolutionMercadona(parsing_date=evol_date, format=evol_format, availability=evol_availabilty, price_per_unit=evol_pricePerUnit,
                                      price=evol_price, nutriscore=evol_nutriscore, certification=evol_certification, nutrition=evol_nutrition,
                                      ingredients=evol_ingredients, allergens=evol_allergens, reviews=customerReviews,
                                      on_discount=on_discount)
            return evol
        return None
    
@dataclass
class MarketMercadona(Market):
    name: str = "MERCADONA"
    country: str = "ES"
    address: str = "Valence"

    @classmethod
    def from_dict_to_object(cls, product: dict):
        return cls(
            name=product.get("market") or "MERCADONA",
            country=product.get("market_country") or "ES",
            address=product.get("market_address") or "Valence"
        )

@dataclass
class ProductMercadona(Product):
    @classmethod
    def from_dict_to_object(cls, product: Dict) -> 'ProductMercadona':
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
        market = MarketMercadona(
        name=market_data.get("name"),
        country=market_data.get("country"),
        address=market_data.get("address")
)
        categories = product.get("categories")  # list
        categories: list[Category] = from_dict_to_objects(Category, categories)

        lang_desc = product.get("lang_desc")  # dict
        lang_desc = LangDesc.from_dict_to_object(lang_desc=lang_desc)

        label = LabelMercadona.from_dict_to_object(product=product)

        evolutions = product.get("evolution")  # list
        evolutions = from_dict_to_objects(Evolution, evolutions)
        
        product = ProductMercadona(ean=ean, origin=origin, unit_of_mesure=unit_of_mesure,
                                   created_at=created_at, updated_at=updated_at, market=market, categories=categories,
                                   lang_desc=lang_desc, evolutions=evolutions, label=label)

        return product

