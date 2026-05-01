import json
import re
import sys
import os
from dataclasses import asdict
from typing import Any, Dict, Final, List, Optional, Tuple, override
from selenium.webdriver.common.by import By
from selenium import webdriver


sys.path.append('src')
sys.path.append('./')
from utils.appium_utils import wait_el, wait_els
from src.model.product import Nutrition
from src.model.product import Label
from src.model.my_model import ProductType
from src.countries.spain.AlCampoV3.robots import webdriverInstance

"""from src.countries.spain.AlCampoV3.model import all_brands
from src.model.my_model import ProductType
from src.model.product import Nutrition"""
from src.utils.my_utils import (
    all_attrs_are_none,
    are_string_exist_in_list,
    are_strings_equal,
    convert_to_float,
    convert_to_target_unit,
    get_all_files_inside_given_folder,
    remove_punctuation,
    remove_substring_and_clean,
    remove_substrings_and_clean,
    write_output_to_file,
    match_nutrition_key,
    normalize_to_mg

)

class ProductContentEroski(object): 

    HALAL_PRESENCE: Final [List[str]] = ["halal", "Halal" , "HALAL", "kosher"]

    BIO_PRESENCE: Final [List[str]] = ["ECOLÓGICO", "eco","biológicas", "ecológico" ,"De agricultura ecológica", "ecológica" ,"Organic", "BIO" , 
                                       "ecológicos" , "ecológicas" , "biológica" , "Eco" , "De cultivo ecológico" , "agricultura ecológica" , "ALMENDRA ecológica" , "bio"] 
    
    VEGAN_PRESENCE: Final [List[str]] = ["vegano", "Vegetánea", "végétalien" , "Vegetal" , "Vegano" ]

    SPANISH_PRESENCE:Final [List[str]] = ["España" , "Origen de la leche España","ganaderos españoles", "ORIGEN DE LA LECHE: ESPAÑA", "de origen español" 
                                         ,"ORIGEN: ESPAÑA","Origen Nacional" ,"País de Ordeño: España","receta española", "Proviene de la agricultura española",
                                           "País de transformación: España" ,"agricultura española " , "Origen de la leche: España"]
    
    SPANICH_ABSENCE:Final [List[str]] = [ "HOLANDA", "Francia", "Harina acondicionada de trigo", "República Checa"]
    

    LACTOSE_PRESENCE:Final [List[str]] = ["lactosa" ,"CONTIENE LACTOBACILLUS CASEI","aroma (contiene lactosa)","LECHE Y SUS DERIVADOS (INCLUIDA LA LACTOSA)",
                                         ]
    
    LACTOSE_ABSENCE:Final [List[str]] = ["LACTASA" , "leche pasteurizada sin lactosa", "elaborado sin lactosa" ,"sin lacosa", "Sin lácteos",
                                         "Leche en polvo desnatada sin lactosa","Naturalmente sin lactosa" ,"enzima lactasa", "SIN LACTOSA"
                                         "Sin lactosa","lactasa"]
    
    GLUTEN_PRESENCE: Final [List[str]] = [" Pueden contener trazas de GLUTEN" , "gluten de trigo", "PASTA ALIMENTICIA DE SÉMOLA DE TRIGO DURO (GLUTEN)", "Semola de trigo duro (100%)(gluten)","pan rallado (contiene gluten)","Harina integral de avena (contiene gluten)",
                                           "TRAZAS DE: SÉSAMO Y SOJA","puede contener CEREALES QUE CONTIENEN GLUTEN","Contiene gluten","Harina de trigo (gluten)", 
                                           "Puede contener trazas de cereales con gluten" ,"Puede contener trazas de cereales (gluten menos de 5ppm)",
                                           "Puede contener trazas de cereales que contienen gluten" ,"Harina de TRIGO (GLUTEN)" , "GLUTEN MENOS DE 5PPM" ,"GLUTEN"]
    
    GLUTEN_ABSENCE: Final [List[str]] = ["Sin gluten", "sin gluten 100%" , "sin gluten","pan rallado sin gluten", "no contiene gluten"]

    FAT_ABSENCE:Final [List[str]] = ["sin grasas añadidas", "sin grasas" ,"Sin grasas añadidas" ,"Sin grasa añadida" ,"Sin grasa" ,"Sin grasas"]

    SUGAR_ABSENCE:Final [List[str]] = ["0% azucar","no tiene azúcares añadidos","ni azúcares añadidos", "Sin azucares añadidos" ,"sin azúcar" , "sin azúcares añadidos" ,  ]

    ADDITIVE_ABSENCE:Final [List[str]] = ["BIO 100% ", "sin conservantes" ,"Sin ningún tipo de aditivo"]

    DYE_ABSENCE:Final [List[str]] = ["aroma natural","aroma natural de vainilla", "ARÔME NATUREL" ]

    GMO_ABSENCE:Final [List[str]] = ["sin OGM", "sin OGM" ,"Sin OGM" ,"Sin organismos modificados genéticamente" ,"Sin organismos genéticamente modificados",]

    PRESERVATIVE_ABSENCE:Final [List[str]] = ["sin conservantes", "sin conservante" ,"Sin conservantes" ,"Sin conservante" ,"Sin conservantes añadidos"]

    INGREDIENTS_SUBSTRINGS: Final[List[str]] = [
    # 🧾 Expressions marketing ou décoratives
    "ingredientes ecológicos","ver las fotos","y nada más","un poco de bueno","sin azúcares añadidos","productos procedentes de la agricultura ecológica naturalmente sin gluten","procedente de la agricultura ecológica","ingredientes procedentes de la agricultura ecológica",
    "presencia según la acidez de las frutas","contiene azúcares naturalmente presentes en las frutas, como todos los jugos",
    "de francia", "de meurthe-et-moselle", "de ecuador", "de occitania","de provenza", "de nueva aquitania", "de suecia", "de españa", "francesas",
    "un chorrito de jugo de","un pequeño extracto de","una pizca de extracto de","una gota de extracto de","un dedo de","un poco de jugo de",
    "un hilo de","un toque de infusión de","una ralladura de","un trozo de","algunas", "colorante :", "colorante:","acidificante :", "acidificante:","estabilizante:", "estabilizante :","concentrado", "concentrada","*",
    ]
    # sugar if < 0.9% ==> sugar free

    
    @classmethod
    def get_packaging_info(cls, product_pricing_unit: Optional[str]) -> tuple[Optional[str], Optional[str], Optional[float]]:
        if not isinstance(product_pricing_unit, str):
            return None, None, None

        original_text = product_pricing_unit
        product_pricing_unit = product_pricing_unit.lower().replace(",", ".").strip()

        matter = ProductType.OTHER.name  # 👈 bien: on utilise .name pour avoir une str
        unit_of_measure = None

        if any(keyword in product_pricing_unit for keyword in ["kilogramo", "kg" , "KILO"]):
            matter = ProductType.SUBSTANCE.name
            unit_of_measure = "kg"
        elif any(keyword in product_pricing_unit for keyword in ["gramo", "gr", "g"]):
            matter = ProductType.SUBSTANCE.name
            unit_of_measure = "g"
        elif any(keyword in product_pricing_unit for keyword in ["pièce", "unidad", "pce"]):
            matter = ProductType.PIECE.name
            unit_of_measure = "piece"
        elif any(keyword in product_pricing_unit for keyword in ["litro", "l" , "LITRO"]):
            matter = ProductType.LIQUID.name
            unit_of_measure = "l"

        numbers = re.findall(r"[-+]?\d*\.\d+|\d+", product_pricing_unit)
        value = float(numbers[0]) if numbers else None

        print(f"[DEBUG] packaging: '{original_text}' → unit: {unit_of_measure}, matter: {matter}, value: {value}")
        return unit_of_measure, matter, value
    
    @staticmethod
    def extract_brand_from_title(driver, index: int, fallback: str = "EROSKI") -> str:
        """
        Extrait la marque depuis le titre produit.
        - La marque est supposée être constituée de 1 à 3 mots en majuscules (≥ 2 lettres chacun)
        situés avant la première virgule.
        - Si aucune marque valide n'est trouvée → fallback ("EROSKI").
        """
        try:
            full_title = wait_el(driver, By.CSS_SELECTOR, "h1.description-title").text.strip()

            marque = fallback
            if "," in full_title:
                brand_part = full_title.split(",")[0]

                # Regex : capture 1 à 3 mots en majuscules (y compris accents)
                brand_match = re.search(
                    r"\b([A-ZÁÉÍÓÚÑÜ]{2,}(?:\s+[A-ZÁÉÍÓÚÑÜ]{2,}){0,2})\b",
                    brand_part
                )
                if brand_match:
                    marque = brand_match.group(1).strip()

            print(f"[{index}] 🏷️ Marque : {marque}")
            return marque

        except Exception:
            print(f"[{index}] ❌ Impossible d'extraire la marque. Valeur par défaut utilisée : {fallback}")
            return fallback

        
    @staticmethod
    def get_label_and_origin(driver: webdriver) -> tuple[Optional[Label], Optional[str]]:
        if not driver:
            return None, None

        label = Label()
        spanish_origin = None

        try:
            # Cherche le bloc des attributs produit (basé sur le titre h2)
            header = wait_el(driver, By.XPATH, "//h2[contains(text(), 'Atributos del producto')]")
            if not header:
                return label, spanish_origin

            attributes_block = wait_el(header, By.XPATH, "./parent::*")
            if not attributes_block:
                return label, spanish_origin

            icon_divs = wait_els(attributes_block, By.CSS_SELECTOR, "div.sc-mmemlz-0")

            for div in icon_divs:
                try:
                    icon_svg = wait_el(div, By.CSS_SELECTOR, "svg")
                    if not icon_svg:
                        continue
                    icon_id = icon_svg.get_attribute("data-icon")

                    if "lactose_free" in icon_id:
                        label.lactose_free = True
                    elif "cooled" in icon_id:
                        label.cooled = True
                    elif "vegan" in icon_id:
                        label.vegan = True
                    elif "eco" in icon_id:
                        label.bio = True
                    elif "gluten" in icon_id:
                        label.gluten_free = True
                    elif "gmofree" in icon_id:
                        label.gmo_free = True
                    elif "froozen" in icon_id:
                        label.frozen = True
                    elif "pregnancy" in icon_id:
                        label.pregnancy_unsafe = True
                    elif "vegetarian" in icon_id or "fruitslegumesfr" in icon_id:
                        label.vegetarian = True
                        spanish_origin = "espana"
                    elif "regional" in icon_id or "frenchpoultrymeat" in icon_id:
                        label.fr_greengrocery = True
                        spanish_origin = "espana"
                    elif "fatfree" in icon_id:
                        label.fat_free = True
                    elif "addedsugarfree" in icon_id:
                        label.sugar_added_free = True
                except:
                    continue
        except:
            pass

        return label, spanish_origin
    
    @staticmethod
    def detect_allergens(ingredients_text: Optional[str], allergens_list: List[str]) -> List[str]:
        if not ingredients_text:
            return []
        ingredients_lower = ingredients_text.lower()
        found_allergens = []
        for allergen in allergens_list:
            if allergen.lower() in ingredients_lower:
                found_allergens.append(allergen)
        return found_allergens

    @staticmethod
    def flatten_nutrition(nut):
        flat = {}
        # énergies
        if "energies" in nut:
            e = nut["energies"]
            flat["Energía (kJ)"]   = e.get("kj",   0)
            flat["Energía (kcal)"] = e.get("kcal", 0)
        # sels (mg → g si nécessaire) et clé en espagnol pour le mapping
        if "minerals" in nut:
            m = nut["minerals"]
            raw_s = m.get("salt", 0)
            # si la valeur est >10 (typiquement mg), on convertit en g
            g_s   = raw_s / 1000.0 if raw_s > 10 else raw_s
            flat["Sal"] = g_s

        # graisses saturées
        if "fats" in nut:
            f = nut["fats"]
            flat["Grasas saturadas"] = f.get("saturates", 0)
        # protéines
        if "proteins" in nut:
            p = nut["proteins"]
            flat["Proteínas"] = p.get("proteins", 0)
        # glucides, sucres & fibres
        if "carbohydrates" in nut:
            c = nut["carbohydrates"]
            flat["Hidratos de carbono"] = c.get("carbohydrates", 0)
            flat["Azúcares"]             = c.get("sugars",         0)
            flat["Fibra alimentaria"]    = c.get("dietary_fiber",  0)
        return flat

    @staticmethod
    def calculate_nutriscore_from_nested(nutrition: dict | Nutrition) -> str:
        try:
            # 1) Aplatir si on reçoit le dict imbriqué complet
            if isinstance(nutrition, dict) and "energies" in nutrition:
                nutrition = ProductContentEroski.flatten_nutrition(nutrition)

            # 2) Transformer l'objet Nutrition en dict si besoin
            if not isinstance(nutrition, dict):
                if hasattr(nutrition, "to_dict"):
                    nutrition = nutrition.to_dict()
                else:
                    nutrition = vars(nutrition)


            # 4) Utilitaires
            def to_float(value):
                try:
                    return float(str(value).replace(",", ".").strip())
                except:
                    return 0.0

            key_map = {
                "Azúcares": "sugars",
                "Grasas saturadas": "saturated_fats",
                "Fibra alimentaria": "fibers",
                "Sal": "salt",
                "Proteínas": "proteins",
                "Hidratos de carbono": "carbohydrates",
                "Energía (kJ)": "Energía (kJ)",
                "Energía (kcal)": "Energía (kcal)",
            }
            nutrition = {key_map.get(k, k): v for k, v in nutrition.items()}

            # 5) Extraction des valeurs numériques
            energy_kj =   to_float(nutrition.get("Energía (kJ)", 0))
            sugars_g  =   to_float(nutrition.get("sugars",         0))
            satfat_g  =   to_float(nutrition.get("saturated_fats", 0))
            fiber_g   =   to_float(nutrition.get("fibers",         0))
            protein_g =   to_float(nutrition.get("proteins",       0))
            salt_g    =   to_float(nutrition.get("salt",           0))
            fruits_pct =  to_float(nutrition.get("fruits_percentage", 0))

            # 6) Points négatifs
            pts_energy = min(int(energy_kj / 335), 10)
            pts_sugar  = min(int(sugars_g  / 4.5), 10)
            pts_satfat = min(int(satfat_g  / 1),   10)
            pts_salt   = min(int(salt_g    / 0.09),10)
            neg = pts_energy + pts_sugar + pts_satfat + pts_salt

            # 7) Points positifs
            pts_fiber   = min(int(fiber_g   / 0.9), 5)
            pts_protein = min(int(protein_g / 1.6), 5)
            if   fruits_pct >= 80: pts_fruits = 5
            elif fruits_pct >= 60: pts_fruits = 2
            elif fruits_pct >= 40: pts_fruits = 1
            else:                  pts_fruits = 0
            pos = pts_fiber + pts_protein + pts_fruits

            # 8) Score final et lettre
            score = neg - pos
            if   score <= -1: result = "A"
            elif score <=  2: result = "B"
            elif score <= 10: result = "C"
            elif score <= 18: result = "D"
            else:             result = "E"

            print(f"[Nutri-Score] Score = {score} → Nutri-Score = {result}")
            return result

        except Exception as e:
            print(f"❌ Erreur calcul Nutriscore : {e}")
            return "N/A"
        
    @classmethod
    def convert_nutrition_name(cls, nutrition_name):
        """Converts a spanish nutrition name to its English equivalent.

        Args:
            nutrition_name (str): The French name of a nutrition element.

        Returns:
            str: The English equivalent of the nutrition name, or None if not found.
        """

        # Define the dictionary for name mapping
        nutrition_name = {
            "Valor energético (Kj)": "energy_value(kJ)",
            "Valor energético (Kcal)": "energy_value(kcal)",
            "Grasas": "fats",
            "Grasas saturadas": "saturated_fatty_acids",
            "Hidratos de carbono": "carbohydrates",
            "glucides": "carbohydrates",
            "Azúcares": "sugar",
            "Fibres alimentaires": "dietary_fiber",
            "fibres alimentaires": "dietary_fiber",
            "Proteínas": "proteins",
            "Proteínas": "proteines",
            "Sal": "salt",
            "Sal": "salt",
            "calcio": "calcium",
            "Vitamina D": "vitamin_D",
            "Fibra": "fiber",
            "Ácido linoleico = LA": "Linoleic_Acid",
            "Ácido alfa-linolénico = ALA": "Alpha_Linolenic_Acid",
            "sodio": "sodium",
            "Vitamina A": "vitamin_A",
            "Vitamina D": "vitamin_D",
            "Vitamina E": "vitamin_E",
            "Vitamina K": "vitamin_K",
            "Vitamina C": "vitamin_C",
            "Vitamina B6": "vitamin_B6",
            "vitamina B3": "vitamin_B3",
            "Tiamina": "thiamine",
            "Riboflavina": "riboflavine",
            "Niacina": "niacin",
            "Vitamina B6": "vitamin_B6",
            "Ácido fólico": "folic_Acid",
            "Vitamina B12": "vitamin_B12",
            "Biotina": "biotin",
            "Ácido pantoténico": "pantothenic_Acid",
            "Potasio": "potassium",
            "Fósforo": "phosphorus",
            "Hierro": "iron",
            "zinc": "zinc",
            "yodo": "iodine",
            "almidón": "starch",
            "magnesio": "magnesium",
            "Magnesio": "magnesium",
            "Lactosa": "lactose",
            "omega 3": "omega_3",
            "Incluye ácidos grasos monoinsaturados": "Including_monounsaturated_fatty_acids",
            "Incluye ácidos grasos poliinsaturados": "Including_polyunsaturated_fatty_acids",
            "ácidos grasos monoinsaturados": "Monounsaturated_fatty_acids",
            "Unidad energética": "energy_value(kJ)",
            "Valor energético": "energy_value(kcal)",
            "Cloruro": "Chloride",
            "Magnesio": "Magnesium",
            "Cobre": "Copper",
            "Fluoruro": "Flouride",
            "Selenio": "Selenium",
            "Colina": "Choline",
            "Inositol": "Inositol",
            "L-Carnitina": "LCarnitine",
            "FOS": "FOS",
            "GOS": "GOS",
            "3'Galactosyllactoses": "GAL",
            "Cloruro": "Chloride"
        }

        # Check if nutrition_name exists in the dictionary
        converted_name = nutrition_name.get(nutrition_name)

        # Return converted name or None if not found
        return converted_name
class NutritionContentEroski:
        
        ENERGY_VALUE_KJ_FINAL: Final[List[Tuple[str, int]]] = [("Valor energético (Kj)", 95), ("Energía.*kj", 95), ("Unidad energética KJ", 95), ("kj", 95), ("energy_value_kJ", 95)]
        ENERGY_VALUE_KCAL_FINAL: Final[List[Tuple[str, int]]] = [("Energía (kcal)", 95),("Valor energético (Kcal)", 95),("kcal", 95),("kilocaloría", 95),("energy_value_kcal", 95)]
        FATS_FINAL: Final[List[Tuple[str, int]]] = [("Grasas", 95), ("Grasas totales", 95), ("grasas", 95)]
        SATURATES_FINAL: Final[List[Tuple[str, int]]] = [("Grasas saturadas", 90), ("Ácidos grasos saturados", 90), ("saturadas", 95), ("of_which_saturates", 95), ("de las cuales saturadas", 90)]
        CARBOHYDRATES_FINAL: Final[List[Tuple[str, int]]] = [("Hidratos de carbono", 90), ("carbohidratos", 90)]
        WITH_SUGAR_FINAL: Final[List[Tuple[str, int]]] = [("de los cuales azúcares", 95), ("con azúcares", 95), ("de los cuales: azúcares", 90)]
        SUGARS_FINAL: Final[List[Tuple[str, int]]] = [("Azúcares", 95), ("azúcar", 90), ("azúcares", 90)]
        DIETARY_FIBER_FINAL: Final[List[Tuple[str, int]]] = [("Fibra alimentaria", 95), ("fibra dietética", 95)]
        PROTEINES_FINAL: Final[List[Tuple[str, int]]] = [("Proteínas", 90), ("proteína", 90), ("proteínas", 90)]
        SALT_FINAL: Final[List[Tuple[str, int]]] = [("Sal", 90), ("sal", 90)]
        CALCIUM_FINAL: Final[str] = "calcio"
        FIBER_FINAL: Final[List[Tuple[str, int]]] = [("Fibra", 90), ("fibra", 90)]
        LINOLEIC_ACID_FINAL: Final[List[Tuple[str, int]]] = [("Ácido linoleico = LA", 90), ("LINOLEIC_ACID", 90)]
        ALPHA_LINOLENIC_ACID_FINAL: Final[List[Tuple[str, int]]] = [("Ácido alfa-linolénico = ALA", 90), ("ALPHA_LINOLENIC_ACID", 90)]
        SODIUM_FINAL: Final[str] = "sodio"
        POTASSIUM_FINAL: Final[str] = "Potasio"
        CHROMIUM_FINAL: Final[List[Tuple[str, int]]] = [("Cromo", 90), ("cromo", 90)]
        PHOSPHORUS_FINAL: Final[List[Tuple[str, int]]] = [("Fósforo", 90), ("fósforo", 90)]
        IRON_FINAL: Final[List[Tuple[str, int]]] = [("Hierro", 95), ("hierro", 90)]
        ZINC_FINAL: Final[str] = "zinc"
        IODINE_FINAL: Final[List[Tuple[str, int]]] = [("Yodo", 90), ("yodo", 90)]
        STARCH_FINAL: Final[List[Tuple[str, int]]] = [("Almidón", 90), ("almidón", 90)]
        MAGNESIUM_FINAL: Final[List[Tuple[str, int]]] = [("Magnesio", 90), ("magnesio", 90)]
        LACTOSE_FINAL: Final[str] = "lactosa"
        OMEGA_3_FINAL: Final[List[Tuple[str, int]]] = [("Omega 3", 90), ("omega 3", 90)]
        SATURATED_FATTY_ACIDS_FINAL: Final[List[Tuple[str, int]]] = [("Ácidos grasos saturados", 90), ("SATURATED_FATTY_ACIDS", 90)]
        MONOUNSATURATED_FATTY_ACIDS_FINAL: Final[List[Tuple[str, int]]] = [("Ácidos grasos monoinsaturados", 90), ("MONOUNSATURATED_FATTY_ACIDS", 90)]
        INCLUDING_MONOUNSATURATED_FATTY_ACIDS_FINAL: Final[List[Tuple[str, int]]] = [("Incluye ácidos grasos monoinsaturados", 90), ("INCLUDING_MONOUNSATURATED_FATTY_ACIDS", 90)]
        INCLUDING_POLYUNSATURATED_FATTY_ACIDS_FINAL: Final[List[Tuple[str, int]]] = [("Incluye ácidos grasos poliinsaturados", 90), ("INCLUDING_POLYUNSATURATED_FATTY_ACIDS", 90)]
        CHLORIDE_FINAL: Final[List[Tuple[str, int]]] = [("Cloruro", 90), ("cloruro", 90)]
        COPPER_FINAL: Final[List[Tuple[str, int]]] = [("Cobre", 90), ("cobre", 90)]
        FLUORIDE_FINAL: Final[List[Tuple[str, int]]] = [("Flúor", 90), ("FLUORIDE", 90)]
        SELENIUM_FINAL: Final[List[Tuple[str, int]]] = [("Selenio", 85), ("selenio", 85)]
        CHOLINE_FINAL: Final[str] = "Colina"
        INOSITOL_FINAL: Final[str] = "Inositol"
        L_CARNITINE_FINAL: Final[List[Tuple[str, int]]] = [("L-Carnitina", 95), ("L_CARNITINE", 95)]
        FOS_FINAL: Final[str] = "FOS"
        GOS_FINAL: Final[str] = "GOS"
        GAL_FINAL: Final[List[Tuple[str, int]]] = [("3'Galactosil-lactosas", 95), ("GAL", 95)]
        MANAGANESE_FINAL: Final[List[Tuple[str, int]]] = [("Manganeso", 85), ("manganeso", 85)]
        POLYOLS_FINAL: Final[List[Tuple[str, int]]] = [("Polioles", 95), ("de los cuales: polioles", 95)]

        # Vitamines
        VITAMINE_A: Final[List[Tuple[str, int]]] = [("Vitamina A", 99), ("retinol", 90), ("A", 95), ("vitamin_a", 99), ("vitamina_a", 99)]
        VITAMINE_B1: Final[List[Tuple[str, int]]] = [("Vitamina B1", 99), ("Tiamina", 90), ("B1", 95), ("vitamin_b1", 99)]
        VITAMINE_B2: Final[List[Tuple[str, int]]] = [("Vitamina B2", 99), ("Riboflavina", 90), ("B2", 95), ("vitamin_b2", 99)]
        VITAMINE_B3: Final[List[Tuple[str, int]]] = [("Vitamina B3", 99), ("Niacina", 90), ("B3", 95), ("vitamin_b3", 99)]
        VITAMINE_B5: Final[List[Tuple[str, int]]] = [("Vitamina B5", 99), ("Ácido pantoténico", 90), ("B5", 95), ("vitamin_b5", 99)]
        VITAMINE_B6: Final[List[Tuple[str, int]]] = [("Vitamina B6", 99), ("Piridoxina", 90), ("B6", 95), ("vitamin_b6", 99)]
        VITAMINE_B7: Final[List[Tuple[str, int]]] = [("Vitamina B7", 99), ("Biotina", 90), ("B7", 95), ("vitamin_b7", 99)]
        VITAMINE_B9: Final[List[Tuple[str, int]]] = [("Vitamina B9", 99), ("Ácido fólico", 90), ("B9", 95), ("vitamin_b9", 99)]
        VITAMINE_B12: Final[List[Tuple[str, int]]] = [("Vitamina B12", 99), ("Cobalamina", 90), ("B12", 95), ("vitamin_b12", 99)]
        VITAMINE_C: Final[List[Tuple[str, int]]] = [("Vitamina C", 99), ("Ácido ascórbico", 90), ("C", 95), ("vitamin_c", 99)]
        VITAMINE_D: Final[List[Tuple[str, int]]] = [("Vitamina D", 99), ("Colecalciferol", 90), ("D", 95), ("vitamin_d", 99)]
        VITAMINE_E: Final[List[Tuple[str, int]]] = [("Vitamina E", 99), ("Tocoferol", 90), ("E", 95), ("vitamin_e", 99)]
        VITAMINE_K: Final[List[Tuple[str, int]]] = [("Vitamina K", 99), ("Filoquinona", 90), ("K", 95), ("vitamin_k", 99)]

class NutritionEroski(Nutrition):
    @classmethod
    @override
    def convert_dict_to_nutrition_object(cls, nutritions: dict | None) -> Nutrition | None:
        if not isinstance(nutritions, dict):
            return None
        nutrition = Nutrition()
        energies = Nutrition.Energy()
        fats = Nutrition.Fats()
        fats_measurement = Nutrition.Fats.get_measurement_unit()
        carbohydrates = Nutrition.Carbohydrates()
        carbohydrates_measurement = Nutrition.Carbohydrates.get_measurement_unit()
        proteins = Nutrition.Proteins()
        proteins_measurement = Nutrition.Proteins.get_measurement_unit()
        fatty_acids = Nutrition.FattyAcids()
        fatty_measurement = Nutrition.FattyAcids.get_measurement_unit()
        minerals = Nutrition.Minerals()
        minerals_measurement = Nutrition.Minerals.get_measurement_unit()
        vitamins = Nutrition.Vitamins()
        vitamins_measurement = Nutrition.Vitamins.get_measurement_unit()
        vitaminLikes = Nutrition.VitaminLikes()
        vitaminLikes_measurement = Nutrition.VitaminLikes.get_measurement_unit()

        for key, value in nutritions.items():
            print(f"key: {key}, value: {value}")

            key_clean = key.strip().lower()
            value_clean = value.strip()

            # ✅ Traitement prioritaire pour les kilojoules (kJ)
            if match_nutrition_key(key, NutritionContentEroski.ENERGY_VALUE_KJ_FINAL):
                try:
                    value_clean = remove_substring_and_clean(value_clean, "kj")
                    energies.kj = convert_to_float(value_clean)
                    print(f"✅ énergie kJ (via match_nutrition_key) : {energies.kj}")
                except Exception as e:
                    print(f"[WARN] Erreur conversion kJ pour '{key}' : {e}")

            elif key_clean == "energía (kcal)":
                try:
                    kcal_match = re.search(r"([\d.]+)", value_clean)
                    if kcal_match:
                        energies.kcal = convert_to_float(kcal_match.group(1))
                        print(f"✅ énergie kcal détectée explicitement : {energies.kcal}")
                except Exception as e:
                    print(f"[WARN] Erreur conversion explicite kcal : {e}")

            elif key_clean == "energía (kj)":
                try:
                    kj_match = re.search(r"([\d.]+)", value_clean)
                    if kj_match:
                        energies.kj = convert_to_float(kj_match.group(1))
                        print(f"✅ énergie kJ détectée explicitement : {energies.kj}")
                except Exception as e:
                    print(f"[WARN] Erreur conversion explicite kj : {e}")

            elif match_nutrition_key(key, NutritionContentEroski.ENERGY_VALUE_KCAL_FINAL):
                print(f"✅ Match kcal via fuzzy match : {key} = {value_clean}")
                try:
                    kcal_match = re.search(r"([\d.]+)", value_clean)
                    if kcal_match:
                        energies.kcal = convert_to_float(kcal_match.group(1))
                except Exception as e:
                    print(f"[WARN] Erreur conversion kcal fuzzy : {e}")

            # ✅ TRAITEMENT EN PARALLÈLE POUR 'energía' GÉNÉRIQUE
            if key_clean == "energía":
                if "kcal" in value_clean.lower() or "kilocaloría" in value_clean.lower():
                    print("✅ Clé ambiguë 'Energía' contient kcal → traitée comme kcal")
                    try:
                        kcal_match = re.search(r"([\d.]+)", value_clean)
                        if kcal_match:
                            energies.kcal = convert_to_float(kcal_match.group(1))
                    except Exception as e:
                        print(f"[WARN] Erreur conversion kcal (Energía) : {e}")

                if "kj" in value_clean.lower() or "kilojulio" in value_clean.lower():
                    print("✅ Clé ambiguë 'Energía' contient kj → traitée comme kj")
                    try:
                        kj_match = re.search(r"([\d.]+)", value_clean)
                        if kj_match:
                            energies.kj = convert_to_float(kj_match.group(1))
                    except Exception as e:
                        print(f"[WARN] Erreur conversion kJ (Energía) : {e}")

            # macronutrients
            elif are_string_exist_in_list(key, NutritionContentEroski.FATS_FINAL):
                fats.fats = convert_to_target_unit(value, fats_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.SATURATES_FINAL):
                fats.saturates = convert_to_target_unit(value, fats_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.CARBOHYDRATES_FINAL):
                carbohydrates.carbohydrates = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.WITH_SUGAR_FINAL):
                carbohydrates.of_which_sugars = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.SUGARS_FINAL):
                carbohydrates.sugars = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.DIETARY_FIBER_FINAL):
                carbohydrates.dietary_fiber = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.STARCH_FINAL):
                carbohydrates.starch = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_strings_equal(key, NutritionContentEroski.LACTOSE_FINAL, 90):
                carbohydrates.lactose = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.GAL_FINAL):
                carbohydrates.gal = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.FIBER_FINAL):
                carbohydrates.fiber = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.POLYOLS_FINAL):
                carbohydrates.polyols = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.PROTEINES_FINAL):
                proteins.proteins = convert_to_target_unit(value, proteins_measurement)

            # Minerals
            elif are_strings_equal(key, NutritionContentEroski.SODIUM_FINAL, 90):
                minerals.sodium = normalize_to_mg(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.SALT_FINAL):
                minerals.salt = normalize_to_mg(value, minerals_measurement)
            elif are_strings_equal(key, NutritionContentEroski.CALCIUM_FINAL, 90):
                minerals.calcium = normalize_to_mg(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.MANAGANESE_FINAL):
                minerals.manganese = normalize_to_mg(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.MAGNESIUM_FINAL):
                minerals.magnesium = normalize_to_mg(value, minerals_measurement)
            elif are_strings_equal(key, NutritionContentEroski.POTASSIUM_FINAL, 90):
                minerals.potassium = normalize_to_mg(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.CHROMIUM_FINAL):
                minerals.chromium = normalize_to_mg(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.PHOSPHORUS_FINAL):
                minerals.phosphorus = normalize_to_mg(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.IRON_FINAL):
                minerals.iron = normalize_to_mg(value, minerals_measurement)
            elif are_strings_equal(key, NutritionContentEroski.ZINC_FINAL, 90):
                minerals.zinc = normalize_to_mg(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.IODINE_FINAL):
                minerals.iodine = normalize_to_mg(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.CHLORIDE_FINAL):
                minerals.chloride = normalize_to_mg(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.COPPER_FINAL):
                minerals.copper = normalize_to_mg(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.FLUORIDE_FINAL):
                minerals.fluoride = normalize_to_mg(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.SELENIUM_FINAL):
                minerals.selenium = normalize_to_mg(value, minerals_measurement)

            # FattyAcids
            elif are_string_exist_in_list(key, NutritionContentEroski.LINOLEIC_ACID_FINAL):
                fatty_acids.linoleic_acid = normalize_to_mg(value, fatty_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.ALPHA_LINOLENIC_ACID_FINAL):
                fatty_acids.alpha_linolenic_acid = normalize_to_mg(value, fatty_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.OMEGA_3_FINAL):
                fatty_acids.omega_3 = normalize_to_mg(value, fatty_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.SATURATED_FATTY_ACIDS_FINAL):
                fatty_acids.saturated_fatty_acids = normalize_to_mg(value, fatty_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.MONOUNSATURATED_FATTY_ACIDS_FINAL):
                fatty_acids.monounsaturated_fatty_acids = normalize_to_mg(value, fatty_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.INCLUDING_MONOUNSATURATED_FATTY_ACIDS_FINAL):
                fatty_acids.including_monounsaturated_fatty_acids = normalize_to_mg(value, fatty_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.INCLUDING_POLYUNSATURATED_FATTY_ACIDS_FINAL):
                fatty_acids.including_polyunsaturated_fatty_acids = normalize_to_mg(value, fatty_measurement)

            # Essential Nutrients or Vitamin-like
            elif are_strings_equal(key, NutritionContentEroski.CHOLINE_FINAL, 90):
                vitaminLikes.choline = convert_to_target_unit(value, vitaminLikes_measurement)
            elif are_strings_equal(key, NutritionContentEroski.INOSITOL_FINAL, 90):
                vitaminLikes.inositol = convert_to_target_unit(value, vitaminLikes_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.L_CARNITINE_FINAL):
                vitaminLikes.lcarnitine = convert_to_target_unit(value, vitaminLikes_measurement)
            elif are_strings_equal(key, NutritionContentEroski.FOS_FINAL, 90):
                vitaminLikes.fos = convert_to_target_unit(value, vitaminLikes_measurement)
            elif are_strings_equal(key, NutritionContentEroski.GOS_FINAL, 90):
                vitaminLikes.gos = convert_to_target_unit(value, vitaminLikes_measurement)

            # Vitamins: classified by order of exitence in food products
            elif are_string_exist_in_list(key, NutritionContentEroski.VITAMINE_B1):
                vitamins.vitamin_b1 = normalize_to_mg(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.VITAMINE_B2):
                vitamins.vitamin_b2 = normalize_to_mg(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.VITAMINE_B3):
                vitamins.vitamin_b3 = normalize_to_mg(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.VITAMINE_B5):
                vitamins.vitamin_b5 = normalize_to_mg(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.VITAMINE_B6):
                vitamins.vitamin_b6 = normalize_to_mg(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.VITAMINE_B7):
                vitamins.vitamin_b7 = normalize_to_mg(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.VITAMINE_B9):
                vitamins.vitamin_b9 = normalize_to_mg(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.VITAMINE_B12):
                vitamins.vitamin_b12 = normalize_to_mg(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.VITAMINE_C):
                vitamins.vitamin_c = normalize_to_mg(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.VITAMINE_A):
                vitamins.vitamin_a = normalize_to_mg(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.VITAMINE_E):
                vitamins.vitamin_e = normalize_to_mg(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.VITAMINE_K):
                vitamins.vitamin_k = normalize_to_mg(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentEroski.VITAMINE_D):
                vitamins.vitamin_d = normalize_to_mg(value, vitamins_measurement)

            """else:
                print(f"key not found: {key}")
                nutrition.unknown = nutrition.unknown if nutrition.unknown is dict else dict()
                nutrition.unknown[key] = convert_to_target_unit(value, "mg") if nutrition.unknown is not dict else dict(
                )"""

        nutrition.carbohydrates = carbohydrates if not all_attrs_are_none(carbohydrates) else None
        nutrition.fats = fats if not all_attrs_are_none(fats) else None
        nutrition.proteins = proteins if not all_attrs_are_none(proteins) else None
        nutrition.energies = energies if not all_attrs_are_none(energies) else None
        nutrition.fatty_acids = fatty_acids if not all_attrs_are_none(fatty_acids) else None
        nutrition.minerals = minerals if not all_attrs_are_none(minerals) else None
        nutrition.vitamins = vitamins if not all_attrs_are_none(vitamins) else None
        nutrition.vitamin_likes = vitaminLikes if not all_attrs_are_none(vitaminLikes) else None
        nutrition = nutrition if not all_attrs_are_none(nutrition) else None
        #print(f"nutrition result: " + str(nutrition))
        return nutrition

    @classmethod
    def extract_last_integer(cls, text: str) -> str | None:
        """
        Extract the last integer before 'ml' or 'g' from the given text.
        Exemples valides : "100 g", "100ml", "valores por 100 mL", etc.
        """
        print(f"Extracting last integer from: {text}")

        # Recherche du dernier nombre suivi de 'ml', 'g', etc.
        pattern = r'(?<=\/\s)(\d+)(?=\s?(?:mL|g))'

        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            return matches[-1]  # On prend le dernier match
        return None
    

    

    @staticmethod
    def keep_first_element(data_list: List[Any]) -> List[Any]:
        return [data_list[0]] if data_list else []

    @staticmethod
    def convert_to_nested_json(input_dict: Dict[str, bool]) -> List[Label]:
        label_dicts = []

        for category, value in input_dict.items():
            label_dict = {}
            if "additive" in category:
                label_dict['additive'] = False
            if "preservative_absent" in category:
                label_dict['preservative'] = False
            if "gmo_absent" in category:
                label_dict['gmo'] = False
            if "gmo_presence" in category:
                label_dict['gmo'] = True
            if "fat_absent" in category:
                label_dict['fat'] = False
            if "sugar_absent" in category:
                label_dict['sugar'] = False
            if "gluten_presence" in category:
                label_dict['gluten'] = True
            if "gluten_absent" in category:
                label_dict['gluten'] = False
            if "halal" in category:
                label_dict['halal'] = True
            if "lactose_presence" in category:
                label_dict['lactose'] = True
            if "lactose_absent" in category:
                label_dict['lactose'] = False

            if label_dict:
                label_dicts.append(label_dict)

        unique_label_dicts = [dict(t) for t in {tuple(d.items()) for d in label_dicts}]
        unique_labels = [Label(**label_dict) for label_dict in unique_label_dicts]
        return ProductContentEroski.keep_first_element(unique_labels)

    @staticmethod
    def concat_labels(labels1: List[Label], labels2: List[Label]) -> List[Label]:
        combined = labels1 + labels2
        seen = set()
        unique = []
        for label in combined:
            frozen = frozenset(asdict(label).items())
            if frozen not in seen:
                seen.add(frozen)
                unique.append(label)
        return unique
    
    @classmethod
    def compute_nutrition_values_per_100_g_or_ml(cls, nutrition: dict) -> dict:
        print(f"Modify the nutrition values...")
        if not isinstance(nutrition, dict):
            return None
        for key, value in nutrition.items():
            if not isinstance(value, str):
                nutrition[key] = value
                continue
            last_value = cls.extract_last_integer(value)
            if last_value is not None:
                nutrition[key] = cls.process_value(
                    last_value=last_value.lower(), value=value.lower())
        return nutrition

    @classmethod
    def modify_nutrition_in_file(cls, file_path: str, overwrite: bool = False):
        print(f"Reading JSON file: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for product in data:
            evolutions = product.get('evolutions', [])
            for evolution in evolutions:
                if 'nutrition_facts' in evolution:
                    nutrition = evolution['nutrition_facts']
                    nutrition = cls.compute_nutrition_values_per_100_g_or_ml(nutrition)
                    nutrition = cls.convert_dict_to_nutrition_object(nutrition)
                    evolution['nutrition_facts'] = nutrition

        output_path = file_path if overwrite else file_path.replace(".json", "_2.json")
        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False, allow_nan=False,
                      default=lambda o: {k: v for k, v in o.__dict__.items() if v is not None})
        print(f"Saved updated nutrition data to {output_path}")

    @classmethod
    def modify_all_nutrition_values(cls, root_folder: str, overwrite: bool = False):
        for dirpath, _, filenames in os.walk(root_folder):
            for filename in filenames:
                if filename.endswith(".json"):
                    file_path = os.path.join(dirpath, filename)
                    try:
                        cls.modify_nutrition_in_file(file_path, overwrite=overwrite)
                    except Exception as e:
                        print(f"❌ Failed to process {file_path}: {e}")

    def convert_unit_of_mesure(mesure_data):
        unit = None
        matter = None
        parts = mesure_data.split(
            ".")
        if len(parts) > 0:

            unit_mesure = parts[-1]
            if unit_mesure == "litro":
                matter = ProductType.LIQUID.name
                unit = "l"
            elif unit_mesure == "kilogramo":
                matter = ProductType.SUBSTANCE.name
                unit = "kg"
            elif unit_mesure == "ud":
                matter = ProductType.PIECE.name
                unit = "piece"

        return unit
    
    


# ===== TESTING =====
if __name__ == "__main__":
    cmdargs = sys.argv

    # Print it
    print(
        f"The total numbers of args passed to the script: {len(cmdargs)}, Args list: {cmdargs}")

