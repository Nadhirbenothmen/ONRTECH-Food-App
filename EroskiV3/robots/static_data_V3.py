import logging
import os
from statistics import mean
import sys
from turtle import back
from typing import Final, List, Optional, Union

from typing_extensions import override

from src.model.static_category_aisle import StaticAisle, StaticCategory
from src.utils.my_utils import get_filename_from_filepath

sys.path.append('src')
current_file_directory = os.path.dirname(os.path.abspath(__file__))

FOLDER_PATH: Final[str] = os.path.join(
    current_file_directory, "products")

class CategoryParser:
    @classmethod
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        raise NameError("fatal error, this method should be overriden")

    @staticmethod
    def category_path() -> str:
        raise NameError("fatal error, this method should be overriden")

#Feeding

class EroskiFeedingOilVinegarSaltFlourAndBreadcrumbsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Feeding_Oil_vinegar_salt_flour_and_breadcrumbs")

    SUNFLOWER_OIL = StaticAisle(name="Sunflower oil",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059988-aceite-vinagre-sal-harina-y-pan-rallado/2059992-aceite-de-girasol/",
                                     original_file_uri=os.path.join(category_path(), "Sunflower_oil.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sunflower_oil_detailed.json"))
    
    INTENSE_OLIVE_OIL = StaticAisle(name="Intense olive oil", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059988-aceite-vinagre-sal-harina-y-pan-rallado/2059991-aceite-de-oliva-intenso/",
                                     original_file_uri=os.path.join(category_path(), "Intense_olive_oil.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Intense_olive_oil_detailed.json"))
    
    MILD_OLIVE_OIL = StaticAisle(name="Mild olive oil",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059988-aceite-vinagre-sal-harina-y-pan-rallado/2059990-aceite-de-oliva-suave/",
                                     original_file_uri=os.path.join(category_path(), "Mild_olive_oil.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mild_olive_oil_detailed.json"))
    
    VIRGIN_OLIVE_OIL = StaticAisle(name="Virgin olive oil",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059988-aceite-vinagre-sal-harina-y-pan-rallado/2059989-aceite-de-oliva-virgen/",
                                     original_file_uri=os.path.join(category_path(), "Virgin_olive_oil.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Virgin_olive_oil_detailed.json"))
    
    OTHER_OILS = StaticAisle(name="Other oils",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059988-aceite-vinagre-sal-harina-y-pan-rallado/2059993-otros-aceites/",
                                     original_file_uri=os.path.join(category_path(), "Other_oils.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_oils_detailed.json"))
    
    FLOUR = StaticAisle(name="Flour",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059988-aceite-vinagre-sal-harina-y-pan-rallado/2059998-harina/",
                                     original_file_uri=os.path.join(category_path(), "Flour.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Flour_detailed.json"))
    
    BREADCRUMBS = StaticAisle(name="Breadcrumbs",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059988-aceite-vinagre-sal-harina-y-pan-rallado/2060000-pastillas-caldo/",
                                     original_file_uri=os.path.join(category_path(), "Breadcrumbs.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Breadcrumbs_detailed.json"))
    
    BROTH_CUBES = StaticAisle(name="Broth cubes",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059988-aceite-vinagre-sal-harina-y-pan-rallado/2059989-aceite-de-oliva-virgen/",
                                     original_file_uri=os.path.join(category_path(), "Broth_cubes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Broth_cubes_detailed.json"))
    
    SALT = StaticAisle(name="Salt",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059988-aceite-vinagre-sal-harina-y-pan-rallado/2059996-sal/",
                                     original_file_uri=os.path.join(category_path(), "Salt.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Salt_detailed.json"))
    
    SPECIAL_VINEGARS = StaticAisle(name="Special vinegars",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059988-aceite-vinagre-sal-harina-y-pan-rallado/2059994-vinagres-especiales/",
                                     original_file_uri=os.path.join(category_path(), "Special_vinegars.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Special_vinegars_detailed.json"))
    
    VINEGAR = StaticAisle(name="Vinegar",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059988-aceite-vinagre-sal-harina-y-pan-rallado/2059995-vinagre/",
                                     original_file_uri=os.path.join(category_path(), "Vinegar.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vinegar_detailed.json"))
    

    aisles: Final[List[StaticAisle]] = [SUNFLOWER_OIL, INTENSE_OLIVE_OIL, MILD_OLIVE_OIL, VIRGIN_OLIVE_OIL, OTHER_OILS, FLOUR, BREADCRUMBS, BROTH_CUBES, SALT, SPECIAL_VINEGARS, VINEGAR]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "SUNFLOWER_OIL":
                    aisles = [cls.SUNFLOWER_OIL]
                case "INTENSE_OLIVE_OIL":
                    aisles = [cls.INTENSE_OLIVE_OIL]
                case "MILD_OLIVE_OIL":
                    aisles = [cls.MILD_OLIVE_OIL]
                case "VIRGIN_OLIVE_OIL":
                    aisles = [cls.VIRGIN_OLIVE_OIL]
                case "OTHER_OILS":
                    aisles = [cls.OTHER_OILS]
                case "FLOUR":
                    aisles = [cls.FLOUR]
                case "BREADCRUMBS":
                    aisles = [cls.BREADCRUMBS]
                case "BROTH_CUBES":
                    aisles = [cls.BROTH_CUBES]
                case "SALT":
                    aisles = [cls.SALT]
                case "SPECIAL_VINEGARS":
                    aisles = [cls.SPECIAL_VINEGARS]
                case "VINEGAR":
                    aisles = [cls.VINEGAR]
        return aisles
    
class EroskiFeedingOlivesAndPicklesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Feeding_Olives_and_pickles")

    SPECIAL_OLIVES = StaticAisle(name="Special olives",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060067-aceitunas-y-encurtidos/2060071-aceitunas-especiales/",
                                     original_file_uri=os.path.join(category_path(), "Special_olives.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Special_olives_detailed.json"))
    
    BLACK_OLIVES = StaticAisle(name="black olives", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060067-aceitunas-y-encurtidos/2060070-aceitunas-negras/",
                                     original_file_uri=os.path.join(category_path(), "black_olives.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "black_olives_oil_detailed.json"))
    
    STUFFED_OLIVES = StaticAisle(name="Stuffed Olives",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060067-aceitunas-y-encurtidos/2060068-aceitunas-rellenas/",
                                     original_file_uri=os.path.join(category_path(), "Stuffed_Olives.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Stuffed_Olives_detailed.json"))
    
    GREEN_OLIVES = StaticAisle(name="green olives",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060067-aceitunas-y-encurtidos/2060069-aceitunas-verdes/",
                                     original_file_uri=os.path.join(category_path(), "green_olives.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "green_olives_detailed.json"))
    
    BANDERILLAS_AND_COCKTAIL = StaticAisle(name="Banderillas and cocktail",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060067-aceitunas-y-encurtidos/2060073-banderillas-y-cocktail/",
                                     original_file_uri=os.path.join(category_path(), "Banderillas_and_cocktail.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Banderillas_and_cocktail_detailed.json"))
    
    CHILLIES_CAPERS_AND_OTHERS = StaticAisle(name="Chillies, capers and others",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060067-aceitunas-y-encurtidos/2060074-guindillas-alcaparras-y-otros/",
                                     original_file_uri=os.path.join(category_path(), "Chillies_capers_and_others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chillies_capers_and_others_detailed.json"))
    
    PICKLES_AND_CHIVES = StaticAisle(name="Pickles and chives",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060067-aceitunas-y-encurtidos/2060072-pepinillos-y-cebolletas/",
                                     original_file_uri=os.path.join(category_path(), "Pickles_and_chives.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pickles_and_chives_detailed.json"))
    
    OTHER_TRADITIONAL_PICKLES = StaticAisle(name="Other traditional pickles",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060067-aceitunas-y-encurtidos/2060075-otros-encurtidos-tradicionales/",
                                     original_file_uri=os.path.join(category_path(), "Other_traditional_pickles.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_traditional_pickles_detailed.json"))
    
   

    aisles: Final[List[StaticAisle]] = [SPECIAL_OLIVES, BLACK_OLIVES, STUFFED_OLIVES, GREEN_OLIVES, BANDERILLAS_AND_COCKTAIL, CHILLIES_CAPERS_AND_OTHERS, PICKLES_AND_CHIVES, OTHER_TRADITIONAL_PICKLES]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "SPECIAL_OLIVES":
                    aisles = [cls.SPECIAL_OLIVES]
                case "BLACK_OLIVES":
                    aisles = [cls.BLACK_OLIVES]
                case "STUFFED_OLIVES":
                    aisles = [cls.STUFFED_OLIVES]
                case "GREEN_OLIVES":
                    aisles = [cls.GREEN_OLIVES]
                case "BANDERILLAS_AND_COCKTAIL":
                    aisles = [cls.BANDERILLAS_AND_COCKTAIL]
                case "CHILLIES_CAPERS_AND_OTHERS":
                    aisles = [cls.CHILLIES_CAPERS_AND_OTHERS]
                case "PICKLES_AND_CHIVES":
                    aisles = [cls.PICKLES_AND_CHIVES]
                case "OTHER_TRADITIONAL_PICKLES":
                    aisles = [cls.OTHER_TRADITIONAL_PICKLES]
                
        return aisles
    
class EroskiFeedingCannedFishAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Feeding_Canned_fish")

    CLAMS_RAZOR_CLAMS_AND_OTHERS = StaticAisle(name="Clams, razor clams and others",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060015-conservas-de-pescado/2060025-almejas-navajas-y-otros/",
                                     original_file_uri=os.path.join(category_path(), "Clams_razor_clams_and_others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Clams_razor_clams_and_others_detailed.json"))
    
    TUNA_OIL = StaticAisle(name="Tuna oil", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060015-conservas-de-pescado/2060016-atun-aceite/",
                                     original_file_uri=os.path.join(category_path(), "Tuna_oil.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tuna_oil_detailed.json"))
    
    MARINATED_TUNA_AND_BONITO = StaticAisle(name="Marinated tuna and bonito",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060015-conservas-de-pescado/2060019-atun-y-bonito-escabeche/",
                                     original_file_uri=os.path.join(category_path(), "Marinated_tuna_and_bonito.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Marinated_tuna_and_bonito_detailed.json"))
    
    NATURAL_TUNA_AND_BONITO = StaticAisle(name="Natural tuna and bonito",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060015-conservas-de-pescado/2060018-atun-y-bonito-natural/",
                                     original_file_uri=os.path.join(category_path(), "Natural_tuna_and_bonito.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Natural_tuna_and_bonito_detailed.json"))
    
    NICE_OIL = StaticAisle(name="Nice oil",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060015-conservas-de-pescado/2060017-bonito-aceite/",
                                     original_file_uri=os.path.join(category_path(), "Nice_oil.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Nice_oil_detailed.json"))
    
    BONITO_AND_TUNA_BELLY = StaticAisle(name="Bonito and tuna belly",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060015-conservas-de-pescado/2060020-ventresca-de-bonito-y-atun/",
                                     original_file_uri=os.path.join(category_path(), "Bonito_and_tuna_belly.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Bonito_and_tuna_belly_detailed.json"))
    
    COCKLES = StaticAisle(name="Cockles",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060015-conservas-de-pescado/2060024-berberechos/",
                                     original_file_uri=os.path.join(category_path(), "Cockles.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cockles_detailed.json"))
    
    MACKEREL = StaticAisle(name="Mackerel",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060015-conservas-de-pescado/2060027-caballa/",
                                     original_file_uri=os.path.join(category_path(), "Mackerel.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mackerel_detailed.json"))
    
    SQUID_OCTOPUS_AND_CUTTLEFISH = StaticAisle(name="Squid, octopus and cuttlefish",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060015-conservas-de-pescado/2060026-calamar-pulpo-y-chipiron/",
                                     original_file_uri=os.path.join(category_path(), "Squid_octopus_and_cuttlefish.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Squid_octopus_and_cuttlefish_detailed.json"))
    
    MUSSEL = StaticAisle(name="Mussel",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060015-conservas-de-pescado/2060022-mejillon/",
                                     original_file_uri=os.path.join(category_path(), "Mussel.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mussel_detailed.json"))
    
    SARDINE_AND_PILCHARDLES = StaticAisle(name="Sardine and pilchard",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060015-conservas-de-pescado/2060023-sardina-y-sardinilla/",
                                     original_file_uri=os.path.join(category_path(), "Sardine_and_pilchard.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sardine_and_pilchard_detailed.json"))
    
    OTHER_PRESERVES = StaticAisle(name="Other preserves",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060015-conservas-de-pescado/2060028-otras-conservas/",
                                     original_file_uri=os.path.join(category_path(), "Other_preserves.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_preserves_detailed.json"))
    
   

    aisles: Final[List[StaticAisle]] = [CLAMS_RAZOR_CLAMS_AND_OTHERS, TUNA_OIL, MARINATED_TUNA_AND_BONITO, NATURAL_TUNA_AND_BONITO, NICE_OIL, BONITO_AND_TUNA_BELLY, COCKLES, MACKEREL, SQUID_OCTOPUS_AND_CUTTLEFISH, MUSSEL, SARDINE_AND_PILCHARDLES, OTHER_PRESERVES]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "CLAMS_RAZOR_CLAMS_AND_OTHERS":
                    aisles = [cls.CLAMS_RAZOR_CLAMS_AND_OTHERS]
                case "TUNA_OIL":
                    aisles = [cls.TUNA_OIL]
                case "MARINATED_TUNA_AND_BONITO":
                    aisles = [cls.MARINATED_TUNA_AND_BONITO]
                case "NATURAL_TUNA_AND_BONITO":
                    aisles = [cls.NATURAL_TUNA_AND_BONITO]
                case "NICE_OIL":
                    aisles = [cls.NICE_OIL]
                case "BONITO_AND_TUNA_BELLY":
                    aisles = [cls.BONITO_AND_TUNA_BELLY]
                case "COCKLES":
                    aisles = [cls.COCKLES]
                case "MACKEREL":
                    aisles = [cls.MACKEREL]
                case "SQUID_OCTOPUS_AND_CUTTLEFISH":
                    aisles = [cls.SQUID_OCTOPUS_AND_CUTTLEFISH]
                case "MUSSEL":
                    aisles = [cls.MUSSEL]
                case "SARDINE_AND_PILCHARDLES":
                    aisles = [cls.SARDINE_AND_PILCHARDLES]
                case "OTHER_PRESERVES":
                    aisles = [cls.OTHER_PRESERVES]
                
        return aisles
    
class EroskiFeedingPreservedVegetablesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Feeding_Preserved_vegetables")

    ARTICHOKES_AND_VEGETABLES = StaticAisle(name="Artichokes and vegetables",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060001-conservas-vegetales/2060009-alcachofas-y-menestras/",
                                     original_file_uri=os.path.join(category_path(), "Artichokes_and_vegetables.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Artichokes_and_vegetables_detailed.json"))
    
    MUSHROOMS_AND_TOADSTOOLS = StaticAisle(name="Mushrooms and toadstools", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060001-conservas-vegetales/2060011-champinones-y-setas/",
                                     original_file_uri=os.path.join(category_path(), "Mushrooms_and_toadstools.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mushrooms_and_toadstools_detailed.json"))
    
    PRESERVED_FRUIT = StaticAisle(name="Preserved fruit",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060001-conservas-vegetales/2060014-conservas-fruta/",
                                     original_file_uri=os.path.join(category_path(), "Preserved_fruit.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Preserved_fruit_detailed.json"))
    
    ASPARAGUS = StaticAisle(name="Asparagus",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060001-conservas-vegetales/2060006-esparragos/",
                                     original_file_uri=os.path.join(category_path(), "Asparagus.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Asparagus_detailed.json"))
    
    SPINACH_CHARD_AND_OTHERS = StaticAisle(name="Spinach, chard and others",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060001-conservas-vegetales/2060010-espinacas-acelgas-y-otros/",
                                     original_file_uri=os.path.join(category_path(), "Spinach_chard_and_others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Spinach_chard_and_others_detailed.json"))
    
    PEAS_AND_CORN = StaticAisle(name="Peas and corn",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060001-conservas-vegetales/2060008-guisantes-y-maiz/",
                                     original_file_uri=os.path.join(category_path(), "Peas_and_corn.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Peas_and_corn_detailed.json"))
    
    RED_PEPPERS_OTHERS = StaticAisle(name="Red peppers, others",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060001-conservas-vegetales/2060005-pimientos-rojos-otros/",
                                     original_file_uri=os.path.join(category_path(), "Red_peppers_others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Red_peppers_others_detailed.json"))
    
    RED_PIQUILLO_PEPPERS = StaticAisle(name="Red piquillo peppers",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060001-conservas-vegetales/2060004-pimientos-rojos-piquillo/",
                                     original_file_uri=os.path.join(category_path(), "Red_piquillo_peppers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Red_piquillo_peppers_detailed.json"))
    
    FRIED_TOMATO = StaticAisle(name="Fried tomato",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060001-conservas-vegetales/2060002-tomate-frito/",
                                     original_file_uri=os.path.join(category_path(), "Fried_tomato.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fried_tomato_detailed.json"))
    
    NATURAL_TOMATO = StaticAisle(name="Natural tomato",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060001-conservas-vegetales/2060003-tomate-natural/",
                                     original_file_uri=os.path.join(category_path(), "Natural_tomato.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Natural_tomato_detailed.json"))
    
    VEGETABLE_SALAD = StaticAisle(name="Vegetable salad",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060001-conservas-vegetales/2060012-vegetales-ensalada/",
                                     original_file_uri=os.path.join(category_path(), "Vegetable_salad.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vegetable_salad_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [ARTICHOKES_AND_VEGETABLES, MUSHROOMS_AND_TOADSTOOLS, PRESERVED_FRUIT, ASPARAGUS, SPINACH_CHARD_AND_OTHERS, PEAS_AND_CORN, RED_PEPPERS_OTHERS,RED_PIQUILLO_PEPPERS,FRIED_TOMATO, NATURAL_TOMATO, VEGETABLE_SALAD]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "ARTICHOKES_AND_VEGETABLES":
                    aisles = [cls.ARTICHOKES_AND_VEGETABLES]
                case "MUSHROOMS_AND_TOADSTOOLS":
                    aisles = [cls.MUSHROOMS_AND_TOADSTOOLS]
                case "PRESERVED_FRUIT":
                    aisles = [cls.PRESERVED_FRUIT]
                case "ASPARAGUS":
                    aisles = [cls.ASPARAGUS]
                case "SPINACH_CHARD_AND_OTHERS":
                    aisles = [cls.SPINACH_CHARD_AND_OTHERS]
                case "PEAS_AND_CORN":
                    aisles = [cls.PEAS_AND_CORN]
                case "RED_PEPPERS_OTHERS":
                    aisles = [cls.RED_PEPPERS_OTHERS]
                case "RED_PIQUILLO_PEPPERS":
                    aisles = [cls.RED_PIQUILLO_PEPPERS]
                case "FRIED_TOMATO":
                    aisles = [cls.FRIED_TOMATO]
                case "NATURAL_TOMATO":
                    aisles = [cls.NATURAL_TOMATO]
                case "VEGETABLE_SALAD":
                    aisles = [cls.VEGETABLE_SALAD]
                
                
        return aisles
    
class EroskiFeedingNutsAndSnacksAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Feeding_Nuts_and_snacks")

    ALMONDS_AND_HAZELNUTS = StaticAisle(name="Almonds and hazelnuts",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060076-frutos-secos-patatas-y-snacks/2060081-almendras-y-avellanas/",
                                     original_file_uri=os.path.join(category_path(), "Almonds_and_hazelnuts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Almonds_and_hazelnuts_detailed.json"))
    
    PEANUTS_CORN_AND_COCKTAIL = StaticAisle(name="Peanuts, corn and cocktail", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060076-frutos-secos-patatas-y-snacks/2060080-cacahuetesmaiz-y-coktail/",
                                     original_file_uri=os.path.join(category_path(), "Peanuts_corn_and_cocktail.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Peanuts_corn_and_cocktail_detailed.json"))
    
    DRIED_FRUITS = StaticAisle(name="Dried fruits",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060076-frutos-secos-patatas-y-snacks/2060083-frutas-desecadas/",
                                     original_file_uri=os.path.join(category_path(), "Dried_fruits.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Dried_fruits_detailed.json"))
    
    NUTS_AND_OTHER_DRIED_FRUITS = StaticAisle(name="Nuts and other dried fruits",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060076-frutos-secos-patatas-y-snacks/2060082-nueces-y-otros-frutos-secos/",
                                     original_file_uri=os.path.join(category_path(), "Nuts_and_other_dried_fruits.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Nuts_and_other_dried_fruits_detailed.json"))
    
    TUBE_POTATOES = StaticAisle(name="Tube potatoes",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060076-frutos-secos-patatas-y-snacks/2060092-patatas-de-tubo/",
                                     original_file_uri=os.path.join(category_path(), "Tube_potatoes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tube_potatoes_detailed.json"))
    
    LIGHT_POTATOES = StaticAisle(name="Light potatoes",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060076-frutos-secos-patatas-y-snacks/2060089-patatas-light/",
                                     original_file_uri=os.path.join(category_path(), "Light_potatoes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Light_potatoes_detailed.json"))
    
    SMOOTH_FLAVORED_POTATOES = StaticAisle(name="Smooth flavored potatoes",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060076-frutos-secos-patatas-y-snacks/2060091-patatas-lisas-sabor/",
                                     original_file_uri=os.path.join(category_path(), "Smooth_flavored_potatoes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Smooth_flavored_potatoes_detailed.json"))
    
    TRADITIONAL_SMOOTH_POTATOES = StaticAisle(name="Traditional smooth potatoes",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060076-frutos-secos-patatas-y-snacks/2060088-patatas-lisas-tradicionales/",
                                     original_file_uri=os.path.join(category_path(), "Traditional_smooth_potatoes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Traditional_smooth_potatoes_detailed.json"))
    
    WAVY_FLAVORED_POTATOES = StaticAisle(name="Wavy flavored potatoes",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060076-frutos-secos-patatas-y-snacks/2060093-patatas-onduladas-sabores/",
                                     original_file_uri=os.path.join(category_path(), "Wavy_flavored_potatoes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Wavy_flavored_potatoes_detailed.json"))
    
    TRADITIONAL_WAVY_POTATOES = StaticAisle(name="Traditional wavy potatoes",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060076-frutos-secos-patatas-y-snacks/2060090-patatas-onduladas-tradicionales/",
                                     original_file_uri=os.path.join(category_path(), "Traditional_wavy_potatoes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Traditional_wavy_potatoes_detailed.json"))
    
    PIPES = StaticAisle(name="Pipes",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060076-frutos-secos-patatas-y-snacks/2060077-pipas/",
                                     original_file_uri=os.path.join(category_path(), "Pipes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pipes_detailed.json"))
    
    PISTACHIOS_AND_CASHEWS = StaticAisle(name="Pistachios and cashews",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060076-frutos-secos-patatas-y-snacks/2060079-pistachos-y-anacardos/",
                                     original_file_uri=os.path.join(category_path(), "Pistachios_and_cashews.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pistachios_and_cashews_detailed.json"))
    
    SNACKS_AND_OTHER_APPETIZERS = StaticAisle(name="Snacks and other appetizers",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060076-frutos-secos-patatas-y-snacks/2060094-snack-y-otros-aperitivos/",
                                     original_file_uri=os.path.join(category_path(), "Snacks_and_other_appetizers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Snacks_and_other_appetizers_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [ALMONDS_AND_HAZELNUTS, PEANUTS_CORN_AND_COCKTAIL, DRIED_FRUITS, NUTS_AND_OTHER_DRIED_FRUITS, TUBE_POTATOES, LIGHT_POTATOES, SMOOTH_FLAVORED_POTATOES, TRADITIONAL_SMOOTH_POTATOES, WAVY_FLAVORED_POTATOES, TRADITIONAL_WAVY_POTATOES, PIPES, PISTACHIOS_AND_CASHEWS, SNACKS_AND_OTHER_APPETIZERS]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "ALMONDS_AND_HAZELNUTS":
                    aisles = [cls.ALMONDS_AND_HAZELNUTS]
                case "PEANUTS_CORN_AND_COCKTAIL":
                    aisles = [cls.PEANUTS_CORN_AND_COCKTAIL]
                case "DRIED_FRUITS":
                    aisles = [cls.DRIED_FRUITS]
                case "NUTS_AND_OTHER_DRIED_FRUITS":
                    aisles = [cls.NUTS_AND_OTHER_DRIED_FRUITS]
                case "TUBE_POTATOES":
                    aisles = [cls.TUBE_POTATOES]
                case "LIGHT_POTATOES":
                    aisles = [cls.LIGHT_POTATOES]
                case "SMOOTH_FLAVORED_POTATOES":
                    aisles = [cls.SMOOTH_FLAVORED_POTATOES]
                case "TRADITIONAL_SMOOTH_POTATOES":
                    aisles = [cls.TRADITIONAL_SMOOTH_POTATOES]
                case "WAVY_FLAVORED_POTATOES":
                    aisles = [cls.WAVY_FLAVORED_POTATOES]
                case "TRADITIONAL_WAVY_POTATOES":
                    aisles = [cls.TRADITIONAL_WAVY_POTATOES]
                case "PIPES":
                    aisles = [cls.PIPES]
                case "PISTACHIOS_AND_CASHEWS":
                    aisles = [cls.PISTACHIOS_AND_CASHEWS]
                case "SNACKS_AND_OTHER_APPETIZERS":
                    aisles = [cls.SNACKS_AND_OTHER_APPETIZERS]
           
                
        return aisles
                                                          
class EroskiFeedingMilkAndBeveragesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Feeding_Milk_and_beverages")

    MILK_CALCIUM = StaticAisle(name="Milk calcium",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059807-leche-batidos-y-bebidas-vegetales/2059811-leche-calcio/",
                                     original_file_uri=os.path.join(category_path(), "Milk_calcium.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Milk_calcium_detailed.json"))
    
    CONDENSED_MILK = StaticAisle(name="Condensed milk", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059807-leche-batidos-y-bebidas-vegetales/2059817-leche-condensada/",
                                     original_file_uri=os.path.join(category_path(), "Condensed_milk.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Condensed_milk_detailed.json"))
    
    SKIMMED_MILK = StaticAisle(name="Skimmed milk",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059807-leche-batidos-y-bebidas-vegetales/2059809-leche-desnatada/",
                                     original_file_uri=os.path.join(category_path(), "Skimmed_milk.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Skimmed_milk_detailed.json"))
    
    POWDERED_MILK = StaticAisle(name="Powdered milk",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059807-leche-batidos-y-bebidas-vegetales/2059816-leche-en-polvo/",
                                     original_file_uri=os.path.join(category_path(), "Powdered_milk.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Powdered_milk_detailed.json"))
    
    WHOLE_MILK = StaticAisle(name="Whole milk",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059807-leche-batidos-y-bebidas-vegetales/2059813-leche-fresca/",
                                     original_file_uri=os.path.join(category_path(), "Whole_milk.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Whole_milk_detailed.json"))
    
    FRESH_MILK = StaticAisle(name="Fresh milk",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060076-frutos-secos-patatas-y-snacks/2060089-patatas-light/",
                                     original_file_uri=os.path.join(category_path(), "Fresh_milk.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fresh_milk_detailed.json"))
    
    SEMI_SKIMMED_MILK = StaticAisle(name="Semi-skimmed milk",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059807-leche-batidos-y-bebidas-vegetales/2059808-leche-semidesnatada/",
                                     original_file_uri=os.path.join(category_path(), "Semi_skimmed_milk.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Semi_skimmed_milk_detailed.json"))
    
    LACTOSE_FREE_AND_SPECIAL_MILK = StaticAisle(name="Lactose-free and special milk",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059807-leche-batidos-y-bebidas-vegetales/2059815-leche-sin-lactosa-y-especiales/",
                                     original_file_uri=os.path.join(category_path(), "Lactose_free_and_special_milk.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Lactose_free_and_special_milk_detailed.json"))
    
    COCOA_AND_LIQUID_CHOCOLATE_SHAKE = StaticAisle(name="Cocoa and liquid chocolate shake",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059807-leche-batidos-y-bebidas-vegetales/2059843-batido-de-cacao-y-chocolate-liquido/",
                                     original_file_uri=os.path.join(category_path(), "Cocoa_and_liquid_chocolate_shake.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cocoa_and_liquid_chocolate_shake_detailed.json"))
    
    SOY_AND_OTHER_CEREAL_DRINKS = StaticAisle(name="Soy and other cereal drinks",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059807-leche-batidos-y-bebidas-vegetales/2059814-bebida-de-soja-y-otros-cereales/",
                                     original_file_uri=os.path.join(category_path(), "Soy_and_other_cereal_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Soy_and_other_cereal_drinks_detailed.json"))
    
    HORCHATA = StaticAisle(name="Horchata",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059807-leche-batidos-y-bebidas-vegetales/2059847-horchata/",
                                     original_file_uri=os.path.join(category_path(), "Horchata.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Horchata_detailed.json"))
    
    LACTOJUICE = StaticAisle(name="Lactojuice",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059807-leche-batidos-y-bebidas-vegetales/2059849-lactozumo/",
                                     original_file_uri=os.path.join(category_path(), "Lactojuice.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Lactojuice_detailed.json"))
    
    OTHER_SHAKES = StaticAisle(name="Other shakes",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059807-leche-batidos-y-bebidas-vegetales/2059846-otros-batidos/",
                                     original_file_uri=os.path.join(category_path(), "Other_shakes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_shakes_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [MILK_CALCIUM, CONDENSED_MILK, SKIMMED_MILK, POWDERED_MILK, WHOLE_MILK, FRESH_MILK, SEMI_SKIMMED_MILK, LACTOSE_FREE_AND_SPECIAL_MILK, COCOA_AND_LIQUID_CHOCOLATE_SHAKE, SOY_AND_OTHER_CEREAL_DRINKS, HORCHATA, LACTOJUICE, OTHER_SHAKES]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "MILK_CALCIUM":
                    aisles = [cls.MILK_CALCIUM]
                case "CONDENSED_MILK":
                    aisles = [cls.CONDENSED_MILK]
                case "SKIMMED_MILK":
                    aisles = [cls.SKIMMED_MILK]
                case "POWDERED_MILK":
                    aisles = [cls.POWDERED_MILK]
                case "WHOLE_MILK":
                    aisles = [cls.WHOLE_MILK]
                case "FRESH_MILK":
                    aisles = [cls.FRESH_MILK]
                case "SEMI_SKIMMED_MILK":
                    aisles = [cls.SEMI_SKIMMED_MILK]
                case "LACTOSE_FREE_AND_SPECIAL_MILK":
                    aisles = [cls.LACTOSE_FREE_AND_SPECIAL_MILK]
                case "COCOA_AND_LIQUID_CHOCOLATE_SHAKE":
                    aisles = [cls.COCOA_AND_LIQUID_CHOCOLATE_SHAKE]
                case "SOY_AND_OTHER_CEREAL_DRINKS":
                    aisles = [cls.SOY_AND_OTHER_CEREAL_DRINKS]
                case "HORCHATA":
                    aisles = [cls.HORCHATA]
                case "LACTOJUICE":
                    aisles = [cls.LACTOJUICE]
                case "OTHER_SHAKES":
                    aisles = [cls.OTHER_SHAKES]
           
                
        return aisles
                                                          
class EroskiFeedingLegumesRiceAndPastaAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Feeding_Legumes_rice_pasta")

    RICE = StaticAisle(name="Rice",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060029-legumbres-arroz-y-pasta/2060032-arroz/",
                                     original_file_uri=os.path.join(category_path(), "Rice.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Rice_detailed.json"))
    
    SPAGHETTI_NOODLES_AND_LONG_PASTA = StaticAisle(name="Spaghetti, noodles and long pasta", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060029-legumbres-arroz-y-pasta/2060033-espagueti-tallarines-y-pasta-larga/",
                                     original_file_uri=os.path.join(category_path(), "Spaghetti_noodles_and_long_pasta.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Spaghetti_noodles_and_long_pasta_detailed.json"))
    
    NOODLES_AND_PASTA_SOUP = StaticAisle(name="Noodles and pasta soup",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060029-legumbres-arroz-y-pasta/2060036-fideos-y-pasta-sopa/",
                                     original_file_uri=os.path.join(category_path(), "Noodles_and_pasta_soup.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Noodles_and_pasta_soup_detailed.json"))
    
    LASAGNA_AND_CANNELLONI = StaticAisle(name="Lasagna and cannelloni",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060029-legumbres-arroz-y-pasta/2060037-lasana-y-canelones/",
                                     original_file_uri=os.path.join(category_path(), "Lasagna_and_cannelloni.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Lasagna_and_cannelloni_detailed.json"))
    
    VEGETABLES = StaticAisle(name="Vegetables",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060029-legumbres-arroz-y-pasta/2060030-legumbres/",
                                     original_file_uri=os.path.join(category_path(), "Vegetables.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vegetables_detailed.json"))
    
    COOKED_LEGUMES = StaticAisle(name="Cooked legumes",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060029-legumbres-arroz-y-pasta/2060031-legumbres-cocidas/",
                                     original_file_uri=os.path.join(category_path(), "Cooked_legumes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cooked_legumes_detailed.json"))
    
    MACARONI_AND_SHORT_PASTA = StaticAisle(name="Macaroni and short pasta",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060029-legumbres-arroz-y-pasta/2060034-macarrones-y-pasta-corta/",
                                     original_file_uri=os.path.join(category_path(), "Macaroni_and_short_pasta.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Macaroni_and_short_pasta_detailed.json"))
    
    EGG_PASTA_AND_NESTS = StaticAisle(name="Egg pasta and nests",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060029-legumbres-arroz-y-pasta/2060039-pasta-al-huevo-y-nidos/",
                                     original_file_uri=os.path.join(category_path(), "Egg_pasta_and_nests.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Egg_pasta_and_nests_detailed.json"))
    
    PASTA_GOURMET = StaticAisle(name="Pasta Gourmet",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060029-legumbres-arroz-y-pasta/23061098-pasta-gourmet/",
                                     original_file_uri=os.path.join(category_path(), "Pasta_Gourmet.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pasta_Gourmet_detailed.json"))
    
    GLUTEN_FREE_AND_WHOLEMEAL_PASTA = StaticAisle(name="Gluten-free and wholemeal pasta",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060029-legumbres-arroz-y-pasta/2060851-pasta-sin-gluten-e-integral/",
                                     original_file_uri=os.path.join(category_path(), "Gluten_free_and_wholemeal_pasta.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Gluten_free_and_wholemeal_pasta_detailed.json"))
    
    VEGETABLE_PASTA_AND_SALADS = StaticAisle(name="Vegetable pasta and salads",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060029-legumbres-arroz-y-pasta/2060035-pasta-vegetal-y-ensaladas/",
                                     original_file_uri=os.path.join(category_path(), "Vegetable_pasta_and_salads.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vegetable_pasta_and_salads_detailed.json"))
    
    SAUCES = StaticAisle(name="Sauces",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060029-legumbres-arroz-y-pasta/4000101-salsas-/",
                                     original_file_uri=os.path.join(category_path(), "Sauces.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sauces_detailed.json"))
    
    SEMOLINA_TAPIOCA_AND_OTHERS = StaticAisle(name="Semolina, tapioca and others",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060029-legumbres-arroz-y-pasta/2060040-semolas--tapioca-y-otras/",
                                     original_file_uri=os.path.join(category_path(), "Semolina_tapioca_and_others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Semolina_tapioca_and_others_detailed.json"))
    
    TORTELINI_RAVIOLI_AND_OTHERS = StaticAisle(name="Tortelini, ravioli and others",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060029-legumbres-arroz-y-pasta/2060038-tortelinis-raviolis-y-otras/",
                                     original_file_uri=os.path.join(category_path(), "Tortelini_ravioli_and_others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tortelini_ravioli_and_others_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [RICE, SPAGHETTI_NOODLES_AND_LONG_PASTA, NOODLES_AND_PASTA_SOUP, LASAGNA_AND_CANNELLONI, VEGETABLES, COOKED_LEGUMES, MACARONI_AND_SHORT_PASTA, EGG_PASTA_AND_NESTS, PASTA_GOURMET, GLUTEN_FREE_AND_WHOLEMEAL_PASTA, VEGETABLE_PASTA_AND_SALADS, SAUCES, SEMOLINA_TAPIOCA_AND_OTHERS, TORTELINI_RAVIOLI_AND_OTHERS]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "RICE":
                    aisles = [cls.RICE]
                case "SPAGHETTI_NOODLES_AND_LONG_PASTA":
                    aisles = [cls.SPAGHETTI_NOODLES_AND_LONG_PASTA]
                case "NOODLES_AND_PASTA_SOUP":
                    aisles = [cls.NOODLES_AND_PASTA_SOUP]
                case "LASAGNA_AND_CANNELLONI":
                    aisles = [cls.LASAGNA_AND_CANNELLONI]
                case "VEGETABLES":
                    aisles = [cls.VEGETABLES]
                case "COOKED_LEGUMES":
                    aisles = [cls.COOKED_LEGUMES]
                case "MACARONI_AND_SHORT_PASTA":
                    aisles = [cls.MACARONI_AND_SHORT_PASTA]
                case "EGG_PASTA_AND_NESTS":
                    aisles = [cls.EGG_PASTA_AND_NESTS]
                case "PASTA_GOURMET":
                    aisles = [cls.PASTA_GOURMET]
                case "GLUTEN_FREE_AND_WHOLEMEAL_PASTA":
                    aisles = [cls.GLUTEN_FREE_AND_WHOLEMEAL_PASTA]
                case "VEGETABLE_PASTA_AND_SALADS":
                    aisles = [cls.VEGETABLE_PASTA_AND_SALADS]
                case "SAUCES":
                    aisles = [cls.SAUCES]
                case "SEMOLINA_TAPIOCA_AND_OTHERS":
                    aisles = [cls.SEMOLINA_TAPIOCA_AND_OTHERS]
                case "TORTELINI_RAVIOLI_AND_OTHERS":
                    aisles = [cls.TORTELINI_RAVIOLI_AND_OTHERS]
           
                
        return aisles
                                                          
class EroskiFeedingButterAndCreamAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Feeding_Butter_cream")

    BECHAMEL = StaticAisle(name="Bechamel",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059851-mantequilla-nata-y-cremas/2059857-bechamel/",
                                     original_file_uri=os.path.join(category_path(), "Bechamel.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Bechamel_detailed.json"))
    
    BUTTER = StaticAisle(name="Butter", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059851-mantequilla-nata-y-cremas/2059852-mantequilla/",
                                     original_file_uri=os.path.join(category_path(), "Butter.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Butter_detailed.json"))
    
    MARGARINE = StaticAisle(name="Margarine",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059851-mantequilla-nata-y-cremas/2059853-margarina/",
                                     original_file_uri=os.path.join(category_path(), "Margarine.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Margarine_detailed.json"))
    
    PASTRY_CREAM = StaticAisle(name="Pastry cream",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059851-mantequilla-nata-y-cremas/2059855-nata-de-reposteria/",
                                     original_file_uri=os.path.join(category_path(), "Pastry_cream.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pastry_cream_detailed.json"))
    
    FRESH_CREAM = StaticAisle(name="Fresh cream",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059851-mantequilla-nata-y-cremas/2059856-nata-fresca/",
                                     original_file_uri=os.path.join(category_path(), "Fresh_cream.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fresh_cream_detailed.json"))
    
    COOKING_CREAM = StaticAisle(name="Cooking cream",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059851-mantequilla-nata-y-cremas/2059854-nata-para-cocinar/",
                                     original_file_uri=os.path.join(category_path(), "Cooking_cream.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cooking_cream_detailed.json"))
    

    
    aisles: Final[List[StaticAisle]] = [BECHAMEL, BUTTER, MARGARINE, PASTRY_CREAM, FRESH_CREAM, COOKING_CREAM]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "BECHAMEL":
                    aisles = [cls.BECHAMEL]
                case "BUTTER":
                    aisles = [cls.BUTTER]
                case "MARGARINE":
                    aisles = [cls.MARGARINE]
                case "PASTRY_CREAM":
                    aisles = [cls.PASTRY_CREAM]
                case "FRESH_CREAM":
                    aisles = [cls.FRESH_CREAM]
                case "COOKING_CREAM":
                    aisles = [cls.COOKING_CREAM]
              
        return aisles
                                                          
class EroskiFeedingReadyMealsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Feeding_Ready_meals")

    MEAT_POULTRY_AND_GAME = StaticAisle(name="Meat, poultry and game",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060042-platos-preparados/2060049-carne-ave-y-caza/",
                                     original_file_uri=os.path.join(category_path(), "Meat_poultry_and_game.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Meat_poultry_and_game_detailed.json"))
    
    MEXICAN_FOOD = StaticAisle(name="Mexican Food", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060042-platos-preparados/2060051-comida-mejicana/",
                                     original_file_uri=os.path.join(category_path(), "Mexican_Food.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mexican_Food_detailed.json"))
    
    ORIENTAL_FOOD = StaticAisle(name="Oriental Food",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060042-platos-preparados/2060052-comida-oriental/",
                                     original_file_uri=os.path.join(category_path(), "Oriental_Food.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Oriental_Food_detailed.json"))
    
    FOOD_OTHER_ORIGINS = StaticAisle(name="Food other origins",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060042-platos-preparados/2060055-comida-otros-origenes/",
                                     original_file_uri=os.path.join(category_path(), "Food_other_origins.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Food_other_origins_detailed.json"))
    
    PREPARED_SALADS = StaticAisle(name="Prepared salads",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060042-platos-preparados/2060046-ensaladas--preparadas/",
                                     original_file_uri=os.path.join(category_path(), "Prepared_salads.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Prepared_salads_detailed.json"))
    
    LEGUMES_RICE_AND_PASTA = StaticAisle(name="Legumes, rice and pasta",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060042-platos-preparados/2060044-legumbres-arroz-y-pasta/",
                                     original_file_uri=os.path.join(category_path(), "Legumes_rice_and_pasta.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Legumes_rice_and_pasta_detailed.json"))
    
    FISH = StaticAisle(name="Fish", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060042-platos-preparados/2060048-pescado/",
                                     original_file_uri=os.path.join(category_path(), "Fish.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fish_detailed.json"))
    
    MASHED_POTATOES = StaticAisle(name="Mashed potatoes",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060042-platos-preparados/2060045-pure-de-patatas/",
                                     original_file_uri=os.path.join(category_path(), "Mashed_potatoes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mashed_potatoes_detailed.json"))
    
    SAUSAGES_AND_LEAN_FOODS = StaticAisle(name="Sausages and lean foods",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060042-platos-preparados/2060050-salchichas-y-magros/",
                                     original_file_uri=os.path.join(category_path(), "Sausages_and_lean_foods.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sausages_and_lean_foods_detailed.json"))
    
    SOUPS_BROTHS_AND_CREAMS = StaticAisle(name="Soups, broths and creams",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060042-platos-preparados/2060043-sopas-caldos-y-cremas/",
                                     original_file_uri=os.path.join(category_path(), "Soups_broths_and_creams.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Soups_broths_and_creams_detailed.json"))
    
    VEGETABLES_AND_STUFFED_PEPPERS = StaticAisle(name="Vegetables and stuffed peppers",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060042-platos-preparados/2060047-verduras-y-pimientos-rellenos/",
                                     original_file_uri=os.path.join(category_path(), "Vegetables_and_stuffed_peppers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vegetables_and_stuffed_peppers_detailed.json"))
    

    
    aisles: Final[List[StaticAisle]] = [MEAT_POULTRY_AND_GAME, MEXICAN_FOOD, ORIENTAL_FOOD, FOOD_OTHER_ORIGINS, PREPARED_SALADS, LEGUMES_RICE_AND_PASTA, FISH, MASHED_POTATOES, SAUSAGES_AND_LEAN_FOODS, SOUPS_BROTHS_AND_CREAMS, VEGETABLES_AND_STUFFED_PEPPERS]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "MEAT_POULTRY_AND_GAME":
                    aisles = [cls.MEAT_POULTRY_AND_GAME]
                case "MEXICAN_FOOD":
                    aisles = [cls.MEXICAN_FOOD]
                case "ORIENTAL_FOOD":
                    aisles = [cls.ORIENTAL_FOOD]
                case "FOOD_OTHER_ORIGINS":
                    aisles = [cls.FOOD_OTHER_ORIGINS]
                case "PREPARED_SALADS":
                    aisles = [cls.PREPARED_SALADS]
                case "LEGUMES_RICE_AND_PASTA":
                    aisles = [cls.LEGUMES_RICE_AND_PASTA]
                case "FISH":
                    aisles = [cls.FISH]
                case "MASHED_POTATOES":
                    aisles = [cls.MASHED_POTATOES]
                case "SAUSAGES_AND_LEAN_FOODS":
                    aisles = [cls.SAUSAGES_AND_LEAN_FOODS]
                case "SOUPS_BROTHS_AND_CREAMS":
                    aisles = [cls.SOUPS_BROTHS_AND_CREAMS]
                case "VEGETABLES_AND_STUFFED_PEPPERS":
                    aisles = [cls.VEGETABLES_AND_STUFFED_PEPPERS]
              
        return aisles
                                                          
class EroskiFeedingDairyDessertsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Feeding_Dairy_desserts")

    RICE_PUDDING = StaticAisle(name="Rice pudding",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059831-postres-lacteos-/2059835-arroz-con-leche-/",
                                     original_file_uri=os.path.join(category_path(), "Rice_pudding.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Rice_pudding_detailed.json"))
    
    COFFEES_AND_COLD_DRINKS = StaticAisle(name="Coffees and cold drinks", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059831-postres-lacteos-/5000301-cafes-y-bebidas-frias/",
                                     original_file_uri=os.path.join(category_path(), "Coffees_and_cold_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Coffees_and_cold_drinks_detailed.json"))
    
    CUPS_WITH_CREAM_AND_MOUSSES = StaticAisle(name="Cups with cream and mousses",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059831-postres-lacteos-/2059837-copas-con-nata-y-mousses/",
                                     original_file_uri=os.path.join(category_path(), "Cups_with_cream_and_mousses.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cups_with_cream_and_mousses_detailed.json"))
    
    CURD = StaticAisle(name="Curd",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059831-postres-lacteos-/2059834-cuajada/",
                                     original_file_uri=os.path.join(category_path(), "Curd.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Curd_detailed.json"))
    
    FLAN = StaticAisle(name="Flan",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059831-postres-lacteos-/2059833-flan/",
                                     original_file_uri=os.path.join(category_path(), "Flan.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Flan_detailed.json"))
    
    JELLIES = StaticAisle(name="Jellies",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059831-postres-lacteos-/2059840-gelatinas/",
                                     original_file_uri=os.path.join(category_path(), "Jellies.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Jellies_detailed.json"))
    
    CUSTARD = StaticAisle(name="Custard", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059831-postres-lacteos-/2059832-natillas/",
                                     original_file_uri=os.path.join(category_path(), "Custard.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Custard_detailed.json"))
    
    CHOCOLATE_AND_OTHER_DESSERTS = StaticAisle(name="Chocolate and other desserts",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059831-postres-lacteos-/2059838-postres-de-chocolate-y-otros/",
                                     original_file_uri=os.path.join(category_path(), "Chocolate_and_other_desserts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chocolate_and_other_desserts_detailed.json"))
    
    NO_COLD = StaticAisle(name="No cold",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059831-postres-lacteos-/2059841-sin-frio/",
                                     original_file_uri=os.path.join(category_path(), "No_cold.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "No_cold_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [RICE_PUDDING, COFFEES_AND_COLD_DRINKS, CUPS_WITH_CREAM_AND_MOUSSES, CURD, FLAN, JELLIES, CUSTARD, CHOCOLATE_AND_OTHER_DESSERTS, NO_COLD]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "RICE_PUDDING":
                    aisles = [cls.RICE_PUDDING]
                case "COFFEES_AND_COLD_DRINKS":
                    aisles = [cls.COFFEES_AND_COLD_DRINKS]
                case "CUPS_WITH_CREAM_AND_MOUSSES":
                    aisles = [cls.CUPS_WITH_CREAM_AND_MOUSSES]
                case "CURD":
                    aisles = [cls.CURD]
                case "FLAN":
                    aisles = [cls.FLAN]
                case "JELLIES":
                    aisles = [cls.JELLIES]
                case "CUSTARD":
                    aisles = [cls.CUSTARD]
                case "CHOCOLATE_AND_OTHER_DESSERTS":
                    aisles = [cls.CHOCOLATE_AND_OTHER_DESSERTS]
                case "NO_COLD":
                    aisles = [cls.NO_COLD]
                
              
        return aisles
                                                          
class EroskiFeedingDieteticsProductsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Feeding_Dietetics_products")

    SPORTS_NUTRITION = StaticAisle(name="Sports nutrition",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/5000365-productos-de-dietetica/5000382-alimentacion-deportiva/",
                                     original_file_uri=os.path.join(category_path(), "Sports_nutrition.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sports_nutrition_detailed.json"))
    
    PLANT_BASED_DRINKS = StaticAisle(name="Plant-based drinks", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/5000365-productos-de-dietetica/5000379-bebidas-vegetales/",
                                     original_file_uri=os.path.join(category_path(), "Plant_based_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Plant_based_drinks_detailed.json"))
    
    PHYTOTHERAPY = StaticAisle(name="Phytotherapy",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/5000365-productos-de-dietetica/5000380-fitoterapia/",
                                     original_file_uri=os.path.join(category_path(), "Phytotherapy.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Phytotherapy_detailed.json"))
    
    NUTRITION_AND_DIETETICS = StaticAisle(name="Nutrition and dietetics",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/5000365-productos-de-dietetica/5000381-nutricion-y-dietetica/",
                                     original_file_uri=os.path.join(category_path(), "Nutrition_and_dietetics.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Nutrition_and_dietetics_detailed.json"))
    
    GLUTEN_FREE_PRODUCTS = StaticAisle(name="Gluten-free products",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/5000365-productos-de-dietetica/5000385-productos-sin-gluten/",
                                     original_file_uri=os.path.join(category_path(), "Gluten_free_products.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Gluten_free_products_detailed.json"))
    
    PANCAKES = StaticAisle(name="Pancakes",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/5000365-productos-de-dietetica/5000386-tortitas/",
                                     original_file_uri=os.path.join(category_path(), "Pancakes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pancakes_detailed.json"))
    
    SUPERFOODS = StaticAisle(name="Superfoods", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/5000365-productos-de-dietetica/5000387-superalimentos/",
                                     original_file_uri=os.path.join(category_path(), "Superfoods.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Superfoods_detailed.json"))
    
    
    
    aisles: Final[List[StaticAisle]] = [SPORTS_NUTRITION, PLANT_BASED_DRINKS, PHYTOTHERAPY, NUTRITION_AND_DIETETICS, GLUTEN_FREE_PRODUCTS, PANCAKES, SUPERFOODS]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "SPORTS_NUTRITION":
                    aisles = [cls.SPORTS_NUTRITION]
                case "PLANT_BASED_DRINKS":
                    aisles = [cls.PLANT_BASED_DRINKS]
                case "PHYTOTHERAPY":
                    aisles = [cls.PHYTOTHERAPY]
                case "NUTRITION_AND_DIETETICS":
                    aisles = [cls.NUTRITION_AND_DIETETICS]
                case "GLUTEN_FREE_PRODUCTS":
                    aisles = [cls.GLUTEN_FREE_PRODUCTS]
                case "PANCAKES":
                    aisles = [cls.PANCAKES]
                case "SUPERFOODS":
                    aisles = [cls.SUPERFOODS]
               
        return aisles
                                                          
class EroskiFeedingOrganicProductsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Feeding_Organic_products")

    ECO_OILS_AND_CONDIMENTS = StaticAisle(name="Eco oils and condiments",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/5000364-productos-ecologicos/5000368-aceites-y-condimentos-eco/",
                                     original_file_uri=os.path.join(category_path(), "Eco_oils_and_condiments.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Eco_oils_and_condiments_detailed.json"))
    
    ECO_SNACKS_OLIVES_AND_PICKLES = StaticAisle(name="Eco snacks, olives and pickles", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/5000364-productos-ecologicos/5000369-aperitivos-olivas-y-encurtidos-eco/",
                                     original_file_uri=os.path.join(category_path(), "Eco_snacks_olives_and_pickles.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Eco_snacks_olives_and_pickles_detailed.json"))
    
    ORGANIC_RICE_SEEDS_AND_LEGUMES = StaticAisle(name="Organic rice, seeds and legumes",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/5000364-productos-ecologicos/5000370-arroces-semillas-y-legumbres-eco/",
                                     original_file_uri=os.path.join(category_path(), "Organic_rice_seeds_and_legumes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_rice_seeds_and_legumes_detailed.json"))
    
    ECO_DRINKS = StaticAisle(name="Eco drinks",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/5000364-productos-ecologicos/5000376-bebidas-eco/",
                                     original_file_uri=os.path.join(category_path(), "Eco_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Eco_drinks_detailed.json"))
    
    ECO_PRESERVES = StaticAisle(name="Eco preserves",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/5000364-productos-ecologicos/5000373-conservas-eco/",
                                     original_file_uri=os.path.join(category_path(), "Eco_preserves.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Eco_preserves_detailed.json"))
    
    ECO_BREAKFASTS_AND_SNACKS = StaticAisle(name="Eco breakfasts and snacks",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/5000364-productos-ecologicos/5000372-desayunos-y-meriendas-eco/",
                                     original_file_uri=os.path.join(category_path(), "Eco_breakfasts_and_snacks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Eco_breakfasts_and_snacks_detailed.json"))
    
    ECO_SWEETS_AND_SWEETENERS = StaticAisle(name="Eco sweets and sweeteners", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/5000365-productos-de-dietetica/5000387-superalimentos/",
                                     original_file_uri=os.path.join(category_path(), "Eco_sweets_and_sweeteners.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Eco_sweets_and_sweeteners_detailed.json"))
    
    ORGANIC_MILK_AND_VEGETABLE_DRINKS = StaticAisle(name="Organic milk and vegetable drinks",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/5000364-productos-ecologicos/5000375-leche-y-bebidas-vegetales-eco/",
                                     original_file_uri=os.path.join(category_path(), "Organic_milk_and_vegetable_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_milk_and_vegetable_drinks_detailed.json"))
    
    ECO_PASTAS_SOUPS_AND_CREAMS = StaticAisle(name="Eco pastas, soups and creams",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/5000364-productos-ecologicos/5000374-pastassopas-y-cremas-eco/",
                                     original_file_uri=os.path.join(category_path(), "Eco_pastas_soups_and_creams.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Eco_pastas_soups_and_creams_detailed.json"))
    
    REFRIGERATED = StaticAisle(name="Refrigerated", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/5000364-productos-ecologicos/5000389-refrigerados/",
                                     original_file_uri=os.path.join(category_path(), "Refrigerated.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Refrigerated_detailed.json"))
    
    
    
    aisles: Final[List[StaticAisle]] = [ECO_OILS_AND_CONDIMENTS, ECO_SNACKS_OLIVES_AND_PICKLES, ORGANIC_RICE_SEEDS_AND_LEGUMES, ECO_DRINKS, ECO_PRESERVES, ECO_BREAKFASTS_AND_SNACKS, ECO_SWEETS_AND_SWEETENERS, ORGANIC_MILK_AND_VEGETABLE_DRINKS, ECO_PASTAS_SOUPS_AND_CREAMS, REFRIGERATED]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "ECO_OILS_AND_CONDIMENTS":
                    aisles = [cls.ECO_OILS_AND_CONDIMENTS]
                case "ECO_SNACKS_OLIVES_AND_PICKLES":
                    aisles = [cls.ECO_SNACKS_OLIVES_AND_PICKLES]
                case "ORGANIC_RICE_SEEDS_AND_LEGUMES":
                    aisles = [cls.ORGANIC_RICE_SEEDS_AND_LEGUMES]
                case "ECO_DRINKS":
                    aisles = [cls.ECO_DRINKS]
                case "ECO_PRESERVES":
                    aisles = [cls.ECO_PRESERVES]
                case "ECO_BREAKFASTS_AND_SNACKS":
                    aisles = [cls.ECO_BREAKFASTS_AND_SNACKS]
                case "ECO_SWEETS_AND_SWEETENERS":
                    aisles = [cls.ECO_SWEETS_AND_SWEETENERS]
                case "ORGANIC_MILK_AND_VEGETABLE_DRINKS":
                    aisles = [cls.ORGANIC_MILK_AND_VEGETABLE_DRINKS]
                case "ECO_PASTAS_SOUPS_AND_CREAMS":
                    aisles = [cls.ECO_PASTAS_SOUPS_AND_CREAMS]
                case "REFRIGERATED":
                    aisles = [cls.REFRIGERATED]
               
        return aisles
                                                         
class EroskiFeedingSaucesAndSpicesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Feeding_Sauces_and_spices")

    SAFFRON_AND_COLORING = StaticAisle(name="Saffron and coloring",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060056-salsas-y-especias/2060064-azafran-y-colorante/",
                                     original_file_uri=os.path.join(category_path(), "Saffron_and_coloring.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Saffron_and_coloring_detailed.json"))
    
    PARSLEY_AND_OREGANO = StaticAisle(name="Parsley and oregano", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060056-salsas-y-especias/2060065-perejil-y-oregano/",
                                     original_file_uri=os.path.join(category_path(), "Parsley_and_oregano.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Parsley_and_oregano_detailed.json"))
    
    OTHER_SPICES = StaticAisle(name="Other spices",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060056-salsas-y-especias/2060066-otras-especias/",
                                     original_file_uri=os.path.join(category_path(), "Other_spices.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_spices_detailed.json"))
    
    KETCHUP_AND_MUSTARD = StaticAisle(name="Ketchup and mustard",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060056-salsas-y-especias/2060058-ketchup-y-mostaza/",
                                     original_file_uri=os.path.join(category_path(), "Ketchup_and_mustard.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Ketchup_and_mustard_detailed.json"))
    
    MAYONNAISE = StaticAisle(name="Mayonnaise",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060056-salsas-y-especias/2060057-mayonesa/",
                                     original_file_uri=os.path.join(category_path(), "Mayonnaise.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mayonnaise_detailed.json"))
    
    SOY_SAUCE_SPICY_AND_OTHERS = StaticAisle(name="Soy sauce, spicy and others",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060056-salsas-y-especias/2060059-salsa-de-soja-picantes-y-otras/",
                                     original_file_uri=os.path.join(category_path(), "Soy_sauce_spicy_and_others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Soy_sauce_spicy_and_others_detailed.json"))
    
    MEAT_SAUCES = StaticAisle(name="Meat sauces", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060056-salsas-y-especias/2060063-salsas-para-carne/",
                                     original_file_uri=os.path.join(category_path(), "Meat_sauces.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Meat_sauces_detailed.json"))
    
    PASTA_SAUCES = StaticAisle(name="Pasta sauces",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060056-salsas-y-especias/2060060-salsas-para-pasta/",
                                     original_file_uri=os.path.join(category_path(), "Pasta_sauces.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pasta_sauces_detailed.json"))
    
    PINK_BRAVA_AND_BARBECUE_SAUCE = StaticAisle(name="Pink, brava and barbecue sauce",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060056-salsas-y-especias/2060061-salsa-rosa-brava-y-barbacoa/",
                                     original_file_uri=os.path.join(category_path(), "Pink_brava_and_barbecue_sauce.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pink_brava_and_barbecue_sauce_detailed.json"))
    
    OTHER_COLD_SAUCES = StaticAisle(name="Other cold sauces", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060056-salsas-y-especias/2060062-otras-salsas-frias/",
                                     original_file_uri=os.path.join(category_path(), "Other_cold_sauces.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_cold_sauces_detailed.json"))
    
    
    
    aisles: Final[List[StaticAisle]] = [SAFFRON_AND_COLORING, PARSLEY_AND_OREGANO, OTHER_SPICES, KETCHUP_AND_MUSTARD, MAYONNAISE, SOY_SAUCE_SPICY_AND_OTHERS, MEAT_SAUCES, PASTA_SAUCES, PINK_BRAVA_AND_BARBECUE_SAUCE, OTHER_COLD_SAUCES]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "SAFFRON_AND_COLORING":
                    aisles = [cls.SAFFRON_AND_COLORING]
                case "PARSLEY_AND_OREGANO":
                    aisles = [cls.PARSLEY_AND_OREGANO]
                case "OTHER_SPICES":
                    aisles = [cls.OTHER_SPICES]
                case "KETCHUP_AND_MUSTARD":
                    aisles = [cls.KETCHUP_AND_MUSTARD]
                case "MAYONNAISE":
                    aisles = [cls.MAYONNAISE]
                case "SOY_SAUCE_SPICY_AND_OTHERS":
                    aisles = [cls.SOY_SAUCE_SPICY_AND_OTHERS]
                case "MEAT_SAUCES":
                    aisles = [cls.MEAT_SAUCES]
                case "PASTA_SAUCES":
                    aisles = [cls.PASTA_SAUCES]
                case "PINK_BRAVA_AND_BARBECUE_SAUCE":
                    aisles = [cls.PINK_BRAVA_AND_BARBECUE_SAUCE]
                case "OTHER_COLD_SAUCES":
                    aisles = [cls.OTHER_COLD_SAUCES]
               
        return aisles
                                                          
class EroskiFeedingYoghurtsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Feeding_Yoghurts")

    LCASEI_AND_PROBIOTICS = StaticAisle(name="L.Casei and probiotics",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059818-yogures/2059827-lcasei-y-probioticos/",
                                     original_file_uri=os.path.join(category_path(), "LCasei_and_probiotics.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "LCasei_and_probiotics_detailed.json"))
    
    PETIT_AND_OTHER_CHILDREN = StaticAisle(name="Petit and other children's", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059818-yogures/2059828-petit-y-otros-infantiles/",
                                     original_file_uri=os.path.join(category_path(), "Petit_and_other_children.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Petit_and_other_children_detailed.json"))
    
    HEALTH_AND_AESTHETICS = StaticAisle(name="Health and aesthetics",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059818-yogures/2059829-salud-y-estetica/",
                                     original_file_uri=os.path.join(category_path(), "Health_and_aesthetics.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Health_and_aesthetics_detailed.json"))
    
    BIFIDUS_YOGURT = StaticAisle(name="Bifidus yogurt",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059818-yogures/2059824-yogur-bifidus/",
                                     original_file_uri=os.path.join(category_path(), "Bifidus_yogurt.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Bifidus_yogurt_detailed.json"))
    
    BIFIDUS_YOGURT_0 = StaticAisle(name="Bifidus yogurt 0%",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059818-yogures/2059825-yogur-bifidus-0/",
                                     original_file_uri=os.path.join(category_path(), "Bifidus_yogurt_0.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Bifidus_yogurt_0_detailed.json"))
    
    CREAMY_YOGURT = StaticAisle(name="Creamy yogurt",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059818-yogures/2059821-yogur-cremoso/",
                                     original_file_uri=os.path.join(category_path(), "Creamy_yogurt.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Creamy_yogurt_detailed.json"))
    
    FRUIT_YOGURT_AND_FLAVORS = StaticAisle(name="Fruit yogurt and flavors", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059818-yogures/2059820-yogur-de-frutas-y-sabores/",
                                     original_file_uri=os.path.join(category_path(), "Fruit_yogurt_and_flavors.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fruit_yogurt_and_flavors_detailed.json"))
    
    SKIMMED_YOGURT = StaticAisle(name="Skimmed yogurt",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059818-yogures/2059823-yogur-desnatado/",
                                     original_file_uri=os.path.join(category_path(), "Skimmed_yogurt.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Skimmed_yogurt_detailed.json"))
    
    ORGANIC_YOGURT_AND_SPECIALS = StaticAisle(name="Organic yogurt and specials",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059818-yogures/2059822-yogur-ecologico-y-especiales/",
                                     original_file_uri=os.path.join(category_path(), "Organic_yogurt_and_specials.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_yogurt_and_specials_detailed.json"))
    
    LIQUID_YOGURT_AND_OTHERS = StaticAisle(name="Liquid yogurt and others", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059818-yogures/2059826-yogur-liquido-y-otros/",
                                     original_file_uri=os.path.join(category_path(), "Liquid_yogurt_and_others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Liquid_yogurt_and_others_detailed.json"))
    
    NATURAL_YOGURT = StaticAisle(name="Natural yogurt",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059818-yogures/2059819-yogur-natural/",
                                     original_file_uri=os.path.join(category_path(), "Natural_yogurt.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Natural_yogurt_detailed.json"))
    
    SOY_AND_100_PLANT_BASED_YOGURT = StaticAisle(name="Soy and 100% plant-based yogurt", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059818-yogures/2059830-yogur-soja-y-100-vegetal/",
                                     original_file_uri=os.path.join(category_path(), "Soy_and_100_plant_based_yogurt.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Soy_and_100_plant_based_yogurt_detailed.json"))
    
    
    
    aisles: Final[List[StaticAisle]] = [LCASEI_AND_PROBIOTICS, PETIT_AND_OTHER_CHILDREN, HEALTH_AND_AESTHETICS, BIFIDUS_YOGURT, BIFIDUS_YOGURT_0, CREAMY_YOGURT, FRUIT_YOGURT_AND_FLAVORS, SKIMMED_YOGURT, ORGANIC_YOGURT_AND_SPECIALS, LIQUID_YOGURT_AND_OTHERS, NATURAL_YOGURT, SOY_AND_100_PLANT_BASED_YOGURT]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "LCASEI_AND_PROBIOTICS":
                    aisles = [cls.LCASEI_AND_PROBIOTICS]
                case "PETIT_AND_OTHER_CHILDREN":
                    aisles = [cls.PETIT_AND_OTHER_CHILDREN]
                case "HEALTH_AND_AESTHETICS":
                    aisles = [cls.HEALTH_AND_AESTHETICS]
                case "BIFIDUS_YOGURT":
                    aisles = [cls.BIFIDUS_YOGURT]
                case "BIFIDUS_YOGURT_0":
                    aisles = [cls.BIFIDUS_YOGURT_0]
                case "CREAMY_YOGURT":
                    aisles = [cls.CREAMY_YOGURT]
                case "FRUIT_YOGURT_AND_FLAVORS":
                    aisles = [cls.FRUIT_YOGURT_AND_FLAVORS]
                case "SKIMMED_YOGURT":
                    aisles = [cls.SKIMMED_YOGURT]
                case "ORGANIC_YOGURT_AND_SPECIALS":
                    aisles = [cls.ORGANIC_YOGURT_AND_SPECIALS]
                case "LIQUID_YOGURT_AND_OTHERS":
                    aisles = [cls.LIQUID_YOGURT_AND_OTHERS]
                case "NATURAL_YOGURT":
                    aisles = [cls.NATURAL_YOGURT]
                case "SOY_AND_100_PLANT_BASED_YOGURT":
                    aisles = [cls.SOY_AND_100_PLANT_BASED_YOGURT]
              
               
        return aisles
                                                          
class EroskiFeedingInternationalFoodAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Feeding_International_food")

    MEXICAN_FOOD = StaticAisle(name="Mexican Food",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/4000017-comida-internacional/4000018-comida-mexicana/",
                                     original_file_uri=os.path.join(category_path(), "Mexican_Food.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mexican_Food_detailed.json"))
    
    ORIENTAL_FOOD = StaticAisle(name="Oriental food", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/4000017-comida-internacional/4000019-comida-oriental/",
                                     original_file_uri=os.path.join(category_path(), "Oriental_food.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Oriental_food_detailed.json"))
    
    OTHER_ORIGINS = StaticAisle(name="Other origins",  url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/4000017-comida-internacional/4000020-otros-origenes/",
                                     original_file_uri=os.path.join(category_path(), "Other_origins.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_origins_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [MEXICAN_FOOD, ORIENTAL_FOOD, OTHER_ORIGINS]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "MEXICAN_FOOD":
                    aisles = [cls.MEXICAN_FOOD]
                case "ORIENTAL_FOOD":
                    aisles = [cls.ORIENTAL_FOOD]
                case "OTHER_ORIGINS":
                    aisles = [cls.OTHER_ORIGINS]
           
        return aisles

#Fresh
                                                   
class EroskiFreshMeatAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Fresh_Meat")

    MARINATED = StaticAisle(name="Marinated",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059746-carnes-y-aves/2059757-adobados/",
                                     original_file_uri=os.path.join(category_path(), "Marinated.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Marinated_detailed.json"))
    
    YEARLING = StaticAisle(name="Yearling", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059746-carnes-y-aves/2059748-anojo-/",
                                     original_file_uri=os.path.join(category_path(), "Yearling.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Yearling_detailed.json"))
    
    MINCED_MEAT_AND_HAMBURGERS = StaticAisle(name="Minced meat and hamburgers",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059746-carnes-y-aves/2059755-carne-picada-y-hamburguesas/",
                                     original_file_uri=os.path.join(category_path(), "Minced_meat_and_hamburgers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Minced_meat_and_hamburgers_detailed.json"))
    
    PORK_AND_IBERIAN_PORK = StaticAisle(name="Pork and Iberian pork",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059746-carnes-y-aves/2059750-cerdo-y-cerdo-iberico/",
                                     original_file_uri=os.path.join(category_path(), "Pork_and_Iberian_pork.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pork_and_Iberian_pork_detailed.json"))
    
    RABBIT = StaticAisle(name="Rabbit", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059746-carnes-y-aves/2059752-conejo/",
                                     original_file_uri=os.path.join(category_path(), "Rabbit.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Rabbit_detailed.json"))
    
    LAMB_AND_SUCKLING_PIG = StaticAisle(name="Lamb and suckling pig",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059746-carnes-y-aves/2059751-cordero-y-cochinillo/",
                                     original_file_uri=os.path.join(category_path(), "Lamb_and_suckling_pig.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Lamb_and_suckling_pig_detailed.json"))
    
    PROCESSED_AND_BREADED = StaticAisle(name="Processed and breaded",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059746-carnes-y-aves/2059758-elaborados-y-empanados/",
                                     original_file_uri=os.path.join(category_path(), "Processed_and_breaded.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Processed_and_breaded_detailed.json"))
    
    TURKEY_DUCK_AND_OTHER_BIRDS = StaticAisle(name="Turkey, duck and other birds", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059746-carnes-y-aves/2059754-pavo-pato-y-otras-aves/",
                                     original_file_uri=os.path.join(category_path(), "Turkey_duck_and_other_birds.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Turkey_duck_and_other_birds_detailed.json"))
    
    CHICKEN = StaticAisle(name="Chicken",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059746-carnes-y-aves/2059753-pollo/",
                                     original_file_uri=os.path.join(category_path(), "Chicken.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chicken_detailed.json"))
    
    SAUSAGE_BLACK_PUDDING_AND_CHORIZO = StaticAisle(name="Sausage, black pudding and chorizo",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059746-carnes-y-aves/2059756-salchicha-morcilla-y-chorizo/",
                                     original_file_uri=os.path.join(category_path(), "Sausage_black_pudding_and_chorizo.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sausage_black_pudding_and_chorizo_detailed.json"))
    
    VEAL = StaticAisle(name="Veal",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059746-carnes-y-aves/2059747-ternera/",
                                     original_file_uri=os.path.join(category_path(), "Veal.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Veal_detailed.json"))
    
    COW_OX_AND_BULL = StaticAisle(name="Cow, ox and bull", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059746-carnes-y-aves/2059749-vaca-buey-y-toro/",
                                     original_file_uri=os.path.join(category_path(), "Cow_ox_and_bull.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cow_ox_and_bull_detailed.json"))
    
    OTHER_MEATS_AND_OFFAL = StaticAisle(name="Other meats and offal",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059746-carnes-y-aves/2059759-otras-carnes-y-casqueria/",
                                     original_file_uri=os.path.join(category_path(), "Other_meats_and_offal.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_meats_and_offal_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [MARINATED, YEARLING, MINCED_MEAT_AND_HAMBURGERS, PORK_AND_IBERIAN_PORK, RABBIT, LAMB_AND_SUCKLING_PIG, PROCESSED_AND_BREADED, TURKEY_DUCK_AND_OTHER_BIRDS, CHICKEN, SAUSAGE_BLACK_PUDDING_AND_CHORIZO, VEAL, COW_OX_AND_BULL, OTHER_MEATS_AND_OFFAL]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "MARINATED":
                    aisles = [cls.MARINATED]
                case "YEARLING":
                    aisles = [cls.YEARLING]
                case "MINCED_MEAT_AND_HAMBURGERS":
                    aisles = [cls.MINCED_MEAT_AND_HAMBURGERS]
                case "PORK_AND_IBERIAN_PORK":
                    aisles = [cls.PORK_AND_IBERIAN_PORK]
                case "RABBIT":
                    aisles = [cls.RABBIT]
                case "LAMB_AND_SUCKLING_PIG":
                    aisles = [cls.LAMB_AND_SUCKLING_PIG]
                case "PROCESSED_AND_BREADED":
                    aisles = [cls.PROCESSED_AND_BREADED]
                case "TURKEY_DUCK_AND_OTHER_BIRDS":
                    aisles = [cls.TURKEY_DUCK_AND_OTHER_BIRDS]
                case "CHICKEN":
                    aisles = [cls.CHICKEN]
                case "SAUSAGE_BLACK_PUDDING_AND_CHORIZO":
                    aisles = [cls.SAUSAGE_BLACK_PUDDING_AND_CHORIZO]
                case "VEAL":
                    aisles = [cls.VEAL]
                case "COW_OX_AND_BULL":
                    aisles = [cls.COW_OX_AND_BULL]
                case "OTHER_MEATS_AND_OFFAL":
                    aisles = [cls.OTHER_MEATS_AND_OFFAL]
           
        return aisles
                                                          
class EroskiFreshCuredMeatAndSausagesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Fresh_Cured_meat_and_sausages")

    CHISTORRA_AND_SAUSAGE = StaticAisle(name="Chistorra and sausage",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059880-curados-y-embutidos/2059888-chistorra-y-longaniza/",
                                     original_file_uri=os.path.join(category_path(), "Chistorra_and_sausage.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chistorra_and_sausage_detailed.json"))
    
    CHORIZO = StaticAisle(name="Chorizo", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059880-curados-y-embutidos/2059883-chorizo/",
                                     original_file_uri=os.path.join(category_path(), "Chorizo.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chorizo_detailed.json"))
    
    PREPARED_SAUSAGES = StaticAisle(name="Prepared sausages",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059880-curados-y-embutidos/2059890-embutidos-preparados/",
                                     original_file_uri=os.path.join(category_path(), "Prepared_sausages.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Prepared_sausages_detailed.json"))
    
    CURED_HAM = StaticAisle(name="Cured ham",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059880-curados-y-embutidos/2059881-jamon-curado/",
                                     original_file_uri=os.path.join(category_path(), "Cured_ham.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cured_ham_detailed.json"))
    
    CURED_HAM_PIECE = StaticAisle(name="Cured ham piece", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059880-curados-y-embutidos/2059882-jamon-curado-pieza/",
                                     original_file_uri=os.path.join(category_path(), "Cured_ham_piece.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cured_ham_piece_detailed.json"))
    
    BACK = StaticAisle(name="Back",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059880-curados-y-embutidos/2059884-lomo/",
                                     original_file_uri=os.path.join(category_path(), "Back.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Back_detailed.json"))
    
    BACON_AND_BLACK_PUDDING = StaticAisle(name="Bacon and black pudding",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059880-curados-y-embutidos/2059887-panceta-y-morcilla/",
                                     original_file_uri=os.path.join(category_path(), "Bacon_and_black_pudding.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Bacon_and_black_pudding_detailed.json"))
    
    CURED_TURKEY_AND_OTHER_POULTRY = StaticAisle(name="Cured turkey and other poultry", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059880-curados-y-embutidos/2059892-pavo-y-otras-aves-curados/",
                                     original_file_uri=os.path.join(category_path(), "Cured_turkey_and_other_poultry.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cured_turkey_and_other_poultry_detailed.json"))
    
    SALAMI_AND_SOBRASADA = StaticAisle(name="Salami and sobrasada",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059880-curados-y-embutidos/2059886-salami-y-sobrasada/",
                                     original_file_uri=os.path.join(category_path(), "Salami_and_sobrasada.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Salami_and_sobrasada_detailed.json"))
    
    SAUSAGE_AND_FUET = StaticAisle(name="Sausage and fuet",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059880-curados-y-embutidos/2059885-salchichon-y-fuet/",
                                     original_file_uri=os.path.join(category_path(), "Sausage_and_fuet.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sausage_and_fuet_detailed.json"))
    
    CURED_TAQUITOS = StaticAisle(name="Cured Taquitos",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059880-curados-y-embutidos/2060865-taquitos-curados/",
                                     original_file_uri=os.path.join(category_path(), "Cured_Taquitos.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cured_Taquitos_detailed.json"))
    
    OTHER_CURED_MEATS_AND_SAUSAGES = StaticAisle(name="Other cured meats and sausages", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059880-curados-y-embutidos/2059893-otros-curados-y-embutidos/",
                                     original_file_uri=os.path.join(category_path(), "Other_cured_meats_and_sausages.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_cured_meats_and_sausages_detailed.json"))
    
    
    
    aisles: Final[List[StaticAisle]] = [CHISTORRA_AND_SAUSAGE, CHORIZO, PREPARED_SAUSAGES, CURED_HAM, CURED_HAM_PIECE, BACK, BACON_AND_BLACK_PUDDING, CURED_TURKEY_AND_OTHER_POULTRY, SALAMI_AND_SOBRASADA, SAUSAGE_AND_FUET, CURED_TAQUITOS, OTHER_CURED_MEATS_AND_SAUSAGES]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "CHISTORRA_AND_SAUSAGE":
                    aisles = [cls.CHISTORRA_AND_SAUSAGE]
                case "CHORIZO":
                    aisles = [cls.CHORIZO]
                case "PREPARED_SAUSAGES":
                    aisles = [cls.PREPARED_SAUSAGES]
                case "CURED_HAM":
                    aisles = [cls.CURED_HAM]
                case "CURED_HAM_PIECE":
                    aisles = [cls.CURED_HAM_PIECE]
                case "BACK":
                    aisles = [cls.BACK]
                case "BACON_AND_BLACK_PUDDING":
                    aisles = [cls.BACON_AND_BLACK_PUDDING]
                case "CURED_TURKEY_AND_OTHER_POULTRY":
                    aisles = [cls.CURED_TURKEY_AND_OTHER_POULTRY]
                case "SALAMI_AND_SOBRASADA":
                    aisles = [cls.SALAMI_AND_SOBRASADA]
                case "SAUSAGE_AND_FUET":
                    aisles = [cls.SAUSAGE_AND_FUET]
                case "CURED_TAQUITOS":
                    aisles = [cls.CURED_TAQUITOS]
                case "OTHER_CURED_MEATS_AND_SAUSAGES":
                    aisles = [cls.OTHER_CURED_MEATS_AND_SAUSAGES]
              
           
        return aisles
                                                          
class EroskiFreshColdCutsAndStewsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Fresh_Cold_cuts_and_stews")

    BACON = StaticAisle(name="Bacon",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059872-fiambres-y-cocidos/2059875-bacon/",
                                     original_file_uri=os.path.join(category_path(), "Bacon.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Bacon_detailed.json"))
    
    PIGS_HEAD = StaticAisle(name="Pig's head", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059872-fiambres-y-cocidos/2059877-cabeza-de-cerdo/",
                                     original_file_uri=os.path.join(category_path(), "Pigs_head.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pigs_head_detailed.json"))
    
    PORK_DELI_MEATS = StaticAisle(name="Pork deli meats",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059872-fiambres-y-cocidos/2059878-fiambres-de-cerdo/",
                                     original_file_uri=os.path.join(category_path(), "Pork_deli_meats.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pork_deli_meats_detailed.json"))
    
    COOKED_HAM = StaticAisle(name="Cooked ham",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059872-fiambres-y-cocidos/2059873-jamon-cocido/",
                                     original_file_uri=os.path.join(category_path(), "Cooked_ham.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cooked_ham_detailed.json"))
    
    TURKEY_AND_OTHER_COLD_CUTS = StaticAisle(name="Turkey and other cold cuts", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059872-fiambres-y-cocidos/2059874-pavo-y-otras-aves-fiambres/",
                                     original_file_uri=os.path.join(category_path(), "Turkey_and_other_cold_cuts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Turkey_and_other_cold_cuts_detailed.json"))
    
    COOKED_TAQUITOS = StaticAisle(name="Cooked Taquitos",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059872-fiambres-y-cocidos/2060854-taquitos-cocidos/",
                                     original_file_uri=os.path.join(category_path(), "Cooked_Taquitos.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cooked_Taquitos_detailed.json"))
    
    OTHER_COLD_CUTS_AND_STEWS = StaticAisle(name="Other cold cuts and stews", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059872-fiambres-y-cocidos/2059879-otros-fiambres-y-cocidos/",
                                     original_file_uri=os.path.join(category_path(), "Other_cold_cuts_and_stews.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_cold_cuts_and_stews_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [BACON, PIGS_HEAD, PORK_DELI_MEATS, COOKED_HAM, TURKEY_AND_OTHER_COLD_CUTS, COOKED_TAQUITOS, OTHER_COLD_CUTS_AND_STEWS]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "BACON":
                    aisles = [cls.BACON]
                case "PIGS_HEAD":
                    aisles = [cls.PIGS_HEAD]
                case "PORK_DELI_MEATS":
                    aisles = [cls.PORK_DELI_MEATS]
                case "COOKED_HAM":
                    aisles = [cls.COOKED_HAM]
                case "TURKEY_AND_OTHER_COLD_CUTS":
                    aisles = [cls.TURKEY_AND_OTHER_COLD_CUTS]
                case "COOKED_TAQUITOS":
                    aisles = [cls.COOKED_TAQUITOS]
                case "OTHER_COLD_CUTS_AND_STEWS":
                    aisles = [cls.OTHER_COLD_CUTS_AND_STEWS]
               
        return aisles
                                                          
class EroskiFreshFruitAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Fresh_Fruit")

    PLUMS_AND_GRAPES = StaticAisle(name="Plums and grapes",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059699-frutas/2059706-ciruelas-y-uvas/",
                                     original_file_uri=os.path.join(category_path(), "Plums_and_grapes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Plums_and_grapes_detailed.json"))
    
    STRAWBERRIES_CHERRIES_AND_BERRIES = StaticAisle(name="Strawberries, cherries and berries", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059699-frutas/2059704-fresas-cerezas-y-frutos-rojos/",
                                     original_file_uri=os.path.join(category_path(), "Strawberries_cherries_and_berries.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Strawberries_cherries_and_berries_detailed.json"))
    
    BROKEN_FRUIT_AND_JUICES = StaticAisle(name="Broken fruit and juices",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059699-frutas/2059709-fruta-partida-y-zumos/",
                                     original_file_uri=os.path.join(category_path(), "Broken_fruit_and_juices.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Broken_fruit_and_juices_detailed.json"))
    
    NUTS = StaticAisle(name="Nuts",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059699-frutas/5000105-frutos-secos/",
                                     original_file_uri=os.path.join(category_path(), "Nuts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Nuts_detailed.json"))
    
    APPLES_AND_PEARS = StaticAisle(name="Apples and pears", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059699-frutas/2059701-manzanas-y-peras/",
                                     original_file_uri=os.path.join(category_path(), "Apples_and_pears.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Apples_and_pears_detailed.json"))
    
    MELON_AND_WATERMELON = StaticAisle(name="Melon and watermelon",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059699-frutas/2059705-melon-y-sandia/",
                                     original_file_uri=os.path.join(category_path(), "Melon_and_watermelon.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Melon_and_watermelon_detailed.json"))
    
    ORANGES_AND_OTHER_CITRUS_FRUITS = StaticAisle(name="Oranges and other citrus fruits", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059872-fiambres-y-cocidos/2059879-otros-fiambres-y-cocidos/",
                                     original_file_uri=os.path.join(category_path(), "Oranges_and_other_citrus_fruits.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Oranges_and_other_citrus_fruits_detailed.json"))
    
    PINEAPPLE_AVOCADO_MANGO_AND_PAPAYA = StaticAisle(name="Pineapple, avocado, mango and papaya", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059699-frutas/2059703-pina-aguacate-mango-y-papaya/",
                                     original_file_uri=os.path.join(category_path(), "Pineapple_avocado_mango_and_papaya.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pineapple_avocado_mango_and_papaya_detailed.json"))
    
    BANANAS_AND_KIWIS = StaticAisle(name="Bananas and kiwis",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059699-frutas/2059702-platanos-y-kiwis/",
                                     original_file_uri=os.path.join(category_path(), "Bananas_and_kiwis.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Bananas_and_kiwis_detailed.json"))
    
    CASSAVA_COCONUT_AND_OTHERS = StaticAisle(name="Cassava, coconut and others", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059699-frutas/2059708-yuca-coco-y-otros/",
                                     original_file_uri=os.path.join(category_path(), "Cassava_coconut_and_others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cassava_coconut_and_others_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [PLUMS_AND_GRAPES, STRAWBERRIES_CHERRIES_AND_BERRIES, BROKEN_FRUIT_AND_JUICES, NUTS, APPLES_AND_PEARS, MELON_AND_WATERMELON, ORANGES_AND_OTHER_CITRUS_FRUITS, PINEAPPLE_AVOCADO_MANGO_AND_PAPAYA, BANANAS_AND_KIWIS, CASSAVA_COCONUT_AND_OTHERS]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "PLUMS_AND_GRAPES":
                    aisles = [cls.PLUMS_AND_GRAPES]
                case "STRAWBERRIES_CHERRIES_AND_BERRIES":
                    aisles = [cls.STRAWBERRIES_CHERRIES_AND_BERRIES]
                case "BROKEN_FRUIT_AND_JUICES":
                    aisles = [cls.BROKEN_FRUIT_AND_JUICES]
                case "NUTS":
                    aisles = [cls.NUTS]
                case "APPLES_AND_PEARS":
                    aisles = [cls.APPLES_AND_PEARS]
                case "MELON_AND_WATERMELON":
                    aisles = [cls.MELON_AND_WATERMELON]
                case "ORANGES_AND_OTHER_CITRUS_FRUITS":
                    aisles = [cls.ORANGES_AND_OTHER_CITRUS_FRUITS]
                case "PINEAPPLE_AVOCADO_MANGO_AND_PAPAYA":
                    aisles = [cls.PINEAPPLE_AVOCADO_MANGO_AND_PAPAYA]
                case "BANANAS_AND_KIWIS":
                    aisles = [cls.BANANAS_AND_KIWIS]
                case "CASSAVA_COCONUT_AND_OTHERS":
                    aisles = [cls.CASSAVA_COCONUT_AND_OTHERS]
               
        return aisles
                                                          
class EroskiFreshEggsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Fresh_Eggs")

    FREE_RANGE_AND_ORGANIC_EGGS = StaticAisle(name="Free-range and organic eggs",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059760-huevos/2059766-huevos-camperos-y-ecologicos/",
                                     original_file_uri=os.path.join(category_path(), "Free_range_and_organic_eggs.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Free_range_and_organic_eggs_detailed.json"))
    
    QUAIL_EGGS = StaticAisle(name="Quail eggs", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059760-huevos/2059767-huevos-de-codorniz/",
                                     original_file_uri=os.path.join(category_path(), "Quail_eggs.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Quail_eggs_detailed.json"))
    
    EGGS_SIZE_M = StaticAisle(name="Eggs size M",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059760-huevos/2059762-huevos-talla-m/",
                                     original_file_uri=os.path.join(category_path(), "Eggs_size_M.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Eggs_size_M_detailed.json"))
    
    EGGS_SIZE_L = StaticAisle(name="Eggs size L", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059760-huevos/2059763-huevos-talla-l/",
                                     original_file_uri=os.path.join(category_path(), "Eggs_size_L.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Eggs_size_L_detailed.json"))
    
    EGGS_SIZE_XL = StaticAisle(name="Eggs size XL",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059760-huevos/2059764-huevos-talla-xl/",
                                     original_file_uri=os.path.join(category_path(), "Eggs_size_XL.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Eggs_size_XL_detailed.json"))
    
    EGG_PRODUCTS = StaticAisle(name="Egg products", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059760-huevos/2059768-ovoproductos/",
                                     original_file_uri=os.path.join(category_path(), "Egg_products.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Egg_products_detailed.json"))

    
    aisles: Final[List[StaticAisle]] = [FREE_RANGE_AND_ORGANIC_EGGS, QUAIL_EGGS, EGGS_SIZE_M, EGGS_SIZE_L, EGGS_SIZE_XL, EGG_PRODUCTS]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "FREE_RANGE_AND_ORGANIC_EGGS":
                    aisles = [cls.FREE_RANGE_AND_ORGANIC_EGGS]
                case "QUAIL_EGGS":
                    aisles = [cls.QUAIL_EGGS]
                case "EGGS_SIZE_M":
                    aisles = [cls.EGGS_SIZE_M]
                case "EGGS_SIZE_L":
                    aisles = [cls.EGGS_SIZE_L]
                case "EGGS_SIZE_XL":
                    aisles = [cls.EGGS_SIZE_XL]
                case "EGG_PRODUCTS":
                    aisles = [cls.EGG_PRODUCTS]
                  
        return aisles
                                                          
class EroskiFreshIberianSausagesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Fresh_Iberian_sausages")

    IBERIAN_CHORIZO = StaticAisle(name="Iberian chorizo",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059894-ibericos/2059897-chorizo-iberico/",
                                     original_file_uri=os.path.join(category_path(), "Iberian_chorizo.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Iberian_chorizo_detailed.json"))
    
    IBERIAN_HAM = StaticAisle(name="Iberian ham", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059894-ibericos/2059895-jamon-iberico/",
                                     original_file_uri=os.path.join(category_path(), "Iberian_ham.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Iberian_ham_detailed.json"))
    
    IBERIAN_HAM_PIECE = StaticAisle(name="Iberian ham piece",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059894-ibericos/2059896-jamon-iberico-pieza/",
                                     original_file_uri=os.path.join(category_path(), "Iberian_ham_piece.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Iberian_ham_piece_detailed.json"))
    
    IBERIAN_LOIN = StaticAisle(name="Iberian loin", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059894-ibericos/2059898-lomo-iberico/",
                                     original_file_uri=os.path.join(category_path(), "Iberian_loin.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Iberian_loin_detailed.json"))
    
    IBERIAN_SAUSAGE = StaticAisle(name="Iberian sausage",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059894-ibericos/2059899-salchichon-iberico/",
                                     original_file_uri=os.path.join(category_path(), "Iberian_sausage.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Iberian_sausage_detailed.json"))
    
    OTHER_IBERIAN_HAMS = StaticAisle(name="Other Iberian hams", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059894-ibericos/2059900-otros-ibericos/",
                                     original_file_uri=os.path.join(category_path(), "Other_Iberian_hams.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_Iberian_hams_detailed.json"))

    
    aisles: Final[List[StaticAisle]] = [IBERIAN_CHORIZO, IBERIAN_HAM, IBERIAN_HAM_PIECE, IBERIAN_LOIN, IBERIAN_SAUSAGE, OTHER_IBERIAN_HAMS]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "IBERIAN_CHORIZO":
                    aisles = [cls.IBERIAN_CHORIZO]
                case "IBERIAN_HAM":
                    aisles = [cls.IBERIAN_HAM]
                case "IBERIAN_HAM_PIECE":
                    aisles = [cls.IBERIAN_HAM_PIECE]
                case "IBERIAN_LOIN":
                    aisles = [cls.IBERIAN_LOIN]
                case "IBERIAN_SAUSAGE":
                    aisles = [cls.IBERIAN_SAUSAGE]
                case "OTHER_IBERIAN_HAMS":
                    aisles = [cls.OTHER_IBERIAN_HAMS]
                  
        return aisles
                                                          
class EroskiFreshSeafoodAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Fresh_Seafood")

    CLAM_MUSSEL_SCALLOP_AND_RAZOR_CLAM = StaticAisle(name="Clam, mussel, scallop and razor clam",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059736-mariscos/2059740-almeja-mejillon-vieira-y-navaja/",
                                     original_file_uri=os.path.join(category_path(), "Clam_mussel_scallop_and_razor_clam.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Clam_mussel_scallop_and_razor_clam_detailed.json"))
    
    PERIWINKLES_CRABS_AND_OTHERS = StaticAisle(name="Periwinkles, crabs and others", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059736-mariscos/2059743-bigaros-cangrejos-y-otros/",
                                     original_file_uri=os.path.join(category_path(), "Periwinkles_crabs_and_others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Periwinkles_crabs_and_others_detailed.json"))
    
    BEEF_SPIDER_CRAB_AND_CRAB = StaticAisle(name="Beef, spider crab and crab",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059736-mariscos/2059741-buey-centollo-y-necora/",
                                     original_file_uri=os.path.join(category_path(), "Beef_spider_crab_and_crab.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Beef_spider_crab_and_crab_detailed.json"))
    
    PRAWNS_AND_LANGOUSTINES = StaticAisle(name="Prawns and langoustines", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059736-mariscos/2059739-gambas-y-cigalas/",
                                     original_file_uri=os.path.join(category_path(), "Prawns_and_langoustines.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Prawns_and_langoustines_detailed.json"))
    
    COOKED_PRAWNS = StaticAisle(name="Cooked prawns",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059736-mariscos/2059737-langostino-cocido/",
                                     original_file_uri=os.path.join(category_path(), "Cooked_prawns.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cooked_prawns_detailed.json"))
    
    RAW_PRAWNS = StaticAisle(name="Raw prawns", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059736-mariscos/2059738-langostino-crudo/",
                                     original_file_uri=os.path.join(category_path(), "Raw_prawns.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Raw_prawnss_detailed.json"))

    
    aisles: Final[List[StaticAisle]] = [CLAM_MUSSEL_SCALLOP_AND_RAZOR_CLAM, PERIWINKLES_CRABS_AND_OTHERS, BEEF_SPIDER_CRAB_AND_CRAB, PRAWNS_AND_LANGOUSTINES, COOKED_PRAWNS, RAW_PRAWNS]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "CLAM_MUSSEL_SCALLOP_AND_RAZOR_CLAM":
                    aisles = [cls.CLAM_MUSSEL_SCALLOP_AND_RAZOR_CLAM]
                case "PERIWINKLES_CRABS_AND_OTHERS":
                    aisles = [cls.PERIWINKLES_CRABS_AND_OTHERS]
                case "BEEF_SPIDER_CRAB_AND_CRAB":
                    aisles = [cls.BEEF_SPIDER_CRAB_AND_CRAB]
                case "PRAWNS_AND_LANGOUSTINES":
                    aisles = [cls.PRAWNS_AND_LANGOUSTINES]
                case "COOKED_PRAWNS":
                    aisles = [cls.COOKED_PRAWNS]
                case "RAW_PRAWNS":
                    aisles = [cls.RAW_PRAWNS]
                  
        return aisles
                                                                                              
class EroskiFreshBakeryAndPastryAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Fresh_Bakery_and_pastry")

    WHITE_BREAD = StaticAisle(name="White bread",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059783-panaderia-y-pasteleria/2059785-pan-blanco/",
                                     original_file_uri=os.path.join(category_path(), "White_bread.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "White_bread_detailed.json"))
    
    TRADITIONAL_BREAD = StaticAisle(name="Traditional bread", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059783-panaderia-y-pasteleria/2059786-pan-tradicional/",
                                     original_file_uri=os.path.join(category_path(), "Traditional_bread.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Traditional_bread_detailed.json"))
    
    BURGER_MOLD_AND_OTHERS = StaticAisle(name="Burger, mold and others",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059783-panaderia-y-pasteleria/2059791-burguer-de-molde-y-otros/",
                                     original_file_uri=os.path.join(category_path(), "Burger_mold_and_others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Burger_mold_and_others_detailed.json"))
    
    GLUTEN_FREE_BREAD = StaticAisle(name="Gluten-free bread", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059783-panaderia-y-pasteleria/2059795-pan-sin-gluten/",
                                     original_file_uri=os.path.join(category_path(), "Gluten_free_bread.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Gluten_free_bread_detailed.json"))
    
    CROISSANTS_NEAPOLITANS_AND_OTHERS = StaticAisle(name="Croissants, Neapolitans and others",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059783-panaderia-y-pasteleria/2059802-croissants-napolitanas-y-otros/",
                                     original_file_uri=os.path.join(category_path(), "Croissants_Neapolitans_and_others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Croissants_Neapolitans_and_others_detailed.json"))
    
    PASTRIES = StaticAisle(name="Pastries", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059783-panaderia-y-pasteleria/2059803-hojaldres-/",
                                     original_file_uri=os.path.join(category_path(), "Pastries.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pastries_detailed.json"))
    
    EMPANADAS_AND_SAVOURY_PASTRIES = StaticAisle(name="Empanadas and savoury pastries",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059783-panaderia-y-pasteleria/2059794-empanadas-y-bolleria-salada/",
                                     original_file_uri=os.path.join(category_path(), "Empanadas_and_savoury_pastries.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Empanadas_and_savoury_pastries_detailed.json"))
    
    SALOONS_AND_OTHERS = StaticAisle(name="Saloons and others", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059783-panaderia-y-pasteleria/4000014-berlinas-y-otros/",
                                     original_file_uri=os.path.join(category_path(), "Saloons_and_others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Saloons_and_others_detailed.json"))
    
    BISCUITS_AND_OTHERS = StaticAisle(name="Biscuits and others",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059783-panaderia-y-pasteleria/2059804-bizcochos-y-otros/",
                                     original_file_uri=os.path.join(category_path(), "Biscuits_and_others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Biscuits_and_others_detailed.json"))
    
    MUFFINS_AND_DONUTS = StaticAisle(name="Muffins and donuts", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059783-panaderia-y-pasteleria/4000015-magdalenas-y-rosquillas/",
                                     original_file_uri=os.path.join(category_path(), "Muffins_and_donuts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Muffins_and_donuts_detailed.json"))
    
    TEA_CAKES_AND_VOL_AUVANES = StaticAisle(name="Tea cakes and vol-auvanes",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059783-panaderia-y-pasteleria/4000016-pastas-de-te-y-volovanes/",
                                     original_file_uri=os.path.join(category_path(), "Tea_cakes_and_vol_auvanes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tea_cakes_and_vol_auvanes_detailed.json"))
    
    CAKES_AND_TARTS = StaticAisle(name="Cakes and tarts", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059783-panaderia-y-pasteleria/2059800-pasteles-y-tartas/",
                                     original_file_uri=os.path.join(category_path(), "Cakes_and_tarts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cakes_and_tarts_detailed.json"))

    
    aisles: Final[List[StaticAisle]] = [WHITE_BREAD, TRADITIONAL_BREAD, BURGER_MOLD_AND_OTHERS, GLUTEN_FREE_BREAD, CROISSANTS_NEAPOLITANS_AND_OTHERS, PASTRIES, EMPANADAS_AND_SAVOURY_PASTRIES, SALOONS_AND_OTHERS, BISCUITS_AND_OTHERS, MUFFINS_AND_DONUTS, TEA_CAKES_AND_VOL_AUVANES, CAKES_AND_TARTS]
    

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "WHITE_BREAD":
                    aisles = [cls.WHITE_BREAD]
                case "TRADITIONAL_BREAD":
                    aisles = [cls.TRADITIONAL_BREAD]
                case "BURGER_MOLD_AND_OTHERS":
                    aisles = [cls.BURGER_MOLD_AND_OTHERS]
                case "GLUTEN_FREE_BREAD":
                    aisles = [cls.GLUTEN_FREE_BREAD]
                case "CROISSANTS_NEAPOLITANS_AND_OTHERS":
                    aisles = [cls.CROISSANTS_NEAPOLITANS_AND_OTHERS]
                case "PASTRIES":
                    aisles = [cls.PASTRIES]
                case "EMPANADAS_AND_SAVOURY_PASTRIES":
                    aisles = [cls.EMPANADAS_AND_SAVOURY_PASTRIES]
                case "SALOONS_AND_OTHERS":
                    aisles = [cls.SALOONS_AND_OTHERS]
                case "BISCUITS_AND_OTHERS":
                    aisles = [cls.BISCUITS_AND_OTHERS]
                case "MUFFINS_AND_DONUTS":
                    aisles = [cls.MUFFINS_AND_DONUTS]
                case "TEA_CAKES_AND_VOL_AUVANES":
                    aisles = [cls.TEA_CAKES_AND_VOL_AUVANES]
                case "CAKES_AND_TARTS":
                    aisles = [cls.CAKES_AND_TARTS]
                  
        return aisles
                                                          
class EroskiFreshFishAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Fresh_Fish")

    SMOKED_ROE_AND_SALTED = StaticAisle(name="Smoked, roe and salted",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059722-pescados/2059734-ahumados-huevas-y-salazones/",
                                     original_file_uri=os.path.join(category_path(), "Smoked_roe_and_salted.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Smoked_roe_and_salted_detailed.json"))
    
    ANCHOVY_SARDINES_MACKEREL_AND_MACKEREL = StaticAisle(name="Anchovy, sardines, mackerel and mackerel", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059722-pescados/2059724-anchoa-sardina-chicharro-y-verdel/",
                                     original_file_uri=os.path.join(category_path(), "Anchovy_sardines_mackerel_and_mackerel.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Anchovy_sardines_mackerel_and_mackerel_detailed.json"))
    
    ANCHOVIES_AND_ANCHOVIES = StaticAisle(name="Anchovies and anchovies",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059722-pescados/2059735-anchoas-y-boquerones-conserva/",
                                     original_file_uri=os.path.join(category_path(), "Anchovies_and_anchovies.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Anchovies_and_anchovies_detailed.json"))
    
    BONITO_TUNA_AND_SWORDFISH = StaticAisle(name="Bonito, tuna and swordfish", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059722-pescados/2059728-bonito-atun-y-pez-espada/",
                                     original_file_uri=os.path.join(category_path(), "Bonito_tuna_and_swordfish.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Bonito_tuna_and_swordfish_detailed.json"))
    
    SQUID_CUTTLEFISH_AND_OCTOPUS = StaticAisle(name="Squid, cuttlefish and octopus",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059722-pescados/2059731-calamar-sepia-y-pulpo/",
                                     original_file_uri=os.path.join(category_path(), "Squid_cuttlefish_and_octopus.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Squid_cuttlefish_and_octopus_detailed.json"))
    
    CONGER_EEL_AND_MONKFISH = StaticAisle(name="Conger eel and monkfish", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059722-pescados/2059729-congrio-y-rape/",
                                     original_file_uri=os.path.join(category_path(), "Conger_eel_and_monkfish.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Conger_eel_and_monkfish_detailed.json"))
    
    ROOSTER_SOLE_AND_COD = StaticAisle(name="Rooster, sole and cod",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059722-pescados/2059725-gallo-lenguadina-y-bacalao/",
                                     original_file_uri=os.path.join(category_path(), "Rooster_sole_and_cod.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Rooster_sole_and_cod_detailed.json"))
    
    EEL_SUBSTITUTE_AND_SURIMI = StaticAisle(name="Eel substitute and surimi", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059722-pescados/2059733-sucedaneo-de-angulas-y-surimi/",
                                     original_file_uri=os.path.join(category_path(), "Eel_substitute_and_surimi.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Eel_substitute_and_surimi_detailed.json"))
    
    HAKE_LILY_AND_WHITING = StaticAisle(name="Hake, lily and whiting",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059722-pescados/2059723-merluza-lirio-y-pescadilla/",
                                     original_file_uri=os.path.join(category_path(), "Hake_lily_and_whiting.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Hake_lily_and_whiting_detailed.json"))
    
    SEA_BASS_SEA_BREAM_TURBOT_AND_SEA_BREAM = StaticAisle(name="Sea bass, sea bream, turbot and sea bream", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059722-pescados/2059726-lubina-dorada-rodaballo-y-besugo/",
                                     original_file_uri=os.path.join(category_path(), "Sea_bass_sea_bream_turbot_and_sea_bream.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sea_bass_sea_bream_turbot_and_sea_bream_detailed.json"))
    
    PREPARED_FISH_AND_OTHER = StaticAisle(name="Prepared fish and other",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059722-pescados/2059732-pescados-preparados-y-otros/",
                                     original_file_uri=os.path.join(category_path(), "Prepared_fish_and_other.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Prepared_fish_and_other_detailed.json"))
    
    SALMON_AND_TROUT = StaticAisle(name="Salmon and Trout", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059722-pescados/2059727-salmon-y-trucha/",
                                     original_file_uri=os.path.join(category_path(), "Salmon_and_Trout.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Salmon_and_Trout_detailed.json"))

    
    aisles: Final[List[StaticAisle]] = [SMOKED_ROE_AND_SALTED, ANCHOVY_SARDINES_MACKEREL_AND_MACKEREL, ANCHOVIES_AND_ANCHOVIES, BONITO_TUNA_AND_SWORDFISH, SQUID_CUTTLEFISH_AND_OCTOPUS, CONGER_EEL_AND_MONKFISH, ROOSTER_SOLE_AND_COD, EEL_SUBSTITUTE_AND_SURIMI, HAKE_LILY_AND_WHITING, SEA_BASS_SEA_BREAM_TURBOT_AND_SEA_BREAM, PREPARED_FISH_AND_OTHER, SALMON_AND_TROUT]
    

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "SMOKED_ROE_AND_SALTED":
                    aisles = [cls.SMOKED_ROE_AND_SALTED]
                case "ANCHOVY_SARDINES_MACKEREL_AND_MACKEREL":
                    aisles = [cls.ANCHOVY_SARDINES_MACKEREL_AND_MACKEREL]
                case "ANCHOVIES_AND_ANCHOVIES":
                    aisles = [cls.ANCHOVIES_AND_ANCHOVIES]
                case "BONITO_TUNA_AND_SWORDFISH":
                    aisles = [cls.BONITO_TUNA_AND_SWORDFISH]
                case "SQUID_CUTTLEFISH_AND_OCTOPUS":
                    aisles = [cls.SQUID_CUTTLEFISH_AND_OCTOPUS]
                case "CONGER_EEL_AND_MONKFISH":
                    aisles = [cls.CONGER_EEL_AND_MONKFISH]
                case "ROOSTER_SOLE_AND_COD":
                    aisles = [cls.ROOSTER_SOLE_AND_COD]
                case "EEL_SUBSTITUTE_AND_SURIMI":
                    aisles = [cls.EEL_SUBSTITUTE_AND_SURIMI]
                case "HAKE_LILY_AND_WHITING":
                    aisles = [cls.HAKE_LILY_AND_WHITING]
                case "SEA_BASS_SEA_BREAM_TURBOT_AND_SEA_BREAM":
                    aisles = [cls.SEA_BASS_SEA_BREAM_TURBOT_AND_SEA_BREAM]
                case "PREPARED_FISH_AND_OTHER":
                    aisles = [cls.PREPARED_FISH_AND_OTHER]
                case "SALMON_AND_TROUT":
                    aisles = [cls.SALMON_AND_TROUT]
                  
        return aisles
                                                          
class EroskiFreshReadyMealsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Fresh_Ready_meals")

    HEAT_AND_READY = StaticAisle(name="Heat and Ready",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059769-platos-preparados/5000145-calentar-y-listo/",
                                     original_file_uri=os.path.join(category_path(), "Heat_and_Ready.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Heat_and_Ready_detailed.json"))
    
    ENJOY_COOKING = StaticAisle(name="Enjoy cooking", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059769-platos-preparados/5000146-disfruta-cocinando/",
                                     original_file_uri=os.path.join(category_path(), "Enjoy_cooking.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Enjoy_cooking_detailed.json"))
    
    READY_TO_EAT = StaticAisle(name="Ready to eat",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059769-platos-preparados/5000144-listo-para-comer/",
                                     original_file_uri=os.path.join(category_path(), "Ready_to_eat.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Ready_to_eat_detailed.json"))
    
    PIZZA = StaticAisle(name="Pizza", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059769-platos-preparados/4000012-pizza/",
                                     original_file_uri=os.path.join(category_path(), "Pizza.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pizza_detailed.json"))
    
    SUSHI = StaticAisle(name="Sushi",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059769-platos-preparados/4000011-sushi/",
                                     original_file_uri=os.path.join(category_path(), "Sushi.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sushi_detailed.json"))
   

    
    aisles: Final[List[StaticAisle]] = [HEAT_AND_READY, ENJOY_COOKING, READY_TO_EAT, PIZZA, SUSHI]
    

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "HEAT_AND_READY":
                    aisles = [cls.HEAT_AND_READY]
                case "ENJOY_COOKING":
                    aisles = [cls.ENJOY_COOKING]
                case "READY_TO_EAT":
                    aisles = [cls.READY_TO_EAT]
                case "PIZZA":
                    aisles = [cls.PIZZA]
                case "SUSHI":
                    aisles = [cls.SUSHI]
                 
        return aisles
                                                          
class EroskiFreshCheeseAndQuinceAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Fresh_Cheese_and_quince")

    CHILDRENS_AND_PORTIONS = StaticAisle(name="Children's and portions",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059858-queso-y-membrillo/2059867-infantiles-y-porciones/",
                                     original_file_uri=os.path.join(category_path(), "Childrens_and_portions.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Childrens_and_portions_detailed.json"))
    
    BLUE_CHEESE = StaticAisle(name="Blue cheese", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059858-queso-y-membrillo/2059865-queso-azul/",
                                     original_file_uri=os.path.join(category_path(), "Blue_cheese.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Blue_cheese_detailed.json"))
    
    CURED_AND_OLD_CHEESE = StaticAisle(name="Cured and old cheese",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059858-queso-y-membrillo/2059862-queso-curado-y-viejo/",
                                     original_file_uri=os.path.join(category_path(), "Cured_and_old_cheese.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cured_and_old_cheese_detailed.json"))
    
    FRESH_CHEESE = StaticAisle(name="Fresh cheese", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059858-queso-y-membrillo/2059859-queso-fresco/",
                                     original_file_uri=os.path.join(category_path(), "Fresh_cheese.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fresh_cheese_detailed.json"))
    
    SLICED_AND_MELTED_CHEESE = StaticAisle(name="Sliced and melted cheese",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059858-queso-y-membrillo/2059863-queso-lonchas-y-fundidos/",
                                     original_file_uri=os.path.join(category_path(), "Sliced_and_melted_cheese.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sliced_and_melted_cheese_detailed.json"))
   
    SEMI_CURED_CHEESE = StaticAisle(name="Semi-cured cheese",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059858-queso-y-membrillo/2059861-queso-semicurado-/",
                                     original_file_uri=os.path.join(category_path(), "Semi_cured_cheese.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Semi_cured_cheese_detailed.json"))
    
    SOFT_CHEESE = StaticAisle(name="Soft cheese", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059858-queso-y-membrillo/2059860-queso-tierno/",
                                     original_file_uri=os.path.join(category_path(), "Soft_cheese.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Soft_cheese_detailed.json"))
    
    INTERNATIONAL_CHEESES = StaticAisle(name="International cheeses",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059858-queso-y-membrillo/2059864-quesos-internacionales/",
                                     original_file_uri=os.path.join(category_path(), "International_cheeses.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "International_cheeses_detailed.json"))
    
    TUB_CHEESE = StaticAisle(name="Tub cheese", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059858-queso-y-membrillo/2059868-queso-tarrina/",
                                     original_file_uri=os.path.join(category_path(), "Tub_cheese.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tub_cheese_detailed.json"))
    
    SHREDDED_CHEESE = StaticAisle(name="Shredded cheese",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059858-queso-y-membrillo/2059869-queso-rallado/",
                                     original_file_uri=os.path.join(category_path(), "Shredded_cheese.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Shredded_cheese_detailed.json"))
   
    CHEESE_BOARDS_AND_TRAYS = StaticAisle(name="Cheese boards and trays",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059858-queso-y-membrillo/2059870-tablas-y-bandejas-de-queso-/",
                                     original_file_uri=os.path.join(category_path(), "Cheese_boards_and_trays.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cheese_boards_and_trays_detailed.json"))
    
    QUINCE = StaticAisle(name="Quince", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059858-queso-y-membrillo/2059871-membrillo/",
                                     original_file_uri=os.path.join(category_path(), "Quince.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Quince_detailed.json"))
  
   
    aisles: Final[List[StaticAisle]] = [CHILDRENS_AND_PORTIONS, BLUE_CHEESE, CURED_AND_OLD_CHEESE, FRESH_CHEESE, SLICED_AND_MELTED_CHEESE, SEMI_CURED_CHEESE, SOFT_CHEESE, INTERNATIONAL_CHEESES, TUB_CHEESE, SHREDDED_CHEESE, CHEESE_BOARDS_AND_TRAYS, QUINCE]
    

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "CHILDRENS_AND_PORTIONS":
                    aisles = [cls.CHILDRENS_AND_PORTIONS]
                case "BLUE_CHEESE":
                    aisles = [cls.BLUE_CHEESE]
                case "CURED_AND_OLD_CHEESE":
                    aisles = [cls.CURED_AND_OLD_CHEESE]
                case "SLICED_AND_MELTED_CHEESE":
                    aisles = [cls.SLICED_AND_MELTED_CHEESE]
                case "SEMI_CURED_CHEESE":
                    aisles = [cls.SEMI_CURED_CHEESE]
                case "SOFT_CHEESE":
                    aisles = [cls.SOFT_CHEESE]
                case "INTERNATIONAL_CHEESES":
                    aisles = [cls.INTERNATIONAL_CHEESES]
                case "TUB_CHEESE":
                    aisles = [cls.TUB_CHEESE]
                case "SHREDDED_CHEESE":
                    aisles = [cls.SHREDDED_CHEESE]
                case "CHEESE_BOARDS_AND_TRAYS":
                    aisles = [cls.CHEESE_BOARDS_AND_TRAYS]
                case "QUINCE":
                    aisles = [cls.QUINCE]
                 
        return aisles
                                                          
class EroskiFreshSausagesPâtéAndFoieGrasAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Fresh_Sausages_pâté_and_foie_gras")

    CREAMS_SOBRASADAS_AND_BUTTERS = StaticAisle(name="Creams, sobrasadas and butters",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059901-salchichas-pates-y-foie/2059913-cremas-sobrasadas-y-mantecas/",
                                     original_file_uri=os.path.join(category_path(), "Creams_sobrasadas_and_butters.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Creams_sobrasadas_and_butters_detailed.json"))
    
    FOIE_GRAS_AND_PÂTÉS = StaticAisle(name="Foie gras and pâtés", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059901-salchichas-pates-y-foie/2059916-foie-gras-y-pates/",
                                     original_file_uri=os.path.join(category_path(), "Foie_gras_and_pâtés.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Foie_gras_and_pâtés_detailed.json"))
    
    PORK_PÂTÉ = StaticAisle(name="Pork pâté",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059901-salchichas-pates-y-foie/2059911-pate-de-cerdo/",
                                     original_file_uri=os.path.join(category_path(), "Pork_pâté.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pork_pâté_detailed.json"))
    
    DUCK_AND_GOOSE_PÂTÉ = StaticAisle(name="Duck and goose pâté", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059901-salchichas-pates-y-foie/2059910-pate-de-pato-y-oca/",
                                     original_file_uri=os.path.join(category_path(), "Duck_and_goose_pâté.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Duck_and_goose_pâté_detailed.json"))
    
    ORGANIC_PÂTÉ = StaticAisle(name="Organic pâté",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059901-salchichas-pates-y-foie/2060964-pate-ecologico/",
                                     original_file_uri=os.path.join(category_path(), "Organic_pâté.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_pâté_detailed.json"))
   
    FISH_PÂTÉ_AND_OTHERS = StaticAisle(name="Fish pâté and others",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059901-salchichas-pates-y-foie/2059915-pate-de-pescado-y-otros/",
                                     original_file_uri=os.path.join(category_path(), "Fish_pâté_and_others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fish_pâté_and_others_detailed.json"))
    
    GOURMET_PÂTÉS = StaticAisle(name="Gourmet pâtés", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059901-salchichas-pates-y-foie/2059914-pates-gourmet/",
                                     original_file_uri=os.path.join(category_path(), "Gourmet_pâtés.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Gourmet_pâtés_detailed.json"))
    
    WHITE_SAUSAGES = StaticAisle(name="White sausages",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059901-salchichas-pates-y-foie/2059906-salchichas-blancas/",
                                     original_file_uri=os.path.join(category_path(), "White_sausages.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "White_sausages_detailed.json"))
    
    SPECIAL_SAUSAGES = StaticAisle(name="Special sausages", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059901-salchichas-pates-y-foie/2059908-salchichas-especiales/",
                                     original_file_uri=os.path.join(category_path(), "Special_sausages.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Special_sausages_detailed.json"))
    
    FRANKFURT_SAUSAGES = StaticAisle(name="Frankfurt sausages",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059901-salchichas-pates-y-foie/2059902-salchichas-frankfurt/",
                                     original_file_uri=os.path.join(category_path(), "Frankfurt_sausages.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Frankfurt_sausages_detailed.json"))
   
    THICK_SAUSAGES = StaticAisle(name="Thick sausages",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059901-salchichas-pates-y-foie/2059907-salchichas-gruesas/",
                                     original_file_uri=os.path.join(category_path(), "Thick_sausages.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Thick_sausages_detailed.json"))
    
    SAUSAGES_CHICKEN_AND_TURKEY = StaticAisle(name="Sausages, chicken and turkey", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059901-salchichas-pates-y-foie/2059904-salchichas-pollo-y-pavo/",
                                     original_file_uri=os.path.join(category_path(), "Sausages_chicken_and_turkey.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sausages_chicken_and_turkey_detailed.json"))
   
    SAUSAGES_CHEESE = StaticAisle(name="Sausages cheese",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059901-salchichas-pates-y-foie/2059905-salchichas-queso/",
                                     original_file_uri=os.path.join(category_path(), "Sausages_cheese.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sausages_cheese_detailed.json"))
    
    VIENNA_SAUSAGES = StaticAisle(name="Vienna Sausages", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059901-salchichas-pates-y-foie/2059903-salchichas-viena/",
                                     original_file_uri=os.path.join(category_path(), "Vienna_Sausages.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vienna_Sausages_detailed.json"))
  
   
    aisles: Final[List[StaticAisle]] = [CREAMS_SOBRASADAS_AND_BUTTERS, FOIE_GRAS_AND_PÂTÉS, PORK_PÂTÉ, DUCK_AND_GOOSE_PÂTÉ, ORGANIC_PÂTÉ, FISH_PÂTÉ_AND_OTHERS, GOURMET_PÂTÉS, WHITE_SAUSAGES, SPECIAL_SAUSAGES, FRANKFURT_SAUSAGES, THICK_SAUSAGES, SAUSAGES_CHICKEN_AND_TURKEY, SAUSAGES_CHEESE, VIENNA_SAUSAGES]
    

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "CREAMS_SOBRASADAS_AND_BUTTERS":
                    aisles = [cls.CREAMS_SOBRASADAS_AND_BUTTERS]
                case "FOIE_GRAS_AND_PÂTÉS":
                    aisles = [cls.FOIE_GRAS_AND_PÂTÉS]
                case "PORK_PÂTÉ":
                    aisles = [cls.PORK_PÂTÉ]
                case "DUCK_AND_GOOSE_PÂTÉ":
                    aisles = [cls.DUCK_AND_GOOSE_PÂTÉ]
                case "ORGANIC_PÂTÉ":
                    aisles = [cls.ORGANIC_PÂTÉ]
                case "FISH_PÂTÉ_AND_OTHERS":
                    aisles = [cls.FISH_PÂTÉ_AND_OTHERS]
                case "GOURMET_PÂTÉS":
                    aisles = [cls.GOURMET_PÂTÉS]
                case "WHITE_SAUSAGES":
                    aisles = [cls.WHITE_SAUSAGES]
                case "SPECIAL_SAUSAGES":
                    aisles = [cls.SPECIAL_SAUSAGES]
                case "FRANKFURT_SAUSAGES":
                    aisles = [cls.FRANKFURT_SAUSAGES]
                case "THICK_SAUSAGES":
                    aisles = [cls.THICK_SAUSAGES]
                case "SAUSAGES_CHICKEN_AND_TURKEY":
                    aisles = [cls.SAUSAGES_CHICKEN_AND_TURKEY]
                case "SAUSAGES_CHEESE":
                    aisles = [cls.SAUSAGES_CHEESE]
                case "VIENNA_SAUSAGES":
                    aisles = [cls.VIENNA_SAUSAGES]
                 
        return aisles
                                                          
class EroskiFreshVegetablesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Fresh_Vegetables")

    SWISS_CHARD_SPINACH_AND_OTHERS = StaticAisle(name="Swiss chard, spinach and others",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059710-verduras-y-hortalizas/2059719-acelgas-espinacas-y-otras/",
                                     original_file_uri=os.path.join(category_path(), "Swiss_chard_spinach_and_others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Swiss_chard_spinach_and_others_detailed.json"))
    
    GARLIC_AND_ONIONS = StaticAisle(name="Garlic and onions", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059710-verduras-y-hortalizas/2059712-ajos-y-cebollas/",
                                     original_file_uri=os.path.join(category_path(), "Garlic_and_onions.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Garlic_and_onions_detailed.json"))
    
    AUBERGINE_PUMPKIN_AND_ZUCCHINI = StaticAisle(name="Aubergine, pumpkin and zucchini",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059710-verduras-y-hortalizas/2059717-berenjena-calabaza-y-calabacin/",
                                     original_file_uri=os.path.join(category_path(), "Aubergine_pumpkin_and_zucchini.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Aubergine_pumpkin_and_zucchini_detailed.json"))
    
    READY_TO_EAT_SALADS = StaticAisle(name="Ready-to-eat salads", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059710-verduras-y-hortalizas/2059715-ensaladas-listas-para-consumir/",
                                     original_file_uri=os.path.join(category_path(), "Ready_to_eat_salads.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Ready_to_eat_salads_detailed.json"))
    
    MUSHROOMS = StaticAisle(name="Mushrooms",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059710-verduras-y-hortalizas/2059718-hongos-setas-y-champinones/",
                                     original_file_uri=os.path.join(category_path(), "Mushrooms.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mushrooms_detailed.json"))
   
    LETTUCE_CUCUMBER_AND_OTHERS = StaticAisle(name="Lettuce, cucumber and others",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059710-verduras-y-hortalizas/2059716-lechuga-pepino-y-otros/",
                                     original_file_uri=os.path.join(category_path(), "Lettuce_cucumber_and_others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Lettuce_cucumber_and_others_detailed.json"))
    
    POTATOES_AND_CARROTS = StaticAisle(name="Potatoes and carrots", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059710-verduras-y-hortalizas/2059711-patatas-y-zanahorias/",
                                     original_file_uri=os.path.join(category_path(), "Potatoes_and_carrots.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Potatoes_and_carrots_detailed.json"))
    
    PREPARED_AND_PRE_COOKED = StaticAisle(name="Prepared and pre-cooked",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059710-verduras-y-hortalizas/2059720-preparados-y-precocinados/",
                                     original_file_uri=os.path.join(category_path(), "Prepared_and_pre_cooked.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Prepared_and_pre_cooked_detailed.json"))
    
    LEEKS_BEANS_LEGUMES_AND_CABBAGES = StaticAisle(name="Leeks, beans, legumes and cabbages", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059710-verduras-y-hortalizas/2059713-puerros-judias-legumbres-y-repollos/",
                                     original_file_uri=os.path.join(category_path(), "Leeks_beans_legumes_and_cabbages.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Leeks_beans_legumes_and_cabbages_detailed.json"))
    
    SAUCES_HERBS_AND_SPICES = StaticAisle(name="Sauces, herbs and spices",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059710-verduras-y-hortalizas/2059721-salsas-hierbas-y-especias/",
                                     original_file_uri=os.path.join(category_path(), "Sauces_herbs_and_spices.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sauces_herbs_and_spices_detailed.json"))
   
    TOMATOES_AND_PEPPERS = StaticAisle(name="Tomatoes and peppers",  url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059710-verduras-y-hortalizas/2059714-tomates-y-pimientos/",
                                     original_file_uri=os.path.join(category_path(), "Tomatoes_and_peppers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tomatoes_and_peppers_detailed.json"))
    
  
   
    aisles: Final[List[StaticAisle]] = [SWISS_CHARD_SPINACH_AND_OTHERS, GARLIC_AND_ONIONS, AUBERGINE_PUMPKIN_AND_ZUCCHINI, READY_TO_EAT_SALADS, MUSHROOMS, LETTUCE_CUCUMBER_AND_OTHERS, POTATOES_AND_CARROTS, PREPARED_AND_PRE_COOKED, LEEKS_BEANS_LEGUMES_AND_CABBAGES, SAUCES_HERBS_AND_SPICES, TOMATOES_AND_PEPPERS]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "SWISS_CHARD_SPINACH_AND_OTHERS":
                    aisles = [cls.SWISS_CHARD_SPINACH_AND_OTHERS]
                case "GARLIC_AND_ONIONS":
                    aisles = [cls.GARLIC_AND_ONIONS]
                case "AUBERGINE_PUMPKIN_AND_ZUCCHINI":
                    aisles = [cls.AUBERGINE_PUMPKIN_AND_ZUCCHINI]
                case "READY_TO_EAT_SALADS":
                    aisles = [cls.READY_TO_EAT_SALADS]
                case "MUSHROOMS":
                    aisles = [cls.MUSHROOMS]
                case "LETTUCE_CUCUMBER_AND_OTHERS":
                    aisles = [cls.LETTUCE_CUCUMBER_AND_OTHERS]
                case "POTATOES_AND_CARROTS":
                    aisles = [cls.POTATOES_AND_CARROTS]
                case "PREPARED_AND_PRE_COOKED":
                    aisles = [cls.PREPARED_AND_PRE_COOKED]
                case "LEEKS_BEANS_LEGUMES_AND_CABBAGES":
                    aisles = [cls.LEEKS_BEANS_LEGUMES_AND_CABBAGES]
                case "SAUCES_HERBS_AND_SPICES":
                    aisles = [cls.SAUCES_HERBS_AND_SPICES]
                case "TOMATOES_AND_PEPPERS":
                    aisles = [cls.TOMATOES_AND_PEPPERS]
               
                 
        return aisles

#Sweets and Brreakfast

class EroskiSweetsCofeeAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Sweets_Cofee")

    CHICORY_AND_SOLUBLE_CEREALS = StaticAisle(name="Chicory and soluble cereals",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060119-la-tienda-del-cafe/2060124-achicoria-y-cereales-solubles/",
                                     original_file_uri=os.path.join(category_path(), "Chicory_and_soluble_cereals.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chicory_and_soluble_cereals_detailed.json"))
    
    COFFEE_CAPSULES = StaticAisle(name="Coffee capsules", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060119-la-tienda-del-cafe/2060122-cafe-capsulas/",
                                     original_file_uri=os.path.join(category_path(), "Coffee_capsules.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Coffee_capsules_detailed.json"))
    
    COFFEE_BEANS = StaticAisle(name="Coffee beans",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060119-la-tienda-del-cafe/2060123-cafe-grano/",
                                     original_file_uri=os.path.join(category_path(), "Coffee_beans.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Coffee_beans_detailed.json"))
    
    GROUND_COFFEE = StaticAisle(name="Ground coffee", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060119-la-tienda-del-cafe/2060120-cafe-molido/",
                                     original_file_uri=os.path.join(category_path(), "Ground_coffee.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Ground_coffee_detailed.json"))
    
    INSTANT_COFFEE = StaticAisle(name="Instant coffee",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060119-la-tienda-del-cafe/2060121-cafe-soluble/",
                                     original_file_uri=os.path.join(category_path(), "Instant_coffee.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Instant_coffee_detailed.json"))
   
    
    aisles: Final[List[StaticAisle]] = [CHICORY_AND_SOLUBLE_CEREALS, COFFEE_CAPSULES, COFFEE_BEANS, GROUND_COFFEE, INSTANT_COFFEE]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "CHICORY_AND_SOLUBLE_CEREALS":
                    aisles = [cls.CHICORY_AND_SOLUBLE_CEREALS]
                case "COFFEE_CAPSULES":
                    aisles = [cls.COFFEE_CAPSULES]
                case "COFFEE_BEANS":
                    aisles = [cls.COFFEE_BEANS]
                case "GROUND_COFFEE":
                    aisles = [cls.GROUND_COFFEE]
                case "INSTANT_COFFEE":
                    aisles = [cls.INSTANT_COFFEE]
              
        return aisles
    
class EroskiSweetsSugarAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Sweets_Sugar")

    PASTRY_ORNAMENTS = StaticAisle(name="Pastry ornaments",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060182-azucar-y-edulcorante/5000290-adornos-reposteria/",
                                     original_file_uri=os.path.join(category_path(), "Pastry_ornaments.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pastry_ornaments_detailed.json"))
    
    ORGANIC_SUGAR = StaticAisle(name="Organic sugar", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060182-azucar-y-edulcorante/2060965-azucar-ecologico/",
                                     original_file_uri=os.path.join(category_path(), "Organic_sugar.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_sugar_detailed.json"))
    
    SPECIAL_SUGAR = StaticAisle(name="Special sugar",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060182-azucar-y-edulcorante/2060185-azucar-especial/",
                                     original_file_uri=os.path.join(category_path(), "Special_sugar.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Special_sugar_detailed.json"))
    
    SUGARS = StaticAisle(name="Sugars", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060182-azucar-y-edulcorante/2060186-azucarillos/",
                                     original_file_uri=os.path.join(category_path(), "Sugars.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sugars_detailed.json"))
    
    BROWN_SUGAR = StaticAisle(name="Brown sugar",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060182-azucar-y-edulcorante/2060184-azucar-moreno/",
                                     original_file_uri=os.path.join(category_path(), "Brown_sugar.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Brown_sugar_detailed.json"))
   
    SUGAR_PACKET = StaticAisle(name="Sugar Packet",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060182-azucar-y-edulcorante/2060183-azucar-paquete/",
                                     original_file_uri=os.path.join(category_path(), "Sugar_Packet.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sugar_Packet_detailed.json"))
    
    CATALAN_CREAM_AND_OTHER_CREAMS = StaticAisle(name="Catalan cream and other creams", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060182-azucar-y-edulcorante/5000294-crema-catalana-y-otras-cremas/",
                                     original_file_uri=os.path.join(category_path(), "Catalan_cream_and_other_creams.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Catalan_cream_and_other_creams_detailed.json"))
    
    SWEETENER_AND_FRUCTOSE = StaticAisle(name="Sweetener and fructose",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060182-azucar-y-edulcorante/2060187-edulcorante-y-fructosa/",
                                     original_file_uri=os.path.join(category_path(), "Sweetener_and_fructose.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sweetener_and_fructose_detailed.json"))
    
    FLANS_CUSTARD_AND_CURDS = StaticAisle(name="Flans, custard and curds", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060182-azucar-y-edulcorante/5000293-flanes-natillas-y-cuajadas/",
                                     original_file_uri=os.path.join(category_path(), "Flans_custard_and_curds.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Flans_custard_and_curds_detailed.json"))
    
    PASTRY_JELLIES = StaticAisle(name="Pastry jellies",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060182-azucar-y-edulcorante/5000288-gelatinas-reposteria/",
                                     original_file_uri=os.path.join(category_path(), "Pastry_jellies.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pastry_jellies_detailed.json"))
   
    YEASTS_AND_OTHERS = StaticAisle(name="Yeasts and others",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060182-azucar-y-edulcorante/5000287-levaduras-y-otros/",
                                     original_file_uri=os.path.join(category_path(), "Yeasts_and_others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Yeasts_and_others_detailed.json"))
    
    CAKES_TARTS_AND_BISCUITS = StaticAisle(name="Cakes, tarts and biscuits", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060182-azucar-y-edulcorante/5000291-pasteles-tartas-y-bizcochos/",
                                     original_file_uri=os.path.join(category_path(), "Cakes_tarts_and_biscuits.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cakes_tarts_and_biscuits_detailed.json"))
    
    SYRUP_AND_LIQUID_CARAMEL = StaticAisle(name="Syrup and liquid caramel",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060182-azucar-y-edulcorante/5000289-sirope-y-caramelo-liquido/",
                                     original_file_uri=os.path.join(category_path(), "Syrup_and_liquid_caramel.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Syrup_and_liquid_caramel_detailed.json"))
   
    
    aisles: Final[List[StaticAisle]] = [PASTRY_ORNAMENTS, ORGANIC_SUGAR, SPECIAL_SUGAR, SUGARS, BROWN_SUGAR, SUGAR_PACKET, CATALAN_CREAM_AND_OTHER_CREAMS, SWEETENER_AND_FRUCTOSE, FLANS_CUSTARD_AND_CURDS, PASTRY_JELLIES, YEASTS_AND_OTHERS, CAKES_TARTS_AND_BISCUITS, SYRUP_AND_LIQUID_CARAMEL]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "PASTRY_ORNAMENTS":
                    aisles = [cls.PASTRY_ORNAMENTS]
                case "ORGANIC_SUGAR":
                    aisles = [cls.ORGANIC_SUGAR]
                case "SPECIAL_SUGAR":
                    aisles = [cls.SPECIAL_SUGAR]
                case "SUGARS":
                    aisles = [cls.SUGARS]
                case "BROWN_SUGAR":
                    aisles = [cls.BROWN_SUGAR]
                case "SUGAR_PACKET":
                    aisles = [cls.SUGAR_PACKET]
                case "CATALAN_CREAM_AND_OTHER_CREAMS":
                    aisles = [cls.CATALAN_CREAM_AND_OTHER_CREAMS]
                case "SWEETENER_AND_FRUCTOSE":
                    aisles = [cls.SWEETENER_AND_FRUCTOSE]
                case "FLANS_CUSTARD_AND_CURDS":
                    aisles = [cls.FLANS_CUSTARD_AND_CURDS]
                case "PASTRY_JELLIES":
                    aisles = [cls.PASTRY_JELLIES]
                case "YEASTS_AND_OTHERS":
                    aisles = [cls.YEASTS_AND_OTHERS]
                case "CAKES_TARTS_AND_BISCUITS":
                    aisles = [cls.CAKES_TARTS_AND_BISCUITS]
                case "SYRUP_AND_LIQUID_CARAMEL":
                    aisles = [cls.SYRUP_AND_LIQUID_CARAMEL]
              
        return aisles
    
class EroskiSweetsPastriesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Sweets_Pastries")

    SPONGE_CAKE_SHORTBREAD_AND_ENSAIMADAS = StaticAisle(name="Sponge cake, shortbread and ensaimadas",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060162-bolleria/2060167-bizcocho-mantecada-y-ensaimadas/",
                                     original_file_uri=os.path.join(category_path(), "Sponge_cake_shortbread_and_ensaimadas.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sponge_cake_shortbread_and_ensaimadas_detailed.json"))
    
    GLUTEN_FREE_PASTRIES = StaticAisle(name="Gluten-free pastries", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060162-bolleria/2060863-bolleria-sin-gluten/",
                                     original_file_uri=os.path.join(category_path(), "Gluten_free_pastries.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Gluten_free_pastries_detailed.json"))
    
    REEDS_PALM_TREES_AND_NEAPOLITANS = StaticAisle(name="Reeds, palm trees and Neapolitans",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060162-bolleria/2060168-canas-palmeras-y-napolitanas/",
                                     original_file_uri=os.path.join(category_path(), "Reeds_palm_trees_and_Neapolitans.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Reeds_palm_trees_and_Neapolitans_detailed.json"))
    
    CROISSANTS_PASTRIES = StaticAisle(name="Croissants pastries", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060162-bolleria/2060166-croissants-bolleria/",
                                     original_file_uri=os.path.join(category_path(), "Croissants_pastries.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Croissants_pastries_detailed.json"))
    
    MUFFINS = StaticAisle(name="Muffins",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060162-bolleria/2060165-magdalenas/",
                                     original_file_uri=os.path.join(category_path(), "Muffins.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Muffins_detailed.json"))
   
    MILK_BREAD = StaticAisle(name="Milk bread",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060162-bolleria/2060164-pan-de-leche/",
                                     original_file_uri=os.path.join(category_path(), "Milk_bread.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Milk_bread_detailed.json"))
    
    SOBAOS = StaticAisle(name="Sobaos", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060162-bolleria/2060163-sobaos/",
                                     original_file_uri=os.path.join(category_path(), "Sobaos.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sobaos_detailed.json"))
    
    CAKES_AND_PASTRIES = StaticAisle(name="Cakes and pastries",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060162-bolleria/2060170-tartas-y-pasteles/",
                                     original_file_uri=os.path.join(category_path(), "Cakes_and_pastries.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cakes_and_pastries_detailed.json"))
    
    OTHER_PASTRIES = StaticAisle(name="Other pastries", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060162-bolleria/2060172-otros-bolleria/",
                                     original_file_uri=os.path.join(category_path(), "Other_pastries.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_pastries_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [SPONGE_CAKE_SHORTBREAD_AND_ENSAIMADAS, GLUTEN_FREE_PASTRIES, REEDS_PALM_TREES_AND_NEAPOLITANS, CROISSANTS_PASTRIES, MUFFINS, MILK_BREAD, SOBAOS, CAKES_AND_PASTRIES, OTHER_PASTRIES]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "SPONGE_CAKE_SHORTBREAD_AND_ENSAIMADAS":
                    aisles = [cls.SPONGE_CAKE_SHORTBREAD_AND_ENSAIMADAS]
                case "GLUTEN_FREE_PASTRIES":
                    aisles = [cls.GLUTEN_FREE_PASTRIES]
                case "REEDS_PALM_TREES_AND_NEAPOLITANS":
                    aisles = [cls.REEDS_PALM_TREES_AND_NEAPOLITANS]
                case "CROISSANTS_PASTRIES":
                    aisles = [cls.CROISSANTS_PASTRIES]
                case "MUFFINS":
                    aisles = [cls.MUFFINS]
                case "MILK_BREAD":
                    aisles = [cls.MILK_BREAD]
                case "SOBAOS":
                    aisles = [cls.SOBAOS]
                case "CAKES_AND_PASTRIES":
                    aisles = [cls.CAKES_AND_PASTRIES]
                case "OTHER_PASTRIES":
                    aisles = [cls.OTHER_PASTRIES]
                
        return aisles
    
class EroskiSweetsCocoaAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Sweets_Cocoa")

    INSTANT_COCOA = StaticAisle(name="Instant cocoa",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060129-cacao-en-polvo-y-crema-de-cacao/4000013-cacao-instantaneo/",
                                     original_file_uri=os.path.join(category_path(), "Instant_cocoa.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Instant_cocoa_detailed.json"))
    
    SOLUBLE_COCOA = StaticAisle(name="Soluble cocoa", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060129-cacao-en-polvo-y-crema-de-cacao/2060130-cacao-soluble/",
                                     original_file_uri=os.path.join(category_path(), "Soluble_cocoa.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Soluble_cocoa_detailed.json"))
    
    POWDERED_HOT_CHOCOLATE = StaticAisle(name="Powdered hot chocolate",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060129-cacao-en-polvo-y-crema-de-cacao/2060134-chocolate-a-la-taza-en-polvo/",
                                     original_file_uri=os.path.join(category_path(), "Powdered_hot_chocolate.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Powdered_hot_chocolate_detailed.json"))
    
    COCOA_CREAMS = StaticAisle(name="Cocoa creams", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060129-cacao-en-polvo-y-crema-de-cacao/2060131-cremas-de-cacao-/",
                                     original_file_uri=os.path.join(category_path(), "Cocoa_creams.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cocoa_creams_detailed.json"))
    
    SNACK_AND_OTHERS = StaticAisle(name="Snack and others",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060129-cacao-en-polvo-y-crema-de-cacao/2060133-snack-y-otros/",
                                     original_file_uri=os.path.join(category_path(), "Snack_and_others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Snack_and_others_detailed.json"))
   
 
    
    aisles: Final[List[StaticAisle]] = [INSTANT_COCOA, SOLUBLE_COCOA, POWDERED_HOT_CHOCOLATE, COCOA_CREAMS, SNACK_AND_OTHERS]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "INSTANT_COCOA":
                    aisles = [cls.INSTANT_COCOA]
                case "SOLUBLE_COCOA":
                    aisles = [cls.SOLUBLE_COCOA]
                case "POWDERED_HOT_CHOCOLATE":
                    aisles = [cls.POWDERED_HOT_CHOCOLATE]
                case "COCOA_CREAMS":
                    aisles = [cls.COCOA_CREAMS]
                case "SNACK_AND_OTHERS":
                    aisles = [cls.SNACK_AND_OTHERS]
                
                
        return aisles
    
class EroskiSweetsCandyAndSweetsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Sweets_Candy_and_sweets")

    CANDIES = StaticAisle(name="Candies",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060202-caramelos-chicles-y-golosinas/2060206-caramelos/",
                                     original_file_uri=os.path.join(category_path(), "Candies.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Candies_detailed.json"))
    
    GUM = StaticAisle(name="Gum", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060202-caramelos-chicles-y-golosinas/2060203-chicles/",
                                     original_file_uri=os.path.join(category_path(), "Gum.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Gum_detailed.json"))
    
    LOLLIPOPS = StaticAisle(name="Lollipops",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060202-caramelos-chicles-y-golosinas/2060207-chupa-chups/",
                                     original_file_uri=os.path.join(category_path(), "Lollipops.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Lollipops_detailed.json"))
    
    CANDY = StaticAisle(name="Candy", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060202-caramelos-chicles-y-golosinas/2060210-golosinas/",
                                     original_file_uri=os.path.join(category_path(), "Candy.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Candy_detailed.json"))
    
    CHOCOLATE_SPRINKLES_AND_CHOCOLATES = StaticAisle(name="Chocolate sprinkles and chocolates",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060202-caramelos-chicles-y-golosinas/2060209-grajeas-y-bombones-de-chocolate/",
                                     original_file_uri=os.path.join(category_path(), "Chocolate_sprinkles_and_chocolates.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chocolate_sprinkles_and_chocolates_detailed.json"))
    
    LICORICE_GUMMIES_AND_OTHERS = StaticAisle(name="Licorice, gummies and others",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060202-caramelos-chicles-y-golosinas/2060208-regalices-gomas-y-otros/",
                                     original_file_uri=os.path.join(category_path(), "Licorice_gummies_and_others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Licorice_gummies_and_others_detailed.json"))
   
 
    
    aisles: Final[List[StaticAisle]] = [CANDIES, GUM, LOLLIPOPS, CANDY, CHOCOLATE_SPRINKLES_AND_CHOCOLATES, LICORICE_GUMMIES_AND_OTHERS]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "CANDIES":
                    aisles = [cls.CANDIES]
                case "GUM":
                    aisles = [cls.GUM]
                case "LOLLIPOPS":
                    aisles = [cls.LOLLIPOPS]
                case "CANDY":
                    aisles = [cls.CANDY]
                case "CHOCOLATE_SPRINKLES_AND_CHOCOLATES":
                    aisles = [cls.CHOCOLATE_SPRINKLES_AND_CHOCOLATES]
                case "LICORICE_GUMMIES_AND_OTHERS":
                    aisles = [cls.LICORICE_GUMMIES_AND_OTHERS]
                
                
        return aisles
    
class EroskiSweetsCerealAndBarsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Sweets_Cereal_and_bars")

    BARS = StaticAisle(name="Bars",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/5000189-cereales-y-barritas/2060145-barritas/",
                                     original_file_uri=os.path.join(category_path(), "Bars.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Bars_detailed.json"))
    
    FIBRE_LINE_AND_MUESLI_CEREALS = StaticAisle(name="Fibre, line and muesli cereals", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/5000189-cereales-y-barritas/2060148-cereales-fibra-linea-y-muesli/",
                                     original_file_uri=os.path.join(category_path(), "Fibre_line_and_muesli_cereals.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fibre_line_and_muesli_cereals_detailed.json"))
    
    INFANT_CEREALS = StaticAisle(name="Infant cereals",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/5000189-cereales-y-barritas/2060147-cereales-infantiles/",
                                     original_file_uri=os.path.join(category_path(), "Infant_cereals.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Infant_cereals_detailed.json"))
    
    CORNFLAKES = StaticAisle(name="Cornflakes", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/5000189-cereales-y-barritas/2060146-cornflakes/",
                                     original_file_uri=os.path.join(category_path(), "Cornflakes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cornflakes_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [BARS, FIBRE_LINE_AND_MUESLI_CEREALS, INFANT_CEREALS, CORNFLAKES]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "BARS":
                    aisles = [cls.BARS]
                case "FIBRE_LINE_AND_MUESLI_CEREALS":
                    aisles = [cls.FIBRE_LINE_AND_MUESLI_CEREALS]
                case "INFANT_CEREALS":
                    aisles = [cls.INFANT_CEREALS]
                case "CORNFLAKES":
                    aisles = [cls.CORNFLAKES]
              
                
        return aisles
    
class EroskiSweetsChocolatesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Sweets_Chocolates")

    CHOCOLATES = StaticAisle(name="Chocolates",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060190-chocolates-y-bombones/2060200-bombones/",
                                     original_file_uri=os.path.join(category_path(), "Chocolates.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chocolates_detailed.json"))
    
    HOT_CHOCOLATE = StaticAisle(name="Hot chocolate", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060190-chocolates-y-bombones/2060199-chocolate-a-la-taza/",
                                     original_file_uri=os.path.join(category_path(), "Hot_chocolate.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Hot_chocolate_detailed.json"))
    
    MILK_CHOCOLATE = StaticAisle(name="Milk chocolate",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060190-chocolates-y-bombones/2060191-chocolate-con-leche/",
                                     original_file_uri=os.path.join(category_path(), "Milk_chocolate.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Milk_chocolate_detailed.json"))
    
    MILK_CHOCOLATE_AND_NUTS = StaticAisle(name="Milk chocolate and nuts", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060190-chocolates-y-bombones/2060192-chocolate-con-leche-y-frutos-secos/",
                                     original_file_uri=os.path.join(category_path(), "Milk_chocolate_and_nuts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Milk_chocolate_and_nuts_detailed.json"))
    
    CHILDRENS_CHOCOLATE = StaticAisle(name="Children's chocolate",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060190-chocolates-y-bombones/2060197-chocolate-infantil/",
                                     original_file_uri=os.path.join(category_path(), "Childrens_chocolate.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Childrens_chocolate_detailed.json"))
    
    DARK_CHOCOLATE = StaticAisle(name="Dark chocolate", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060190-chocolates-y-bombones/2060193-chocolate-negro/",
                                     original_file_uri=os.path.join(category_path(), "Dark_chocolate.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Dark_chocolate_detailed.json"))
    
    DARK_CHOCOLATE_WITH_NUTS = StaticAisle(name="Dark chocolate with nuts",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060190-chocolates-y-bombones/2060194-chocolate-negro-con-frutos-secos/",
                                     original_file_uri=os.path.join(category_path(), "Dark_chocolate_with_nuts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Dark_chocolate_with_nuts_detailed.json"))
    
    CHOCOLATE_FOR_DESSERTS = StaticAisle(name="Chocolate for desserts", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060190-chocolates-y-bombones/2060201-chocolate-para-postres/",
                                     original_file_uri=os.path.join(category_path(), "Chocolate_for_desserts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chocolate_for_desserts_detailed.json"))
  
    SUGAR_FREE_CHOCOLATE = StaticAisle(name="Sugar-free chocolate",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060190-chocolates-y-bombones/2060196-chocolate-sin-azucar/",
                                     original_file_uri=os.path.join(category_path(), "Sugar_free_chocolate.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sugar_free_chocolate_detailed.json"))
    
    FILLED_CHOCOLATES_AND_OTHERS = StaticAisle(name="Filled chocolates and others", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060190-chocolates-y-bombones/2060195-chocolates-rellenos-y-otros/",
                                     original_file_uri=os.path.join(category_path(), "Filled_chocolates_and_others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Filled_chocolates_and_others_detailed.json"))
    
    CHOCOLATE_SNACK = StaticAisle(name="Chocolate snack",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060190-chocolates-y-bombones/2060198-merienda-chocolate/",
                                     original_file_uri=os.path.join(category_path(), "Chocolate_snack.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chocolate_snack_detailed.json"))
    
   
    
    aisles: Final[List[StaticAisle]] = [CHOCOLATES, HOT_CHOCOLATE, MILK_CHOCOLATE, MILK_CHOCOLATE_AND_NUTS, CHILDRENS_CHOCOLATE, DARK_CHOCOLATE, DARK_CHOCOLATE_WITH_NUTS, CHOCOLATE_FOR_DESSERTS, SUGAR_FREE_CHOCOLATE, FILLED_CHOCOLATES_AND_OTHERS, CHOCOLATE_SNACK]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "CHOCOLATES":
                    aisles = [cls.CHOCOLATES]
                case "HOT_CHOCOLATE":
                    aisles = [cls.HOT_CHOCOLATE]
                case "MILK_CHOCOLATE":
                    aisles = [cls.MILK_CHOCOLATE]
                case "MILK_CHOCOLATE_AND_NUTS":
                    aisles = [cls.MILK_CHOCOLATE_AND_NUTS]
                case "CHILDRENS_CHOCOLATE":
                    aisles = [cls.CHILDRENS_CHOCOLATE]
                case "DARK_CHOCOLATE":
                    aisles = [cls.DARK_CHOCOLATE]
                case "DARK_CHOCOLATE_WITH_NUTS":
                    aisles = [cls.DARK_CHOCOLATE_WITH_NUTS]
                case "CHOCOLATE_FOR_DESSERTS":
                    aisles = [cls.CHOCOLATE_FOR_DESSERTS]
                case "SUGAR_FREE_CHOCOLATE":
                    aisles = [cls.SUGAR_FREE_CHOCOLATE]
                case "FILLED_CHOCOLATES_AND_OTHERS":
                    aisles = [cls.FILLED_CHOCOLATES_AND_OTHERS]
                case "CHOCOLATE_SNACK":
                    aisles = [cls.CHOCOLATE_SNACK]
               
        return aisles
    
class EroskiSweetsBiscuitsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Sweets_Biscuits")

    BISCUITS_APPETIZERS = StaticAisle(name="Biscuits appetizers",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060135-galletas/2060142-galletas-aperitivos/",
                                     original_file_uri=os.path.join(category_path(), "Biscuits_appetizers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Biscuits_appetizers_detailed.json"))
    
    CLASSIC_COOKIES = StaticAisle(name="Classic Cookies", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060135-galletas/2060136-galletas-clasicas/",
                                     original_file_uri=os.path.join(category_path(), "Classic_Cookies.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Classic_Cookies_detailed.json"))
    
    CHILDRENS_BREAKFAST_BISCUITS = StaticAisle(name="Children's breakfast biscuits",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060135-galletas/2060138-galletas-desayuno-infantil/",
                                     original_file_uri=os.path.join(category_path(), "Childrens_breakfast_biscuits.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Childrens_breakfast_biscuits_detailed.json"))
    
    FIBRE_WHOLEMEAL_AND_ORGANIC_BISCUITS = StaticAisle(name="Fibre, wholemeal and organic biscuits", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060135-galletas/2060139-galletas-fibra-integrales-y-ecologicas/",
                                     original_file_uri=os.path.join(category_path(), "Fibre_wholemeal_and_organic_biscuits.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fibre_wholemeal_and_organic_biscuits_detailed.json"))
    
    FILLED_AND_COVERED_BISCUITS = StaticAisle(name="Filled and covered biscuits",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060135-galletas/2060141-galletas-rellenas-y-cubiertas/",
                                     original_file_uri=os.path.join(category_path(), "Filled_and_covered_biscuits.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Filled_and_covered_biscuits_detailed.json"))
    
    GLUTEN_FREE_BISCUITS = StaticAisle(name="Gluten-free biscuits", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060135-galletas/2060143-galletas-sin-gluten/",
                                     original_file_uri=os.path.join(category_path(), "Gluten_free_biscuits.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Gluten_free_biscuits_detailed.json"))
    
    SNACK_BISCUITS_ASSORTED_BISCUITS_AND_PASTRIES = StaticAisle(name="Snack biscuits, assorted biscuits and pastries",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060135-galletas/2060137-galletas-snack-surtidas-y-pastas/",
                                     original_file_uri=os.path.join(category_path(), "Snack_biscuits_assorted_biscuits_and_pastries.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Snack_biscuits_assorted_biscuits_and_pastries_detailed.json"))
  
    
   
    
    aisles: Final[List[StaticAisle]] = [BISCUITS_APPETIZERS, CLASSIC_COOKIES, CHILDRENS_BREAKFAST_BISCUITS, FIBRE_WHOLEMEAL_AND_ORGANIC_BISCUITS, FILLED_AND_COVERED_BISCUITS, GLUTEN_FREE_BISCUITS, SNACK_BISCUITS_ASSORTED_BISCUITS_AND_PASTRIES]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "BISCUITS_APPETIZERS":
                    aisles = [cls.BISCUITS_APPETIZERS]
                case "CLASSIC_COOKIES":
                    aisles = [cls.CLASSIC_COOKIES]
                case "CHILDRENS_BREAKFAST_BISCUITS":
                    aisles = [cls.CHILDRENS_BREAKFAST_BISCUITS]
                case "FIBRE_WHOLEMEAL_AND_ORGANIC_BISCUITS":
                    aisles = [cls.FIBRE_WHOLEMEAL_AND_ORGANIC_BISCUITS]
                case "FILLED_AND_COVERED_BISCUITS":
                    aisles = [cls.FILLED_AND_COVERED_BISCUITS]
                case "GLUTEN_FREE_BISCUITS":
                    aisles = [cls.GLUTEN_FREE_BISCUITS]
                case "SNACK_BISCUITS_ASSORTED_BISCUITS_AND_PASTRIES":
                    aisles = [cls.SNACK_BISCUITS_ASSORTED_BISCUITS_AND_PASTRIES]
                
               
        return aisles
    
class EroskiSweetsInfusionAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Sweets_Infusion")

    HEALTHY_INFUSIONS = StaticAisle(name="Healthy infusions",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/4000095-infusiones/2060128-infusiones-saludables/",
                                     original_file_uri=os.path.join(category_path(), "Healthy_infusions.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Healthy_infusions_detailed.json"))
    
    CHAMOMILE = StaticAisle(name="Chamomile", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/4000095-infusiones/2060126-manzanilla/",
                                     original_file_uri=os.path.join(category_path(), "Chamomile.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chamomile_detailed.json"))
    
    TEA = StaticAisle(name="Tea",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/4000095-infusiones/2060125-te/",
                                     original_file_uri=os.path.join(category_path(), "Tea.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tea_detailed.json"))
    
    LINDEN_AND_PENNYROYAL = StaticAisle(name="Linden and pennyroyal", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/4000095-infusiones/2060127-tila-y-poleo/",
                                     original_file_uri=os.path.join(category_path(), "Linden_and_pennyroyal.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Linden_and_pennyroyal_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [HEALTHY_INFUSIONS, CHAMOMILE, TEA, LINDEN_AND_PENNYROYAL]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "HEALTHY_INFUSIONS":
                    aisles = [cls.HEALTHY_INFUSIONS]
                case "CHAMOMILE":
                    aisles = [cls.CHAMOMILE]
                case "TEA":
                    aisles = [cls.TEA]
                case "LINDEN_AND_PENNYROYAL":
                    aisles = [cls.LINDEN_AND_PENNYROYAL]
              
        return aisles
    
class EroskiSweetsHoneyAndjamAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Sweets_Honey_and_jam")

    STRAWBERRY_AND_PLUM = StaticAisle(name="Strawberry and plum",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060173-miel-y-mermelada/2060175-fresa-y-ciruela/",
                                     original_file_uri=os.path.join(category_path(), "Strawberry_and_plum.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Strawberry_and_plum_detailed.json"))
    
    PEACH_AND_APRICOT = StaticAisle(name="Peach and apricot", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060173-miel-y-mermelada/2060174-melocoton-y-albaricoque/",
                                     original_file_uri=os.path.join(category_path(), "Peach_and_apricot.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Peach_and_apricot_detailed.json"))
    
    JAM_PORTIONS = StaticAisle(name="Jam portions",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060173-miel-y-mermelada/2060177-mermelada-porciones/",
                                     original_file_uri=os.path.join(category_path(), "Jam_portions.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Jam_portions_detailed.json"))
    
    LIGHT_JAMS = StaticAisle(name="Light jams", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060173-miel-y-mermelada/2060176-mermeladas-ligeras/",
                                     original_file_uri=os.path.join(category_path(), "Light_jams.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Light_jams_detailed.json"))
    
    OTHER_JAMS = StaticAisle(name="Other jams",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060173-miel-y-mermelada/2060178-otras-mermeladas/",
                                     original_file_uri=os.path.join(category_path(), "Other_jams.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_jams_detailed.json"))
    
    MILFLORES_HONEY = StaticAisle(name="Milflores honey", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060173-miel-y-mermelada/2060179-miel-milflores/",
                                     original_file_uri=os.path.join(category_path(), "Milflores_honey.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Milflores_honey_detailed.json"))
    
    MONOFLOWER_HONEY = StaticAisle(name="Monoflower honey",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060173-miel-y-mermelada/2060180-miel-monoflores/",
                                     original_file_uri=os.path.join(category_path(), "Monoflower_honey.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Monoflower_honey_detailed.json"))
    
    OTHER_HONEYS = StaticAisle(name="Other honeys", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060173-miel-y-mermelada/2060181-otras-mieles/",
                                     original_file_uri=os.path.join(category_path(), "Other_honeys.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_honeys_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [STRAWBERRY_AND_PLUM, PEACH_AND_APRICOT, JAM_PORTIONS, LIGHT_JAMS, OTHER_JAMS, MILFLORES_HONEY, MONOFLOWER_HONEY, OTHER_HONEYS]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "STRAWBERRY_AND_PLUM":
                    aisles = [cls.STRAWBERRY_AND_PLUM]
                case "PEACH_AND_APRICOT":
                    aisles = [cls.PEACH_AND_APRICOT]
                case "JAM_PORTIONS":
                    aisles = [cls.JAM_PORTIONS]
                case "LIGHT_JAMS":
                    aisles = [cls.LIGHT_JAMS]
                case "OTHER_JAMS":
                    aisles = [cls.OTHER_JAMS]
                case "MILFLORES_HONEY":
                    aisles = [cls.MILFLORES_HONEY]
                case "MONOFLOWER_HONEY":
                    aisles = [cls.MONOFLOWER_HONEY]
                case "OTHER_HONEYS":
                    aisles = [cls.OTHER_HONEYS]
              
        return aisles
    
class EroskiSweetsSlicedAndToastedBreadAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Sweets_Slice_and_toasted_bread")

    BISCOTTES_CROUTONS_AND_OTHERS = StaticAisle(name="Biscottes, croutons and others",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060149-pan-de-molde-y-tostado/2060159-biscottes-picatostes-y-otros/",
                                     original_file_uri=os.path.join(category_path(), "Biscottes_croutons_and_others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Biscottes_croutons_and_others_detailed.json"))
    
    MINI_BISCOTTES_AND_ROLLS = StaticAisle(name="Mini biscottes and rolls", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060149-pan-de-molde-y-tostado/2060160-minibiscottes-y-panecillos/",
                                     original_file_uri=os.path.join(category_path(), "Mini_biscottes_and_rolls.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mini_biscottes_and_rolls_detailed.json"))
    
    BURGER_BREAD_HOT_DOGS_AND_OTHERS = StaticAisle(name="Burger bread, hot dogs and others",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060149-pan-de-molde-y-tostado/2060157-pan-burguer-hot-dogs-y-otros/",
                                     original_file_uri=os.path.join(category_path(), "Burger_bread_hot_dogs_and_others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Burger_bread_hot_dogs_and_others_detailed.json"))
    
    SLICED_BREAD_WITH_CRUST = StaticAisle(name="Sliced bread with crust", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060149-pan-de-molde-y-tostado/2060152-pan-de-molde-con-corteza/",
                                     original_file_uri=os.path.join(category_path(), "Sliced_bread_with_crust.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sliced_bread_with_crust_detailed.json"))
    
    SLICED_BREAD_WITH_RUSTIC_CRUST = StaticAisle(name="Sliced bread with rustic crust",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060149-pan-de-molde-y-tostado/2060153-pan-de-molde-con-corteza-rustica/",
                                     original_file_uri=os.path.join(category_path(), "Sliced_bread_with_rustic_crust.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sliced_bread_with_rustic_crust_detailed.json"))
    
    WHOLEMEAL_SLICED_BREAD = StaticAisle(name="Wholemeal sliced bread", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060149-pan-de-molde-y-tostado/2060154-pan-de-molde-integral/",
                                     original_file_uri=os.path.join(category_path(), "Wholemeal_sliced_bread.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Wholemeal_sliced_bread_detailed.json"))
    
    CRUSTLESS_SLICED_BREAD = StaticAisle(name="Crustless sliced bread",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060149-pan-de-molde-y-tostado/2060150-pan-de-molde-sin-corteza/",
                                     original_file_uri=os.path.join(category_path(), "Crustless_sliced_bread.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Crustless_sliced_bread_detailed.json"))
    
    TOAST = StaticAisle(name="Toast", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060149-pan-de-molde-y-tostado/2060158-pan-tostado/",
                                     original_file_uri=os.path.join(category_path(), "Toast.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Toast_detailed.json"))
  
    TOASTS_AND_CRACKERS = StaticAisle(name="Toasts and crackers", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060149-pan-de-molde-y-tostado/2060161-tostas-y-crackers/",
                                     original_file_uri=os.path.join(category_path(), "Toasts_and_crackers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Toasts_and_crackers_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [BISCOTTES_CROUTONS_AND_OTHERS, MINI_BISCOTTES_AND_ROLLS, BURGER_BREAD_HOT_DOGS_AND_OTHERS, SLICED_BREAD_WITH_CRUST, SLICED_BREAD_WITH_RUSTIC_CRUST, WHOLEMEAL_SLICED_BREAD, CRUSTLESS_SLICED_BREAD, TOAST, TOASTS_AND_CRACKERS]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "BISCOTTES_CROUTONS_AND_OTHERS":
                    aisles = [cls.BISCOTTES_CROUTONS_AND_OTHERS]
                case "MINI_BISCOTTES_AND_ROLLS":
                    aisles = [cls.MINI_BISCOTTES_AND_ROLLS]
                case "BURGER_BREAD_HOT_DOGS_AND_OTHERS":
                    aisles = [cls.BURGER_BREAD_HOT_DOGS_AND_OTHERS]
                case "SLICED_BREAD_WITH_CRUST":
                    aisles = [cls.SLICED_BREAD_WITH_CRUST]
                case "SLICED_BREAD_WITH_RUSTIC_CRUST":
                    aisles = [cls.SLICED_BREAD_WITH_RUSTIC_CRUST]
                case "WHOLEMEAL_SLICED_BREAD":
                    aisles = [cls.WHOLEMEAL_SLICED_BREAD]
                case "CRUSTLESS_SLICED_BREAD":
                    aisles = [cls.CRUSTLESS_SLICED_BREAD]
                case "TOAST":
                    aisles = [cls.TOAST]
                case "TOASTS_AND_CRACKERS":
                    aisles = [cls.TOASTS_AND_CRACKERS]
              
        return aisles
    
class EroskiSweetsOrganicProductsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Sweets_Organic_products")

    BREAKFAST_AND_SNACKS = StaticAisle(name="Breakfast and snacks",  url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/5000302-productos-ecologicos/5000305-desayunos-y-meriendas/",
                                     original_file_uri=os.path.join(category_path(), "Breakfast_and_snacks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Breakfast_and_snacks_detailed.json"))
    
    SWEETS_AND_SWEETENERS = StaticAisle(name="Sweets and sweeteners", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/5000302-productos-ecologicos/5000303-dulces-y-edulcorantes/",
                                     original_file_uri=os.path.join(category_path(), "Sweets_and_sweeteners.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sweets_and_sweeteners_detailed.json"))
    
    
    
    aisles: Final[List[StaticAisle]] = [BREAKFAST_AND_SNACKS, SWEETS_AND_SWEETENERS]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "BREAKFAST_AND_SNACKS":
                    aisles = [cls.BREAKFAST_AND_SNACKS]
                case "SWEETS_AND_SWEETENERS":
                    aisles = [cls.SWEETS_AND_SWEETENERS]
                
              
        return aisles
    
#Beverages

class EroskiDrinkWaterAlimentation(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Beverages_Water")

    FLAVORED_WATER = StaticAisle(name="Flavored Water", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060212-agua/2060218-agua-con-sabores/",
                                 original_file_uri=os.path.join(category_path(), "Flavored_Water.json"),
                                 mini_file_detailed_uri=os.path.join(category_path(), "Flavored_Water_detailed.json"))
    
    WATER_FROM_1L_TO_2L = StaticAisle(name="Water From 1Liter To 2Liters", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060212-agua/2060214-agua-de-1-litro-a-2-litros/",
                                      original_file_uri=os.path.join(category_path(), "Water_From_1Liter_To_2Liters.json"),
                                      mini_file_detailed_uri=os.path.join(category_path(), "Water_From_1Liter_To_2Liters_detailed.json"))
    
    WATER_UP_TO_1L = StaticAisle(name="Water Up To 1Liter", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060212-agua/2060213-agua-hasta-1-litro/",
                                 original_file_uri=os.path.join(category_path(), "Water_Up_To_1Liter.json"),
                                 mini_file_detailed_uri=os.path.join(category_path(), "Water_Up_To_1Liter_detailed.json"))
    
    WATER_MORE_THAN_2L = StaticAisle(name="Water More Than 2Liters", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060212-agua/2060215-agua-mas-de-2-litros/",
                                     original_file_uri=os.path.join(category_path(), "Water_More_Than_2Liters.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Water_More_Than_2Liters_detailed.json"))
    
    WITH_GAS_MORE_THAN_1L = StaticAisle(name="With Gas More Than 1Liter", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060212-agua/2060216-con-gas-mas-de-1-litro/",
                                        original_file_uri=os.path.join(category_path(), "With_Gas_More_Than_1Liter.json"),
                                        mini_file_detailed_uri=os.path.join(category_path(), "With_Gas_More_Than_1Liter_detailed.json"))
    
    WITH_GAS_LESS_THAN_1L = StaticAisle(name="With Gas Less Than 1Liter", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060212-agua/2060217-con-gas-menos-de-1-litro/",
                                         original_file_uri=os.path.join(category_path(), "With_Gas_Less_Than_1Liter.json"),
                                         mini_file_detailed_uri=os.path.join(category_path(), "With_Gas_Less_Than_1Liter_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [FLAVORED_WATER, WATER_FROM_1L_TO_2L, WATER_UP_TO_1L, WATER_MORE_THAN_2L, WITH_GAS_MORE_THAN_1L, WITH_GAS_LESS_THAN_1L]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "FLAVORED_WATER":
                    aisles = [cls.FLAVORED_WATER]
                case "WATER_FROM_1L_TO_2L":
                    aisles = [cls.WATER_FROM_1L_TO_2L]
                case "WATER_UP_TO_1L":
                    aisles = [cls.WATER_UP_TO_1L]
                case "WATER_MORE_THAN_2L":
                    aisles = [cls.WATER_MORE_THAN_2L]
                case "WITH_GAS_MORE_THAN_1L":
                    aisles = [cls.WITH_GAS_MORE_THAN_1L]
                case "WITH_GAS_LESS_THAN_1L":
                    aisles = [cls.WITH_GAS_LESS_THAN_1L]
        
        return aisles

class EroskiDrinkCavaChampagneAndCiderAlimentation(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Beverages_Cava_champagne_and_cider")

    CAVA_BRUT = StaticAisle(name="Cava Brut", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060304-cavachampan-y-sidra/2060306-cava-brut-/",
                             original_file_uri=os.path.join(category_path(), "Cava_Brut.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Cava_Brut_detailed.json"))
    
    CAVA_BRUT_NATURE = StaticAisle(name="CavaBrutNature", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060304-cavachampan-y-sidra/2060305-cava-brut-nature/",
                                   original_file_uri=os.path.join(category_path(), "Cava_Brut_Nature.json"),
                                   mini_file_detailed_uri=os.path.join(category_path(), "Cava_Brut_Nature_detailed.json"))
    
    PINK_CAVA = StaticAisle(name="Pink Cava", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060304-cavachampan-y-sidra/2060310-cava-rosado/",
                            original_file_uri=os.path.join(category_path(), "Pink_Cava.json"),
                            mini_file_detailed_uri=os.path.join(category_path(), "Pink_Cava_detailed.json"))
    
    MEDIUM_AND_MINI_CAVAS = StaticAisle(name="MediumAndMiniCavas", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060304-cavachampan-y-sidra/2060309-cava-medianos-y-minis/",
                                        original_file_uri=os.path.join(category_path(), "Medium_And_MiniCavas.json"),
                                        mini_file_detailed_uri=os.path.join(category_path(), "Medium_And_MiniCavas_detailed.json"))
    
    DRY_CAVA = StaticAisle(name="Dry Cava", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060304-cavachampan-y-sidra/2060308-cava-seco/",
                           original_file_uri=os.path.join(category_path(), "Dry_Cava.json"),
                           mini_file_detailed_uri=os.path.join(category_path(), "Dry_Cava_detailed.json"))
    
    SEMIDRY_CAVA = StaticAisle(name="Semidry Cava", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060304-cavachampan-y-sidra/2060307-cava-semi-seco/",
                               original_file_uri=os.path.join(category_path(), "Semidry_Cava.json"),
                               mini_file_detailed_uri=os.path.join(category_path(), "Semidry_Cava_detailed.json"))
    
    OTHER_CAVAS = StaticAisle(name="Other Cavas", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060304-cavachampan-y-sidra/2060311-otros-cavas/",
                              original_file_uri=os.path.join(category_path(), "Other_Cavas.json"),
                              mini_file_detailed_uri=os.path.join(category_path(), "Other_Cavas_detailed.json"))
    
    CHAMPAGNE = StaticAisle(name="Champagne", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060304-cavachampan-y-sidra/2060314-champagne/",
                            original_file_uri=os.path.join(category_path(), "Champagne.json"),
                            mini_file_detailed_uri=os.path.join(category_path(), "Champagne_detailed.json"))
    
    SPARKLING_CIDER = StaticAisle(name="Sparkling Cider", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060304-cavachampan-y-sidra/2060313-sidra-achampanada/",
                                  original_file_uri=os.path.join(category_path(), "Sparkling_Cider.json"),
                                  mini_file_detailed_uri=os.path.join(category_path(), "Sparkling_Cider_detailed.json"))
    
    NATURAL_CIDER = StaticAisle(name="NaturalCider", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060304-cavachampan-y-sidra/2060312-sidra-natural/",
                                original_file_uri=os.path.join(category_path(), "Natural_Cider.json"),
                                mini_file_detailed_uri=os.path.join(category_path(), "Natural_Cider_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [CAVA_BRUT, CAVA_BRUT_NATURE, PINK_CAVA, MEDIUM_AND_MINI_CAVAS, DRY_CAVA, SEMIDRY_CAVA, OTHER_CAVAS, CHAMPAGNE, SPARKLING_CIDER, NATURAL_CIDER]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "CAVA_BRUT":
                    aisles = [cls.CAVA_BRUT]
                case "CAVA_BRUT_NATURE":
                    aisles = [cls.CAVA_BRUT_NATURE]
                case "PINK_CAVA":
                    aisles = [cls.PINK_CAVA]
                case "MEDIUM_AND_MINI_CAVAS":
                    aisles = [cls.MEDIUM_AND_MINI_CAVAS]
                case "DRY_CAVA":
                    aisles = [cls.DRY_CAVA]
                case "SEMIDRY_CAVA":
                    aisles = [cls.SEMIDRY_CAVA]
                case "OTHER_CAVAS":
                    aisles = [cls.OTHER_CAVAS]
                case "CHAMPAGNE":
                    aisles = [cls.CHAMPAGNE]
                case "SPARKLING_CIDER":
                    aisles = [cls.SPARKLING_CIDER]
                case "NATURAL_CIDER":
                    aisles = [cls.NATURAL_CIDER]
        
        return aisles

class EroskiDrinkBeersAlimentation(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Beverages_Beers")

    ZERO0 = StaticAisle(name="zero0", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060233-cervezas/4000001-00/",
                             original_file_uri=os.path.join(category_path(), "Zero0.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Zero0_detailed.json"))
    
    EXTRA = StaticAisle(name="Extra", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060233-cervezas/4000002-extra/",
                                   original_file_uri=os.path.join(category_path(), "Extra.json"),
                                   mini_file_detailed_uri=os.path.join(category_path(), "Extra_detailed.json"))
    
    LAGER = StaticAisle(name="Lager", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060233-cervezas/4000000-lager/",
                            original_file_uri=os.path.join(category_path(), "Lager.json"),
                            mini_file_detailed_uri=os.path.join(category_path(), "Lager_detailed.json"))
    
    PREMIUM = StaticAisle(name="Premium", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060233-cervezas/4000004-premium/",
                                        original_file_uri=os.path.join(category_path(), "Premium.json"),
                                        mini_file_detailed_uri=os.path.join(category_path(), "Premium_detailed.json"))
    
    FLAVORS = StaticAisle(name="Flavors", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060233-cervezas/4000003-sabores/",
                           original_file_uri=os.path.join(category_path(), "Flavors.json"),
                           mini_file_detailed_uri=os.path.join(category_path(), "Flavors_detailed.json"))
  
    
    aisles: Final[List[StaticAisle]] = [ZERO0, EXTRA, LAGER, PREMIUM, FLAVORS]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "ZERO0":
                    aisles = [cls.ZERO0]
                case "EXTRA":
                    aisles = [cls.EXTRA]
                case "LAGER":
                    aisles = [cls.LAGER]
                case "PREMIUM":
                    aisles = [cls.PREMIUM]
                case "FLAVORS":
                    aisles = [cls.FLAVORS]
                
        return aisles

class EroskiDrinksAlimentation(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Beverages_Drinks")

    FINE = StaticAisle(name="Fine", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060294-finos-dulces-y-aperitivos/2060297-fino/",
                             original_file_uri=os.path.join(category_path(), "Fine.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Fine_detailed.json"))
    
    MUSCAT = StaticAisle(name="Muscat", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060294-finos-dulces-y-aperitivos/2060299-moscatel/",
                                   original_file_uri=os.path.join(category_path(), "Muscat.json"),
                                   mini_file_detailed_uri=os.path.join(category_path(), "Muscat_detailed.json"))
    
    MUST = StaticAisle(name="Must", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060294-finos-dulces-y-aperitivos/2060295-mosto/",
                            original_file_uri=os.path.join(category_path(), "Must.json"),
                            mini_file_detailed_uri=os.path.join(category_path(), "Must_detailed.json"))
    
    VERMOUTH = StaticAisle(name="Vermouth", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060294-finos-dulces-y-aperitivos/2060296-vermouth/",
                                        original_file_uri=os.path.join(category_path(), "Vermouth.json"),
                                        mini_file_detailed_uri=os.path.join(category_path(), "Vermouth_detailed.json"))
    
    MANZANILLA_WINE = StaticAisle(name="Manzanilla Wine", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060294-finos-dulces-y-aperitivos/2060298--vino-manzanilla/",
                           original_file_uri=os.path.join(category_path(), "Manzanilla_Wine.json"),
                           mini_file_detailed_uri=os.path.join(category_path(), "Manzanilla_Wine_detailed.json"))
  
    
    aisles: Final[List[StaticAisle]] = [FINE, MUSCAT, MUST, VERMOUTH, MANZANILLA_WINE]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "FINE":
                    aisles = [cls.FINE]
                case "MUSCAT":
                    aisles = [cls.MUSCAT]
                case "MUST":
                    aisles = [cls.MUST]
                case "VERMOUTH":
                    aisles = [cls.VERMOUTH]
                case "MANZANILLA_WINE":
                    aisles = [cls.MANZANILLA_WINE]
                
        return aisles

class EroskiDrinkLiquorAlimentation(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Beverages_Liquor")

    ANISE = StaticAisle(name="Anise", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060315-licor/2060324-anis/",
                             original_file_uri=os.path.join(category_path(), "Anise.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Anise_detailed.json"))
    
    COCKTAIL_AND_MIXED_DRINKS = StaticAisle(name="Cocktail and mixed drinks", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060315-licor/2060326-cocktail-y-combinados/",
                                   original_file_uri=os.path.join(category_path(), "Cocktail_and_mixed_drinks.json"),
                                   mini_file_detailed_uri=os.path.join(category_path(), "Cocktail_and_mixed_drinks_detailed.json"))
    
    COGNAC_AND_BRANDY = StaticAisle(name="Cognac and brandy", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060315-licor/2060321-cognac-y-brandy/",
                            original_file_uri=os.path.join(category_path(), "Cognac_and_brandy.json"),
                            mini_file_detailed_uri=os.path.join(category_path(), "Cognac_and_brandy_detailed.json"))
    
    GENEVA = StaticAisle(name="Geneva", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060315-licor/2060317-ginebra/",
                                        original_file_uri=os.path.join(category_path(), "Geneva.json"),
                                        mini_file_detailed_uri=os.path.join(category_path(), "Geneva_detailed.json"))
    
    FRUIT_LIQUEUR_WITH_ALCOHOL = StaticAisle(name="Fruit liqueur with alcohol", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060315-licor/2060319-licor-fruta-con-alcohol/",
                           original_file_uri=os.path.join(category_path(), "Fruit_liqueur_with_alcohol.json"),
                           mini_file_detailed_uri=os.path.join(category_path(), "Fruit_liqueur_with_alcohol_detailed.json"))
  
    NON_ALCOHOLIC_FRUIT_LIQUEUR = StaticAisle(name="Non-alcoholic fruit liqueur", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060315-licor/2060325-licor-frutas-sin-alcohol/",
                             original_file_uri=os.path.join(category_path(), "Non_alcoholic_fruit_liqueur.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Non_alcoholic_fruit_liqueur_detailed.json"))
    
    POMACE_AND_BRANDY = StaticAisle(name="Pomace and brandy", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060315-licor/2060320-orujo-y-aguardiente/",
                                   original_file_uri=os.path.join(category_path(), "Pomace_and_brandy.json"),
                                   mini_file_detailed_uri=os.path.join(category_path(), "Pomace_and_brandy_detailed.json"))
    
    PACHARÁN_AND_PUNCH = StaticAisle(name="Pacharán and punch", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060315-licor/2060322-pacharan-y-ponche/",
                            original_file_uri=os.path.join(category_path(), "Pacharán_and_punch.json"),
                            mini_file_detailed_uri=os.path.join(category_path(), "Pacharán_and_punch_detailed.json"))
    
    RUM = StaticAisle(name="Rum", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060315-licor/2060318-ron/",
                                        original_file_uri=os.path.join(category_path(), "Rum.json"),
                                        mini_file_detailed_uri=os.path.join(category_path(), "Rum_detailed.json"))
    
    VODKA_AND_TEQUILA = StaticAisle(name="Vodka and tequila", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060315-licor/2060323-vodka-y-tequila/",
                           original_file_uri=os.path.join(category_path(), "Vodka_and_tequila.json"),
                           mini_file_detailed_uri=os.path.join(category_path(), "Vodka_and_tequila_detailed.json"))
    
    WHISKY = StaticAisle(name="Whisky", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060315-licor/2060316-whisky/",
                           original_file_uri=os.path.join(category_path(), "Whisky.json"),
                           mini_file_detailed_uri=os.path.join(category_path(), "Whisky_detailed.json"))
  
    
    aisles: Final[List[StaticAisle]] = [ANISE, COCKTAIL_AND_MIXED_DRINKS, COGNAC_AND_BRANDY, GENEVA, FRUIT_LIQUEUR_WITH_ALCOHOL, NON_ALCOHOLIC_FRUIT_LIQUEUR, POMACE_AND_BRANDY, PACHARÁN_AND_PUNCH, RUM, VODKA_AND_TEQUILA, WHISKY]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "ANISE":
                    aisles = [cls.ANISE]
                case "COCKTAIL_AND_MIXED_DRINKS":
                    aisles = [cls.COCKTAIL_AND_MIXED_DRINKS]
                case "COGNAC_AND_BRANDY":
                    aisles = [cls.COGNAC_AND_BRANDY]
                case "GENEVA":
                    aisles = [cls.GENEVA]
                case "FRUIT_LIQUEUR_WITH_ALCOHOL":
                    aisles = [cls.FRUIT_LIQUEUR_WITH_ALCOHOL]
                case "NON_ALCOHOLIC_FRUIT_LIQUEUR":
                    aisles = [cls.NON_ALCOHOLIC_FRUIT_LIQUEUR]
                case "POMACE_AND_BRANDY":
                    aisles = [cls.POMACE_AND_BRANDY]
                case "PACHARÁN_AND_PUNCH":
                    aisles = [cls.PACHARÁN_AND_PUNCH]
                case "RUM":
                    aisles = [cls.RUM]
                case "VODKA_AND_TEQUILA":
                    aisles = [cls.VODKA_AND_TEQUILA]
                case "WHISKY":
                    aisles = [cls.WHISKY]
                
        return aisles

class EroskiDrinkOrganicProductsAlimentation(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Beverages_Drink_organic_products")

    ECO_DRINKS = StaticAisle(name="Eco drinks", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/5000308-productos-ecologicos/5000359-bebidas-eco/",
                             original_file_uri=os.path.join(category_path(), "Eco_drinks.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Eco_drinks_detailed.json"))
    
   
    aisles: Final[List[StaticAisle]] = [ECO_DRINKS]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "ECO_DRINKS":
                    aisles = [cls.ECO_DRINKS]
               
        return aisles

class EroskiDrinkRefreshementsAlimentation(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Beverages_Refreshements")

    ENERGY_DRINKS = StaticAisle(name="Energy drinks", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060219-refrescos/2060228-bebidas-energeticas/",
                             original_file_uri=os.path.join(category_path(), "Energy_drinks.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Energy_drinks_detailed.json"))
    
    ISOTONIC_DRINKS = StaticAisle(name="Isotonic drinks", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060219-refrescos/2060226-bebidas-isotonicas/",
                             original_file_uri=os.path.join(category_path(), "Isotonic_drinks.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Isotonic_drinks_detailed.json"))
    
    TAIL = StaticAisle(name="Tail", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060219-refrescos/2060221-cola-/",
                             original_file_uri=os.path.join(category_path(), "Tail.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Tail_detailed.json"))
    
    SPARKLING_LEMON = StaticAisle(name="Sparkling lemon", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060219-refrescos/2060223-limon-con-gas/",
                             original_file_uri=os.path.join(category_path(), "Sparkling_lemon.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Sparkling_lemon_detailed.json"))
    
    SPARKLING_ORANGE = StaticAisle(name="Sparkling orange", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060219-refrescos/2060222-naranja-con-gas/",
                             original_file_uri=os.path.join(category_path(), "Sparkling_orange.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Sparkling_orange_detailed.json"))
    
    OTHERS_WITH_GAS = StaticAisle(name="Others with gas", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060219-refrescos/2060225-otros-con-gas/",
                             original_file_uri=os.path.join(category_path(), "Others_with_gas.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Others_with_gas_detailed.json"))
    
    STILL_LEMON = StaticAisle(name="Still lemon", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060219-refrescos/2060230-limon-sin-gas/",
                             original_file_uri=os.path.join(category_path(), "Still_lemon.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Still_lemon_detailed.json"))
    
    STILL_ORANGE = StaticAisle(name="Still orange", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060219-refrescos/2060229-naranja-sin-gas/",
                             original_file_uri=os.path.join(category_path(), "Still_orange.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Still_orange_detailed.json"))
    
    OTHERS_WITHOUT_GAS = StaticAisle(name="Others without gas", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060219-refrescos/2060232-otros-sin-gas/",
                             original_file_uri=os.path.join(category_path(), "Others_without_gas.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Others_without_gas_detailed.json"))
    
    TEA_REFRESHMENTS = StaticAisle(name="Tea Refreshments", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060219-refrescos/2060227-refrescos-de-te/",
                             original_file_uri=os.path.join(category_path(), "Tea_Refreshments.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Tea_Refreshments_detailed.json"))
    
    TONICS_BITTERS_AND_SOFT_DRINKS = StaticAisle(name="Tonics, bitters and soft drinks", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060219-refrescos/2060224-tonicas-bitter-y-gaseosas/",
                             original_file_uri=os.path.join(category_path(), "Tonics_bitters_and_soft_drinks.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Tonics_bitters_and_soft_drinks_detailed.json"))
    
    
   
    aisles: Final[List[StaticAisle]] = [ENERGY_DRINKS, ISOTONIC_DRINKS, TAIL, SPARKLING_LEMON, SPARKLING_ORANGE, OTHERS_WITH_GAS, STILL_LEMON, STILL_ORANGE, OTHERS_WITHOUT_GAS, 
                                        TEA_REFRESHMENTS, TONICS_BITTERS_AND_SOFT_DRINKS]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "ENERGY_DRINKS":
                    aisles = [cls.ENERGY_DRINKS]
                case "ISOTONIC_DRINKS":
                    aisles = [cls.ISOTONIC_DRINKS]
                case "TAIL":
                    aisles = [cls.TAIL]
                case "SPARKLING_LEMON":
                    aisles = [cls.SPARKLING_LEMON]
                case "SPARKLING_ORANGE":
                    aisles = [cls.SPARKLING_ORANGE]
                case "OTHERS_WITH_GAS":
                    aisles = [cls.OTHERS_WITH_GAS]
                case "STILL_LEMON":
                    aisles = [cls.STILL_LEMON]
                case "STILL_ORANGE":
                    aisles = [cls.STILL_ORANGE]
                case "OTHERS_WITHOUT_GAS":
                    aisles = [cls.OTHERS_WITHOUT_GAS]
                case "TEA_REFRESHMENTS":
                    aisles = [cls.TEA_REFRESHMENTS]
                case "TONICS_BITTERS_AND_SOFT_DRINKS":
                    aisles = [cls.TONICS_BITTERS_AND_SOFT_DRINKS]
                
        return aisles

class EroskiDrinkWhiteWinesAlimentation(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Beverages_White_wines")

    NAVARRA_WHITE = StaticAisle(name="Navarra white", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060266-vinos-blancos/2060274-do-navarra-blanco/",
                             original_file_uri=os.path.join(category_path(), "Navarra_white.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Navarra_white_detailed.json"))
    
    PENEDÈS_WHITE = StaticAisle(name="Penedès white", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060266-vinos-blancos/2060268-do-penedes-blanco/",
                             original_file_uri=os.path.join(category_path(), "Penedès_white.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Penedès_white_detailed.json"))
    
    RÍAS_BAIXAS = StaticAisle(name="Rías Baixas", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060266-vinos-blancos/2060269-do-rias-baixas/",
                             original_file_uri=os.path.join(category_path(), "Rías_Baixas.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Rías_Baixas_detailed.json"))
    
    RIBEIRO = StaticAisle(name="Ribeiro", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060266-vinos-blancos/2060275-do-ribeiro/",
                             original_file_uri=os.path.join(category_path(), "Ribeiro.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Ribeiro_detailed.json"))
    
    RIOJA_WHITE = StaticAisle(name="Rioja white", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060266-vinos-blancos/2060271-do-rioja-blanco-/",
                             original_file_uri=os.path.join(category_path(), "Rioja_white.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Rioja_white_detailed.json"))
    
    RUEDA = StaticAisle(name="Rueda", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060266-vinos-blancos/2060267-do-rueda/",
                             original_file_uri=os.path.join(category_path(), "Rueda.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Rueda_detailed.json"))
    
    TXAKOLI = StaticAisle(name="Txakoli", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060266-vinos-blancos/2060272-do-txakoli/",
                             original_file_uri=os.path.join(category_path(), "Txakoli.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Txakoli_detailed.json"))
    
    VALDEPEÑAS_WHITE = StaticAisle(name="Valdepeñas white", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060266-vinos-blancos/2060276-do-valdepenas-blanco/",
                             original_file_uri=os.path.join(category_path(), "Valdepeñas_white.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Valdepeñas_white_detailed.json"))
    
    OTHER_WHITE_WINES = StaticAisle(name="Other white wines", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060266-vinos-blancos/2060277-otros-vinos-blancos/",
                             original_file_uri=os.path.join(category_path(), "Other_white_wines.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Other_white_wines_detailed.json"))
  
    
    aisles: Final[List[StaticAisle]] = [NAVARRA_WHITE, PENEDÈS_WHITE, RÍAS_BAIXAS, RIBEIRO, RIOJA_WHITE, RUEDA, TXAKOLI, VALDEPEÑAS_WHITE, OTHER_WHITE_WINES]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "NAVARRA_WHITE":
                    aisles = [cls.NAVARRA_WHITE]
                case "PENEDÈS_WHITE":
                    aisles = [cls.PENEDÈS_WHITE]
                case "RÍAS_BAIXAS":
                    aisles = [cls.RÍAS_BAIXAS]
                case "RIBEIRO":
                    aisles = [cls.RIBEIRO]
                case "RIOJA_WHITE":
                    aisles = [cls.RIOJA_WHITE]
                case "RUEDA":
                    aisles = [cls.RUEDA]
                case "TXAKOLI":
                    aisles = [cls.TXAKOLI]
                case "VALDEPEÑAS_WHITE":
                    aisles = [cls.VALDEPEÑAS_WHITE]
                case "OTHER_WHITE_WINES":
                    aisles = [cls.OTHER_WHITE_WINES]
     
        return aisles

class EroskiDrinkTableWinesAlimentation(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Beverages_Table_wines")

    WINE_BRIK = StaticAisle(name="Wine brik", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060289-vinos-de-mesa-y-sangrias/2060290-vino-brik/",
                             original_file_uri=os.path.join(category_path(), "Wine_brik.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Wine_brik_detailed.json"))
    
    CRYSTAL_WINE = StaticAisle(name="Crystal wine", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060289-vinos-de-mesa-y-sangrias/2060291-vino-cristal/",
                             original_file_uri=os.path.join(category_path(), "Crystal_wine.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Crystal_wine_detailed.json"))
    
    WINE_CARAFE = StaticAisle(name="Wine carafe", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060289-vinos-de-mesa-y-sangrias/2060293-vino-garrafa/",
                             original_file_uri=os.path.join(category_path(), "Wine_carafe.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Wine_carafe_detailed.json"))
    
    SANGRIAS_AND_TINTO_DE_VERANO = StaticAisle(name="Sangrias and tinto de verano", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060289-vinos-de-mesa-y-sangrias/2060292-sangrias-y-tinto-de-verano/",
                             original_file_uri=os.path.join(category_path(), "Sangrias_and_tinto_de_verano.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Sangrias_and_tinto_de_verano_detailed.json"))
   
    
    aisles: Final[List[StaticAisle]] = [WINE_BRIK, CRYSTAL_WINE, WINE_CARAFE, SANGRIAS_AND_TINTO_DE_VERANO]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "WINE_BRIK":
                    aisles = [cls.WINE_BRIK]
                case "CRYSTAL_WINE":
                    aisles = [cls.CRYSTAL_WINE]
                case "WINE_CARAFE":
                    aisles = [cls.WINE_CARAFE]
                case "SANGRIAS_AND_TINTO_DE_VERANO":
                    aisles = [cls.SANGRIAS_AND_TINTO_DE_VERANO]
                
     
        return aisles

class EroskiDrinkPinkWinesAlimentation(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Beverages_Pink_wines")

    NAVARRA_ROSÉ = StaticAisle(name="Navarra rosé", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060278-vinos-rosados/2060279-do-navarra-rosado/",
                             original_file_uri=os.path.join(category_path(), "Navarra_rosé.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Navarra_rosé_detailed.json"))
    
    PENEDÈS_ROSÉ = StaticAisle(name="Penedès rosé", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060278-vinos-rosados/2060284-do-penedes-rosado/",
                             original_file_uri=os.path.join(category_path(), "Penedès_rosé.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Penedès_rosé_detailed.json"))
    
    RIOJA_ROSÉ = StaticAisle(name="Rioja rosé", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060278-vinos-rosados/2060282-do-rioja-rosado/",
                             original_file_uri=os.path.join(category_path(), "Rioja_rosé.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Rioja_rosé_detailed.json"))
    
    VALDEPEÑAS_ROSÉ = StaticAisle(name="Valdepeñas rosé", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060278-vinos-rosados/2060285-do-valdepenas-rosado/",
                             original_file_uri=os.path.join(category_path(), "Valdepeñas_rosé.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Valdepeñas_rosé_detailed.json"))
   
    OTHER_ROSÉ_WINES = StaticAisle(name="Other rosé wines", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060278-vinos-rosados/2060288-otros-vinos-rosados/",
                             original_file_uri=os.path.join(category_path(), "Other_rosé_wines.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Other_rosé_wines_detailed.json"))
   
    
    aisles: Final[List[StaticAisle]] = [NAVARRA_ROSÉ, PENEDÈS_ROSÉ, RIOJA_ROSÉ, VALDEPEÑAS_ROSÉ, OTHER_ROSÉ_WINES]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "NAVARRA_ROSÉ":
                    aisles = [cls.NAVARRA_ROSÉ]
                case "PENEDÈS_ROSÉ":
                    aisles = [cls.PENEDÈS_ROSÉ]
                case "RIOJA_ROSÉ":
                    aisles = [cls.RIOJA_ROSÉ]
                case "VALDEPEÑAS_ROSÉ":
                    aisles = [cls.VALDEPEÑAS_ROSÉ]
                case "OTHER_ROSÉ_WINES":
                    aisles = [cls.OTHER_ROSÉ_WINES]
                
     
        return aisles

class EroskiDrinkRedWinesAlimentation(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Beverages_Red_wines")

    JUMILLA = StaticAisle(name="Jumilla", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060252-vinos-tintos/2060261-do-jumilla/",
                             original_file_uri=os.path.join(category_path(), "Jumilla.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Jumilla_detailed.json"))
    
    LA_MANCHA = StaticAisle(name="La Mancha", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060252-vinos-tintos/2060260-do-la-mancha/",
                             original_file_uri=os.path.join(category_path(), "La_Mancha.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "La_Mancha_detailed.json"))
    
    NAVARRA = StaticAisle(name="Navarra", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060252-vinos-tintos/2060257-do-navarra-/",
                             original_file_uri=os.path.join(category_path(), "Navarra.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Navarra_detailed.json"))
    
    RIBERA_DE_DUERO = StaticAisle(name="Ribera de Duero", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060252-vinos-tintos/2060258-do-ribera-de-duero-/",
                             original_file_uri=os.path.join(category_path(), "Ribera_de_Duero.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Ribera_de_Duero_detailed.json"))
   
    RIOJA_CRIANZA = StaticAisle(name="Rioja Crianza", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060252-vinos-tintos/2060254-do-rioja-crianza/",
                             original_file_uri=os.path.join(category_path(), "Rioja_Crianza.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Rioja_Crianza_detailed.json"))
   
    RIOJA_JOVEN = StaticAisle(name="Rioja Joven", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060252-vinos-tintos/2060253-do-rioja-joven/",
                             original_file_uri=os.path.join(category_path(), "Rioja_Joven.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Rioja_Joven_detailed.json"))
    
    RIOJA_RESERVA = StaticAisle(name="Rioja Reserva", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060252-vinos-tintos/2060255-do-rioja-reserva/",
                             original_file_uri=os.path.join(category_path(), "Rioja_Reserva.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Rioja_Reservaa_detailed.json"))
    
    SOMONTANO = StaticAisle(name="Somontano", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060252-vinos-tintos/2060262-do-somontano/",
                             original_file_uri=os.path.join(category_path(), "Somontano.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Somontano_detailed.json"))
    
    TORO = StaticAisle(name="Toro", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060252-vinos-tintos/2060263-do-toro/",
                             original_file_uri=os.path.join(category_path(), "Toro.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Toro_detailed.json"))
   
    VALDEPEÑAS = StaticAisle(name="Valdepeñas", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060252-vinos-tintos/2060259-do-valdepenas-/",
                             original_file_uri=os.path.join(category_path(), "Valdepeñas.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Valdepeñas_detailed.json"))
   
    WINES_OF_THE_LAND = StaticAisle(name="Wines of the land", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060252-vinos-tintos/2060264-vinos-de-la-tierra-/",
                             original_file_uri=os.path.join(category_path(), "Wines_of_the_land.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Wines_of_the_land_detailed.json"))
    
    OTHER_RED_WINES = StaticAisle(name="Other red wines", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060252-vinos-tintos/2060265-otros-vinos-tintos/",
                             original_file_uri=os.path.join(category_path(), "Other_red_wines.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Other_red_wines_detailed.json"))
    
   
   
    
    aisles: Final[List[StaticAisle]] = [JUMILLA, LA_MANCHA, NAVARRA, RIBERA_DE_DUERO, RIOJA_CRIANZA, RIOJA_JOVEN, RIOJA_RESERVA, SOMONTANO, TORO, VALDEPEÑAS, WINES_OF_THE_LAND, OTHER_RED_WINES]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "JUMILLA":
                    aisles = [cls.JUMILLA]
                case "LA_MANCHA":
                    aisles = [cls.LA_MANCHA]
                case "NAVARRA":
                    aisles = [cls.NAVARRA]
                case "RIBERA_DE_DUERO":
                    aisles = [cls.RIBERA_DE_DUERO]
                case "RIOJA_CRIANZA":
                    aisles = [cls.RIOJA_CRIANZA]
                case "RIOJA_JOVEN":
                    aisles = [cls.RIOJA_JOVEN]
                case "RIOJA_RESERVA":
                    aisles = [cls.RIOJA_RESERVA]
                case "SOMONTANO":
                    aisles = [cls.SOMONTANO]
                case "TORO":
                    aisles = [cls.TORO]
                case "VALDEPEÑAS":
                    aisles = [cls.VALDEPEÑAS]
                case "WINES_OF_THE_LAND":
                    aisles = [cls.WINES_OF_THE_LAND]
                case "OTHER_RED_WINES":
                    aisles = [cls.OTHER_RED_WINES]
               
     
        return aisles

class EroskiDrinkJuiceAndNectarAlimentation(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Beverages_Juice_and_nectar")

    FUNCTIONAL = StaticAisle(name="Functional", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060243-zumos-y-nectar/4000007-funcionales/",
                             original_file_uri=os.path.join(category_path(), "Functional.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Functional_detailed.json"))
    
    TO_GO = StaticAisle(name="To go", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060243-zumos-y-nectar/4000008-to-go/",
                             original_file_uri=os.path.join(category_path(), "To_go.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "To_go_detailed.json"))
    
    REFRIGERATED_JUICES = StaticAisle(name="Refrigerated juices", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060243-zumos-y-nectar/4000010-zumos-refrigerados/",
                             original_file_uri=os.path.join(category_path(), "Refrigerated_juices.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Refrigerated_juices_detailed.json"))
    
    JUICES_AND_NECTARS = StaticAisle(name="Juices and nectars", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060243-zumos-y-nectar/4000006-zumos-y-nectares/",
                             original_file_uri=os.path.join(category_path(), "Juices_and_nectars.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Juices_and_nectars_detailed.json"))
   
   
    
   
   
    
    aisles: Final[List[StaticAisle]] = [FUNCTIONAL, TO_GO, REFRIGERATED_JUICES, JUICES_AND_NECTARS]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "FUNCTIONAL":
                    aisles = [cls.FUNCTIONAL]
                case "TO_GO":
                    aisles = [cls.TO_GO]
                case "REFRIGERATED_JUICES":
                    aisles = [cls.REFRIGERATED_JUICES]
                case "JUICES_AND_NECTARS":
                    aisles = [cls.JUICES_AND_NECTARS]
              
        return aisles

#FrozenFood

class EroskiFrozenIceCreamAndDessertsAlimentation(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frozen_Ice_cream_and_desserts")

    ICE_CUBES = StaticAisle(name="Ice cubes", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059952-helados-y-postres/2059960-cubitos-de-hielo/",
                             original_file_uri=os.path.join(category_path(), "Ice_cubes.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Ice_cubes_detailed.json"))
    
    ICED_FRUITS = StaticAisle(name="Iced fruits", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059952-helados-y-postres/2059963-frutas-heladas/",
                             original_file_uri=os.path.join(category_path(), "Iced_fruits.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Iced_fruits_detailed.json"))
    
    ICE_CREAM_BLOCK = StaticAisle(name="Ice cream block", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059952-helados-y-postres/2059962-helados-bloque/",
                             original_file_uri=os.path.join(category_path(), "Ice_cream_block.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Ice_cream_block_detailed.json"))
    
    CHOCOLATE_ICE_CREAM = StaticAisle(name="Chocolate ice cream", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059952-helados-y-postres/2059953-helados-bombon/",
                             original_file_uri=os.path.join(category_path(), "Chocolate_ice_cream.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Chocolate_ice_cream_detailed.json"))
 
    ICE_CREAM_CONE = StaticAisle(name="Ice cream cone", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059952-helados-y-postres/2059956-helados-cono/",
                             original_file_uri=os.path.join(category_path(), "Ice_cream_cone.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Ice_cream_cone_detailed.json"))
    
    ICE_CREAM_AND_CHILDRENS_ICE_CREAM = StaticAisle(name="Ice cream and children's ice cream", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059952-helados-y-postres/2059955-helados-hielo-e-infantiles/",
                             original_file_uri=os.path.join(category_path(), "Ice_cream_and_childrens_ice_cream.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Ice_cream_and_childrens_ice_cream_detailed.json"))
    
    OTHER_ICE_CREAMS = StaticAisle(name="Other ice creams", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059952-helados-y-postres/2059961-otros-helados/",
                             original_file_uri=os.path.join(category_path(), "Other_ice_creams.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Other_ice_creams_detailed.json"))
    
    ICE_CREAM_TUBS = StaticAisle(name="Ice cream tubs", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059952-helados-y-postres/2059954-helados-tarrina/",
                             original_file_uri=os.path.join(category_path(), "Ice_cream_tubs.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Ice_cream_tubs_detailed.json"))
    
    CREAM_SLUSHIES_AND_TRUFFLES = StaticAisle(name="Cream, slushies and truffles", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059952-helados-y-postres/2059959-nata-granizados-y-trufas/",
                             original_file_uri=os.path.join(category_path(), "Cream_slushies_and_truffles.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Cream_slushies_and_truffles_detailed.json"))
    
    SANDWICH_AND_SNACKS = StaticAisle(name="Sandwich and snacks", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059952-helados-y-postres/2059957-sandwich-y-snacks/",
                             original_file_uri=os.path.join(category_path(), "Sandwich_and_snacks.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Sandwich_and_snacks_detailed.json"))
    
    ICE_CREAM_CAKES = StaticAisle(name="Ice cream cakes", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059952-helados-y-postres/2059958-tartas-heladas/",
                             original_file_uri=os.path.join(category_path(), "Ice_cream_cakes.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Ice_cream_cakes_detailed.json"))
   
    
    aisles: Final[List[StaticAisle]] = [ICE_CUBES, ICED_FRUITS, ICE_CREAM_BLOCK, CHOCOLATE_ICE_CREAM, ICE_CREAM_CONE, ICE_CREAM_AND_CHILDRENS_ICE_CREAM, OTHER_ICE_CREAMS, ICE_CREAM_TUBS, CREAM_SLUSHIES_AND_TRUFFLES, SANDWICH_AND_SNACKS, ICE_CREAM_CAKES]	

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "ICE_CUBES":
                    aisles = [cls.ICE_CUBES]
                case "ICED_FRUITS":
                    aisles = [cls.ICED_FRUITS]
                case "ICE_CREAM_BLOCK":
                    aisles = [cls.ICE_CREAM_BLOCK]
                case "CHOCOLATE_ICE_CREAM":
                    aisles = [cls.CHOCOLATE_ICE_CREAM]
                case "ICE_CREAM_CONE":
                    aisles = [cls.ICE_CREAM_CONE]
                case "ICE_CREAM_AND_CHILDRENS_ICE_CREAM":
                    aisles = [cls.ICE_CREAM_AND_CHILDRENS_ICE_CREAM]
                case "OTHER_ICE_CREAMS":
                    aisles = [cls.OTHER_ICE_CREAMS]
                case "ICE_CREAM_TUBS":
                    aisles = [cls.ICE_CREAM_TUBS]
                case "CREAM_SLUSHIES_AND_TRUFFLES":
                    aisles = [cls.CREAM_SLUSHIES_AND_TRUFFLES]
                case "SANDWICH_AND_SNACKS":
                    aisles = [cls.SANDWICH_AND_SNACKS]
                case "ICE_CREAM_CAKES":
                    aisles = [cls.ICE_CREAM_CAKES]
              
        return aisles

class EroskiFrozenBakeryAndPastryAlimentation(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frozen_Bakery_and_pastry")

    CHURROS_AND_PORRAS = StaticAisle(name="Churros and porras", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059983-panaderia-y-pasteleria/2059986-churros-y-porras/",
                             original_file_uri=os.path.join(category_path(), "Churros_and_porras.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Churros_and_porras_detailed.json"))
    
    OTHER_MASSES = StaticAisle(name="Other masses", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059983-panaderia-y-pasteleria/2059985-otras-masas/",
                             original_file_uri=os.path.join(category_path(), "Other_masses.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Other_masses_detailed.json"))
    
   
    aisles: Final[List[StaticAisle]] = [CHURROS_AND_PORRAS, OTHER_MASSES]	

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "CHURROS_AND_PORRAS":
                    aisles = [cls.CHURROS_AND_PORRAS]
                case "OTHER_MASSES":
                    aisles = [cls.OTHER_MASSES]
               
              
        return aisles

class EroskiFrozenVegetableAlimentation(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frozen_vegetable")

    ARTICHOKES = StaticAisle(name="Artichokes", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059942-patatas-verduras-y-setas/2059948-alcachofas/",
                             original_file_uri=os.path.join(category_path(), "Artichokes.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Artichokes_detailed.json"))
    
    SALAD = StaticAisle(name="Salad", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059942-patatas-verduras-y-setas/2059949-ensaladilla/",
                             original_file_uri=os.path.join(category_path(), "Salad.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Salad_detailed.json"))
    
    SPINACH_AND_BROAD_BEANS = StaticAisle(name="Spinach and broad beans", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059942-patatas-verduras-y-setas/2059947-espinacas-y-habas/",
                             original_file_uri=os.path.join(category_path(), "Spinach_and_broad_beans.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Spinach_and_broad_beans_detailed.json"))
    
    PEAS = StaticAisle(name="Peas", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059942-patatas-verduras-y-setas/2059946-guisantes/",
                             original_file_uri=os.path.join(category_path(), "Peas.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Peas_detailed.json"))
    
    JEWISH = StaticAisle(name="Jewish", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059942-patatas-verduras-y-setas/2059945-judias/",
                             original_file_uri=os.path.join(category_path(), "Jewish.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Jewish_detailed.json"))
    
    STEW = StaticAisle(name="Stew", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059942-patatas-verduras-y-setas/2059944-menestra/",
                             original_file_uri=os.path.join(category_path(), "Stew.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Stew_detailed.json"))
    
    POTATOES = StaticAisle(name="Potatoes", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059942-patatas-verduras-y-setas/2059943-patatas/",
                             original_file_uri=os.path.join(category_path(), "Potatoes.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Potatoes_detailed.json"))
    
    OTHER_VEGETABLES = StaticAisle(name="Other vegetables", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059942-patatas-verduras-y-setas/2059950-otras-verduras-/",
                             original_file_uri=os.path.join(category_path(), "Other_vegetables.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Other_vegetables_detailed.json"))
    
   
    aisles: Final[List[StaticAisle]] = [ARTICHOKES, SALAD, SPINACH_AND_BROAD_BEANS, PEAS, JEWISH, STEW, POTATOES, OTHER_VEGETABLES]	

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "ARTICHOKES":
                    aisles = [cls.ARTICHOKES]
                case "SALAD":
                    aisles = [cls.SALAD]
                case "SPINACH_AND_BROAD_BEANS":
                    aisles = [cls.SPINACH_AND_BROAD_BEANS]
                case "PEAS":
                    aisles = [cls.PEAS]
                case "JEWISH":
                    aisles = [cls.JEWISH]
                case "STEW":
                    aisles = [cls.STEW]
                case "POTATOES":
                    aisles = [cls.POTATOES]
                case "OTHER_VEGETABLES":
                    aisles = [cls.OTHER_VEGETABLES]
               
              
        return aisles

class EroskiFrozenFishAlimentation(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frozen_fish")

    COD = StaticAisle(name="Cod", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059927-pescado/2059929-bacalao/",
                             original_file_uri=os.path.join(category_path(), "Cod.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Cod_detailed.json"))
    
    SQUID = StaticAisle(name="Squid", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059927-pescado/2059931-calamar-/",
                             original_file_uri=os.path.join(category_path(), "Squid.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Squid_detailed.json"))
    
    HAKE = StaticAisle(name="Hake", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059927-pescado/2059928-merluza/",
                             original_file_uri=os.path.join(category_path(), "Hake.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Hake_detailed.json"))
    
    PREPARED_FISH = StaticAisle(name="Prepared fish" , url= "https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059927-pescado/2059932-pescados-preparados/",
                             original_file_uri=os.path.join(category_path(), "Prepared_fish.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Prepared_fish_detailed.json"))
    
    OTHER_FISH = StaticAisle(name="Other fish", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059927-pescado/2059933-otros-pescados/",
                             original_file_uri=os.path.join(category_path(), "Other_fish.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Other_fish_detailed.json"))
    
   
    aisles: Final[List[StaticAisle]] = [COD, SQUID, HAKE, PREPARED_FISH, OTHER_FISH]	

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "COD":
                    aisles = [cls.COD]
                case "SQUID":
                    aisles = [cls.SQUID]
                case "HAKE":
                    aisles = [cls.HAKE]
                case "PREPARED_FISH":
                    aisles = [cls.PREPARED_FISH]
                case "OTHER_FISH":
                    aisles = [cls.OTHER_FISH]
            
        return aisles

class EroskiFrozenPizzasAlimentation(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frozen_pizzas")

    PIZZA_BASE = StaticAisle(name="Cod", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059920-pizzas/2059926-base-pizza/",
                             original_file_uri=os.path.join(category_path(), "Pizza_base.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Pizza_base_detailed.json"))
    
    BAGUETTE_PIZZA = StaticAisle(name="Baguette pizza", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059920-pizzas/2059923-pizza-baguette/",
                             original_file_uri=os.path.join(category_path(), "Baguette_pizza.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Baguette_pizza_detailed.json"))
    
    PIZZAS = StaticAisle(name="Pizzas", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059920-pizzas/2059921-pizzas/",
                             original_file_uri=os.path.join(category_path(), "Pizzas.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Pizzas_detailed.json"))
    
    SNACK_PIZZA = StaticAisle(name="Snack pizza", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059920-pizzas/2059924-pizza-snack/",
                             original_file_uri=os.path.join(category_path(), "Snack_pizza.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Snack_pizza_detailed.json"))
    
   
    aisles: Final[List[StaticAisle]] = [PIZZA_BASE, BAGUETTE_PIZZA, PIZZAS, SNACK_PIZZA]	

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "PIZZA_BASE":
                    aisles = [cls.PIZZA_BASE]
                case "BAGUETTE_PIZZA":
                    aisles = [cls.BAGUETTE_PIZZA]
                case "PIZZAS":
                    aisles = [cls.PIZZAS]
                case "SNACK_PIZZA":
                    aisles = [cls.SNACK_PIZZA]
            
        return aisles

class EroskiFrozenReadyMealsAlimentation(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frozen_ready_meals")

    WINGS_MEATBALLS_AND_OTHERS = StaticAisle(name="Wings, meatballs and others", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059964-platos-preparados/2059973-alitas-albondigas-y-otros/",
                             original_file_uri=os.path.join(category_path(), "Wings_meatballs_and_others.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Wings_meatballs_and_others_detailed.json"))
    
    INTERNATIONAL_FOOD = StaticAisle(name="International food", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059964-platos-preparados/2059975-comida-internacional/",
                             original_file_uri=os.path.join(category_path(), "International_food.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "International_food_detailed.json"))
    
    CANNELLONI = StaticAisle(name="Cannelloni", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059964-platos-preparados/2059967-canelones/",
                             original_file_uri=os.path.join(category_path(), "Cannelloni.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Cannelloni_detailed.json"))
    
    CROQUETTES = StaticAisle(name="Croquettes", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059964-platos-preparados/2059965-croquetas/",
                             original_file_uri=os.path.join(category_path(), "Croquettes.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Croquettes_detailed.json"))
    
    DUMPLINGS = StaticAisle(name="Dumplings", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059964-platos-preparados/2059970-empanadillas/",
                             original_file_uri=os.path.join(category_path(), "Dumplings.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Dumplings_detailed.json"))
    
    LASAGNA = StaticAisle(name="Lasagna", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059964-platos-preparados/2059966-lasana/",
                             original_file_uri=os.path.join(category_path(), "Lasagna.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Lasagna_detailed.json"))
    
    NUGGETS_AND_CHICKEN = StaticAisle(name="Nuggets and chicken", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059964-platos-preparados/2059969-nuggets-y-pollo/",
                             original_file_uri=os.path.join(category_path(), "Nuggets_and_chicken.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Nuggets_and_chicken_detailed.json"))
    
    ST_JAMES = StaticAisle(name="St. James", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059964-platos-preparados/2059971-san-jacobo/",
                             original_file_uri=os.path.join(category_path(), "St_James.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "St_James_detailed.json"))
    
    OTHER_FRIED_FOODS = StaticAisle(name="Other fried foods", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059964-platos-preparados/2059972-otros-fritos/",
                             original_file_uri=os.path.join(category_path(), "Other_fried_foods.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Other_fried_foods_detailed.json"))
    
    VEGAN_PRODUCTS = StaticAisle(name="Vegan products", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059964-platos-preparados/4000030-productos-veganos/",
                             original_file_uri=os.path.join(category_path(), "Vegan_products.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Vegan_products_detailed.json"))
    
    FIRST_COURSES = StaticAisle(name="First courses", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059964-platos-preparados/4000031-primeros-platos/",
                             original_file_uri=os.path.join(category_path(), "First_courses.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "First_courses_detailed.json"))
    
    SECOND_COURSES = StaticAisle(name="Second courses", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059964-platos-preparados/4000032-segundos-platos/",
                             original_file_uri=os.path.join(category_path(), "Second_courses.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Second_courses_detailed.json"))
    
   
    aisles: Final[List[StaticAisle]] = [WINGS_MEATBALLS_AND_OTHERS, INTERNATIONAL_FOOD, CANNELLONI, CROQUETTES, DUMPLINGS, LASAGNA, NUGGETS_AND_CHICKEN, ST_JAMES, OTHER_FRIED_FOODS, VEGAN_PRODUCTS, FIRST_COURSES, SECOND_COURSES]	

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "WINGS_MEATBALLS_AND_OTHERS":
                    aisles = [cls.WINGS_MEATBALLS_AND_OTHERS]
                case "INTERNATIONAL_FOOD":
                    aisles = [cls.INTERNATIONAL_FOOD]
                case "CANNELLONI":
                    aisles = [cls.CANNELLONI]
                case "CROQUETTES":
                    aisles = [cls.CROQUETTES]
                case "DUMPLINGS":
                    aisles = [cls.DUMPLINGS]
                case "LASAGNA":
                    aisles = [cls.LASAGNA]
                case "NUGGETS_AND_CHICKEN":
                    aisles = [cls.NUGGETS_AND_CHICKEN]
                case "ST_JAMES":
                    aisles = [cls.ST_JAMES]
                case "OTHER_FRIED_FOODS":
                    aisles = [cls.OTHER_FRIED_FOODS]
                case "VEGAN_PRODUCTS":
                    aisles = [cls.VEGAN_PRODUCTS]
                case "FIRST_COURSES":
                    aisles = [cls.FIRST_COURSES]
                case "SECOND_COURSES":
                    aisles = [cls.SECOND_COURSES]
            
        return aisles

class EroskiFrozenSeafoodAlimentation(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frozen_seafood")

    EEL_SUBSTITUTE = StaticAisle(name="Eel substitute", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059934-marisco/2059939-sucedaneo-de-angulas/",
                             original_file_uri=os.path.join(category_path(), "Eel_substitute.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Eel_substitute_detailed.json"))
    
    FROZEN_COOKED_PRAWNS = StaticAisle(name="Frozen cooked prawns", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059934-marisco/2059937-langostino-cocido-congelado/",
                             original_file_uri=os.path.join(category_path(), "Frozen_cooked_prawns.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Frozen_cooked_prawns_detailed.json"))
    
    FROZEN_RAW_PRAWNS = StaticAisle(name="Frozen raw prawns", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059934-marisco/2059936-langostino-crudo-congelado/",
                             original_file_uri=os.path.join(category_path(), "Frozen_raw_prawns.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Frozen_raw_prawns_detailed.json"))
    
    PAELLA_PREPARED = StaticAisle(name="Paella Prepared", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059934-marisco/2059941-preparado-paella/",
                             original_file_uri=os.path.join(category_path(), "Paella_Prepared.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Paella_Prepared_detailed.json"))
    
    SURIMI_AND_STICKS = StaticAisle(name="Surimi and sticks", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059934-marisco/2059940-surimi-y-palitos/",
                             original_file_uri=os.path.join(category_path(), "Surimi_and_sticks.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Surimi_and_sticks_detailed.json"))
    
    OTHER_SEAFOOD = StaticAisle(name="Other seafood", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059934-marisco/2059938-otros-mariscos/",
                             original_file_uri=os.path.join(category_path(), "Other_seafood.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Other_seafood_detailed.json"))
    
   
    aisles: Final[List[StaticAisle]] = [EEL_SUBSTITUTE, FROZEN_COOKED_PRAWNS, FROZEN_RAW_PRAWNS, PAELLA_PREPARED, SURIMI_AND_STICKS, OTHER_SEAFOOD]	

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "EEL_SUBSTITUTE":
                    aisles = [cls.EEL_SUBSTITUTE]
                case "FROZEN_COOKED_PRAWNS":
                    aisles = [cls.FROZEN_COOKED_PRAWNS]
                case "FROZEN_RAW_PRAWNS":
                    aisles = [cls.FROZEN_RAW_PRAWNS]
                case "PAELLA_PREPARED":
                    aisles = [cls.PAELLA_PREPARED]
                case "SURIMI_AND_STICKS":
                    aisles = [cls.SURIMI_AND_STICKS]
                case "OTHER_SEAFOOD":
                    aisles = [cls.OTHER_SEAFOOD]
                
        return aisles

class EroskiFrozenstirFriesAndScramblesAlimentation(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frozen_stir_fries_and_scrambles")

    SAUTÉED_RICE_AND_PASTA = StaticAisle(name="Sautéed rice and pasta", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059977-salteados-y-revueltos/2059978-salteado-arroz-y-pasta/",
                             original_file_uri=os.path.join(category_path(), "Sautéed_rice_and_pasta.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Sautéed_rice_and_pasta_detailed.json"))
    
    SAUTÉED_VEGETABLES_AND_LEGUMES = StaticAisle(name="Sautéed vegetables and legumes", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059977-salteados-y-revueltos/2059979-salteado-verduras-y-legumbres/",
                             original_file_uri=os.path.join(category_path(), "Sautéed_vegetables_and_legumes.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Sautéed_vegetables_and_legumes_detailed.json"))
    
 
    aisles: Final[List[StaticAisle]] = [SAUTÉED_RICE_AND_PASTA, SAUTÉED_VEGETABLES_AND_LEGUMES]	

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "SAUTÉED_RICE_AND_PASTA":
                    aisles = [cls.SAUTÉED_RICE_AND_PASTA]
                case "SAUTÉED_VEGETABLES_AND_LEGUMES":
                    aisles = [cls.SAUTÉED_VEGETABLES_AND_LEGUMES]
                
                
        return aisles

#Bebe

class EroskiBabyMilkAlimentation(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "baby_Milk")

    LIQUID_FIRST_BABY_MILK1 = StaticAisle(name="Liquid first baby milk 1", url="https://supermercado.eroski.es/es/supermercado/2060327-bebe/2060352-leche-y-aguas/2060354-leche-liquida-inicio-1/",
                             original_file_uri=os.path.join(category_path(), "Liquid_first_baby_milk1.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Liquid_first_baby_milk1_detailed.json"))

    POWDERED_FIRST_BABY_MILK1 = StaticAisle(name="Powdered first baby milk 1", url="https://supermercado.eroski.es/es/supermercado/2060327-bebe/2060352-leche-y-aguas/2060353-leche-polvo-inicio-1/",
                             original_file_uri=os.path.join(category_path(), "Powdered_first_baby_milk1.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Powdered_first_baby_milk1_detailed.json"))
    
    LIQUID_MILK_CONTINUED2  = StaticAisle(name="Liquid milk continued 2", url="https://supermercado.eroski.es/es/supermercado/2060327-bebe/2060352-leche-y-aguas/2060356-leche-liquida-continuacion-2/",
                             original_file_uri=os.path.join(category_path(), "Liquid_milk_continued2.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Liquid_milk_continued2_detailed.json"))
    
    POWDERED_MILK_CONTINUED2  = StaticAisle(name="Powdered milk continued 2", url="https://supermercado.eroski.es/es/supermercado/2060327-bebe/2060352-leche-y-aguas/2060355-leche-polvo-continuacion-2/",
                             original_file_uri=os.path.join(category_path(), "Powdered_milk_continued2.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Powdered_milk_continued2_detailed.json"))
    
    LIQUID_MILK_GROWTH3  = StaticAisle(name="Liquid milk growth 3", url="https://supermercado.eroski.es/es/supermercado/2060327-bebe/2060352-leche-y-aguas/2060358-leche-liquida-crecimiento-3/",
                             original_file_uri=os.path.join(category_path(), "Liquid_milk_growth3.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Liquid_milk_growth3_detailed.json"))
    
    POWDERED_BABY_MILK3  = StaticAisle(name="Powdered baby milk 3", url="https://supermercado.eroski.es/es/supermercado/2060327-bebe/2060352-leche-y-aguas/2060357-leche-polvo-crecimiento-3/",
                             original_file_uri=os.path.join(category_path(), "Powdered_baby_milk3.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Powdered_baby_milk32_detailed.json"))


    aisles: Final[List[StaticAisle]] = [LIQUID_FIRST_BABY_MILK1, POWDERED_FIRST_BABY_MILK1, LIQUID_MILK_CONTINUED2, POWDERED_MILK_CONTINUED2, LIQUID_MILK_GROWTH3, POWDERED_BABY_MILK3]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "LIQUID_FIRST_BABY_MILK1":
                    aisles = [cls.LIQUID_FIRST_BABY_MILK1]
                case "POWDERED_FIRST_BABY_MILK1":
                    aisles = [cls.POWDERED_FIRST_BABY_MILK1]
                case "LIQUID_MILK_CONTINUED2":
                    aisles = [cls.LIQUID_MILK_CONTINUED2]
                case "POWDERED_MILK_CONTINUED2":
                    aisles = [cls.POWDERED_MILK_CONTINUED2]
                case "LIQUID_MILK_GROWTH3":
                    aisles = [cls.LIQUID_MILK_GROWTH3]
                case "POWDERED_BABY_MILK3":
                    aisles = [cls.POWDERED_BABY_MILK3]
                
                
        return aisles
    
class EroskiBabyDesertAndAfternoonTeaAlimentation(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Baby_Desert_And_Afternoon_Tea")

    DAIRY_DESSERT = StaticAisle(name="Dairy dessert", url="https://supermercado.eroski.es/es/supermercado/2060327-bebe/2060383-postres-y-meriendas/2060389-postre-lacteo/",
                             original_file_uri=os.path.join(category_path(), "Dairy_dessert.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Dairy_dessert_detailed.json"))
    
    ORGANIC_DESSERT_AFTERNOON_TEA  = StaticAisle(name="Organic dessert-afternoon tea", url="https://supermercado.eroski.es/es/supermercado/2060327-bebe/2060383-postres-y-meriendas/2060391-postres-y-meriendas-biologicas/",
                             original_file_uri=os.path.join(category_path(), "Organic_dessert_afternoon_tea.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Organic_dessert_afternoon_tea_detailed.json"))
    
    OTHER_DESSERTS  = StaticAisle(name="Other desserts", url="https://supermercado.eroski.es/es/supermercado/2060327-bebe/2060383-postres-y-meriendas/2060392-otros-postres/",
                             original_file_uri=os.path.join(category_path(), "Other_desserts.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Other_desserts_detailed.json"))
    

    
 
    aisles: Final[List[StaticAisle]] = [DAIRY_DESSERT, ORGANIC_DESSERT_AFTERNOON_TEA, OTHER_DESSERTS]	

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "DAIRY_DESSERT":
                    aisles = [cls.DAIRY_DESSERT]
                case "ORGANIC_DESSERT_AFTERNOON_TEA":
                    aisles = [cls.ORGANIC_DESSERT_AFTERNOON_TEA]
                case "OTHER_DESSERTS":
                    aisles = [cls.OTHER_DESSERTS]
                
                
        return aisles
    
class EroskiBabyOrganicProductsAlimentation(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Baby_Organic_products")

    BABY_PRODUCTS = StaticAisle(name="Baby products", url="https://supermercado.eroski.es/es/supermercado/2060327-bebe/5000310-productos-ecologicos/",
                             original_file_uri=os.path.join(category_path(), "Baby_products.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Baby_products_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [BABY_PRODUCTS]
    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "BABY_PRODUCTS":
                    aisles = [cls.BABY_PRODUCTS]
        return aisles
                
class EroskiBabymealsAlimentation(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Baby_Meals")

    BISCUITS_AND_SNACKS = StaticAisle(name="Biscuits and snacks", url="https://supermercado.eroski.es/es/supermercado/2060327-bebe/2060361-tarritos-potitos-papillas-y-otros-alimentos/2060379-galletas-y-snacks/",
                             original_file_uri=os.path.join(category_path(), "Biscuits_and_snacks.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Biscuits_and_snacks_detailed.json"))
    
    MENUS = StaticAisle(name="Menus", url="https://supermercado.eroski.es/es/supermercado/2060327-bebe/2060361-tarritos-potitos-papillas-y-otros-alimentos/2060367-menus/",
                             original_file_uri=os.path.join(category_path(), "Menus.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Menus_detailed.json"))
    
    ORGANIC_BABY_CEREAL = StaticAisle(name="Organic baby cereal", url="https://supermercado.eroski.es/es/supermercado/2060327-bebe/2060361-tarritos-potitos-papillas-y-otros-alimentos/2060377-papillas-biologicas/",
                             original_file_uri=os.path.join(category_path(), "Organic_baby_cereal.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Organic_baby_cereal_detailed.json"))
    
    POWDERED_BABY_CEREAL = StaticAisle(name="Powdered baby cereal", url="https://supermercado.eroski.es/es/supermercado/2060327-bebe/2060361-tarritos-potitos-papillas-y-otros-alimentos/2060369-papillas-polvo-cereales/",
                             original_file_uri=os.path.join(category_path(), "Powdered_baby_cereal.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Powdered_baby_cereal_detailed.json"))
    
    LIQUID_BABY_CEREAL = StaticAisle(name="Liquid baby cereal", url="https://supermercado.eroski.es/es/supermercado/2060327-bebe/2060361-tarritos-potitos-papillas-y-otros-alimentos/2060374-papillas-liquidas-cereales/",
                             original_file_uri=os.path.join(category_path(), "Liquid_baby_cereal.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Liquid_baby_cereal_detailed.json"))
    
    MEAT_BABY_MEALS = StaticAisle(name="Meat baby meals", url="https://supermercado.eroski.es/es/supermercado/2060327-bebe/2060361-tarritos-potitos-papillas-y-otros-alimentos/2060364-tarritos-y-tarrinas-de-carne/",
                             original_file_uri=os.path.join(category_path(), "Meat_baby_meals.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Meat_baby_meals_detailed.json"))
    
    FRUIT_BABY_MEALS = StaticAisle(name="Fruit baby meals", url="https://supermercado.eroski.es/es/supermercado/2060327-bebe/2060361-tarritos-potitos-papillas-y-otros-alimentos/2060362-tarritos-y-tarrinas-de-fruta/",
                             original_file_uri=os.path.join(category_path(), "Fruit_baby_meals.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Fruit_baby_meals_detailed.json"))
    
    FISH_BABY_MEALS = StaticAisle(name="Fish baby meals", url="https://supermercado.eroski.es/es/supermercado/2060327-bebe/2060361-tarritos-potitos-papillas-y-otros-alimentos/2060365-tarritos-y-tarrinas-de-pescado/",
                             original_file_uri=os.path.join(category_path(), "Fish_baby_meals.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Fish_baby_meals_detailed.json"))
    
    VEGETABLE_BABY_MEALS = StaticAisle(name="Vegetable baby meals", url="https://supermercado.eroski.es/es/supermercado/2060327-bebe/2060361-tarritos-potitos-papillas-y-otros-alimentos/2060363-tarritos-y-tarrinas-de-verduras/",
                             original_file_uri=os.path.join(category_path(), "Vegetable_baby_meals.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "Vegetable_baby_meals_detailed.json"))
    
    

    
 
    aisles: Final[List[StaticAisle]] = [BISCUITS_AND_SNACKS, MENUS, ORGANIC_BABY_CEREAL, POWDERED_BABY_CEREAL, LIQUID_BABY_CEREAL, MEAT_BABY_MEALS, FRUIT_BABY_MEALS, FISH_BABY_MEALS, VEGETABLE_BABY_MEALS]	

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "BISCUITS_AND_SNACKS":
                    aisles = [cls.BISCUITS_AND_SNACKS]
                case "MENUS":
                    aisles = [cls.MENUS]
                case "ORGANIC_BABY_CEREAL":
                    aisles = [cls.ORGANIC_BABY_CEREAL]
                case "POWDERED_BABY_CEREAL":
                    aisles = [cls.POWDERED_BABY_CEREAL]
                case "LIQUID_BABY_CEREAL":
                    aisles = [cls.LIQUID_BABY_CEREAL]
                case "MEAT_BABY_MEALS":
                    aisles = [cls.MEAT_BABY_MEALS]
                case "FRUIT_BABY_MEALS":
                    aisles = [cls.FRUIT_BABY_MEALS]
                case "FISH_BABY_MEALS":
                    aisles = [cls.FISH_BABY_MEALS]
                case "VEGETABLE_BABY_MEALS":
                    aisles = [cls.VEGETABLE_BABY_MEALS]
                
                
        return aisles

Eroski_categories_with_uris: Final[list[StaticCategory]] = [

    #FEEDING_CATEGORY:

    StaticCategory(name="Oil vinegar salt flour and breadcrumbs online", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059988-aceite-vinagre-sal-harina-y-pan-rallado/", aisles=EroskiFeedingOilVinegarSaltFlourAndBreadcrumbsAlimentations.aisles),
    
    StaticCategory(name="Olives and Pickles Online", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060067-aceitunas-y-encurtidos/", aisles=EroskiFeedingOlivesAndPicklesAlimentations.aisles),
    
    StaticCategory(name="Canned Fish Online", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060015-conservas-de-pescado/", aisles=EroskiFeedingCannedFishAlimentations.aisles),
    
    StaticCategory(name="Canned Vegetables Online", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060001-conservas-vegetales/", aisles=EroskiFeedingPreservedVegetablesAlimentations.aisles),
    
    StaticCategory(name="Nuts and Snacks Online", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060076-frutos-secos-patatas-y-snacks/", aisles=EroskiFeedingNutsAndSnacksAlimentations.aisles),
    
    StaticCategory(name="Milk and Beverages Online", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059807-leche-batidos-y-bebidas-vegetales/", aisles=EroskiFeedingMilkAndBeveragesAlimentations.aisles),
    
    StaticCategory(name="Legumes Rice and Pasta Online", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060029-legumbres-arroz-y-pasta/", aisles=EroskiFeedingLegumesRiceAndPastaAlimentations.aisles),
    
    StaticCategory(name="Butter and Cream Online", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059851-mantequilla-nata-y-cremas/", aisles=EroskiFeedingButterAndCreamAlimentations.aisles),
    
    StaticCategory(name="Online Ready Meals", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060042-platos-preparados/", aisles=EroskiFeedingReadyMealsAlimentations.aisles),
    
    StaticCategory(name="Dairy Desserts Online", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059831-postres-lacteos-/", aisles=EroskiFeedingDairyDessertsAlimentations.aisles),
    
    StaticCategory(name="Online Dietetics Products", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/5000365-productos-de-dietetica/", aisles=EroskiFeedingDieteticsProductsAlimentations.aisles),
    
    StaticCategory(name="Organic Products Online", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/5000364-productos-ecologicos/", aisles=EroskiFeedingOrganicProductsAlimentations.aisles),
    
    StaticCategory(name="Sauces and Spices Online", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2060056-salsas-y-especias/", aisles=EroskiFeedingSaucesAndSpicesAlimentations.aisles),
    
    StaticCategory(name="Yoghurts Online", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/2059818-yogures/", aisles=EroskiFeedingYoghurtsAlimentations.aisles),
    
    StaticCategory(name="International Food Online", url="https://supermercado.eroski.es/es/supermercado/2059806-alimentacion/4000017-comida-internacional/", aisles=EroskiFeedingInternationalFoodAlimentations.aisles),
    
    #FRESH_CATEGORY:

    StaticCategory(name="Online meats", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059746-carnes-y-aves/", aisles=EroskiFreshMeatAlimentations.aisles),
    
    StaticCategory(name="Cured meat and sausages online", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059880-curados-y-embutidos/", aisles=EroskiFreshCuredMeatAndSausagesAlimentations.aisles),
    
    StaticCategory(name="Cold cuts and stews online", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059872-fiambres-y-cocidos/", aisles=EroskiFreshColdCutsAndStewsAlimentations.aisles),
    
    StaticCategory(name="Fruit online", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059699-frutas/", aisles=EroskiFreshFruitAlimentations.aisles),
    
    StaticCategory(name="Eggs online", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059760-huevos/", aisles=EroskiFreshEggsAlimentations.aisles),
    
    StaticCategory(name="Iberian sausages online", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059894-ibericos/", aisles=EroskiFreshIberianSausagesAlimentations.aisles),
    
    StaticCategory(name="Seafood online", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059736-mariscos/", aisles=EroskiFreshSeafoodAlimentations.aisles),
    
    StaticCategory(name="Online bakery and pastry", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059783-panaderia-y-pasteleria/", aisles=EroskiFreshBakeryAndPastryAlimentations.aisles),
    
    StaticCategory(name="Fish online", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059722-pescados/", aisles=EroskiFreshFishAlimentations.aisles),
    
    StaticCategory(name="Online ready meals", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059769-platos-preparados/", aisles=EroskiFreshReadyMealsAlimentations.aisles),
    
    StaticCategory(name="Cheese and quince online", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059858-queso-y-membrillo/", aisles=EroskiFreshCheeseAndQuinceAlimentations.aisles),
    
    StaticCategory(name="Sausages pâté and foie gras online", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059901-salchichas-pates-y-foie/", aisles=EroskiFreshSausagesPâtéAndFoieGrasAlimentations.aisles),
    
    StaticCategory(name="Vegetables online", url="https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059710-verduras-y-hortalizas/", aisles=EroskiFreshVegetablesAlimentations.aisles),

    #SWEETS_CATEGORY:
    
    StaticCategory(name="Coffee", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060119-la-tienda-del-cafe/", aisles=EroskiSweetsCofeeAlimentations.aisles),
    
    StaticCategory(name="Online Sugar", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060182-azucar-y-edulcorante/", aisles=EroskiSweetsSugarAlimentations.aisles),
    
    StaticCategory(name="Pastries", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060162-bolleria/", aisles=EroskiSweetsPastriesAlimentations.aisles),
    
    StaticCategory(name="Cocoa online", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060129-cacao-en-polvo-y-crema-de-cacao/", aisles=EroskiSweetsCocoaAlimentations.aisles),
    
    StaticCategory(name="Candy gum and sweets online", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060202-caramelos-chicles-y-golosinas/", aisles=EroskiSweetsCandyAndSweetsAlimentations.aisles),
    
    StaticCategory(name="Cereals and bars online", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/5000189-cereales-y-barritas/", aisles=EroskiSweetsCerealAndBarsAlimentations.aisles),
    
    StaticCategory(name="Chocolates and chocolates online", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060190-chocolates-y-bombones/", aisles=EroskiSweetsChocolatesAlimentations.aisles),
    
    StaticCategory(name="Biscuits", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060135-galletas/", aisles=EroskiSweetsBiscuitsAlimentations.aisles),
    
    StaticCategory(name="Infusions and tea online", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/4000095-infusiones/", aisles=EroskiSweetsInfusionAlimentations.aisles),
    
    StaticCategory(name="Honey and jam online", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060173-miel-y-mermelada/", aisles=EroskiSweetsHoneyAndjamAlimentations.aisles),
    
    StaticCategory(name="Sliced and Toasted", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/2060149-pan-de-molde-y-tostado/", aisles=EroskiSweetsSlicedAndToastedBreadAlimentations.aisles),
    
    StaticCategory(name="Organic products online", url="https://supermercado.eroski.es/es/supermercado/2060118-dulces-y-desayuno/5000302-productos-ecologicos/", aisles=EroskiSweetsOrganicProductsAlimentations.aisles),

    #DRINKS_CATEGORY:
    
    StaticCategory(name="Water online", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060212-agua/", aisles=EroskiDrinkWaterAlimentation.aisles),
    
    StaticCategory(name="Cava cider and champagne online", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060304-cavachampan-y-sidra/", aisles=EroskiDrinkCavaChampagneAndCiderAlimentation.aisles),
    
    StaticCategory(name="Online beers", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060233-cervezas/", aisles=EroskiDrinkBeersAlimentation.aisles),
    
    StaticCategory(name="Drinks for online aperitif", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060294-finos-dulces-y-aperitivos/", aisles=EroskiDrinksAlimentation.aisles),
    
    StaticCategory(name="Online liquors", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060315-licor/", aisles=EroskiDrinkLiquorAlimentation.aisles),
    
    StaticCategory(name="Organic drinks online", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/5000308-productos-ecologicos/", aisles=EroskiDrinkOrganicProductsAlimentation.aisles),
    
    StaticCategory(name="Online refreshments", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060219-refrescos/", aisles=EroskiDrinkRefreshementsAlimentation.aisles),
    
    StaticCategory(name="White wines", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060266-vinos-blancos/", aisles=EroskiDrinkWhiteWinesAlimentation.aisles),
    
    StaticCategory(name="Table wines and sangrias online", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060289-vinos-de-mesa-y-sangrias/", aisles=EroskiDrinkTableWinesAlimentation.aisles),
    
    StaticCategory(name="Rosé wine online", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060278-vinos-rosados/", aisles=EroskiDrinkPinkWinesAlimentation.aisles),
    
    StaticCategory(name="Red wine online", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060252-vinos-tintos/", aisles=EroskiDrinkRedWinesAlimentation.aisles),
    
    StaticCategory(name="Juices and nectar online", url="https://supermercado.eroski.es/es/supermercado/2060211-bebidas/2060243-zumos-y-nectar/", aisles=EroskiDrinkJuiceAndNectarAlimentation.aisles),

    #FROZEN_CATEGORY:
    
    StaticCategory(name="Ice cream and desserts", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059952-helados-y-postres/", aisles=EroskiFrozenIceCreamAndDessertsAlimentation.aisles),
    
    StaticCategory(name="Frozen bread and dough", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059983-panaderia-y-pasteleria/", aisles=EroskiFrozenBakeryAndPastryAlimentation.aisles),
    
    StaticCategory(name="Frozen vegetables", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059942-patatas-verduras-y-setas/", aisles=EroskiFrozenVegetableAlimentation.aisles),
    
    StaticCategory(name="Frozen fish", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059927-pescado/", aisles=EroskiFrozenFishAlimentation.aisles),
    
    StaticCategory(name="Frozen pizzas", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059920-pizzas/", aisles=EroskiFrozenPizzasAlimentation.aisles),
    
    StaticCategory(name="Frozen ready meals", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059964-platos-preparados/", aisles=EroskiFrozenReadyMealsAlimentation.aisles),
    
    StaticCategory(name="Frozen seafood", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059934-marisco/", aisles=EroskiFrozenSeafoodAlimentation.aisles),
    
    StaticCategory(name="Frozen stirfries and scrambles", url="https://supermercado.eroski.es/es/supermercado/2059919-congelados/2059977-salteados-y-revueltos/", aisles=EroskiFrozenstirFriesAndScramblesAlimentation.aisles),
    
    #BEBE_CATEGORY:

    StaticCategory(name="Baby milk", url="https://supermercado.eroski.es/es/supermercado/2060327-bebe/2060352-leche-y-aguas/", aisles=EroskiBabyMilkAlimentation.aisles),

    StaticCategory(name="Baby dessert and afternoon tea", url="https://supermercado.eroski.es/es/supermercado/2060327-bebe/2060383-postres-y-meriendas/", aisles=EroskiBabyDesertAndAfternoonTeaAlimentation.aisles),

    StaticCategory(name="Baby organic products", url="https://supermercado.eroski.es/es/supermercado/2060327-bebe/5000310-productos-ecologicos/", aisles=EroskiBabyOrganicProductsAlimentation.aisles),
    
    StaticCategory(name="Baby meals", url="https://supermercado.eroski.es/es/supermercado/2060327-bebe/2060361-tarritos-potitos-papillas-y-otros-alimentos/", aisles=EroskiBabymealsAlimentation.aisles),
]

# /Users/marwenrhayem/Projects/mrh/LaNoria_backoffice/.venv/bin/python3 /Users/marwenrhayem/Projects/mrh/LaNoria_backoffice/src/robots/france/auchan/Auchan.py src/robots/france/carrefour/products/cremerie/cremerie_yaourts_fromages_blancs_detailed_24_02_14_11.59.json


def get_static_aisles_from_user_cmdargs(cmdargs: list[str]) -> list[StaticAisle]:
    '''
    first argument can be either: category name or aisle name or file path
    '''
    if not isinstance(cmdargs, list):
        return []
    aisles: list[StaticAisle] = []
    if len(cmdargs) == 1:
        logging.warning(f"Parse ALL categories at once will take a lot of time!! parse them one by one!")
        print("\033[91mThis is red text\033[0m")
        sys.exit()
        for category in Eroski_categories_with_uris:
            print(f"""category.name: {category.name}, 
                  aisles length: {len(category.aisles)}""")
            aisles += category.aisles

    elif len(cmdargs) >= 2:
        print(f"going to parse: {cmdargs[1]}")
        if os.path.isdir(cmdargs[1]):
            logging.error(f"args should be a file or aisle not a folder, args:{cmdargs[1]}")
            sys.exit()
        elif os.path.isfile(cmdargs[1]):
            res = get_filename_from_filepath(cmdargs[1])
            print(f"file name to parse: {res}")
            sys.exit()
            aisle = StaticAisle(name=str(res), url=None,
                                original_file_uri=cmdargs[1], created_from_file=True)
            aisles.append(aisle)
            print(f"aisles to parse: {aisles}")

        else:
            split_list = cmdargs[1].split(".")
            category = split_list[0] if len(split_list) > 1 else cmdargs[1]
            match category:
                case "EroskiFeedingOilVinegarSaltFlourAndBreadcrumbsAlimentations":
                    aisles = EroskiFeedingOilVinegarSaltFlourAndBreadcrumbsAlimentations.get_aisles(cmdargs[1])
                case "EroskiFeedingOlivesAndPicklesAlimentations":
                    aisles = EroskiFeedingOlivesAndPicklesAlimentations.get_aisles(cmdargs[1])
                case "EroskiFeedingCannedFishAlimentations":
                    aisles = EroskiFeedingCannedFishAlimentations.get_aisles(cmdargs[1])
                case "EroskiFeedingPreservedVegetablesAlimentations":
                    aisles = EroskiFeedingPreservedVegetablesAlimentations.get_aisles(cmdargs[1])
                case "EroskiFeedingNutsAndSnacksAlimentations":
                    aisles = EroskiFeedingNutsAndSnacksAlimentations.get_aisles(cmdargs[1])
                case "EroskiFeedingMilkAndBeveragesAlimentations":
                    aisles = EroskiFeedingMilkAndBeveragesAlimentations.get_aisles(cmdargs[1])
                case "EroskiFeedingLegumesRiceAndPastaAlimentations":
                    aisles = EroskiFeedingLegumesRiceAndPastaAlimentations.get_aisles(cmdargs[1])
                case "EroskiFeedingButterAndCreamAlimentations":
                    aisles = EroskiFeedingButterAndCreamAlimentations.get_aisles(cmdargs[1])
                case "EroskiFeedingReadyMealsAlimentations":
                    aisles = EroskiFeedingReadyMealsAlimentations.get_aisles(cmdargs[1])
                case "EroskiFeedingDairyDessertsAlimentations":
                    aisles = EroskiFeedingDairyDessertsAlimentations.get_aisles(cmdargs[1])
                case "EroskiFeedingDieteticsProductsAlimentations":
                    aisles = EroskiFeedingDieteticsProductsAlimentations.get_aisles(cmdargs[1])
                case "EroskiFeedingOrganicProductsAlimentations":
                    aisles = EroskiFeedingOrganicProductsAlimentations.get_aisles(cmdargs[1])
                case "EroskiFeedingSaucesAndSpicesAlimentations":
                    aisles = EroskiFeedingSaucesAndSpicesAlimentations.get_aisles(cmdargs[1])
                case "EroskiFeedingYoghurtsAlimentations":
                    aisles = EroskiFeedingYoghurtsAlimentations.get_aisles(cmdargs[1])
                case "EroskiFeedingInternationalFoodAlimentations":
                    aisles = EroskiFeedingInternationalFoodAlimentations.get_aisles(cmdargs[1])
                case "EroskiFreshMeatAlimentations":
                    aisles = EroskiFreshMeatAlimentations.get_aisles(cmdargs[1])
                case "EroskiFreshCuredMeatAndSausagesAlimentations":
                    aisles = EroskiFreshCuredMeatAndSausagesAlimentations.get_aisles(cmdargs[1])
                case "EroskiFreshColdCutsAndStewsAlimentations":
                    aisles = EroskiFreshColdCutsAndStewsAlimentations.get_aisles(cmdargs[1])
                case "EroskiFreshFruitAlimentations":
                    aisles = EroskiFreshFruitAlimentations.get_aisles(cmdargs[1])
                case "EroskiFreshEggsAlimentations":
                    aisles = EroskiFreshEggsAlimentations.get_aisles(cmdargs[1])
                case "EroskiFreshIberianSausagesAlimentations":
                    aisles = EroskiFreshIberianSausagesAlimentations.get_aisles(cmdargs[1])
                case "EroskiFreshSeafoodAlimentations":
                    aisles = EroskiFreshSeafoodAlimentations.get_aisles(cmdargs[1])
                case "EroskiFreshBakeryAndPastryAlimentations":
                    aisles = EroskiFreshBakeryAndPastryAlimentations.get_aisles(cmdargs[1])
                case "EroskiFreshFishAlimentations":
                    aisles = EroskiFreshFishAlimentations.get_aisles(cmdargs[1])
                case "EroskiFreshReadyMealsAlimentations":
                    aisles = EroskiFreshReadyMealsAlimentations.get_aisles(cmdargs[1])
                case "EroskiFreshCheeseAndQuinceAlimentations":
                    aisles = EroskiFreshCheeseAndQuinceAlimentations.get_aisles(cmdargs[1])
                case "EroskiFreshSausagesPâtéAndFoieGrasAlimentations":
                    aisles = EroskiFreshSausagesPâtéAndFoieGrasAlimentations.get_aisles(cmdargs[1])
                case "EroskiFreshVegetablesAlimentations":
                    aisles = EroskiFreshVegetablesAlimentations.get_aisles(cmdargs[1])
                case "EroskiSweetsCofeeAlimentations":
                    aisles = EroskiSweetsCofeeAlimentations.get_aisles(cmdargs[1])
                case "EroskiSweetsSugarAlimentations":
                    aisles = EroskiSweetsSugarAlimentations.get_aisles(cmdargs[1])
                case "EroskiSweetsPastriesAlimentations":
                    aisles = EroskiSweetsPastriesAlimentations.get_aisles(cmdargs[1])
                case "EroskiSweetsCocoaAlimentations":
                    aisles = EroskiSweetsCocoaAlimentations.get_aisles(cmdargs[1])
                case "EroskiSweetsCandyAndSweetsAlimentations":
                    aisles = EroskiSweetsCandyAndSweetsAlimentations.get_aisles(cmdargs[1])
                case "EroskiSweetsCerealAndBarsAlimentations":
                    aisles = EroskiSweetsCerealAndBarsAlimentations.get_aisles(cmdargs[1])
                case "EroskiSweetsChocolatesAlimentations":
                    aisles = EroskiSweetsChocolatesAlimentations.get_aisles(cmdargs[1])
                case "EroskiSweetsBiscuitsAlimentations":
                    aisles = EroskiSweetsBiscuitsAlimentations.get_aisles(cmdargs[1])
                case "EroskiSweetsInfusionAlimentations":
                    aisles = EroskiSweetsInfusionAlimentations.get_aisles(cmdargs[1])
                case "EroskiSweetsHoneyAndjamAlimentations":
                    aisles = EroskiSweetsHoneyAndjamAlimentations.get_aisles(cmdargs[1])
                case "EroskiSweetsSlicedAndToastedBreadAlimentations":
                    aisles = EroskiSweetsSlicedAndToastedBreadAlimentations.get_aisles(cmdargs[1])
                case "EroskiSweetsOrganicProductsAlimentations":
                    aisles = EroskiSweetsOrganicProductsAlimentations.get_aisles(cmdargs[1])
                case "EroskiDrinkWaterAlimentation":
                    aisles = EroskiDrinkWaterAlimentation.get_aisles(cmdargs[1])
                case "EroskiDrinkCavaChampagneAndCiderAlimentation":
                    aisles = EroskiDrinkCavaChampagneAndCiderAlimentation.get_aisles(cmdargs[1])
                case "EroskiDrinkBeersAlimentation":
                    aisles = EroskiDrinkBeersAlimentation.get_aisles(cmdargs[1])
                case "EroskiDrinksAlimentation":
                    aisles = EroskiDrinksAlimentation.get_aisles(cmdargs[1])
                case "EroskiDrinkLiquorAlimentation":
                    aisles = EroskiDrinkLiquorAlimentation.get_aisles(cmdargs[1])
                case "EroskiDrinkOrganicProductsAlimentation":
                    aisles = EroskiDrinkOrganicProductsAlimentation.get_aisles(cmdargs[1])
                case "EroskiDrinkRefreshementsAlimentation":
                    aisles = EroskiDrinkRefreshementsAlimentation.get_aisles(cmdargs[1])
                case "EroskiDrinkWhiteWinesAlimentation":
                    aisles = EroskiDrinkWhiteWinesAlimentation.get_aisles(cmdargs[1])
                case "EroskiDrinkTableWinesAlimentation":
                    aisles = EroskiDrinkTableWinesAlimentation.get_aisles(cmdargs[1])
                case "EroskiDrinkPinkWinesAlimentation":
                    aisles = EroskiDrinkPinkWinesAlimentation.get_aisles(cmdargs[1])
                case "EroskiDrinkRedWinesAlimentation":
                    aisles = EroskiDrinkRedWinesAlimentation.get_aisles(cmdargs[1])
                case "EroskiDrinkJuiceAndNectarAlimentation":
                    aisles = EroskiDrinkJuiceAndNectarAlimentation.get_aisles(cmdargs[1])
                case "EroskiFrozenIceCreamAndDessertsAlimentation":
                    aisles = EroskiFrozenIceCreamAndDessertsAlimentation.get_aisles(cmdargs[1])
                case "EroskiFrozenBakeryAndPastryAlimentation":
                    aisles = EroskiFrozenBakeryAndPastryAlimentation.get_aisles(cmdargs[1])
                case "EroskiFrozenVegetableAlimentation":
                    aisles = EroskiFrozenVegetableAlimentation.get_aisles(cmdargs[1])
                case "EroskiFrozenFishAlimentation":
                    aisles = EroskiFrozenFishAlimentation.get_aisles(cmdargs[1])
                case "EroskiFrozenPizzasAlimentation":
                    aisles = EroskiFrozenPizzasAlimentation.get_aisles(cmdargs[1])
                case "EroskiFrozenReadyMealsAlimentation":
                    aisles = EroskiFrozenReadyMealsAlimentation.get_aisles(cmdargs[1])
                case "EroskiFrozenSeafoodAlimentation":
                    aisles = EroskiFrozenSeafoodAlimentation.get_aisles(cmdargs[1])
                case "EroskiFrozenstirFriesAndScramblesAlimentation":
                    aisles = EroskiFrozenstirFriesAndScramblesAlimentation.get_aisles(cmdargs[1])
                case "EroskiBabyMilkAlimentation":
                    aisles = EroskiBabyMilkAlimentation.get_aisles(cmdargs[1])
                case "EroskiBabyDesertAndAfternoonTeaAlimentation":
                    aisles = EroskiBabyDesertAndAfternoonTeaAlimentation.get_aisles(cmdargs[1])
                case "EroskiBabyOrganicProductsAlimentation":
                    aisles = EroskiBabyOrganicProductsAlimentation.get_aisles(cmdargs[1])
                case "EroskiBabymealsAlimentation":
                    aisles = EroskiBabymealsAlimentation.get_aisles(cmdargs[1])
                case _:
                    logging.error(f"args source not found: {cmdargs[1]}")
                    sys.exit()

    return aisles
