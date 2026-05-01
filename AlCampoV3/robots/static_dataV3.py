import logging
import os
from statistics import mean
import sys
from turtle import back
from typing import Final, List, Optional, Union

from pyparsing import C
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

#Frescoes

class AlcampoFrescoesFruitsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frescoes_Fruits")

    PLANTAINS_AND_BANANAS = StaticAisle(name="Plantains and Bananas",  url="https://www.compraonline.alcampo.es/categories/frescos/frutas/pl%C3%A1tanos-y-bananas/OC170104?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Plantains_and_Bananas.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Plantains_and_Bananas_detailed.json"))
    
    ORANGES_MANDARINS_AND_LEMONS = StaticAisle(name="Oranges, Mandarins and Lemons", url="https://www.compraonline.alcampo.es/categories/frescos/frutas/naranjas-mandarinas-y-limones/OC170101?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Oranges_Mandarins_and_Lemons.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Oranges_Mandarins_and_Lemons_detailed.json"))
    
    TROPICAL_AND_EXOTIC = StaticAisle(name="Tropical and Exotic",  url="https://www.compraonline.alcampo.es/categories/frescos/frutas/tropicales-y-ex%C3%B3ticas/OC170106?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Tropical_and_Exotic.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tropical_and_Exotic_detailed.json"))
    
    STRAWBERRIES = StaticAisle(name="Strawberries",  url="https://www.compraonline.alcampo.es/categories/frescos/frutas/fresas/OC170109001?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Strawberries.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Strawberries_detailed.json"))
    
    PEARS_AND_APPLES = StaticAisle(name="Pears and Apples",  url="https://www.compraonline.alcampo.es/categories/frescos/frutas/peras-y-manzanas/OC170102001?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Pears_and_Apples.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pears_and_Apples_detailed.json"))
    
    SEASONAL_FRUITS = StaticAisle(name="Seasonal fruits",  url="https://www.compraonline.alcampo.es/categories/frescos/frutas/frutas-de-temporada/OC170105?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Seasonal_fruits.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Seasonal_fruits_detailed.json"))
    
    WATERMELONS_AND_MELONS = StaticAisle(name="Watermelons and Melons",  url="https://www.compraonline.alcampo.es/categories/frescos/frutas/sand%C3%ADas-y-melones/OC170110?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Watermelons_and_Melons.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Watermelons_and_Melons_detailed.json"))
    
    FOREST_FRUITS = StaticAisle(name="Forest fruits",  url="https://www.compraonline.alcampo.es/categories/frescos/frutas/frutas-del-bosque/OC170109?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Forest_fruits.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Forest_fruits_detailed.json"))
    
    ORGANIC_FRUITS = StaticAisle(name="Organic fruits",  url="https://www.compraonline.alcampo.es/categories/frescos/frutas/frutas-ecol%C3%B3gicas/OC170107?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_fruits.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_fruits_detailed.json"))
    
    FRESHLY_SQUEEZED_JUICE = StaticAisle(name="Freshly squeezed juice",  url="https://www.compraonline.alcampo.es/categories/frescos/frutas/zumo-exprimido/OC12082022?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Freshly_squeezed_juice.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Freshly_squeezed_juice_detailed.json"))
    
    CUT_FRUIT = StaticAisle(name="Cut fruit",  url="https://www.compraonline.alcampo.es/categories/frescos/frutas/fruta-cortada/OC170105003?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cut_fruit.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cut_fruit_detailed.json"))
    
    FRUIT_PUREE_AND_SNACKS = StaticAisle(name="Fruit puree and snacks",  url="https://www.compraonline.alcampo.es/categories/frescos/frutas/pur%C3%A9-y-snacks-de-frutas/OCPureSnacksFrutas?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Fruit_puree_and_snacks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fruit_puree_and_snacks_detailed.json"))
    
    MY_FRUITS_AND_VEGETABLES = StaticAisle(name="My fruits and vegetables",  url="https://www.compraonline.alcampo.es/categories/frescos/frutas/mis-frutas-y-verduras/OC170128122022?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "My_fruits_and_vegetables.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "My_fruits_and_vegetables_detailed.json"))
    
    GRAPES = StaticAisle(name="Grapes",  url="https://www.compraonline.alcampo.es/categories/frescos/frutas/uvas/OC170105001?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Grapes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Grapes_detailed.json"))
    
    
    

    aisles: Final[List[StaticAisle]] = [PLANTAINS_AND_BANANAS, ORANGES_MANDARINS_AND_LEMONS, TROPICAL_AND_EXOTIC, STRAWBERRIES, PEARS_AND_APPLES, SEASONAL_FRUITS, WATERMELONS_AND_MELONS, 
                                        FOREST_FRUITS, ORGANIC_FRUITS, FRESHLY_SQUEEZED_JUICE, CUT_FRUIT, FRUIT_PUREE_AND_SNACKS, MY_FRUITS_AND_VEGETABLES,GRAPES]

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
                case "PLANTAINS_AND_BANANAS":
                    aisles = [cls.PLANTAINS_AND_BANANAS]
                case "ORANGES_MANDARINS_AND_LEMONS":
                    aisles = [cls.ORANGES_MANDARINS_AND_LEMONS]
                case "TROPICAL_AND_EXOTIC":
                    aisles = [cls.TROPICAL_AND_EXOTIC]
                case "STRAWBERRIES":
                    aisles = [cls.STRAWBERRIES]
                case "PEARS_AND_APPLES":
                    aisles = [cls.PEARS_AND_APPLES]
                case "SEASONAL_FRUITS":
                    aisles = [cls.SEASONAL_FRUITS]
                case "WATERMELONS_AND_MELONS":
                    aisles = [cls.WATERMELONS_AND_MELONS]
                case "FOREST_FRUITS":
                    aisles = [cls.FOREST_FRUITS]
                case "ORGANIC_FRUITS":
                    aisles = [cls.ORGANIC_FRUITS]
                case "FRESHLY_SQUEEZED_JUICE":
                    aisles = [cls.FRESHLY_SQUEEZED_JUICE]
                case "CUT_FRUIT":
                    aisles = [cls.CUT_FRUIT]
                case "FRUIT_PUREE_AND_SNACKS":
                    aisles = [cls.FRUIT_PUREE_AND_SNACKS]
                case "CUT_FMY_FRUITS_AND_VEGETABLESRUIT":
                    aisles = [cls.MY_FRUITS_AND_VEGETABLES]
                case "GRAPES":
                    aisles = [cls.GRAPES]
        return aisles
    
class AlcampoFrescoesVegetablesAndGreensAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frescoes_Vegetables_and_Greens")

    SALADS_AND_PREPARED_VEGETABLES = StaticAisle(name="Salads and prepared vegetables",  url="https://www.compraonline.alcampo.es/categories/frescos/verduras-y-hortalizas/ensaladas-y-verduras-preparadas/OC170209?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Salads_and_prepared_vegetables.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Salads_and_prepared_vegetables_detailed.json"))
    
    POTATOES_GARLIC_AND_ONIONS = StaticAisle(name="Potatoes, garlic and onions", url="https://www.compraonline.alcampo.es/categories/frescos/verduras-y-hortalizas/patatas-ajos-y-cebollas/OCPatataAjoCebolla?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Potatoes_garlic_and_onions.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Potatoes_garlic_and_onions_detailed.json"))
    
    TOMATOES_CUCUMBERS_AND_PEPPERS = StaticAisle(name="Tomatoes, cucumbers and peppers",  url="https://www.compraonline.alcampo.es/categories/frescos/verduras-y-hortalizas/tomates-pepinos-y-pimientos/OC170207?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Tomatoes_cucumbers_and_peppers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tomatoes_cucumbers_and_peppers_detailed.json"))
    
    CARROTS_AND_LEEKS = StaticAisle(name="Carrots and Leeks",  url="https://www.compraonline.alcampo.es/categories/frescos/verduras-y-hortalizas/zanahorias-y-puerros/OC170208009?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Carrots_and_Leeks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Carrots_and_Leeks_detailed.json"))
    
    PUMPKIN_ZUCCHINI_AND_EGGPLANT = StaticAisle(name="Pumpkin, zucchini and eggplant",  url="https://www.compraonline.alcampo.es/categories/frescos/verduras-y-hortalizas/calabaza-calabac%C3%ADn-y-berenjenas/OCCalabazasBerenjenas?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Pumpkin_zucchini_and_eggplant.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pumpkin_zucchini_and_eggplant_detailed.json"))
    
    LETTUCE_CAULIFLOWER_AND_CABBAGE = StaticAisle(name="Lettuce, cauliflower and cabbage",  url="https://www.compraonline.alcampo.es/categories/frescos/verduras-y-hortalizas/lechugas-coliflor-y-repollos/OCLechugasColRepollo?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Lettuce_cauliflower_and_cabbage.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Lettuce_cauliflower_and_cabbage_detailed.json"))
    
    AROMATICS_BUNCHES_AND_OTHERS = StaticAisle(name="Aromatics, bunches and others",  url="https://www.compraonline.alcampo.es/categories/frescos/verduras-y-hortalizas/arom%C3%A1ticas-manojos-y-otras/OC170208?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Aromatics_bunches_and_others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Aromatics_bunches_and_others_detailed.json"))
    
    BEANS_ARTICHOKES_AND_ASPARAGUS = StaticAisle(name="Beans, artichokes and asparagus",  url="https://www.compraonline.alcampo.es/categories/frescos/verduras-y-hortalizas/jud%C3%ADa-alcachofa-y-esp%C3%A1rragos/OCJudiasEsparragos?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Beans_artichokes_and_asparagus.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Beans_artichokes_and_asparagus_detailed.json"))
    
    MUSHROOMS_AND_TOADSTOOLS = StaticAisle(name="Mushrooms and Toadstools",  url="https://www.compraonline.alcampo.es/categories/frescos/verduras-y-hortalizas/champi%C3%B1ones-y-setas/OC170204?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Mushrooms_and_Toadstools.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mushrooms_and_Toadstools_detailed.json"))
    
    ORGANIC_VEGETABLES = StaticAisle(name="Organic Vegetables",  url="https://www.compraonline.alcampo.es/categories/frescos/verduras-y-hortalizas/verduras-ecol%C3%B3gicas/OC170210?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Vegetables.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Vegetables_detailed.json"))
    

    aisles: Final[List[StaticAisle]] = [SALADS_AND_PREPARED_VEGETABLES, POTATOES_GARLIC_AND_ONIONS, TOMATOES_CUCUMBERS_AND_PEPPERS, CARROTS_AND_LEEKS, PUMPKIN_ZUCCHINI_AND_EGGPLANT, LETTUCE_CAULIFLOWER_AND_CABBAGE,
                                        AROMATICS_BUNCHES_AND_OTHERS, BEANS_ARTICHOKES_AND_ASPARAGUS, MUSHROOMS_AND_TOADSTOOLS, ORGANIC_VEGETABLES]

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
                case "SALADS_AND_PREPARED_VEGETABLES":
                    aisles = [cls.SALADS_AND_PREPARED_VEGETABLES]
                case "POTATOES_GARLIC_AND_ONIONS":
                    aisles = [cls.POTATOES_GARLIC_AND_ONIONS]
                case "TOMATOES_CUCUMBERS_AND_PEPPERS":
                    aisles = [cls.TOMATOES_CUCUMBERS_AND_PEPPERS]
                case "CARROTS_AND_LEEKS":
                    aisles = [cls.CARROTS_AND_LEEKS]
                case "PUMPKIN_ZUCCHINI_AND_EGGPLANT":
                    aisles = [cls.PUMPKIN_ZUCCHINI_AND_EGGPLANT]
                case "LETTUCE_CAULIFLOWER_AND_CABBAGE":
                    aisles = [cls.LETTUCE_CAULIFLOWER_AND_CABBAGE]
                case "AROMATICS_BUNCHES_AND_OTHERS":
                    aisles = [cls.AROMATICS_BUNCHES_AND_OTHERS]
                case "BEANS_ARTICHOKES_AND_ASPARAGUS":
                    aisles = [cls.BEANS_ARTICHOKES_AND_ASPARAGUS]
                case "MUSHROOMS_AND_TOADSTOOLS":
                    aisles = [cls.MUSHROOMS_AND_TOADSTOOLS]
                case "ORGANIC_VEGETABLES":
                    aisles = [cls.ORGANIC_VEGETABLES]
                
        return aisles
    
class AlcampoFrescoesMeatAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frescoes_Meat")

    CHICKEN = StaticAisle(name="Chicken",  url="https://www.compraonline.alcampo.es/categories/frescos/carne/pollo/OC1301?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Chicken.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chicken_detailed.json"))
    
    BOVINE = StaticAisle(name="Bovine", url="https://www.compraonline.alcampo.es/categories/frescos/carne/vacuno/OC1304?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Bovine.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Bovine_detailed.json"))
    
    PIG = StaticAisle(name="Pig",  url="https://www.compraonline.alcampo.es/categories/frescos/carne/cerdo/OC1302?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Pig.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pig_detailed.json"))
    
    PREPARED = StaticAisle(name="Prepared",  url="https://www.compraonline.alcampo.es/categories/frescos/carne/elaborados/OC1307?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Prepared.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Prepared_detailed.json"))
    
    BURGER_MEAT_AND_MINCED_MEAT = StaticAisle(name="Burger meat and minced meat",  url="https://www.compraonline.alcampo.es/categories/frescos/carne/burguer-meat-y-picada/OC1827?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Burger_meat_and_minced_meat.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Burger_meat_and_minced_meat_detailed.json"))
    
    LAMB = StaticAisle(name="Lamb",  url="https://www.compraonline.alcampo.es/categories/frescos/carne/cordero/OC1303?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Lamb.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Lamb_detailed.json"))
    
    TURKEY = StaticAisle(name="Turkey",  url="https://www.compraonline.alcampo.es/categories/frescos/carne/pavo/OC130103?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Turkey.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Turkey_detailed.json"))
    
    OTHER_BIRDS = StaticAisle(name="Other birds",  url="https://www.compraonline.alcampo.es/categories/frescos/carne/otras-aves/OC130110?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Other_birds.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_birds_detailed.json"))
    
    RABBIT = StaticAisle(name="Rabbit",  url="https://www.compraonline.alcampo.es/categories/frescos/carne/conejo/OC1305?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Rabbit.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Rabbit_detailed.json"))
    
    EQUINE_AND_HUNTING = StaticAisle(name="Equine and hunting",  url="https://www.compraonline.alcampo.es/categories/frescos/carne/equino-y-caza/OC1309?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Equine_and_hunting.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Equine_and_hunting_detailed.json"))
    
    OFFAL = StaticAisle(name="Offal",  url="https://www.compraonline.alcampo.es/categories/frescos/carne/casquer%C3%ADa/OC1308?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Offal.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Offal_detailed.json"))
    
    ESSENTIAL_MEAT_FOR_YOUR_BARBECUE = StaticAisle(name="Essential meat for your barbecue",  url="https://www.compraonline.alcampo.es/categories/frescos/carne/carne-indispensable-para-tu-barbacoa/OCBBQ2025?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Essential_meat_for_your_barbecue.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Essential_meat_for_your_barbecue_detailed.json"))
    
    ESSENTIALS_FOR_YOUR_AIR_FRYER = StaticAisle(name="Essentials for your air fryer",  url="https://www.compraonline.alcampo.es/categories/frescos/carne/esenciales-para-tu-freidora-de-aire/OCcarnfreiaire?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Essentials_for_your_air_fryer.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Essentials_for_your_air_fryer_detailed.json"))
    

    aisles: Final[List[StaticAisle]] = [CHICKEN, BOVINE, PIG, PREPARED, BURGER_MEAT_AND_MINCED_MEAT, LAMB, TURKEY, OTHER_BIRDS, RABBIT, EQUINE_AND_HUNTING, OFFAL, ESSENTIAL_MEAT_FOR_YOUR_BARBECUE,
                                        ESSENTIALS_FOR_YOUR_AIR_FRYER]

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
                case "CHICKEN":
                    aisles = [cls.CHICKEN]
                case "BOVINE":
                    aisles = [cls.BOVINE]
                case "PIG":
                    aisles = [cls.PIG]
                case "PREPARED":
                    aisles = [cls.PREPARED]
                case "BURGER_MEAT_AND_MINCED_MEAT":
                    aisles = [cls.BURGER_MEAT_AND_MINCED_MEAT]
                case "LAMB":
                    aisles = [cls.LAMB]
                case "TURKEY":
                    aisles = [cls.TURKEY]
                case "OTHER_BIRDS":
                    aisles = [cls.OTHER_BIRDS]
                case "RABBIT":
                    aisles = [cls.RABBIT]
                case "EQUINE_AND_HUNTING":
                    aisles = [cls.EQUINE_AND_HUNTING]
                case "OFFAL":
                    aisles = [cls.OFFAL]
                case "ESSENTIAL_MEAT_FOR_YOUR_BARBECUE":
                    aisles = [cls.ESSENTIAL_MEAT_FOR_YOUR_BARBECUE]
                case "ESSENTIALS_FOR_YOUR_AIR_FRYER":
                    aisles = [cls.ESSENTIALS_FOR_YOUR_AIR_FRYER]
                
        return aisles
    
class AlcampoFrescoesShellfishAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frescoes_Fish")

    FISH = StaticAisle(name="Fish",  url="https://www.compraonline.alcampo.es/categories/frescos/pescados-mariscos-y-moluscos/pescado/OC1401?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Fish.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fish_detailed.json"))
    
    SEAFOOD = StaticAisle(name="Seafood", url="https://www.compraonline.alcampo.es/categories/frescos/pescados-mariscos-y-moluscos/marisco/OC1402?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Seafood.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Seafood_detailed.json"))
    
    FRESH_SQUID_CUTTLEFISH_AND_OTHER_CEPHALOPODS = StaticAisle(name="Fresh squid, cuttlefish and other cephalopods",  url="https://www.compraonline.alcampo.es/categories/frescos/pescados-mariscos-y-moluscos/calamar-sepia-y-otros-cefal%C3%B3podos-frescos/OC1846?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Fresh_squid_cuttlefish_and_other_cephalopods.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fresh_squid_cuttlefish_and_other_cephalopods_detailed.json"))
    
    COD_AND_SALTED_FISH = StaticAisle(name="Cod and salted fish",  url="https://www.compraonline.alcampo.es/categories/frescos/pescados-mariscos-y-moluscos/bacalao-y-salazones/OC1407?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cod_and_salted_fish.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cod_and_salted_fish_detailed.json"))
    
    FRESH_OCTOPUS = StaticAisle(name="Fresh Octopus",  url="https://www.compraonline.alcampo.es/categories/frescos/pescados-mariscos-y-moluscos/pulpo-fresco/OC1409?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Fresh_Octopus.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fresh_Octopus_detailed.json"))
    
    FISHMONGER_BY_THE_CUT = StaticAisle(name="Fishmonger by the cut",  url="https://www.compraonline.alcampo.es/categories/frescos/pescados-mariscos-y-moluscos/pescaderia-al-corte/OC23042021?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Fishmonger_by_the_cut.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fishmonger_by_the_cut_detailed.json"))

    ESSENTIAL_FISH_FOR_YOUR_BARBECUE = StaticAisle(name="Essential fish for your barbecue",  url="https://www.compraonline.alcampo.es/categories/frescos/pescados-mariscos-y-moluscos/pescado-indispensable-para-tu-barbacoa/OCBBQPesc?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Essential_fish_for_your_barbecue.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Essential_fish_for_your_barbecue_detailed.json"))
    

    aisles: Final[List[StaticAisle]] = [FISH, SEAFOOD, FRESH_SQUID_CUTTLEFISH_AND_OTHER_CEPHALOPODS, COD_AND_SALTED_FISH, FRESH_OCTOPUS, 
                                        FISHMONGER_BY_THE_CUT, ESSENTIAL_FISH_FOR_YOUR_BARBECUE]

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
                case "FISH":
                    aisles = [cls.FISH]
                case "SEAFOOD":
                    aisles = [cls.SEAFOOD]
                case "FRESH_SQUID_CUTTLEFISH_AND_OTHER_CEPHALOPODS":
                    aisles = [cls.FRESH_SQUID_CUTTLEFISH_AND_OTHER_CEPHALOPODS]
                case "COD_AND_SALTED_FISH":
                    aisles = [cls.COD_AND_SALTED_FISH]
                case "FRESH_OCTOPUS":
                    aisles = [cls.FRESH_OCTOPUS]
                case "FISHMONGER_BY_THE_CUT":
                    aisles = [cls.FISHMONGER_BY_THE_CUT]
                case "ESSENTIAL_FISH_FOR_YOUR_BARBECUE":
                    aisles = [cls.ESSENTIAL_FISH_FOR_YOUR_BARBECUE]

            
                
        return aisles
    
class AlcampoFrescoesSmokedFoodAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frescoes_Smoked_Food")

    SMOKED = StaticAisle(name="Smoked",  url="https://www.compraonline.alcampo.es/categories/frescos/ahumados-surimis-anchoas-pulpos-y-otros/ahumados/OC1403?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Smoked.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Smoked_detailed.json"))
    
    SURIMIS_AND_EEL_SUBSTITUTES = StaticAisle(name="Surimis and eel substitutes", url="https://www.compraonline.alcampo.es/categories/frescos/ahumados-surimis-anchoas-pulpos-y-otros/surimis-y-suced%C3%A1neos-de-angula/OCSURIYOTROS?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Surimis_and_eel_substitutes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Surimis_and_eel_substitutes_detailed.json"))
    
    COOKED_OCTOPUS_IN_ITS_OWN_JUICE = StaticAisle(name="Cooked octopus in its own juice",  url="https://www.compraonline.alcampo.es/categories/frescos/ahumados-surimis-anchoas-pulpos-y-otros/pulpo-cocido-y-en-su-jugo/OC140503?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cooked_octopus_in_its_own_juice.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cooked_octopus_in_its_own_juice_detailed.json"))
    
    ANCHOVIES = StaticAisle(name="Anchovies",  url="https://www.compraonline.alcampo.es/categories/frescos/ahumados-surimis-anchoas-pulpos-y-otros/anchoas/OC140601?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Anchovies.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Anchovies_detailed.json"))
    
    ANCHOVIES_IN_VINEGAR = StaticAisle(name="Anchovies in vinegar",  url="https://www.compraonline.alcampo.es/categories/frescos/ahumados-surimis-anchoas-pulpos-y-otros/boquerones-en-vinagre/OC140602?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Anchovies_in_vinegar.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Anchovies_in_vinegar_detailed.json"))
    
    MUSSELS = StaticAisle(name="Mussels",  url="https://www.compraonline.alcampo.es/categories/frescos/ahumados-surimis-anchoas-pulpos-y-otros/mejillones/OC14050301?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Mussels.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mussels_detailed.json"))
    
    SEAFOOD = StaticAisle(name="Seafood", url="https://www.compraonline.alcampo.es/categories/frescos/ahumados-surimis-anchoas-pulpos-y-otros/tapas-de-marisco-pescado/OC14050302?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Seafood.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Seafood_detailed.json"))
    
    ROE_AND_SUBSTITUTES = StaticAisle(name="Roe and substitutes",  url="https://www.compraonline.alcampo.es/categories/frescos/ahumados-surimis-anchoas-pulpos-y-otros/huevas-y-suced%C3%A1neos/OC14050303?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Roe_and_substitutes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Roe_and_substitutes_detailed.json"))
    
    SEAFOOD_PATES_AND_CREAMS = StaticAisle(name="Seafood pates and creams",  url="https://www.compraonline.alcampo.es/categories/frescos/ahumados-surimis-anchoas-pulpos-y-otros/pat%C3%A9s-y-cremas-de-marisco/OC14050304?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Seafood_pates_and_creams.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Seafood_pates_and_creams_detailed.json"))
    
    OTHER_CEPHALOPODS = StaticAisle(name="Other cephalopods",  url="https://www.compraonline.alcampo.es/categories/frescos/ahumados-surimis-anchoas-pulpos-y-otros/otros-cefal%C3%B3podos/OCcefalopodos?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Other_cephalopods.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_cephalopods_detailed.json"))
    
    COD_SPECIAL = StaticAisle(name="Cod Special",  url="https://www.compraonline.alcampo.es/categories/frescos/ahumados-surimis-anchoas-pulpos-y-otros/especial-de-bacalao/OCESPBAC?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cod_Special.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cod_Special_detailed.json"))
    

    aisles: Final[List[StaticAisle]] = [SMOKED, SURIMIS_AND_EEL_SUBSTITUTES, COOKED_OCTOPUS_IN_ITS_OWN_JUICE, ANCHOVIES, ANCHOVIES_IN_VINEGAR, MUSSELS, SEAFOOD, ROE_AND_SUBSTITUTES, SEAFOOD_PATES_AND_CREAMS, 
                                        OTHER_CEPHALOPODS, COD_SPECIAL]

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
                case "SMOKED":
                    aisles = [cls.SMOKED]
                case "SURIMIS_AND_EEL_SUBSTITUTES":
                    aisles = [cls.SURIMIS_AND_EEL_SUBSTITUTES]
                case "COOKED_OCTOPUS_IN_ITS_OWN_JUICE":
                    aisles = [cls.COOKED_OCTOPUS_IN_ITS_OWN_JUICE]
                case "ANCHOVIES":
                    aisles = [cls.ANCHOVIES]
                case "ANCHOVIES_IN_VINEGAR":
                    aisles = [cls.ANCHOVIES_IN_VINEGAR]
                case "MUSSELS":
                    aisles = [cls.MUSSELS]
                case "SEAFOOD":
                    aisles = [cls.SEAFOOD]
                case "ROE_AND_SUBSTITUTES":
                    aisles = [cls.ROE_AND_SUBSTITUTES]
                case "SEAFOOD_PATES_AND_CREAMS":
                    aisles = [cls.SEAFOOD_PATES_AND_CREAMS]
                case "OTHER_CEPHALOPODS":
                    aisles = [cls.OTHER_CEPHALOPODS]
                case "COD_SPECIAL":
                    aisles = [cls.COD_SPECIAL]
            
                
        return aisles
    
class AlcampoFrescoesDelicatessenAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frescoes_Delicatessen")

    COOKED_CUT = StaticAisle(name="Cooked cut",  url="https://www.compraonline.alcampo.es/categories/frescos/charcuter%C3%ADa/cocidos-al-corte/OC1781?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cooked_cut.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cooked_cut_detailed.json"))
    
    CURED_CUT = StaticAisle(name="Cured cut", url="https://www.compraonline.alcampo.es/categories/frescos/charcuter%C3%ADa/curados-al-corte/OC178111?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cured_cut.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cured_cut_detailed.json"))
    
    SLICED_COOKED = StaticAisle(name="Sliced cooked",  url="https://www.compraonline.alcampo.es/categories/frescos/charcuter%C3%ADa/loncheado-cocido/OC178112?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Sliced_cooked.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sliced_cooked_detailed.json"))
    
    CURED_SLICED = StaticAisle(name="Cured sliced",  url="https://www.compraonline.alcampo.es/categories/frescos/charcuter%C3%ADa/loncheado-curado/OC178113?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cured_sliced.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cured_sliced_detailed.json"))
    
    SLICED_IBERIAN_HAM = StaticAisle(name="Sliced Iberian ham",  url="https://www.compraonline.alcampo.es/categories/frescos/charcuter%C3%ADa/loncheado-ib%C3%A9rico/OC178114?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Sliced_Iberian_ham.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sliced_Iberian_ham_detailed.json"))
    
    WHOLE_PIECES_OF_SAUSAGE = StaticAisle(name="Whole pieces of sausage",  url="https://www.compraonline.alcampo.es/categories/frescos/charcuter%C3%ADa/embutidos-piezas-enteras/OC178115?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Whole_pieces_of_sausage.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Whole_pieces_of_sausage_detailed.json"))
    
    WHOLE_PIECES_OF_COLD_CUTS = StaticAisle(name="Whole pieces of cold cuts", url="https://www.compraonline.alcampo.es/categories/frescos/charcuter%C3%ADa/fiambres-piezas-enteras/OC178116?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Whole_pieces_of_cold_cuts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Whole_pieces_of_cold_cuts_detailed.json"))
    
    SAUSAGES = StaticAisle(name="Sausages",  url="https://www.compraonline.alcampo.es/categories/frescos/charcuter%C3%ADa/salchichas/OC178117?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Sausages.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sausages_detailed.json"))
    
    TACOS_AND_PIECES_OF_LOIN_AND_HAM = StaticAisle(name="Tacos and pieces of loin and ham",  url="https://www.compraonline.alcampo.es/categories/frescos/charcuter%C3%ADa/tacos-y-piezas-lomo-y-jam%C3%B3n/OC178118?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Tacos_and_pieces_of_loin_and_ham.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tacos_and_pieces_of_loin_and_ham_detailed.json"))
    
    FOIE_GRAS = StaticAisle(name="Foie grass",  url="https://www.compraonline.alcampo.es/categories/frescos/charcuter%C3%ADa/foie-gras-pat%C3%A9s-y-sobrasadas/OC1504?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Foie_gras.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Foie_gras_detailed.json"))
    
    DELICATESSEN_IN_TACOS = StaticAisle(name="Delicatessen in tacos",  url="https://www.compraonline.alcampo.es/categories/frescos/charcuter%C3%ADa/charcuteria-en-taquitos/OC154002?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Delicatessen_in_tacos.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Delicatessen_in_tacos_detailed.json"))
    

    aisles: Final[List[StaticAisle]] = [COOKED_CUT, CURED_CUT, SLICED_COOKED, CURED_SLICED, SLICED_IBERIAN_HAM, WHOLE_PIECES_OF_SAUSAGE, WHOLE_PIECES_OF_COLD_CUTS, SAUSAGES, TACOS_AND_PIECES_OF_LOIN_AND_HAM, 
                                        FOIE_GRAS, DELICATESSEN_IN_TACOS]

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
                case "COOKED_CUT":
                    aisles = [cls.COOKED_CUT]
                case "CURED_CUT":
                    aisles = [cls.CURED_CUT]
                case "SLICED_COOKED":
                    aisles = [cls.SLICED_COOKED]
                case "CURED_SLICED":
                    aisles = [cls.CURED_SLICED]
                case "SLICED_IBERIAN_HAM":
                    aisles = [cls.SLICED_IBERIAN_HAM]
                case "WHOLE_PIECES_OF_SAUSAGE":
                    aisles = [cls.WHOLE_PIECES_OF_SAUSAGE]
                case "WHOLE_PIECES_OF_COLD_CUTS":
                    aisles = [cls.WHOLE_PIECES_OF_COLD_CUTS]
                case "SAUSAGES":
                    aisles = [cls.SAUSAGES]
                case "TACOS_AND_PIECES_OF_LOIN_AND_HAM":
                    aisles = [cls.TACOS_AND_PIECES_OF_LOIN_AND_HAM]
                case "FOIE_GRAS":
                    aisles = [cls.FOIE_GRAS]
                case "DELICATESSEN_IN_TACOS":
                    aisles = [cls.DELICATESSEN_IN_TACOS]
            
                
        return aisles
    
class AlcampoFrescoesHamAndShouldersAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frescoes_Ham")

    IBERIAN_CEBO_HAM = StaticAisle(name="Iberian cebo ham",  url="https://www.compraonline.alcampo.es/categories/frescos/jamones-y-paletas/jam%C3%B3n-cebo-ib%C3%A9rico/OC15100102?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Iberian_cebo_ham.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Iberian_cebo_ham_detailed.json"))
    
    IBERIAN_ACORN_FED_HAM = StaticAisle(name="Iberian acorn-fed ham", url="https://www.compraonline.alcampo.es/categories/frescos/jamones-y-paletas/jam%C3%B3n-bellota-ib%C3%A9rica/OC15100103?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Iberian_acorn_fed_ham.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Iberian_acorn_fed_ham_detailed.json"))
    
    SERRANO_HAM = StaticAisle(name="Serrano ham",  url="https://www.compraonline.alcampo.es/categories/frescos/jamones-y-paletas/jam%C3%B3n-curado-o-serrano/OC15100101?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Serrano_ham.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Serrano_ham_detailed.json"))
    
    LOTS_OF_HAM = StaticAisle(name="Lots of ham",  url="https://www.compraonline.alcampo.es/categories/frescos/jamones-y-paletas/lotes-de-jam%C3%B3n/OC15100107?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Lots_of_ham.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Lots_of_ham_detailed.json"))
    
    IBERIAN_CEBO_SHOULDER = StaticAisle(name="Iberian cebo shoulder",  url="https://www.compraonline.alcampo.es/categories/frescos/jamones-y-paletas/paleta-cebo-ib%C3%A9rica/OC15100105?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Iberian_cebo_shoulder.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Iberian_cebo_shoulder_detailed.json"))
    
    IBERIAN_ACORN_FED_SHOULDER = StaticAisle(name="Iberian acorn-fed shoulder",  url="https://www.compraonline.alcampo.es/categories/frescos/jamones-y-paletas/paleta-bellota-ib%C3%A9rica/OC15100106?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Iberian_acorn_fed_shoulder.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Iberian_acorn_fed_shoulder_detailed.json"))
    
    CURED_OR_MOUNTAIN_SHOULDER = StaticAisle(name="Cured or mountain shoulder", url="https://www.compraonline.alcampo.es/categories/frescos/jamones-y-paletas/paleta-curada-o-serrana/OC15100104?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cured_or_mountain_shoulder.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cured_or_mountain_shoulder_detailed.json"))
    
    
    
    aisles: Final[List[StaticAisle]] = [IBERIAN_CEBO_HAM, IBERIAN_ACORN_FED_HAM, SERRANO_HAM, LOTS_OF_HAM, IBERIAN_CEBO_SHOULDER, IBERIAN_ACORN_FED_SHOULDER, CURED_OR_MOUNTAIN_SHOULDER]

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
                case "IBERIAN_CEBO_HAM":
                    aisles = [cls.IBERIAN_CEBO_HAM]
                case "IBERIAN_ACORN_FED_HAM":
                    aisles = [cls.IBERIAN_ACORN_FED_HAM]
                case "SERRANO_HAM":
                    aisles = [cls.SERRANO_HAM]
                case "LOTS_OF_HAM":
                    aisles = [cls.LOTS_OF_HAM]
                case "IBERIAN_CEBO_SHOULDER":
                    aisles = [cls.IBERIAN_CEBO_SHOULDER]
                case "IBERIAN_ACORN_FED_SHOULDER":
                    aisles = [cls.IBERIAN_ACORN_FED_SHOULDER]
                case "CURED_OR_MOUNTAIN_SHOULDER":
                    aisles = [cls.CURED_OR_MOUNTAIN_SHOULDER]
               
                
        return aisles
    
class AlcampoFrescoesCheesesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frescoes_Cheese")

    COUNTER_CHEESES_BY_THE_CUT = StaticAisle(name="Counter cheeses by the cut",  url="https://www.compraonline.alcampo.es/categories/frescos/quesos/quesos-mostrador-al-corte/OCQueso?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Counter_cheeses_by_the_cut.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Counter_cheeses_by_the_cut_detailed.json"))
    
    SLICED_CHEESE = StaticAisle(name="Sliced cheese", url="https://www.compraonline.alcampo.es/categories/frescos/quesos/queso-en-lonchas/OC3504?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Sliced_cheese.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sliced_cheese_detailed.json"))
    
    GRATED_CHEESE_AND_SALAD = StaticAisle(name="Grated cheese and salad",  url="https://www.compraonline.alcampo.es/categories/frescos/quesos/queso-rallado-y-ensalada/OC3505?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Grated_cheese_and_salad.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Grated_cheese_and_salad_detailed.json"))
    
    SPREADS_AND_CHEESE_CREAMS = StaticAisle(name="Spreads and cheese creams",  url="https://www.compraonline.alcampo.es/categories/frescos/quesos/untables-y-cremas-de-queso/OC3506?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Spreads_and_cheese_creams.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Spreads_and_cheese_creams_detailed.json"))
    
    FRESH_CHEESE = StaticAisle(name="Fresh cheese",  url="https://www.compraonline.alcampo.es/categories/frescos/quesos/queso-fresco/OC3503?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Fresh_cheese.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fresh_cheese_detailed.json"))
    
    PURE_SHEEP_CHEESE = StaticAisle(name="Pure sheep cheese",  url="https://www.compraonline.alcampo.es/categories/frescos/quesos/queso-puro-oveja/OC350101?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Pure_sheep_cheese.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pure_sheep_cheese_detailed.json"))
    
    SEMI_CURED_MIXED_CHEESE = StaticAisle(name="Semi-cured mixed cheese", url="https://www.compraonline.alcampo.es/categories/frescos/quesos/queso-mezcla-semicurado/OC350103?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Semi_cured_mixed_cheese.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Semi_cured_mixed_cheese_detailed.json"))
    
    CURED_MIXED_CHEESE = StaticAisle(name="Cured mixed cheese",  url="https://www.compraonline.alcampo.es/categories/frescos/quesos/queso-mezcla-curado/OC350102?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cured_mixed_cheese.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cured_mixed_cheese_detailed.json"))
    
    GOAT_CHEESE = StaticAisle(name="Goat cheese", url="https://www.compraonline.alcampo.es/categories/frescos/quesos/queso-de-cabra/OC350104?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Goat_cheese.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Goat_cheese_detailed.json"))
    
    SOFT_CHEESE = StaticAisle(name="Soft cheese",  url="https://www.compraonline.alcampo.es/categories/frescos/quesos/queso-tierno/OC350105?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Soft_cheese.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Soft_cheese_detailed.json"))
    
    SPECIALTY_CHEESES = StaticAisle(name="Specialty cheeses",  url="https://www.compraonline.alcampo.es/categories/frescos/quesos/quesos-especialidades/OC3502?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Specialty_cheeses.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Specialty_cheeses_detailed.json"))
    
    BOARDS_AND_CUTS = StaticAisle(name="Boards and cuts",  url="https://www.compraonline.alcampo.es/categories/frescos/quesos/tablas-y-cortados/OC350207?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Boards_and_cuts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Boards_and_cuts_detailed.json"))
    
    CHEESE_IN_PORTIONS = StaticAisle(name="Cheese in portions",  url="https://www.compraonline.alcampo.es/categories/frescos/quesos/queso-en-porciones/OC350601?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cheese_in_portions.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cheese_in_portions_detailed.json"))
    
    QUINCE_AND_CHEESECAKE = StaticAisle(name="Quince and cheesecake", url="https://www.compraonline.alcampo.es/categories/frescos/quesos/membrillo-y-tarta-de-queso/OCMembrilloTartaQueso?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Quince_and_cheesecake.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Quince_and_cheesecake_detailed.json"))
    
    REGIONAL_CHEESES = StaticAisle(name="Regional cheeses",  url="https://www.compraonline.alcampo.es/categories/frescos/quesos/quesos-regionales/OC350106?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Regional_cheeses.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Regional_cheeses_detailed.json"))
    
    ORGANIC_CHEESES = StaticAisle(name="Organic Cheeses", url="https://www.compraonline.alcampo.es/categories/frescos/quesos/quesos-ecol%C3%B3gicos/OC26112021106Bis?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Cheeses.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Cheeses_detailed.json"))
    
    
    
    aisles: Final[List[StaticAisle]] = [COUNTER_CHEESES_BY_THE_CUT, SLICED_CHEESE, GRATED_CHEESE_AND_SALAD, SPREADS_AND_CHEESE_CREAMS, FRESH_CHEESE, PURE_SHEEP_CHEESE, SEMI_CURED_MIXED_CHEESE, CURED_MIXED_CHEESE,
                                        GOAT_CHEESE, SOFT_CHEESE, SPECIALTY_CHEESES, BOARDS_AND_CUTS, CHEESE_IN_PORTIONS, QUINCE_AND_CHEESECAKE, REGIONAL_CHEESES, ORGANIC_CHEESES]

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
                case "COUNTER_CHEESES_BY_THE_CUT":
                    aisles = [cls.COUNTER_CHEESES_BY_THE_CUT]
                case "SLICED_CHEESE":
                    aisles = [cls.SLICED_CHEESE]
                case "GRATED_CHEESE_AND_SALAD":
                    aisles = [cls.GRATED_CHEESE_AND_SALAD]
                case "SPREADS_AND_CHEESE_CREAMS":
                    aisles = [cls.SPREADS_AND_CHEESE_CREAMS]
                case "FRESH_CHEESE":
                    aisles = [cls.FRESH_CHEESE]
                case "PURE_SHEEP_CHEESE":
                    aisles = [cls.PURE_SHEEP_CHEESE]
                case "SEMI_CURED_MIXED_CHEESE":
                    aisles = [cls.SEMI_CURED_MIXED_CHEESE]
                case "CURED_MIXED_CHEESE":
                    aisles = [cls.CURED_MIXED_CHEESE]
                case "GOAT_CHEESE":
                    aisles = [cls.GOAT_CHEESE]
                case "SOFT_CHEESE":
                    aisles = [cls.SOFT_CHEESE]
                case "SPECIALTY_CHEESES":
                    aisles = [cls.SPECIALTY_CHEESES]
                case "BOARDS_AND_CUTS":
                    aisles = [cls.BOARDS_AND_CUTS]
                case "CHEESE_IN_PORTIONS":
                    aisles = [cls.CHEESE_IN_PORTIONS]
                case "QUINCE_AND_CHEESECAKE":
                    aisles = [cls.QUINCE_AND_CHEESECAKE]
                case "REGIONAL_CHEESES":
                    aisles = [cls.REGIONAL_CHEESES]
                case "ORGANIC_CHEESES":
                    aisles = [cls.ORGANIC_CHEESES]
               
                
        return aisles
    
class AlcampoFrescoesBakeryAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frescoes_Bakery")

    EMPANADAS = StaticAisle(name="Empanadas",  url="https://www.compraonline.alcampo.es/categories/frescos/panader%C3%ADa/empanadas/OC12818?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Empanadas.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Empanadas_detailed.json"))
    
    LOAVES_CIABATTAS_AND_BAGUETTES = StaticAisle(name="Loaves, ciabattas and baguettes", url="https://www.compraonline.alcampo.es/categories/frescos/panader%C3%ADa/barras-chapatas-y-baguettes/OC12811?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Loaves_ciabattas_and_baguettes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Loaves_ciabattas_and_baguettes_detailed.json"))
    
    BREADS_AND_LOAVES = StaticAisle(name="Breads and loaves",  url="https://www.compraonline.alcampo.es/categories/frescos/panader%C3%ADa/panes-y-hogazas/OC12813?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Breads_and_loaves.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Breads_and_loaves_detailed.json"))
    
    WHOLE_WHEAT_AND_UNSALTED_BREAD = StaticAisle(name="Whole wheat and unsalted bread",  url="https://www.compraonline.alcampo.es/categories/frescos/panader%C3%ADa/pan-integral-y-sin-sal/OC12814?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Whole_wheat_and_unsalted_bread.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Whole_wheat_and_unsalted_bread_detailed.json"))
    
    SLICED_AND_SLICED_BRED = StaticAisle(name="Sliced and Sliced bred",  url="https://www.compraonline.alcampo.es/categories/frescos/panader%C3%ADa/pan-cortado-y-de-molde/OC12815?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Sliced_and_Sliced_bred.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sliced_and_Sliced_bred_detailed.json"))
    
    SMALL_FORMATS = StaticAisle(name="Small Formats",  url="https://www.compraonline.alcampo.es/categories/frescos/panader%C3%ADa/peque%C3%B1os-formatos/OC12816?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Small_Formats.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Small_Formats_detailed.json"))
    
    BREAD_WITH_CEREALS = StaticAisle(name="Bread with cereals", url="https://www.compraonline.alcampo.es/categories/frescos/panader%C3%ADa/pan-con-cereales/OC12810?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Bread_with_cereals.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Bread_with_cereals_detailed.json"))
    
    TARTLETS_AND_TOASTED_BREAD = StaticAisle(name="tartlets and toasted bread",  url="https://www.compraonline.alcampo.es/categories/frescos/panader%C3%ADa/volovanes-tartaletas-y-pan-tostado/OC12819?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "tartlets_and_toasted_bread.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "tartlets_and_toasted_bread_detailed.json"))
    
    FRESH_YEAST = StaticAisle(name="Fresh yeast", url="https://www.compraonline.alcampo.es/categories/frescos/panader%C3%ADa/levadura-fresca/OC128111?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Fresh_yeast.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fresh_yeast_detailed.json"))
    
    SALTY_SNACKS = StaticAisle(name="Salty snacks",  url="https://www.compraonline.alcampo.es/categories/frescos/panader%C3%ADa/snacks-salados/OC12817?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Salty_snacks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Salty_snacks_detailed.json"))
    

    aisles: Final[List[StaticAisle]] = [EMPANADAS, LOAVES_CIABATTAS_AND_BAGUETTES, BREADS_AND_LOAVES, WHOLE_WHEAT_AND_UNSALTED_BREAD, SLICED_AND_SLICED_BRED, SMALL_FORMATS, BREAD_WITH_CEREALS, 
                                        TARTLETS_AND_TOASTED_BREAD, FRESH_YEAST, SALTY_SNACKS]

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
                case "EMPANADAS":
                    aisles = [cls.EMPANADAS]
                case "LOAVES_CIABATTAS_AND_BAGUETTES":
                    aisles = [cls.LOAVES_CIABATTAS_AND_BAGUETTES]
                case "BREADS_AND_LOAVES":
                    aisles = [cls.BREADS_AND_LOAVES]
                case "WHOLE_WHEAT_AND_UNSALTED_BREAD":
                    aisles = [cls.WHOLE_WHEAT_AND_UNSALTED_BREAD]
                case "SLICED_AND_SLICED_BRED":
                    aisles = [cls.SLICED_AND_SLICED_BRED]
                case "SMALL_FORMATS":
                    aisles = [cls.SMALL_FORMATS]
                case "BREAD_WITH_CEREALS":
                    aisles = [cls.BREAD_WITH_CEREALS]
                case "TARTLETS_AND_TOASTED_BREAD":
                    aisles = [cls.TARTLETS_AND_TOASTED_BREAD]
                case "FRESH_YEAST":
                    aisles = [cls.FRESH_YEAST]
                case "SALTY_SNACKS":
                    aisles = [cls.SALTY_SNACKS]
              
               
                
        return aisles
    
class AlcampoFrescoesPastryAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frescoes_Pastry")

    CAKES_PASTRIES_AND_TEA_CAKE = StaticAisle(name="Cakes, pastries and tea cake",  url="https://www.compraonline.alcampo.es/categories/frescos/pasteler%C3%ADa/tartas-pasteles-y-pastas-de-t%C3%A9/OC12821?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cakes_pastries_and_tea_cake.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cakes_pastries_and_tea_cake_detailed.json"))
    
    MUFFINS_CUPCAKES_AND_CAKES = StaticAisle(name="Muffins, cupcakes and cakes", url="https://www.compraonline.alcampo.es/categories/frescos/pasteler%C3%ADa/muffins-magdalenas-y-bizcochos/OC12822?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Muffins_cupcakes_and_cakes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Muffins_cupcakes_and_cakes_detailed.json"))
    
    CROISSANTS_AND_NEAPOLITAN_PASTRIES = StaticAisle(name="croissants and Neapolitan pastries",  url="https://www.compraonline.alcampo.es/categories/frescos/pasteler%C3%ADa/palmeras-croissants-y-napolitanas/OC12825?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "croissants_and_Neapolitan_pastries.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "croissants_and_Neapolitan_pastries_detailed.json"))
    
    DOUGHNUTS_AND_DONUTS = StaticAisle(name="Doughnuts and donuts",  url="https://www.compraonline.alcampo.es/categories/frescos/pasteler%C3%ADa/rosquillas-y-berlinas/OC12823?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Doughnuts_and_donuts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Doughnuts_and_donuts_detailed.json"))
    
    OTHER_BUNS_AND_PUFF_PASTRIES = StaticAisle(name="Other buns and puff pastries",  url="https://www.compraonline.alcampo.es/categories/frescos/pasteler%C3%ADa/otros-bollos-y-hojaldres/OC12827?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Other_buns_and_puff_pastries.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_buns_and_puff_pastries_detailed.json"))
    
    REGIONAL_PRODUCTS = StaticAisle(name="Regional products",  url="https://www.compraonline.alcampo.es/categories/frescos/pasteler%C3%ADa/productos-regionales/OC12829?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Regional_products.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Regional_products_detailed.json"))
    
    FATHERS_DAY = StaticAisle(name="Father's Day", url="https://www.compraonline.alcampo.es/categories/frescos/pasteler%C3%ADa/d%C3%ADa-del-padre/OCPASTDIAPADR?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Fathers_Day.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fathers_Day_detailed.json"))
    
    MOTHERS_DAY = StaticAisle(name="Mother's Day", url="https://www.compraonline.alcampo.es/categories/frescos/pasteler%C3%ADa/d%C3%ADa-de-la-madre/OCPASTDIAMADR?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Mothers_Day.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mothers_Day_detailed.json"))
    
    

    aisles: Final[List[StaticAisle]] = [CAKES_PASTRIES_AND_TEA_CAKE, MUFFINS_CUPCAKES_AND_CAKES, CROISSANTS_AND_NEAPOLITAN_PASTRIES, DOUGHNUTS_AND_DONUTS, OTHER_BUNS_AND_PUFF_PASTRIES, REGIONAL_PRODUCTS, FATHERS_DAY, MOTHERS_DAY]

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
                case "CAKES_PASTRIES_AND_TEA_CAKE":
                    aisles = [cls.CAKES_PASTRIES_AND_TEA_CAKE]
                case "MUFFINS_CUPCAKES_AND_CAKES":
                    aisles = [cls.MUFFINS_CUPCAKES_AND_CAKES]
                case "CROISSANTS_AND_NEAPOLITAN_PASTRIES":
                    aisles = [cls.CROISSANTS_AND_NEAPOLITAN_PASTRIES]
                case "DOUGHNUTS_AND_DONUTS":
                    aisles = [cls.DOUGHNUTS_AND_DONUTS]
                case "OTHER_BUNS_AND_PUFF_PASTRIES":
                    aisles = [cls.OTHER_BUNS_AND_PUFF_PASTRIES]
                case "REGIONAL_PRODUCTS":
                    aisles = [cls.REGIONAL_PRODUCTS]
                case "FATHERS_DAY":
                    aisles = [cls.FATHERS_DAY]
                case "MOTHERS_DAY":
                    aisles = [cls.MOTHERS_DAY]
           
        return aisles

#Milk

class AlcampoMilkMilkAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Milk")

    SEMI_SKIMMED_MILK = StaticAisle(name="Semi-skimmed milk",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/leche/leche-semidesnatada/OCSemidesnatada?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Semi_skimmed_milk.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Semi_skimmed_milk_detailed.json"))
    
    WHOLE_MILK = StaticAisle(name="Whole milk", url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/leche/leche-entera/OCEntera?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Whole_milk.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Whole_milk_detailed.json"))
    
    SKIMMED_MILK = StaticAisle(name="Skimmed milk",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/leche/leche-desnatada/OCDesnatada?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Skimmed_milk.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Skimmed_milk_detailed.json"))
    
    LOW_OR_LACTOSE_FREE_MILK = StaticAisle(name="Low or lactose-free milk",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/leche/leche-baja-o-sin-lactosa/OCSinlactosa?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Low_or_lactose_free_milk.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Low_or_lactose_free_milk_detailed.json"))
    
    MILK_WITH_CALCIUM = StaticAisle(name="Milk with calcium",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/leche/leche-con-calcio/OCLechecalcio?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Milk_with_calcium.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Milk_with_calcium_detailed.json"))
    
    FRESH_MILK = StaticAisle(name="Fresh milk",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/leche/leche-fresca/OCFresca?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Fresh_milk.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fresh_milk_detailed.json"))
    
    SHEEP_OR_GOAT_MILK = StaticAisle(name="Sheep or goat milk", url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/leche/leche-oveja-o-cabra/OCLecheoveja?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Sheep_or_goat_milk.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sheep_or_goat_milk_detailed.json"))
    
    OMEGA_3DAIRY_PREPARATIONS = StaticAisle(name="Omega 3 dairy preparations",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/leche/preparados-l%C3%A1cteos-omega-3/OCPreparadosomega3leche?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Omega_3dairy_preparations.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Omega_3dairy_preparations_detailed.json"))
    
    CHILDREN_ENERGY_AND_GROWTH = StaticAisle(name="Children, Energy and Growth",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/leche/infantil-energ%C3%ADa-y-crecimiento/OCPreparadoinfantilleche?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Children_Energy_and_Growth.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Children_Energy_and_Growth_detailed.json"))
    
    FIBER_AND_CHOLESTEROL_CONTROL_PREPARATIONS = StaticAisle(name="Fiber and cholesterol control preparations", url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/leche/preparados-fibra-y-control-colesterol/OCPreparadofibracolesterolleche?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Fiber_and_cholesterol_control_preparations.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fiber_and_cholesterol_control_preparations_detailed.json"))
    
    ORGANIC_MILK = StaticAisle(name="Organic Milk", url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/leche/leche-ecol%C3%B3gica/OClecheeco?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Milk.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Milk_detailed.json"))
    
    

    aisles: Final[List[StaticAisle]] = [SEMI_SKIMMED_MILK, WHOLE_MILK, SKIMMED_MILK, LOW_OR_LACTOSE_FREE_MILK, MILK_WITH_CALCIUM, FRESH_MILK, SHEEP_OR_GOAT_MILK, OMEGA_3DAIRY_PREPARATIONS, CHILDREN_ENERGY_AND_GROWTH,
                                        FIBER_AND_CHOLESTEROL_CONTROL_PREPARATIONS, ORGANIC_MILK]

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
                case "SEMI_SKIMMED_MILK":
                    aisles = [cls.SEMI_SKIMMED_MILK]
                case "WHOLE_MILK":
                    aisles = [cls.WHOLE_MILK]
                case "SKIMMED_MILK":
                    aisles = [cls.SKIMMED_MILK]
                case "LOW_OR_LACTOSE_FREE_MILK":
                    aisles = [cls.LOW_OR_LACTOSE_FREE_MILK]
                case "MILK_WITH_CALCIUM":
                    aisles = [cls.MILK_WITH_CALCIUM]
                case "FRESH_MILK":
                    aisles = [cls.FRESH_MILK]
                case "SHEEP_OR_GOAT_MILK":
                    aisles = [cls.SHEEP_OR_GOAT_MILK]
                case "OMEGA_3DAIRY_PREPARATIONS":
                    aisles = [cls.OMEGA_3DAIRY_PREPARATIONS]
                case "CHILDREN_ENERGY_AND_GROWTH":
                    aisles = [cls.CHILDREN_ENERGY_AND_GROWTH]
                case "FIBER_AND_CHOLESTEROL_CONTROL_PREPARATIONS":
                    aisles = [cls.FIBER_AND_CHOLESTEROL_CONTROL_PREPARATIONS]
                case "ORGANIC_MILK":
                    aisles = [cls.ORGANIC_MILK]
                
           
        return aisles
    
class AlcampoMilkVegetablesDrinksAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Milk_Vegetables_drinks")

    SOY_DRINKS = StaticAisle(name="Soy drinks",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/bebidas-vegetales/bebidas-de-soja/OC160314?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Soy_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Soy_drinks_detailed.json"))
    
    OAT_DRINKS = StaticAisle(name="Oat drinks", url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/bebidas-vegetales/bebidas-de-avena/OC16031001?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Oat_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Oat_drinks_detailed.json"))
    
    RICE_DRINKS = StaticAisle(name="Rice drinks",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/bebidas-vegetales/bebidas-de-arroz/OC16031002?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Rice_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Rice_drinks_detailed.json"))
    
    ALMOND_DRINKS = StaticAisle(name="Almond drinks",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/bebidas-vegetales/bebidas-de-almendra/OC16031003?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Almond_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Almond_drinks_detailed.json"))
    
    OTHERS = StaticAisle(name="Others",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/bebidas-vegetales/otras/OC0911202125?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Others_detailed.json"))
    

    aisles: Final[List[StaticAisle]] = [SOY_DRINKS, OAT_DRINKS, RICE_DRINKS, ALMOND_DRINKS, OTHERS]

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
                case "SOY_DRINKS":
                    aisles = [cls.SOY_DRINKS]
                case "OAT_DRINKS":
                    aisles = [cls.OAT_DRINKS]
                case "RICE_DRINKS":
                    aisles = [cls.RICE_DRINKS]
                case "ALMOND_DRINKS":
                    aisles = [cls.ALMOND_DRINKS]
                case "OTHERS":
                    aisles = [cls.OTHERS]
        
        return aisles
    
class AlcampoMilkDairyPreparationAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Milk_Dairy_preparation")

    OMEGA_3DAIRY_PREPARATIONS = StaticAisle(name="Omega 3 dairy preparations",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/preparado-l%C3%A1cteo/preparados-l%C3%A1cteos-omega-3/OCPreparadosomega3?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Omega_3dairy_preparations.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Omega_3dairy_preparations_detailed.json"))
    
    CHILDREN_ENERGY_AND_GROWTH = StaticAisle(name="Children, Energy and Growth", url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/preparado-l%C3%A1cteo/infantil-energ%C3%ADa-y-crecimiento/OCPreparadoinfantil?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Children_Energy_and_Growth.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Children_Energy_and_Growth_detailed.json"))
    
    FIBER_AND_CHOLESTEROL_CONTROL_PREPARATIONS = StaticAisle(name="Fiber and cholesterol control preparations",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/preparado-l%C3%A1cteo/preparados-fibra-y-control-colesterol/OCPreparadofibra?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Fiber_and_cholesterol_control_preparations.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fiber_and_cholesterol_control_preparations_detailed.json"))
  
    
    aisles: Final[List[StaticAisle]] = [OMEGA_3DAIRY_PREPARATIONS, CHILDREN_ENERGY_AND_GROWTH, FIBER_AND_CHOLESTEROL_CONTROL_PREPARATIONS]

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
                case "OMEGA_3DAIRY_PREPARATIONS":
                    aisles = [cls.OMEGA_3DAIRY_PREPARATIONS]
                case "CHILDREN_ENERGY_AND_GROWTH":
                    aisles = [cls.CHILDREN_ENERGY_AND_GROWTH]
                case "FIBER_AND_CHOLESTEROL_CONTROL_PREPARATIONS":
                    aisles = [cls.FIBER_AND_CHOLESTEROL_CONTROL_PREPARATIONS]
                
                
        return aisles
    
class AlcampoMilkEggsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Milk_Eggs")

    EGGS_BY_SIZE = StaticAisle(name="Eggs by size",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/huevos/huevos-por-tama%C3%B1os/OCHuevoportallas?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Eggs_by_size.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Eggs_by_size_detailed.json"))
    
    FREE_RANGE_EGGS = StaticAisle(name="Free-range eggs", url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/huevos/huevos-de-gallinas-camperas/OCHuevocampero?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Free_range_eggs.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Free_range_eggs_detailed.json"))
    
    EGGS_FROM_LOOSE = StaticAisle(name="Eggs from loose",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/huevos/huevos-de-gallinas-sueltas-en-el-gallinero/OCHuevogallinero?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Eggs_from_loose.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Eggs_from_loose_detailed.json"))
  
    EGGS_FROM_HENS = StaticAisle(name="Eggs from hens",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/huevos/huevos-de-gallinas-en-jaulas-acondicionadas/OCHuevojaulasacon?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Eggs_from_hens.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Eggs_from_hens_detailed.json"))
    
    QUAIL_AND_SPECIAL_EGGS = StaticAisle(name="Quail and special eggs", url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/huevos/huevos-codorniz-y-especiales/OCHuevosespeciales?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Quail_and_special_eggs.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Quail_and_special_eggs_detailed.json"))
    
    BOILED_EGGS_AND_EGG_WHITES = StaticAisle(name="Boiled Eggs and Egg Whites",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/huevos/huevos-cocidos-y-claras/OCCocidos?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Boiled_Eggs_and_Egg_Whites.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Boiled_Eggs_and_Egg_Whites_detailed.json"))
  
    SPUN_EGG = StaticAisle(name="Spun Egg",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/huevos/huevo-hilado/OCHuevohilado?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Spun_Egg.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Spun_Egg_detailed.json"))
  
    
    aisles: Final[List[StaticAisle]] = [EGGS_BY_SIZE, FREE_RANGE_EGGS, EGGS_FROM_LOOSE, EGGS_FROM_HENS, QUAIL_AND_SPECIAL_EGGS, BOILED_EGGS_AND_EGG_WHITES, SPUN_EGG]

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
                case "EGGS_BY_SIZE":
                    aisles = [cls.EGGS_BY_SIZE]
                case "FREE_RANGE_EGGS":
                    aisles = [cls.FREE_RANGE_EGGS]
                case "EGGS_FROM_LOOSE":
                    aisles = [cls.EGGS_FROM_LOOSE]
                case "EGGS_FROM_HENS":
                    aisles = [cls.EGGS_FROM_HENS]
                case "QUAIL_AND_SPECIAL_EGGS":
                    aisles = [cls.QUAIL_AND_SPECIAL_EGGS]
                case "BOILED_EGGS_AND_EGG_WHITES":
                    aisles = [cls.BOILED_EGGS_AND_EGG_WHITES]
                case "SPUN_EGG":
                    aisles = [cls.SPUN_EGG]
                
                
        return aisles
    
class AlcampoMilkYoghurtAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Milk_Yoghurt")

    BIFIDUS_YOGURTS = StaticAisle(name="Bifidus Yogurts",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/yogures-b%C3%ADfidus-y-l-casei/yogures-bifidus/OC160104?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Bifidus_Yogurts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Bifidus_Yogurts_detailed.json"))
    
    LCASEI = StaticAisle(name="L.Casei", url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/yogures-b%C3%ADfidus-y-l-casei/l-casei/OC160105?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "LCasei.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "LCasei_detailed.json"))
    
    FUNCTIONAL_YOGURTS = StaticAisle(name="Functional Yogurts",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/yogures-b%C3%ADfidus-y-l-casei/yogures-funcionales/OC160106?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Functional_Yogurts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Functional_Yogurts_detailed.json"))
  
    NATURAL_YOGURTS = StaticAisle(name="Natural Yogurts",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/yogures-b%C3%ADfidus-y-l-casei/yogures-naturales/OC160101?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Natural_Yogurts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Natural_Yogurts_detailed.json"))
    
    FLAVORED_YOGURTS = StaticAisle(name="Flavored Yogurts", url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/yogures-b%C3%ADfidus-y-l-casei/yogures-sabores/OC160102?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Flavored_Yogurts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Flavored_Yogurts_detailed.json"))
    
    GREEK_AND_CREAMY_YOGURTS = StaticAisle(name="Greek and creamy yogurts",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/yogures-b%C3%ADfidus-y-l-casei/yogures-griegos-y-cremosos/OC160108?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Greek_and_creamy_yogurts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Greek_and_creamy_yogurts_detailed.json"))
  
    SKIMMED_YOGURTS = StaticAisle(name="Skimmed Yogurts",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/yogures-b%C3%ADfidus-y-l-casei/yogures-desnatados/OC160103?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Skimmed_Yogurts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Skimmed_Yogurts_detailed.json"))
  
    YOGURTS_WITH_SNACKS = StaticAisle(name="Yogurts with snacks",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/yogures-b%C3%ADfidus-y-l-casei/yogures-con-snacks/OC160110?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Yogurts_with_snacks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Yogurts_with_snacks_detailed.json"))
    
    GOAT = StaticAisle(name="Goat",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/yogures-b%C3%ADfidus-y-l-casei/yogures-de-cabra-oveja/OC160129?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Goat.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Goat_detailed.json"))
  
    LIQUID_YOGURTS = StaticAisle(name="Liquid Yogurts",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/yogures-b%C3%ADfidus-y-l-casei/yogures-l%C3%ADquidos/OC160134?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Liquid_Yogurts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Liquid_Yogurts_detailed.json"))
  
    ORGANIC_YOGURTS = StaticAisle(name="Organic Yogurts",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/yogures-b%C3%ADfidus-y-l-casei/yogures-ecol%C3%B3gicos/OC1164866351?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Yogurts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Yogurts_detailed.json"))
  
    
    aisles: Final[List[StaticAisle]] = [BIFIDUS_YOGURTS, LCASEI, FUNCTIONAL_YOGURTS, NATURAL_YOGURTS, FLAVORED_YOGURTS, GREEK_AND_CREAMY_YOGURTS, SKIMMED_YOGURTS, YOGURTS_WITH_SNACKS, GOAT, LIQUID_YOGURTS, 
                                        ORGANIC_YOGURTS]

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
                case "BIFIDUS_YOGURTS":
                    aisles = [cls.BIFIDUS_YOGURTS]
                case "LCASEI":
                    aisles = [cls.LCASEI]
                case "FUNCTIONAL_YOGURTS":
                    aisles = [cls.FUNCTIONAL_YOGURTS]
                case "NATURAL_YOGURTS":
                    aisles = [cls.NATURAL_YOGURTS]
                case "FLAVORED_YOGURTS":
                    aisles = [cls.FLAVORED_YOGURTS]
                case "GREEK_AND_CREAMY_YOGURTS":
                    aisles = [cls.GREEK_AND_CREAMY_YOGURTS]
                case "SKIMMED_YOGURTS":
                    aisles = [cls.SKIMMED_YOGURTS]
                case "YOGURTS_WITH_SNACKS":
                    aisles = [cls.YOGURTS_WITH_SNACKS]
                case "GOAT":
                    aisles = [cls.GOAT]
                case "LIQUID_YOGURTS":
                    aisles = [cls.LIQUID_YOGURTS]
                case "ORGANIC_YOGURTS":
                    aisles = [cls.ORGANIC_YOGURTS]
                
                
        return aisles
    
class AlcampoMilkDairyDessertsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Milk_Dairy_desserts")

    PETIT = StaticAisle(name="Petit or Children",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/postres-l%C3%A1cteos/petit-o-infantiles/OC160201?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Petit.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Petit_detailed.json"))
    
    CUSTARD = StaticAisle(name="Custard", url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/postres-l%C3%A1cteos/natillas/OC160202?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Custard.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Custard_detailed.json"))
    
    FLAN = StaticAisle(name="Flan",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/postres-l%C3%A1cteos/flan-crema-catalana-y-otros/OC160210?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Flan.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Flan_detailed.json"))
  
    GELATIN = StaticAisle(name="Gelatin",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/postres-l%C3%A1cteos/gelatina/OC160212?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Gelatin.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Gelatin_detailed.json"))
    
    CUP_AND_MOUSSE = StaticAisle(name="Cup and Mousse", url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/postres-l%C3%A1cteos/copa-y-mousse/OC160213?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cup_and_Mousse.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cup_and_Mousse_detailed.json"))
    
    ITALIAN_DESSERTS = StaticAisle(name="Italian desserts",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/postres-l%C3%A1cteos/postres-italianos/OC160214?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Italian_desserts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Italian_desserts_detailed.json"))
  
    OTHER_DESSERTS = StaticAisle(name="Other desserts",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/postres-l%C3%A1cteos/otros-postres/OC160215?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Other_desserts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_desserts_detailed.json"))
  
    SOY_ALMOND_OAT = StaticAisle(name="Soy, almond, oat",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/postres-l%C3%A1cteos/soja-almendra-avena/OC160109?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Soy_almond_oat.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Soy_almond_oat_detailed.json"))
    
    KEFIR = StaticAisle(name="Kefir",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/postres-l%C3%A1cteos/k%C3%A9fir/OC160211?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Kefir.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Kefir_detailed.json"))
  
    PREPARED_CHOCOLATES = StaticAisle(name="Prepared chocolates",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/postres/chocolates-preparados/OC160406?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Prepared_chocolates.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Prepared_chocolates_detailed.json"))
  
    RICE_PUDDING_AND_CURD = StaticAisle(name="Rice pudding and curd",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/postres/arroz-con-leche-y-cuajada/OCArrozycuajada?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Rice_pudding_and_curd.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Rice_pudding_and_curd_detailed.json"))
  
    aisles: Final[List[StaticAisle]] = [PETIT, CUSTARD, FLAN, GELATIN, CUP_AND_MOUSSE, ITALIAN_DESSERTS, OTHER_DESSERTS, SOY_ALMOND_OAT, KEFIR , PREPARED_CHOCOLATES, RICE_PUDDING_AND_CURD]

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
                case "PETIT":
                    aisles = [cls.PETIT]
                case "CUSTARD":
                    aisles = [cls.CUSTARD]
                case "FLAN":
                    aisles = [cls.FLAN]
                case "GELATIN":
                    aisles = [cls.GELATIN]
                case "CUP_AND_MOUSSE":
                    aisles = [cls.CUP_AND_MOUSSE]
                case "ITALIAN_DESSERTS":
                    aisles = [cls.ITALIAN_DESSERTS]
                case "OTHER_DESSERTS":
                    aisles = [cls.OTHER_DESSERTS]
                case "SOY_ALMOND_OAT":
                    aisles = [cls.SOY_ALMOND_OAT]
                case "KEFIR":
                    aisles = [cls.KEFIR]
                case "PREPARED_CHOCOLATES":
                    aisles = [cls.PREPARED_CHOCOLATES]
                case "RICE_PUDDING_AND_CURD":
                    aisles = [cls.RICE_PUDDING_AND_CURD]
               
        return aisles
    
class AlcampoMilkButterAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Milk_Butter")

    SALTED_BUTTER = StaticAisle(name="Salted Butter",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/mantequilla/mantequilla-con-sal/OC160601?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Salted_Butter.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Salted_Butter_detailed.json"))
    
    UNSALTED_BUTTER = StaticAisle(name="Unsalted Butter", url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/mantequilla/mantequilla-sin-sal/OC160602?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Unsalted_Butter.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Unsalted_Butter_detailed.json"))
    
    SPECIAL_BUTTERS = StaticAisle(name="Special Butters",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/mantequilla/mantequillas-especiales/OC160603?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Special_Butters.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Special_Butters_detailed.json"))
  
    ORGANIC_BUTTERS = StaticAisle(name="Organic Butters",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/mantequilla/mantequillas-ecol%C3%B3gicas/OC1164869540?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Butters.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Butters_detailed.json"))
  
    aisles: Final[List[StaticAisle]] = [SALTED_BUTTER, UNSALTED_BUTTER, SPECIAL_BUTTERS, ORGANIC_BUTTERS]

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
                case "SALTED_BUTTER":
                    aisles = [cls.SALTED_BUTTER]
                case "UNSALTED_BUTTER":
                    aisles = [cls.UNSALTED_BUTTER]
                case "SPECIAL_BUTTERS":
                    aisles = [cls.SPECIAL_BUTTERS]
                case "ORGANIC_BUTTERS":
                    aisles = [cls.ORGANIC_BUTTERS]
               
        return aisles
    
class AlcampoMilkMargarineAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Milk_Margarine")

    MARGARINES_AND_OTHER_SPREADS = StaticAisle(name="Margarines and other spreads",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/margarinas-y-otros-untables/OC1607?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Margarines_and_other_spreads.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Margarines_and_other_spreads_detailed.json"))
    
  
    aisles: Final[List[StaticAisle]] = [MARGARINES_AND_OTHER_SPREADS]

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
                case "MARGARINES_AND_OTHER_SPREADS":
                    aisles = [cls.MARGARINES_AND_OTHER_SPREADS]
                
               
        return aisles
    
class AlcampoMilkCreamAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Milk_Cream")

    WHIPPING_CREAM = StaticAisle(name="Whipping cream",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/nata/nata-para-montar/OC160502?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Whipping_cream.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Whipping_cream_detailed.json"))
    
    SAUCES_FOR_COOKING = StaticAisle(name="Sauces for cooking",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/nata/salsas-para-cocina/OC160504?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Sauces_for_cooking.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sauces_for_cooking_detailed.json"))
    
    SPRAY_CREAM = StaticAisle(name="Spray Cream",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/nata/nata-en-spray/OC160503?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Spray_Cream.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Spray_Cream_detailed.json"))
    
    COOKING_CREAM = StaticAisle(name="Cooking cream",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/nata/nata-para-cocinar/OC160501?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cooking_cream.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cooking_cream_detailed.json"))
    
  
    aisles: Final[List[StaticAisle]] = [WHIPPING_CREAM, SAUCES_FOR_COOKING, SPRAY_CREAM, COOKING_CREAM]

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
                case "WHIPPING_CREAM":
                    aisles = [cls.WHIPPING_CREAM]
                case "SAUCES_FOR_COOKING":
                    aisles = [cls.SAUCES_FOR_COOKING]
                case "SPRAY_CREAM":
                    aisles = [cls.SPRAY_CREAM]
                case "COOKING_CREAM":
                    aisles = [cls.COOKING_CREAM]
                
               
        return aisles
    
class AlcampoMilkSmothiesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Milk_Smothies")

    PREPARED_COFFEES = StaticAisle(name="Prepared coffees",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/batidos-y-horchatas/caf%C3%A9s-preparados/OC24?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Prepared_coffees.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Prepared_coffees_detailed.json"))
    
    SMOOTHIES = StaticAisle(name="Smoothies",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/batidos-y-horchatas/batidos/OCBatidos?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Smoothies.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Smoothies_detailed.json"))
    
    HORCHATA = StaticAisle(name="Horchata",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/batidos-y-horchatas/horchata/OC160404?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Horchata.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Horchata_detailed.json"))
    
    PREPARED_CHOCOLATES = StaticAisle(name="Prepared chocolates",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/postres/chocolates-preparados/OC160406?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Prepared_chocolates.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Prepared_chocolates_detailed.json"))
    
   
    aisles: Final[List[StaticAisle]] = [PREPARED_COFFEES, SMOOTHIES, HORCHATA, PREPARED_CHOCOLATES]
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
                case "PREPARED_COFFEES":
                    aisles = [cls.PREPARED_COFFEES]
                case "SMOOTHIES":
                    aisles = [cls.SMOOTHIES]
                case "HORCHATA":
                    aisles = [cls.HORCHATA]
                case "PREPARED_CHOCOLATES":
                    aisles = [cls.PREPARED_CHOCOLATES]
             
        return aisles
    
class AlcampoMilkJuicesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Milk_Juices")

    JUICES_WITH_MILK = StaticAisle(name="Juices with milk",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/zumos-con-leche/OC160403?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Juices_with_milk.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Juices_with_milk_detailed.json"))
    
    
   
    aisles: Final[List[StaticAisle]] = [JUICES_WITH_MILK]
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
                case "JUICES_WITH_MILK":
                    aisles = [cls.JUICES_WITH_MILK]
           
        return aisles
    
class AlcampoMilkCondensedAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Milk_Condensed")

    CONDENSED_MILK = StaticAisle(name="Condensed milk",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/leche-condensada-polvo-y-evaporada/leche-condensada/OC160308?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Condensed_milk.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Condensed_milk_detailed.json"))
    
    POWDERED_AND_EVAPORATED = StaticAisle(name="Powdered and Evaporated",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/leche-condensada-polvo-y-evaporada/en-polvo-y-evaporada/OC160309?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Powdered_and_Evaporated.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Powdered_and_Evaporated_detailed.json"))
    
    
   
    aisles: Final[List[StaticAisle]] = [CONDENSED_MILK, POWDERED_AND_EVAPORATED]
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
                case "CONDENSED_MILK":
                    aisles = [cls.CONDENSED_MILK]
                case "POWDERED_AND_EVAPORATED":
                    aisles = [cls.POWDERED_AND_EVAPORATED]
           
        return aisles
    
class AlcampoMilkProteinProductsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Milk_Protein_Products")

    PROTEIN_PRODUCTS = StaticAisle(name="Protein Products",  url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/productos-proteicos/OC1612?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Protein_Products.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Protein_Products_detailed.json"))
    

    
    
   
    aisles: Final[List[StaticAisle]] = [PROTEIN_PRODUCTS]
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
                case "PROTEIN_PRODUCTS":
                    aisles = [cls.PROTEIN_PRODUCTS]
           
        return aisles
    
#Feeding

class AlcampoFeedingOilVinegarSaltAndSpicesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Feeding_Oil_vinegar_salt_and_spices")

    OILS = StaticAisle(name="Oils",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/aceite-vinagre-sal-y-especias/aceites/OC2301?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Oils.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Oils_detailed.json"))
    
    VINEGARS = StaticAisle(name="Vinegars",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/aceite-vinagre-sal-y-especias/vinagres/OC1001?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Vinegars.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vinegars_detailed.json"))
    
    SALT_SPICES_AND_SEASONINGS = StaticAisle(name="Salt, spices and seasonings",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/aceite-vinagre-sal-y-especias/sal-especias-y-sazonadores/OC100111?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Salt_spices_and_seasonings.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Salt_spices_and_seasonings_detailed.json"))
    
    ESSENTIALS_FOR_YOUR_AIR_FRYER = StaticAisle(name="Essentials for your air fryer",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/aceite-vinagre-sal-y-especias/esenciales-para-tu-freidora-de-aire/OCESFREAI?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Essentials_for_your_air_fryer.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Essentials_for_your_air_fryer_detailed.json"))
    
    
   
    aisles: Final[List[StaticAisle]] = [OILS, VINEGARS, SALT_SPICES_AND_SEASONINGS, ESSENTIALS_FOR_YOUR_AIR_FRYER]
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
                case "OILS":
                    aisles = [cls.OILS]
                case "VINEGARS":
                    aisles = [cls.VINEGARS]
                case "SALT_SPICES_AND_SEASONINGS":
                    aisles = [cls.SALT_SPICES_AND_SEASONINGS]
                case "ESSENTIALS_FOR_YOUR_AIR_FRYER":
                    aisles = [cls.ESSENTIALS_FOR_YOUR_AIR_FRYER]
           
        return aisles
    
class AlcampoFeedingCannedFishAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Feeding_Canned_fish")

    TUNA = StaticAisle(name="Tuna",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-de-pescado/at%C3%BAn/OCConservasAtun?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Tuna.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tuna_detailed.json"))
    
    BONITO_AND_TUNA_BELLY = StaticAisle(name="Bonito and tuna belly",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-de-pescado/bonito-y-ventresca/OC100402004?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Bonito_and_tuna_belly.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Bonito_and_tuna_belly_detailed.json"))
    
    MUSSELS = StaticAisle(name="Mussels",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-de-pescado/mejillones/OC100402010?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Mussels.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mussels_detailed.json"))
    
    NEEDLEFISH_SARDINES_AND_PILCHARDS = StaticAisle(name="Needlefish, sardines and pilchards",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-de-pescado/agujas-sardinas-y-sardinillas/OC100402005?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Needlefish_sardines_and_pilchards.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Needlefish_sardines_and_pilchards_detailed.json"))
    
    ANCHOVIES_AND_WHITEBAIT = StaticAisle(name="Anchovies and whitebait",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-de-pescado/anchoas-y-boquerones/OC100402007?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Anchovies_and_whitebait.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Anchovies_and_whitebait_detailed.json"))
    
    MACKEREL_AND_HORSE_MACKEREL = StaticAisle(name="Mackerel and horse mackerel",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-de-pescado/caballa-y-melva/OC100402006?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Mackerel_and_horse_mackerel.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mackerel_and_horse_mackerel_detailed.json"))
    
    COCKLES = StaticAisle(name="Cockles",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-de-pescado/berberechos/OC100402011?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cockles.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cockles_detailed.json"))
    
    RAZOR_CLAMS_AND_SCALLOPS = StaticAisle(name="Razor Clams and Scallops",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-de-pescado/almejas-navajas-y-zamburi%C3%B1as/OC100402012?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Razor_Clams_and_Scallops.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Razor_Clams_and_Scallops_detailed.json"))
    
    SQUID_OCTOPUS_SQUID_CUTTLEFISH = StaticAisle(name="Squid Octopus Squid Cuttlefish",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-de-pescado/calamares-pulpo-chipirones-sepia/OCConservasCalamares?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Squid_Octopus_Squid_Cuttlefish.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Squid_Octopus_Squid_Cuttlefish_detailed.json"))
    
    OTHER_CANNED_FISH = StaticAisle(name="Other canned fish",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-de-pescado/otras-conservas-de-pescado/OCOtrasConservasPescado?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Other_canned_fish.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_canned_fish_detailed.json"))
    
    
   
    aisles: Final[List[StaticAisle]] = [TUNA, BONITO_AND_TUNA_BELLY, MUSSELS, NEEDLEFISH_SARDINES_AND_PILCHARDS, ANCHOVIES_AND_WHITEBAIT, MACKEREL_AND_HORSE_MACKEREL, COCKLES, RAZOR_CLAMS_AND_SCALLOPS, 
                                        SQUID_OCTOPUS_SQUID_CUTTLEFISH, OTHER_CANNED_FISH]
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
                case "TUNA":
                    aisles = [cls.TUNA]
                case "BONITO_AND_TUNA_BELLY":
                    aisles = [cls.BONITO_AND_TUNA_BELLY]
                case "MUSSELS":
                    aisles = [cls.MUSSELS]
                case "NEEDLEFISH_SARDINES_AND_PILCHARDS":
                    aisles = [cls.NEEDLEFISH_SARDINES_AND_PILCHARDS]
                case "ANCHOVIES_AND_WHITEBAIT":
                    aisles = [cls.ANCHOVIES_AND_WHITEBAIT]
                case "MACKEREL_AND_HORSE_MACKEREL":
                    aisles = [cls.MACKEREL_AND_HORSE_MACKEREL]
                case "COCKLES":
                    aisles = [cls.COCKLES]
                case "RAZOR_CLAMS_AND_SCALLOPS":
                    aisles = [cls.RAZOR_CLAMS_AND_SCALLOPS]
                case "SQUID_OCTOPUS_SQUID_CUTTLEFISH":
                    aisles = [cls.SQUID_OCTOPUS_SQUID_CUTTLEFISH]
                case "OTHER_CANNED_FISH":
                    aisles = [cls.OTHER_CANNED_FISH]
           
        return aisles
    
class AlcampoFeedingCannedVegetablesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Feeding_Canned_vegetables")

    ASPARAGUS = StaticAisle(name="Asparagus",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-vegetales/esp%C3%A1rragos/OC100401005?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Asparagus.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Asparagus_detailed.json"))
    
    RED_PEPPERS = StaticAisle(name="Red peppers",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-vegetales/pimientos-rojos/OC100401007?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Red_peppers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Red_peppers_detailed.json"))
    
    CORN_PEAS_AND_CARROTS = StaticAisle(name="Corn, peas and carrots",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-vegetales/ma%C3%ADz-guisantes-y-zanahorias/OC100401013?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Corn_peas_and_carrots.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Corn_peas_and_carrots_detailed.json"))
    
    CRUSHED_TOMATOES = StaticAisle(name="Crushed tomatoes",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-vegetales/tomates-triturados/OC100401008?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Crushed_tomatoes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Crushed_tomatoes_detailed.json"))
    
    MUSHROOMS_TOADSTOOLS_AND_TRUFFLES = StaticAisle(name="Mushrooms, toadstools and truffles",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-vegetales/champi%C3%B1ones-setas-y-trufas/OC100401004?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Mushrooms_toadstools_and_truffles.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mushrooms_toadstools_and_truffles_detailed.json"))
    
    GREEN_BEANS_POTATOES_AND_ONIONS = StaticAisle(name="Green beans, potatoes and onions",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-vegetales/jud%C3%ADas-verdes-patatas-y-cebollas/OC100401006?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Green_beans_potatoes_and_onions.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Green_beans_potatoes_and_onions_detailed.json"))
    
    ARTICHOKES = StaticAisle(name="Artichokes",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-vegetales/alcachofas/OC100401001?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Artichokes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Artichokes_detailed.json"))
    
    MACEDONIAS_AND_MENESTRAS = StaticAisle(name="Macedonias and Menestras",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-vegetales/macedonias-y-menestras/OC100401010?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Macedonias_and_Menestras.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Macedonias_and_Menestras_detailed.json"))
    
    RATATOUILLE_AND_SOFRITOS = StaticAisle(name="Ratatouille and sofritos",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-vegetales/pisto-y-sofritos/OC100401011?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Ratatouille_and_sofritos.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Ratatouille_and_sofritos_detailed.json"))
    
    OTHER_CANNED_VEGETABLES = StaticAisle(name="Other canned vegetables",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-vegetales/otras-conservas-vegetales/OCOtrasConservasVegetales?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Other_canned_vegetables.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_canned_vegetables_detailed.json"))
    
    ORGANIC_CANNED_VEGETABLES = StaticAisle(name="Organic canned vegetables",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-vegetales/conservas-vegetales-ecol%C3%B3gicas/OC1163072207?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_canned_vegetables.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_canned_vegetables_detailed.json"))
    
    
   
    aisles: Final[List[StaticAisle]] = [ASPARAGUS, RED_PEPPERS, CORN_PEAS_AND_CARROTS, CRUSHED_TOMATOES, MUSHROOMS_TOADSTOOLS_AND_TRUFFLES, GREEN_BEANS_POTATOES_AND_ONIONS, ARTICHOKES, MACEDONIAS_AND_MENESTRAS,
                                        RATATOUILLE_AND_SOFRITOS, OTHER_CANNED_VEGETABLES, ORGANIC_CANNED_VEGETABLES]
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
                case "ASPARAGUS":
                    aisles = [cls.ASPARAGUS]
                case "RED_PEPPERS":
                    aisles = [cls.RED_PEPPERS]
                case "CORN_PEAS_AND_CARROTS":
                    aisles = [cls.CORN_PEAS_AND_CARROTS]
                case "CRUSHED_TOMATOES":
                    aisles = [cls.CRUSHED_TOMATOES]
                case "MUSHROOMS_TOADSTOOLS_AND_TRUFFLES":
                    aisles = [cls.MUSHROOMS_TOADSTOOLS_AND_TRUFFLES]
                case "GREEN_BEANS_POTATOES_AND_ONIONS":
                    aisles = [cls.GREEN_BEANS_POTATOES_AND_ONIONS]
                case "ARTICHOKES":
                    aisles = [cls.ARTICHOKES]
                case "MACEDONIAS_AND_MENESTRAS":
                    aisles = [cls.MACEDONIAS_AND_MENESTRAS]
                case "RATATOUILLE_AND_SOFRITOS":
                    aisles = [cls.RATATOUILLE_AND_SOFRITOS]
                case "OTHER_CANNED_VEGETABLES":
                    aisles = [cls.OTHER_CANNED_VEGETABLES]
                case "ORGANIC_CANNED_VEGETABLES":
                    aisles = [cls.ORGANIC_CANNED_VEGETABLES]
           
        return aisles
    
class AlcampoFeedingCannedMeatAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Feeding_Canned_meat")

    PATES_AND_FOIE_GRAS = StaticAisle(name="Pates and Foie Gras",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-c%C3%A1rnicas-platos-preparados-y-alm%C3%ADbares/pat%C3%A9s-y-foie-gras/OC100403?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Pates_and_Foie_Gras.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pates_and_Foie_Gras_detailed.json"))
    
    CANNED_MEAT = StaticAisle(name="Canned meat",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-c%C3%A1rnicas-platos-preparados-y-alm%C3%ADbares/conservas-de-carne/OC100406?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Canned_meat.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Canned_meat_detailed.json"))
    
    PRESERVED_FRUITS_AND_SYRUPS = StaticAisle(name="Preserved fruits and syrups",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-c%C3%A1rnicas-platos-preparados-y-alm%C3%ADbares/frutas-en-conserva-y-alm%C3%ADbares/OC100405?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Preserved_fruits_and_syrups.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Corn_peas_and_carrots_detailed.json"))
    
    CANNED_PREPARED_DISHES = StaticAisle(name="Canned prepared dishes",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-c%C3%A1rnicas-platos-preparados-y-alm%C3%ADbares/platos-preparados-en-conserva/OC100404?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Canned_prepared_dishes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Canned_prepared_dishes_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [PATES_AND_FOIE_GRAS, CANNED_MEAT, PRESERVED_FRUITS_AND_SYRUPS, CANNED_PREPARED_DISHES]
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
                case "PATES_AND_FOIE_GRAS":
                    aisles = [cls.PATES_AND_FOIE_GRAS]
                case "CANNED_MEAT":
                    aisles = [cls.CANNED_MEAT]
                case "PRESERVED_FRUITS_AND_SYRUPS":
                    aisles = [cls.PRESERVED_FRUITS_AND_SYRUPS]
                case "CANNED_PREPARED_DISHES":
                    aisles = [cls.CANNED_PREPARED_DISHES]
                
        return aisles
    
class AlcampoFeedingFriedTomatoAndSaucesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Feeding_Fried_tomato_and_sauces")

    FRIED_TOMATO = StaticAisle(name="Fried Tomato",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/tomate-frito-y-salsas/tomate-frito/OCSalsaTomate?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Fried_Tomato.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fried_Tomato_detailed.json"))
    
    KETCHUP = StaticAisle(name="Ketchup",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/tomate-frito-y-salsas/ketchup/OC100202003?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Ketchup.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Ketchup_detailed.json"))
    
    MAYONNAISE = StaticAisle(name="Mayonnaise",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/tomate-frito-y-salsas/mayonesa/OCMayonesa?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Mayonnaise.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mayonnaise_detailed.json"))
    
    BARBECUE = StaticAisle(name="Barbecue",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/tomate-frito-y-salsas/barbacoa-y-otras-salsas-para-carne/OCSalsasCarne?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Barbecue.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Barbecue_detailed.json"))
    
    MUSTARD = StaticAisle(name="Mustard",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/tomate-frito-y-salsas/mostaza/OCMostaza?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Mustard.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mustard_detailed.json"))
    
    PASTA_SAUCES = StaticAisle(name="Pasta sauces",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/tomate-frito-y-salsas/salsas-para-pasta/OCSalsasPasta?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Pasta_sauces.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pasta_sauces_detailed.json"))
    
    HOT_SAUCES = StaticAisle(name="Hot Sauces",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/tomate-frito-y-salsas/salsas-picantes/OCSalsasPicantes?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Hot_Sauces.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Hot_Sauces_detailed.json"))
    
    CAESAR_SAUCE_AND_YOGURT = StaticAisle(name="Caesar sauce and yogurt",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/tomate-frito-y-salsas/salsa-c%C3%A9sar-y-yogur/OCSalsasEnsalada?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Caesar_sauce_and_yogurt.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Caesar_sauce_and_yogurt_detailed.json"))
    
    ROMESCO = StaticAisle(name="Romesco",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/tomate-frito-y-salsas/romesco/OCSalsaromesco?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Romesco.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Romesco_detailed.json"))
    
    OTHER_SAUCES = StaticAisle(name="Other Sauces",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/tomate-frito-y-salsas/otras-salsas/OC1002?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Other_Sauces.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_Sauces_detailed.json"))
    
    DEHYDRATED_SAUCES = StaticAisle(name="Dehydrated sauces",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/tomate-frito-y-salsas/salsas-deshidratadas/OCsalsasdeshidratadas?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Dehydrated_sauces.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Dehydrated_sauces_detailed.json"))
    
    VEGETABLE_AND_TOMATO_PREPARATIONS = StaticAisle(name="Vegetable and Tomato Preparations",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/tomate-frito-y-salsas/preparados-de-verdura-y-tomate/OCpreparadosverdura?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Vegetable_and_Tomato_Preparations.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vegetable_and_Tomato_Preparations_detailed.json"))
    
    GARLIC_AND_ALI_OLI_SAUCES = StaticAisle(name="Garlic and Ali Oli Sauces",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/tomate-frito-y-salsas/salsas-de-ajo-y-ali-oli/OCsalsasajo?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Garlic_and_Ali_Oli_Sauces.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Garlic_and_Ali_Oli_Sauces_detailed.json"))
    
    SOY_SAUCES = StaticAisle(name="Soy Sauces",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/tomate-frito-y-salsas/salsas-de-soja/OCsalsasoja?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Soy_Sauces.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Soy_Sauces_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [FRIED_TOMATO, KETCHUP, MAYONNAISE, BARBECUE, MUSTARD, PASTA_SAUCES, HOT_SAUCES, CAESAR_SAUCE_AND_YOGURT, ROMESCO, OTHER_SAUCES, DEHYDRATED_SAUCES, 
                                        VEGETABLE_AND_TOMATO_PREPARATIONS, GARLIC_AND_ALI_OLI_SAUCES, SOY_SAUCES]
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
                case "FRIED_TOMATO":
                    aisles = [cls.FRIED_TOMATO]
                case "KETCHUP":
                    aisles = [cls.KETCHUP]
                case "MAYONNAISE":
                    aisles = [cls.MAYONNAISE]
                case "BARBECUE":
                    aisles = [cls.BARBECUE]
                case "MUSTARD":
                    aisles = [cls.MUSTARD]
                case "PASTA_SAUCES":
                    aisles = [cls.PASTA_SAUCES]
                case "HOT_SAUCES":
                    aisles = [cls.HOT_SAUCES]
                case "CAESAR_SAUCE_AND_YOGURT":
                    aisles = [cls.CAESAR_SAUCE_AND_YOGURT]
                case "ROMESCO":
                    aisles = [cls.ROMESCO]
                case "OTHER_SAUCES":
                    aisles = [cls.OTHER_SAUCES]
                case "DEHYDRATED_SAUCES":
                    aisles = [cls.DEHYDRATED_SAUCES]
                case "VEGETABLE_AND_TOMATO_PREPARATIONS":
                    aisles = [cls.VEGETABLE_AND_TOMATO_PREPARATIONS]
                case "GARLIC_AND_ALI_OLI_SAUCES":
                    aisles = [cls.GARLIC_AND_ALI_OLI_SAUCES]
                case "SOY_SAUCES":
                    aisles = [cls.SOY_SAUCES]
                
        return aisles
    
class AlcampoFeedingAppetizersNutsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Feeding_Appetizers_nuts")

    NUTS = StaticAisle(name="Nuts",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/aperitivos-aceitunas-y-frutos-secos/frutos-secos/OC100302?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Nuts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Nuts_detailed.json"))
    
    CHIPS = StaticAisle(name="Chips",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/aperitivos-aceitunas-y-frutos-secos/patatas-fritas/OC100304?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Chips.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chips_detailed.json"))
    
    SNACKS = StaticAisle(name="Snacks",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/aperitivos-aceitunas-y-frutos-secos/snacks/OC100306?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Snacks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Snacks_detailed.json"))
    
    OLIVES_AND_PICKLES = StaticAisle(name="Olives and pickles",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/aperitivos-aceitunas-y-frutos-secos/aceitunas-y-encurtidos/OC100301?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Olives_and_pickles.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Olives_and_pickles_detailed.json"))
    
    POPCORN = StaticAisle(name="Popcorn",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/aperitivos-aceitunas-y-frutos-secos/palomitas/OC100303?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Popcorn.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Popcorn_detailed.json"))
    
    SALTY_CRACKERS = StaticAisle(name="Salty Crackers",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/aperitivos-aceitunas-y-frutos-secos/galletas-saladas/OC100305?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Salty_Crackers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Salty_Crackers_detailed.json"))
   
    HEALTHY_SNACKS = StaticAisle(name="Healthy snacks",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/aperitivos-aceitunas-y-frutos-secos/aperitivos-saludables/OC100307?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Healthy_snacks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Healthy_snacks_detailed.json"))
   
    
    aisles: Final[List[StaticAisle]] = [NUTS, CHIPS, SNACKS, OLIVES_AND_PICKLES, POPCORN, SALTY_CRACKERS, HEALTHY_SNACKS]
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
                case "NUTS":
                    aisles = [cls.NUTS]
                case "CHIPS":
                    aisles = [cls.CHIPS]
                case "SNACKS":
                    aisles = [cls.SNACKS]
                case "OLIVES_AND_PICKLES":
                    aisles = [cls.OLIVES_AND_PICKLES]
                case "POPCORN":
                    aisles = [cls.POPCORN]
                case "SALTY_CRACKERS":
                    aisles = [cls.SALTY_CRACKERS]
                case "HEALTHY_SNACKS":
                    aisles = [cls.HEALTHY_SNACKS]
                
                
        return aisles
    
class AlcampoFeedingPastaAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Feeding_Pasta")

    MACARONI_AND_SHORT_PASTATS = StaticAisle(name="Macaroni and Short Pasta",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/pasta-alimenticia/macarrones-y-pasta-corta/OC100501002?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Macaroni_and_Short_Pasta.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Macaroni_and_Short_Pasta_detailed.json"))
    
    SPAGHETTI_AND_NOODLES = StaticAisle(name="Spaghetti and Noodles",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/pasta-alimenticia/espaguetis-y-tallarines/OC100501001?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Spaghetti_and_Noodles.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Spaghetti_and_Noodles_detailed.json"))
    
    NOODLE_AND_PASTA_SOUP = StaticAisle(name="Noodle and Pasta Soup",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/pasta-alimenticia/fideos-y-pasta-sopa/OC100501003?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Noodle_and_Pasta_Soup.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Noodle_and_Pasta_Soup_detailed.json"))
    
    PASTA_WITH_VEGETABLES = StaticAisle(name="Pasta with Vegetables",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/pasta-alimenticia/pasta-con-vegetales/OC100501005?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Pasta_with_Vegetables.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pasta_with_Vegetables_detailed.json"))
    
    WHOLE_WHEAT_PASTA = StaticAisle(name="Whole wheat pasta",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/pasta-alimenticia/pasta-integral/OC100501006?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Whole_wheat_pasta.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Whole_wheat_pasta_detailed.json"))
    
    EGG_PASTA = StaticAisle(name="Egg Pasta",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/pasta-alimenticia/pasta-al-huevo/OC100501004?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Egg_Pasta.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Egg_Pasta_detailed.json"))
   
    CANNELLONI_AND_LASAGNA = StaticAisle(name="Cannelloni and Lasagna",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/pasta-alimenticia/canelones-y-lasa%C3%B1as/OC100501007?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cannelloni_and_Lasagna.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cannelloni_and_Lasagna_detailed.json"))
    
    SPIRALS_AND_BOWS = StaticAisle(name="Spirals and Bows",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/pasta-alimenticia/espirales-y-lacitos/OC100501011?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Spirals_and_Bows.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Spirals_and_Bows_detailed.json"))
    
    OTHER_PASTAS = StaticAisle(name="Other Pastas",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/pasta-alimenticia/otras-pastas/OC100501009?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Other_Pastas.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_Pastas_detailed.json"))
    
    STUFFED_PASTA = StaticAisle(name="Stuffed Pasta",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/pasta-alimenticia/pasta-rellena/OC100501008?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Stuffed_Pasta.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Stuffed_Pasta_detailed.json"))
    
    PASTA_TABLE_IN_ITALY = StaticAisle(name="Pasta Table in Italy",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/pasta-alimenticia/pasta-tavola-in-italia/OCtavola?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Pasta_Table_in_Italy.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pasta_Table_in_Italy_detailed.json"))
    
    PASTA_SAUCES = StaticAisle(name="Pasta Sauces",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/pasta-alimenticia/salsas-para-pastas/OC100501010?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Pasta_Sauces.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pasta_Sauces_detailed.json"))
   
    ORGANIC_PASTA = StaticAisle(name="Organic Pasta",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/pasta-alimenticia/pasta-ecol%C3%B3gica/OCpastaeco?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Pasta.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Pasta_detailed.json"))
   
    
    aisles: Final[List[StaticAisle]] = [MACARONI_AND_SHORT_PASTATS, SPAGHETTI_AND_NOODLES, NOODLE_AND_PASTA_SOUP, PASTA_WITH_VEGETABLES, WHOLE_WHEAT_PASTA, EGG_PASTA, CANNELLONI_AND_LASAGNA,
                                        SPIRALS_AND_BOWS, OTHER_PASTAS, STUFFED_PASTA, PASTA_TABLE_IN_ITALY, PASTA_SAUCES, ORGANIC_PASTA]
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
                case "MACARONI_AND_SHORT_PASTATS":
                    aisles = [cls.MACARONI_AND_SHORT_PASTATS]
                case "SPAGHETTI_AND_NOODLES":
                    aisles = [cls.SPAGHETTI_AND_NOODLES]
                case "NOODLE_AND_PASTA_SOUP":
                    aisles = [cls.NOODLE_AND_PASTA_SOUP]
                case "PASTA_WITH_VEGETABLES":
                    aisles = [cls.PASTA_WITH_VEGETABLES]
                case "WHOLE_WHEAT_PASTA":
                    aisles = [cls.WHOLE_WHEAT_PASTA]
                case "EGG_PASTA":
                    aisles = [cls.EGG_PASTA]
                case "CANNELLONI_AND_LASAGNA":
                    aisles = [cls.CANNELLONI_AND_LASAGNA]
                case "SPIRALS_AND_BOWS":
                    aisles = [cls.SPIRALS_AND_BOWS]
                case "OTHER_PASTAS":
                    aisles = [cls.OTHER_PASTAS]
                case "STUFFED_PASTA":
                    aisles = [cls.STUFFED_PASTA]
                case "PASTA_TABLE_IN_ITALY":
                    aisles = [cls.PASTA_TABLE_IN_ITALY]
                case "PASTA_SAUCES":
                    aisles = [cls.PASTA_SAUCES]
                case "ORGANIC_PASTA":
                    aisles = [cls.ORGANIC_PASTA]
                
                
        return aisles
    
class AlcampoFeedingRiceAndLegumesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Feeding_Rice_and_legumes")

    RICE = StaticAisle(name="Rice",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/arroz-y-legumbres/arroz/OC100502?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Rice.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Rice_detailed.json"))
    
    LEGUMES = StaticAisle(name="Legumes",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/arroz-y-legumbres/legumbres/OC2112208?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Legumes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Legumes_detailed.json"))
    
    QUINOA_COUSCOUS_AND_OTHERS = StaticAisle(name="Quinoa, couscous and others",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/arroz-y-legumbres/quinoa-couscous-y-otros/OC100506?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Quinoa_couscous_and_others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Quinoa_couscous_and_others_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [RICE, LEGUMES, QUINOA_COUSCOUS_AND_OTHERS]
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
                case "LEGUMES":
                    aisles = [cls.LEGUMES]
                case "QUINOA_COUSCOUS_AND_OTHERS":
                    aisles = [cls.QUINOA_COUSCOUS_AND_OTHERS]
          
        return aisles
    
class AlcampoFeedingBakeryFlourAndDoughsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Feeding_Bakery_flour_and_doughs")

    FLOURS_AND_DOUGHS = StaticAisle(name="Flours and doughs",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/panader%C3%ADa-harina-y-masas/harinas-y-masas/OC100605012?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Flours_and_doughs.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Flours_and_doughs_detailed.json"))
    
    SLICED_BREAD = StaticAisle(name="Sliced bread",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/panader%C3%ADa-harina-y-masas/pan-de-molde/OCPanMolde?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Sliced_bread.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sliced_bread_detailed.json"))
    
    SPECIAL_BREAD = StaticAisle(name="Special bread",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/panader%C3%ADa-harina-y-masas/pan-especial/OC101004?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Special_bread.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Special_bread_detailed.json"))
    
    HAMBURGER_BUN_HOT_DOG_AND_SPECIALS = StaticAisle(name="Hamburger bun, hot dog and specials",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/panader%C3%ADa-harina-y-masas/pan-hamburguesa-perrito-y-especiales/OC101005?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Hamburger_bun_hot_dog_and_specials.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Hamburger_bun_hot_dog_and_specials_detailed.json"))
    
    TOAST = StaticAisle(name="Toast",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/panader%C3%ADa-harina-y-masas/pan-tostado/OC1010?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Toast.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Toast_detailed.json"))
    
    PEAKS_AND_SNACKS = StaticAisle(name="Peaks and Snacks",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/panader%C3%ADa-harina-y-masas/picos-y-snacks/OC101011?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Peaks_and_Snacks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Peaks_and_Snacks_detailed.json"))
    
    BREADCRUMBS = StaticAisle(name="Breadcrumbs",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/panader%C3%ADa-harina-y-masas/pan-rallado-y-pan-precocinado/OCPanRalladoPrecocinado?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Breadcrumbs.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Breadcrumbs_detailed.json"))
    
    ORGANIC_INDUSTRIAL_BAKERY = StaticAisle(name="Organic Industrial Bakery",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/panader%C3%ADa-harina-y-masas/panader%C3%ADa-industrial-ecol%C3%B3gica/OCPanaderiaeco?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Industrial_Bakery.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Industrial_Bakery_detailed.json"))
   
    aisles: Final[List[StaticAisle]] = [FLOURS_AND_DOUGHS, SLICED_BREAD, SPECIAL_BREAD, HAMBURGER_BUN_HOT_DOG_AND_SPECIALS, TOAST, PEAKS_AND_SNACKS, BREADCRUMBS, ORGANIC_INDUSTRIAL_BAKERY]
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
                case "FLOURS_AND_DOUGHS":
                    aisles = [cls.FLOURS_AND_DOUGHS]
                case "SLICED_BREAD":
                    aisles = [cls.SLICED_BREAD]
                case "SPECIAL_BREAD":
                    aisles = [cls.SPECIAL_BREAD]
                case "HAMBURGER_BUN_HOT_DOG_AND_SPECIALS":
                    aisles = [cls.HAMBURGER_BUN_HOT_DOG_AND_SPECIALS]
                case "TOAST":
                    aisles = [cls.TOAST]
                case "PEAKS_AND_SNACKS":
                    aisles = [cls.PEAKS_AND_SNACKS]
                case "BREADCRUMBS":
                    aisles = [cls.BREADCRUMBS]
                case "ORGANIC_INDUSTRIAL_BAKERY":
                    aisles = [cls.ORGANIC_INDUSTRIAL_BAKERY]
             
        return aisles
    
class AlcampoFeedingSoupsBrothsAndCreamsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Feeding_Soups_broths_and_creams")

    SOUPS = StaticAisle(name="Soups",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/sopas-caldos-y-cremas/sopas/OCSopas?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Soups.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Soups_detailed.json"))
    
    BROTHS = StaticAisle(name="Broths",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/sopas-caldos-y-cremas/caldos/OCCaldos?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Broths.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Broths_detailed.json"))
    
    CREAMS = StaticAisle(name="Creams",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/sopas-caldos-y-cremas/cremas/OCCremas?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Creams.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Creams_detailed.json"))
    
    PUREE = StaticAisle(name="Puree",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/sopas-caldos-y-cremas/pur%C3%A9/OC100607001?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Puree.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Puree_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [SOUPS, BROTHS, CREAMS, PUREE]
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
                case "SOUPS":
                    aisles = [cls.SOUPS]
                case "BROTHS":
                    aisles = [cls.BROTHS]
                case "CREAMS":
                    aisles = [cls.CREAMS]
                case "PUREE":
                    aisles = [cls.PUREE]
                
             
        return aisles
    
class AlcampoFeedingInternationalFoodAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Feeding_International_food")

    ORIENTAL_FOOD = StaticAisle(name="Oriental food",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/comida-internacional/comida-oriental/OCComidaOriental?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Oriental_food.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Oriental_food_detailed.json"))
    
    MEXICAN_FOOD = StaticAisle(name="Mexican food",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/comida-internacional/comida-mexicana/OC100608?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Mexican_food.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mexican_food_detailed.json"))
    
    OTHER_FOODS = StaticAisle(name="Other foods",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/comida-internacional/otros-alimentos-del-mundo/OC10060903?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Other_foods.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_foods_detailed.json"))
    
    INTERNATIONAL_SAUCES = StaticAisle(name="International sauces",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/comida-internacional/salsas-internacionales/OCSalsasOrientales?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "International_sauces.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "International_sauces_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [ORIENTAL_FOOD, MEXICAN_FOOD, OTHER_FOODS, INTERNATIONAL_SAUCES]
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
                case "ORIENTAL_FOOD":
                    aisles = [cls.ORIENTAL_FOOD]
                case "MEXICAN_FOOD":
                    aisles = [cls.MEXICAN_FOOD]
                case "OTHER_FOODS":
                    aisles = [cls.OTHER_FOODS]
                case "INTERNATIONAL_SAUCES":
                    aisles = [cls.INTERNATIONAL_SAUCES]
                
             
        return aisles
    
#Breakfast and snacks

class AlcampoBreakfastCafesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Breakfast_Cafes")

    COFFEE_CAPSULES = StaticAisle(name="Coffee capsules",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/caf%C3%A9s/caf%C3%A9-c%C3%A1psulas/OC1008061?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Coffee_capsules.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Coffee_capsules_detailed.json"))
    
    GROUND_COFFEE = StaticAisle(name="Ground Coffee",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/caf%C3%A9s/caf%C3%A9-molido/OC1008064?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Ground_Coffee.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Ground_Coffee_detailed.json"))
    
    COFFEE_BEANS = StaticAisle(name="Coffee beans",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/caf%C3%A9s/caf%C3%A9-en-grano/OC1008063?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Coffee_beans.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Coffee_beans_detailed.json"))
    
    INSTANT_COFFEE = StaticAisle(name="Instant coffee",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/caf%C3%A9s/caf%C3%A9-soluble/OC1008062?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Instant_coffee.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Instant_coffee_detailed.json"))
    
    CAPPUCCINO = StaticAisle(name="Cappuccino",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/caf%C3%A9s/capuchino/OC100806009?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cappuccino.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cappuccino_detailed.json"))
    
    ORGANIC_COFFEE = StaticAisle(name="Organic Coffee",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/caf%C3%A9s/caf%C3%A9-ecol%C3%B3gico/OCcafeeco?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Coffee.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Coffee_detailed.json"))
    
    PREPARED_COFFEES = StaticAisle(name="Prepared coffees",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/caf%C3%A9s/caf%C3%A9s-preparados/OC241?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Prepared_coffees.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Prepared_coffees_detailed.json"))
    
    CEREALS_AND_SOLUBLE_CHICORY = StaticAisle(name="Cereals and soluble chicory",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/caf%C3%A9s/cereales-y-achicoria-soluble/OC100806010?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cereals_and_soluble_chicory.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cereals_and_soluble_chicory_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [COFFEE_CAPSULES, GROUND_COFFEE, COFFEE_BEANS, INSTANT_COFFEE, CAPPUCCINO, ORGANIC_COFFEE, PREPARED_COFFEES, CEREALS_AND_SOLUBLE_CHICORY]
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
                case "COFFEE_CAPSULES":
                    aisles = [cls.COFFEE_CAPSULES]
                case "GROUND_COFFEE":
                    aisles = [cls.GROUND_COFFEE]
                case "COFFEE_BEANS":
                    aisles = [cls.COFFEE_BEANS]
                case "INSTANT_COFFEE":
                    aisles = [cls.INSTANT_COFFEE]
                case "CAPPUCCINO":
                    aisles = [cls.CAPPUCCINO]
                case "ORGANIC_COFFEE":
                    aisles = [cls.ORGANIC_COFFEE]
                case "PREPARED_COFFEES":
                    aisles = [cls.PREPARED_COFFEES]
                case "CEREALS_AND_SOLUBLE_CHICORY":
                    aisles = [cls.CEREALS_AND_SOLUBLE_CHICORY]
                
             
        return aisles
    
class AlcampoBreakfastCookiesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Breakfast_Cookies")

    MARIA_COOKIES = StaticAisle(name="Maria cookies",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/galletas/galletas-mar%C3%ADa/OC100805001?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Maria_cookies.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Maria_cookies_detailed.json"))
    
    TOASTED_AND_ARTISANAL = StaticAisle(name="Toasted and artisanal",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/galletas/tostadas-y-artesanas/OC100805036?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Toasted_and_artisanal.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Toasted_and_artisanal_detailed.json"))
    
    DIGESTIVE_BISCUITS = StaticAisle(name="Digestive Biscuits",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/galletas/galletas-digestive/OC100805003?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Digestive_Biscuits.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Digestive_Biscuits_detailed.json"))
    
    CEREAL_COOKIES = StaticAisle(name="Cereal cookies",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/galletas/galletas-con-cereales/OC100805011?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cereal_cookies.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cereal_cookies_detailed.json"))
    
    CHILDRENS_COOKIES = StaticAisle(name="Children's cookies",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/galletas/galletas-infantiles/OC100805013?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Childrens_cookies.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Childrens_cookies_detailed.json"))
    
    CHOCOLATE_COOKIES = StaticAisle(name="Chocolate cookies",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/galletas/galletas-chocolate/OC100805006?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Chocolate_cookies.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chocolate_cookies_detailed.json"))
    
    FILLED_COOKIES = StaticAisle(name="Filled cookies",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/galletas/galletas-rellenas/OC100805007?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Filled_cookies.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Filled_cookies_detailed.json"))
    
    COOKIES_WITHOUT_ADDED_SUGAR = StaticAisle(name="Cookies without added sugar",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/galletas/galletas-sin-az%C3%BAcar-a%C3%B1adido/OC10120202?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cookies_without_added_sugar.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cookies_without_added_sugar_detailed.json"))
    
    CAKES_AND_WAFFLES = StaticAisle(name="Cakes and Waffles",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/galletas/bizcochos-y-barquillos/OC100805008?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cakes_and_Waffles.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cakes_and_Waffles_detailed.json"))
    
    ASSORTMENT_OF_COOKIES_AND_PASTRIES = StaticAisle(name="Assortment of Cookies and Pastries",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/galletas/surtido-galletas-y-pastas/OC100805010?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Assortment_of_Cookies_and_Pastries.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Assortment_of_Cookies_and_Pastries_detailed.json"))
    
    BUTTER_COOKIES = StaticAisle(name="Butter cookies",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/galletas/galletas-de-mantequilla/OC100805023?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Butter_cookies.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Butter_cookies_detailed.json"))
    
    ORGANIC_COOKIES = StaticAisle(name="Organic Cookies",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/galletas/galletas-ecol%C3%B3gicas/OC100805205?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Cookies.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Cookies_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [MARIA_COOKIES, TOASTED_AND_ARTISANAL, DIGESTIVE_BISCUITS, CEREAL_COOKIES, CHILDRENS_COOKIES, CHOCOLATE_COOKIES, FILLED_COOKIES, COOKIES_WITHOUT_ADDED_SUGAR, 
                                        CAKES_AND_WAFFLES, ASSORTMENT_OF_COOKIES_AND_PASTRIES, BUTTER_COOKIES, ORGANIC_COOKIES]
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
                case "MARIA_COOKIES":
                    aisles = [cls.MARIA_COOKIES]
                case "TOASTED_AND_ARTISANAL":
                    aisles = [cls.TOASTED_AND_ARTISANAL]
                case "DIGESTIVE_BISCUITS":
                    aisles = [cls.DIGESTIVE_BISCUITS]
                case "CEREAL_COOKIES":
                    aisles = [cls.CEREAL_COOKIES]
                case "CHILDRENS_COOKIES":
                    aisles = [cls.CHILDRENS_COOKIES]
                case "CHOCOLATE_COOKIES":
                    aisles = [cls.CHOCOLATE_COOKIES]
                case "FILLED_COOKIES":
                    aisles = [cls.FILLED_COOKIES]
                case "COOKIES_WITHOUT_ADDED_SUGAR":
                    aisles = [cls.COOKIES_WITHOUT_ADDED_SUGAR]
                case "CAKES_AND_WAFFLES":
                    aisles = [cls.CAKES_AND_WAFFLES]
                case "ASSORTMENT_OF_COOKIES_AND_PASTRIES":
                    aisles = [cls.ASSORTMENT_OF_COOKIES_AND_PASTRIES]
                case "BUTTER_COOKIES":
                    aisles = [cls.BUTTER_COOKIES]
                case "ORGANIC_COOKIES":
                    aisles = [cls.ORGANIC_COOKIES]
                
             
        return aisles
    
class AlcampoBreakfastChocolatesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Breakfast_Chocolates")

    CHOCOLATE_BARS = StaticAisle(name="Chocolate bars",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/chocolates-cremas-untar-y-bombones/tabletas-de-chocolate/OC100803?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Chocolate_bars.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chocolate_bars_detailed.json"))
    
    CHOCOLATE_AND_OTHER_SPREADS = StaticAisle(name="Chocolate and other spreads",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/chocolates-cremas-untar-y-bombones/cremas-de-untar-chocolate-y-otras/OC100803019?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Chocolate_and_other_spreads.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chocolate_and_other_spreads_detailed.json"))
    
    CHOCOLATE_SNACKS = StaticAisle(name="Chocolate snacks",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/chocolates-cremas-untar-y-bombones/snacks-de-chocolate/OC100803005?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Chocolate_snacks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chocolate_snacks_detailed.json"))
    
    CHOCOLATES_AND_TRUFFLES = StaticAisle(name="Chocolates and Truffles",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/chocolates-cremas-untar-y-bombones/bombones-y-trufas/OC100901?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Chocolates_and_Truffles.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chocolates_and_Truffles_detailed.json"))
    
    CHRISTMAS_FIGURES_AND_CALENDAR = StaticAisle(name="Christmas Figures and Calendar",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/chocolates-cremas-untar-y-bombones/figuras-y-calendario-navidad/OC306041?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Christmas_Figures_and_Calendar.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Christmas_Figures_and_Calendar_detailed.json"))
    
    CHOCOLATE_IN_CAPSULES = StaticAisle(name="Chocolate in capsules",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/chocolates-cremas-untar-y-bombones/chocolate-en-c%C3%A1psulas/OC100803015?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Chocolate_in_capsules.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chocolate_in_capsules_detailed.json"))
    
    HOT_CHOCOLATE = StaticAisle(name="Hot chocolate",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/chocolates-cremas-untar-y-bombones/chocolate-a-la-taza/OC100803016?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Hot_chocolate.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Hot_chocolate_detailed.json"))
    
    
    
    aisles: Final[List[StaticAisle]] = [CHOCOLATE_BARS, CHOCOLATE_AND_OTHER_SPREADS, CHOCOLATE_SNACKS, CHOCOLATES_AND_TRUFFLES, CHRISTMAS_FIGURES_AND_CALENDAR, CHOCOLATE_IN_CAPSULES, HOT_CHOCOLATE]
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
                case "CHOCOLATE_BARS":
                    aisles = [cls.CHOCOLATE_BARS]
                case "CHOCOLATE_AND_OTHER_SPREADS":
                    aisles = [cls.CHOCOLATE_AND_OTHER_SPREADS]
                case "DIGESTIVE_BISCUCHOCOLATE_SNACKSITS":
                    aisles = [cls.CHOCOLATE_SNACKS]
                case "CHOCOLATES_AND_TRUFFLES":
                    aisles = [cls.CHOCOLATES_AND_TRUFFLES]
                case "CHRISTMAS_FIGURES_AND_CALENDAR":
                    aisles = [cls.CHRISTMAS_FIGURES_AND_CALENDAR]
                case "CHOCOLATE_IN_CAPSULES":
                    aisles = [cls.CHOCOLATE_IN_CAPSULES]
                case "HOT_CHOCOLATE":
                    aisles = [cls.HOT_CHOCOLATE]
           
        return aisles
    
class AlcampoBreakfastPastriesAndCakesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Breakfast_Pastries_and_cakes")

    CROISSANTS_CUPCAKES_AND_MUFFINS = StaticAisle(name="Croissants, Cupcakes and Muffins",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/boller%C3%ADa-y-pasteler%C3%ADa/croissants-magdalenas-y-muffins/OC101104?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Croissants_Cupcakes_and_Muffins.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Croissants_Cupcakes_and_Muffins_detailed.json"))
    
    DOUGHNUTS_AND_SOBAOS = StaticAisle(name="Doughnuts and Sobaos",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/boller%C3%ADa-y-pasteler%C3%ADa/rosquillas-y-sobaos/OCRosquillassobaos?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Doughnuts_and_Sobaos.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Doughnuts_and_Sobaos_detailed.json"))
    
    PALM_TREES_PUFF_PASTRY_AND_CANES = StaticAisle(name="Palm trees, puff pastry and canes",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/boller%C3%ADa-y-pasteler%C3%ADa/palmeras-hojaldres-y-ca%C3%B1as/OC101113?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Palm_trees_puff_pastry_and_canes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Palm_trees_puff_pastry_and_canes_detailed.json"))
    
    CAKES_BISCUITS_AND_COKES = StaticAisle(name="Cakes, biscuits and cokes",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/boller%C3%ADa-y-pasteler%C3%ADa/pastelitos-bizcochos-y-cocas/OCpastelitos?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cakes_biscuits_and_cokes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cakes_biscuits_and_cokes_detailed.json"))
    
    NEAPOLITANS_CARACOLAS_AND_ENSAIMADAS = StaticAisle(name="Neapolitans, Caracolas and Ensaimadas",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/boller%C3%ADa-y-pasteler%C3%ADa/napolitanas-caracolas-y-ensaimadas/OCnapolitanascaracolasensaimadas?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Neapolitans_Caracolas_and_Ensaimadas.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Neapolitans_Caracolas_and_Ensaimadas_detailed.json"))
    
    BRIOCHE_AND_MILK_BREAD = StaticAisle(name="Brioche and Milk Bread",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/boller%C3%ADa-y-pasteler%C3%ADa/brioche-y-pan-de-leche/OC101102?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Brioche_and_Milk_Bread.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Brioche_and_Milk_Bread_detailed.json"))
    
    PLUMCAKES_AND_ARMS = StaticAisle(name="Plumcakes and Arms",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/boller%C3%ADa-y-pasteler%C3%ADa/plumcakes-y-brazos/OC101114?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Plumcakes_and_Arms.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Plumcakes_and_Arms_detailed.json"))
    
    WAFFLES_CREPES_AND_PANCAKES = StaticAisle(name="Waffles, Crepes and Pancakes",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/boller%C3%ADa-y-pasteler%C3%ADa/gofres-crepes-y-tortitas/OC101115?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Waffles_Crepes_and_Pancakes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Waffles_Crepes_and_Pancakes_detailed.json"))
    
    CAKES_PASTRIES_AND_SPECIALTIES = StaticAisle(name="Cakes, Pastries and Specialties",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/boller%C3%ADa-y-pasteler%C3%ADa/tortas-pastas-y-especialidades/OCTortasPastasEspecialidades?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cakes_Pastries_and_Specialties.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cakes_Pastries_and_Specialties_detailed.json"))
    
    ORGANIC_PASTRIES = StaticAisle(name="Organic Pastries",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/boller%C3%ADa-y-pasteler%C3%ADa/boller%C3%ADa-ecol%C3%B3gica/OCpasteleriaeco?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Pastries.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Pastries_detailed.json"))
    
    
    
    aisles: Final[List[StaticAisle]] = [CROISSANTS_CUPCAKES_AND_MUFFINS, DOUGHNUTS_AND_SOBAOS, PALM_TREES_PUFF_PASTRY_AND_CANES, CAKES_BISCUITS_AND_COKES, NEAPOLITANS_CARACOLAS_AND_ENSAIMADAS, 
                                        BRIOCHE_AND_MILK_BREAD, PLUMCAKES_AND_ARMS, WAFFLES_CREPES_AND_PANCAKES, CAKES_PASTRIES_AND_SPECIALTIES, ORGANIC_PASTRIES]
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
                case "CROISSANTS_CUPCAKES_AND_MUFFINS":
                    aisles = [cls.CROISSANTS_CUPCAKES_AND_MUFFINS]
                case "DOUGHNUTS_AND_SOBAOS":
                    aisles = [cls.DOUGHNUTS_AND_SOBAOS]
                case "PALM_TREES_PUFF_PASTRY_AND_CANES":
                    aisles = [cls.PALM_TREES_PUFF_PASTRY_AND_CANES]
                case "CAKES_BISCUITS_AND_COKES":
                    aisles = [cls.CAKES_BISCUITS_AND_COKES]
                case "NEAPOLITANS_CARACOLAS_AND_ENSAIMADAS":
                    aisles = [cls.NEAPOLITANS_CARACOLAS_AND_ENSAIMADAS]
                case "BRIOCHE_AND_MILK_BREAD":
                    aisles = [cls.BRIOCHE_AND_MILK_BREAD]
                case "PLUMCAKES_AND_ARMS":
                    aisles = [cls.PLUMCAKES_AND_ARMS]
                case "WAFFLES_CREPES_AND_PANCAKES":
                    aisles = [cls.WAFFLES_CREPES_AND_PANCAKES]
                case "CAKES_PASTRIES_AND_SPECIALTIES":
                    aisles = [cls.CAKES_PASTRIES_AND_SPECIALTIES]
                case "ORGANIC_PASTRIES":
                    aisles = [cls.ORGANIC_PASTRIES]
           
        return aisles
    
class AlcampoBreakfastCerealsAndBarsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Breakfast_Cereals_and_bars")

    CEREAL_WITH_CHOCOLATE = StaticAisle(name="Cereal with Chocolate",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/cereales-y-barritas/cereales-con-chocolate/OC100804003?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cereal_with_Chocolate.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cereal_with_Chocolate_detailed.json"))
    
    CEREALS_LINE = StaticAisle(name="Cereals Line",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/cereales-y-barritas/cereales-l%C3%ADnea/OC100804006?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cereals_Line.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cereals_Line_detailed.json"))
    
    MUESLI_CEREALS = StaticAisle(name="Muesli Cereals",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/cereales-y-barritas/cereales-muesli/OC100804004?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Muesli_Cereals.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Muesli_Cereals_detailed.json"))
    
    CEREALS_WITH_FIBER = StaticAisle(name="Cereals with fiber",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/cereales-y-barritas/cereales-con-fibra/OC100804005?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cereals_with_fiber.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cereals_with_fiber_detailed.json"))
    
    CEREALS_WITH_HONEY = StaticAisle(name="Cereals with honey",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/cereales-y-barritas/cereales-con-miel/OC100804002?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cereals_with_honey.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cereals_with_honey_detailed.json"))
    
    CEREAL_BARS = StaticAisle(name="Cereal Bars",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/cereales-y-barritas/barritas-cereales/OC100804008?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cereal_Bars.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cereal_Bars_detailed.json"))
    
    CORNFLAKES = StaticAisle(name="Cornflakes",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/cereales-y-barritas/cornflakes/OC100804001?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cornflakes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cornflakes_detailed.json"))
    
    OTHER_INFANT_CEREALS = StaticAisle(name="Other Infant Cereals",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/cereales-y-barritas/otros-cereales-infantiles/OC100804007?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Other_Infant_Cereals.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_Infant_Cereals_detailed.json"))
    
    ORGANIC_CEREALS = StaticAisle(name="Organic Cereals",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/cereales-y-barritas/cereales-ecol%C3%B3gicos/OC100804009?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Cereals.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Cereals_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [CEREAL_WITH_CHOCOLATE, CEREALS_LINE, MUESLI_CEREALS, CEREALS_WITH_FIBER, CEREALS_WITH_HONEY, CEREAL_BARS, CORNFLAKES, OTHER_INFANT_CEREALS, ORGANIC_CEREALS]
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
                case "CEREAL_WITH_CHOCOLATE":
                    aisles = [cls.CEREAL_WITH_CHOCOLATE]
                case "CEREALS_LINE":
                    aisles = [cls.CEREALS_LINE]
                case "MUESLI_CEREALS":
                    aisles = [cls.MUESLI_CEREALS]
                case "CEREALS_WITH_FIBER":
                    aisles = [cls.CEREALS_WITH_FIBER]
                case "CEREALS_WITH_HONEY":
                    aisles = [cls.CEREALS_WITH_HONEY]
                case "CEREAL_BARS":
                    aisles = [cls.CEREAL_BARS]
                case "CORNFLAKES":
                    aisles = [cls.CORNFLAKES]
                case "OTHER_INFANT_CEREALS":
                    aisles = [cls.OTHER_INFANT_CEREALS]
                case "ORGANIC_CEREALS":
                    aisles = [cls.ORGANIC_CEREALS]
                
           
        return aisles
    
class AlcampoBreakfastSugarAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Breakfast_Sugar")

    SUGAR = StaticAisle(name="Sugar",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/az%C3%BAcar-miel-y-otros-edulcorantes/az%C3%BAcar/OC100801?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Sugar.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sugar_detailed.json"))
    
    SWEETENERS = StaticAisle(name="Sweeteners",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/az%C3%BAcar-miel-y-otros-edulcorantes/edulcorantes/OC100801009?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Sweeteners.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sweeteners_detailed.json"))
    
    PANELA = StaticAisle(name="Panela",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/az%C3%BAcar-miel-y-otros-edulcorantes/panela/OC100801010?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Panela.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Panela_detailed.json"))
    
    HONEY = StaticAisle(name="Honey",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/az%C3%BAcar-miel-y-otros-edulcorantes/miel/OC100811?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Honey.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Honey_detailed.json"))
    
    ORGANIC_SUGAR = StaticAisle(name="Organic Sugar and Sweetener",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/az%C3%BAcar-miel-y-otros-edulcorantes/az%C3%BAcar-y-edulcorante-ecol%C3%B3gicos/OCazucareco?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Sugar.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Sugar_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [SUGAR, SWEETENERS, PANELA, HONEY, ORGANIC_SUGAR]
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
                case "SUGAR":
                    aisles = [cls.SUGAR]
                case "SWEETENERS":
                    aisles = [cls.SWEETENERS]
                case "PANELA":
                    aisles = [cls.PANELA]
                case "HONEY":
                    aisles = [cls.HONEY]
                case "ORGANIC_SUGAR":
                    aisles = [cls.ORGANIC_SUGAR]
           
        return aisles
    
class AlcampoBreakfastCocaoAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Breakfast_Cocao")

    SOLUBLE_COCOA_POWDER = StaticAisle(name="Soluble cocoa powder",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/cacaos-solubles/cacao-polvo-soluble/OC100808?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Soluble_cocoa_powder.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Soluble_cocoa_powder_detailed.json"))
    
    INSTANT_COCOA_POWDER = StaticAisle(name="Instant cocoa powder",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/cacaos-solubles/cacao-polvo-instantaneo/OC1116216216?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Instant_cocoa_powder.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Instant_cocoa_powder_detailed.json"))
    
    COCOA_POWDER_SPECIALTIES = StaticAisle(name="Cocoa powder specialties",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/cacaos-solubles/cacao-polvo-especialidades/OC1116216215?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cocoa_powder_specialties.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cocoa_powder_specialties_detailed.json"))
    
    CUP_OF_COCOA = StaticAisle(name="Cup of cocoa",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/cacaos-solubles/cacao-a-la-taza/OC1116216211?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cup_of_cocoa.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cup_of_cocoa_detailed.json"))
    
    COCOA_IN_SINGLE_DOSES = StaticAisle(name="Cocoa in single doses",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/cacaos-solubles/cacao-en-monodosis/OC1116216214?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cocoa_in_single_doses.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cocoa_in_single_doses_detailed.json"))
    
    ORGANIC_COCOA = StaticAisle(name="Organic Cocoa",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/cacaos-solubles/cacaos-ecol%C3%B3gicos/OCcacaoseco?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Cocoa.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Cocoa_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [SOLUBLE_COCOA_POWDER, INSTANT_COCOA_POWDER, COCOA_POWDER_SPECIALTIES, CUP_OF_COCOA, COCOA_IN_SINGLE_DOSES, ORGANIC_COCOA]
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
                case "SOLUBLE_COCOA_POWDER":
                    aisles = [cls.SOLUBLE_COCOA_POWDER]
                case "INSTANT_COCOA_POWDER":
                    aisles = [cls.INSTANT_COCOA_POWDER]
                case "COCOA_POWDER_SPECIALTIES":
                    aisles = [cls.COCOA_POWDER_SPECIALTIES]
                case "CUP_OF_COCOA":
                    aisles = [cls.CUP_OF_COCOA]
                case "COCOA_IN_SINGLE_DOSES":
                    aisles = [cls.COCOA_IN_SINGLE_DOSES]
                case "ORGANIC_COCOA":
                    aisles = [cls.ORGANIC_COCOA]
           
        return aisles
    
class AlcampoBreakfastTeaAndInfusionAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Breakfast_Tea_and_infusion")

    SINGLE_DOSE_INFUSIONS = StaticAisle(name="Single-dose infusions",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/t%C3%A9-e-infusiones/infusiones-monodosis/OC100807008?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Single_dose_infusions.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Single_dose_infusions_detailed.json"))
    
    TEA = StaticAisle(name="Tea",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/t%C3%A9-e-infusiones/t%C3%A9/OC100807007?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Tea.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tea_detailed.json"))
    
    INFUSIONS = StaticAisle(name="Infusions",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/t%C3%A9-e-infusiones/infusiones/OC100807006?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Infusions.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Infusions_detailed.json"))
    
    YERBA_MATE = StaticAisle(name="Yerba mate",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/t%C3%A9-e-infusiones/yerba-mate/OC100807005?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Yerba_mate.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Yerba_mate_detailed.json"))
    
    PENNYROYAL = StaticAisle(name="Pennyroyal",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/t%C3%A9-e-infusiones/poleo-menta/OC100807003?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Pennyroyal.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pennyroyal_detailed.json"))
    
    LINDEN = StaticAisle(name="Linden",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/t%C3%A9-e-infusiones/tila/OC100807004?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Linden.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Linden_detailed.json"))
    
    CHAMOMILE = StaticAisle(name="Chamomile",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/t%C3%A9-e-infusiones/manzanilla/OC100807002?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Chamomile.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chamomile_detailed.json"))
    
    ORGANIC_TEA_AND_INFUSIONS = StaticAisle(name="Organic tea and infusions",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/t%C3%A9-e-infusiones/t%C3%A9-e-infusiones-ecol%C3%B3gicas/OC100807009?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_tea_and_infusions.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_tea_and_infusions_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [SINGLE_DOSE_INFUSIONS, TEA, INFUSIONS, YERBA_MATE, PENNYROYAL, LINDEN, CHAMOMILE, ORGANIC_TEA_AND_INFUSIONS]
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
                case "SINGLE_DOSE_INFUSIONS":
                    aisles = [cls.SINGLE_DOSE_INFUSIONS]
                case "TEA":
                    aisles = [cls.TEA]
                case "INFUSIONS":
                    aisles = [cls.INFUSIONS]
                case "YERBA_MATE":
                    aisles = [cls.YERBA_MATE]
                case "PENNYROYAL":
                    aisles = [cls.PENNYROYAL]
                case "LINDEN":
                    aisles = [cls.LINDEN]
                case "CHAMOMILE":
                    aisles = [cls.CHAMOMILE]
                case "ORGANIC_TEA_AND_INFUSIONS":
                    aisles = [cls.ORGANIC_TEA_AND_INFUSIONS]
           
        return aisles
    
class AlcampoBreakfastJamAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Breakfast_Jam")

    JAM_AND_PRESERVE = StaticAisle(name="Jam and Preserve",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/mermelada-almibares-membrillo/mermelada-y-confitura/OC100810?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Jam_and_Preserve.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Jam_and_Preserve_detailed.json"))
    
    SYRUPS = StaticAisle(name="Syrups",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/mermelada-almibares-membrillo/alm%C3%ADbares/OC142018?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Syrups.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Syrups_detailed.json"))
    
    QUINCE_MOLASSES_AND_OTHERS = StaticAisle(name="Quince, molasses and others",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/mermelada-almibares-membrillo/membrillo-melaza-y-otros/OCMembrilloOtros?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Quince_molasses_and_others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Quince_molasses_and_others_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [JAM_AND_PRESERVE, SYRUPS, QUINCE_MOLASSES_AND_OTHERS]
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
                case "JAM_AND_PRESERVE":
                    aisles = [cls.JAM_AND_PRESERVE]
                case "SYRUPS":
                    aisles = [cls.SYRUPS]
                case "QUINCE_MOLASSES_AND_OTHERS":
                    aisles = [cls.QUINCE_MOLASSES_AND_OTHERS]
                
        return aisles
    
class AlcampoBreakfastCandiesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Breakfast_Candies")

    CANDIES = StaticAisle(name="Candies",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/golosinas/caramelos/OC100902002?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Candies.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Candies_detailed.json"))
    
    JELLY_BEANS = StaticAisle(name="Jelly beans",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/golosinas/caramelos-de-goma/OC100902003?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Jelly_beans.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Jelly_beans_detailed.json"))
    
    CHEWING_GUM = StaticAisle(name="Chewing gum",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/golosinas/chicles/OC100902001?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Chewing_gum.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chewing_gum_detailed.json"))
    
    CHOCOLATES = StaticAisle(name="Chocolates",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/golosinas/chocolatinas/OC100902005?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Chocolates.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chocolates_detailed.json"))
    
    CLOUDS = StaticAisle(name="Clouds",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/golosinas/nubes/OC100902004?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Clouds.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Clouds_detailed.json"))
    
    OTHERS = StaticAisle(name="Others",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/golosinas/otros/OC100902006?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Others.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Others_detailed.json"))
    

    aisles: Final[List[StaticAisle]] = [CANDIES, JELLY_BEANS, CHEWING_GUM, CHOCOLATES, CLOUDS, OTHERS]
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
                case "JELLY_BEANS":
                    aisles = [cls.JELLY_BEANS]
                case "CHEWING_GUM":
                    aisles = [cls.CHEWING_GUM]
                case "CHOCOLATES":
                    aisles = [cls.CHOCOLATES]
                case "CLOUDS":
                    aisles = [cls.CLOUDS]
                case "OTHERS":
                    aisles = [cls.OTHERS]
                
        return aisles
    
class AlcampoBreakfastDessertsPreparationAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Breakfast_Desserts_preparation")

    CONDENSED_POWDERED_AND_EVAPORATED_MILK = StaticAisle(name="Condensed, powdered and evaporated milk",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/preparaci%C3%B3n-postres/leche-condensada-polvo-y-evaporada/OC10071201?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Condensed_powdered_and_evaporated_milk.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Condensed_powdered_and_evaporated_milk_detailed.json"))
    
    BOOSTERS_AND_GASIFIERS = StaticAisle(name="Boosters and gasifiers",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/preparaci%C3%B3n-postres/impulsores-y-gasificantes/OC100703?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Boosters_and_gasifiers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Boosters_and_gasifiers_detailed.json"))
    
    DESSERTS = StaticAisle(name="Desserts",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/preparaci%C3%B3n-postres/postres/OC10071203?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Desserts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Desserts_detailed.json"))
    
    LIQUID_CARAMEL_AND_SYRUPS = StaticAisle(name="Liquid caramel and syrups",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/preparaci%C3%B3n-postres/caramelo-l%C3%ADquido-y-siropes/OC100711?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Liquid_caramel_and_syrups.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Liquid_caramel_and_syrups_detailed.json"))
    
    ADD_ONS = StaticAisle(name="Add-ons",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/preparaci%C3%B3n-postres/complementos/OC100712?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Add_ons.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Add_ons_detailed.json"))
    
    FINAL_TOUCH_OR_DECORATION = StaticAisle(name="Final touch or decoration",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/preparaci%C3%B3n-postres/toque-final-o-decoraci%C3%B3n/OC10071215?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Final_touch_or_decoration.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Final_touch_or_decoration_detailed.json"))
    
    CANDLES = StaticAisle(name="Candles",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/preparaci%C3%B3n-postres/velas/OC10071218?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Candles.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Candles_detailed.json"))
    
    YEASTS = StaticAisle(name="Yeasts",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/preparaci%C3%B3n-postres/levaduras/OC10071217?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Yeasts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Yeasts_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [CONDENSED_POWDERED_AND_EVAPORATED_MILK, BOOSTERS_AND_GASIFIERS, DESSERTS, LIQUID_CARAMEL_AND_SYRUPS, ADD_ONS, FINAL_TOUCH_OR_DECORATION, CANDLES, YEASTS]
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
                case "CONDENSED_POWDERED_AND_EVAPORATED_MILK":
                    aisles = [cls.CONDENSED_POWDERED_AND_EVAPORATED_MILK]
                case "BOOSTERS_AND_GASIFIERS":
                    aisles = [cls.BOOSTERS_AND_GASIFIERS]
                case "DESSERTS":
                    aisles = [cls.DESSERTS]
                case "LIQUID_CARAMEL_AND_SYRUPS":
                    aisles = [cls.LIQUID_CARAMEL_AND_SYRUPS]
                case "ADD_ONS":
                    aisles = [cls.ADD_ONS]
                case "FINAL_TOUCH_OR_DECORATION":
                    aisles = [cls.FINAL_TOUCH_OR_DECORATION]
                case "CANDLES":
                    aisles = [cls.CANDLES]
                case "YEASTS":
                    aisles = [cls.YEASTS]
                
        return aisles
    
class AlcampoBreakfastFoodBankAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Breakfast_Food_bank")

    FOOD_BANK_COLLECTION = StaticAisle(name="Food bank collection",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/recogida-banco-de-alimentos/OCCBA?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Food_bank_collection.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Food_bank_collection_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [FOOD_BANK_COLLECTION]
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
                case "FOOD_BANK_COLLECTION":
                    aisles = [cls.FOOD_BANK_COLLECTION]
              
        return aisles
    
class AlcampoBreakfastNougatsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Breakfast_Nougats")

    NOUGATS = StaticAisle(name="Nougats",  url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/turrones/OC100903?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Nougats.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Nougats_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [NOUGATS]
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
                case "NOUGATS":
                    aisles = [cls.NOUGATS]
              
        return aisles
    
#frozen

class AlcampoFrozentFishAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frozen_fish")

    FROZEN_FISH = StaticAisle(name="Frozen Fish",  url="https://www.compraonline.alcampo.es/categories/congelados/pescados-mariscos-y-surimis/pescados-congelados/OC120102?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Frozen_Fish.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Frozen_Fish_detailed.json"))
    
    FROZEN_SEAFOOD = StaticAisle(name="Frozen Seafood",  url="https://www.compraonline.alcampo.es/categories/congelados/pescados-mariscos-y-surimis/mariscos-congelados/OC120105?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Frozen_Seafood.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Frozen_Seafood_detailed.json"))
    
    BREADED_FISH = StaticAisle(name="Breaded Fish",  url="https://www.compraonline.alcampo.es/categories/congelados/pescados-mariscos-y-surimis/pescados-empanados/OC120505?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Breaded_Fish.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Breaded_Fish_detailed.json"))
    
    BREADED_SQUID_AND_SEAFOOD = StaticAisle(name="Breaded Squid and Seafood",  url="https://www.compraonline.alcampo.es/categories/congelados/pescados-mariscos-y-surimis/calamares-y-mariscos-rebozados/OC120506?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Breaded_Squid_and_Seafood.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Breaded_Squid_and_Seafood_detailed.json"))
    
    SURIMIS = StaticAisle(name="Surimis",  url="https://www.compraonline.alcampo.es/categories/congelados/pescados-mariscos-y-surimis/surimis/OC120104?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Surimis.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Surimis_detailed.json"))
    
    EEL_SUBSTITUTES = StaticAisle(name="Eel substitutes",  url="https://www.compraonline.alcampo.es/categories/congelados/pescados-mariscos-y-surimis/suced%C3%A1neos-de-angula/OCCongeladoGulas?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Eel_substitutes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Eel_substitutes_detailed.json"))
 
    
    aisles: Final[List[StaticAisle]] = [FROZEN_FISH, FROZEN_SEAFOOD, BREADED_FISH, BREADED_SQUID_AND_SEAFOOD, SURIMIS, EEL_SUBSTITUTES]
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
                case "FROZEN_FISH":
                    aisles = [cls.FROZEN_FISH]
                case "FROZEN_SEAFOOD":
                    aisles = [cls.FROZEN_SEAFOOD]
                case "BREADED_FISH":
                    aisles = [cls.BREADED_FISH]
                case "BREADED_SQUID_AND_SEAFOOD":
                    aisles = [cls.BREADED_SQUID_AND_SEAFOOD]
                case "SURIMIS":
                    aisles = [cls.SURIMIS]
                case "EEL_SUBSTITUTES":
                    aisles = [cls.EEL_SUBSTITUTES]
                
                
        return aisles
    
class AlcampoFrozentIceCreamAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frozen_ice_cream")

    TUBS = StaticAisle(name="Tubs",  url="https://www.compraonline.alcampo.es/categories/congelados/helados/tarrinas/OCTarrinasHelado?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Tubs.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tubs_detailed.json"))
    
    CHOCOLATES = StaticAisle(name="Chocolates",  url="https://www.compraonline.alcampo.es/categories/congelados/helados/bombones/OC120802?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Chocolates.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chocolates_detailed.json"))
    
    CONES = StaticAisle(name="Cones",  url="https://www.compraonline.alcampo.es/categories/congelados/helados/conos/OC120803?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cones.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cones_detailed.json"))
    
    SANDWICH = StaticAisle(name="Sandwich",  url="https://www.compraonline.alcampo.es/categories/congelados/helados/s%C3%A1ndwich/OC120806?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Sandwich.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sandwich_detailed.json"))
    
    POLES = StaticAisle(name="Poles",  url="https://www.compraonline.alcampo.es/categories/congelados/helados/polos/OC120804?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Poles.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Poles_detailed.json"))
    
    SNACKS = StaticAisle(name="Snacks",  url="https://www.compraonline.alcampo.es/categories/congelados/helados/snacks/OC120805?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Snacks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Snacks_detailed.json"))
    
    BARS_AND_BLOCKS = StaticAisle(name="Bars and blocks",  url="https://www.compraonline.alcampo.es/categories/congelados/helados/barras-y-bloques/OCBarrasHelado?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Bars_and_blocks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Bars_and_blocks_detailed.json"))
    
    SPECIAL_ICE_CREAMS = StaticAisle(name="Special ice creams",  url="https://www.compraonline.alcampo.es/categories/congelados/helados/helados-especiales/OCHELESP?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Special_ice_creams.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Special_ice_creams_detailed.json"))
    
    DIETARY_AND_ECOLOGICAL = StaticAisle(name="Dietary and ecological",  url="https://www.compraonline.alcampo.es/categories/congelados/helados/diet%C3%A9ticos-y-ecol%C3%B3gicos/OC120809?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Dietary_and_ecological.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Dietary_and_ecological_detailed.json"))
    
    SLUSHIES = StaticAisle(name="Slushies",  url="https://www.compraonline.alcampo.es/categories/congelados/helados/granizados/OC289?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Slushies.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Slushiesd_detailed.json"))
    
    COOKIES_AND_WAFERS = StaticAisle(name="Cookies and wafers",  url="https://www.compraonline.alcampo.es/categories/congelados/helados/galletas-y-barquillos/OCBarquillos?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cookies_and_wafers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cookies_and_wafers_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [TUBS, CHOCOLATES, CONES, SANDWICH, POLES, SNACKS, BARS_AND_BLOCKS, SPECIAL_ICE_CREAMS, DIETARY_AND_ECOLOGICAL, SLUSHIES, COOKIES_AND_WAFERS]
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
                case "TUBS":
                    aisles = [cls.TUBS]
                case "CHOCOLATES":
                    aisles = [cls.CHOCOLATES]
                case "CONES":
                    aisles = [cls.CONES]
                case "SANDWICH":
                    aisles = [cls.SANDWICH]
                case "POLES":
                    aisles = [cls.POLES]
                case "SNACKS":
                    aisles = [cls.SNACKS]
                case "BARS_AND_BLOCKS":
                    aisles = [cls.BARS_AND_BLOCKS]
                case "SPECIAL_ICE_CREAMS":
                    aisles = [cls.SPECIAL_ICE_CREAMS]
                case "DIETARY_AND_ECOLOGICAL":
                    aisles = [cls.DIETARY_AND_ECOLOGICAL]
                case "SLUSHIES":
                    aisles = [cls.SLUSHIES]
                case "COOKIES_AND_WAFERS":
                    aisles = [cls.COOKIES_AND_WAFERS]
            
        return aisles
    
class AlcampoFrozentVegetablesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frozen_vegetables")

    VEGETABLE_PREPARATIONS = StaticAisle(name="Vegetable Preparations",  url="https://www.compraonline.alcampo.es/categories/congelados/verduras-congeladas/preparados-de-verdura/OC120311?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Vegetable_Preparations.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vegetable_Preparations_detailed.json"))
    
    CHARD_AND_SPINACH = StaticAisle(name="Chard and Spinach",  url="https://www.compraonline.alcampo.es/categories/congelados/verduras-congeladas/acelgas-y-espinacas/OC120303?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Chard_and_Spinach.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chard_and_Spinach_detailed.json"))
    
    GARLIC_ONION_AND_CORN = StaticAisle(name="Garlic, Onion and Corn",  url="https://www.compraonline.alcampo.es/categories/congelados/verduras-congeladas/ajo-cebolla-y-maiz/OC120309?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Garlic_Onion_and_Corn.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Garlic_Onion_and_Corn_detailed.json"))
    
    ARTICHOKES_AND_THISTLES = StaticAisle(name="Artichokes and Thistles",  url="https://www.compraonline.alcampo.es/categories/congelados/verduras-congeladas/alcachofas-y-cardos/OC120305?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Artichokes_and_Thistles.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Artichokes_and_Thistles_detailed.json"))
    
    CABBAGE_CAULIFLOWER_AND_BROCCOLI = StaticAisle(name="Cabbage, Cauliflower and Broccoli",  url="https://www.compraonline.alcampo.es/categories/congelados/verduras-congeladas/col-coliflor-y-br%C3%B3coli/OC120304?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cabbage_Cauliflower_and_Broccoli.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cabbage_Cauliflower_and_Broccoli_detailed.json"))
    
    MUSHROOM_AND_CARROT = StaticAisle(name="Mushroom and Carrot",  url="https://www.compraonline.alcampo.es/categories/congelados/verduras-congeladas/champi%C3%B1%C3%B3n-y-zanahoria/OC120307?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Mushroom_and_Carrot.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mushroom_and_Carrot_detailed.json"))
    
    POTATO_SALAD_AND_VEGETABLE_STEW = StaticAisle(name="Potato Salad and Vegetable Stew",  url="https://www.compraonline.alcampo.es/categories/congelados/verduras-congeladas/ensaladilla-y-menestra/OC120308?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Potato_Salad_and_Vegetable_Stew.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Potato_Salad_and_Vegetable_Stew_detailed.json"))
    
    ASPARAGUS_AND_PEAS = StaticAisle(name="Asparagus and Peas",  url="https://www.compraonline.alcampo.es/categories/congelados/verduras-congeladas/esp%C3%A1rragos-y-guisantes/OC120302?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Asparagus_and_Peas.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Asparagus_and_Peas_detailed.json"))
    
    BEANS_BROAD_BEANS_AND_POCHAS = StaticAisle(name="Beans, Broad Beans and Pochas",  url="https://www.compraonline.alcampo.es/categories/congelados/verduras-congeladas/jud%C3%ADas-habas-y-pochas/OC120301?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Beans_Broad_Beans_and_Pochas.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Beans_Broad_Beans_and_Pochas_detailed.json"))
    
    OTHER_VEGETABLES = StaticAisle(name="Other Vegetables",  url="https://www.compraonline.alcampo.es/categories/congelados/verduras-congeladas/otras-verduras/OC120310?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Other_Vegetables.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_Vegetables_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [VEGETABLE_PREPARATIONS, CHARD_AND_SPINACH, GARLIC_ONION_AND_CORN, ARTICHOKES_AND_THISTLES, CABBAGE_CAULIFLOWER_AND_BROCCOLI, MUSHROOM_AND_CARROT, 
                                        POTATO_SALAD_AND_VEGETABLE_STEW, ASPARAGUS_AND_PEAS, BEANS_BROAD_BEANS_AND_POCHAS, OTHER_VEGETABLES]
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
                case "VEGETABLE_PREPARATIONS":
                    aisles = [cls.VEGETABLE_PREPARATIONS]
                case "CHARD_AND_SPINACH":
                    aisles = [cls.CHARD_AND_SPINACH]
                case "GARLIC_ONION_AND_CORN":
                    aisles = [cls.GARLIC_ONION_AND_CORN]
                case "ARTICHOKES_AND_THISTLES":
                    aisles = [cls.ARTICHOKES_AND_THISTLES]
                case "CABBAGE_CAULIFLOWER_AND_BROCCOLI":
                    aisles = [cls.CABBAGE_CAULIFLOWER_AND_BROCCOLI]
                case "MUSHROOM_AND_CARROT":
                    aisles = [cls.MUSHROOM_AND_CARROT]
                case "POTATO_SALAD_AND_VEGETABLE_STEW":
                    aisles = [cls.POTATO_SALAD_AND_VEGETABLE_STEW]
                case "ASPARAGUS_AND_PEAS":
                    aisles = [cls.ASPARAGUS_AND_PEAS]
                case "BEANS_BROAD_BEANS_AND_POCHAS":
                    aisles = [cls.BEANS_BROAD_BEANS_AND_POCHAS]
                case "OTHER_VEGETABLES":
                    aisles = [cls.OTHER_VEGETABLES]
             
        return aisles
    
class AlcampoFrozentMealsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frozen_meals")

    SOUPS_AND_CREAMS = StaticAisle(name="Soups and creams",  url="https://www.compraonline.alcampo.es/categories/congelados/platos-preparados-congelados/sopas-y-cremas/OCSopasCremasCongeladas?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Soups_and_creams.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Soups_and_creams_detailed.json"))
    
    PASTA_DISHES = StaticAisle(name="Pasta dishes",  url="https://www.compraonline.alcampo.es/categories/congelados/platos-preparados-congelados/platos-de-pasta/OC120502?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Pasta_dishes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pasta_dishes_detailed.json"))
    
    FROZEN_PIZZAS = StaticAisle(name="Frozen Pizzas",  url="https://www.compraonline.alcampo.es/categories/congelados/platos-preparados-congelados/pizzas-congeladas/OC120401?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Frozen_Pizzas.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Frozen_Pizzas_detailed.json"))
    
    MEXICAN_DISHES = StaticAisle(name="Mexican dishes",  url="https://www.compraonline.alcampo.es/categories/congelados/platos-preparados-congelados/platos-mejicanos/OCPlatosMejicanosCongelados?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Mexican_dishes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mexican_dishes_detailed.json"))
    
    ORIENTAL_DISHES = StaticAisle(name="Oriental dishes",  url="https://www.compraonline.alcampo.es/categories/congelados/platos-preparados-congelados/platos-orientales/OCPlatosOrientalesCongelados?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Oriental_dishes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Oriental_dishes_detailed.json"))
    
    MEAT_DISHES = StaticAisle(name="Meat dishes",  url="https://www.compraonline.alcampo.es/categories/congelados/platos-preparados-congelados/platos-de-carne/OCPlatosCarneCongelados?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Meat_dishes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Meat_dishes_detailed.json"))
    
    STIR_FRIES_AND_RICE = StaticAisle(name="Stir-fries and Rice",  url="https://www.compraonline.alcampo.es/categories/congelados/platos-preparados-congelados/salteados-y-arroces/OC1206?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Stir_fries_and_Rice.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Stir_fries_and_Rice_detailed.json"))
    
    WRAPS_CREPES_AND_PUFF_PASTRIES = StaticAisle(name="Wraps, crepes and puff pastries",  url="https://www.compraonline.alcampo.es/categories/congelados/platos-preparados-congelados/wraps-crepes-y-hojaldres/OCCrepesHojaldres?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Wraps_crepes_and_puff_pastries.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Wraps_crepes_and_puff_pastries_detailed.json"))
    
    APPETIZERS = StaticAisle(name="Appetizers",  url="https://www.compraonline.alcampo.es/categories/congelados/platos-preparados-congelados/aperitivos/OC120501?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Appetizers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Appetizers_detailed.json"))
    
    FISH_DISHES = StaticAisle(name="Fish dishes",  url="https://www.compraonline.alcampo.es/categories/congelados/platos-preparados-congelados/platos-de-pescado/OCPlatosPescadoCongelados?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Fish_dishes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fish_dishes_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [SOUPS_AND_CREAMS, PASTA_DISHES, FROZEN_PIZZAS, MEXICAN_DISHES, ORIENTAL_DISHES, MEAT_DISHES, STIR_FRIES_AND_RICE, WRAPS_CREPES_AND_PUFF_PASTRIES, APPETIZERS, FISH_DISHES]
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
                case "SOUPS_AND_CREAMS":
                    aisles = [cls.SOUPS_AND_CREAMS]
                case "PASTA_DISHES":
                    aisles = [cls.PASTA_DISHES]
                case "FROZEN_PIZZAS":
                    aisles = [cls.FROZEN_PIZZAS]
                case "MEXICAN_DISHES":
                    aisles = [cls.MEXICAN_DISHES]
                case "ORIENTAL_DISHES":
                    aisles = [cls.ORIENTAL_DISHES]
                case "MEAT_DISHES":
                    aisles = [cls.MEAT_DISHES]
                case "STIR_FRIES_AND_RICE":
                    aisles = [cls.STIR_FRIES_AND_RICE]
                case "WRAPS_CREPES_AND_PUFF_PASTRIES":
                    aisles = [cls.WRAPS_CREPES_AND_PUFF_PASTRIES]
                case "APPETIZERS":
                    aisles = [cls.APPETIZERS]
                case "FISH_DISHES":
                    aisles = [cls.FISH_DISHES]
             
        return aisles
    
class AlcampoFrozentPotatoesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frozen_Potatoes_croquettes_and_empanadas")

    EMPANADILLAS = StaticAisle(name="Empanadillas",  url="https://www.compraonline.alcampo.es/categories/congelados/patatas-croquetas-y-empanadillas/empanadillas/OC120504?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Empanadillas.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Empanadillas_detailed.json"))
    
    CHIPS = StaticAisle(name="Chips",  url="https://www.compraonline.alcampo.es/categories/congelados/patatas-croquetas-y-empanadillas/patatas-fritas/OC120312?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Chips.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chips_detailed.json"))
    
    CROQUETTES = StaticAisle(name="Croquettes",  url="https://www.compraonline.alcampo.es/categories/congelados/patatas-croquetas-y-empanadillas/croquetas/OC120503?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Croquettes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Croquettes_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [EMPANADILLAS, CHIPS, CROQUETTES]
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
                case "EMPANADILLAS":
                    aisles = [cls.EMPANADILLAS]
                case "CHIPS":
                    aisles = [cls.CHIPS]
                case "CROQUETTES":
                    aisles = [cls.CROQUETTES]
                    
        return aisles
    
class AlcampoFrozentBreadedChickenAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frozen_breaded_chicken")

    SAINT_JAMES = StaticAisle(name="Saint James",  url="https://www.compraonline.alcampo.es/categories/congelados/san-jacobos-y-pollo-empanado/san-jacobos/OCSanJacobos?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Saint_James.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Saint_James_detailed.json"))
    
    FLAMENQUINES = StaticAisle(name="Flamenquines",  url="https://www.compraonline.alcampo.es/categories/congelados/san-jacobos-y-pollo-empanado/flamenquines/OCFlamenquines?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Flamenquines.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Flamenquines_detailed.json"))
    
    NUGGETS = StaticAisle(name="Nuggets",  url="https://www.compraonline.alcampo.es/categories/congelados/san-jacobos-y-pollo-empanado/nuggets/OCNuggets?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Nuggets.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Nuggets_detailed.json"))
    
    FINGERS = StaticAisle(name="Fingers",  url="https://www.compraonline.alcampo.es/categories/congelados/san-jacobos-y-pollo-empanado/fingers/OCFingers?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Fingers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fingers_detailed.json"))
    
    BREADED_BREAST = StaticAisle(name="Breaded breast",  url="https://www.compraonline.alcampo.es/categories/congelados/san-jacobos-y-pollo-empanado/pechuga-empanada/OCPechugaEmpanada?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Breaded_breast.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Breaded_breast_detailed.json"))
    
    ESCALOPE_CORDON_BLEU = StaticAisle(name="Escalope cordon bleu",  url="https://www.compraonline.alcampo.es/categories/congelados/san-jacobos-y-pollo-empanado/escalope-cord%C3%B3n-blue/OCEscalopePollo?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Escalope_cordon_bleu.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Escalope_cordon_bleu_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [SAINT_JAMES, FLAMENQUINES, NUGGETS, FINGERS, BREADED_BREAST, ESCALOPE_CORDON_BLEU]
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
                case "SAINT_JAMES":
                    aisles = [cls.SAINT_JAMES]
                case "FLAMENQUINES":
                    aisles = [cls.FLAMENQUINES]
                case "NUGGETS":
                    aisles = [cls.NUGGETS]
                case "FINGERS":
                    aisles = [cls.FINGERS]
                case "BREADED_BREAST":
                    aisles = [cls.BREADED_BREAST]
                case "ESCALOPE_CORDON_BLEU":
                    aisles = [cls.ESCALOPE_CORDON_BLEU]

        return aisles
    
class AlcampoFrozentMeatAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frozen_meat")

    MEAT = StaticAisle(name="Meat",  url="https://www.compraonline.alcampo.es/categories/congelados/carne/OC1202?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Meat.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Meat_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [MEAT]
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
                case "MEAT":
                    aisles = [cls.MEAT]
              
        return aisles
    
class AlcampoFrozentPastriesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frozen_pastries")

    ICE_AND_INSULATED_BAGS = StaticAisle(name="Ice and insulated bags",  url="https://www.compraonline.alcampo.es/categories/congelados/reposter%C3%ADa-hielo-y-bolsas-isot%C3%A9rmicas/hielo-y-bolsas-isot%C3%A9rmicas/OC1210?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Ice_and_insulated_bags.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Ice_and_insulated_bags_detailed.json"))
    
    BREAD_AND_DOUGHS = StaticAisle(name="Bread and doughs",  url="https://www.compraonline.alcampo.es/categories/congelados/reposter%C3%ADa-hielo-y-bolsas-isot%C3%A9rmicas/pan-y-masas/OCPanCongelado?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Bread_and_doughs.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Bread_and_doughs_detailed.json"))
    
    CHURROS_AND_PORRAS = StaticAisle(name="Churros and porras",  url="https://www.compraonline.alcampo.es/categories/congelados/reposter%C3%ADa-hielo-y-bolsas-isot%C3%A9rmicas/churros-y-porras/OCChurros?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Churros_and_porras.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Churros_and_porras_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [ICE_AND_INSULATED_BAGS, BREAD_AND_DOUGHS, CHURROS_AND_PORRAS]
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
                case "ICE_AND_INSULATED_BAGS":
                    aisles = [cls.ICE_AND_INSULATED_BAGS]
                case "BREAD_AND_DOUGHS":
                    aisles = [cls.BREAD_AND_DOUGHS]
                case "CHURROS_AND_PORRAS":
                    aisles = [cls.CHURROS_AND_PORRAS]
              
        return aisles
    
class AlcampoFrozentFruitAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frozen_fruit")

    PROFITEROLES_AND_OTHER_DESSERTS = StaticAisle(name="Profiteroles and other desserts",  url="https://www.compraonline.alcampo.es/categories/congelados/tartas-postres-y-fruta-congelada/profiteroles-y-otros-postres/OC12093?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Profiteroles_and_other_desserts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Profiteroles_and_other_desserts_detailed.json"))
    
    FROZEN_FRUIT = StaticAisle(name="Frozen fruit",  url="https://www.compraonline.alcampo.es/categories/congelados/tartas-postres-y-fruta-congelada/fruta-congelada/OC12094?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Frozen_fruit.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Frozen_fruit_detailed.json"))
    
    CAKES_AND_ROLLS = StaticAisle(name="Cakes and Rolls",  url="https://www.compraonline.alcampo.es/categories/congelados/tartas-postres-y-fruta-congelada/tartas-y-brazos/OC12091?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cakes_and_Rolls.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cakes_and_Rolls_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [PROFITEROLES_AND_OTHER_DESSERTS, FROZEN_FRUIT, CAKES_AND_ROLLS]
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
                case "PROFITEROLES_AND_OTHER_DESSERTS":
                    aisles = [cls.PROFITEROLES_AND_OTHER_DESSERTS]
                case "FROZEN_FRUIT":
                    aisles = [cls.FROZEN_FRUIT]
                case "CAKES_AND_ROLLS":
                    aisles = [cls.CAKES_AND_ROLLS]
              
        return aisles
    
class AlcampoFrozentEssentialsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frozen_Essentials_AirFryer")

    FROZEN_FISH = StaticAisle(name="Frozen fish",  url="http://compraonline.alcampo.es/categories/congelados/esenciales-para-tu-freidora-de-aire/pescado-congelado/OCconfreiaire4?sortBy=favorite",
                                     original_file_uri=os.path.join(category_path(), "Frozen_fish.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Frozen_fish_detailed.json"))
    
    FROZEN_READY_MEALS = StaticAisle(name="Frozen ready meals",  url="https://www.compraonline.alcampo.es/categories/congelados/esenciales-para-tu-freidora-de-aire/platos-preparados-congelados/OCconfreiaire1?sortBy=favorite",
                                     original_file_uri=os.path.join(category_path(), "Frozen_ready_meals.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Frozen_ready_meals_detailed.json"))
    
    FROZEN_VEGETABLES = StaticAisle(name="Frozen vegetables",  url="https://www.compraonline.alcampo.es/categories/congelados/esenciales-para-tu-freidora-de-aire/verduras-congeladas/OCconfreiaire2?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Frozen_vegetables.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Frozen_vegetables_detailed.json"))
    
    FROZEN_DESSERTS = StaticAisle(name="Frozen desserts",  url="https://www.compraonline.alcampo.es/categories/congelados/esenciales-para-tu-freidora-de-aire/postres-congelados/OCconfreiaire3?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Frozen_desserts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Frozen_desserts_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [FROZEN_FISH, FROZEN_READY_MEALS, FROZEN_VEGETABLES, FROZEN_DESSERTS]
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
                case "FROZEN_FISH":
                    aisles = [cls.FROZEN_FISH]
                case "FROZEN_READY_MEALS":
                    aisles = [cls.FROZEN_READY_MEALS]
                case "FROZEN_VEGETABLES":
                    aisles = [cls.FROZEN_VEGETABLES]
                case "FROZEN_DESSERTS":
                    aisles = [cls.FROZEN_DESSERTS]
              
        return aisles
    
#prepared_Food

class AlcampoPreparedSushiAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Prepared_sushi")

    SUSHI_AND_SASHIMI = StaticAisle(name="Sushi and sashimi",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/sushi/sushi-y-sashimi/OC1405021?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Sushi_and_sashimi.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sushi_and_sashimi_detailed.json"))
    
    SALAD_SPOKES_AND_NOODLES = StaticAisle(name="Salads, pokes and noodles",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/sushi/ensaladas-pokes-y-tallarines/OC1405022?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Salad_spokes_and_noodles.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Salad_spokes_and_noodles_detailed.json"))
    
    GYOZAS_SKEWERS_AND_CHICKEN = StaticAisle(name="Gyozas, skewers and chicken",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/sushi/gyozas-brochetas-y-pollo/OC1405023?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Gyozas_skewers_and_chicken.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Gyozas_skewers_and_chicken_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [SUSHI_AND_SASHIMI, SALAD_SPOKES_AND_NOODLES, GYOZAS_SKEWERS_AND_CHICKEN]
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
                case "SUSHI_AND_SASHIMI":
                    aisles = [cls.SUSHI_AND_SASHIMI]
                case "SALAD_SPOKES_AND_NOODLES":
                    aisles = [cls.SALAD_SPOKES_AND_NOODLES]
                case "GYOZAS_SKEWERS_AND_CHICKEN":
                    aisles = [cls.GYOZAS_SKEWERS_AND_CHICKEN]
              
        return aisles
    
class AlcampoPreparedPizzaAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Prepared_pizza")

    REFRIGERATED_PIZZAS = StaticAisle(name="Refrigerated pizzas",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/pizzas/pizzas-refrigeradas/OC9411?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Refrigerated_pizzas.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Refrigerated_pizzas_detailed.json"))
    
    FROZEN_THIN_CRUST_PIZZAS = StaticAisle(name="Frozen thin-crust pizzas",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/pizzas/pizzas-masa-fina-congeladas/OC9412?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Frozen_thin_crust_pizzas.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Frozen_thin_crust_pizzas_detailed.json"))
    
    PANINIS = StaticAisle(name="Paninis",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/pizzas/paninis/OC9413?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Paninis.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Paninis_detailed.json"))
    
    SPECIALTY_FROZEN_PIZZAS = StaticAisle(name="Specialty frozen pizzas",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/pizzas/pizzas-especiales-congeladas/OC9414?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Specialty_frozen_pizzas.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Specialty_frozen_pizzas_detailed.json"))
    
    FROZEN_DEEP_DISH_PIZZAS = StaticAisle(name="Frozen deep-dish pizzas",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/pizzas/pizzas-masa-gruesa-congeladas/OC9415?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Frozen_deep_dish_pizzas.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Frozen_deep_dish_pizzas_detailed.json"))
    
    FROZEN_PIZZA_BASES = StaticAisle(name="Frozen pizza bases",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/pizzas/bases-de-pizza-congeladas/OC9416?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Frozen_pizza_bases.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Frozen_pizza_bases_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [REFRIGERATED_PIZZAS, FROZEN_THIN_CRUST_PIZZAS, PANINIS, SPECIALTY_FROZEN_PIZZAS, FROZEN_DEEP_DISH_PIZZAS, FROZEN_PIZZA_BASES]
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
                case "REFRIGERATED_PIZZAS":
                    aisles = [cls.REFRIGERATED_PIZZAS]
                case "FROZEN_THIN_CRUST_PIZZAS":
                    aisles = [cls.FROZEN_THIN_CRUST_PIZZAS]
                case "PANINIS":
                    aisles = [cls.PANINIS]
                case "SPECIALTY_FROZEN_PIZZAS":
                    aisles = [cls.SPECIALTY_FROZEN_PIZZAS]
                case "FROZEN_DEEP_DISH_PIZZAS":
                    aisles = [cls.FROZEN_DEEP_DISH_PIZZAS]
                case "FROZEN_PIZZA_BASES":
                    aisles = [cls.FROZEN_PIZZA_BASES]
              
        return aisles
    
class AlcampoPreparedGazpachosAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Prepared_gazpachos")

    GAZPACHOS = StaticAisle(name="Gazpachos",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/gazpachos-y-cremas/gazpachos/OC9431?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Gazpachos.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Gazpachos_detailed.json"))
    
    SALMOREJOS = StaticAisle(name="Salmorejos",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/gazpachos-y-cremas/salmorejos/OC9432?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Salmorejos.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Salmorejos_detailed.json"))
    
    REFRIGERATED_SOUPS_AND_CREAMS = StaticAisle(name="Refrigerated soups and creams",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/gazpachos-y-cremas/sopas-y-cremas-refrigeradas/OC094274?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Refrigerated_soups_and_creams.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Refrigerated_soups_and_creams_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [GAZPACHOS, SALMOREJOS, REFRIGERATED_SOUPS_AND_CREAMS]
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
                case "GAZPACHOS":
                    aisles = [cls.GAZPACHOS]
                case "SALMOREJOS":
                    aisles = [cls.SALMOREJOS]
                case "REFRIGERATED_SOUPS_AND_CREAMS":
                    aisles = [cls.REFRIGERATED_SOUPS_AND_CREAMS]
            
        return aisles
    
class AlcampoPreparedTortillasAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Prepared_Tortillas")

    POTATO_TORTILLAS = StaticAisle(name="Potato tortillas",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/tortillas-de-patata/OC09426?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Potato_tortillas.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Potato_tortillas_detailed.json"))
   
    aisles: Final[List[StaticAisle]] = [POTATO_TORTILLAS]
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
                case "POTATO_TORTILLAS":
                    aisles = [cls.POTATO_TORTILLAS]
              
        return aisles
    
class AlcampoPreparedRiceAndPastaAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Prepared_Rice_and_pasta")

    REFRIGERATED_PASTA_DISHES = StaticAisle(name="Refrigerated pasta dishes",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/arroces-y-pastas/platos-de-pasta-refrigerada/OC20022018521?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Refrigerated_pasta_dishes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Refrigerated_pasta_dishes_detailed.json"))
   
    FRESH_STUFFED_PASTA = StaticAisle(name="Fresh stuffed pasta",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/arroces-y-pastas/pasta-fresca-rellena/OC20022018522?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Fresh_stuffed_pasta.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fresh_stuffed_pasta_detailed.json"))
   
    PASTA_SAUCE = StaticAisle(name="Pasta sauce",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/arroces-y-pastas/salsa-para-pasta/OC20022018523?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Pasta_sauce.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pasta_sauce_detailed.json"))
   
    SMOOTH_FRESH_PASTA = StaticAisle(name="Smooth fresh pasta",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/arroces-y-pastas/pasta-fresca-lisa/OC20022018524?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Smooth_fresh_pasta.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Smooth_fresh_pasta_detailed.json"))
   
    aisles: Final[List[StaticAisle]] = [REFRIGERATED_PASTA_DISHES, FRESH_STUFFED_PASTA, PASTA_SAUCE, SMOOTH_FRESH_PASTA]
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
                case "REFRIGERATED_PASTA_DISHES":
                    aisles = [cls.REFRIGERATED_PASTA_DISHES]
                case "FRESH_STUFFED_PASTA":
                    aisles = [cls.FRESH_STUFFED_PASTA]
                case "PASTA_SAUCE":
                    aisles = [cls.PASTA_SAUCE]
                case "SMOOTH_FRESH_PASTA":
                    aisles = [cls.SMOOTH_FRESH_PASTA]
              
        return aisles
    
class AlcampoPreparedOtherSpecialitiesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Prepared_Other_specialities")

    REFRIGERATED_COOKED_MEALS = StaticAisle(name="Refrigerated cooked meals",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/otras-especialidades/platos-cocinados-refrigerados/OC094271?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Refrigerated_cooked_meals.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Refrigerated_cooked_meals_detailed.json"))
   
    REFRIGERATED_CROQUETTES = StaticAisle(name="Refrigerated croquettes",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/otras-especialidades/croquetas-refrigeradas/OC094272?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Refrigerated_croquettes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Refrigerated_croquettes_detailed.json"))
   
    SAUCES = StaticAisle(name="Sauces",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/otras-especialidades/salsas/OC094273?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Sauces.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sauces_detailed.json"))
   
    APPETIZERS = StaticAisle(name="Appetizers",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/otras-especialidades/aperitivos/OC094275?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Appetizers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Appetizers_detailed.json"))
   
    aisles: Final[List[StaticAisle]] = [REFRIGERATED_COOKED_MEALS, REFRIGERATED_CROQUETTES, SAUCES, APPETIZERS]
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
                case "REFRIGERATED_COOKED_MEALS":
                    aisles = [cls.REFRIGERATED_COOKED_MEALS]
                case "REFRIGERATED_CROQUETTES":
                    aisles = [cls.REFRIGERATED_CROQUETTES]
                case "SAUCES":
                    aisles = [cls.SAUCES]
                case "APPETIZERS":
                    aisles = [cls.APPETIZERS]
              
        return aisles
    
class AlcampoPreparedHummusAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Prepared_Hummus")

    HUMMUS_AND_GUACAMOLE = StaticAisle(name="Hummus and guacamole",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/hummus-guacamole-y-otros/hummus-y-guacamole/OC0908201811?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Hummus_and_guacamole.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Hummus_and_guacamole_detailed.json"))
   
    aisles: Final[List[StaticAisle]] = [HUMMUS_AND_GUACAMOLE]
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
                case "HUMMUS_AND_GUACAMOLE":
                    aisles = [cls.HUMMUS_AND_GUACAMOLE]
              
        return aisles
    
class AlcampoPreparedInternationalDishesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Prepared_International_dishes")

    REFRIGERATED_MEXICAN_DISHES = StaticAisle(name="Refrigerated Mexican Dishes",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/platos-internacionales/platos-mexicanos-refrigerados/OC094211?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Refrigerated_Mexican_Dishes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Refrigerated_Mexican_Dishes_detailed.json"))
   
    OTHER_INTERNATIONAL_DISHES = StaticAisle(name="Other international dishes",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/platos-internacionales/otros-platos-internacionales/OC094212?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Other_international_dishes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_international_dishes_detailed.json"))
   
    aisles: Final[List[StaticAisle]] = [REFRIGERATED_MEXICAN_DISHES, OTHER_INTERNATIONAL_DISHES]
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
                case "REFRIGERATED_MEXICAN_DISHES":
                    aisles = [cls.REFRIGERATED_MEXICAN_DISHES]
                case "OTHER_INTERNATIONAL_DISHES":
                    aisles = [cls.OTHER_INTERNATIONAL_DISHES]
              
        return aisles
    
class AlcampoPreparedBassesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Prepared_basses")

    MASSES = StaticAisle(name="Masses",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/masas-y-bases/masas/OC09431?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Masses.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Masses_detailed.json"))
   
    BASES = StaticAisle(name="Bases",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/masas-y-bases/bases/OC09432?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Bases.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Bases_detailed.json"))
   
    aisles: Final[List[StaticAisle]] = [MASSES, BASES]
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
                case "MASSES":
                    aisles = [cls.MASSES]
                case "BASES":
                    aisles = [cls.BASES]
              
        return aisles
    
class AlcampoPreparedVegeterianFoodAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Prepared_vegeterian_food")

    VEGETARIAN_FOODS = StaticAisle(name="Vegetarian foods",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/alimentos-vegetarianos/OC09441?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Vegetarian_foods.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vegetarian_foods_detailed.json"))
  
    aisles: Final[List[StaticAisle]] = [VEGETARIAN_FOODS]
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
                case "VEGETARIAN_FOODS":
                    aisles = [cls.VEGETARIAN_FOODS]
             
        return aisles
    
class AlcampoPreparedSandwichAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Prepared_sandwich")

    SANDWICHES = StaticAisle(name="Sandwiches",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/s%C3%A1ndwiches-bocadillos-y-roscas/s%C3%A1ndwiches/OC20022018531?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Sandwiches.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sandwiches_detailed.json"))
  
    HAMBURGERS_AND_HOT_DOGS = StaticAisle(name="Hamburgers and hot dogs",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/s%C3%A1ndwiches-bocadillos-y-roscas/hamburguesas-y-perritos/OC20022018532?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Hamburgers_and_hot_dogs.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Hamburgers_and_hot_dogs_detailed.json"))
  
    THREADS = StaticAisle(name="Threads",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/s%C3%A1ndwiches-bocadillos-y-roscas/roscas/OC9417?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Threads.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Threads_detailed.json"))
  
    SANDWICHES_AND_WRAPS = StaticAisle(name="Sandwiches and wraps",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/s%C3%A1ndwiches-bocadillos-y-roscas/bocadillos-y-wraps/OC20022018533?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Sandwiches_and_wraps.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sandwiches_and_wraps_detailed.json"))
  
    aisles: Final[List[StaticAisle]] = [SANDWICHES, HAMBURGERS_AND_HOT_DOGS, THREADS, SANDWICHES_AND_WRAPS]
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
                case "SANDWICHES":
                    aisles = [cls.SANDWICHES]
                case "HAMBURGERS_AND_HOT_DOGS":
                    aisles = [cls.HAMBURGERS_AND_HOT_DOGS]
                case "THREADS":
                    aisles = [cls.THREADS]
                case "SANDWICHES_AND_WRAPS":
                    aisles = [cls.SANDWICHES_AND_WRAPS]
             
        return aisles
    
class AlcampoPreparedRoastMeatsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Prepared_roast_meats")

    MEAT_DISHES = StaticAisle(name="Meat dishes",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/asados-y-carnes/platos-de-carne/OC094231?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Meat_dishes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Meat_dishes_detailed.json"))
  
    ROTIS_AND_FILLINGS = StaticAisle(name="Rotis and fillings",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/asados-y-carnes/rotis-y-rellenos/OC094232?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Rotis_and_fillings.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Rotis_and_fillings_detailed.json"))
  
    ROASTED_CHICKEN = StaticAisle(name="Roasted chicken",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/asados-y-carnes/pollo-asado/OC094233?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Roasted_chicken.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Roasted_chicken_detailed.json"))
  
    ROAST_CASES = StaticAisle(name="Roast cases",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/asados-y-carnes/estuches-de-asados/OC094234?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Roast_cases.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Roast_cases_detailed.json"))
  
    OTHER_MEATS = StaticAisle(name="Other meats",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/asados-y-carnes/otras-carnes/OC094235?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Other_meats.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_meats_detailed.json"))
  
    CALLUSES_AND_EAR = StaticAisle(name="Calluses and ear",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/asados-y-carnes/callos-y-oreja/OC094236?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Calluses_and_ear.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Calluses_and_ear_detailed.json"))
  
    aisles: Final[List[StaticAisle]] = [MEAT_DISHES, ROTIS_AND_FILLINGS, ROASTED_CHICKEN, ROAST_CASES, OTHER_MEATS, CALLUSES_AND_EAR]
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
                case "MEAT_DISHES":
                    aisles = [cls.MEAT_DISHES]
                case "ROTIS_AND_FILLINGS":
                    aisles = [cls.ROTIS_AND_FILLINGS]
                case "ROASTED_CHICKEN":
                    aisles = [cls.ROASTED_CHICKEN]
                case "ROAST_CASES":
                    aisles = [cls.ROAST_CASES]
                case "OTHER_MEATS":
                    aisles = [cls.OTHER_MEATS]
                case "CALLUSES_AND_EAR":
                    aisles = [cls.CALLUSES_AND_EAR]
             
        return aisles
    
class AlcampoPreparedRefrigiratedSaladsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Prepared_refrigirated_salads")

    REFRIGERATED_SALADS = StaticAisle(name="Refrigerated salads",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/ensaladas-refrigeradas/OC9421?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Refrigerated_salads.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Refrigerated_salads_detailed.json"))
  
    aisles: Final[List[StaticAisle]] = [REFRIGERATED_SALADS]
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
                case "REFRIGERATED_SALADS":
                    aisles = [cls.REFRIGERATED_SALADS]
                
             
        return aisles
    
class AlcampoPreparedEmpanadasAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Prepared_Empanadas")

    BAKED_EMPANADAS = StaticAisle(name="Baked empanadas",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/empanadas/empanadas-horneadas/OC094281?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Baked_empanadas.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Baked_empanadas_detailed.json"))
  
    REFRIGERATED_EMPANADAS = StaticAisle(name="Refrigerated empanadas",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/empanadas/empanadas-refrigeradas/OC094282?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Refrigerated_empanadas.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Refrigerated_empanadas_detailed.json"))
  
    aisles: Final[List[StaticAisle]] = [BAKED_EMPANADAS, REFRIGERATED_EMPANADAS]
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
                case "BAKED_EMPANADAS":
                    aisles = [cls.BAKED_EMPANADAS]
                case "REFRIGERATED_EMPANADAS":
                    aisles = [cls.REFRIGERATED_EMPANADAS]
                
        return aisles
    
class AlcampoPreparedCannedDishesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Prepared_Canned_dishes")

    SNAILS = StaticAisle(name="Snails",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-c%C3%A1rnicas-platos-preparados-y-alm%C3%ADbares/platos-preparados-en-conserva/caracoles/OC1004041?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Snails.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Snails_detailed.json"))
  
    CALLUSES = StaticAisle(name="Calluses",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-c%C3%A1rnicas-platos-preparados-y-alm%C3%ADbares/platos-preparados-en-conserva/callos/OC1004042?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Calluses.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Calluses_detailed.json"))
  
    FABADAS_AND_BEANS = StaticAisle(name="Fabadas and beans",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-c%C3%A1rnicas-platos-preparados-y-alm%C3%ADbares/platos-preparados-en-conserva/fabadas-y-alubias/OC1004043?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Fabadas_and_beans.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fabadas_and_beans_detailed.json"))
  
    OTHER_LEGUMES = StaticAisle(name="Other legumes",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-c%C3%A1rnicas-platos-preparados-y-alm%C3%ADbares/platos-preparados-en-conserva/otras-legumbres/OC1004044?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Other_legumes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_legumes_detailed.json"))
  
    CANNED_PASTA = StaticAisle(name="Canned pasta",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-c%C3%A1rnicas-platos-preparados-y-alm%C3%ADbares/platos-preparados-en-conserva/pastas-lata/OC1004045?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Canned_pasta.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Canned_pasta_detailed.json"))
  
    FAST_FOOD = StaticAisle(name="Fast food",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-c%C3%A1rnicas-platos-preparados-y-alm%C3%ADbares/platos-preparados-en-conserva/cocina-r%C3%A1pida/OC1004046?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Fast_food.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fast_food_detailed.json"))
  
    MEATBALLS = StaticAisle(name="Meatballs",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-c%C3%A1rnicas-platos-preparados-y-alm%C3%ADbares/platos-preparados-en-conserva/albondigas/OC1004047?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Meatballs.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Meatballs_detailed.json"))
  
    PEPPERS_AND_VEGETABLES = StaticAisle(name="Peppers and vegetables",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-c%C3%A1rnicas-platos-preparados-y-alm%C3%ADbares/platos-preparados-en-conserva/pimientos-y-vegetales/OC1004048?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Peppers_and_vegetables.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Peppers_and_vegetables_detailed.json"))
  
    OTHER_SALADS = StaticAisle(name="Other salads",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-c%C3%A1rnicas-platos-preparados-y-alm%C3%ADbares/platos-preparados-en-conserva/otras-ensaladas/OC1004049?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Other_salads.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_salads_detailed.json"))
  
    TUNA_SALADS_AND_SALADS = StaticAisle(name="Tuna salads and salads",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-c%C3%A1rnicas-platos-preparados-y-alm%C3%ADbares/platos-preparados-en-conserva/ensaladas-at%C3%BAn-y-ensaladillas/OC10040410?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Tuna_salads_and_salads.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tuna_salads_and_salads_detailed.json"))
    
    COLD_CAKES = StaticAisle(name="Cold cakes",  url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-c%C3%A1rnicas-platos-preparados-y-alm%C3%ADbares/platos-preparados-en-conserva/pasteles-fr%C3%ADos/OC1004050?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cold_cakes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cold_cakes_detailed.json"))
  
    aisles: Final[List[StaticAisle]] = [SNAILS, CALLUSES, FABADAS_AND_BEANS, OTHER_LEGUMES, CANNED_PASTA, FAST_FOOD, MEATBALLS, PEPPERS_AND_VEGETABLES, OTHER_SALADS, TUNA_SALADS_AND_SALADS, COLD_CAKES]
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
                case "SNAILS":
                    aisles = [cls.SNAILS]
                case "CALLUSES":
                    aisles = [cls.CALLUSES]
                case "FABADAS_AND_BEANS":
                    aisles = [cls.FABADAS_AND_BEANS]
                case "OTHER_LEGUMES":
                    aisles = [cls.OTHER_LEGUMES]
                case "CANNED_PASTA":
                    aisles = [cls.CANNED_PASTA]
                case "FAST_FOOD":
                    aisles = [cls.FAST_FOOD]
                case "MEATBALLS":
                    aisles = [cls.MEATBALLS]
                case "PEPPERS_AND_VEGETABLES":
                    aisles = [cls.PEPPERS_AND_VEGETABLES]
                case "OTHER_SALADS":
                    aisles = [cls.OTHER_SALADS]
                case "TUNA_SALADS_AND_SALADS":
                    aisles = [cls.TUNA_SALADS_AND_SALADS]
                case "COLD_CAKES":
                    aisles = [cls.COLD_CAKES]
                
        return aisles
    
class AlcampoPreparedEssentialsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Prepared_Essentials_AirFryer")

    VEGETABLE_PROTEIN_DISHES = StaticAisle(name="Vegetable protein dishes",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/esenciales-para-tu-freidora-de-aire/platos-de-prote%C3%ADna-vegetal/OCcpfreiaire3?sortBy=favorite",
                                     original_file_uri=os.path.join(category_path(), "Vegetable_protein_dishes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vegetable_protein_dishes_detailed.json"))
  
    SPECIALTIES = StaticAisle(name="Specialties",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/esenciales-para-tu-freidora-de-aire/especialidades/OCcpfreiaire2?sortBy=favorite",
                                     original_file_uri=os.path.join(category_path(), "Specialties.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Specialties_detailed.json"))
  
    PIZZAS_AND_BAGELS = StaticAisle(name="Pizzas and bagels",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/esenciales-para-tu-freidora-de-aire/pizzas-y-roscas/OCcpfreiaire1?sortBy=favorite",
                                     original_file_uri=os.path.join(category_path(), "Pizzas_and_bagels.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pizzas_and_bagels_detailed.json"))
  
    INTERNATIONAL_PREPARED_FOOD = StaticAisle(name="International prepared food",  url="https://www.compraonline.alcampo.es/categories/comida-preparada/esenciales-para-tu-freidora-de-aire/comida-preparada-internacional/OCcpfreiaire4?sortBy=favorite",
                                     original_file_uri=os.path.join(category_path(), "International_prepared_food.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "International_prepared_food_detailed.json"))
  
   
  
    aisles: Final[List[StaticAisle]] = [VEGETABLE_PROTEIN_DISHES, SPECIALTIES, PIZZAS_AND_BAGELS, INTERNATIONAL_PREPARED_FOOD]
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
                case "VEGETABLE_PROTEIN_DISHES":
                    aisles = [cls.VEGETABLE_PROTEIN_DISHES]
                case "SPECIALTIES":
                    aisles = [cls.SPECIALTIES]
                case "PIZZAS_AND_BAGELS":
                    aisles = [cls.PIZZAS_AND_BAGELS]
                case "INTERNATIONAL_PREPARED_FOOD":
                    aisles = [cls.INTERNATIONAL_PREPARED_FOOD]
                
        return aisles
    
#Drinks

class AlcampoDrinksSoftDrinksAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Drinks_Soft_drinks")

    COLA_SOFT_DRINK = StaticAisle(name="Cola soft drink",  url="https://www.compraonline.alcampo.es/categories/bebidas/refrescos/refresco-de-cola/OCRefrescoCola?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cola_soft_drink.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cola_soft_drink_detailed.json"))
  
    ORANGE_SODA = StaticAisle(name="Orange soda",  url="https://www.compraonline.alcampo.es/categories/bebidas/refrescos/refresco-de-naranja/OCRefrescoNaranja?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Orange_soda.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Orange_soda_detailed.json"))
  
    LEMON_AND_LIME_SODA = StaticAisle(name="Lemon and lime soda",  url="https://www.compraonline.alcampo.es/categories/bebidas/refrescos/refresco-de-lim%C3%B3n-y-lima-lim%C3%B3n/OCRefrescoLimon?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Lemon_and_lime_soda.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Lemon_and_lime_soda_detailed.json"))
  
    ENERGY_DRINKS = StaticAisle(name="Energy drinks",  url="https://www.compraonline.alcampo.es/categories/bebidas/refrescos/bebidas-energ%C3%A9ticas/OC110311?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Energy_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Energy_drinks_detailed.json"))
  
    ISOTONIC_DRINKS = StaticAisle(name="Isotonic drinks",  url="https://www.compraonline.alcampo.es/categories/bebidas/refrescos/bebidas-isot%C3%B3nicas/OC1103111?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Isotonic_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Isotonic_drinks_detailed.json"))
  
    TEAS_AND_OTHER_FLAVORS = StaticAisle(name="Teas and other flavors",  url="https://www.compraonline.alcampo.es/categories/bebidas/refrescos/t%C3%A9s-y-otros-sabores/OC110308?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Teas_and_other_flavors.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Teas_and_other_flavors_detailed.json"))
  
    POWDERED_SOFT_DRINKS = StaticAisle(name="Powdered soft drinks",  url="https://www.compraonline.alcampo.es/categories/bebidas/refrescos/refrescos-en-polvo/OC110310?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Powdered_soft_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Powdered_soft_drinks_detailed.json"))
  
    TONIC_AND_BITTER = StaticAisle(name="Tonic and Bitter",  url="https://www.compraonline.alcampo.es/categories/bebidas/refrescos/t%C3%B3nica-y-bitter/OC110303?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Tonic_and_Bitter.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tonic_and_Bitter_detailed.json"))
  
  
    aisles: Final[List[StaticAisle]] = [COLA_SOFT_DRINK, ORANGE_SODA, LEMON_AND_LIME_SODA, ENERGY_DRINKS, ISOTONIC_DRINKS, TEAS_AND_OTHER_FLAVORS, POWDERED_SOFT_DRINKS, TONIC_AND_BITTER]
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
                case "COLA_SOFT_DRINK":
                    aisles = [cls.COLA_SOFT_DRINK]
                case "ORANGE_SODA":
                    aisles = [cls.ORANGE_SODA]
                case "LEMON_AND_LIME_SODA":
                    aisles = [cls.LEMON_AND_LIME_SODA]
                case "ENERGY_DRINKS":
                    aisles = [cls.ENERGY_DRINKS]
                case "ISOTONIC_DRINKS":
                    aisles = [cls.ISOTONIC_DRINKS]
                case "TEAS_AND_OTHER_FLAVORS":
                    aisles = [cls.TEAS_AND_OTHER_FLAVORS]
                case "POWDERED_SOFT_DRINKS":
                    aisles = [cls.POWDERED_SOFT_DRINKS]
                case "TONIC_AND_BITTER":
                    aisles = [cls.TONIC_AND_BITTER]
                
        return aisles
    
class AlcampoDrinksWaterSodaAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Drinks_Water_soda")

    STILL_WATERS = StaticAisle(name="Still waters",  url="https://www.compraonline.alcampo.es/categories/bebidas/agua-soda-y-gaseosas/aguas-sin-gas/OC1101041?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Still_waters.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Still_waters_detailed.json"))
  
    SPARKLING_WATER = StaticAisle(name="Sparkling water",  url="https://www.compraonline.alcampo.es/categories/bebidas/agua-soda-y-gaseosas/aguas-con-gas/OC1101042?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Sparkling_water.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sparkling_water_detailed.json"))
  
    FLAVORED_WATERS = StaticAisle(name="Flavored waters",  url="https://www.compraonline.alcampo.es/categories/bebidas/agua-soda-y-gaseosas/aguas-sabores/OC1101043?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Flavored_waters.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Flavored_waters_detailed.json"))
  
    SODA_AND_SOFT_DRINK = StaticAisle(name="Soda and Soft Drink",  url="https://www.compraonline.alcampo.es/categories/bebidas/agua-soda-y-gaseosas/gaseosa-y-soda/OCgaseosaysoda?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Soda_and_Soft_Drink.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Soda_and_Soft_Drink_detailed.json"))
  
    aisles: Final[List[StaticAisle]] = [STILL_WATERS, SPARKLING_WATER, FLAVORED_WATERS, SODA_AND_SOFT_DRINK]
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
                case "STILL_WATERS":
                    aisles = [cls.STILL_WATERS]
                case "SPARKLING_WATER":
                    aisles = [cls.SPARKLING_WATER]
                case "FLAVORED_WATERS":
                    aisles = [cls.FLAVORED_WATERS]
                case "SODA_AND_SOFT_DRINK":
                    aisles = [cls.SODA_AND_SOFT_DRINK]
                
        return aisles
    
class AlcampoDrinksJuicesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Drinks_juices")

    REFRIGERADOS = StaticAisle(name="Refrigerados",  url="https://www.compraonline.alcampo.es/categories/bebidas/zumos-de-frutas/refrigerados/OC110209?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Refrigerados.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Refrigerados_detailed.json"))
  
    JUICES_WITH_MILK = StaticAisle(name="Juices with milk",  url="https://www.compraonline.alcampo.es/categories/bebidas/zumos-de-frutas/zumos-con-leche-soja/OC6331072?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Juices_with_milk.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Juices_with_milk_detailed.json"))
  
    NECTAR = StaticAisle(name="Nectar",  url="https://www.compraonline.alcampo.es/categories/bebidas/zumos-de-frutas/n%C3%A9ctar-concentrados-y-exprimidos/OC633107?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Nectar.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Nectar_detailed.json"))
  
    JUICE_DRINKS = StaticAisle(name="Juice drinks",  url="https://www.compraonline.alcampo.es/categories/bebidas/zumos-de-frutas/refrescos-de-zumo/OC6331071?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Juice_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Juice_drinks_detailed.json"))
  
    MINI_BRICK = StaticAisle(name="Mini Brick",  url="https://www.compraonline.alcampo.es/categories/bebidas/zumos-de-frutas/mini-brick/OC110207?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Mini_Brick.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mini_Brick_detailed.json"))
  
    MUST = StaticAisle(name="Must",  url="https://www.compraonline.alcampo.es/categories/bebidas/zumos-de-frutas/mosto/OC110208?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Must.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Must_detailed.json"))
  
    NO_ADDED_SUGARS = StaticAisle(name="No added sugars",  url="https://www.compraonline.alcampo.es/categories/bebidas/zumos-de-frutas/sin-az%C3%BAcares-a%C3%B1adidos/OC110210?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "No_added_sugars.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "No_added_sugars_detailed.json"))
  
    aisles: Final[List[StaticAisle]] = [REFRIGERADOS, JUICES_WITH_MILK, NECTAR, JUICE_DRINKS, MINI_BRICK, MUST, NO_ADDED_SUGARS]
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
                case "REFRIGERADOS":
                    aisles = [cls.REFRIGERADOS]
                case "JUICES_WITH_MILK":
                    aisles = [cls.JUICES_WITH_MILK]
                case "NECTAR":
                    aisles = [cls.NECTAR]
                case "JUICE_DRINKS":
                    aisles = [cls.JUICE_DRINKS]
                case "MINI_BRICK":
                    aisles = [cls.MINI_BRICK]
                case "MUST":
                    aisles = [cls.MUST]
                case "NO_ADDED_SUGARS":
                    aisles = [cls.NO_ADDED_SUGARS]
                
        return aisles
    
class AlcampoDrinksBeersAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Drinks_Beers")

    STANDARD_CAN_OF_BEER = StaticAisle(name="Standard can of beer",  url="https://www.compraonline.alcampo.es/categories/bebidas/cervezas/cerveza-lata-est%C3%A1ndar/OC110701?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Standard_can_of_beer.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Standard_can_of_beer_detailed.json"))
  
    STANDARD_BOTTLE_BEER = StaticAisle(name="Standard bottle beer",  url="https://www.compraonline.alcampo.es/categories/bebidas/cervezas/cerveza-botella-est%C3%A1ndar/OC110703?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Standard_bottle_beer.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Standard_bottle_beer_detailed.json"))
  
    PREMIUM_BEERS = StaticAisle(name="Premium beers",  url="https://www.compraonline.alcampo.es/categories/bebidas/cervezas/cervezas-premium/OC110713?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Premium_beers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Premium_beers_detailed.json"))
  
    LARGE_FORMAT_BEERS = StaticAisle(name="Large format beers",  url="https://www.compraonline.alcampo.es/categories/bebidas/cervezas/cervezas-gran-formato/OC110702?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Large_format_beers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Large_format_beers_detailed.json"))
  
    RADLER_AND_OTHER_FLAVORS = StaticAisle(name="Radler and other flavors",  url="https://www.compraonline.alcampo.es/categories/bebidas/cervezas/radler-y-otros-sabores/OC110714?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Radler_and_other_flavors.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Radler_and_other_flavors_detailed.json"))
  
    NON_ALCOHOLIC_BEERS = StaticAisle(name="Non-alcoholic beers",  url="https://www.compraonline.alcampo.es/categories/bebidas/cervezas/cervezas-sin-alcohol/OC110712?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Non_alcoholic_beers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Non_alcoholic_beers_detailed.json"))
  
    CASES_OF_BEER = StaticAisle(name="Cases of beer",  url="https://www.compraonline.alcampo.es/categories/bebidas/cervezas/estuches-de-cerveza/OC110718?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cases_of_beer.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cases_of_beer_detailed.json"))
  
    BEER_OFFERS = StaticAisle(name="Beer offers",  url="https://www.compraonline.alcampo.es/categories/bebidas/cervezas/ofertas-de-cerveza/OCOfertasAlimentacion?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Beer_offers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Beer_offers_detailed.json"))
  
    LOCAL_BEERS = StaticAisle(name="Local beers",  url="https://www.compraonline.alcampo.es/categories/bebidas/cervezas/cervezas-locales/OC110717?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Local_beers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Local_beers_detailed.json"))
  
    aisles: Final[List[StaticAisle]] = [STANDARD_CAN_OF_BEER, STANDARD_BOTTLE_BEER, PREMIUM_BEERS, LARGE_FORMAT_BEERS, RADLER_AND_OTHER_FLAVORS, NON_ALCOHOLIC_BEERS, CASES_OF_BEER, BEER_OFFERS, LOCAL_BEERS]
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
                case "STANDARD_CAN_OF_BEER":
                    aisles = [cls.STANDARD_CAN_OF_BEER]
                case "STANDARD_BOTTLE_BEER":
                    aisles = [cls.STANDARD_BOTTLE_BEER]
                case "PREMIUM_BEERS":
                    aisles = [cls.PREMIUM_BEERS]
                case "LARGE_FORMAT_BEERS":
                    aisles = [cls.LARGE_FORMAT_BEERS]
                case "RADLER_AND_OTHER_FLAVORS":
                    aisles = [cls.RADLER_AND_OTHER_FLAVORS]
                case "NON_ALCOHOLIC_BEERS":
                    aisles = [cls.NON_ALCOHOLIC_BEERS]
                case "CASES_OF_BEER":
                    aisles = [cls.CASES_OF_BEER]
                case "BEER_OFFERS":
                    aisles = [cls.BEER_OFFERS]
                case "LOCAL_BEERS":
                    aisles = [cls.LOCAL_BEERS]
                
        return aisles
    
class AlcampoDrinksRedWineAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Drinks_Red_wine")

    RIOJA = StaticAisle(name="Rioja",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-tinto/rioja/OC11511?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Rioja.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Rioja_detailed.json"))
  
    RIBERA_DEL_DUERO = StaticAisle(name="Ribera del Duero",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-tinto/ribera-del-duero/OC11512?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Ribera_del_Duero.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Ribera_del_Duero_detailed.json"))
  
    TORO_AND_OTHER_DOS_OF_CASTILLA_Y_LEÓN = StaticAisle(name="Toro and other DOs of Castilla y León",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-tinto/toro-y-otras-d-o-s-de-castilla-y-le%C3%B3n/OC11513?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Toro_and_other_DOs_of_Castilla_y_León.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Toro_and_other_DOs_of_Castilla_y_León_detailed.json"))
  
    SOMONTANO = StaticAisle(name="Somontano",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-tinto/somontano-y-otras-d-o-s-de-arag%C3%B3n/OC15525?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Somontano.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Somontano_detailed.json"))
  
    VALDEPEÑAS = StaticAisle(name="Valdepeñas",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-tinto/valdepe%C3%B1as-y-otras-d-o-s-de-castilla-la-mancha/OC11515?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Valdepeñas.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Valdepeñas_detailed.json"))
  
    PENEDÉS = StaticAisle(name="Penedés",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-tinto/pened%C3%A9s-y-otras-d-o-s-de-catalu%C3%B1a/OC11516?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Penedés.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Penedés_detailed.json"))
  
    WINES_OF_NAVARRA = StaticAisle(name="Wines of Navarra",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-tinto/vinos-comunidad-valenciana-y-baleares/OC111213005?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Wines_of_Navarra.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Wines_of_Navarra_detailed.json"))
  
    WINES_FROM_THE_VALENCIAN_COMMUNITY = StaticAisle(name="Wines from the Valencian Community ",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-tinto/vinos-comunidad-valenciana-y-baleares/OC111213005?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Wines_from_the_Valencian_Community .json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Wines_from_the_Valencian_Community_detailed.json"))
  
    OTHER_DOS = StaticAisle(name="Other DOs",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-tinto/otras-d-o/OC111213006?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Other_DOs.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_DOs_detailed.json"))
  
    ORGANIC_WINES = StaticAisle(name="Organic Wines",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-tinto/vinos-ecol%C3%B3gicos/OC11519?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Wines.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Wines_detailed.json"))
  
    INTERNATIONAL_WINES = StaticAisle(name="International wines",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-tinto/vinos-internacionales/OC11518?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "International_wines.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "International_wines_detailed.json"))
  
    SPECIAL_FORMATS = StaticAisle(name="Special Formats",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-tinto/formatos-especiales/OC115110?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Special_Formats.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Special_Formats_detailed.json"))
  
    WINE_CASES = StaticAisle(name="Wine cases",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-tinto/estuches-de-vino/OC111009?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Wine_cases.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Wine_cases_detailed.json"))
  
  
    aisles: Final[List[StaticAisle]] = [RIOJA, RIBERA_DEL_DUERO, TORO_AND_OTHER_DOS_OF_CASTILLA_Y_LEÓN, SOMONTANO, VALDEPEÑAS, PENEDÉS, WINES_OF_NAVARRA, WINES_FROM_THE_VALENCIAN_COMMUNITY, OTHER_DOS, 
                                        ORGANIC_WINES, INTERNATIONAL_WINES, SPECIAL_FORMATS, WINE_CASES]
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
                case "RIOJA":
                    aisles = [cls.RIOJA]
                case "RIBERA_DEL_DUERO":
                    aisles = [cls.RIBERA_DEL_DUERO]
                case "TORO_AND_OTHER_DOS_OF_CASTILLA_Y_LEÓN":
                    aisles = [cls.TORO_AND_OTHER_DOS_OF_CASTILLA_Y_LEÓN]
                case "SOMONTANO":
                    aisles = [cls.SOMONTANO]
                case "VALDEPEÑAS":
                    aisles = [cls.VALDEPEÑAS]
                case "PENEDÉS":
                    aisles = [cls.PENEDÉS]
                case "WINES_OF_NAVARRA":
                    aisles = [cls.WINES_OF_NAVARRA]
                case "WINES_FROM_THE_VALENCIAN_COMMUNITY":
                    aisles = [cls.WINES_FROM_THE_VALENCIAN_COMMUNITY]
                case "OTHER_DOS":
                    aisles = [cls.OTHER_DOS]
                case "ORGANIC_WINES":
                    aisles = [cls.ORGANIC_WINES]
                case "INTERNATIONAL_WINES":
                    aisles = [cls.INTERNATIONAL_WINES]
                case "SPECIAL_FORMATS":
                    aisles = [cls.SPECIAL_FORMATS]
                case "WINE_CASES":
                    aisles = [cls.WINE_CASES]
                
                
        return aisles
    
class AlcampoDrinksWhiteWineAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Drinks_White_wine")

    
    RUEDA = StaticAisle(name="Rueda",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-blanco/rueda-y-otras-d-o-s-castilla-y-le%C3%B3n/OC11522?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Rueda.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Rueda_detailed.json"))
  
    RÍAS_BAIXAS = StaticAisle(name="Rías Baixas",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-blanco/r%C3%ADas-baixas-y-otras-d-o-s-galicia/OC111003001?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Rías_Baixas.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Rías_Baixas_detailed.json"))
  
    SOMONTANO = StaticAisle(name="Somontano",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-blanco/somontano-y-otras-d-o-s-arag%C3%B3n/OC11525?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Somontano.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Somontano_detailed.json"))
    
    RIOJA = StaticAisle(name="Rioja",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-blanco/rioja/OC11524?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Rioja.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Rioja_detailed.json"))
    
    PENEDÉS = StaticAisle(name="Penedés",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-blanco/pened%C3%A9s-y-otras-d-o-s-catalu%C3%B1a/OC111007?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Penedés.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Penedés_detailed.json"))
    
    VALDEPEÑAS = StaticAisle(name="Valdepeñas",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-blanco/valdepe%C3%B1as-y-otras-d-o-castilla-la-mancha/OC11526?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Valdepeñas.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Valdepeñas_detailed.json"))
  
    WINES_OF_ANDALUSIA = StaticAisle(name="Wines of andalusia",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-blanco/vinos-de-andaluc%C3%ADa/OCAndaluciaBlanco?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Wines_of_Andalusia.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Wines_of_Andalusia_detailed.json"))
  
    OTHER_DOS = StaticAisle(name="Other DOs",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-blanco/otras-d-o/OC11527?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Other_DOs.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_DOs_detailed.json"))
    
    INTERNATIONAL_WINES = StaticAisle(name="International wines",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-blanco/vinos-internacionales/OC11529?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "International_wines.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "International_wines_detailed.json"))
  
    SPECIAL_FORMATS = StaticAisle(name="Special Formats",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-blanco/formatos-especiales/OC1152110?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Special_Formats.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Special_Formats_detailed.json"))
  
    aisles: Final[List[StaticAisle]] = [RUEDA, RÍAS_BAIXAS, SOMONTANO, RIOJA, PENEDÉS, VALDEPEÑAS, WINES_OF_ANDALUSIA, OTHER_DOS, INTERNATIONAL_WINES, SPECIAL_FORMATS]
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
                case "RUEDA":
                    aisles = [cls.RUEDA]
                case "RÍAS_BAIXAS":
                    aisles = [cls.RÍAS_BAIXAS]
                case "SOMONTANO":
                    aisles = [cls.SOMONTANO]
                case "RIOJA":
                    aisles = [cls.RIOJA]
                case "PENEDÉS":
                    aisles = [cls.PENEDÉS]
                case "VALDEPEÑAS":
                    aisles = [cls.VALDEPEÑAS]
                case "WINES_OF_ANDALUSIA":
                    aisles = [cls.WINES_OF_ANDALUSIA]
                case "OTHER_DOS":
                    aisles = [cls.OTHER_DOS]
                case "INTERNATIONAL_WINES":
                    aisles = [cls.INTERNATIONAL_WINES]
                case "SPECIAL_FORMATS":
                    aisles = [cls.SPECIAL_FORMATS]
                
        return aisles
    
class AlcampoDrinksRoséAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Drinks_Rosé")

    
    ROSÉ_WINE = StaticAisle(name="Rosé wine",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-rosados-frizzantes-dulces-y-olorosos/vino-rosado/OC11531?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Rosé_wine.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Rosé_wine_detailed.json"))
  
    SHERRY_WINES_SWEET_AND_DRY = StaticAisle(name="Sherry wines, sweet and dry",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-rosados-frizzantes-dulces-y-olorosos/vinos-de-jerez-dulces-y-secos/OC11532?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Sherry_wines_sweet_and_dry.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sherry_wines_sweet_and_dry_detailed.json"))
  
    TABLE_WINES_CARTONS_AND_CARAFES = StaticAisle(name="Table wines, cartons and carafes",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-rosados-frizzantes-dulces-y-olorosos/vinos-de-mesa-brik-y-garrafa/OC11533?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Table_wines_cartons_and_carafes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Table_wines_cartons_and_carafes_detailed.json"))
    
    FRIZZANTES = StaticAisle(name="Frizzantes",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-rosados-frizzantes-dulces-y-olorosos/frizzantes/OC11535?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Frizzantes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Frizzantes_detailed.json"))
    
    SANGRIAS = StaticAisle(name="Sangrias",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-rosados-frizzantes-dulces-y-olorosos/sangr%C3%ADas/OC110901?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Sangrias.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sangrias_detailed.json"))
  
    SUMMER_REDS = StaticAisle(name="Summer Reds",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-rosados-frizzantes-dulces-y-olorosos/tintos-de-verano/OC110904?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Summer_Reds.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Summer_Reds_detailed.json"))
  
    aisles: Final[List[StaticAisle]] = [ROSÉ_WINE, SHERRY_WINES_SWEET_AND_DRY, TABLE_WINES_CARTONS_AND_CARAFES, FRIZZANTES, SANGRIAS, SUMMER_REDS]
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
                case "ROSÉ_WINE":
                    aisles = [cls.ROSÉ_WINE]
                case "SHERRY_WINES_SWEET_AND_DRY":
                    aisles = [cls.SHERRY_WINES_SWEET_AND_DRY]
                case "TABLE_WINES_CARTONS_AND_CARAFES":
                    aisles = [cls.TABLE_WINES_CARTONS_AND_CARAFES]
                case "FRIZZANTES":
                    aisles = [cls.FRIZZANTES]
                case "SANGRIAS":
                    aisles = [cls.SANGRIAS]
                case "SUMMER_REDS":
                    aisles = [cls.SUMMER_REDS]
               
        return aisles
    
class AlcampoDrinksChampagneAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Drinks_Champagne")

    
    CAVAS_AND_CASES = StaticAisle(name="Cavas and cases",  url="https://www.compraonline.alcampo.es/categories/bebidas/champagne-cavas-y-sidras/cavas-y-estuches/OC11561?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cavas_and_cases.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cavas_and_cases_detailed.json"))
  
    CHAMPAGNE = StaticAisle(name="Champagne",  url="https://www.compraonline.alcampo.es/categories/bebidas/champagne-cavas-y-sidras/champagne/OC11562?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Champagne.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Champagne_detailed.json"))
  
    CIDERS = StaticAisle(name="Ciders",  url="https://www.compraonline.alcampo.es/categories/bebidas/champagne-cavas-y-sidras/sidras/OC11563?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Ciders.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Ciders_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [CAVAS_AND_CASES, CHAMPAGNE, CIDERS]
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
                case "CAVAS_AND_CASES":
                    aisles = [cls.CAVAS_AND_CASES]
                case "CHAMPAGNE":
                    aisles = [cls.CHAMPAGNE]
                case "CIDERS":
                    aisles = [cls.CIDERS]
                
        return aisles
    
class AlcampoDrinksAlcoholicBeveragesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Drinks_Alcoholic_beverages")

    
    GENEVA = StaticAisle(name="Geneva",  url="https://www.compraonline.alcampo.es/categories/bebidas/vino-rosados-frizzantes-dulces-y-olorosos/tintos-de-verano/OC110904?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Geneva.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Geneva_detailed.json"))
  
    WHISKEY = StaticAisle(name="Whiskey",  url="https://www.compraonline.alcampo.es/categories/bebidas/bebidas-alcoh%C3%B3licas/whisky/OC11542?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Whiskey.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Whiskey_detailed.json"))
  
    Rum = StaticAisle(name="Rum",  url="https://www.compraonline.alcampo.es/categories/bebidas/bebidas-alcoh%C3%B3licas/ron/OC11543?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Rum.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Rum_detailed.json"))
    
    VODKA = StaticAisle(name="Vodka",  url="https://www.compraonline.alcampo.es/categories/bebidas/bebidas-alcoh%C3%B3licas/vodka-y-tequila/OC11544?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Vodka.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vodka_detailed.json"))
  
    COGNAC = StaticAisle(name="Cognac",  url="https://www.compraonline.alcampo.es/categories/bebidas/bebidas-alcoh%C3%B3licas/brandy-y-cognac/OC11545?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cognac.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cognac_detailed.json"))
  
    MOJITOS = StaticAisle(name="Mojitos",  url="https://www.compraonline.alcampo.es/categories/bebidas/bebidas-alcoh%C3%B3licas/mojitos-cockteles-y-combinados/OC11546?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Mojitos.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mojitos_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [GENEVA, WHISKEY, Rum, VODKA, COGNAC, MOJITOS]
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
                case "GENEVA":
                    aisles = [cls.GENEVA]
                case "WHISKEY":
                    aisles = [cls.WHISKEY]
                case "Rum":
                    aisles = [cls.Rum]
                case "VODKA":
                    aisles = [cls.VODKA]
                case "COGNAC":
                    aisles = [cls.COGNAC]
                case "MOJITOS":
                    aisles = [cls.MOJITOS]
                
        return aisles
    
class AlcampoDrinksLiquorsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Drinks_Liquors")

    
    FRUIT_LIQUEUR = StaticAisle(name="Fruit Liqueur",  url="https://www.compraonline.alcampo.es/categories/bebidas/licores/licor-de-frutas/OC11551?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Fruit_Liqueur.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fruit_Liqueur_detailed.json"))
  
    SPIRITS = StaticAisle(name="Spirits",  url="https://www.compraonline.alcampo.es/categories/bebidas/licores/aguardientes-licores-y-orujos/OC11558?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Spirits.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Spirits_detailed.json"))
  
    CREAMS = StaticAisle(name="Creams",  url="https://www.compraonline.alcampo.es/categories/bebidas/licores/cremas/OC11553?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Creams.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Creams_detailed.json"))
    
    PACHARÁN = StaticAisle(name="Pacharán",  url="https://www.compraonline.alcampo.es/categories/bebidas/licores/pachar%C3%A1n/OC11552?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Pacharán.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pacharán_detailed.json"))
  
    VERMOUTH = StaticAisle(name="Vermouth",  url="https://www.compraonline.alcampo.es/categories/bebidas/licores/vermouth/OC11554?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Vermouth.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vermouth_detailed.json"))
  
    ANISE = StaticAisle(name="Anise",  url="https://www.compraonline.alcampo.es/categories/bebidas/licores/an%C3%ADs/OC11555?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Anise.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Anise_detailed.json"))
    
    PUNCH = StaticAisle(name="Punch",  url="https://www.compraonline.alcampo.es/categories/bebidas/licores/ponche/OC11556?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Punch.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Punch_detailed.json"))
  
    OTHER_ALCOHOLIC_SPIRITS = StaticAisle(name="Other alcoholic spirits",  url="https://www.compraonline.alcampo.es/categories/bebidas/licores/otros-licores-con-alcohol/OC11559?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Other_alcoholic_spirits.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_alcoholic_spirits_detailed.json"))
  
    NON_ALCOHOLIC_LIQUORS = StaticAisle(name="Non-alcoholic liquors",  url="https://www.compraonline.alcampo.es/categories/bebidas/licores/licores-sin-alcohol/OC11557?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Non_alcoholic_liquors.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Non_alcoholic_liquors_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [FRUIT_LIQUEUR, SPIRITS, CREAMS, PACHARÁN, VERMOUTH, ANISE, PUNCH, OTHER_ALCOHOLIC_SPIRITS, NON_ALCOHOLIC_LIQUORS]
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
                case "FRUIT_LIQUEUR":
                    aisles = [cls.FRUIT_LIQUEUR]
                case "SPIRITS":
                    aisles = [cls.SPIRITS]
                case "CREAMS":
                    aisles = [cls.CREAMS]
                case "PACHARÁN":
                    aisles = [cls.PACHARÁN]
                case "VERMOUTH":
                    aisles = [cls.VERMOUTH]
                case "ANISE":
                    aisles = [cls.ANISE]
                case "PUNCH":
                    aisles = [cls.PUNCH]
                case "OTHER_ALCOHOLIC_SPIRITS":
                    aisles = [cls.OTHER_ALCOHOLIC_SPIRITS]
                case "NON_ALCOHOLIC_LIQUORS":
                    aisles = [cls.NON_ALCOHOLIC_LIQUORS]
                
        return aisles
    
class AlcampoDrinksZero0Alimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Drinks_Zero_0")

    
    DRINKS_0 = StaticAisle(name="Drinks 0.0",  url="https://www.compraonline.alcampo.es/categories/bebidas/bebidas-0-0/OC250420222?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Drinks_0.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Drinks_0_detailed.json"))
  
    
    aisles: Final[List[StaticAisle]] = [DRINKS_0]
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
                case "DRINKS_0":
                    aisles = [cls.DRINKS_0]
                
                
        return aisles
    
class AlcampoDrinksNonAlcoholicWinesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Drinks_Non_alcoholic_wines")

    
    NON_ALCOHOLIC_WINES = StaticAisle(name="Non-alcoholic wines",  url="https://www.compraonline.alcampo.es/categories/bebidas/vinos-sin-alcohol/OC25042023?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Non_alcoholic_wines.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Non_alcoholic_wines_detailed.json"))
  
    
    aisles: Final[List[StaticAisle]] = [NON_ALCOHOLIC_WINES]
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
                case "NON_ALCOHOLIC_WINES":
                    aisles = [cls.NON_ALCOHOLIC_WINES]
                
                
        return aisles
    
class AlcampoDrinksOrganicWinesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Drinks_organic_wines")

    
    ORGANIC_WINES_AND_CAVAS = StaticAisle(name="Organic wines and cavas",  url="https://www.compraonline.alcampo.es/categories/bebidas/bebidas-ecol%C3%B3gicas/vinos-y-cavas-ecol%C3%B3gicos/OC1013031?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_wines_and_cavas.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_wines_and_cavas_detailed.json"))
  
    
    aisles: Final[List[StaticAisle]] = [ORGANIC_WINES_AND_CAVAS]
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
                case "ORGANIC_WINES_AND_CAVAS":
                    aisles = [cls.ORGANIC_WINES_AND_CAVAS]
             
        return aisles
    
#Organic_Supermarket

class AlcampoSupermarketOrganicProductAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Organic_Product")

    
    ORGANIC_VEGETABLES = StaticAisle(name="Organic Vegetables",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/producto-fresco-ecol%C3%B3gico/verduras-ecol%C3%B3gicas/OC26112021102?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Vegetables.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Vegetables_detailed.json"))

    ORGANIC_FRUITS = StaticAisle(name="Organic Fruits",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/producto-fresco-ecol%C3%B3gico/frutas-ecol%C3%B3gicas/OC26112021101?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Fruits.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Fruits_detailed.json"))
 
    ORGANIC_MEAT = StaticAisle(name="Organic Meat",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/producto-fresco-ecol%C3%B3gico/carne-ecol%C3%B3gica/OC26112021103?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Meat.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Meat_detailed.json"))
 
    ORGANIC_FISH = StaticAisle(name="Organic Fish",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/producto-fresco-ecol%C3%B3gico/pescado-ecol%C3%B3gico/OC2611202111?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Fish.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Fish_detailed.json"))
 
    ORGANIC_FROZEN_FOODS = StaticAisle(name="Organic Frozen Foods",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/producto-fresco-ecol%C3%B3gico/congelados-ecol%C3%B3gicos/OC2611202113?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Frozen_Foods.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Frozen_Foods_detailed.json"))
  
    ORGANIC_CHEESES = StaticAisle(name="Organic Cheeses",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/producto-fresco-ecol%C3%B3gico/quesos-ecol%C3%B3gicos/OC26112021106?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Cheeses.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Cheeses_detailed.json"))
  
    ORGANIC_PREPARED_DISHES = StaticAisle(name="Organic Prepared Dishes",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/producto-fresco-ecol%C3%B3gico/platos-preparados-ecol%C3%B3gicos/OC26112021107?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Prepared_Dishes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Prepared_Dishes_detailed.json"))
  
    ORGANIC_DELICATESSEN = StaticAisle(name="Organic Delicatessen",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/producto-fresco-ecol%C3%B3gico/charcuter%C3%ADa-ecol%C3%B3gica/OC26112021105?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Delicatessen.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Delicatessen_detailed.json"))
  
    
    aisles: Final[List[StaticAisle]] = [ORGANIC_VEGETABLES, ORGANIC_FRUITS, ORGANIC_MEAT, ORGANIC_FISH, ORGANIC_FROZEN_FOODS, ORGANIC_CHEESES, ORGANIC_PREPARED_DISHES, ORGANIC_DELICATESSEN]
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
                case "ORGANIC_VEGETABLES":
                    aisles = [cls.ORGANIC_VEGETABLES]
                case "ORGANIC_FRUITS":
                    aisles = [cls.ORGANIC_FRUITS]
                case "ORGANIC_MEAT":
                    aisles = [cls.ORGANIC_MEAT]
                case "ORGANIC_FISH":
                    aisles = [cls.ORGANIC_FISH]
                case "ORGANIC_FROZEN_FOODS":
                    aisles = [cls.ORGANIC_FROZEN_FOODS]
                case "ORGANIC_CHEESES":
                    aisles = [cls.ORGANIC_CHEESES]
                case "ORGANIC_PREPARED_DISHES":
                    aisles = [cls.ORGANIC_PREPARED_DISHES]
                case "ORGANIC_DELICATESSEN":
                    aisles = [cls.ORGANIC_DELICATESSEN]
            
        return aisles
    
class AlcampoSupermarketOrganicDairyAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Organic_Dairy")

    
    ORGANIC_MILK = StaticAisle(name="Organic milk",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/l%C3%A1cteos-y-huevos-de-producci%C3%B3n-ecol%C3%B3gica/leches-y-natas-ecol%C3%B3gicas/OC26112021221?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_milk.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_milk_detailed.json"))

    ORGANICALLY_PRODUCED_EGGS = StaticAisle(name="Organically produced eggs",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/l%C3%A1cteos-y-huevos-de-producci%C3%B3n-ecol%C3%B3gica/huevos-de-producci%C3%B3n-ecol%C3%B3gica/OC26112021222?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organically_produced_eggs.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organically_produced_eggs_detailed.json"))
 
    ORGANIC_YOGURTS = StaticAisle(name="Organic yogurts",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/l%C3%A1cteos-y-huevos-de-producci%C3%B3n-ecol%C3%B3gica/yogures-y-postres-ecol%C3%B3gicos/OC26112021223?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_yogurts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_yogurts_detailed.json"))
 
    ORGANIC_BUTTERS = StaticAisle(name="Organic butters",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/l%C3%A1cteos-y-huevos-de-producci%C3%B3n-ecol%C3%B3gica/mantequillas-y-margarinas-ecol%C3%B3gicas/OC26112021224?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_butters.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_butters_detailed.json"))
 
    ORGANIC_KEFIR = StaticAisle(name="Organic Kefir",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/l%C3%A1cteos-y-huevos-de-producci%C3%B3n-ecol%C3%B3gica/k%C3%A9fir-ecol%C3%B3gico/OC26112021225?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Kefir.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Kefir_detailed.json"))
  
    aisles: Final[List[StaticAisle]] = [ORGANIC_MILK, ORGANICALLY_PRODUCED_EGGS, ORGANIC_YOGURTS, ORGANIC_BUTTERS, ORGANIC_KEFIR]
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
                case "ORGANIC_MILK":
                    aisles = [cls.ORGANIC_MILK]
                case "ORGANICALLY_PRODUCED_EGGS":
                    aisles = [cls.ORGANICALLY_PRODUCED_EGGS]
                case "ORGANIC_YOGURTS":
                    aisles = [cls.ORGANIC_YOGURTS]
                case "ORGANIC_BUTTERS":
                    aisles = [cls.ORGANIC_BUTTERS]
                case "ORGANIC_KEFIR":
                    aisles = [cls.ORGANIC_KEFIR]
            
        return aisles
    
class AlcampoSupermarketOrganicPantryAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Organic_Pantry")

    
    ORGANIC_SNACKS = StaticAisle(name="Organic Snacks",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/tu-despensa-ecol%C3%B3gica/aperitivos-y-frutos-secos-ecol%C3%B3gicos/OC26112021214?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Snacks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Snacks_detailed.json"))

    ORGANIC_OLIVES = StaticAisle(name="Organic Olives",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/tu-despensa-ecol%C3%B3gica/aceitunas-y-encurtidos-ecol%C3%B3gicas/OC26112021211?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Olives.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Olives_detailed.json"))
 
    ORGANIC_CANNED_FISH = StaticAisle(name="Organic Canned Fish",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/tu-despensa-ecol%C3%B3gica/consevas-de-pescado-ecol%C3%B3gicas/OC26112021215?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Canned_fish.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Canned_fish_detailed.json"))
 
    ORGANIC_CANNED_VEGETABLES = StaticAisle(name="Organic Canned Vegetables",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/tu-despensa-ecol%C3%B3gica/conservas-vegetales-ecol%C3%B3gicas/OC26112021216?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Canned_Vegetables.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Canned_Vegetables_detailed.json"))
 
    ORGANIC_LEGUMES = StaticAisle(name="Organic Legumes",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/tu-despensa-ecol%C3%B3gica/legumbres-ecol%C3%B3gicas/OC26112021217?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Legumes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Legumes_detailed.json"))
  
    ORGANIC_PASTA = StaticAisle(name="Organic Pasta",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/tu-despensa-ecol%C3%B3gica/pasta-y-arroces-ecol%C3%B3gicos/OC26112021218?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Pasta.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Pasta_detailed.json"))

    ORGANIC_OILS = StaticAisle(name="Organic oils",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/tu-despensa-ecol%C3%B3gica/aceites-y-vinagres-ecol%C3%B3gicos/OC26112021219?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_oils.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_oils_detailed.json"))
 
    ORGANIC_SOUPS = StaticAisle(name="Organic soups",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/tu-despensa-ecol%C3%B3gica/sopas-y-platos-preparados-ecol%C3%B3gicos/OC261120212110?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_soups.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_soups_detailed.json"))
 
    ORGANIC_SAUCES = StaticAisle(name="Organic Sauces",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/tu-despensa-ecol%C3%B3gica/salsas-y-condimientos-ecol%C3%B3gicos/OC261120212111?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Sauces.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Sauces_detailed.json"))
 
    ORGANIC_PANCAKES = StaticAisle(name="Organic Pancakes",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/tu-despensa-ecol%C3%B3gica/tortitas-ecol%C3%B3gicas/OC26112021212?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Pancakes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Pancakes_detailed.json"))
  
    ORGANIC_FLOURS = StaticAisle(name="Organic Flours",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/tu-despensa-ecol%C3%B3gica/harinas-ecol%C3%B3gicas/OC26112021213?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Flours.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Flours_detailed.json"))
 
    ORGANIC_SEEDS = StaticAisle(name="Organic Seeds",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/tu-despensa-ecol%C3%B3gica/semillas-y-superalimentos-ecol%C3%B3gicos/OC261120212112?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Seeds.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Seeds_detailed.json"))
  
    aisles: Final[List[StaticAisle]] = [ORGANIC_SNACKS, ORGANIC_OLIVES, ORGANIC_CANNED_FISH, ORGANIC_CANNED_VEGETABLES, ORGANIC_LEGUMES, ORGANIC_PASTA, ORGANIC_OILS, ORGANIC_SOUPS, ORGANIC_SAUCES, 
                                        ORGANIC_PANCAKES, ORGANIC_FLOURS, ORGANIC_SEEDS]
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
                case "ORGANIC_SNACKS":
                    aisles = [cls.ORGANIC_SNACKS]
                case "ORGANIC_OLIVES":
                    aisles = [cls.ORGANIC_OLIVES]
                case "ORGANIC_CANNED_FISH":
                    aisles = [cls.ORGANIC_CANNED_FISH]
                case "ORGANIC_CANNED_VEGETABLES":
                    aisles = [cls.ORGANIC_CANNED_VEGETABLES]
                case "ORGANIC_LEGUMES":
                    aisles = [cls.ORGANIC_LEGUMES]
                case "ORGANIC_PASTA":
                    aisles = [cls.ORGANIC_PASTA]
                case "ORGANIC_OILS":
                    aisles = [cls.ORGANIC_OILS]
                case "ORGANIC_SOUPS":
                    aisles = [cls.ORGANIC_SOUPS]
                case "ORGANIC_SAUCES":
                    aisles = [cls.ORGANIC_SAUCES]
                case "ORGANIC_PANCAKES":
                    aisles = [cls.ORGANIC_PANCAKES]
                case "ORGANIC_FLOURS":
                    aisles = [cls.ORGANIC_FLOURS]
                case "ORGANIC_SEEDS":
                    aisles = [cls.ORGANIC_SEEDS]
                
        return aisles
    
class AlcampoSupermarketOrganicBreakfastAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Organic_Breakfast")

    
    ORGANIC_CEREALS = StaticAisle(name="Organic Cereals",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/desayunos-ecol%C3%B3gicos/cereales-ecol%C3%B3gicos/OC261120212311?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Cereals.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Cereals_detailed.json"))

    ORGANIC_INFUSIONS = StaticAisle(name="Organic Infusions",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/desayunos-ecol%C3%B3gicos/infusiones-y-caf%C3%A9-ecol%C3%B3gicos/OC261120212312?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Infusions.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Infusions_detailed.json"))
 
    ORGANIC_COOKIES = StaticAisle(name="Organic Cookies",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/desayunos-ecol%C3%B3gicos/galletas-ecol%C3%B3gicas/OC261120212313?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Cookies.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Cookies_detailed.json"))
 
    ORGANIC_SUGAR = StaticAisle(name="Organic Sugar",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/desayunos-ecol%C3%B3gicos/az%C3%BAcar-y-cacaos-ecol%C3%B3gicos/OC261120212314?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Sugar.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Sugar_detailed.json"))
 
    ORGANIC_JAMS = StaticAisle(name="Organic Jams",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/desayunos-ecol%C3%B3gicos/mermeladas-y-miel-ecol%C3%B3gicas/OC261120212315?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Jams.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Jams_detailed.json"))
  
    ORGANIC_CHOCOLATES = StaticAisle(name="Organic Chocolates",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/desayunos-ecol%C3%B3gicos/chocolates-ecol%C3%B3gicos/OC261120212316?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Chocolates.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Chocolates_detailed.json"))

    ORGANIC_BAKERY = StaticAisle(name="Organic Bakery",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/desayunos-ecol%C3%B3gicos/panader%C3%ADa-ecol%C3%B3gica/OC261120212317?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Bakery.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Bakery_detailed.json"))
 
    ORGANIC_PASTRY = StaticAisle(name="Organic Pastry",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/desayunos-ecol%C3%B3gicos/pasteler%C3%ADa-ecol%C3%B3gica/OC261120212318?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Pastry.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Pastry_detailed.json"))
 
  
    aisles: Final[List[StaticAisle]] = [ORGANIC_CEREALS, ORGANIC_INFUSIONS, ORGANIC_COOKIES, ORGANIC_SUGAR, ORGANIC_JAMS, ORGANIC_CHOCOLATES, ORGANIC_BAKERY, ORGANIC_PASTRY]
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
                case "ORGANIC_CEREALS":
                    aisles = [cls.ORGANIC_CEREALS]
                case "ORGANIC_INFUSIONS":
                    aisles = [cls.ORGANIC_INFUSIONS]
                case "ORGANIC_COOKIES":
                    aisles = [cls.ORGANIC_COOKIES]
                case "ORGANIC_SUGAR":
                    aisles = [cls.ORGANIC_SUGAR]
                case "ORGANIC_JAMS":
                    aisles = [cls.ORGANIC_JAMS]
                case "ORGANIC_CHOCOLATES":
                    aisles = [cls.ORGANIC_CHOCOLATES]
                case "ORGANIC_BAKERY":
                    aisles = [cls.ORGANIC_BAKERY]
                case "ORGANIC_PASTRY":
                    aisles = [cls.ORGANIC_PASTRY]
                
        return aisles
    
class AlcampoSupermarketOrganicDrinksAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Organic_Drinks")

    
    ORGANIC_WINES = StaticAisle(name="Organic wines",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/bebidas-ecol%C3%B3gicas/vinos-y-cavas-ecol%C3%B3gicos/OC2611202131?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_wines.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_wines_detailed.json"))

    ORGANIC_VEGETABLE_DRINKS = StaticAisle(name="Organic Vegetable Drinks",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/bebidas-ecol%C3%B3gicas/bebidas-vegetales-ecol%C3%B3gicas/OC2311202134?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Vegetable_Drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Vegetable_Drinks_detailed.json"))
 
    ORGANIC_BEERS = StaticAisle(name="Organic beers",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/bebidas-ecol%C3%B3gicas/cervezas-ecol%C3%B3gicas/OC2611202132?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_beers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_beers_detailed.json"))
 
    ORGANIC_JUICES = StaticAisle(name="Organic Juices",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/bebidas-ecol%C3%B3gicas/zumos-y-refrescos-ecol%C3%B3gicos/OC2611202133?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Juices.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Juices_detailed.json"))
 
    aisles: Final[List[StaticAisle]] = [ORGANIC_WINES, ORGANIC_VEGETABLE_DRINKS, ORGANIC_BEERS, ORGANIC_JUICES]
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
                case "ORGANIC_WINES":
                    aisles = [cls.ORGANIC_WINES]
                case "ORGANIC_VEGETABLE_DRINKS":
                    aisles = [cls.ORGANIC_VEGETABLE_DRINKS]
                case "ORGANIC_BEERS":
                    aisles = [cls.ORGANIC_BEERS]
                case "ORGANIC_JUICES":
                    aisles = [cls.ORGANIC_JUICES]
               
        return aisles
    
class AlcampoSupermarketOrganicBabyFoodAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Organic_BabyFood")

    
    ORGANIC_BABY_FOOD = StaticAisle(name="Organic baby food",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/alimentaci%C3%B3n-infantil-ecol%C3%B3gica/OC200520206?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_baby_food.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_baby_food_detailed.json"))

 
    aisles: Final[List[StaticAisle]] = [ORGANIC_BABY_FOOD]
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
                case "ORGANIC_BABY_FOOD":
                    aisles = [cls.ORGANIC_BABY_FOOD]
              
        return aisles
    
class AlcampoSupermarketFairTradeAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Organic_Fair_trade")

    
    FAIR_TRADE = StaticAisle(name="Fair Trade",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/comercio-justo/OC01062020?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Fair_Trade.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fair_Trade_detailed.json"))

 
    aisles: Final[List[StaticAisle]] = [FAIR_TRADE]
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
                case "FAIR_TRADE":
                    aisles = [cls.FAIR_TRADE]
              
        return aisles
    
#Gluten_Lactose-Free

class AlcampoGlutenFreeAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Gluten_Free")

    
    GLUTEN_FREE_BAKERY = StaticAisle(name="Gluten-free bakery",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/sin-gluten-apto-cel%C3%ADacos/panader%C3%ADa-sin-gluten/OC10120401?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Gluten_free_bakery.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Gluten_free_bakery_detailed.json"))
    
    GLUTEN_FREE_COOKIES = StaticAisle(name="Gluten-free cookies",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/sin-gluten-apto-cel%C3%ADacos/galletas-sin-gluten/OC10120404?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Gluten_free_cookies.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Gluten_free_cookies_detailed.json"))
    
    GLUTEN_FREE_PASTRIES = StaticAisle(name="Gluten-free pastries",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/sin-gluten-apto-cel%C3%ADacos/boller%C3%ADa-sin-gluten/OC10120402?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Gluten_free_pastries.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Gluten_free_pastries_detailed.json"))
    
    GLUTEN_FREE_PASTA = StaticAisle(name="Gluten-free pasta",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/sin-gluten-apto-cel%C3%ADacos/pastas-sin-gluten/OC10120405?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Gluten_free_pasta.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Gluten_free_pasta_detailed.json"))
    
    GLUTEN_FREE_CEREALS = StaticAisle(name="Gluten-free cereals",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/sin-gluten-apto-cel%C3%ADacos/cereales-y-barritas-sin-gluten/OC10120403?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Gluten_free_cereals.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Gluten_free_cereals_detailed.json"))
    
    GLUTEN_FREE_PREPARED_DISHES = StaticAisle(name="Gluten-free prepared dishes",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/sin-gluten-apto-cel%C3%ADacos/platos-preparados-sin-gluten/OC832?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Gluten_free_prepared_dishes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Gluten_free_prepared_dishes_detailed.json"))
    
    GLUTEN_FREE_PIZZA = StaticAisle(name="Gluten-free pizza",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/sin-gluten-apto-cel%C3%ADacos/pizza-sin-gluten/OC834?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Gluten_free_pizza.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Gluten_free_pizza_detailed.json"))
    
    OTHER_GLUTEN_FREE_PRODUCTS = StaticAisle(name="Other gluten-free products",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/sin-gluten-apto-cel%C3%ADacos/otros-productos-sin-gluten/OC10120407?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Other_gluten_free_products.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_gluten_free_products_detailed.json"))

    GLUTEN_FREE_BEERS = StaticAisle(name="Gluten-free Beers",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-nutrici%C3%B3n-deportiva-y-funcional/sin-gluten-apto-cel%C3%ADacos/cervezas-sin-gluten/OC10120406?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Gluten_free_Beers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Gluten_free_Beers_detailed.json"))
    
    GLUTEN_FREE_DOUGHTS = StaticAisle(name="Gluten-free Doughts",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-nutrici%C3%B3n-deportiva-y-funcional/sin-gluten-apto-cel%C3%ADacos/masas-y-bases-sin-gluten/OC835?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Gluten_free_doughts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Gluten_free_doughts_detailed.json"))
    
    GLUTEN_FREE_SNACKS = StaticAisle(name="Gluten-free snacks",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-nutrici%C3%B3n-deportiva-y-funcional/sin-gluten-apto-cel%C3%ADacos/snacks-y-tortitas-sin-gluten/OC10120408?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Gluten_free_snacks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Gluten_free_snacks_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [GLUTEN_FREE_BAKERY, GLUTEN_FREE_COOKIES, GLUTEN_FREE_PASTRIES, GLUTEN_FREE_PASTA, GLUTEN_FREE_CEREALS, GLUTEN_FREE_PREPARED_DISHES, GLUTEN_FREE_PIZZA, 
                                        OTHER_GLUTEN_FREE_PRODUCTS, GLUTEN_FREE_BEERS, GLUTEN_FREE_DOUGHTS, GLUTEN_FREE_SNACKS]
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
                case "GLUTEN_FREE_BAKERY":
                    aisles = [cls.GLUTEN_FREE_BAKERY]
                case "GLUTEN_FREE_COOKIES":
                    aisles = [cls.GLUTEN_FREE_COOKIES]
                case "GLUTEN_FREE_PASTRIES":
                    aisles = [cls.GLUTEN_FREE_PASTRIES]
                case "GLUTEN_FREE_PASTA":
                    aisles = [cls.GLUTEN_FREE_PASTA]
                case "GLUTEN_FREE_CEREALS":
                    aisles = [cls.GLUTEN_FREE_CEREALS]
                case "GLUTEN_FREE_PREPARED_DISHES":
                    aisles = [cls.GLUTEN_FREE_PREPARED_DISHES]
                case "GLUTEN_FREE_PIZZA":
                    aisles = [cls.GLUTEN_FREE_PIZZA]
                case "OTHER_GLUTEN_FREE_PRODUCTS":
                    aisles = [cls.OTHER_GLUTEN_FREE_PRODUCTS]
                case "GLUTEN_FREE_BEERS":
                    aisles = [cls.GLUTEN_FREE_BEERS]
                case "GLUTEN_FREE_DOUGHTS":
                    aisles = [cls.GLUTEN_FREE_DOUGHTS]
                case "GLUTEN_FREE_SNACKS":
                    aisles = [cls.GLUTEN_FREE_SNACKS]
              
        return aisles
    
class AlcampoGlutenLactoseFreeAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Gluten_Lactose_free")

    
    DELICATESSEN_AND_LACTOSE_FREE_PREPARED_DISHES = StaticAisle(name="Delicatessen and lactose-free prepared dishes",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/productos-sin-lactosa/charcuteria-y-platos-preparados-sin-lactosa/OC78?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Delicatessen_and_lactose_free_prepared_dishes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Delicatessen_and_lactose_free_prepared_dishes_detailed.json"))
    
    LACTOSE_FREE_YOGURTS = StaticAisle(name="Lactose-free yogurts",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/productos-sin-lactosa/yogures-y-postres-sin-lactosa/OC73?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Lactose_free_yogurts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Lactose_free_yogurts_detailed.json"))
    
    LACTOSE_FREE_CHEESES = StaticAisle(name="Lactose-free cheeses",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/productos-sin-lactosa/quesos-sin-lactosa/OC76?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Lactose_free_cheeses.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Lactose_free_cheeses_detailed.json"))
    
    LACTOSE_FREE_DAIRY = StaticAisle(name="Lactose-free  dairy",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/productos-sin-lactosa/l%C3%A1cteos-sin-lactosa/OC71?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Lactose_free_dairy.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Lactose_free_dairy_detailed.json"))
    
    LACTOSE_FREE_PANTRY = StaticAisle(name="Lactose-free pantry",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/productos-sin-lactosa/despensa-sin-lactosa/OC77?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Lactose_free_pantry.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Lactose_free_pantry_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [DELICATESSEN_AND_LACTOSE_FREE_PREPARED_DISHES, LACTOSE_FREE_YOGURTS, LACTOSE_FREE_CHEESES, LACTOSE_FREE_DAIRY, LACTOSE_FREE_PANTRY]
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
                case "DELICATESSEN_AND_LACTOSE_FREE_PREPARED_DISHES":
                    aisles = [cls.DELICATESSEN_AND_LACTOSE_FREE_PREPARED_DISHES]
                case "LACTOSE_FREE_YOGURTS":
                    aisles = [cls.LACTOSE_FREE_YOGURTS]
                case "LACTOSE_FREE_CHEESES":
                    aisles = [cls.LACTOSE_FREE_CHEESES]
                case "LACTOSE_FREE_DAIRY":
                    aisles = [cls.LACTOSE_FREE_DAIRY]
                case "LACTOSE_FREE_PANTRY":
                    aisles = [cls.LACTOSE_FREE_PANTRY]
            
        return aisles
    
class AlcampoGlutenSportsNutritionAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Gluten_Sports_nutrition")

    
    PROTEIN = StaticAisle(name="Protein",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/nutrici%C3%B3n-deportiva/prote%C3%ADna/OC121?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Protein.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Protein_detailed.json"))
    
    ENERGY = StaticAisle(name="Energy",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/nutrici%C3%B3n-deportiva/energ%C3%ADa/OC122?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Energy.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Energy_detailed.json"))
    
    FROZEN_SPORTS_NUTRITION_MEALS = StaticAisle(name="Frozen Sports Nutrition Meals",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/nutrici%C3%B3n-deportiva/platos-congelados-de-nutrici%C3%B3n-deportiva/OCPCND12?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Frozen_Sports_Nutrition_Meals.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Frozen_Sports_Nutrition_Meals_detailed.json"))
    
    ISOTONIC_DRINKS = StaticAisle(name="Isotonic drinks",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/nutrici%C3%B3n-deportiva/bebidas-isot%C3%B3nicas/OC1103111B?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Isotonic_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Isotonic_drinks_detailed.json"))
    
    BEST_SELLING_PRODUCTS = StaticAisle(name="Best-selling products",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/nutrici%C3%B3n-deportiva/productos-m%C3%A1s-vendidos/OC2080NutDep?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Best_selling_products.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Best_selling_products_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [PROTEIN, ENERGY, FROZEN_SPORTS_NUTRITION_MEALS, ISOTONIC_DRINKS, BEST_SELLING_PRODUCTS]
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
                case "PROTEIN":
                    aisles = [cls.PROTEIN]
                case "ENERGY":
                    aisles = [cls.ENERGY]
                case "FROZEN_SPORTS_NUTRITION_MEALS":
                    aisles = [cls.FROZEN_SPORTS_NUTRITION_MEALS]
                case "ISOTONIC_DRINKS":
                    aisles = [cls.ISOTONIC_DRINKS]
                case "BEST_SELLING_PRODUCTS":
                    aisles = [cls.BEST_SELLING_PRODUCTS]
            
        return aisles
    
class AlcampoGlutenNutritionalSupplementsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Gluten_Nutritional_supplements")

    
    DIGESTIVES = StaticAisle(name="Digestives",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/complementos-nutricionales/digestivos/OC10121002?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Digestives.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Digestives_detailed.json"))
    
    VITAMINS = StaticAisle(name="Vitamins",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/complementos-nutricionales/vitaminas-y-minerales/OC10121001?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Vitamins.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vitamins_detailed.json"))
    
    FLUID_RETENTION = StaticAisle(name="Fluid Retention",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/complementos-nutricionales/retenci%C3%B3n-de-l%C3%ADquidos-y-sistema-urinario/OC10120807?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Fluid_Retention.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fluid_Retention_detailed.json"))
    
    WEIGHT_CONTROL = StaticAisle(name="Weight Control",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/complementos-nutricionales/control-de-peso/OC10120806?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Weight_Control.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Weight_Control_detailed.json"))
    
    JELLIES = StaticAisle(name="Jellies",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/complementos-nutricionales/jaleas-y-propoleos/OC10121008?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Jellies.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Jellies_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [DIGESTIVES, VITAMINS, FLUID_RETENTION, WEIGHT_CONTROL, JELLIES]
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
                case "DIGESTIVES":
                    aisles = [cls.DIGESTIVES]
                case "VITAMINS":
                    aisles = [cls.VITAMINS]
                case "FLUID_RETENTION":
                    aisles = [cls.FLUID_RETENTION]
                case "WEIGHT_CONTROL":
                    aisles = [cls.WEIGHT_CONTROL]
                case "JELLIES":
                    aisles = [cls.JELLIES]
            
        return aisles
    
class AlcampoGlutenSeedsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Gluten_Seeds")

    
    SEEDS_AND_OTHER_CEREALS = StaticAisle(name="Seeds and other cereals",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/semillas-y-otros-cereales/OC10120102?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Seeds_and_other_cereals.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Seeds_and_other_cereals_detailed.json"))
    
    
    
    aisles: Final[List[StaticAisle]] = [SEEDS_AND_OTHER_CEREALS]
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
                case "SEEDS_AND_OTHER_CEREALS":
                    aisles = [cls.SEEDS_AND_OTHER_CEREALS]
                
        return aisles
    
class AlcampoGlutenDietAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Gluten_Diet")

    
    MAINTAIN_WEIGHT = StaticAisle(name="Maintain Weight",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/diet%C3%A9ticos-control-de-peso/mantener-peso/OC679774739?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Maintain_Weight.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Maintain_Weight_detailed.json"))
    
    LOSE_WEIGHT = StaticAisle(name="Lose weight",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/diet%C3%A9ticos-control-de-peso/perder-peso/OC679779771?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Lose_weight.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Lose_weight_detailed.json"))
    
    SPECIAL_DIETS = StaticAisle(name="Special Diets",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/diet%C3%A9ticos-control-de-peso/dietas-especiales/OC679779770?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Special_Diets.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Special_Diets_detailed.json"))
    
    BIMANAN_DIET = StaticAisle(name="Bimanan Diet",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/diet%C3%A9ticos-control-de-peso/dieta-bimanan/OC10120802?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Bimanan_Diet.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Bimanan_Diet_detailed.json"))
    
    BICENTURY_DIET = StaticAisle(name="Bicentury Diet",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/diet%C3%A9ticos-control-de-peso/dieta-bicentury/OC10120803?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Bicentury_Diet.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Bicentury_Diet_detailed.json"))
    
    BARS = StaticAisle(name="Bars",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/diet%C3%A9ticos-control-de-peso/barritas/OC10120809?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Bars.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Bars_detailed.json"))
    
    DIETARY_SUPPLEMENTS = StaticAisle(name="Dietary Supplements",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/diet%C3%A9ticos-control-de-peso/complementos-dietas/OC679779772?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Dietary_Supplements.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Dietary_Supplements_detailed.json"))
    
    
    
    aisles: Final[List[StaticAisle]] = [MAINTAIN_WEIGHT, LOSE_WEIGHT, SPECIAL_DIETS, BIMANAN_DIET, BICENTURY_DIET, BARS, DIETARY_SUPPLEMENTS]
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
                case "MAINTAIN_WEIGHT":
                    aisles = [cls.MAINTAIN_WEIGHT]
                case "LOSE_WEIGHT":
                    aisles = [cls.LOSE_WEIGHT]
                case "SPECIAL_DIETS":
                    aisles = [cls.SPECIAL_DIETS]
                case "BIMANAN_DIET":
                    aisles = [cls.BIMANAN_DIET]
                case "BICENTURY_DIET":
                    aisles = [cls.BICENTURY_DIET]
                case "BARS":
                    aisles = [cls.BARS]
                case "DIETARY_SUPPLEMENTS":
                    aisles = [cls.DIETARY_SUPPLEMENTS]
                
        return aisles
    
class AlcampoGlutenClassicDieteticsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Gluten_Classic_dietetics")

    
    DIET_COOKIES = StaticAisle(name="Diet Cookies",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/diet%C3%A9ticos-cl%C3%A1sicos/galletas-diet/OC1119824743?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Diet_Cookies.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Diet_Cookies_detailed.json"))
    
    DIET_BAKERY = StaticAisle(name="Diet Bakery",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/diet%C3%A9ticos-cl%C3%A1sicos/panader%C3%ADa-diet/OC1119829822?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Diet_Bakery.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Diet_Bakery_detailed.json"))
    
    DIET_CEREALS = StaticAisle(name="Diet Cereals",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/diet%C3%A9ticos-cl%C3%A1sicos/cereales-diet/OC1119829820?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Diet_Cereals.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Diet_Cereals_detailed.json"))
    
    OTHER_DIET_PRODUCTS = StaticAisle(name="Other Diet products",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/diet%C3%A9ticos-cl%C3%A1sicos/otros-productos-diet/OC1119829823?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Other_Diet_products.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_Diet_products_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [DIET_COOKIES, DIET_BAKERY, DIET_CEREALS, OTHER_DIET_PRODUCTS]
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
                case "DIET_COOKIES":
                    aisles = [cls.DIET_COOKIES]
                case "DIET_BAKERY":
                    aisles = [cls.DIET_BAKERY]
                case "DIET_CEREALS":
                    aisles = [cls.DIET_CEREALS]
                case "OTHER_DIET_PRODUCTS":
                    aisles = [cls.OTHER_DIET_PRODUCTS]
               
        return aisles
    
class AlcampoGlutenDietaryWithoutAddedSugarsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Gluten_Dietary_without_added_sugars")

    
    DIET_COOKIES_WITH_NO_ADDED_SUGARS = StaticAisle(name="Diet Cookies with no added sugars",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/diet%C3%A9ticos-sin-az%C3%BAcares-a%C3%B1adidos/galletas-diet-s-az%C3%BAcares-a%C3%B1adidos/OC1119849842?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Diet_Cookies_with_no_added_sugars.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Diet_Cookies_with_no_added_sugars_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [DIET_COOKIES_WITH_NO_ADDED_SUGARS]
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
                case "DIET_COOKIES_WITH_NO_ADDED_SUGARS":
                    aisles = [cls.DIET_COOKIES_WITH_NO_ADDED_SUGARS]
              
        return aisles
    
class AlcampoGlutenPancakeAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Gluten_Pancake")

    
    MINI_PANCAKES = StaticAisle(name="Mini pancakes",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/tortitas/mini-tortitas/OC10120304?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Mini_pancakes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mini_pancakes_detailed.json"))
    
    RICE_CAKES = StaticAisle(name="Rice Cakes",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/tortitas/tortitas-de-arroz/OC10120302?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Rice_Cakes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Rice_Cakes_detailed.json"))
    
    CORN_CAKES = StaticAisle(name="Corn Cakes",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/tortitas/tortitas-de-ma%C3%ADz/OC10120301?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Corn_Cakes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Corn_Cakes_detailed.json"))
    
    MULTIGRAIN_PANCAKES = StaticAisle(name="Multigrain pancakes",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/tortitas/tortitas-multicereales/OC10120303?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Multigrain_pancakes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Multigrain_pancakes_detailed.json"))
    
    ORGANIC_PANCAKES = StaticAisle(name="Organic Pancakes",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/tortitas/tortitas-ecol%C3%B3gicas/OC1162862167?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_Pancakes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_Pancakes_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [MINI_PANCAKES, RICE_CAKES, CORN_CAKES, MULTIGRAIN_PANCAKES, ORGANIC_PANCAKES]
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
                case "MINI_PANCAKES":
                    aisles = [cls.MINI_PANCAKES]
                case "RICE_CAKES":
                    aisles = [cls.RICE_CAKES]
                case "CORN_CAKES":
                    aisles = [cls.CORN_CAKES]
                case "MULTIGRAIN_PANCAKES":
                    aisles = [cls.MULTIGRAIN_PANCAKES]
                case "ORGANIC_PANCAKES":
                    aisles = [cls.ORGANIC_PANCAKES]
              
        return aisles
    
class AlcampoGlutenHerbalistAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Gluten_Herbalist")

    
    HERBALIST = StaticAisle(name="Herbalist",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/herbolario/OC0672074528?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Herbalist.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Herbalist_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [HERBALIST]
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
                case "HERBALIST":
                    aisles = [cls.HERBALIST]
               
        return aisles
    
class AlcampoGlutenFunctionalFoodsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Gluten_Functional_foods")

    
    FUNCTIONAL_BEVERAGES = StaticAisle(name="Functional Beverages",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/alimentos-funcionales/bebidas-funcionales/OCA1B1C1D3?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Functional_Beverages.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Functional_Beverages_detailed.json"))
    
    INSECTS = StaticAisle(name="Insects",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/alimentos-funcionales/insectos/OCA1B1C1D1?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Insects.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Insects_detailed.json"))
    
    FUNCTIONAL_FOODS = StaticAisle(name="Functional Foods",  url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/alimentos-funcionales/alimentos-funcionales/OCA1B1C1D4?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Functional_Foods.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Functional_Foods_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [FUNCTIONAL_BEVERAGES, INSECTS, FUNCTIONAL_FOODS]
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
                case "FUNCTIONAL_BEVERAGES":
                    aisles = [cls.FUNCTIONAL_BEVERAGES]
                case "INSECTS":
                    aisles = [cls.INSECTS]
                case "FUNCTIONAL_FOODS":
                    aisles = [cls.FUNCTIONAL_FOODS]
               
        return aisles
    
#Vegan

class AlcampoVeganProteinAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Vegan_protein")

    
    TOFU = StaticAisle(name="Tofu",  url="https://www.compraonline.alcampo.es/categories/veganos/proteina-vegana/tofu-y-seit%C3%A1n/OC0911202115?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Tofu.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tofu_detailed.json"))
    
    SPREADS = StaticAisle(name="Spreads",  url="https://www.compraonline.alcampo.es/categories/veganos/proteina-vegana/untables/OC0911202116?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Spreads.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Spreads_detailed.json"))
    
    PREPARED_DISHES = StaticAisle(name="Prepared Dishes",  url="https://www.compraonline.alcampo.es/categories/veganos/proteina-vegana/platos-preparados/OC0911202111?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Prepared_Dishes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Prepared_Dishes_detailed.json"))
    
    VEGAN_BURGER = StaticAisle(name="Vegan burger",  url="https://www.compraonline.alcampo.es/categories/veganos/proteina-vegana/burger-vegana/OC0911202113?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Vegan_burger.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vegan_burger_detailed.json"))
    
    VEGAN_VEGETABLE_PREPARATIONS = StaticAisle(name="Vegan vegetable preparations",  url="https://www.compraonline.alcampo.es/categories/veganos/proteina-vegana/elaborados-vegetales-veganos/OC0911202112?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Vegan_vegetable_preparations.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vegan_vegetable_preparations_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [TOFU, SPREADS, PREPARED_DISHES, VEGAN_BURGER, VEGAN_VEGETABLE_PREPARATIONS]
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
                case "TOFU":
                    aisles = [cls.TOFU]
                case "SPREADS":
                    aisles = [cls.SPREADS]
                case "PREPARED_DISHES":
                    aisles = [cls.PREPARED_DISHES]
                case "VEGAN_BURGER":
                    aisles = [cls.VEGAN_BURGER]
                case "VEGAN_VEGETABLE_PREPARATIONS":
                    aisles = [cls.VEGAN_VEGETABLE_PREPARATIONS]
               
        return aisles
    
class AlcampoVeganDietAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Vegan_diet")

    
    VEGAN_PANTRY = StaticAisle(name="Vegan pantry",  url="https://www.compraonline.alcampo.es/categories/veganos/alimentaci%C3%B3n-vegana/despensa-vegana/OC091120214?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Vegan_pantry.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vegan_pantry_detailed.json"))
    
    VEGAN_VEGETABLE_DESSERTS = StaticAisle(name="Vegan Vegetable Desserts",  url="https://www.compraonline.alcampo.es/categories/veganos/alimentaci%C3%B3n-vegana/postres-vegetales-veganos/OC091120217?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Vegan_Vegetable_Desserts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vegan_Vegetable_Desserts_detailed.json"))
    
    VEGAN_BREAKFASTS = StaticAisle(name="Vegan breakfasts",  url="https://www.compraonline.alcampo.es/categories/veganos/alimentaci%C3%B3n-vegana/desayunos-veganos/OC091120213?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Vegan_breakfasts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vegan_breakfasts_detailed.json"))
    
    VEGAN_DOUGHS = StaticAisle(name="Vegan doughs",  url="https://www.compraonline.alcampo.es/categories/veganos/alimentaci%C3%B3n-vegana/masas-veganas/OC0911202141?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Vegan_doughs.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vegan_doughs_detailed.json"))

    aisles: Final[List[StaticAisle]] = [VEGAN_PANTRY, VEGAN_VEGETABLE_DESSERTS, VEGAN_BREAKFASTS, VEGAN_DOUGHS]
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
                case "VEGAN_PANTRY":
                    aisles = [cls.VEGAN_PANTRY]
                case "VEGAN_VEGETABLE_DESSERTS":
                    aisles = [cls.VEGAN_VEGETABLE_DESSERTS]
                case "VEGAN_BREAKFASTS":
                    aisles = [cls.VEGAN_BREAKFASTS]
                case "VEGAN_DOUGHS":
                    aisles = [cls.VEGAN_DOUGHS]
                
               
        return aisles
    
class AlcampoVeganWineAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Vegan_wine")

    
    VEGAN_WINE = StaticAisle(name="Vegan Wine",  url="https://www.compraonline.alcampo.es/categories/veganos/vino-vegano/OC0911202126?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Vegan_Wine.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vegan_Wine_detailed.json"))
    

    aisles: Final[List[StaticAisle]] = [VEGAN_WINE]
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
                case "VEGAN_WINE":
                    aisles = [cls.VEGAN_WINE]
             
        return aisles
    
class AlcampoVeganDrinksAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Vegan_drinks")

    
    VEGAN_SOY_DRINKS = StaticAisle(name="Vegan soy drinks",  url="https://www.compraonline.alcampo.es/categories/veganos/bebidas-veganas/bebidas-de-soja-veganas/OCV160314?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Vegan_soy_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vegan_soy_drinks_detailed.json"))
    
    VEGAN_OAT_DRINKS = StaticAisle(name="Vegan oat drinks",  url="https://www.compraonline.alcampo.es/categories/veganos/bebidas-veganas/bebidas-de-avena-veganas/OCV16031001?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Vegan_oat_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vegan_oat_drinks_detailed.json"))
    
    VEGAN_RICE_DRINKS = StaticAisle(name="Vegan rice drinks",  url="https://www.compraonline.alcampo.es/categories/veganos/bebidas-veganas/bebidas-de-arroz-veganas/OCV16031002?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Vegan_rice_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vegan_rice_drinks_detailed.json"))
    
    VEGAN_ALMOND_DRINKS = StaticAisle(name="Vegan almond drinks",  url="https://www.compraonline.alcampo.es/categories/veganos/bebidas-veganas/bebidas-de-almendra-veganas/OCV16031003?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Vegan_almond_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vegan_almond_drinks_detailed.json"))
    
    OTHER_VEGAN_DRINKS = StaticAisle(name="Other Vegan soy drinks",  url="https://www.compraonline.alcampo.es/categories/veganos/bebidas-veganas/otras-bebidas-veganas/OCV0911202125?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Other_Vegan_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_Vegan_drinks_detailed.json"))
    

    aisles: Final[List[StaticAisle]] = [VEGAN_SOY_DRINKS, VEGAN_OAT_DRINKS, VEGAN_RICE_DRINKS, VEGAN_ALMOND_DRINKS, OTHER_VEGAN_DRINKS]
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
                case "VEGAN_SOY_DRINKS":
                    aisles = [cls.VEGAN_SOY_DRINKS]
                case "VEGAN_OAT_DRINKS":
                    aisles = [cls.VEGAN_OAT_DRINKS]
                case "VEGAN_RICE_DRINKS":
                    aisles = [cls.VEGAN_RICE_DRINKS]
                case "VEGAN_ALMOND_DRINKS":
                    aisles = [cls.VEGAN_ALMOND_DRINKS]
                case "OTHER_VEGAN_DRINKS":
                    aisles = [cls.OTHER_VEGAN_DRINKS]
             
        return aisles
    
#Baby

class AlcampoBabyInfantNutritionAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Baby_Infant_nutrition")

    
    BABY_MILKS = StaticAisle(name="Baby milks",  url="https://www.compraonline.alcampo.es/categories/beb%C3%A9/alimentaci%C3%B3n-infantil/leches-para-beb%C3%A9s/OC8021?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Baby_milks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Baby_milks_detailed.json"))
    
    PORRIDGES = StaticAisle(name="Porridges",  url="https://www.compraonline.alcampo.es/categories/beb%C3%A9/alimentaci%C3%B3n-infantil/papillas/OC8022?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Porridges.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Porridges_detailed.json"))
    
    JARS = StaticAisle(name="Jars",  url="https://www.compraonline.alcampo.es/categories/beb%C3%A9/alimentaci%C3%B3n-infantil/tarritos/OC8023?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Jars.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Jars_detailed.json"))
    
    DESSERTS = StaticAisle(name="Desserts",  url="https://www.compraonline.alcampo.es/categories/beb%C3%A9/alimentaci%C3%B3n-infantil/postres/OC8024?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Desserts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Desserts_detailed.json"))
    
    WATER_AND_JUICES = StaticAisle(name="Water and Juices",  url="https://www.compraonline.alcampo.es/categories/beb%C3%A9/alimentaci%C3%B3n-infantil/agua-y-zumos/OC8025?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Water_and_Juices.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Water_and_Juices_detailed.json"))
    
    ORGANIC_BABY_FOOD = StaticAisle(name="Organic_baby_food",  url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/alimentaci%C3%B3n-infantil-ecol%C3%B3gica/OC200520206?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Organic_baby_food.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Organic_baby_food_detailed.json"))
    
    BAGS = StaticAisle(name="Bags",  url="https://www.compraonline.alcampo.es/categories/beb%C3%A9/alimentaci%C3%B3n-infantil/bolsitas/OC8026?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Bags.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Bags_detailed.json"))
    
    COOKIES_AND_SNACKS = StaticAisle(name="Cookies and Snacks",  url="https://www.compraonline.alcampo.es/categories/beb%C3%A9/alimentaci%C3%B3n-infantil/galletas-y-snacks/OC8027?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cookies_and_Snacks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cookies_and_Snacks_detailed.json"))
    

    aisles: Final[List[StaticAisle]] = [BABY_MILKS, PORRIDGES, JARS, DESSERTS, WATER_AND_JUICES, ORGANIC_BABY_FOOD, BAGS, COOKIES_AND_SNACKS]
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
                case "BABY_MILKS":
                    aisles = [cls.BABY_MILKS]
                case "PORRIDGES":
                    aisles = [cls.PORRIDGES]
                case "JARS":
                    aisles = [cls.JARS]
                case "DESSERTS":
                    aisles = [cls.DESSERTS]
                case "WATER_AND_JUICES":
                    aisles = [cls.WATER_AND_JUICES]
                case "ORGANIC_BABY_FOOD":
                    aisles = [cls.ORGANIC_BABY_FOOD]
                case "BAGS":
                    aisles = [cls.BAGS]
                case "COOKIES_AND_SNACKS":
                    aisles = [cls.COOKIES_AND_SNACKS]
             
        return aisles
    
#Pets

class AlcampoPetsDogFoodAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Pets_Dog_food")

    
    DOG_FOOD = StaticAisle(name="Dog food",  url="https://www.compraonline.alcampo.es/categories/mascotas/comida-perros/pienso-para-perros/OC200801?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Dog_food.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Dog_food_detailed.json"))
    
    WET_DOG_FOOD = StaticAisle(name="Wet dog food",  url="https://www.compraonline.alcampo.es/categories/mascotas/comida-perros/comida-h%C3%BAmeda-para-perros/OC200802?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Wet_dog_food.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Wet_dog_food_detailed.json"))
    
    NATURAL_FOOD_FOR_DOGS = StaticAisle(name="Natural Food for Dogs",  url="https://www.compraonline.alcampo.es/categories/mascotas/comida-perros/comida-natural-para-perros/OC200620191?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Natural_Food_for_Dogs.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Natural_Food_for_Dogs_detailed.json"))
    
    SNACKS_AND_BONES_FOR_DOGS = StaticAisle(name="Snacks and bones for dogs",  url="https://www.compraonline.alcampo.es/categories/mascotas/comida-perros/snacks-y-huesos-para-perros/OC06211?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Snacks_and_bones_for_dogs.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Snacks_and_bones_for_dogs_detailed.json"))
   

    aisles: Final[List[StaticAisle]] = [DOG_FOOD, WET_DOG_FOOD, NATURAL_FOOD_FOR_DOGS, SNACKS_AND_BONES_FOR_DOGS]
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
                case "DOG_FOOD":
                    aisles = [cls.DOG_FOOD]
                case "WET_DOG_FOOD":
                    aisles = [cls.WET_DOG_FOOD]
                case "NATURAL_FOOD_FOR_DOGS":
                    aisles = [cls.NATURAL_FOOD_FOR_DOGS]
                case "SNACKS_AND_BONES_FOR_DOGS":
                    aisles = [cls.SNACKS_AND_BONES_FOR_DOGS]
             
        return aisles
    
class AlcampoPetsCatsFoodAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Pets_Cats_food")

    
    CAT_FOOD = StaticAisle(name="Cat food",  url="https://www.compraonline.alcampo.es/categories/mascotas/comida-gatos/pienso-para-gatos/OC201301?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cat_food.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cat_food_detailed.json"))
    
    WET_CAT_FOOD = StaticAisle(name="Wet cat food",  url="https://www.compraonline.alcampo.es/categories/mascotas/comida-gatos/comida-h%C3%BAmeda-para-gatos/OC201302?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Wet_cat_food.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Wet_cat_food_detailed.json"))
    
    NATURAL_FOOD_FOR_CATS = StaticAisle(name="Natural Food for cats",  url="https://www.compraonline.alcampo.es/categories/mascotas/comida-gatos/comida-natural-gatos/OC200620192?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Natural_Food_for_cats.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Natural_Food_for_cats_detailed.json"))
    
    CAT_SNACKS = StaticAisle(name="Cat snacks",  url="https://www.compraonline.alcampo.es/categories/mascotas/comida-gatos/snacks-para-gatos/OC2006?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Cat_snacks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cat_snacks_detailed.json"))
    
    MILK_AND_MALT_FOR_CATS = StaticAisle(name="Milk and malt for cats",  url="https://www.compraonline.alcampo.es/categories/mascotas/comida-gatos/leche-y-malta-para-gatos/OC06244?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Milk_and_malt_for_cats.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Milk_and_malt_for_cats_detailed.json"))
   

    aisles: Final[List[StaticAisle]] = [CAT_FOOD, WET_CAT_FOOD, NATURAL_FOOD_FOR_CATS, CAT_SNACKS, MILK_AND_MALT_FOR_CATS]
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
                case "CAT_FOOD":
                    aisles = [cls.CAT_FOOD]
                case "WET_CAT_FOOD":
                    aisles = [cls.WET_CAT_FOOD]
                case "NATURAL_FOOD_FOR_CATS":
                    aisles = [cls.NATURAL_FOOD_FOR_CATS]
                case "CAT_SNACKS":
                    aisles = [cls.CAT_SNACKS]
                case "MILK_AND_MALT_FOR_CATS":
                    aisles = [cls.MILK_AND_MALT_FOR_CATS]
             
        return aisles
    
class AlcampoPetsRabbitsFoodAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Pets_Rabbits_food")

    
    HAY_AND_BEDDING = StaticAisle(name="Hay and bedding",  url="https://www.compraonline.alcampo.es/categories/mascotas/conejos-y-roedores/heno-y-lechos/OC06272?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Hay_and_bedding.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Hay_and_bedding_detailed.json"))
    
    FEEDING = StaticAisle(name="Feeding",  url="https://www.compraonline.alcampo.es/categories/mascotas/conejos-y-roedores/alimentaci%C3%B3n/OC200310?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Feeding.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Feeding_detailed.json"))
    
    ACCESSORIES = StaticAisle(name="Accessories",  url="https://www.compraonline.alcampo.es/categories/mascotas/conejos-y-roedores/accesorios/OC06273?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Accessories.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Accessories_detailed.json"))
    
    SNACKS_AND_BARS = StaticAisle(name="Snacks and bars",  url="https://www.compraonline.alcampo.es/categories/mascotas/conejos-y-roedores/snacks-y-barritas/OC06271?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Snacks_and_bars.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Snacks_and_bars_detailed.json"))
  
    aisles: Final[List[StaticAisle]] = [HAY_AND_BEDDING, FEEDING, ACCESSORIES, SNACKS_AND_BARS]
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
                case "HAY_AND_BEDDING":
                    aisles = [cls.HAY_AND_BEDDING]
                case "FEEDING":
                    aisles = [cls.FEEDING]
                case "ACCESSORIES":
                    aisles = [cls.ACCESSORIES]
                case "SNACKS_AND_BARS":
                    aisles = [cls.SNACKS_AND_BARS]
                
             
        return aisles
    
class AlcampoPetsFishFoodAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Pets_Fish_food")

    
    FISH_FEEDING = StaticAisle(name="Fish feeding",  url="https://www.compraonline.alcampo.es/categories/mascotas/peces-y-tortugas/alimentaci%C3%B3n-peces/OC200410?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Fish_feeding.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fish_feeding_detailed.json"))
    
    FEEDING_TURTLES = StaticAisle(name="Feeding turtles",  url="https://www.compraonline.alcampo.es/categories/mascotas/peces-y-tortugas/alimentaci%C3%B3n-tortugas/OC200411?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Feeding_turtles.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Feeding_turtles_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [FISH_FEEDING, FEEDING_TURTLES]
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
                case "FISH_FEEDING":
                    aisles = [cls.FISH_FEEDING]
                case "FEEDING_TURTLES":
                    aisles = [cls.FEEDING_TURTLES]
             
        return aisles
    
class AlcampoPetsBirdsFoodAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Pets_Birds_food")

    
    ACCESSORIES = StaticAisle(name="Accessories",  url="https://www.compraonline.alcampo.es/categories/mascotas/p%C3%A1jaros/accesorios/OC200713?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Accessories.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Accessories_detailed.json"))
    
    FEEDING = StaticAisle(name="Feeding",  url="https://www.compraonline.alcampo.es/categories/mascotas/p%C3%A1jaros/alimentaci%C3%B3n/OC200710?source=navigation",
                                     original_file_uri=os.path.join(category_path(), "Feeding.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Feeding_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [ACCESSORIES, FEEDING]
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
                case "ACCESSORIES":
                    aisles = [cls.ACCESSORIES]
                case "FEEDING":
                    aisles = [cls.FEEDING]
             
        return aisles
    
alcampo_categories_with_uris: Final[list[StaticCategory]] = [

    #FRESCOES

    StaticCategory(name="Fruit", url="https://www.compraonline.alcampo.es/categories/frescos/frutas/OC1701?source=navigation", aisles=AlcampoFrescoesFruitsAlimentations.aisles),
    
    StaticCategory(name="Vegetables and greens", url="https://www.compraonline.alcampo.es/categories/frescos/verduras-y-hortalizas/OC1702?source=navigation", aisles=AlcampoFrescoesVegetablesAndGreensAlimentations.aisles),
    
    StaticCategory(name="Meat", url="https://www.compraonline.alcampo.es/categories/frescos/carne/OC13?source=navigation", aisles=AlcampoFrescoesMeatAlimentations.aisles),
    
    StaticCategory(name="Fish shellfish and mollusks", url="https://www.compraonline.alcampo.es/categories/frescos/pescados-mariscos-y-moluscos/OC14?source=navigation", aisles=AlcampoFrescoesShellfishAlimentations.aisles),
    
    StaticCategory(name="Smoked foods, surimi, anchovies, octopus and others", url="https://www.compraonline.alcampo.es/categories/frescos/ahumados-surimis-anchoas-pulpos-y-otros/OC184?source=navigation", aisles=AlcampoFrescoesSmokedFoodAlimentations.aisles),
    
    StaticCategory(name="Delicatessen", url="https://www.compraonline.alcampo.es/categories/frescos/charcuter%C3%ADa/OC15?source=navigation", aisles=AlcampoFrescoesDelicatessenAlimentations.aisles),
    
    StaticCategory(name="Ham", url="https://www.compraonline.alcampo.es/categories/frescos/jamones-y-paletas/OC151001?source=navigation", aisles=AlcampoFrescoesHamAndShouldersAlimentations.aisles),
    
    StaticCategory(name="Cheeses", url="https://www.compraonline.alcampo.es/categories/frescos/quesos/OCQuesos?source=navigation", aisles=AlcampoFrescoesCheesesAlimentations.aisles),
    
    StaticCategory(name="Bakery", url="https://www.compraonline.alcampo.es/categories/frescos/panader%C3%ADa/OC1281?source=navigation", aisles=AlcampoFrescoesBakeryAlimentations.aisles),
    
    StaticCategory(name="Pastry", url="https://www.compraonline.alcampo.es/categories/frescos/pasteler%C3%ADa/OC1282?source=navigation", aisles=AlcampoFrescoesPastryAlimentations.aisles),

    #MILK

    StaticCategory(name="Milk", url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/leche/OC1603?source=navigation", aisles=AlcampoMilkMilkAlimentations.aisles),
    
    StaticCategory(name="Vegetable drinks", url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/bebidas-vegetales/OC1609?source=navigation", aisles=AlcampoMilkVegetablesDrinksAlimentations.aisles),
    
    StaticCategory(name="Dairy preparation", url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/preparado-l%C3%A1cteo/OCPreparadolacteo?source=navigation", aisles=AlcampoMilkDairyPreparationAlimentations.aisles),
    
    StaticCategory(name="Eggs", url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/huevos/OC1608?source=navigation", aisles=AlcampoMilkEggsAlimentations.aisles),
    
    StaticCategory(name="Yogurts, Bifidus and L-Casei", url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/yogures-b%C3%ADfidus-y-l-casei/OC1601?source=navigation", aisles=AlcampoMilkYoghurtAlimentations.aisles),
    
    StaticCategory(name="Dairy desserts", url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/postres-l%C3%A1cteos/OC1602?source=navigation", aisles=AlcampoMilkDairyDessertsAlimentations.aisles),
    
    StaticCategory(name="Butter", url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/mantequilla/OC1606?source=navigation", aisles=AlcampoMilkButterAlimentations.aisles),
    
    StaticCategory(name="Margarines and other spreads", url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/margarinas-y-otros-untables/OC1607?source=navigation", aisles=AlcampoMilkMargarineAlimentations.aisles),
    
    StaticCategory(name="Cream", url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/nata/OC1605?source=navigation", aisles=AlcampoMilkCreamAlimentations.aisles),
    
    StaticCategory(name="Smoothies and horchatas", url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/batidos-y-horchatas/OC1604?source=navigation", aisles=AlcampoMilkSmothiesAlimentations.aisles),
    
    StaticCategory(name="Juices with milk", url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/zumos-con-leche/OC160403?source=navigation", aisles=AlcampoMilkJuicesAlimentations.aisles),
    
    StaticCategory(name="Condensed powdered and evaporated milk", url="https://www.compraonline.alcampo.es/categories/leche-huevos-l%C3%A1cteos-yogures-y-bebidas-vegetales/leche-condensada-polvo-y-evaporada/OC160316?source=navigation", aisles=AlcampoMilkCondensedAlimentations.aisles),
    
    #FEEDING

    StaticCategory(name="Oil Vinegar, Salt and Spices", url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/aceite-vinagre-sal-y-especias/OC18?source=navigation", aisles=AlcampoFeedingOilVinegarSaltAndSpicesAlimentations.aisles),
    
    StaticCategory(name="Canned fish", url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-de-pescado/OC100402?source=navigation", aisles=AlcampoFeedingCannedFishAlimentations.aisles),
    
    StaticCategory(name="Canned vegetables", url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-vegetales/OC100401?source=navigation", aisles=AlcampoFeedingCannedVegetablesAlimentations.aisles),
    
    StaticCategory(name="Canned meats prepared dishes and syrups", url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-c%C3%A1rnicas-platos-preparados-y-alm%C3%ADbares/OC1004?source=navigation", aisles=AlcampoFeedingCannedMeatAlimentations.aisles),
    
    StaticCategory(name="Fried Tomato and Sauces", url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/tomate-frito-y-salsas/OCTomateySalsas?source=navigation", aisles=AlcampoFeedingFriedTomatoAndSaucesAlimentations.aisles),
    
    StaticCategory(name="Appetizers olives and nuts", url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/aperitivos-aceitunas-y-frutos-secos/OC120?source=navigation", aisles=AlcampoFeedingAppetizersNutsAlimentations.aisles),
    
    StaticCategory(name="Pasta", url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/pasta-alimenticia/OC100501?source=navigation", aisles=AlcampoFeedingPastaAlimentations.aisles),
    
    StaticCategory(name="Rice and Legumes", url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/arroz-y-legumbres/OC140?source=navigation", aisles=AlcampoFeedingRiceAndLegumesAlimentations.aisles),
    
    StaticCategory(name="Bakery Flour and Doughs", url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/panader%C3%ADa-harina-y-masas/OC1009?source=navigation", aisles=AlcampoFeedingBakeryFlourAndDoughsAlimentations.aisles),
    
    StaticCategory(name="Soups Broths and Creams", url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/sopas-caldos-y-cremas/OCCaldosycremas?source=navigation", aisles=AlcampoFeedingSoupsBrothsAndCreamsAlimentations.aisles),
    
    StaticCategory(name="International Food", url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/comida-internacional/OC9410?source=navigation", aisles=AlcampoFeedingInternationalFoodAlimentations.aisles),
    
    #BREAKFAST AND SNACKS

    StaticCategory(name="Cafes", url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/caf%C3%A9s/OC100806?source=navigation", aisles=AlcampoBreakfastCafesAlimentations.aisles),
    
    StaticCategory(name="Cookies", url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/galletas/OC100805?source=navigation", aisles=AlcampoBreakfastCookiesAlimentations.aisles),
    
    StaticCategory(name="Chocolates Spreads and Chocolates", url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/chocolates-cremas-untar-y-bombones/OC1008?source=navigation", aisles=AlcampoBreakfastChocolatesAlimentations.aisles),
    
    StaticCategory(name="Pastries and Cakes", url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/boller%C3%ADa-y-pasteler%C3%ADa/OC1011?source=navigation", aisles=AlcampoBreakfastPastriesAndCakesAlimentations.aisles),
    
    StaticCategory(name="Cereals and Bars", url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/cereales-y-barritas/OC100804?source=navigation", aisles=AlcampoBreakfastCerealsAndBarsAlimentations.aisles),
    
    StaticCategory(name="Sugar, honey and other sweeteners", url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/az%C3%BAcar-miel-y-otros-edulcorantes/OCAzucaryedulcorante?source=navigation", aisles=AlcampoBreakfastSugarAlimentations.aisles),
    
    StaticCategory(name="Soluble cocoa", url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/cacaos-solubles/OC100803017?source=navigation", aisles=AlcampoBreakfastCocaoAlimentations.aisles),
    
    StaticCategory(name="Tea and Infusions", url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/t%C3%A9-e-infusiones/OC100807?source=navigation", aisles=AlcampoBreakfastTeaAndInfusionAlimentations.aisles),
    
    StaticCategory(name="Jam, syrups, quince", url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/mermelada-almibares-membrillo/OC100802?source=navigation", aisles=AlcampoBreakfastJamAlimentations.aisles),
    
    StaticCategory(name="Candies", url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/golosinas/OC100902?source=navigation", aisles=AlcampoBreakfastCandiesAlimentations.aisles),
    
    StaticCategory(name="Dessert Preparation", url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/preparaci%C3%B3n-postres/OC1007?source=navigation", aisles=AlcampoBreakfastDessertsPreparationAlimentations.aisles),
    
    StaticCategory(name="Food bank collection", url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/recogida-banco-de-alimentos/OCCBA?source=navigation", aisles=AlcampoBreakfastFoodBankAlimentations.aisles),
    
    StaticCategory(name="Nougats", url="https://www.compraonline.alcampo.es/categories/desayuno-y-merienda/turrones/OC100903?source=navigation", aisles=AlcampoBreakfastNougatsAlimentations.aisles),

    #FROZEN
    
    StaticCategory(name="Fish, seafood and surimi", url="https://www.compraonline.alcampo.es/categories/congelados/pescados-mariscos-y-surimis/OC1201?source=navigation", aisles=AlcampoFrozentFishAlimentations.aisles),
    
    StaticCategory(name="Ice cream", url="https://www.compraonline.alcampo.es/categories/congelados/helados/OC200220184?source=navigation", aisles=AlcampoFrozentIceCreamAlimentations.aisles),
    
    StaticCategory(name="Frozen Vegetables", url="https://www.compraonline.alcampo.es/categories/congelados/verduras-congeladas/OC1203?source=navigation", aisles=AlcampoFrozentVegetablesAlimentations.aisles),
    
    StaticCategory(name="Frozen ready meals", url="https://www.compraonline.alcampo.es/categories/congelados/platos-preparados-congelados/OC1205?source=navigation", aisles=AlcampoFrozentMealsAlimentations.aisles),
    
    StaticCategory(name="Potatoes, croquettes and empanadas", url="https://www.compraonline.alcampo.es/categories/congelados/patatas-croquetas-y-empanadillas/OCCroquetasEmpanadillas?source=navigation", aisles=AlcampoFrozentPotatoesAlimentations.aisles),
    
    StaticCategory(name="San Jacobos and breaded chicken", url="https://www.compraonline.alcampo.es/categories/congelados/san-jacobos-y-pollo-empanado/OCPolloEmpanado?source=navigation", aisles=AlcampoFrozentBreadedChickenAlimentations.aisles),
    
    StaticCategory(name="Meat", url="https://www.compraonline.alcampo.es/categories/congelados/carne/OC1202?source=navigation", aisles=AlcampoFrozentMeatAlimentations.aisles),
    
    StaticCategory(name="Pastries, ice and insulated bags", url="https://www.compraonline.alcampo.es/categories/congelados/reposter%C3%ADa-hielo-y-bolsas-isot%C3%A9rmicas/OC1207?source=navigation", aisles=AlcampoFrozentPastriesAlimentations.aisles),
    
    StaticCategory(name="Cakes, desserts and frozen fruit", url="https://www.compraonline.alcampo.es/categories/congelados/tartas-postres-y-fruta-congelada/OC1209?source=navigation", aisles=AlcampoFrozentFruitAlimentations.aisles),
    
    StaticCategory(name="Essentials AirFryer", url="https://www.compraonline.alcampo.es/categories/congelados/esenciales-para-tu-freidora-de-aire/OCconfreiaire?source=navigation", aisles=AlcampoFrozentEssentialsAlimentations.aisles),
    
    #PREPARED_FOOD

    StaticCategory(name="Sushi", url="https://www.compraonline.alcampo.es/categories/comida-preparada/sushi/OC140502?source=navigation", aisles=AlcampoPreparedSushiAlimentations.aisles),

    StaticCategory(name="Pizzas", url="https://www.compraonline.alcampo.es/categories/comida-preparada/pizzas/OC941?source=navigation", aisles=AlcampoPreparedPizzaAlimentations.aisles),
    
    StaticCategory(name="Gazpachos and creams", url="https://www.compraonline.alcampo.es/categories/comida-preparada/gazpachos-y-cremas/OC943?source=navigation", aisles=AlcampoPreparedGazpachosAlimentations.aisles),
    
    StaticCategory(name="Potato tortillas", url="https://www.compraonline.alcampo.es/categories/comida-preparada/tortillas-de-patata/OC09426?source=navigation", aisles=AlcampoPreparedTortillasAlimentations.aisles),
    
    StaticCategory(name="Rice and pasta", url="https://www.compraonline.alcampo.es/categories/comida-preparada/arroces-y-pastas/OC2002201852?source=navigation", aisles=AlcampoPreparedRiceAndPastaAlimentations.aisles),
    
    StaticCategory(name="Other specialties", url="https://www.compraonline.alcampo.es/categories/comida-preparada/otras-especialidades/OC09427?source=navigation", aisles=AlcampoPreparedOtherSpecialitiesAlimentations.aisles),

    StaticCategory(name="Hummus, guacamole and others", url="https://www.compraonline.alcampo.es/categories/comida-preparada/hummus-guacamole-y-otros/OC090820181?source=navigation", aisles=AlcampoPreparedHummusAlimentations.aisles),
    
    StaticCategory(name="International Dishess", url="https://www.compraonline.alcampo.es/categories/comida-preparada/platos-internacionales/OC09421?source=navigation", aisles=AlcampoPreparedInternationalDishesAlimentations.aisles),
    
    StaticCategory(name="Masses and bases", url="https://www.compraonline.alcampo.es/categories/comida-preparada/masas-y-bases/OC0943?source=navigation", aisles=AlcampoPreparedBassesAlimentations.aisles),
    
    StaticCategory(name="Vegetarian foods", url="https://www.compraonline.alcampo.es/categories/comida-preparada/alimentos-vegetarianos/OC09441?source=navigation", aisles=AlcampoPreparedVegeterianFoodAlimentations.aisles),
    
    StaticCategory(name="Sandwiches snacks and bagels", url="https://www.compraonline.alcampo.es/categories/comida-preparada/s%C3%A1ndwiches-bocadillos-y-roscas/OC2002201853?source=navigation", aisles=AlcampoPreparedSandwichAlimentations.aisles),

    StaticCategory(name="Roasts and meats", url="https://www.compraonline.alcampo.es/categories/comida-preparada/asados-y-carnes/OC09423?source=navigation", aisles=AlcampoPreparedRoastMeatsAlimentations.aisles),
    
    StaticCategory(name="Refrigerated salads", url="https://www.compraonline.alcampo.es/categories/comida-preparada/ensaladas-refrigeradas/OC9421?source=navigation", aisles=AlcampoPreparedRefrigiratedSaladsAlimentations.aisles),
    
    StaticCategory(name="Empanadas", url="https://www.compraonline.alcampo.es/categories/comida-preparada/empanadas/OC09428?source=navigation", aisles=AlcampoPreparedEmpanadasAlimentations.aisles),
    
    StaticCategory(name="Canned prepared dishes", url="https://www.compraonline.alcampo.es/categories/alimentaci%C3%B3n/conservas-c%C3%A1rnicas-platos-preparados-y-alm%C3%ADbares/platos-preparados-en-conserva/OC100404?source=navigation", aisles=AlcampoPreparedCannedDishesAlimentations.aisles),
    
    StaticCategory(name="Essentials AirFryer", url="https://www.compraonline.alcampo.es/categories/comida-preparada/esenciales-para-tu-freidora-de-aire/OCcpfreiaire?source=navigation", aisles=AlcampoPreparedEssentialsAlimentations.aisles),

    #DRINKS
    
    StaticCategory(name="Soft drinks", url="https://www.compraonline.alcampo.es/categories/bebidas/refrescos/OC1103?source=navigation", aisles=AlcampoDrinksSoftDrinksAlimentations.aisles),

    StaticCategory(name="Water, Soda and Soft Drinks", url="https://www.compraonline.alcampo.es/categories/bebidas/agua-soda-y-gaseosas/OC1101?source=navigation", aisles=AlcampoDrinksWaterSodaAlimentations.aisles),
    
    StaticCategory(name="Fruit Juices", url="https://www.compraonline.alcampo.es/categories/bebidas/zumos-de-frutas/OC1102?source=navigation", aisles=AlcampoDrinksJuicesAlimentations.aisles),
    
    StaticCategory(name="Beers", url="https://www.compraonline.alcampo.es/categories/bebidas/cervezas/OC1107?source=navigation", aisles=AlcampoDrinksBeersAlimentations.aisles),
    
    StaticCategory(name="Red wine", url="https://www.compraonline.alcampo.es/categories/bebidas/vino-tinto/OC1151?source=navigation", aisles=AlcampoDrinksRedWineAlimentations.aisles),
    
    StaticCategory(name="White wine", url="https://www.compraonline.alcampo.es/categories/bebidas/vino-blanco/OC1152?source=navigation", aisles=AlcampoDrinksWhiteWineAlimentations.aisles),

    StaticCategory(name="Rosé, sparkling, sweet and oloroso wines", url="https://www.compraonline.alcampo.es/categories/bebidas/vino-rosados-frizzantes-dulces-y-olorosos/OC1153?source=navigation", aisles=AlcampoDrinksRoséAlimentations.aisles),

    StaticCategory(name="Champagne Cavas and Ciders", url="https://www.compraonline.alcampo.es/categories/bebidas/champagne-cavas-y-sidras/OC1156?source=navigation", aisles=AlcampoDrinksChampagneAlimentations.aisles),
    
    StaticCategory(name="Alcoholic Beverages", url="https://www.compraonline.alcampo.es/categories/bebidas/bebidas-alcoh%C3%B3licas/OC1154?source=navigation", aisles=AlcampoDrinksAlcoholicBeveragesAlimentations.aisles),
    
    StaticCategory(name="Liquors", url="https://www.compraonline.alcampo.es/categories/bebidas/licores/OC1155?source=navigation", aisles=AlcampoDrinksLiquorsAlimentations.aisles),
    
    StaticCategory(name="Drinks 0.0", url="https://www.compraonline.alcampo.es/categories/bebidas/bebidas-0-0/OC250420222?source=navigation", aisles=AlcampoDrinksZero0Alimentations.aisles),
    
    StaticCategory(name="Non-alcoholic wines", url="https://www.compraonline.alcampo.es/categories/bebidas/vinos-sin-alcohol/OC25042023?source=navigation", aisles=AlcampoDrinksNonAlcoholicWinesAlimentations.aisles),

    StaticCategory(name="Organic Wines", url="https://www.compraonline.alcampo.es/categories/bebidas/bebidas-ecol%C3%B3gicas/OC101303?source=navigation", aisles=AlcampoDrinksOrganicWinesAlimentations.aisles),

    #ORGANIC_SUPERMARKET

    StaticCategory(name="Fresh Organic Product", url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/producto-fresco-ecol%C3%B3gico/OC261120211?source=navigation", aisles=AlcampoSupermarketOrganicProductAlimentations.aisles),
    
    StaticCategory(name="Organic Dairy and Eggs", url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/l%C3%A1cteos-y-huevos-de-producci%C3%B3n-ecol%C3%B3gica/OC2611202122?source=navigation", aisles=AlcampoSupermarketOrganicDairyAlimentations.aisles),
    
    StaticCategory(name="Your Organic Pantry", url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/tu-despensa-ecol%C3%B3gica/OC2611202121?source=navigation", aisles=AlcampoSupermarketOrganicPantryAlimentations.aisles),
    
    StaticCategory(name="Organic Breakfasts", url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/desayunos-ecol%C3%B3gicos/OC2611202123?source=navigation", aisles=AlcampoSupermarketOrganicBreakfastAlimentations.aisles),
    
    StaticCategory(name="Organic Drinks", url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/bebidas-ecol%C3%B3gicas/OC261120213?source=navigation", aisles=AlcampoSupermarketOrganicDrinksAlimentations.aisles),

    StaticCategory(name="Organic baby food", url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/alimentaci%C3%B3n-infantil-ecol%C3%B3gica/OC200520206?source=navigation", aisles=AlcampoSupermarketOrganicBabyFoodAlimentations.aisles),

    StaticCategory(name="Fair Trade", url="https://www.compraonline.alcampo.es/categories/supermercado-ecol%C3%B3gico/comercio-justo/OC01062020?source=navigation", aisles=AlcampoSupermarketFairTradeAlimentations.aisles),
    
    #GLUTEN-FREE
    
    StaticCategory(name="Gluten-free, suitable for celiacs", url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/sin-gluten-apto-cel%C3%ADacos/OC101204?source=navigation", aisles=AlcampoGlutenFreeAlimentations.aisles),
    
    StaticCategory(name="Lactose-free products", url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/productos-sin-lactosa/OC7?source=navigation", aisles=AlcampoGlutenLactoseFreeAlimentations.aisles),
    
    StaticCategory(name="Sports nutrition", url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/nutrici%C3%B3n-deportiva/OC12?source=navigation", aisles=AlcampoGlutenSportsNutritionAlimentations.aisles),
    
    StaticCategory(name="Nutritional Supplements", url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/complementos-nutricionales/OC101210?source=navigation", aisles=AlcampoGlutenNutritionalSupplementsAlimentations.aisles),
    
    StaticCategory(name="Seeds and other cereals", url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/semillas-y-otros-cereales/OC10120102?source=navigation", aisles=AlcampoGlutenSeedsAlimentations.aisles),
    
    StaticCategory(name="Dietary Weight Control", url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/diet%C3%A9ticos-control-de-peso/OC101208?source=navigation", aisles=AlcampoGlutenDietAlimentations.aisles),
    
    StaticCategory(name="Classic Dietetics", url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/diet%C3%A9ticos-cl%C3%A1sicos/OC111982?source=navigation", aisles=AlcampoGlutenClassicDieteticsAlimentations.aisles),
    
    StaticCategory(name="Dietary without added sugars", url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/diet%C3%A9ticos-sin-az%C3%BAcares-a%C3%B1adidos/OC111984?source=navigation", aisles=AlcampoGlutenDietaryWithoutAddedSugarsAlimentations.aisles),
    
    StaticCategory(name="Pancakes", url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/tortitas/OC101203?source=navigation", aisles=AlcampoGlutenPancakeAlimentations.aisles),
    
    StaticCategory(name="Herbalist", url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/herbolario/OC0672074528?source=navigation", aisles=AlcampoGlutenHerbalistAlimentations.aisles),
    
    StaticCategory(name="Functional Foods", url="https://www.compraonline.alcampo.es/categories/sin-gluten-sin-lactosa-y-otras-dietas-espec%C3%ADficas/alimentos-funcionales/OCA1B1C1?source=navigation", aisles=AlcampoGlutenFunctionalFoodsAlimentations.aisles),
    
    #VEGAN

    StaticCategory(name="Vegan protein", url="https://www.compraonline.alcampo.es/categories/veganos/proteina-vegana/OC091120211?source=navigation", aisles=AlcampoVeganProteinAlimentations.aisles),
    
    StaticCategory(name="Vegan diet", url="https://www.compraonline.alcampo.es/categories/veganos/alimentaci%C3%B3n-vegana/OC091120215?source=navigation", aisles=AlcampoVeganDietAlimentations.aisles),
    
    StaticCategory(name="Vegan Wine", url="https://www.compraonline.alcampo.es/categories/veganos/vino-vegano/OC0911202126?source=navigation", aisles=AlcampoVeganWineAlimentations.aisles),
    
    StaticCategory(name="Vegan drinks", url="https://www.compraonline.alcampo.es/categories/veganos/bebidas-veganas/OC091120212?source=navigation", aisles=AlcampoVeganDrinksAlimentations.aisles),

    #BABY
    
    StaticCategory(name="Infant Nutrition", url="https://www.compraonline.alcampo.es/categories/beb%C3%A9/alimentaci%C3%B3n-infantil/OC802?source=navigation", aisles=AlcampoBabyInfantNutritionAlimentations.aisles),
    
    #PETS

    StaticCategory(name="Dog food", url="https://www.compraonline.alcampo.es/categories/mascotas/comida-perros/OC0621?source=navigation", aisles=AlcampoPetsDogFoodAlimentations.aisles),
    
    StaticCategory(name="Cat food", url="https://www.compraonline.alcampo.es/categories/mascotas/comida-gatos/OC0624?source=navigation", aisles=AlcampoPetsCatsFoodAlimentations.aisles),
    
    StaticCategory(name="Rabbits and rodents", url="https://www.compraonline.alcampo.es/categories/mascotas/conejos-y-roedores/OC0627?source=navigation", aisles=AlcampoPetsRabbitsFoodAlimentations.aisles),
    
    StaticCategory(name="Fish and turtles", url="https://www.compraonline.alcampo.es/categories/mascotas/peces-y-tortugas/OC0629?source=navigation", aisles=AlcampoPetsFishFoodAlimentations.aisles),
    
    StaticCategory(name="Birds", url="https://www.compraonline.alcampo.es/categories/mascotas/p%C3%A1jaros/OC0628?source=navigation", aisles=AlcampoPetsBirdsFoodAlimentations.aisles),
    
  
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
        for category in alcampo_categories_with_uris:
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
                case "AlcampoFrescoesFruitsAlimentations":
                    aisles = AlcampoFrescoesFruitsAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFrescoesVegetablesAndGreensAlimentations":
                    aisles = AlcampoFrescoesVegetablesAndGreensAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFrescoesMeatAlimentations":
                    aisles = AlcampoFrescoesMeatAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFrescoesShellfishAlimentations":
                    aisles = AlcampoFrescoesShellfishAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFrescoesSmokedFoodAlimentations":
                    aisles = AlcampoFrescoesSmokedFoodAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFrescoesDelicatessenAlimentations":
                    aisles = AlcampoFrescoesDelicatessenAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFrescoesHamAndShouldersAlimentations":
                    aisles = AlcampoFrescoesHamAndShouldersAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFrescoesCheesesAlimentations":
                    aisles = AlcampoFrescoesCheesesAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFrescoesBakeryAlimentations":
                    aisles = AlcampoFrescoesBakeryAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFrescoesPastryAlimentations":
                    aisles = AlcampoFrescoesPastryAlimentations.get_aisles(cmdargs[1])
                case "AlcampoMilkMilkAlimentations":
                    aisles = AlcampoMilkMilkAlimentations.get_aisles(cmdargs[1])
                case "AlcampoMilkVegetablesDrinksAlimentations":
                    aisles = AlcampoMilkVegetablesDrinksAlimentations.get_aisles(cmdargs[1])
                case "AlcampoMilkDairyPreparationAlimentations":
                    aisles = AlcampoMilkDairyPreparationAlimentations.get_aisles(cmdargs[1])
                case "AlcampoMilkEggsAlimentations":
                    aisles = AlcampoMilkEggsAlimentations.get_aisles(cmdargs[1])
                case "AlcampoMilkYoghurtAlimentations":
                    aisles = AlcampoMilkYoghurtAlimentations.get_aisles(cmdargs[1])
                case "AlcampoMilkDairyDessertsAlimentations":
                    aisles = AlcampoMilkDairyDessertsAlimentations.get_aisles(cmdargs[1])
                case "AlcampoMilkButterAlimentations":
                    aisles = AlcampoMilkButterAlimentations.get_aisles(cmdargs[1])
                case "AlcampoMilkMargarineAlimentations":
                    aisles = AlcampoMilkMargarineAlimentations.get_aisles(cmdargs[1])
                case "AlcampoMilkCreamAlimentations":
                    aisles = AlcampoMilkCreamAlimentations.get_aisles(cmdargs[1])
                case "AlcampoMilkSmothiesAlimentations":
                    aisles = AlcampoMilkSmothiesAlimentations.get_aisles(cmdargs[1])
                case "AlcampoMilkJuicesAlimentations":
                    aisles = AlcampoMilkJuicesAlimentations.get_aisles(cmdargs[1])
                case "AlcampoMilkCondensedAlimentations":
                    aisles = AlcampoMilkCondensedAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFeedingOilVinegarSaltAndSpicesAlimentations":
                    aisles = AlcampoFeedingOilVinegarSaltAndSpicesAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFeedingCannedFishAlimentations":
                    aisles = AlcampoFeedingCannedFishAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFeedingCannedVegetablesAlimentations":
                    aisles = AlcampoFeedingCannedVegetablesAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFeedingCannedMeatAlimentations":
                    aisles = AlcampoFeedingCannedMeatAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFeedingFriedTomatoAndSaucesAlimentations":
                    aisles = AlcampoFeedingFriedTomatoAndSaucesAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFeedingAppetizersNutsAlimentations":
                    aisles = AlcampoFeedingAppetizersNutsAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFeedingPastaAlimentations":
                    aisles = AlcampoFeedingPastaAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFeedingRiceAndLegumesAlimentations":
                    aisles = AlcampoFeedingRiceAndLegumesAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFeedingBakeryFlourAndDoughsAlimentations":
                    aisles = AlcampoFeedingBakeryFlourAndDoughsAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFeedingSoupsBrothsAndCreamsAlimentations":
                    aisles = AlcampoFeedingSoupsBrothsAndCreamsAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFeedingInternationalFoodAlimentations":
                    aisles = AlcampoFeedingInternationalFoodAlimentations.get_aisles(cmdargs[1])
                case "AlcampoBreakfastCafesAlimentations":
                    aisles = AlcampoBreakfastCookiesAlimentations.get_aisles(cmdargs[1])
                case "CarrefourPainsEtPatisseries":
                    aisles = AlcampoBreakfastCookiesAlimentations.get_aisles(cmdargs[1])
                case "AlcampoBreakfastChocolatesAlimentations":
                    aisles = AlcampoBreakfastChocolatesAlimentations.get_aisles(cmdargs[1])
                case "AlcampoBreakfastPastriesAndCakesAlimentations":
                    aisles = AlcampoBreakfastPastriesAndCakesAlimentations.get_aisles(cmdargs[1])
                case "AlcampoBreakfastCerealsAndBarsAlimentations":
                    aisles = AlcampoBreakfastCerealsAndBarsAlimentations.get_aisles(cmdargs[1])
                case "AlcampoBreakfastSugarAlimentations":
                    aisles = AlcampoBreakfastSugarAlimentations.get_aisles(cmdargs[1])
                case "AlcampoBreakfastCocaoAlimentations":
                    aisles = AlcampoBreakfastCocaoAlimentations.get_aisles(cmdargs[1])
                case "AlcampoBreakfastTeaAndInfusionAlimentations":
                    aisles = AlcampoBreakfastTeaAndInfusionAlimentations.get_aisles(cmdargs[1])
                case "AlcampoBreakfastJamAlimentations":
                    aisles = AlcampoBreakfastJamAlimentations.get_aisles(cmdargs[1])
                case "AlcampoBreakfastCandiesAlimentations":
                    aisles = AlcampoBreakfastCandiesAlimentations.get_aisles(cmdargs[1])
                case "AlcampoBreakfastDessertsPreparationAlimentations":
                    aisles = AlcampoBreakfastDessertsPreparationAlimentations.get_aisles(cmdargs[1])
                case "AlcampoBreakfastFoodBankAlimentations":
                    aisles = AlcampoBreakfastFoodBankAlimentations.get_aisles(cmdargs[1])
                case "AlcampoBreakfastNougatsAlimentations":
                    aisles = AlcampoBreakfastNougatsAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFrozentFishAlimentations":
                    aisles = AlcampoFrozentFishAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFrozentIceCreamAlimentations":
                    aisles = AlcampoFrozentIceCreamAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFrozentVegetablesAlimentations":
                    aisles = AlcampoFrozentVegetablesAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFrozentMealsAlimentations":
                    aisles = AlcampoFrozentMealsAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFrozentPotatoesAlimentations":
                    aisles = AlcampoFrozentPotatoesAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFrozentBreadedChickenAlimentations":
                    aisles = AlcampoFrozentBreadedChickenAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFrozentMeatAlimentations":
                    aisles = AlcampoFrozentMeatAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFrozentPastriesAlimentations":
                    aisles = AlcampoFrozentPastriesAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFrozentFruitAlimentations":
                    aisles = AlcampoFrozentFruitAlimentations.get_aisles(cmdargs[1])
                case "AlcampoFrozentEssentialsAlimentations":
                    aisles = AlcampoFrozentEssentialsAlimentations.get_aisles(cmdargs[1])
                case "AlcampoPreparedSushiAlimentations":
                    aisles = AlcampoPreparedSushiAlimentations.get_aisles(cmdargs[1])
                case "AlcampoPreparedPizzaAlimentations":
                    aisles = AlcampoPreparedPizzaAlimentations.get_aisles(cmdargs[1])
                case "AlcampoPreparedGazpachosAlimentations":
                    aisles = AlcampoPreparedGazpachosAlimentations.get_aisles(cmdargs[1])
                case "AlcampoPreparedTortillasAlimentations":
                    aisles = AlcampoPreparedTortillasAlimentations.get_aisles(cmdargs[1])
                case "AlcampoPreparedRiceAndPastaAlimentations":
                    aisles = AlcampoPreparedRiceAndPastaAlimentations.get_aisles(cmdargs[1])
                case "AlcampoPreparedOtherSpecialitiesAlimentations":
                    aisles = AlcampoPreparedOtherSpecialitiesAlimentations.get_aisles(cmdargs[1])
                case "AlcampoPreparedHummusAlimentations":
                    aisles = AlcampoPreparedHummusAlimentations.get_aisles(cmdargs[1])
                case "AlcampoPreparedInternationalDishesAlimentations":
                    aisles = AlcampoPreparedInternationalDishesAlimentations.get_aisles(cmdargs[1])
                case "AlcampoPreparedBassesAlimentations":
                    aisles = AlcampoPreparedBassesAlimentations.get_aisles(cmdargs[1])
                case "AlcampoPreparedVegeterianFoodAlimentations":
                    aisles = AlcampoPreparedVegeterianFoodAlimentations.get_aisles(cmdargs[1])
                case "AlcampoPreparedSandwichAlimentations":
                    aisles = AlcampoPreparedSandwichAlimentations.get_aisles(cmdargs[1])
                case "AlcampoPreparedRoastMeatsAlimentations":
                    aisles = AlcampoPreparedRoastMeatsAlimentations.get_aisles(cmdargs[1])
                case "AlcampoPreparedRefrigiratedSaladsAlimentations":
                    aisles = AlcampoPreparedRefrigiratedSaladsAlimentations.get_aisles(cmdargs[1])
                case "AlcampoPreparedEmpanadasAlimentations":
                    aisles = AlcampoPreparedEmpanadasAlimentations.get_aisles(cmdargs[1])
                case "AlcampoPreparedCannedDishesAlimentations":
                    aisles = AlcampoPreparedCannedDishesAlimentations.get_aisles(cmdargs[1])
                case "AlcampoPreparedEssentialsAlimentations":
                    aisles = AlcampoPreparedEssentialsAlimentations.get_aisles(cmdargs[1])
                case "AlcampoDrinksSoftDrinksAlimentations":
                    aisles = AlcampoDrinksSoftDrinksAlimentations.get_aisles(cmdargs[1])
                case "AlcampoDrinksWaterSodaAlimentations":
                    aisles = AlcampoDrinksWaterSodaAlimentations.get_aisles(cmdargs[1])
                case "AlcampoDrinksJuicesAlimentations":
                    aisles = AlcampoDrinksJuicesAlimentations.get_aisles(cmdargs[1])
                case "AlcampoDrinksBeersAlimentations":
                    aisles = AlcampoDrinksBeersAlimentations.get_aisles(cmdargs[1])
                case "AlcampoDrinksRedWineAlimentations":
                    aisles = AlcampoDrinksRedWineAlimentations.get_aisles(cmdargs[1])
                case "AlcampoDrinksWhiteWineAlimentations":
                    aisles = AlcampoDrinksWhiteWineAlimentations.get_aisles(cmdargs[1])
                case "AlcampoDrinksRoséAlimentations":
                    aisles = AlcampoDrinksRoséAlimentations.get_aisles(cmdargs[1])
                case "AlcampoDrinksChampagneAlimentations":
                    aisles = AlcampoDrinksChampagneAlimentations.get_aisles(cmdargs[1])
                case "AlcampoDrinksAlcoholicBeveragesAlimentations":
                    aisles = AlcampoDrinksAlcoholicBeveragesAlimentations.get_aisles(cmdargs[1])
                case "AlcampoDrinksLiquorsAlimentations":
                    aisles = AlcampoDrinksLiquorsAlimentations.get_aisles(cmdargs[1])
                case "AlcampoDrinksZero0Alimentations":
                    aisles = AlcampoDrinksZero0Alimentations.get_aisles(cmdargs[1])
                case "AlcampoDrinksNonAlcoholicWinesAlimentations":
                    aisles = AlcampoDrinksNonAlcoholicWinesAlimentations.get_aisles(cmdargs[1])
                case "AlcampoDrinksOrganicWinesAlimentations":
                    aisles = AlcampoDrinksOrganicWinesAlimentations.get_aisles(cmdargs[1])
                case "AlcampoSupermarketOrganicProductAlimentations":
                    aisles = AlcampoSupermarketOrganicProductAlimentations.get_aisles(cmdargs[1])
                case "AlcampoSupermarketOrganicDairyAlimentations":
                    aisles = AlcampoSupermarketOrganicDairyAlimentations.get_aisles(cmdargs[1])
                case "AlcampoSupermarketOrganicPantryAlimentations":
                    aisles = AlcampoSupermarketOrganicPantryAlimentations.get_aisles(cmdargs[1])
                case "AlcampoSupermarketOrganicBreakfastAlimentations":
                    aisles = AlcampoSupermarketOrganicBreakfastAlimentations.get_aisles(cmdargs[1])
                case "AlcampoSupermarketOrganicDrinksAlimentations":
                    aisles = AlcampoSupermarketOrganicDrinksAlimentations.get_aisles(cmdargs[1])
                case "AlcampoSupermarketOrganicBabyFoodAlimentations":
                    aisles = AlcampoSupermarketOrganicBabyFoodAlimentations.get_aisles(cmdargs[1])
                case "AlcampoSupermarketFairTradeAlimentations":
                    aisles = AlcampoSupermarketFairTradeAlimentations.get_aisles(cmdargs[1])
                case "AlcampoGlutenFreeAlimentations":
                    aisles = AlcampoGlutenFreeAlimentations.get_aisles(cmdargs[1])
                case "AlcampoGlutenLactoseFreeAlimentations":
                    aisles = AlcampoGlutenLactoseFreeAlimentations.get_aisles(cmdargs[1])
                case "AlcampoGlutenSportsNutritionAlimentations":
                    aisles = AlcampoGlutenSportsNutritionAlimentations.get_aisles(cmdargs[1])
                case "AlcampoGlutenNutritionalSupplementsAlimentations":
                    aisles = AlcampoGlutenNutritionalSupplementsAlimentations.get_aisles(cmdargs[1])
                case "AlcampoGlutenSeedsAlimentations":
                    aisles = AlcampoGlutenSeedsAlimentations.get_aisles(cmdargs[1])
                case "AlcampoGlutenDietAlimentations":
                    aisles = AlcampoGlutenDietAlimentations.get_aisles(cmdargs[1])
                case "AlcampoGlutenClassicDieteticsAlimentations":
                    aisles = AlcampoGlutenClassicDieteticsAlimentations.get_aisles(cmdargs[1])
                case "AlcampoGlutenDietaryWithoutAddedSugarsAlimentations":
                    aisles = AlcampoGlutenDietaryWithoutAddedSugarsAlimentations.get_aisles(cmdargs[1])
                case "AlcampoGlutenPancakeAlimentations":
                    aisles = AlcampoGlutenPancakeAlimentations.get_aisles(cmdargs[1])
                case "AlcampoGlutenHerbalistAlimentations":
                    aisles = AlcampoGlutenHerbalistAlimentations.get_aisles(cmdargs[1])
                case "AlcampoGlutenFunctionalFoodsAlimentations":
                    aisles = AlcampoGlutenFunctionalFoodsAlimentations.get_aisles(cmdargs[1])
                case "AlcampoVeganProteinAlimentations":
                    aisles = AlcampoVeganProteinAlimentations.get_aisles(cmdargs[1])
                case "AlcampoVeganDietAlimentations":
                    aisles = AlcampoVeganDietAlimentations.get_aisles(cmdargs[1])
                case "AlcampoVeganWineAlimentations":
                    aisles = AlcampoVeganWineAlimentations.get_aisles(cmdargs[1])
                case "AlcampoVeganDrinksAlimentations":
                    aisles = AlcampoVeganDrinksAlimentations.get_aisles(cmdargs[1])
                case "AlcampoBabyInfantNutritionAlimentations":
                    aisles = AlcampoBabyInfantNutritionAlimentations.get_aisles(cmdargs[1])
                case "AlcampoPetsDogFoodAlimentations":
                    aisles = AlcampoPetsDogFoodAlimentations.get_aisles(cmdargs[1])
                case "AlcampoPetsCatsFoodAlimentations":
                    aisles = AlcampoPetsCatsFoodAlimentations.get_aisles(cmdargs[1])
                case "AlcampoPetsRabbitsFoodAlimentations":
                    aisles = AlcampoPetsRabbitsFoodAlimentations.get_aisles(cmdargs[1])
                case "AlcampoPetsFishFoodAlimentations":
                    aisles = AlcampoPetsFishFoodAlimentations.get_aisles(cmdargs[1])
                case "AlcampoPetsBirdsFoodAlimentations":
                    aisles = AlcampoPetsBirdsFoodAlimentations.get_aisles(cmdargs[1])
                case _:
                    logging.error(f"args source not found: {cmdargs[1]}")
                    sys.exit()

    return aisles