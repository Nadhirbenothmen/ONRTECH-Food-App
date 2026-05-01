import json
import re
import sys
from typing import Final, List, Optional, Tuple, override

from src.countries.france.carrefour.model import all_brands
from src.model.my_model import ProductType
from src.model.product import Nutrition
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


class ProductContentCarrefour:
    HALAL_PRESENCE: Final[List[str]] = ["halal"]
    BIO_PRESENCE: Final[List[str]] = ["bio"]
    VEGAN_PRESENCE: Final[List[str]] = ["vegan"]
    FRENCH_PRESENCE: Final[List[str]] = ["origine France", "provient de France", "provenant de l'agriculture biologique en France", "d'origine France",
                                         "Fabriqué en France", "élaboré en France", "Elaboré en France", "Origine : France",
                                         "cultivés en France", "cultivé en France", "cultivée en France",
                                         "fabriquées en France", "Fabriqués en France", "Fabriqué en France", "100% FRANCE", "de la France", "de France",
                                         "hauts france", "MADE IN FRANCE", "Farine de froment : France", "Fabriqué France",
                                         "Farine de blé France", "agriculture biologique en France", "NATURE DE FRANCE", "cultivés et surgelés en France",
                                         "fabriquée en Provence"]
    FRENCH_ABSENCE: Final[List[str]] = ["conditionnés en France",
                                        "conditionné en France", "conditionnées en France", "torréfié lentement en France"]

    LACTOSE_PRESENCE: Final[List[str]] = [", lactose", "lactosérum en poudre", "lactoserum en poudre", "lactose (de LAIT)", "LACTOSÉRUM (LAIT)", "contient du lactose",
                                          "protéines de lactoseruM", "extrait de lactosérum", "lactose (LAIT)", "LAIT en poudre entier", "LACTOSE et protéines de LAI"]
    LACTOSE_ABSENCE: Final[List[str]] = ["sans lactose", "aucun lactose",
                                         "si vous êtes intolérant(e) au lactose.", "convient aux intolérants au lactose"]
    FAT_ABSENCE: Final[List[str]] = [" 0% MG", " 0% de matière grasse",
                                     " 0% de MG", " 0% de mat gr", " 0% mat g", "Pauvre en matières grasses"]
    GMO_ABSENCE: Final[List[str]] = ["sans ogm", "Ne contient pas d'OGM", "OGM : Absence", "OGM 0,", "aucun ingrédient génétiquement modifié",
                                     "aucun de nos ingrédients n'a été maltraité par des OGM", "aucun ingrédient génétiquement modifié",
                                     "aucun ingrédient, additif ou arôme OGM"]
    ADDITIVE_ABSENCE: Final[List[str]] = ["sans additif", "ni additif", "ni d'additif", " 0% additif", "aucun additif", "aucun ajout d'additif",
                                          "aucun ingrédient, additif", "aucun conservateur, colorant ou autre additif"]
    DYE_ABSENCE: Final[List[str]] = ["sans colorant", "ni colorant", "sans arômes et colorant", "NI DE COLORANT", "aucun colorant", "aucun arôme artificiel, colorant",
                                     "ni de conservateurs et colorant", "sans arôme, colorant et conservateur", "Sans additifs, couleur", "aucun conservateur, colorant"]
    PRESERVATIVE_ABSENCE: Final[List[str]] = ["aucun ajout de conservateur", "sans conservateur", "ni conservateur", "pas de conservateur", "sans ajout de conservateur", "aucun conservateur", "aucun arôme artificiel, colorant, conservateur",
                                              "ni de conservateur", "sans arôme, colorant et conservateur", "aucun ajout d'additifs ou de conservateur", "aucun ajout de liants ou de conservateur"]
    GLUTEN_ABSENCE: Final[List[str]] = ["sans gluten", "ni gluten", "absence de gluten",
                                        "pas de gluten", "Dépourvu de gluten"]
    GLUTEN_PRESENCE: Final[List[str]] = ["gluten", "Traces de GLUTEN possibles", "contient de GLUTEN", "Peut contenir des traces de GLUTEN",
                                         "Traces éventuelles de GLUTEN", "Traces éventuelles de FRUITS A COQUE et de GLUTEN", "chapelure (dont GLUTEN)",
                                         "Allergènes :\nGluten", "Traces possibles d'arachide, de fruits à coque, de gluten", "Traces possibles d'arachides, de fruits à coques, de gluten",
                                         "Traces possibles de céleri, de gluten", "peut présenter des traces de GLUTEN", "Traces de LAIT et de GLUTEN",
                                         "Peut contenir : Autres FRUITS A COQUE,GLUTEN", "Allergènes : Gluten", "Traces de LAIT, d'ŒUF, de SOJA, de CELERI et de GLUTEN",
                                         "Présence possible de GLUTEN", "GLUTEN de BLE", "gluten de blé", "Peut contenir : FRUITS A COQUE, LAIT,GLUTEN",
                                         "Présence de GLUTEN", "Trace éventuelle de GLUTEN", "Traces éventuelles de produits à base de GLUTEN"]
    SUGAR_ABSENCE: Final[List[str]] = ["sans sucre", " 0% de sucre", "ne contient pas de sucres ajoutés", "sans adjonctions de sucre",
                                       "aucun sucre"]
    # sugar if < 0.9% ==> sugar free
    # pregnant if  description = non pasteurisé ou = cru ou = alcool ou Non Pasteurisé ou Non Pasteurisée ou Non Pasteurisés ou Non Pasteurisées ou inférieure à la pasteurisation
    INGREDIENTS_SUBSTRINGS: Final[List[str]] = ["Ingrédients biologiques", "de france", "de Meurthe-et-Moselle", "d'Equateur", "d'Occitanie", "de Provence", "de nouvelle-aquitaine", "de Suède", "d'Espagne", "préparation à base de", "présence enfonction de l'acidité des fruits", "issus de l'agriculture biologique", "produits issus de l'agriculture biologique naturellement sans gluten", "matières grasses végétales", "caramel", "voir les photos", "vierge extra", "lichette de jus de", "un petit extrait de", "un soupçon d'", "pincée extrait de", "une lichette d'extrait de", "un doigt de", "un peu de jus de", "un peu de bon", "graines de", "un filet de", "en purée", "mixée", "mixé", "de l'eau de", "écrasées", "un trait d'infusion de", "un trait d'", "une lichette de", "une lichette d'",
                                                "(jus de saison été)", "pressées", "jus de fruits à base de concentrés", "jus et purées de fruits à base de concentrés", "jus et purées de fruits à base de concentrés", "contient des sucres naturellement présents dans les fruits, comme tous les jus", "françaises", "une touché de", "une pincée de", "purée d'", "un morceau de", "une pointe d'extrait de", "antioxydant :", "antioxydant", "un zeste de", " et rien d'autre", "sans sucres ajoutés", "issu de l'agriculture biologique", "ingrédients issus de l'agriculture biologique", "un soupçon de", "une lichette de", "pressés", "pressée", "pressé", "presses", "ajoutées", "quelques", "un peu d'extrait de", "extrait de", "un peu d'", "un trait de", "mixées", "extrait de", "Jus de ", "Jus d'", "pulpe d'", "purée de ", "concentré de", "*", "colorant :", "colorant:", "acidifiant :", "acidifiant:", "stabilisant:", "stabilisant :", "concentré", "concentrée", "jus de saison été"]

    @classmethod
    def get_brand_from_title(cls, title: str) -> str:
        # load brand json file globally and search for brand
        # unknown products brands are considered as CARREFOUR brand.
        product_brand = "CARREFOUR"
        product_title_upper = title.upper()
        for brand in all_brands:
            if brand.upper() in product_title_upper:
                product_brand = brand
                print(f"product_brand: {product_brand}, product: {title}")
                break
        return product_brand.upper()

    @classmethod
    def get_freshness_days(cls, freshness_text: str) -> Optional[int]:
        """get number of freshness days \n
        :param freshness_text: accepted input format: ``' +5 jrs '`` or  ``' +5 sem '``
        """
        if freshness_text is None:
            return None

        list_of_ints = re.findall(r'\d+', freshness_text)
        freshness_value = None if list_of_ints is None or len(
            list_of_ints) == 0 else list_of_ints[0]
        if freshness_value is None:
            return None

        if 'sem' in freshness_text.lower():
            freshness_value = int(freshness_value) * \
                7 if freshness_value.isdigit() else None
            print(f"freshness_value2: {freshness_value}")
        elif 'jrs' in freshness_text.lower():
            freshness_value = freshness_value * \
                1 if freshness_value.isdigit() else freshness_value
        return freshness_value

    @classmethod
    def get_packaging_info(cls, product_pricing_unit: Optional[str]) -> tuple[str | None, str | None, float] | None:
        if not isinstance(product_pricing_unit, str):
            print(f"print2: {product_pricing_unit}")
            return (None, None, None)
        else:
            product_pricing_unit = product_pricing_unit.lower()

        # warning: another ProductType called "U"
        matter = ProductType.OTHER.name
        unit_of_mesure = "Kg"
        product_pricing_unit = product_pricing_unit if product_pricing_unit is not None else ''
        if "kilogramme" in product_pricing_unit or "kg" in product_pricing_unit:
            matter = ProductType.SUBSTANCE.name
            unit_of_mesure = "Kg"
            product_pricing_unit = product_pricing_unit.replace(
                "kilogramme", "").replace("kg", "").replace("g", "").replace("gr", "")
        elif "gramme" in product_pricing_unit or "g" in product_pricing_unit or "gr" in product_pricing_unit:
            matter = ProductType.SUBSTANCE.name
            product_pricing_unit = product_pricing_unit.replace(
                "g", "").replace("gr", "")
            unit_of_mesure = "g"

        elif product_pricing_unit.find("pièce") != -1 or product_pricing_unit.find("u") != -1 or product_pricing_unit.find("pce") != -1:
            matter = ProductType.PIECE.name
            product_pricing_unit = product_pricing_unit.replace(
                "pièce", "")
            unit_of_mesure = "piece"
        elif "l" in product_pricing_unit or "litre" in product_pricing_unit:
            matter = ProductType.LIQUID.name
            product_pricing_unit = product_pricing_unit.replace(
                "L", "").replace("litre", "")
            unit_of_mesure = "l"
        else:
            matter = ProductType.OTHER.name

        product_pricing_unit_all = re.findall(
            r"[-+]?\d*\.\d+|\d+", product_pricing_unit)
        product_pricing_unit = product_pricing_unit_all[0] if len(
            product_pricing_unit_all) > 0 else ""
        product_pricing_unit = float(product_pricing_unit) if product_pricing_unit else None
        print(f"unit_of_mesure: {unit_of_mesure}, matter: {matter}, product_pricing_unit: {product_pricing_unit}")
        return unit_of_mesure, matter, product_pricing_unit

    @classmethod
    def convert_nutrition_name(cls, nutrition_name):
        """Converts a French nutrition name to its English equivalent.

        Args:
            nutrition_name (str): The French name of a nutrition element.

        Returns:
            str: The English equivalent of the nutrition name, or None if not found.
        """

        # Define the dictionary for name mapping
        nutrition_name = {
            "valeur énergétique(kJ)": "energy_value(kJ)",
            "valeur énergétique (kcal)": "energy_value(kcal)",
            "matières grasses": "fats",
            "acides gras saturés": "of_which_saturates",
            "acides gras saturés": "saturated_fatty_acids",
            "Glucides": "carbohydrates",
            "glucides": "carbohydrates",
            "dont Sucres": "with_sugar",
            "dont sucres": "with_sugars",
            "sucres": "sugar",
            "Fibres alimentaires": "dietary_fiber",
            "fibres alimentaires": "dietary_fiber",
            "Protéines": "proteins",
            "protéines": "proteines",
            "Sel": "salt",
            "sel": "salt",
            "calcium": "calcium",
            "Vitamine D": "vitamin_D",
            "Fibre": "fiber",
            "Acide linoléique = LA": "Linoleic_Acid",
            "Acide alpha-linolénique = ALA": "Alpha_Linolenic_Acid",
            "sodium": "sodium",
            "Vitamine A": "vitamin_A",
            "Vitamine D": "vitamin_D",
            "Vitamine E": "vitamin_E",
            "Vitamine K": "vitamin_K",
            "Vitamine C": "vitamin_C",
            "Vitamine B6": "vitamin_B6",
            "vitamine B3": "vitamin_B3",
            "Thiamine": "thiamine",
            "Riboflavine": "riboflavine",
            "Niacine": "niacin",
            "Vitamine B6": "vitamin_B6",
            "Acide folique": "folic_Acid",
            "Vitamine B12": "vitamin_B12",
            "Biotine": "biotin",
            "Acide Pantothénique": "pantothenic_Acid",
            "Potassium": "potassium",
            "Phosphore": "phosphorus",
            "Fer": "iron",
            "zinc": "zinc",
            "iode": "iodine",
            "amidon": "starch",
            "magnésium": "magnesium",
            "Magnésium": "magnesium",
            "Lactose": "lactose",
            "oméga 3": "omega_3",
            "Dont acides gras mono-insaturés": "Including_monounsaturated_fatty_acids",
            "Dont acides gras polyinsaturés": "Including_polyunsaturated_fatty_acids",
            "acides gras mono-insaturés": "Monounsaturated_fatty_acids",
            "Unité énergétique": "energy_value(kJ)",
            "Valeur énergétique": "energy_value(kcal)",
            "Chlorure": "Chloride",
            "Magnésium": "Magnesium",
            "Cuivre": "Copper",
            "Fluorure": "Flouride",
            "Sélénium": "Selenium",
            "Choline": "Choline",
            "Inositol": "Inositol",
            "L-Carnitine": "LCarnitine",
            "FOS": "FOS",
            "GOS": "GOS",
            "3'Galactosyllactoses": "GAL",
            "Chlorure": "Chloride"
        }

        # Check if nutrition_name exists in the dictionary
        converted_name = nutrition_name.get(nutrition_name)

        # Return converted name or None if not found
        return converted_name


class NutritionContentCarrefour:
    '''
    irregular strange nutrition tables:
    https://www.carrefour.fr/p/tarte-au-maroilles-lebeau-3263240000354
    https://www.carrefour.fr/p/feta-bio-aop-hotos-5202425000374
    https://www.carrefour.fr/p/cassoulet-timo-3187420105823
    https://www.carrefour.fr/p/farine-de-sarrasin-bretagne-bio-paysans-d-ici-3760278860375
    https://www.carrefour.fr/p/pates-fraiches-tagliatelle-aux-oeufs-l-italie-des-pates-8005658003139
    https://www.carrefour.fr/p/yaourt-a-boire-multi-fruits-et-peche-gelee-royale-actimel-3033491216121
    https://www.carrefour.fr///p/sesames-decortiquees-seeberger-4008258509029
    https://www.carrefour.fr/p/cafe-soluble-chicoree-bio-leroux-3067140039540
    https://www.carrefour.fr/p/saucisson-gout-boeuf-piquant-halal-3459860005415
    '''
    ENERGY_VALUE_KJ_FINAL: Final[List[Tuple[str, int]]] = [("valeur énergétique kJ", 95), ("Unité énergétique", 95), ("Unité énergétique KJ", 95), ("kj", 95), ("energy_value_kJ", 95)]
    ENERGY_VALUE_KCAL_FINAL: Final[List[Tuple[str, int]]] = [("valeur énergétique kcal", 95), ("Valeur énergétique", 95), ("kcal", 95), ("energy_value_kcal", 95)]
    FATS_FINAL: Final[List[Tuple[str, int]]] = [("matières grasses", 95), ("Matieres grasses", 95), ("fats", 95)]
    # OF_WHICH_SATURATES_FINAL: Final[List[Tuple[str, int]]] = [("Dont acides gras saturés", 90), ("acides gras saturés", 90)]
    SATURATES_FINAL: Final[List[Tuple[str, int]]] = [("Dont acides gras saturés", 90), ("acides gras saturés", 90), ("saturates", 95), ("of_which_saturates", 95), ("Dont saturates", 90)]
    CARBOHYDRATES_FINAL: Final[str] = [("glucides", 90), ("carbohydrates", 90)]
    WITH_SUGAR_FINAL: Final[List[Tuple[str, int]]] = [("dont sucres", 95), ("with_sugars", 95), ("of_which_sugars", 90)]
    SUGARS_FINAL: Final[List[Tuple[str, int]]] = [("sucres", 95), ("sugars", 90), ("sugar", 90)]
    DIETARY_FIBER_FINAL: Final[List[Tuple[str, int]]] = [("fibres alimentaires", 95), ("dietary_fiber", 95)]
    PROTEINES_FINAL: Final[List[Tuple[str, int]]] = [("protéines", 90), ("Protéine", 90), ("PROTEINES", 90), ("Proteins", 90)]
    SALT_FINAL: Final[List[Tuple[str, int]]] = [("sel", 90), ("salt", 90)]
    CALCIUM_FINAL: Final[str] = "calcium"
    FIBER_FINAL: Final[List[Tuple[str, int]]] = [("fibre", 90), ("fiber", 90)]
    LINOLEIC_ACID_FINAL: Final[List[Tuple[str, int]]] = [("Acide linoléique = LA", 90), ("LINOLEIC_ACID", 90)]
    ALPHA_LINOLENIC_ACID_FINAL: Final[List[Tuple[str, int]]] = [("Acide alpha-linolénique = ALA", 90), ("ALPHA_LINOLENIC_ACID", 90)]
    SODIUM_FINAL: Final[str] = "sodium"
    POTASSIUM_FINAL: Final[str] = "Potassium"
    CHROMIUM_FINAL: Final[List[Tuple[str, int]]] = [("chromium", 90), ("chrome", 90)]
    PHOSPHORUS_FINAL: Final[List[Tuple[str, int]]] = [("Phosphore", 90), ("phosphorus", 90)]
    IRON_FINAL: Final[List[Tuple[str, int]]] = [("Fer", 95), ("iron", 90)]
    ZINC_FINAL: Final[str] = "zinc"
    IODINE_FINAL: Final[List[Tuple[str, int]]] = [("iode", 90), ("iodine", 90)]
    STARCH_FINAL: Final[List[Tuple[str, int]]] = [("amidon", 90), ("starch", 90)]
    MAGNESIUM_FINAL: Final[List[Tuple[str, int]]] = [("magnésium", 90), ("magnesium", 90)]
    LACTOSE_FINAL: Final[str] = "lactose"
    OMEGA_3_FINAL: Final[List[Tuple[str, int]]] = [("oméga 3", 90), ("omega 3", 90)]
    SATURATED_FATTY_ACIDS_FINAL: Final[List[Tuple[str, int]]] = [("acides gras saturés", 90), ("SATURATED_FATTY_ACIDS", 90)]
    MONOUNSATURATED_FATTY_ACIDS_FINAL: Final[List[Tuple[str, int]]] = [("acides gras mono-insaturés", 90), ("MONOUNSATURATED_FATTY_ACIDS", 90)]
    INCLUDING_MONOUNSATURATED_FATTY_ACIDS_FINAL: Final[List[Tuple[str, int]]] = [("Dont acides gras mono-insaturés", 90), ("INCLUDING_MONOUNSATURATED_FATTY_ACIDS", 90)]
    INCLUDING_POLYUNSATURATED_FATTY_ACIDS_FINAL: Final[List[Tuple[str, int]]] = [("Dont acides gras polyinsaturés", 90), ("INCLUDING_POLYUNSATURATED_FATTY_ACIDS", 90)]
    CHLORIDE_FINAL: Final[List[Tuple[str, int]]] = [("Chlorure", 90), ("chloride", 90)]
    COPPER_FINAL: Final[List[Tuple[str, int]]] = [("Cuivre", 90), ("copper", 90)]
    FLUORIDE_FINAL: Final[List[Tuple[str, int]]] = [("Fluorure", 90), ("FLUORIDE", 90)]
    SELENIUM_FINAL: Final[List[Tuple[str, int]]] = [("Sélénium", 85), ("sélenium", 85), ("selenium", 85)]
    CHOLINE_FINAL: Final[str] = "Choline"
    INOSITOL_FINAL: Final[str] = "Inositol"
    L_CARNITINE_FINAL: Final[List[Tuple[str, int]]] = [("L-Carnitine", 95), ("L_CARNITINE", 95)]
    FOS_FINAL: Final[str] = "FOS"
    GOS_FINAL: Final[str] = "GOS"
    GAL_FINAL: Final[List[Tuple[str, int]]] = [("galactosyllactoses", 95), ("GAL", 95)]
    MANAGANESE_FINAL: Final[List[Tuple[str, int]]] = [("manganese", 85), ("Manganèse", 85)]
    POLYOLS_FINAL: Final[List[Tuple[str, int]]] = [("polyols", 95), ("Dont polyols", 95)]
    VITAMINE_A: Final[List[Tuple[str, int]]] = [("vitamine A", 99), ("retinol", 90), ("A", 95), ("vitamin_a", 99), ("vitamine_a", 99)]
    VITAMINE_B1: Final[List[Tuple[str, int]]] = [("vitamine B1", 99), ("thiamine", 90), ("B1", 95), ("vitamin_b1", 99)]
    VITAMINE_B2: Final[List[Tuple[str, int]]] = [("vitamine B2", 99), ("Riboflavine", 90), ("B2", 95), ("vitamin_b2", 99)]
    VITAMINE_B3: Final[List[Tuple[str, int]]] = [("vitamine B3", 99), ("Niacine", 90), ("B3", 95), ("vitamin_b3", 99)]
    VITAMINE_B5: Final[List[Tuple[str, int]]] = [("vitamine B5", 99), ("Acide Pantothénique", 90), ("B5", 95), ("vitamin_b5", 99)]
    VITAMINE_B6: Final[List[Tuple[str, int]]] = [("vitamine B6", 99), ("Pyridoxine", 90), ("B6", 95), ("vitamin_b6", 99)]
    VITAMINE_B7: Final[List[Tuple[str, int]]] = [("vitamine B7", 99), ("Biotine", 90), ("B7", 95), ("vitamin_b7", 99)]
    VITAMINE_B9: Final[List[Tuple[str, int]]] = [("vitamine B9", 99), ("Acide folique", 90), ("B9", 95), ("vitamin_b9", 99)]
    VITAMINE_B12: Final[List[Tuple[str, int]]] = [("vitamine B12", 99), ("Cobalamine", 90), ("B12", 95), ("vitamin_b12", 99)]
    VITAMINE_C: Final[List[Tuple[str, int]]] = [("vitamine C", 99), ("acide ascorbique", 90), ("C", 95), ("vitamin_c", 99)]
    VITAMINE_D: Final[List[Tuple[str, int]]] = [("vitamine D", 99), ("cholécalciférol", 90), ("D", 95), ("vitamin_d", 99)]
    VITAMINE_E: Final[List[Tuple[str, int]]] = [("vitamine E", 99), ("tocophérol", 90), ("E", 95), ("vitamin_e", 99)]
    VITAMINE_K: Final[List[Tuple[str, int]]] = [("vitamine K", 99), ("phylloquinone", 90), ("K", 95), ("vitamin_k", 99)]

class NutritionCarrefour(Nutrition):
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
            # energy
            if are_string_exist_in_list(key, NutritionContentCarrefour.ENERGY_VALUE_KJ_FINAL):
                value = remove_substring_and_clean(value, "kj")
                energies.kj = convert_to_float(value)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.ENERGY_VALUE_KCAL_FINAL):
                value = remove_substring_and_clean(value, "kcal")
                energies.kcal = convert_to_float(value)

            # macronutrients
            elif are_string_exist_in_list(key, NutritionContentCarrefour.FATS_FINAL):
                fats.fats = convert_to_target_unit(value, fats_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.SATURATES_FINAL):
                fats.saturates = convert_to_target_unit(value, fats_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.CARBOHYDRATES_FINAL):
                carbohydrates.carbohydrates = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.WITH_SUGAR_FINAL):
                carbohydrates.of_which_sugars = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.SUGARS_FINAL):
                carbohydrates.sugars = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.DIETARY_FIBER_FINAL):
                carbohydrates.dietary_fiber = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.STARCH_FINAL):
                carbohydrates.starch = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_strings_equal(key, NutritionContentCarrefour.LACTOSE_FINAL, 90):
                carbohydrates.lactose = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.GAL_FINAL):
                carbohydrates.gal = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.FIBER_FINAL):
                carbohydrates.fiber = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.POLYOLS_FINAL):
                carbohydrates.polyols = convert_to_target_unit(value, carbohydrates_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.PROTEINES_FINAL):
                proteins.proteins = convert_to_target_unit(value, proteins_measurement)

            # Minerals
            elif are_strings_equal(key, NutritionContentCarrefour.SODIUM_FINAL, 90):
                minerals.sodium = convert_to_target_unit(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.SALT_FINAL):
                minerals.salt = convert_to_target_unit(value, minerals_measurement)
            elif are_strings_equal(key, NutritionContentCarrefour.CALCIUM_FINAL, 90):
                minerals.calcium = convert_to_target_unit(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.MANAGANESE_FINAL):
                minerals.manganese = convert_to_target_unit(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.MAGNESIUM_FINAL):
                minerals.magnesium = convert_to_target_unit(value, minerals_measurement)
            elif are_strings_equal(key, NutritionContentCarrefour.POTASSIUM_FINAL, 90):
                minerals.potassium = convert_to_target_unit(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.CHROMIUM_FINAL):
                minerals.chromium = convert_to_target_unit(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.PHOSPHORUS_FINAL):
                minerals.phosphorus = convert_to_target_unit(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.IRON_FINAL):
                minerals.iron = convert_to_target_unit(value, minerals_measurement)
            elif are_strings_equal(key, NutritionContentCarrefour.ZINC_FINAL, 90):
                minerals.zinc = convert_to_target_unit(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.IODINE_FINAL):
                minerals.iodine = convert_to_target_unit(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.CHLORIDE_FINAL):
                minerals.chloride = convert_to_target_unit(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.COPPER_FINAL):
                minerals.copper = convert_to_target_unit(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.FLUORIDE_FINAL):
                minerals.fluoride = convert_to_target_unit(value, minerals_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.SELENIUM_FINAL):
                minerals.selenium = convert_to_target_unit(value, minerals_measurement)

            # FattyAcids
            elif are_string_exist_in_list(key, NutritionContentCarrefour.LINOLEIC_ACID_FINAL):
                fatty_acids.linoleic_acid = convert_to_target_unit(value, fatty_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.ALPHA_LINOLENIC_ACID_FINAL):
                fatty_acids.alpha_linolenic_acid = convert_to_target_unit(value, fatty_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.OMEGA_3_FINAL):
                fatty_acids.omega_3 = convert_to_target_unit(value, fatty_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.SATURATED_FATTY_ACIDS_FINAL):
                fatty_acids.saturated_fatty_acids = convert_to_target_unit(value, fatty_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.MONOUNSATURATED_FATTY_ACIDS_FINAL):
                fatty_acids.monounsaturated_fatty_acids = convert_to_target_unit(value, fatty_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.INCLUDING_MONOUNSATURATED_FATTY_ACIDS_FINAL):
                fatty_acids.including_monounsaturated_fatty_acids = convert_to_target_unit(value, fatty_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.INCLUDING_POLYUNSATURATED_FATTY_ACIDS_FINAL):
                fatty_acids.including_polyunsaturated_fatty_acids = convert_to_target_unit(value, fatty_measurement)

            # Essential Nutrients or Vitamin-like
            elif are_strings_equal(key, NutritionContentCarrefour.CHOLINE_FINAL, 90):
                vitaminLikes.choline = convert_to_target_unit(value, vitaminLikes_measurement)
            elif are_strings_equal(key, NutritionContentCarrefour.INOSITOL_FINAL, 90):
                vitaminLikes.inositol = convert_to_target_unit(value, vitaminLikes_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.L_CARNITINE_FINAL):
                vitaminLikes.lcarnitine = convert_to_target_unit(value, vitaminLikes_measurement)
            elif are_strings_equal(key, NutritionContentCarrefour.FOS_FINAL, 90):
                vitaminLikes.fos = convert_to_target_unit(value, vitaminLikes_measurement)
            elif are_strings_equal(key, NutritionContentCarrefour.GOS_FINAL, 90):
                vitaminLikes.gos = convert_to_target_unit(value, vitaminLikes_measurement)

            # Vitamins: classified by order of exitence in food products
            elif are_string_exist_in_list(key, NutritionContentCarrefour.VITAMINE_B1):
                vitamins.vitamin_b1 = convert_to_target_unit(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.VITAMINE_B2):
                vitamins.vitamin_b2 = convert_to_target_unit(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.VITAMINE_B3):
                vitamins.vitamin_b3 = convert_to_target_unit(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.VITAMINE_B5):
                vitamins.vitamin_b5 = convert_to_target_unit(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.VITAMINE_B6):
                vitamins.vitamin_b6 = convert_to_target_unit(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.VITAMINE_B7):
                vitamins.vitamin_b7 = convert_to_target_unit(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.VITAMINE_B9):
                vitamins.vitamin_b9 = convert_to_target_unit(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.VITAMINE_B12):
                vitamins.vitamin_b12 = convert_to_target_unit(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.VITAMINE_C):
                vitamins.vitamin_c = convert_to_target_unit(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.VITAMINE_A):
                vitamins.vitamin_a = convert_to_target_unit(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.VITAMINE_E):
                vitamins.vitamin_e = convert_to_target_unit(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.VITAMINE_K):
                vitamins.vitamin_k = convert_to_target_unit(value, vitamins_measurement)
            elif are_string_exist_in_list(key, NutritionContentCarrefour.VITAMINE_D):
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
        """Extract the last integer from the given text."""
        print(f"Extract the last integer from: {text}")

        # Define the regex pattern
        pattern = r'(?<=\/\s)(\d+)(?=\s?(?:mL|g))'

        # Search for the pattern in the input text
        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            # Return the integer value as an int
            return match.group(1)
        else:
            return None

        # Example usage
        inputs = [
            "0.1 g / 100 mL",
            "0.8 g / 49 g",
            "0.9 ml / 55 ml"
        ]

    @classmethod
    def process_value(cls, last_value: str, value: str) -> str:
        """Multiply the first number in the value by (100 / last_value) if last_value is present."""
        substring_for_g = "/ " + last_value + " g"
        substring_for_ml = "/ " + last_value + " ml"
        last_value = float(last_value)
        message = ("value:" + str(value))
        if substring_for_g in value:
            match = re.search(r'(\d+(?:\.\d+)?)', value)
            if match:
                number = float(match.group(1))
                doubled_number: float = number * (100/last_value)
                # Format the doubled number to 2 decimal places
                formatted_number = f"{doubled_number:.3f}"
                formatted_number = f"{float(formatted_number):.10f}".rstrip('0').rstrip(
                    '.')  # Format with enough decimal places to handle cases

                output = re.sub(r'(\d+(?:\.\d+)?)', str(formatted_number),
                                value, 1).replace(substring_for_g, "").strip()  # .replace(substring_for_g, "/ 100 g")
                message += f", output: {output}"
                print(message)
                return output
        elif substring_for_ml in value:
            match = re.search(r'(\d+(?:\.\d+)?)', value)
            if match:
                number = float(match.group(1))
                doubled_number: float = number * (100/last_value)
                # Format the doubled number to 2 decimal places
                formatted_number = f"{doubled_number:.3f}"
                formatted_number = f"{float(formatted_number):.10f}".rstrip('0').rstrip(
                    '.')  # Format with enough decimal places to handle cases

                output = re.sub(r'(\d+(?:\.\d+)?)', str(formatted_number),
                                value, 1).replace(substring_for_ml, "").strip()  # .replace(substring_for_ml, "/ 100 ml")
                message += f", output: {output}"
                print(message)
                return output
        print(message)
        return value

    @classmethod
    def compute_nutrition_values_per_100_g_or_ml(cls, nutrition: dict) -> dict:
        '''
        Modify the nutrition values
        '''
        print(f"Modify the nutrition values...")
        if not isinstance(nutrition, dict):
            return None
        for key, value in nutrition.items():
            # if value is already an int, this means that this value is already proessed in the past
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
        # Step 1: Read the JSON file
        print(f"Step 1: Read the JSON file")
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Step 2: Loop over each item in the list (each product with 'ean')
        print(f"Step 2: Loop over each item in the list")
        for product in data:
            evolutions = product.get('evolutions', [])

            # Step 3: Process each evolution
            print(f"Step 3: Process each evolution")
            for evolution in evolutions:
                if 'nutrition' in evolution:
                    nutrition = evolution['nutrition']
                    # Step 4: Modify the nutrition values
                    nutrition = cls.compute_nutrition_values_per_100_g_or_ml(
                        nutrition=nutrition)
                    nutrition = cls.convert_dict_to_nutrition_object(nutrition)
                    evolution['nutrition'] = nutrition

        # Step 5: Save the modified data back to the same JSON file
        print(f"Step 5: Save the modified data back to the same JSON file")
        file_path = file_path if overwrite else file_path.replace(".json", "_2.json")
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4,
                      ensure_ascii=False,
                      allow_nan=False,
                      default=lambda o: dict(
                          (key, value) for key, value in o.__dict__.items() if value is not None))
        print(f"Nutrition values updated and saved.")

    @classmethod
    def modify_all_nutrition_values(cls):
        folder_path = "src/countries/france/carrefour/robots/products/viandes-et-poissons"
        json_files = get_all_files_inside_given_folder(folder_path)
        for file_path in json_files:
            print(file_path)
            Nutrition.modify_nutrition_in_file(file_path)


# Custom JSON encoder
def custom_serializer(obj):
    if isinstance(obj, Nutrition):
        return obj.__dict__  # Converts the object's attributes to a dictionary
    raise TypeError(f"Object of type {
                    obj.__class__.__name__} is not JSON serializable")


# Exemples
nutrition_name = {
    "valeur énergétique(kJ)": "13",
    "valeur énergétique (kcal)": "12",
    "matières grasses": "30",
    "acides gras saturés": "45",
    "acides gras saturés": "90",
    "Glucides": "0",
    "glucides": "9.7",
    "dont Sucres": "0.03",
    "dont sucres": "with_sugars",
    "sucres": "sugar",
    "Fibres alimentaires": "dietary_fiber",
    "fibres alimentaires": "dietary_fiber",
    "Protéines": "proteins",
    "protéines": "proteines",
    "Sel": "salt",
    "sel": "salt",
    "calcium": "calcium",
    "Vitamine D": "vitamin_D",
    "Fibre": "fiber",
    "Acide linoléique = LA": "Linoleic_Acid",
    "Acide alpha-linolénique = ALA": "Alpha_Linolenic_Acid",
    "sodium": "sodium",
    "Vitamine A": "vitamin_A",
    "Vitamine D": "vitamin_D",
    "Vitamine E": "vitamin_E",
    "Vitamine K": "vitamin_K",
    "Vitamine C": "vitamin_C",
    "Vitamine B6": "vitamin_B6",
    "vitamine B3": "vitamin_B3",
    "Thiamine": "thiamine",
    "Riboflavine": "riboflavine",
    "Niacine": "niacin",
    "Vitamine B6": "vitamin_B6",
    "Acide folique": "folic_Acid",
    "Vitamine B12": "vitamin_B12",
    "Biotine": "biotin",
    "Acide Pantothénique": "pantothenic_Acid",
    "Potassium": "potassium",
    "Phosphore": "phosphorus",
    "Fer": "iron",
    "zinc": "zinc",
            "iode": "iodine",
            "amidon": "starch",
            "magnésium": "magnesium",
            "Magnésium": "magnesium",
            "Lactose": "lactose",
            "oméga 3": "omega_3",
            "Dont acides gras mono-insaturés": "Including_monounsaturated_fatty_acids",
            "Dont acides gras polyinsaturés": "Including_polyunsaturated_fatty_acids",
            "acides gras mono-insaturés": "Monounsaturated_fatty_acids",
            "Unité énergétique": "energy_value(kJ)",
            "Valeur énergétique": "energy_value(kcal)",
            "Chlorure": "Chloride",
            "Magnésium": "Magnesium",
            "Cuivre": "Copper",
            "Fluorure": "Flouride",
            "Sélénium": "Selenium",
            "Choline": "Choline",
            "Inositol": "Inositol",
            "L-Carnitine": "LCarnitine",
            "FOS": "FOS",
            "GOS": "GOS",
            "3'Galactosyllactoses": "GAL",
            "Chlorure": "Chloride"
}
product_8445290624918 = {
    "valeur énergétique (kJ)": "69 kJ / 100 g",
    "valeur énergétique (kcal)": "16 kcal / 100 g",
    "matières grasses": "0.2 g / 100 g",
    "acides gras saturés": "0.1 g / 100 g",
    "glucides": "2 g / 100 g",
    "sucres": "1.3 g / 100 g",
    "fibres alimentaires": "1.3 g / 100 g",
    "protéines": "1 g / 100 g",
    "sel": "0.03 g / 100 g"
}

CONVERT_NUTRITION_DICT_TO_OBJECT = "CONVERT_NUTRITION_DICT_TO_OBJECT"

if __name__ == "__main__":
    cmdargs = sys.argv

    # Print it
    print(f"The total numbers of args passed to the script: {len(cmdargs)}, Args list: {cmdargs}")
    json_file_path = ""
    if CONVERT_NUTRITION_DICT_TO_OBJECT in cmdargs:
        index = cmdargs.index(CONVERT_NUTRITION_DICT_TO_OBJECT)
        json_file_path = str(cmdargs[index + 1]) if len(cmdargs) >= index + 2 else None
        print(f"fallback to hard coded file path")
        json_file_path = json_file_path if json_file_path else "src/countries/france/carrefour/robots/products/bio_ecologie/1boissons_detailed_24_03_08_20_38.json"
        NutritionCarrefour.modify_nutrition_in_file(file_path=json_file_path, overwrite=False)

        
    # res = Nutrition.convert_dict_to_nutrition_Object(
    #     product_8445290624918)
    # json_object = json.dumps(res, ensure_ascii=False,
    #                          default=custom_serializer)
    # print(f"inital dict: {product_8445290624918}")
    # print(f"json_object: {json_object}")
    # Nutrition.modify_nutrition_values(json_file_path)
    # NutritionCarrefour.modify_nutrition_in_file(file_path=json_file_path)

    # g = json_objectV2 = json.dumps(product_8445290624918,
    #                                default=lambda o: dict(
    #                                    (key, value) for key, value in o.__dict__.items() if value is not None),
    #                                indent=4,
    #                                allow_nan=False,
    #                                ensure_ascii=False)
    # write_output_to_file(data=g, file_name= json_file_path.replace(".json", "2.json"),
    #                      path_includes_in_file_name=True, include_seconds_in_date=False, extension='.json')

