import datetime
import json
import random
import re
import sys
from typing import List, Optional, override

#from attr import dataclass
from pydantic.dataclasses import dataclass
from src.model.product import Category, CustomerReviews, Desc, Evolution, Freshness, Label, LangDesc, Market, Offer, Origin, Product
from src.countries.france.carrefour.model.product_content_carrefour import Nutrition, ProductContentCarrefour
from src.model.my_model import from_dict_to_objects
from src.utils.ean_country_checker import get_country_code_from_country_name_in_french_lang, get_country_code_from_ean
from src.utils.my_utils import find_all_substrings_in_text, is_any_string_in_string_list, is_substring_in_list

sys.path.append('src')


ALLERGENS = ["Arachide", "Céleri", "Crustacés", "Crabe", "Crevette", "Écrevisse", "Homard", "Langoustine", "Avoine", "Blé", "Épeautre", "Kamut et leurs souches hybridées", "Orge", "Seigle", "Fruits à coque", "Amande", "Noisette", "Noix", "Noix du Brésil",
             "Noix de cajou", "Noix de macadamia", "Noix de pécan", "Noix du Queensland", "Pistache", "Lait", "Lupin", "Œuf", "Poisson", "Boulot", "Calamar", "Escargot", "Huitre", "Moule", "Palourde", "Pétoncle", "Pieuvre", "Moutarde", "Sésame", "Soja", "Sulfites"]


@dataclass
class LabelCarrefour(Label):
    @classmethod
    def from_dict_to_object(cls, product: dict):
        title = product.get("title")
        details = product.get("details")  # dict
        details_halal: Optional[str] = None
        details_gmo: Optional[str] = None
        details_preservative: Optional[str] = None
        details_additive: Optional[str] = None
        details_gluten: Optional[str] = None
        details_vegan: Optional[str] = None
        details_lactose: Optional[str] = None
        if details is not None:
            details_bio = details.get("bio")
            details_vegetarian = details.get("vegetarian")
            details_halal = details.get("halal")
            details_vegan = details.get(("vegan"))
            details_lactose = details.get(("lactose"))
            details_dye = details.get("dye")
            details_gmo = details.get("gmo")
            details_fat = details.get("fat")
            details_preservative = details.get("preservative")
            details_additive = details.get("additive")
            details_sugar = details.get("sugar")
            details_frozen = details.get("frozen")
            details_gluten = details.get("gluten")
            details_fr_greengrocery = details.get("fr_greengrocery")
            details_pregnant = details.get("pregnant")
            details_fr_greengrocery = details.get("fr_greengrocery")
            details_desc = details.get("desc")

            if details_lactose is None and find_all_substrings_in_text(ProductContentCarrefour.LACTOSE_PRESENCE, details_desc) is not None:
                details_lactose = True
            elif details_lactose is None and find_all_substrings_in_text(ProductContentCarrefour.LACTOSE_ABSENCE, details_desc) is not None:
                details_lactose = False

            if details_vegan is None and find_all_substrings_in_text(ProductContentCarrefour.VEGAN_PRESENCE, details_desc) is not None:
                details_vegan = True

            if details_halal is None and find_all_substrings_in_text(ProductContentCarrefour.HALAL_PRESENCE, title) is not None:
                details_halal = True

            if details_bio is None and find_all_substrings_in_text(ProductContentCarrefour.BIO_PRESENCE, title) is not None:
                details_bio = True

            if details_fat is None and find_all_substrings_in_text(ProductContentCarrefour.FAT_ABSENCE, details_desc) is not None:
                details_fat = False

            if details_gmo is None and find_all_substrings_in_text(ProductContentCarrefour.GMO_ABSENCE, details_desc) is not None:
                details_gmo = False

            if details_additive is None and find_all_substrings_in_text(ProductContentCarrefour.ADDITIVE_ABSENCE, details_desc) is not None:
                details_additive = False

            if details_dye is None and find_all_substrings_in_text(ProductContentCarrefour.DYE_ABSENCE, details_desc) is not None:  # *colorant : E150d* , # *colorant : anthocyanes*
                details_dye = False

            if details_preservative is None and find_all_substrings_in_text(ProductContentCarrefour.PRESERVATIVE_ABSENCE, details_desc) is not None:
                details_preservative = False

            if details_gluten is None and find_all_substrings_in_text(ProductContentCarrefour.GLUTEN_ABSENCE, details_desc) is not None:
                details_gluten = False
            elif details_gluten is None and find_all_substrings_in_text(ProductContentCarrefour.GLUTEN_PRESENCE, details_desc) is not None:
                details_gluten = True

            if details_sugar is None and find_all_substrings_in_text(ProductContentCarrefour.SUGAR_ABSENCE, details_desc) is not None:
                details_sugar = False

            return LabelCarrefour(bio=details_bio, frozen=details_frozen, halal=details_halal, fr_greengrocery=details_fr_greengrocery, gluten=details_gluten,
                                  pregnant=details_pregnant, vegan=details_vegan, vegetarian=details_vegetarian, sugar=details_sugar, lactose=details_lactose)
        return None


class OfferCarrefour(Offer):
    @override
    @classmethod
    def extractInfo(cls, desc: str) -> 'Offer':
            '''
            "A saisir"
            "Promotion"
            "Vu en catalogue"
            "PROMO : 20%"
            "Prime Bio, 10% d'économies"
            "34% d'économies"

            "Le 2ème à -30%"
            "2 achetés = 5,75€"
            "Prenez en 3 = Payez en 2"
            "1 acheté = 10% de remise"
            '''
            requiredProductQuantity: int = None
            if isinstance (desc, str):
                desc = desc.lower()
            else:
                return None
            if is_any_string_in_string_list(["% d'économies", "A saisir", "Promotion", "Vu en catalogue", "PROMO :"], desc):
                requiredProductQuantity = 0
            elif is_any_string_in_string_list(["Prenez en", "achetés =", "ème à", "acheté"], desc):
                # create regex
                match = re.search(r'\d', desc)
                value = match.group(0) if match else None
                value = int(value) if value else None
                requiredProductQuantity = value
            else:
                requiredProductQuantity = None

            return Offer(description=LangDesc(fr=Desc(desc=desc)), requiredProductQuantity=requiredProductQuantity)

    
class EvolutionCarrefour(Evolution):
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

            evol = EvolutionCarrefour(parsing_date=evol_date, format=evol_format, availability=evol_availabilty, price_per_unit=evol_pricePerUnit,
                                      price=evol_price, nutriscore=evol_nutriscore, certification=evol_certification, nutrition=evol_nutrition,
                                      ingredients=evol_ingredients, allergens=evol_allergens, reviews=customerReviews,
                                      on_discount=on_discount)
            return evol
        return None


class MarketCarrefour(Market):
    @classmethod
    @override
    def from_dict_to_object(cls, product: dict):
        market_name = product.get("market") or "carrefour"
        market_address = product.get("address") or "market Paris Alésia"
        market_country = product.get("market_country") or "FR"
        return MarketCarrefour(name=market_name, country=market_country, address=market_address)

    @override
    def __init__(self, name="carrefour", address="market Paris Alésia", country="FR"):
        super().__init__(name="carrefour", address="market Paris Alésia", country="FR")
        self.name = name
        self.address = address
        self.country = country


class ProductCarrefour(Product):
    @override
    @classmethod
    def from_dict_to_object(cls, product: dict) -> 'ProductCarrefour':
        ean = product.get("ean")
        businessType = product.get("businessType")

        origin = Origin(ean=get_country_code_from_ean(ean=ean), explicit=get_country_code_from_country_name_in_french_lang(product.get("origin")),
                        partial=product.get("partial_origin"))

        unit_of_mesure = product.get("unit_of_mesure")
        freshness = Freshness(value=product.get("freshness_value"), period=product.get("freshness_period"))
        freshness = freshness.get_freshness_days_from_object()

        created_at = product.get("created_at")
        updated_at = product.get("updated_at")

        market = MarketCarrefour(name=product.get("market"), country=product.get("market_country"),
                                 address=product.get("market_address"))

        categories = product.get("categories")  # list
        categories: list[Category] = from_dict_to_objects(Category, categories)

        lang_desc = product.get("lang_desc")  # dict
        lang_desc = LangDesc.from_dict_to_object(lang_desc=lang_desc)

        brand = product.get("brand").upper() if product.get("brand") is not None else ProductContentCarrefour.get_brand_from_title(lang_desc.fr.title)

        label = LabelCarrefour.from_dict_to_object(product=product)

        evolutions = product.get("evolution")  # list
        evolutions = from_dict_to_objects(Evolution, evolutions)

        product = ProductCarrefour(ean=ean, brand=brand, business_type=businessType, origin=origin, unit_of_mesure=unit_of_mesure,
                                   freshness=freshness, created_at=created_at, updated_at=updated_at, market=market, categories=categories,
                                   lang_desc=lang_desc, evolutions=evolutions, label=label)

        return product
