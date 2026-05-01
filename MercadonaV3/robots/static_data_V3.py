import logging
import os
import sys
sys.path.append('src')
from typing import Final, List, Optional, Union

from typing_extensions import override

from src.model.static_category_aisle import StaticAisle, StaticCategory
from src.utils.my_utils import get_filename_from_filepath

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

class MercadonaOilsSpicesAndSaucesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Oils_Spices_And_Sauces")

    OIL_VINEGAR_AND_SALT = StaticAisle(name="oil, vinegar & salt", url="https://tienda.mercadona.es/categories/112",
                                     original_file_uri=os.path.join(category_path(), "OilVinegar_and_salt.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "OilVinegar_and_salt_detailed.json"))
    
    SPICES = StaticAisle(name="Spices", url="https://tienda.mercadona.es/categories/115",
                                     original_file_uri=os.path.join(category_path(), "Spices.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Spices_detailed.json"))
    
    MAYONAISE_KETCHUP_AND_MUSTARD = StaticAisle(name="Mayonaise, ketchup & mustard", url="https://tienda.mercadona.es/categories/116",
                                     original_file_uri=os.path.join(category_path(), "Mayonaise_ketchup_and_mustard.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mayonaise_ketchup_and_mustard_detailed.json"))
    
    OTHER_SAUCES = StaticAisle(name="Other sauces", url="https://tienda.mercadona.es/categories/117",
                                     original_file_uri=os.path.join(category_path(), "Other_sauces.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_sauces_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [OIL_VINEGAR_AND_SALT, SPICES, MAYONAISE_KETCHUP_AND_MUSTARD, OTHER_SAUCES]

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
                case "OIL_VINEGAR_AND_SALT":
                    aisles = [cls.OIL_VINEGAR_AND_SALT]
                case "SPICES":
                    aisles = [cls.SPICES]
                case "MAYONAISE_KETCHUP_AND_MUSTARD":
                    aisles = [cls.MAYONAISE_KETCHUP_AND_MUSTARD]
                case "OTHER_SAUCES":
                    aisles = [cls.OTHER_SAUCES]
                
        return aisles
    
class MercadonaWaterAndSoftDrinksAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Water_And_SoftDrinks")

    WATER = StaticAisle(name="Water", url="https://tienda.mercadona.es/categories/156",
                                     original_file_uri=os.path.join(category_path(), "Water.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Water_detailed.json"))
    
    ISTONIC_ENERGY_DRINKS = StaticAisle(name="Istonic & energy drinks", url="https://tienda.mercadona.es/categories/163",
                                     original_file_uri=os.path.join(category_path(), "Istonic_energy_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Istonic_energy_drinks_detailed.json"))
    
    COLA_DRINKS = StaticAisle(name="Cola drinks", url="https://tienda.mercadona.es/categories/158",
                                     original_file_uri=os.path.join(category_path(), "Cola_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cola_drinks_detailed.json"))
    
    ORANGE_AND_LEMON_SOFT_DRINKS = StaticAisle(name="Orange & leamon soft drinks", url="https://tienda.mercadona.es/categories/159",
                                     original_file_uri=os.path.join(category_path(), "Orange_and_lemon_soft_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Orange_and_lemon_soft_drinks_detailed.json"))
    
    TONIC_AND_BITTER = StaticAisle(name="Tonic & bitter", url="https://tienda.mercadona.es/categories/161",
                                     original_file_uri=os.path.join(category_path(), "Tonic_and_bitter.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tonic_and_bitter_detailed.json"))
    
    STILL_AND_TEA_SOFTDRINKS = StaticAisle(name="StillAndTeaSoftDrinks", url="https://tienda.mercadona.es/categories/162",
                                     original_file_uri=os.path.join(category_path(), "Still_and_tea_soft_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Still_and_tea_soft_drinks_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [WATER, ISTONIC_ENERGY_DRINKS, COLA_DRINKS, ORANGE_AND_LEMON_SOFT_DRINKS, TONIC_AND_BITTER, STILL_AND_TEA_SOFTDRINKS]

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
                case "WATER":
                    aisles = [cls.WATER]
                case "ISTONIC_ENERGY_DRINKS":
                    aisles = [cls.ISTONIC_ENERGY_DRINKS]
                case "COLA_DRINKS":
                    aisles = [cls.COLA_DRINKS]
                case "ORANGE_AND_LEMON_SOFT_DRINKS":
                    aisles = [cls.ORANGE_AND_LEMON_SOFT_DRINKS]
                case "TONIC_AND_BITTER":
                    aisles = [cls.TONIC_AND_BITTER]
                case "STILL_AND_TEA_SOFTDRINKS":
                    aisles = [cls.STILL_AND_TEA_SOFTDRINKS]
                
        return aisles
    
class MercadonaSnacksAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Snacks")

    OLIVES_PICKLES = StaticAisle(name="Olives & pickles", url="https://tienda.mercadona.es/categories/135",
                                     original_file_uri=os.path.join(category_path(), "Olives_pickles.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Olives_pickles_detailed.json"))
    
    NUTS_SEEDS_AND_DRIED_FRUIT = StaticAisle(name="Nuts, seeds & dried fruit", url="https://tienda.mercadona.es/categories/133",
                                     original_file_uri=os.path.join(category_path(), "Nuts_seeds_and_dried_fruit.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Nuts_seeds_and_dried_fruit_detailed.json"))
    
    POTATO_CRISP_AND_SNACKS = StaticAisle(name="Potato crisp & snacks", url="https://tienda.mercadona.es/categories/132",
                                     original_file_uri=os.path.join(category_path(), "Potato_crisp_and_snacks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Potato_crisp_and_snacks_detailed.json"))
    
   
    aisles: Final[List[StaticAisle]] = [OLIVES_PICKLES, NUTS_SEEDS_AND_DRIED_FRUIT, POTATO_CRISP_AND_SNACKS]

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
                case "OLIVES_PICKLES":
                    aisles = [cls.OLIVES_PICKLES]
                case "NUTS_SEEDS_AND_DRIED_FRUIT":
                    aisles = [cls.NUTS_SEEDS_AND_DRIED_FRUIT]
                case "POTATO_CRISP_AND_SNACKS":
                    aisles = [cls.POTATO_CRISP_AND_SNACKS]
                           
        return aisles

class MercadonaRicePulsesPastaAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Rice_Pulses_Pasta")

    RICE = StaticAisle(name="Rice", url="https://tienda.mercadona.es/categories/118",
                                     original_file_uri=os.path.join(category_path(), "Rice.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Rice_detailed.json"))
    
    PULSES = StaticAisle(name="Pulses", url="https://tienda.mercadona.es/categories/121",
                                     original_file_uri=os.path.join(category_path(), "Pulses.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pulses_detailed.json"))
    
    PASTA_AND_NOODLES = StaticAisle(name="Pasta & noodles", url="https://tienda.mercadona.es/categories/120",
                                     original_file_uri=os.path.join(category_path(), "Pasta_and_noodles.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pasta_and_noodles_detailed.json"))
    
   
    aisles: Final[List[StaticAisle]] = [RICE, PULSES, PASTA_AND_NOODLES]

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
                case "PULSES":
                    aisles = [cls.PULSES]
                case "PASTA_AND_NOODLES":
                    aisles = [cls.PASTA_AND_NOODLES]
                           
        return aisles
    
class MercadonaSugarSweetsChocolateAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Sugar_Sweets_Chocolate")

    SUGAR_AND_SWEETENERS = StaticAisle(name="Sugar & sweeteners", url="https://tienda.mercadona.es/categories/89",
                                     original_file_uri=os.path.join(category_path(), "Sugar_and_sweteners.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sugar_and_sweteners_detailed.json"))
    
    CHEWING_GUM_AND_CANDY = StaticAisle(name="Chewing gum & candy", url="https://tienda.mercadona.es/categories/95",
                                     original_file_uri=os.path.join(category_path(), "Chewing_gum_and_candy.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chewing_gum_and_candy_detailed.json"))
    
    CHOCOLATE = StaticAisle(name="Chocolate", url="https://tienda.mercadona.es/categories/92",
                                     original_file_uri=os.path.join(category_path(), "Chocolate.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chocolate_detailed.json"))
    
    SWEETS = StaticAisle(name="Sweets", url="https://tienda.mercadona.es/categories/97",
                                     original_file_uri=os.path.join(category_path(), "Sweets.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sweets_detailed.json"))
    
    MARMALADE_AND_HONEY = StaticAisle(name="Marmalade & honey", url="https://tienda.mercadona.es/categories/90",
                                     original_file_uri=os.path.join(category_path(), "Marmalade_and_honey.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Marmalade_and_honey_detailed.json"))
    
   
    
    aisles: Final[List[StaticAisle]] = [SUGAR_AND_SWEETENERS, CHEWING_GUM_AND_CANDY, CHOCOLATE, SWEETS, MARMALADE_AND_HONEY]

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
                case "SUGAR_AND_SWEETENERS":
                    aisles = [cls.SUGAR_AND_SWEETENERS]
                case "CHEWING_GUM_AND_CANDY":
                    aisles = [cls.CHEWING_GUM_AND_CANDY]
                case "CHOCOLATE":
                    aisles = [cls.CHOCOLATE]
                case "SWEETS":
                    aisles = [cls.SWEETS]
                case "MARMALADE_AND_HONEY":
                    aisles = [cls.MARMALADE_AND_HONEY]
                           
        return aisles
    
class MercadonaBabyAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Baby")

    BABY_FOOD = StaticAisle(name="Baby food", url="https://tienda.mercadona.es/categories/216",
                                     original_file_uri=os.path.join(category_path(), "Baby_food.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Baby_food_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [BABY_FOOD]

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
                case "BABY_FOOD":
                    aisles = [cls.BABY_FOOD]
                
        return aisles
    
class MercadonaBeerWineSpiritsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Beer_Wine_Spirits")

    BEER = StaticAisle(name="Beer", url="https://tienda.mercadona.es/categories/164",
                                     original_file_uri=os.path.join(category_path(), "Beer.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Beer_detailed.json"))
    
    ALCOHOL_FREE_BEER = StaticAisle(name="Alcohol-free beer", url="https://tienda.mercadona.es/categories/166",
                                     original_file_uri=os.path.join(category_path(), "Alcohol-free_beer.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Alcohol-free_beer_detailed.json"))
    
    SPIRITS = StaticAisle(name="Spirits", url="https://tienda.mercadona.es/categories/181",
                                     original_file_uri=os.path.join(category_path(), "Spirits.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Spirits_detailed.json"))
    
    CIDER_AND_CAVA = StaticAisle(name="Cider & cava", url="https://tienda.mercadona.es/categories/174",
                                     original_file_uri=os.path.join(category_path(), "Cider_and_cava.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cider_and_cava_detailed.json"))
    
    TINTO_DE_VERANO_AND_SANGRIA = StaticAisle(name="Tinto de verano & sangria", url="https://tienda.mercadona.es/categories/168",
                                     original_file_uri=os.path.join(category_path(), "Tinto_de_verano_and_sangria.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tinto_de_verano_and_sangria_detailed.json"))
    
    WHITE_WINE = StaticAisle(name="White wine", url="https://tienda.mercadona.es/categories/170",
                                     original_file_uri=os.path.join(category_path(), "White_Wine.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "White_Wine_detailed.json"))
    
    LAMBRUSCO_AND_SPARKLING_WINE = StaticAisle(name="Lambrusco & sparkling wine", url="https://tienda.mercadona.es/categories/173",
                                     original_file_uri=os.path.join(category_path(), "Lambrusco_and_sparkling_wine.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Lambrusco_and_sparkling_wine_detailed.json"))
    
    ROSE_WINE = StaticAisle(name="Rose wine", url="https://tienda.mercadona.es/categories/171",
                                     original_file_uri=os.path.join(category_path(), "Rose_Wine.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Rose_Wine_detailed.json"))
    
    RED_WINE = StaticAisle(name="Red wine", url="https://tienda.mercadona.es/categories/169",
                                     original_file_uri=os.path.join(category_path(), "Red_Wine.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Red_Wine_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [BEER, ALCOHOL_FREE_BEER, SPIRITS, CIDER_AND_CAVA, TINTO_DE_VERANO_AND_SANGRIA, WHITE_WINE, LAMBRUSCO_AND_SPARKLING_WINE, ROSE_WINE, RED_WINE]

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
                case "BEER":
                    aisles = [cls.BEER]
                case "ALCOHOL_FREE_BEER":
                    aisles = [cls.ALCOHOL_FREE_BEER]
                case "SPIRITS":
                    aisles = [cls.SPIRITS]
                case "CIDER_AND_CAVA":
                    aisles = [cls.CIDER_AND_CAVA]
                case "TINTO_DE_VERANO_AND_SANGRIA":
                    aisles = [cls.TINTO_DE_VERANO_AND_SANGRIA]
                case "WHITE_WINE":
                    aisles = [cls.WHITE_WINE]
                case "LAMBRUSCO_AND_SPARKLING_WINE":
                    aisles = [cls.LAMBRUSCO_AND_SPARKLING_WINE]
                case "ROSE_WINE":
                    aisles = [cls.ROSE_WINE]
                case "RED_WINE":
                    aisles = [cls.RED_WINE]
                   
        return aisles
    
class MercadonaChocolateDrinksHotChocolateAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Chocolate_Drinks_HotChocolate")

    CHOCOLATE_DRINKS_AND_HOT_CHOCOLATE = StaticAisle(name="Chocolate drinks & hot chocolate", url="https://tienda.mercadona.es/categories/86",
                                     original_file_uri=os.path.join(category_path(), "Chocolate_drinks_and_hot_chocolate.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chocolate_drinks_and_hot_chocolate_detailed.json"))
    
    COFFEE_PODS_AND_SINGLE_CUPS = StaticAisle(name="Coffee pods & single cups", url="https://tienda.mercadona.es/categories/81",
                                     original_file_uri=os.path.join(category_path(), "Coffee_pods_and_single_cups.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Coffee_pods_and_single_cups_detailed.json"))
    
    GROUND_COFFEE_AND_COFFEE_BEANS = StaticAisle(name="Ground coffee & coffee beans", url="https://tienda.mercadona.es/categories/83",
                                     original_file_uri=os.path.join(category_path(), "ground_coffee_and_coffee_beans.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "ground_coffee_and_coffee_beans_detailed.json"))
    
    SOLUBLE_COFFEE_AND_OTHER_DRINKS = StaticAisle(name="Soluble coffee & other drinks", url="https://tienda.mercadona.es/categories/84",
                                     original_file_uri=os.path.join(category_path(), "soluble_coffee_and_other_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "soluble_coffee_and_other_drinks_detailed.json"))
    
    TEA_AND_INFUSIONS = StaticAisle(name="Tea & infusions", url="https://tienda.mercadona.es/categories/88",
                                     original_file_uri=os.path.join(category_path(), "Tea_and_infusions.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tea_and_infusions_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [CHOCOLATE_DRINKS_AND_HOT_CHOCOLATE, COFFEE_PODS_AND_SINGLE_CUPS, GROUND_COFFEE_AND_COFFEE_BEANS, SOLUBLE_COFFEE_AND_OTHER_DRINKS, TEA_AND_INFUSIONS]

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
                case "CHOCOLATE_DRINKS_AND_HOT_CHOCOLATE":
                    aisles = [cls.CHOCOLATE_DRINKS_AND_HOT_CHOCOLATE]
                case "COFFEE_PODS_AND_SINGLE_CUPS":
                    aisles = [cls.COFFEE_PODS_AND_SINGLE_CUPS]
                case "GROUND_COFFEE_AND_COFFEE_BEANS":
                    aisles = [cls.GROUND_COFFEE_AND_COFFEE_BEANS]
                case "SOLUBLE_COFFEE_AND_OTHER_DRINKS":
                    aisles = [cls.SOLUBLE_COFFEE_AND_OTHER_DRINKS]
                case "TEA_AND_INFUSIONS":
                    aisles = [cls.TEA_AND_INFUSIONS]


        return aisles
    
class MercadonaMeatAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Meat")

    MEAT_BOXES = StaticAisle(name="Meat boxes", url="https://tienda.mercadona.es/categories/46",
                                     original_file_uri=os.path.join(category_path(), "Meat_boxes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Meat_boxes_detailed.json"))
    
    POULTRY = StaticAisle(name="Poultry", url="https://tienda.mercadona.es/categories/38",
                                     original_file_uri=os.path.join(category_path(), "Poultry.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Poultry_detailed.json"))
    
    FROZEN_MEAT = StaticAisle(name="Frozen meat", url="https://tienda.mercadona.es/categories/47",
                                     original_file_uri=os.path.join(category_path(), "Frozen_meat.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Frozen_meat_detailed.json"))
    
    PORK = StaticAisle(name="Pork", url="https://tienda.mercadona.es/categories/37",
                                     original_file_uri=os.path.join(category_path(), "Pork.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pork_detailed.json"))
    
    RABBIT_AND_LAMB = StaticAisle(name="Rabbit & lamb", url="https://tienda.mercadona.es/categories/42",
                                     original_file_uri=os.path.join(category_path(), "Rabbit_lamb.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Rabbit_lamb_detailed.json"))
    
    SAUSAGES = StaticAisle(name="Sausages", url="https://tienda.mercadona.es/categories/43",
                                     original_file_uri=os.path.join(category_path(), "Sausages.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sausages_detailed.json"))
    
    BURGERS_AND_MINCED_FOOD = StaticAisle(name="Burgers and minced food", url="https://tienda.mercadona.es/categories/44",
                                     original_file_uri=os.path.join(category_path(), "Burgers_and_minced_food.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Burgers_and_minced_food_detailed.json"))
    
    BEEF = StaticAisle(name="Beef", url="https://tienda.mercadona.es/categories/40",
                                     original_file_uri=os.path.join(category_path(), "Beef.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Beef_detailed.json"))
    
    BREADED_AND_PREPARED_MEATS = StaticAisle(name="Breaded & prepared meats", url="https://tienda.mercadona.es/categories/45",
                                     original_file_uri=os.path.join(category_path(), "Breaded_and_prepared_meats.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Breaded_and_prepared_meats_detailed.json"))
    
    
    
    aisles: Final[List[StaticAisle]] = [MEAT_BOXES, POULTRY, FROZEN_MEAT, PORK, RABBIT_AND_LAMB, SAUSAGES, BURGERS_AND_MINCED_FOOD, BEEF, BREADED_AND_PREPARED_MEATS]

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
                case "MEAT_BOXES":
                    aisles = [cls.MEAT_BOXES]
                case "POULTRY":
                    aisles = [cls.POULTRY]
                case "FROZEN_MEAT":
                    aisles = [cls.FROZEN_MEAT]
                case "PORK":
                    aisles = [cls.PORK]
                case "RABBIT_AND_LAMB":
                    aisles = [cls.RABBIT_AND_LAMB]
                case "SAUSAGES":
                    aisles = [cls.SAUSAGES]
                case "BURGERS_AND_MINCED_FOOD":
                    aisles = [cls.BURGERS_AND_MINCED_FOOD]
                case "BEEF":
                    aisles = [cls.BEEF]
                case "BREADED_AND_PREPARED_MEATS":
                    aisles = [cls.BREADED_AND_PREPARED_MEATS]
                

        return aisles
    
class MercadonaCerealAndBiscuitsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Cereal_And_Biscuits")

    CEREAL = StaticAisle(name="Cereal", url="https://tienda.mercadona.es/categories/78",
                                     original_file_uri=os.path.join(category_path(), "Cereal.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cereal_detailed.json"))
    
    BISCUITS = StaticAisle(name="Biscuits", url="https://tienda.mercadona.es/categories/80",
                                     original_file_uri=os.path.join(category_path(), "Biscuits.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Biscuits_detailed.json"))
    
    CAKES = StaticAisle(name="Cakes", url="https://tienda.mercadona.es/categories/79",
                                     original_file_uri=os.path.join(category_path(), "Cakes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cakes_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [CEREAL, BISCUITS, CAKES]

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
                case "CEREAL":
                    aisles = [cls.CEREAL]
                case "BISCUITS":
                    aisles = [cls.BISCUITS]
                case "CAKES":
                    aisles = [cls.CAKES]
                
        return aisles
    
class MercadonaDeliAndCheeseAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Deli_And_Cheese")

    COOKED_POULTRY_AND_HAM = StaticAisle(name="Cooked poultry & ham", url="https://tienda.mercadona.es/categories/48",
                                     original_file_uri=os.path.join(category_path(), "Cooked_poultry_and_ham.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cooked_poultry_and_ham_detailed.json"))
    
    BACON_AND_SAUSAGES = StaticAisle(name="Bacon & sausages", url="https://tienda.mercadona.es/categories/52",
                                     original_file_uri=os.path.join(category_path(), "Bacon_sausages.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Bacon_sausages_detailed.json"))
    
    CHOPPED_PORK_AND_MORTADELLA = StaticAisle(name="Chopped pork & mortadella", url="https://tienda.mercadona.es/categories/49",
                                     original_file_uri=os.path.join(category_path(), "Chopped_pork_and_mortadella.json"),                            
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chopped_pork_and_mortadella_detailed.json"))
    
    CURED_MEAT = StaticAisle(name="Cured meat", url="https://tienda.mercadona.es/categories/51",
                                     original_file_uri=os.path.join(category_path(), "Cured_meat.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cured_meat_detailed.json"))
    
    SERRANO_HAM = StaticAisle(name="Serrano ham", url="https://tienda.mercadona.es/categories/50",
                                     original_file_uri=os.path.join(category_path(), "Serrano_ham.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Serrano_ham_detailed.json"))
    
    PATE_AND_SOBRASADA = StaticAisle(name="Pate & sobrasada", url="https://tienda.mercadona.es/categories/58",
                                     original_file_uri=os.path.join(category_path(), "Pate_and_sobrasada.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pate_and_sobrasada_detailed.json"))
    
    CURED_SEMICURED_AND_SOFT_CHEESE = StaticAisle(name="Cured, semicured & soft cheese", url="https://tienda.mercadona.es/categories/54",
                                     original_file_uri=os.path.join(category_path(), "Cured_semicured_and_soft_cheese.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cured_semicured_and_soft_cheese_detailed.json"))
    
    SLICED_GRADED_AND_PORTIONED_CHEESE = StaticAisle(name="Sliced, grated & portioned cheese", url="https://tienda.mercadona.es/categories/56",
                                     original_file_uri=os.path.join(category_path(), "Slice_grated_and_portioned_cheese.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Slice_grated_and_portioned_cheese_detailed.json"))
    
    CHEESE_SPREAD_AND_FRESH_CHEESE = StaticAisle(name="Cheese spread & fresh cheese", url="https://tienda.mercadona.es/categories/53",
                                     original_file_uri=os.path.join(category_path(), "Cheese_spread_and_fresh_cheese.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cheese_spread_and_fresh_cheese_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [COOKED_POULTRY_AND_HAM, BACON_AND_SAUSAGES, CHOPPED_PORK_AND_MORTADELLA, CURED_MEAT, SERRANO_HAM, PATE_AND_SOBRASADA, CURED_SEMICURED_AND_SOFT_CHEESE, SLICED_GRADED_AND_PORTIONED_CHEESE, CHEESE_SPREAD_AND_FRESH_CHEESE]

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
                case "COOKED_POULTRY_AND_HAM":
                    aisles = [cls.COOKED_POULTRY_AND_HAM]
                case "BACON_AND_SAUSAGES":
                    aisles = [cls.BACON_AND_SAUSAGES]
                case "CHOPPED_PORK_AND_MORTADELLA":
                    aisles = [cls.CHOPPED_PORK_AND_MORTADELLA]
                case "CURED_MEAT":
                    aisles = [cls.CURED_MEAT]
                case "SERRANO_HAM":
                    aisles = [cls.SERRANO_HAM]
                case "PATE_AND_SOBRASADA":
                    aisles = [cls.PATE_AND_SOBRASADA]
                case "CURED_SEMICURED_AND_SOFT_CHEESE":
                    aisles = [cls.CURED_SEMICURED_AND_SOFT_CHEESE]
                case "SLICED_GRADED_AND_PORTIONED_CHEESE":
                    aisles = [cls.SLICED_GRADED_AND_PORTIONED_CHEESE]
                case "CHEESE_SPREAD_AND_FRESH_CHEESE":
                    aisles = [cls.CHEESE_SPREAD_AND_FRESH_CHEESE]
                
        return aisles
    
class MercadonaFrozenFoodAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frozen_Food")

    RICE_AND_PASTA = StaticAisle(name="Rice & pasta", url="https://tienda.mercadona.es/categories/147",
                                     original_file_uri=os.path.join(category_path(), "Rice_and_pasta.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Rice_and_pasta_detailed.json"))
    
    MEAT = StaticAisle(name="Meat", url="https://tienda.mercadona.es/categories/148",
                                     original_file_uri=os.path.join(category_path(), "Meat.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Meat_detailed.json"))
    
    ICE_CREAM = StaticAisle(name="Ice cream", url="https://tienda.mercadona.es/categories/154",
                                     original_file_uri=os.path.join(category_path(), "Ice_cream.json"),                            
                                     mini_file_detailed_uri=os.path.join(category_path(), "Ice_cream_detailed.json"))
    
    ICE = StaticAisle(name="Ice", url="https://tienda.mercadona.es/categories/155",
                                     original_file_uri=os.path.join(category_path(), "Ice.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Ice_detailed.json"))
    
    SEAFOOD = StaticAisle(name="Seafood", url="https://tienda.mercadona.es/categories/150",
                                     original_file_uri=os.path.join(category_path(), "Seafood.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Seafood_detailed.json"))
    
    FISH = StaticAisle(name="Fish", url="https://tienda.mercadona.es/categories/149",
                                     original_file_uri=os.path.join(category_path(), "Fish.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fish_detailed.json"))
    
    PIZZA = StaticAisle(name="Pizza", url="https://tienda.mercadona.es/categories/151",
                                     original_file_uri=os.path.join(category_path(), "Pizza.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pizza_detailed.json"))
    
    BREADED_FOOD = StaticAisle(name="Breaded food", url="https://tienda.mercadona.es/categories/884",
                                     original_file_uri=os.path.join(category_path(), "Breaded_food.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Breaded_food_detailed.json"))
    
    CAKE_AND_CHURROS = StaticAisle(name="Cake & churros", url="https://tienda.mercadona.es/categories/152",
                                     original_file_uri=os.path.join(category_path(), "Cake_and_churros.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cake_and_churros_detailed.json"))
    
    VEGETABLES = StaticAisle(name="Vegetables", url="https://tienda.mercadona.es/categories/145",
                                     original_file_uri=os.path.join(category_path(), "Vegetables.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vegetables_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [RICE_AND_PASTA, MEAT, ICE_CREAM, ICE, SEAFOOD, FISH, PIZZA, BREADED_FOOD, CAKE_AND_CHURROS, VEGETABLES]

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
                case "RICE_AND_PASTA":
                    aisles = [cls.RICE_AND_PASTA]
                case "MEAT":
                    aisles = [cls.MEAT]
                case "ICE_CREAM":
                    aisles = [cls.ICE_CREAM]
                case "ICE":
                    aisles = [cls.ICE]
                case "SEAFOOD":
                    aisles = [cls.SEAFOOD]
                case "FISH":
                    aisles = [cls.FISH]
                case "PIZZA":
                    aisles = [cls.PIZZA]
                case "BREADED_FOOD":
                    aisles = [cls.BREADED_FOOD]
                case "CAKE_AND_CHURROS":
                    aisles = [cls.CAKE_AND_CHURROS]
                case "VEGETABLES":
                    aisles = [cls.VEGETABLES]
                
        return aisles
    
class MercadonaCansSoupsAndCreamsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Cans_Soups_And_Creams")

    TUNA_AND_OTHER_FISH_CANS = StaticAisle(name="Tuna & other fish cans", url="https://tienda.mercadona.es/categories/122",
                                     original_file_uri=os.path.join(category_path(), "Tuna_and_other_fish_cans.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tuna_and_other_fish_cans_detailed.json"))
    
    COCKLES_AND_MUSSELS = StaticAisle(name="Cockles & mussels", url="https://tienda.mercadona.es/categories/123",
                                     original_file_uri=os.path.join(category_path(), "Cockles_and_mussels.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cockles_and_mussels_detailed.json"))
    
    VEGETABLE_AND_FRUIT_TINS = StaticAisle(name="Vegetable & fruit tins", url="https://tienda.mercadona.es/categories/127",
                                     original_file_uri=os.path.join(category_path(), "Vegetable_and_fruit_tins.json"),                            
                                     mini_file_detailed_uri=os.path.join(category_path(), "Ice_cream_detailed.json"))
    
    GAZPACHO_AND_CREAMS = StaticAisle(name="Gazpacho & creams", url="https://tienda.mercadona.es/categories/130",
                                     original_file_uri=os.path.join(category_path(), "Gazpacho_creams.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Gazpacho_creams_detailed.json"))
    
    SOUPS_AND_STOCKS = StaticAisle(name="Soups & stock", url="https://tienda.mercadona.es/categories/129",
                                     original_file_uri=os.path.join(category_path(), "Soups_stock.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Soups_stock_detailed.json"))
    
    TOMATO = StaticAisle(name="Tomato", url="https://tienda.mercadona.es/categories/126",
                                     original_file_uri=os.path.join(category_path(), "Tomato.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tomato_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [TUNA_AND_OTHER_FISH_CANS, COCKLES_AND_MUSSELS, VEGETABLE_AND_FRUIT_TINS, GAZPACHO_AND_CREAMS, SOUPS_AND_STOCKS, TOMATO]

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
                case "TUNA_AND_OTHER_FISH_CANS":
                    aisles = [cls.TUNA_AND_OTHER_FISH_CANS]
                case "COCKLES_AND_MUSSELS":
                    aisles = [cls.COCKLES_AND_MUSSELS]
                case "VEGETABLE_AND_FRUIT_TINS":
                    aisles = [cls.VEGETABLE_AND_FRUIT_TINS]
                case "GAZPACHO_AND_CREAMS":
                    aisles = [cls.GAZPACHO_AND_CREAMS]
                case "SOUPS_AND_STOCKS":
                    aisles = [cls.SOUPS_AND_STOCKS]
                case "TOMATO":
                    aisles = [cls.TOMATO]
            
        return aisles  

class MercadonaFruitsAndVegetablesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Fruits_And_Vegetables")

    FRUITS = StaticAisle(name="Fruits", url="https://tienda.mercadona.es/categories/27",
                                     original_file_uri=os.path.join(category_path(), "Fruits.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fruits_detailed.json"))
    
    LETTUCE_AND_PREPARED_SALAD = StaticAisle(name="Lettuce & prepared salad", url="https://tienda.mercadona.es/categories/28",
                                     original_file_uri=os.path.join(category_path(), "Lettuce_and_prepared_salad.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Lettuce_and_prepared_salad_detailed.json"))
    
    VEGETABLES = StaticAisle(name="Vegetables", url="https://tienda.mercadona.es/categories/29",
                                     original_file_uri=os.path.join(category_path(), "Vegetables.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vegetables_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [FRUITS, LETTUCE_AND_PREPARED_SALAD, VEGETABLES]

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
                case "FRUITS":
                    aisles = [cls.FRUITS]
                case "LETTUCE_AND_PREPARED_SALAD":
                    aisles = [cls.LETTUCE_AND_PREPARED_SALAD]
                case "VEGETABLES":
                    aisles = [cls.VEGETABLES]
      
        return aisles
    
class MercadonaEggsMilkAndButterAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Eggs_Milk_And_Butter")

    EGGS = StaticAisle(name="Eggs", url="https://tienda.mercadona.es/categories/77",
                                     original_file_uri=os.path.join(category_path(), "Eggs.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Eggs_detailed.json"))
    
    MILK_AND_MILK_ALTERNATIVES = StaticAisle(name="Milk & milk alternatives", url="https://tienda.mercadona.es/categories/72",
                                     original_file_uri=os.path.join(category_path(), "Milk_and_milk_alternatives.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Milk_and_milk_alternatives_detailed.json"))
    
    BUTTER_AND_MARGARINE = StaticAisle(name="Butter & margarine", url="https://tienda.mercadona.es/categories/75",
                                     original_file_uri=os.path.join(category_path(), "Butter_and_margarine.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Butter_and_margarine_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [EGGS, MILK_AND_MILK_ALTERNATIVES, BUTTER_AND_MARGARINE]

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
                case "EGGS":
                    aisles = [cls.EGGS]
                case "MILK_AND_MILK_ALTERNATIVES":
                    aisles = [cls.MILK_AND_MILK_ALTERNATIVES]
                case "BUTTER_AND_MARGARINE":
                    aisles = [cls.BUTTER_AND_MARGARINE]
      
        return aisles

class MercadonaSeafoodAndFishAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Seafood_And_Fish")

    SEAFOOD = StaticAisle(name="Seafood", url="https://tienda.mercadona.es/categories/32",
                                     original_file_uri=os.path.join(category_path(), "Seafood.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Seafood_detailed.json"))
    
    FROZEN_FISH = StaticAisle(name="Frozen fish", url="https://tienda.mercadona.es/categories/34",
                                     original_file_uri=os.path.join(category_path(), "Frozen_fish.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Frozen_fish_detailed.json"))
    
    FRESH_FISH = StaticAisle(name="Fresh fish", url="https://tienda.mercadona.es/categories/31",
                                     original_file_uri=os.path.join(category_path(), "Fresh_fish.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fresh_fish_detailed.json"))

    SALTED_AND_SMOKED = StaticAisle(name="Salted & smoked fish", url="https://tienda.mercadona.es/categories/36",
                                     original_file_uri=os.path.join(category_path(), "Salted_and_smoked fish.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Salted_and_smoked_detailed.json"))
    
    SUSHI = StaticAisle(name="Sushi", url="https://tienda.mercadona.es/categories/789",
                                     original_file_uri=os.path.join(category_path(), "Sushi.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sushi_detailed.json"))
    

   
    
    aisles: Final[List[StaticAisle]] = [SEAFOOD, FROZEN_FISH, FRESH_FISH, SALTED_AND_SMOKED, SUSHI]

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
                case "SEAFOOD":
                    aisles = [cls.SEAFOOD]
                case "FROZEN_FISH":
                    aisles = [cls.FROZEN_FISH]
                case "FRESH_FISH":
                    aisles = [cls.FRESH_FISH]
                case "SALTED_AND_SMOKED":
                    aisles = [cls.SALTED_AND_SMOKED]
                case "SUSHI":
                    aisles = [cls.SUSHI]
  
      
        return aisles

class MercadonaPetAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Pets")

    CAT = StaticAisle(name="Cat", url="https://tienda.mercadona.es/categories/222",
                                     original_file_uri=os.path.join(category_path(), "Cat.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cat_detailed.json"))
    
    DOG = StaticAisle(name="Dog", url="https://tienda.mercadona.es/categories/221",
                                     original_file_uri=os.path.join(category_path(), "Dog.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Dog_detailed.json"))
    
    OTHERS = StaticAisle(name="Others", url="https://tienda.mercadona.es/categories/225",
                                     original_file_uri=os.path.join(category_path(), "Pet_Others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pet_Others_detailed.json"))

  
    

   
    
    aisles: Final[List[StaticAisle]] = [CAT, DOG, OTHERS]

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
                case "CAT":
                    aisles = [cls.CAT]
                case "DOG":
                    aisles = [cls.DOG]
                case "OTHERS":
                    aisles = [cls.OTHERS]
           
        return aisles

class MercadonaBreadAndbakeryAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Bread_And_bakery")

    OVEN_PASTRIES = StaticAisle(name="Oven pastries", url="https://tienda.mercadona.es/categories/65",
                                     original_file_uri=os.path.join(category_path(), "Oven_pastries.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Oven_pastries_detailed.json"))
    
    PACKAGED_PASTRIES = StaticAisle(name="Packaged pastries", url="https://tienda.mercadona.es/categories/66",
                                     original_file_uri=os.path.join(category_path(), "Packaged_pastries.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Packaged_pastries_detailed.json"))
    
    FLOUR_AND_BAKING_SUPPLIES = StaticAisle(name="Flour & baking supplies", url="https://tienda.mercadona.es/categories/69",
                                     original_file_uri=os.path.join(category_path(), "Flour_and_baking_supplies.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Flour_and_baking_supplies_detailed.json"))

    OVEN_BREAD = StaticAisle(name="Oven bread", url="https://tienda.mercadona.es/categories/59",
                                     original_file_uri=os.path.join(category_path(), "Oven_bread.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Oven_bread_detailed.json"))
    
    PACKAGED_SLICED_BREAD_AND_OTHER_SPECIALITIES = StaticAisle(name="Packaged sliced bread & other specialities", url="https://tienda.mercadona.es/categories/60",
                                     original_file_uri=os.path.join(category_path(), "Packaged_sliced_bread_and_other_specialities.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Packaged_sliced_bread_and_other_specialities_detailed.json"))
    
    TOASTED_BREAD_AND_BREADCRUMBS = StaticAisle(name="Toasted bread & breadcrumbs", url="https://tienda.mercadona.es/categories/62",
                                     original_file_uri=os.path.join(category_path(), "Toasted_bread_and_breadcrumbs.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Toasted_bread_and_breadcrumbs_detailed.json"))

    BREADSTICKS_AND_CROUTONS = StaticAisle(name="Breadsticks & croutons", url="https://tienda.mercadona.es/categories/64",
                                     original_file_uri=os.path.join(category_path(), "Breadsticks_and_croutons.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Breadsticks_and_croutons_detailed.json"))
    
    CAKES_AND_TARTS = StaticAisle(name="Cakes & tarts", url="https://tienda.mercadona.es/categories/68",
                                     original_file_uri=os.path.join(category_path(), "Cakes_and_tarts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cakes_and_tarts_detailed.json"))
    
    CANDLES_AND_DECORATION = StaticAisle(name="Candles & decoration", url="https://tienda.mercadona.es/categories/71",
                                     original_file_uri=os.path.join(category_path(), "Candles_and_decoration.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Candles_and_decoration_detailed.json"))

  
    
    aisles: Final[List[StaticAisle]] = [OVEN_PASTRIES, PACKAGED_PASTRIES, FLOUR_AND_BAKING_SUPPLIES, OVEN_BREAD, PACKAGED_SLICED_BREAD_AND_OTHER_SPECIALITIES, TOASTED_BREAD_AND_BREADCRUMBS, BREADSTICKS_AND_CROUTONS, CAKES_AND_TARTS, CANDLES_AND_DECORATION]

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
                case "OVEN_PASTRIES":
                    aisles = [cls.OVEN_PASTRIES]
                case "PACKAGED_PASTRIES":
                    aisles = [cls.PACKAGED_PASTRIES]
                case "FLOUR_AND_BAKING_SUPPLIES":
                    aisles = [cls.FLOUR_AND_BAKING_SUPPLIES]
                case "OVEN_BREAD":
                    aisles = [cls.OVEN_BREAD]
                case "PACKAGED_SLICED_BREAD_AND_OTHER_SPECIALITIES":
                    aisles = [cls.PACKAGED_SLICED_BREAD_AND_OTHER_SPECIALITIES]
                case "TOASTED_BREAD_AND_BREADCRUMBS":
                    aisles = [cls.TOASTED_BREAD_AND_BREADCRUMBS]
                case "BREADSTICKS_AND_CROUTONS":
                    aisles = [cls.BREADSTICKS_AND_CROUTONS]
                case "CAKES_AND_TARTS":
                    aisles = [cls.CAKES_AND_TARTS]
                case "CANDLES_AND_DECORATION":
                    aisles = [cls.CANDLES_AND_DECORATION]
           
        return aisles

class MercadonaPizzaAndReadyMealsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Pizza_And_ReadyMeals")

    READY_TO_EAT = StaticAisle(name="Ready to eat", url="https://tienda.mercadona.es/categories/897",
                                     original_file_uri=os.path.join(category_path(), "Ready_to_eat.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Ready_to_eat_detailed.json"))
    
    PIZZA = StaticAisle(name="Pizza", url="https://tienda.mercadona.es/categories/138",
                                     original_file_uri=os.path.join(category_path(), "Pizza.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pizza_detailed.json"))
    
    HOT_READY_MEALS = StaticAisle(name="Hot ready meals", url="https://tienda.mercadona.es/categories/140",
                                     original_file_uri=os.path.join(category_path(), "Hot_ready_meals.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Hot_ready_meals_detailed.json"))

    COLD_READY_MEALS = StaticAisle(name="Cold ready meals", url="https://tienda.mercadona.es/categories/142",
                                     original_file_uri=os.path.join(category_path(), "Cold_ready_meals.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cold_ready_meals_detailed.json"))

    aisles: Final[List[StaticAisle]] = [READY_TO_EAT, PIZZA, HOT_READY_MEALS, COLD_READY_MEALS]
    
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
                case "READY_TO_EAT":
                    aisles = [cls.READY_TO_EAT]
                case "PIZZA":
                    aisles = [cls.PIZZA]
                case "HOT_READY_MEALS":
                    aisles = [cls.HOT_READY_MEALS]
                case "COLD_READY_MEALS":
                    aisles = [cls.COLD_READY_MEALS]
                
           
        return aisles
    
class MercadonaDessertAndYoghurtAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Dessert_And_Yoghurt")

    BIFIDUS = StaticAisle(name="Bífidus", url="https://tienda.mercadona.es/categories/105",
                                     original_file_uri=os.path.join(category_path(), "Bífidus.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Bífidus_detailed.json"))
    
    FLAN_AND_CUSTARD = StaticAisle(name="Flan & custard", url="https://tienda.mercadona.es/categories/110",
                                     original_file_uri=os.path.join(category_path(), "Flan_and_custard.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Flan_and_custard_detailed.json"))
    
    JELLY_AND_OTHER_DESSERTS = StaticAisle(name="Jelly & other desserts", url="https://tienda.mercadona.es/categories/111",
                                     original_file_uri=os.path.join(category_path(), "Jelly_and_other_desserts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Hot_ready_meals_detailed.json"))

    SOY_DESSERTS = StaticAisle(name="Soy desserts", url="https://tienda.mercadona.es/categories/106",
                                     original_file_uri=os.path.join(category_path(), "Soy_desserts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Soy_desserts_detailed.json"))

    LOW_FAT_YOGHURT = StaticAisle(name="Low fat yoghurt", url="https://tienda.mercadona.es/categories/103",
                                     original_file_uri=os.path.join(category_path(), "Low_fat_yoghurt.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Low_fat_yoghurt_detailed.json"))
    
    GREEK_YOGHURT = StaticAisle(name="Greek yoghurt", url="https://tienda.mercadona.es/categories/109",
                                     original_file_uri=os.path.join(category_path(), "Greek_yoghurt.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Greek_yoghurt_detailed.json"))
    
    LIQUID_YOGHURT = StaticAisle(name="Liquid yoghurt", url="https://tienda.mercadona.es/categories/108",
                                     original_file_uri=os.path.join(category_path(), "Liquid_yoghurt.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Liquid_yoghurt_detailed.json"))

    NATURAL_AND_FLAVOURED_YOGHURT = StaticAisle(name="Natural & flavoured yoghurt", url="https://tienda.mercadona.es/categories/104",
                                     original_file_uri=os.path.join(category_path(), "Natural_and_flavoured_yoghurt.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Natural_and_flavoured_yoghurt_detailed.json"))

    CHILDRENS_YOGHURT_AND_DESSERT = StaticAisle(name="Children's yoghurt & dessert", url="https://tienda.mercadona.es/categories/107",
                                     original_file_uri=os.path.join(category_path(), "Children's_yoghurt_and_dessert.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Children's_yoghurt_and_dessert_detailed.json"))

    aisles: Final[List[StaticAisle]] = [BIFIDUS , FLAN_AND_CUSTARD, JELLY_AND_OTHER_DESSERTS, SOY_DESSERTS, LOW_FAT_YOGHURT, GREEK_YOGHURT, LIQUID_YOGHURT, NATURAL_AND_FLAVOURED_YOGHURT, CHILDRENS_YOGHURT_AND_DESSERT]
    
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
                case "BIFIDUS":
                    aisles = [cls.BIFIDUS]
                case "FLAN_AND_CUSTARD":
                    aisles = [cls.FLAN_AND_CUSTARD]
                case "JELLY_AND_OTHER_DESSERTS":
                    aisles = [cls.JELLY_AND_OTHER_DESSERTS]
                case "SOY_DESSERTS":
                    aisles = [cls.SOY_DESSERTS]
                case "LOW_FAT_YOGHURT":
                    aisles = [cls.LOW_FAT_YOGHURT]
                case "GREEK_YOGHURT":
                    aisles = [cls.GREEK_YOGHURT]
                case "LIQUID_YOGHURT":
                    aisles = [cls.LIQUID_YOGHURT]
                case "NATURAL_AND_FLAVOURED_YOGHURT":
                    aisles = [cls.NATURAL_AND_FLAVOURED_YOGHURT]
                case "CHILDRENS_YOGHURT_AND_DESSERT":
                    aisles = [cls.CHILDRENS_YOGHURT_AND_DESSERT]
               
           
        return aisles
    
class MercadonaJuiceAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Juices")

    ASSORTED_FRUIT = StaticAisle(name="Assorted fruit", url="https://tienda.mercadona.es/categories/99",
                                     original_file_uri=os.path.join(category_path(), "Assorted_fruit.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Assorted_fruit_detailed.json"))
    
    PEACH_AND_PINEAPPLE = StaticAisle(name="Peach & pineapple", url="https://tienda.mercadona.es/categories/100",
                                     original_file_uri=os.path.join(category_path(), "Peach_and_pineapple.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Peach_and_pineapple_detailed.json"))
    
    ORANGE = StaticAisle(name="Orange", url="https://tienda.mercadona.es/categories/143",
                                     original_file_uri=os.path.join(category_path(), "Orange.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Orange_detailed.json"))

    TOMATO_AND_OTHER_FLAVOURS = StaticAisle(name="Tomato & other flavours", url="https://tienda.mercadona.es/categories/98",
                                     original_file_uri=os.path.join(category_path(), "Tomato_and_other_flavours.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tomato_and_other_flavours_detailed.json"))

    aisles: Final[List[StaticAisle]] = [ASSORTED_FRUIT, PEACH_AND_PINEAPPLE, ORANGE, TOMATO_AND_OTHER_FLAVOURS]    
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
                case "ASSORTED_FRUIT":
                    aisles = [cls.ASSORTED_FRUIT]
                case "PEACH_AND_PINEAPPLE":
                    aisles = [cls.PEACH_AND_PINEAPPLE]
                case "ORANGE":
                    aisles = [cls.ORANGE]
                case "TOMATO_AND_OTHER_FLAVOURS":
                    aisles = [cls.TOMATO_AND_OTHER_FLAVOURS]
       
        return aisles
    
mercadona_categories_with_uris: Final[list[StaticCategory]] = [

    StaticCategory(name="Oils Spices and Sauces",
                   url="https://tienda.mercadona.es/categories/112", aisles=MercadonaOilsSpicesAndSaucesAlimentations.aisles),

    StaticCategory(name="Water and soft drinks", url="https://tienda.mercadona.es/categories/156",
                   aisles=MercadonaWaterAndSoftDrinksAlimentations.aisles),

    StaticCategory(name="Snacks", url="https://tienda.mercadona.es/categories/135",
                   aisles=MercadonaSnacksAlimentations.aisles),

    StaticCategory(name="Rice pulses and pasta", url="https://tienda.mercadona.es/categories/118",
                   aisles=MercadonaRicePulsesPastaAlimentations.aisles),

    StaticCategory(name="Sugar sweets and chocolate", url="https://tienda.mercadona.es/categories/89",
                   aisles=MercadonaSugarSweetsChocolateAlimentations.aisles),

    StaticCategory(name="Baby", url="https://tienda.mercadona.es/categories/216",
                   aisles=MercadonaBabyAlimentations.aisles),

    StaticCategory(name="Beer wine and spirits", url="https://tienda.mercadona.es/categories/164",
                   aisles=MercadonaBeerWineSpiritsAlimentations.aisles),

    StaticCategory(name="Chocolate drinks coffee and tea", url="https://tienda.mercadona.es/categories/86",
                   aisles=MercadonaChocolateDrinksHotChocolateAlimentations.aisles),

    StaticCategory(name="Meat", url="https://tienda.mercadona.es/categories/46",
                   aisles=MercadonaMeatAlimentations.aisles),

    StaticCategory(name="Cereal and biscuits", url="https://tienda.mercadona.es/categories/78",
                   aisles=MercadonaCerealAndBiscuitsAlimentations.aisles),

    StaticCategory(name="Deli and cheese", url="https://tienda.mercadona.es/categories/48",
                   aisles=MercadonaDeliAndCheeseAlimentations.aisles),

    StaticCategory(name="Frozen food", url="https://tienda.mercadona.es/categories/147",
                   aisles=MercadonaFrozenFoodAlimentations.aisles),

    StaticCategory(name="Cans soups and creams", url="https://tienda.mercadona.es/categories/122",
                   aisles=MercadonaCansSoupsAndCreamsAlimentations.aisles),

    StaticCategory(name="Fruits and vegetables", url="https://tienda.mercadona.es/categories/27",
                   aisles=MercadonaFruitsAndVegetablesAlimentations.aisles),

    StaticCategory(name="Eggs milk and butter", url="https://tienda.mercadona.es/categories/77",
                   aisles=MercadonaEggsMilkAndButterAlimentations.aisles),

    StaticCategory(name="Seafood and fish", url="https://tienda.mercadona.es/categories/32",
                   aisles=MercadonaSeafoodAndFishAlimentations.aisles),

    StaticCategory(name="Pet", url="https://tienda.mercadona.es/categories/222",
                   aisles=MercadonaPetAlimentations.aisles),

    StaticCategory(name="Bread and bakery", url="https://tienda.mercadona.es/categories/65",
                   aisles=MercadonaBreadAndbakeryAlimentations.aisles),

    StaticCategory(name="Pizza and ready meals", url="https://tienda.mercadona.es/categories/897",
                   aisles=MercadonaPizzaAndReadyMealsAlimentations.aisles),

    StaticCategory(name="Dessert and yoghurt", url="https://tienda.mercadona.es/categories/105",
                   aisles=MercadonaDessertAndYoghurtAlimentations.aisles),

    StaticCategory(name="Juice", url="https://tienda.mercadona.es/categories/99",
                   aisles=MercadonaJuiceAlimentations.aisles),

    
]



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
        for category in mercadona_categories_with_uris:
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
                case "MercadonaOilsSpicesAndSaucesAlimentations":
                    aisles = MercadonaOilsSpicesAndSaucesAlimentations.get_aisles(cmdargs[1])
                case "MercadonaWaterAndSoftDrinksAlimentations":
                    aisles = MercadonaWaterAndSoftDrinksAlimentations.get_aisles(
                        cmdargs[1])
                case "MercadonaSnacksAlimentations":
                    aisles = MercadonaSnacksAlimentations.get_aisles(cmdargs[1])
                case "MercadonaRicePulsesPastaAlimentations":
                    aisles = MercadonaRicePulsesPastaAlimentations.get_aisles(cmdargs[1])
                case "MercadonaSugarSweetsChocolateAlimentations":
                    aisles = MercadonaSugarSweetsChocolateAlimentations.get_aisles(cmdargs[1])
                case "MercadonaBabyAlimentations":
                    aisles = MercadonaBabyAlimentations.get_aisles(cmdargs[1])
                case "MercadonaBeerWineSpiritsAlimentations":
                    aisles = MercadonaBeerWineSpiritsAlimentations.get_aisles(cmdargs[1])
                case "MercadonaChocolateDrinksHotChocolateAlimentations":
                    aisles = MercadonaChocolateDrinksHotChocolateAlimentations.get_aisles(cmdargs[1])
                case "MercadonaMeatAlimentations":
                    aisles = MercadonaMeatAlimentations.get_aisles(cmdargs[1])
                case "MercadonaCerealAndBiscuitsAlimentations":
                    aisles = MercadonaCerealAndBiscuitsAlimentations.get_aisles(cmdargs[1])
                case "MercadonaDeliAndCheeseAlimentations":
                    aisles = MercadonaDeliAndCheeseAlimentations.get_aisles(cmdargs[1])
                case "MercadonaFrozenFoodAlimentations":
                    aisles = MercadonaFrozenFoodAlimentations.get_aisles(cmdargs[1])
                case "MercadonaCansSoupsAndCreamsAlimentations":
                    aisles = MercadonaCansSoupsAndCreamsAlimentations.get_aisles(cmdargs[1])
                case "MercadonaFruitsAndVegetablesAlimentations":
                    aisles = MercadonaFruitsAndVegetablesAlimentations.get_aisles(cmdargs[1])
                case "MercadonaEggsMilkAndButterAlimentations":
                    aisles = MercadonaEggsMilkAndButterAlimentations.get_aisles(cmdargs[1])
                case "MercadonaSeafoodAndFishAlimentations":
                    aisles = MercadonaSeafoodAndFishAlimentations.get_aisles(cmdargs[1])
                case "Mercadona_Pet_Alimentations":
                    aisles = MercadonaPetAlimentations.get_aisles(cmdargs[1])
                case "MercadonaBreadAndbakeryAlimentations":
                    aisles = MercadonaBreadAndbakeryAlimentations.get_aisles(cmdargs[1])
                case "MercadonaPizzaAndReadyMealsAlimentations":
                    aisles = MercadonaPizzaAndReadyMealsAlimentations.get_aisles(cmdargs[1])
                case "MercadonaDessertAndYoghurtAlimentations":
                    aisles = MercadonaDessertAndYoghurtAlimentations.get_aisles(cmdargs[1])
                case "MercadonaJuiceAlimentations":
                    aisles = MercadonaJuiceAlimentations.get_aisles(cmdargs[1])              
                case _:
                    logging.error(f"args source not found: {cmdargs[1]}")
                    sys.exit()

    return aisles
    
    
