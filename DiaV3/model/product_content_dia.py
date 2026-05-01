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
from src.countries.spain.DiaV3.robots import webdriverInstance

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
)


class ProductContentDia(object): 

    HALAL_PRESENCE: Final [List[str]] = ["halal", "Halal" , "HALAL", "kasher" , "kosher"]

    BIO_PRESENCE: Final [List[str]] = ["Naturalmente", "producción ecológica", "ECOLÓGICO", "eco","biológicas", "ecológico" ,"agricultura ecológica","ecológica" ,"Organic", "BIO" , 
                                       "ecológicos" , "ecológicas" , "biológica" , "Eco"]
    
    VEGAN_PRESENCE: Final [List[str]] = ["100% vegetal", "vegano", "Vegetánea", "végétalien" , "Vegetal" , "Vegano" ]

    SPANISH_PRESENCE:Final [List[str]] = ["Origen de la leche: España", "Producido en España", "Origen de la leche España", "España" ," Origen: España", "Origen de la leche España","ganaderos españoles", "ORIGEN DE LA LECHE: ESPAÑA", "de origen español" 
                                         ,"ORIGEN: ESPAÑA","Origen: ESPAÑA", "Origen Nacional" ,"País de Ordeño: España","receta española", "Proviene de la agricultura española",
                                           "País de transformación: España" ,"agricultura española ","Originarias"]
    
    SPANICH_ABSENCE:Final [List[str]] = ["UE","italiano","Origen: Francia","Italia","Murcia","" "HOLANDA", "Francia", "Harina acondicionada de trigo", "República Checa"]
    
    
    LACTOSE_PRESENCE:Final [List[str]] = ["lactosuero", "suero lácteo en polvo" , "L-Casei", "sales minerales lácteas" , "lactosa",
                                           "cultivos de ácido láctico", "LÁCTEOS" ,
                                           "CONTIENE LACTOBACILLUS CASEI", "aroma (contiene lactosa)","LECHE Y SUS DERIVADOS (INCLUIDA LA LACTOSA)",
                                           "sólidos lácteos", 
                                           ]
    LACTOSE_ABSENCE:Final [List[str]] = [ "LACTASA", "sin lactosa", "leche pasteurizada sin lactosa", "elaborado sin lactosa" ,"sin lacosa", "Sin lácteos",
                                         "Leche en polvo desnatada sin lactosa","enzima lactasa" ,"Naturalmente sin lactosa" ,
                                          "Sin lactosa"]
    
    GLUTEN_PRESENCE: Final [List[str]] = ["Contiene gluten", "Puede contener granos de cereal (gluten)" ,"gluten", "gluten de trigo", "Puede contener trazas de gluten", "gluten de trigo", "PASTA ALIMENTICIA DE SÉMOLA DE TRIGO DURO (GLUTEN)",
                                           "Semola de trigo duro (100%)(gluten)","pan rallado (contiene gluten)","Harina integral de avena (contiene gluten)",
                                           "puede contener CEREALES QUE CONTIENEN GLUTEN","Contiene gluten","Harina de trigo (gluten)",
                                           "Puede contener trazas de cereales con gluten" ,"Puede contener trazas de cereales (gluten menos de 5ppm)" ,
                                           "Puede contener trazas de cereales que contienen gluten" ,"Harina de TRIGO (GLUTEN)"]
    
    GLUTEN_ABSENCE: Final [List[str]] = ["Sin gluten", "sin gluten 100%" , "sin gluten","pan rallado sin gluten", "no contiene gluten"]

    FAT_ABSENCE:Final [List[str]] = ["0% M.G", "" "sin grasas añadidas", "sin grasas" ,"Sin grasas añadidas" ,"Sin grasa añadida" ,"Sin grasa" ,"Sin grasas"]

    SUGAR_ABSENCE:Final [List[str]] = ["0% azúcares", "zero","no tiene azúcares añadidos","ni azúcares añadidos", "Sin azucares añadidos" , "sin azúcares" ,"Sin azúcares añadidos" ,"Sin azúcares" ,"Sin azúcares añadidos" ,"Sin azúcar añadido" ,"Sin azúcares añadidos" ,"sin azúcares añadidos", "sin azúcares añadidos"]

    ADDITIVE_ABSENCE:Final [List[str]] = ["Sin conservantes",""  "BIO 100% ", "sin conservantes" ,"Sin ningún tipo de aditivo","sin aditivos" ,"natural"]

    DYE_ABSENCE:Final [List[str]] = ["Sin colorantes","aroma natural","aroma natural de vainilla", "ARÔME NATUREL", "Sin aromas" ]

    GMO_ABSENCE:Final [List[str]] = ["sin OGM", "sin OGM" ,"Sin OGM" ,"Sin organismos modificados genéticamente" ,"Sin organismos genéticamente modificados",]

    PRESERVATIVE_ABSENCE:Final [List[str]] = ["ni conservantes","sin conservantes", "sin conservante" ,"Sin conservantes" ,"Sin conservante" ,"Sin conservantes añadidos"]

    INGREDIENTS_SUBSTRINGS: Final[List[str]] = [
    "ingredientes ecológicos","ver las fotos","y nada más","un poco de bueno","sin azúcares añadidos","productos procedentes de la agricultura ecológica naturalmente sin gluten","procedente de la agricultura ecológica","ingredientes procedentes de la agricultura ecológica",
    "presencia según la acidez de las frutas","contiene azúcares naturalmente presentes en las frutas, como todos los jugos",
    "de francia", "de meurthe-et-moselle", "de ecuador", "de occitania","de provenza", "de nueva aquitania", "de suecia", "de españa", "francesas",
    "un chorrito de jugo de","un pequeño extracto de","una pizca de extracto de","una gota de extracto de","un dedo de","un poco de jugo de",
    "un hilo de","un toque de infusión de","una ralladura de","un trozo de","algunas", "colorante :", "colorante:","acidificante :", "acidificante:","estabilizante:", "estabilizante :","concentrado", "concentrada","*",
    ]

    
    # --- Brand constants ---
    FORBIDDEN_SUFFIX: Final[set[str]] = {
        "brik", "botella", "spray", "pack", "lata", "bolsa", "caja", "frasco",
        "sobre", "bandeja", "capsulas", "cápsulas", "ud", "uds",
        "unidad", "unidades", "paquete"
    }
    KNOWN_BRANDS: Final[set[str]] = {
        "McCain", "Nestlé", "Maggi", "Don Simón", "Granini", "Juver", "Pascual",
        "La Española", "La Cocina De Senen", "Dia", "Ramblers", "Sidul"
    }

    # --- Brand functions ---
    @classmethod
    def clean_brand(cls, candidate: str) -> str:
        """
        Nettoie une marque extraite :
        - enlève 'de Dia' (ou d'autres enseignes) à la fin
        - enlève mots interdits (spray, brik, botella, paquete...)
        - met en Title Case
        """
        candidate = candidate.strip()

        # 🔹 Supprimer "de Dia", "de Carrefour", etc.
        candidate = re.sub(r"\s+de\s+(dia|carrefour|eroski)\b", "", candidate, flags=re.IGNORECASE)

        parts = candidate.split()

        # 🔹 Supprimer tous les suffixes interdits, même au milieu
        parts = [p for p in parts if p.lower() not in cls.FORBIDDEN_SUFFIX]

        brand = " ".join(parts).title() if parts else "Dia"

        # 🔹 Si la marque nettoyée correspond à une marque connue, on respecte la casse d'origine
        for known in cls.KNOWN_BRANDS:
            if known.lower() == brand.lower():
                return known

        return brand

    @classmethod
    def extract_brand_from_title(cls, title: str) -> str:
        if not title:
            return "Dia"

        words = title.strip().split()
        if len(words) <= 1:
            return "Dia"

        # Supprimer le premier mot du titre
        title_wo_first = " ".join(words[1:])

        forbidden_units = {"kg", "g", "gr", "gramos", "ml", "cl", "l", "litros", "litro"}
        clean_title = " ".join(
            [w for w in title_wo_first.split() if w.lower() not in forbidden_units]
        )

        # 1. Marques composées (Majuscule suivie d’un autre mot)
        match = re.findall(
            r"\b([A-ZÁÉÍÓÚÑÜ][\wáéíóúñü]+(?:\s+[A-Za-zÁÉÍÓÚÑÜáéíóúñü]+)+)\b",
            clean_title,
        )
        if match:
            return cls.clean_brand(match[-1].strip())

        # 2. Marques simples capitalisées
        match = re.findall(r"\b([A-ZÁÉÍÓÚÑÜ][a-záéíóúñü]+)\b", clean_title)
        if match:
            return cls.clean_brand(match[-1].strip())

        # 3. Marques tout en majuscules
        match = re.findall(r"\b([A-ZÁÉÍÓÚÑÜ]{2,}(?:\s+[A-ZÁÉÍÓÚÑÜ]{2,})*)\b", clean_title)
        if match:
            return cls.clean_brand(match[-1].strip())

        # 4. Vérifier les marques connues
        for brand in cls.KNOWN_BRANDS:
            if brand.lower() in title.lower():
                return brand

        return "Dia"


    
    @staticmethod
    def extract_full_format_from_title(title: str, index: Optional[int] = None) -> Optional[str]:
        title = title.lower().replace("×", "x").replace("*", "x").replace(",", ".").replace("·", " ").strip()

        # Mots descriptifs fréquents avant la quantité
        descriptors = r"(pack|vaso|paquete|lote|bandeja|botella|lata|unidad|uds\.?|unidades|piezas|bolsa|frasco|tarro|caja|botellita|envase|rollo|tubo|sobre|brik|pieza|malla|tarrina)"

        # Liste des patterns de formats à tester dans l'ordre (du plus spécifique au plus simple)
        patterns = [
            # ex: "pack 6 x 125 g", "pack de 6 uds. de 25 g", "6 uds x 25 g", "6 x 25 g"
            rf'\b{descriptors}?\s*\d+\s*x\s*\d+[.,]?\d*\s*(g|gr|kg|ml|l|cl|mg|ug|µg)\b',
            rf'\b{descriptors}?\s*pack\s*de\s*\d+\s*uds?\.?\s*de\s*\d+[.,]?\d*\s*(g|gr|kg|ml|l|cl|mg|ug|µg)\b',
            rf'\b{descriptors}?\s*\d+\s*uds?\.?\s*x\s*\d+[.,]?\d*\s*(g|gr|kg|ml|l|cl|mg|ug|µg)\b',
            rf'\b{descriptors}?\s*\d+\s*x\s*\d+[.,]?\d*\s*(g|gr|kg|ml|l|cl|mg|ug|µg)\b',

            # ex: "bandeja 900 g", "lata 330 ml", "botella 1 l", "pack vaso 200 ml"
            rf'\b{descriptors}\s*\d+[.,]?\d*\s*(g|gr|kg|ml|l|cl|mg|ug|µg)\b',

            # ex: "900 g", "1 kg", "500 ml", "25 cl"
            r'\b\d+[.,]?\d*\s*(g|gr|kg|ml|l|cl|mg|ug|µg)\b',

            # ex: "6 unidades", "4 piezas"
            rf'\b\d+\s*{descriptors}s?\b',

            # fallback très simple : nombre seul avec unité (même sans mot descriptif)
            r'\b\d+[.,]?\d*\s*(g|gr|kg|ml|l|cl|mg|ug|µg)\b',
        ]

        for pattern in patterns:
            match = re.search(pattern, title)
            if match:
                result = match.group(0).strip()
                prefix = f"[{index}] " if index is not None else ""
                print(f"{prefix}FORMAT extrait: {result}")
                return result

        if index is not None:
            print(f"[{index}] FORMAT non trouvé")
        else:
            print("FORMAT non trouvé")
        return None
    
        
    @classmethod
    def get_packaging_info(cls, product_pricing_unit: Optional[str]) -> tuple[Optional[str], Optional[str], Optional[float]]:
        if not isinstance(product_pricing_unit, str):
            return None, None, None

        original_text = product_pricing_unit
        product_pricing_unit = product_pricing_unit.lower().replace(",", ".").strip()

        matter = ProductType.OTHER.name
        unit_of_measure = None

        # ordre très important ici !
        if any(kw in product_pricing_unit for kw in ["kilogramo", "kg", "kilo"]):
            matter = ProductType.SUBSTANCE.name
            unit_of_measure = "kg"
        elif any(kw in product_pricing_unit for kw in ["gramo", "gr", "g"]):
            matter = ProductType.SUBSTANCE.name
            unit_of_measure = "g"
        elif any(kw in product_pricing_unit for kw in ["litro", "litros", "l"]):
            matter = ProductType.LIQUID.name
            unit_of_measure = "l"
        elif any(kw in product_pricing_unit for kw in ["pièce", "u", "pce", "unidad"]):
            matter = ProductType.PIECE.name
            unit_of_measure = "piece"

        # Extraction de la valeur numérique
        numbers = re.findall(r"[-+]?\d*\.\d+|\d+", product_pricing_unit)
        value = float(numbers[0]) if numbers else None

        print(f"[DEBUG] packaging: '{original_text}' → unit: {unit_of_measure}, matter: {matter}, value: {value}")
        return unit_of_measure, matter, value

    
    @staticmethod
    def get_label_and_origin(driver: webdriver) -> tuple[Optional[Label], Optional[str]]:
        """
        Méthode désactivée pour ignorer toute interaction avec les icônes SVG.
        Retourne un objet Label vide et aucune origine.
        """
        return Label(), None
    
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
    def enrich_nested_nutrition(nutrition: dict) -> dict:
        """
        Adapter le dictionnaire nested de nutrition pour s'assurer que tous les champs requis sont présents.
        """
        def safe_float(val):
            try:
                if isinstance(val, str):
                    val = val.replace(",", ".").split()[0]
                return float(val)
            except:
                return 0.0

        # Ajouter fiber depuis carbohydrates
        if "carbohydrates" in nutrition and "dietary_fiber" in nutrition["carbohydrates"]:
            fiber_raw = nutrition["carbohydrates"]["dietary_fiber"]
            nutrition["fiber"] = safe_float(fiber_raw)

        # Initialiser minerals si absent
        nutrition.setdefault("minerals", {})

        # Ajouter salt à 0 s’il n'existe pas
        if "salt" not in nutrition["minerals"]:
            nutrition["minerals"]["salt"] = 0

        # Ajouter fruits_percentage à 0 si absent
        nutrition.setdefault("fruits_percentage", 0)

        return nutrition


    @staticmethod
    def calculate_nutriscore_from_nested(nutrition: dict) -> str:
        try:
            # 1) Récupération des valeurs nutritionnelles
            energy_kj   = nutrition.get("energies", {}).get("kj", 0)
            carbs       = nutrition.get("carbohydrates", {})
            sugars_g    = carbs.get("of_which_sugars", carbs.get("sugars", 0))
            satfat_g    = nutrition.get("fats", {}).get("saturates", 0)
            fiber_g     = nutrition.get("fiber", 0)
            protein_g   = nutrition.get("proteins", {}).get("proteins", 0)
            salt_mg     = nutrition.get("minerals", {}).get("salt", 0)
            fruits_percentage = nutrition.get("fruits_percentage", 0)

            # 🔎 Conversion si nécessaire
            def to_float(v): return float(str(v).replace(",", ".").split()[0]) if isinstance(v, str) else float(v or 0)

            energy_kj   = to_float(energy_kj)
            sugars_g    = to_float(sugars_g)
            satfat_g    = to_float(satfat_g)
            fiber_g     = to_float(fiber_g)
            protein_g   = to_float(protein_g)
            salt_mg     = to_float(salt_mg)
            fruits_percentage = to_float(fruits_percentage)

            # 2) Calcul points négatifs
            pts_energy = min(int(energy_kj / 335), 10)
            pts_sugar  = min(int(sugars_g  / 4.5), 10)
            pts_satfat = min(int(satfat_g  / 1), 10)
            pts_salt   = min(int((salt_mg / 1000.0) / 0.09), 10)

            neg = pts_energy + pts_sugar + pts_satfat + pts_salt

            # 3) Points positifs
            pts_fiber   = min(int(fiber_g   / 0.9), 5)
            pts_protein = min(int(protein_g / 1.6), 5)

            if fruits_percentage >= 80:
                pts_fruits = 5
            elif fruits_percentage >= 60:
                pts_fruits = 2
            elif fruits_percentage >= 40:
                pts_fruits = 1
            else:
                pts_fruits = 0

            pos = pts_fiber + pts_protein + pts_fruits

            # 4) Score total
            score = neg - pos

            print(f"🧮 NutriScore → neg={neg} (energy={pts_energy}, sugar={pts_sugar}, satfat={pts_satfat}, salt={pts_salt}), "
                f"pos={pos} (fiber={pts_fiber}, protein={pts_protein}, fruits={pts_fruits}) → score={score}")

            # 5) Attribution lettre
            if score <= -1: return "A"
            elif score <= 2: return "B"
            elif score <= 10: return "C"
            elif score <= 18: return "D"
            else: return "E"

        except Exception as e:
            print(f"❌ Exception NutriScore: {e}")
            return "N/A"




    
class NutritionContentDia:
        
        ENERGY_VALUE_KJ_FINAL: Final[List[Tuple[str, int]]] = [("Valor energético (Kj)", 95), ("Unidad energética", 95), ("Unidad energética KJ", 95), ("kj", 95), ("energy_value_kJ", 95)]
        ENERGY_VALUE_KCAL_FINAL: Final[List[Tuple[str, int]]] = [("Valor energético (Kcal)", 95), ("Valor energético", 95), ("kcal", 95), ("energy_value_kcal", 95)]
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
                "Valor energético (KJ)": "energy_value(kJ)",
                "Valor energético (Kcal)": "energy_value(kcal)",
                "Grasas": "fats",
                "de las cuales saturadas": "saturated_fatty_acids",
                "Hidratos de carbono": "carbohydrates",
                "glucides": "carbohydrates",
                "de los cuales azúcares": "sugar",
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

class NutritionDia(Nutrition):
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

            # ✅ Si la valeur est déjà un dict → énergie
            if isinstance(value, dict):
                if key.lower() == "energy":
                    energies.kj = value.get("kj")
                    energies.kcal = value.get("kcal")
                continue
            # energy
            if are_string_exist_in_list(key, NutritionContentDia.ENERGY_VALUE_KJ_FINAL):
                value = remove_substring_and_clean(value, "kj")
                energies.kj = convert_to_float(value)
            elif are_string_exist_in_list(key, NutritionContentDia.ENERGY_VALUE_KCAL_FINAL):
                value = remove_substring_and_clean(value, "kcal")
                energies.kcal = convert_to_float(value)

            # macronutrients
            elif are_string_exist_in_list(key, NutritionContentDia.FATS_FINAL):
                fats.fats = convert_to_target_unit(value, fats_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.SATURATES_FINAL):
                fats.saturates = convert_to_target_unit(value, fats_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.CARBOHYDRATES_FINAL):
                carbohydrates.carbohydrates = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.WITH_SUGAR_FINAL):
                carbohydrates.of_which_sugars = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.SUGARS_FINAL):
                carbohydrates.sugars = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.DIETARY_FIBER_FINAL):
                carbohydrates.dietary_fiber = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.STARCH_FINAL):
                carbohydrates.starch = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_strings_equal(key, NutritionContentDia.LACTOSE_FINAL, 90):
                carbohydrates.lactose = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.GAL_FINAL):
                carbohydrates.gal = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.FIBER_FINAL):
                carbohydrates.fiber = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.POLYOLS_FINAL):
                carbohydrates.polyols = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.PROTEINES_FINAL):
                proteins.proteins = convert_to_target_unit(value, proteins_measurement)

            # Minerals
            elif are_strings_equal(key, NutritionContentDia.SODIUM_FINAL, 90):
                minerals.sodium = convert_to_target_unit(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.SALT_FINAL):
                minerals.salt = convert_to_target_unit(value, minerals_measurement)
            elif are_strings_equal(key, NutritionContentDia.CALCIUM_FINAL, 90):
                minerals.calcium = convert_to_target_unit(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.MANAGANESE_FINAL):
                minerals.manganese = convert_to_target_unit(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.MAGNESIUM_FINAL):
                minerals.magnesium = convert_to_target_unit(value, minerals_measurement)
            elif are_strings_equal(key, NutritionContentDia.POTASSIUM_FINAL, 90):
                minerals.potassium = convert_to_target_unit(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.CHROMIUM_FINAL):
                minerals.chromium = convert_to_target_unit(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.PHOSPHORUS_FINAL):
                minerals.phosphorus = convert_to_target_unit(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.IRON_FINAL):
                minerals.iron = convert_to_target_unit(value, minerals_measurement)
            elif are_strings_equal(key, NutritionContentDia.ZINC_FINAL, 90):
                minerals.zinc = convert_to_target_unit(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.IODINE_FINAL):
                minerals.iodine = convert_to_target_unit(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.CHLORIDE_FINAL):
                minerals.chloride = convert_to_target_unit(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.COPPER_FINAL):
                minerals.copper = convert_to_target_unit(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.FLUORIDE_FINAL):
                minerals.fluoride = convert_to_target_unit(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.SELENIUM_FINAL):
                minerals.selenium = convert_to_target_unit(value, minerals_measurement)

            # FattyAcids
            elif are_string_exist_in_list(key, NutritionContentDia.LINOLEIC_ACID_FINAL):
                fatty_acids.linoleic_acid = convert_to_target_unit(value, fatty_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.ALPHA_LINOLENIC_ACID_FINAL):
                fatty_acids.alpha_linolenic_acid = convert_to_target_unit(value, fatty_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.OMEGA_3_FINAL):
                fatty_acids.omega_3 = convert_to_target_unit(value, fatty_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.SATURATED_FATTY_ACIDS_FINAL):
                fatty_acids.saturated_fatty_acids = convert_to_target_unit(value, fatty_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.MONOUNSATURATED_FATTY_ACIDS_FINAL):
                fatty_acids.monounsaturated_fatty_acids = convert_to_target_unit(value, fatty_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.INCLUDING_MONOUNSATURATED_FATTY_ACIDS_FINAL):
                fatty_acids.including_monounsaturated_fatty_acids = convert_to_target_unit(value, fatty_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.INCLUDING_POLYUNSATURATED_FATTY_ACIDS_FINAL):
                fatty_acids.including_polyunsaturated_fatty_acids = convert_to_target_unit(value, fatty_measurement)

            # Essential Nutrients or Vitamin-like
            elif are_strings_equal(key, NutritionContentDia.CHOLINE_FINAL, 90):
                vitaminLikes.choline = convert_to_target_unit(value, vitaminLikes_measurement)
            elif are_strings_equal(key, NutritionContentDia.INOSITOL_FINAL, 90):
                vitaminLikes.inositol = convert_to_target_unit(value, vitaminLikes_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.L_CARNITINE_FINAL):
                vitaminLikes.lcarnitine = convert_to_target_unit(value, vitaminLikes_measurement)
            elif are_strings_equal(key, NutritionContentDia.FOS_FINAL, 90):
                vitaminLikes.fos = convert_to_target_unit(value, vitaminLikes_measurement)
            elif are_strings_equal(key, NutritionContentDia.GOS_FINAL, 90):
                vitaminLikes.gos = convert_to_target_unit(value, vitaminLikes_measurement)

            # Vitamins: classified by order of exitence in food products
            elif are_string_exist_in_list(key, NutritionContentDia.VITAMINE_B1):
                vitamins.vitamin_b1 = convert_to_target_unit(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.VITAMINE_B2):
                vitamins.vitamin_b2 = convert_to_target_unit(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.VITAMINE_B3):
                vitamins.vitamin_b3 = convert_to_target_unit(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.VITAMINE_B5):
                vitamins.vitamin_b5 = convert_to_target_unit(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.VITAMINE_B6):
                vitamins.vitamin_b6 = convert_to_target_unit(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.VITAMINE_B7):
                vitamins.vitamin_b7 = convert_to_target_unit(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.VITAMINE_B9):
                vitamins.vitamin_b9 = convert_to_target_unit(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.VITAMINE_B12):
                vitamins.vitamin_b12 = convert_to_target_unit(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.VITAMINE_C):
                vitamins.vitamin_c = convert_to_target_unit(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.VITAMINE_A):
                vitamins.vitamin_a = convert_to_target_unit(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.VITAMINE_E):
                vitamins.vitamin_e = convert_to_target_unit(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.VITAMINE_K):
                vitamins.vitamin_k = convert_to_target_unit(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentDia.VITAMINE_D):
                vitamins.vitamin_d = convert_to_target_unit(value, vitamins_measurement)

            else:
                print(f"key not found: {key}")
                nutrition.unknown = nutrition.unknown if nutrition.unknown is dict else dict()
                nutrition.unknown[key] = convert_to_target_unit(value, "mg") if nutrition.unknown is not dict else dict(
                )

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
    

    import re

    def normalize_nutrition_str(v: str) -> tuple[str, str]:
        """
        Nettoie une chaîne de valeur nutritionnelle comme '0,7g' ou '12mg'
        et retourne ('0.7', 'g') ou ('12', 'mg')
        """
        if isinstance(v, str):
            v = v.replace(",", ".").strip()
            v = re.sub(r"(?<=\d)(?=[a-zA-Zµ])", " ", v)  # Ajoute un espace entre nombre et unité
            parts = v.split()
            if len(parts) == 1:
                return parts[0], "g"  # fallback par défaut
            return parts[0], parts[1]
        return str(v), "g"  # fallback si ce n’est pas une chaîne

        def convert_to_target_unit(v: str | float | int, target_unit="mg"):
            """
            Convertit une valeur nutritionnelle textuelle vers l'unité cible, ex: mg
            """
            try:
                if isinstance(v, dict):  # pour l'énergie {'kj': ..., 'kcal': ...}
                    return v

                if isinstance(v, (int, float)):
                    return round(float(v), 4)

                value_str, current_unit = normalize_nutrition_str(v)

                if not re.match(r"^\d+(\.\d+)?$", value_str):
                    return None

                value = float(value_str)

                # Conversion
                if current_unit.lower() in ["mg", "mg."]:
                    value_in_mg = value
                elif current_unit.lower() in ["g", "gr", "g."]:
                    value_in_mg = value * 1000
                elif current_unit.lower() in ["µg", "mcg"]:
                    value_in_mg = value / 1000
                else:
                    value_in_mg = value  # fallback si unité inconnue

                # Retour selon unité cible
                if target_unit == "mg":
                    return round(value_in_mg, 4)
                elif target_unit == "g":
                    return round(value_in_mg / 1000, 4)
                elif target_unit == "µg":
                    return round(value_in_mg * 1000, 4)
                else:
                    return round(value, 4)

            except Exception as e:
                print(f"❌ Erreur lors de la conversion en objet Nutrition: {e}")
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
                label_dict['Sin gluten'] = False
            if "halal" in category:
                label_dict['halal'] = True
            if "lactose_presence" in category:
                label_dict['lactosa'] = True
            if "lactose_absent" in category:
                label_dict['lactasa'] = False

            if label_dict:
                label_dicts.append(label_dict)

        unique_label_dicts = [dict(t) for t in {tuple(d.items()) for d in label_dicts}]
        unique_labels = [Label(**label_dict) for label_dict in unique_label_dicts]
        return ProductContentDia.keep_first_element(unique_labels)

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

