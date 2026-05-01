import logging
import os
import sys
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

class DiaAirFryerAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Air_Fryer")

    AIR_FRYER_POTATOES = StaticAisle(name="Air fryer potatoes",  url="https://www.dia.es/freidora-de-aire-airfryer/patatas-airfryer/c/L2231",
                                     original_file_uri=os.path.join(category_path(), "Air_fryer_potatoes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Air_fryer_potatoes_detailed.json"))
    
    AIR_FRYER_BATTERS = StaticAisle(name="Airfryer batters", url="https://www.dia.es/freidora-de-aire-airfryer/rebozados-airfryer/c/L2232",
                                     original_file_uri=os.path.join(category_path(), "Airfryer_batters.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Airfryer_batters_detailed.json"))
    
    AIR_FRYER_VEGETABLES = StaticAisle(name="Air fryer vegetables",  url="https://www.dia.es/freidora-de-aire-airfryer/verduras-airfryer/c/L2233",
                                     original_file_uri=os.path.join(category_path(), "Air_fryer_vegetables.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Air_fryer_vegetables_detailed.json"))
    
    FISH_AND_SEAFOOD_AIR_FRYER = StaticAisle(name="Fish and seafood airfryer",  url="https://www.dia.es/freidora-de-aire-airfryer/pescados-y-mariscos-airfryer/c/L2234",
                                     original_file_uri=os.path.join(category_path(), "Fish_and_seafood_airfryer.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fish_and_seafood_airfryer_detailed.json"))
    
    MEAT_AIR_FRYER = StaticAisle(name="Meat airfryer",  url="https://www.dia.es/freidora-de-aire-airfryer/carne-airfryer/c/L2235",
                                     original_file_uri=os.path.join(category_path(), "Meat_airfryer.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Meat_airfryer_detailed.json"))
    
    PREPARED_FOOD_AIR_FRYER = StaticAisle(name="Prepared food airfryer",  url="https://www.dia.es/freidora-de-aire-airfryer/comida-preparada-airfryer/c/L2236",
                                     original_file_uri=os.path.join(category_path(), "Prepared_food_airfryer.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Prepared_food_airfryer_detailed.json"))
    
    AIR_FRYER_ACCESSORIES = StaticAisle(name="Air fryer accessories",  url="https://www.dia.es/freidora-de-aire-airfryer/accesorios-airfryer/c/L2237",
                                     original_file_uri=os.path.join(category_path(), "Air_fryer_accessories.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Air_fryer_accessories_detailed.json"))
    

    aisles: Final[List[StaticAisle]] = [AIR_FRYER_POTATOES, AIR_FRYER_BATTERS, AIR_FRYER_VEGETABLES, FISH_AND_SEAFOOD_AIR_FRYER, MEAT_AIR_FRYER, PREPARED_FOOD_AIR_FRYER, AIR_FRYER_ACCESSORIES]

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
                case "AIR_FRYER_POTATOES":
                    aisles = [cls.AIR_FRYER_POTATOES]
                case "AIR_FRYER_BATTERS":
                    aisles = [cls.AIR_FRYER_BATTERS]
                case "AIR_FRYER_VEGETABLES":
                    aisles = [cls.AIR_FRYER_VEGETABLES]
                case "FISH_AND_SEAFOOD_AIR_FRYER":
                    aisles = [cls.FISH_AND_SEAFOOD_AIR_FRYER]
                case "MEAT_AIR_FRYER":
                    aisles = [cls.MEAT_AIR_FRYER]
                case "PREPARED_FOOD_AIR_FRYER":
                    aisles = [cls.PREPARED_FOOD_AIR_FRYER]
                case "AIR_FRYER_ACCESSORIES":
                    aisles = [cls.AIR_FRYER_ACCESSORIES]
        return aisles
    
class DiaCharcuterieAndCheesesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Charcuterie_And_Cheeses")

    COOKED_HAM_CURED_HAM_COLD_CUTS_AND_MORTADELLA = StaticAisle(name="Cooked ham, cured ham, cold cuts and mortadella",  url="https://www.dia.es/charcuteria-y-quesos/jamon-cocido-lacon-fiambres-y-mortadela/c/L2001",
                                     original_file_uri=os.path.join(category_path(), "Cooked_ham_cured_ham_cold_cuts_and_mortadella.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cooked_ham_cured_ham_cold_cuts_and_mortadella_detailed.json"))
    
    CURED_HAM_AND_SHOULDER = StaticAisle(name="Cured ham and shoulder", url="https://www.dia.es/charcuteria-y-quesos/jamon-curado-y-paleta/c/L2004",
                                     original_file_uri=os.path.join(category_path(), "Cured_ham_and_shoulder.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cured_ham_and_shoulder_detailed.json"))
    
    PORK_LOIN_CHORIZO_FUET_SALAMI_SALAMI = StaticAisle(name="Pork loin, chorizo, fuet, salami, salami",  url="https://www.dia.es/charcuteria-y-quesos/lomo-chorizo-fuet-salchichon/c/L2005",
                                     original_file_uri=os.path.join(category_path(), "Pork_loin_chorizo_fuet_salami_salami.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pork_loin_chorizo_fuet_salami_salami_detailed.json"))
    
    CURED_SEMI_CURED_AND_SOFT_CHEESE = StaticAisle(name="Cured, semi-cured and soft cheese",  url="https://www.dia.es/charcuteria-y-quesos/queso-curado-semicurado-y-tierno/c/L2007",
                                     original_file_uri=os.path.join(category_path(), "Cured_semi-cured_and_soft_cheese.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cured_semi-cured_and_soft_cheese_detailed.json"))
    
    FRESH_CHEESE = StaticAisle(name="Fresh cheese",  url="https://www.dia.es/charcuteria-y-quesos/queso-fresco/c/L2008",
                                     original_file_uri=os.path.join(category_path(), "Fresh_cheese.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fresh_cheese_detailed.json"))
    
    BLUE_CHEESE_AND_ROQUEFORT = StaticAisle(name="Blue cheese and roquefort",  url="https://www.dia.es/charcuteria-y-quesos/queso-azul-y-roquefort/c/L2009",
                                     original_file_uri=os.path.join(category_path(), "Blue_cheese_and_roquefort.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Blue_cheese_and_roquefort_detailed.json"))
    
    PROCESSED_CHEESE_AND_CREAMS = StaticAisle(name="Processed cheese and creams",  url="https://www.dia.es/charcuteria-y-quesos/quesos-fundidos-y-cremas/c/L2010",
                                     original_file_uri=os.path.join(category_path(), "Processed_cheese_and_creams.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Processed_cheese_and_creams_detailed.json"))
    
    INTERNATIONAL_CHEESES = StaticAisle(name="International cheeses",  url="https://www.dia.es/charcuteria-y-quesos/quesos-internacionales/c/L2011",
                                     original_file_uri=os.path.join(category_path(), "International_cheeses.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "International_cheeses_detailed.json"))
    
    SAUSAGES = StaticAisle(name="Sausages",  url="https://www.dia.es/charcuteria-y-quesos/salchichas/c/L2206",
                                     original_file_uri=os.path.join(category_path(), "Sausages.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sausages_detailed.json"))
    
    FOIE_PÂTÉ_AND_SOBRASADA = StaticAisle(name="Foie, pâté and sobrasada",  url="https://www.dia.es/charcuteria-y-quesos/foie-pate-y-sobrasada/c/L2012",
                                     original_file_uri=os.path.join(category_path(), "Foie_pâté_and_sobrasada.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Foie_pâté_and_sobrasada_detailed.json"))
    
    
    

    aisles: Final[List[StaticAisle]] = [COOKED_HAM_CURED_HAM_COLD_CUTS_AND_MORTADELLA , CURED_HAM_AND_SHOULDER , PORK_LOIN_CHORIZO_FUET_SALAMI_SALAMI , CURED_SEMI_CURED_AND_SOFT_CHEESE , FRESH_CHEESE , BLUE_CHEESE_AND_ROQUEFORT , PROCESSED_CHEESE_AND_CREAMS , INTERNATIONAL_CHEESES , SAUSAGES , FOIE_PÂTÉ_AND_SOBRASADA]

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
                case "COOKED_HAM_CURED_HAM_COLD_CUTS_AND_MORTADELLA":
                    aisles = [cls.COOKED_HAM_CURED_HAM_COLD_CUTS_AND_MORTADELLA]
                case "CURED_HAM_AND_SHOULDER":
                    aisles = [cls.CURED_HAM_AND_SHOULDER]
                case "PORK_LOIN_CHORIZO_FUET_SALAMI_SALAMI":
                    aisles = [cls.PORK_LOIN_CHORIZO_FUET_SALAMI_SALAMI]
                case "CURED_SEMI_CURED_AND_SOFT_CHEESE":
                    aisles = [cls.CURED_SEMI_CURED_AND_SOFT_CHEESE]
                case "FRESH_CHEESE":
                    aisles = [cls.FRESH_CHEESE]
                case "BLUE_CHEESE_AND_ROQUEFORT":
                    aisles = [cls.BLUE_CHEESE_AND_ROQUEFORT]
                case "PROCESSED_CHEESE_AND_CREAMS":
                    aisles = [cls.PROCESSED_CHEESE_AND_CREAMS]
                case "INTERNATIONAL_CHEESES":
                    aisles = [cls.INTERNATIONAL_CHEESES]
                case "SAUSAGES":
                    aisles = [cls.SAUSAGES]
                case "FOIE_PÂTÉ_AND_SOBRASADA":
                    aisles = [cls.FOIE_PÂTÉ_AND_SOBRASADA]
        return aisles
    
class DiaButcheryAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Butchery")

    CHICKEN = StaticAisle(name="Chicken",  url="https://www.dia.es/carniceria/pollo/c/L2202",
                                     original_file_uri=os.path.join(category_path(), "Chicken.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chicken_detailed.json"))
    
    BEEF = StaticAisle(name="Beef", url="https://www.dia.es/carniceria/vacuno/c/L2013",
                                     original_file_uri=os.path.join(category_path(), "Beef.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Beef_detailed.json"))
    
    PORK = StaticAisle(name="Pork",  url="https://www.dia.es/carniceria/cerdo/c/L2014",
                                     original_file_uri=os.path.join(category_path(), "Pork.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pork_detailed.json"))
    
    TURKEY = StaticAisle(name="Turkey",  url="https://www.dia.es/carniceria/pavo/c/L2015",
                                     original_file_uri=os.path.join(category_path(), "Turkey.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Turkey_detailed.json"))
    
    RABBIT = StaticAisle(name="Rabbit",  url="https://www.dia.es/carniceria/conejo/c/L2016",
                                     original_file_uri=os.path.join(category_path(), "Rabbit.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Rabbit_detailed.json"))
    
    HAMBURGERS_AND_MINCED_MEAT = StaticAisle(name="Hamburgers and minced meat",  url="https://www.dia.es/carniceria/hamburguesas-y-carne-picada/c/L2017",
                                     original_file_uri=os.path.join(category_path(), "Hamburgers_and_minced_meat.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Hamburgers_and_minced_meat_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [CHICKEN, BEEF, PORK, TURKEY, RABBIT, HAMBURGERS_AND_MINCED_MEAT]

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
                case "BEEF":
                    aisles = [cls.BEEF]
                case "PORK":
                    aisles = [cls.PORK]
                case "TURKEY":
                    aisles = [cls.TURKEY]
                case "RABBIT":
                    aisles = [cls.RABBIT]
                case "HAMBURGERS_AND_MINCED_MEAT":
                    aisles = [cls.HAMBURGERS_AND_MINCED_MEAT]
               
        return aisles
        
class DiaFishSmockedFishAndSeafoodAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Fish_Smocked_Fish_And_Seafood")

    FISH = StaticAisle(name="Fish",  url="https://www.dia.es/pescados-mariscos-y-ahumados/pescados/c/L2019",
                                     original_file_uri=os.path.join(category_path(), "Fish.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fish_detailed.json"))
    
    SEAFOOD = StaticAisle(name="Seafood", url="https://www.dia.es/pescados-mariscos-y-ahumados/mariscos/c/L2194",
                                     original_file_uri=os.path.join(category_path(), "Seafood.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Seafood_detailed.json"))
    
    SMOKED_SALTED_AND_PREPARED_FISH = StaticAisle(name="Smoked, salted and prepared fish",  url="https://www.dia.es/pescados-mariscos-y-ahumados/ahumados-salazones-y-preparados/c/L2020",
                                     original_file_uri=os.path.join(category_path(), "Smoked_salted_and_prepared_fish.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Smoked_salted_and_prepared_fish_detailed.json"))
    
    SUBSTITUTE_FOR_ELVERS_AND_SURIMI = StaticAisle(name="Substitute for elvers and surimi",  url="https://www.dia.es/pescados-mariscos-y-ahumados/sucedaneo-de-angulas-y-surimi/c/L2021",
                                     original_file_uri=os.path.join(category_path(), "Substitute_for_elvers_and_surimi.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Substitute_for_elvers_and_surimi_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [FISH, SEAFOOD, SMOKED_SALTED_AND_PREPARED_FISH, SUBSTITUTE_FOR_ELVERS_AND_SURIMI]
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
                case "SMOKED_SALTED_AND_PREPARED_FISH":
                    aisles = [cls.SMOKED_SALTED_AND_PREPARED_FISH]
                case "SUBSTITUTE_FOR_ELVERS_AND_SURIMI":
                    aisles = [cls.SUBSTITUTE_FOR_ELVERS_AND_SURIMI]
             
        return aisles

class DiaVegetablesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Vegetables")

    GARLIC_ONIONS_AND_LEEKS = StaticAisle(name="Garlic, onions and leeks",  url="https://www.dia.es/verduras/ajos-cebollas-y-puerros/c/L2022",
                                     original_file_uri=os.path.join(category_path(), "Garlic_onions_and_leeks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Garlic_onions_and_leeks_detailed.json"))
    
    TOMATOES_PEPPERS_AND_CUCUMBERS = StaticAisle(name="Tomatoes, peppers and cucumbers", url="https://www.dia.es/verduras/tomates-pimientos-y-pepinos/c/L2023",
                                     original_file_uri=os.path.join(category_path(), "Tomatoes_peppers_and_cucumbers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tomatoes_peppers_and_cucumbers_detailed.json"))
    
    COURGETTE_PUMPKIN_AND_AUBERGINE = StaticAisle(name="Courgette, pumpkin and aubergine",  url="https://www.dia.es/verduras/calabacin-calabaza-y-berenjena/c/L2181",
                                     original_file_uri=os.path.join(category_path(), "Courgette_pumpkin_and_aubergine.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Courgette_pumpkin_and_aubergine_detailed.json"))
    
    BEANS_BROCCOLI_AND_CAULIFLOWER = StaticAisle(name="Beans, broccoli and cauliflower",  url="https://www.dia.es/verduras/judias-brocolis-y-coliflores/c/L2024",
                                     original_file_uri=os.path.join(category_path(), "Beans_broccoli_and_cauliflower.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Beans_broccoli_and_cauliflower_detailed.json"))
    
    LETTUCE_ESCAROLE_AND_ENDIVE = StaticAisle(name="Lettuce, escarole and endive",  url="https://www.dia.es/verduras/lechuga-escarolas-y-endivias/c/L2027",
                                     original_file_uri=os.path.join(category_path(), "Lettuce_escarole_and_endive.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Lettuce_escarole_and_endive_detailed.json"))
    
    POTATOES_AND_CARROTS = StaticAisle(name="Potatoes and carrots", url="https://www.dia.es/verduras/patatas-y-zanahorias/c/L2028",
                                     original_file_uri=os.path.join(category_path(), "Potatoes_and_carrots.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Potatoes_and_carrots_detailed.json"))
    
    MUSHROOMS = StaticAisle(name="Mushrooms",  url="https://www.dia.es/verduras/setas-y-champinones/c/L2029",
                                     original_file_uri=os.path.join(category_path(), "Mushrooms.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mushrooms_detailed.json"))
    
    VEGETABLES_AND_PREPARED_SALADS = StaticAisle(name="Vegetables and prepared salads",  url="https://www.dia.es/verduras/verduras-y-ensaladas-preparadas/c/L2030",
                                     original_file_uri=os.path.join(category_path(), "Vegetables_and_prepared_salads.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vegetables_and_prepared_salads_detailed.json"))
    
    OTHER_VEGETABLES = StaticAisle(name="Other vegetables",  url="https://www.dia.es/verduras/otras-verduras/c/L2031",
                                     original_file_uri=os.path.join(category_path(), "Other_vegetables.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_vegetables_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [GARLIC_ONIONS_AND_LEEKS, TOMATOES_PEPPERS_AND_CUCUMBERS, COURGETTE_PUMPKIN_AND_AUBERGINE, BEANS_BROCCOLI_AND_CAULIFLOWER, LETTUCE_ESCAROLE_AND_ENDIVE, POTATOES_AND_CARROTS, MUSHROOMS, VEGETABLES_AND_PREPARED_SALADS, OTHER_VEGETABLES]
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
                case "GARLIC_ONIONS_AND_LEEKS":
                    aisles = [cls.GARLIC_ONIONS_AND_LEEKS]
                case "TOMATOES_PEPPERS_AND_CUCUMBERS":
                    aisles = [cls.TOMATOES_PEPPERS_AND_CUCUMBERS]
                case "COURGETTE_PUMPKIN_AND_AUBERGINE":
                    aisles = [cls.COURGETTE_PUMPKIN_AND_AUBERGINE]
                case "BEANS_BROCCOLI_AND_CAULIFLOWER":
                    aisles = [cls.BEANS_BROCCOLI_AND_CAULIFLOWER]
                case "LETTUCE_ESCAROLE_AND_ENDIVE":
                    aisles = [cls.LETTUCE_ESCAROLE_AND_ENDIVE]
                case "POTATOES_AND_CARROTS":
                    aisles = [cls.POTATOES_AND_CARROTS]
                case "MUSHROOMS":
                    aisles = [cls.MUSHROOMS]
                case "VEGETABLES_AND_PREPARED_SALADS":
                    aisles = [cls.VEGETABLES_AND_PREPARED_SALADS]
                case "OTHER_VEGETABLES":
                    aisles = [cls.OTHER_VEGETABLES]
               
             
        return aisles
    
class DiaFruitsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Fruits")

    SEASONAL_FRUITS = StaticAisle(name="Seasonal fruits",  url="https://www.dia.es/frutas/frutas-de-temporada/c/L2040",
                                     original_file_uri=os.path.join(category_path(), "Seasonal_fruits.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Seasonal_fruits_detailed.json"))
    
    APPLES = StaticAisle(name="Apples", url="https://www.dia.es/frutas/manzanas/c/L2032",
                                     original_file_uri=os.path.join(category_path(), "Apples.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Apples_detailed.json"))
    
    BANANAS = StaticAisle(name="Bananas",  url="https://www.dia.es/frutas/platanos/c/L2033",
                                     original_file_uri=os.path.join(category_path(), "Bananas.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Bananas_detailed.json"))
    
    PEARS = StaticAisle(name="Pears",  url="https://www.dia.es/frutas/peras/c/L2034",
                                     original_file_uri=os.path.join(category_path(), "Pears.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pears_detailed.json"))
    
    ORANGES_AND_TANGERINES = StaticAisle(name="Oranges and tangerines", url="https://www.dia.es/frutas/naranjas-y-mandarinas/c/L2196",
                                     original_file_uri=os.path.join(category_path(), "Oranges_and_tangerines.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Oranges_and_tangerines_detailed.json"))
    
    GRAPES = StaticAisle(name="Grapes",  url="https://www.dia.es/frutas/uvas/c/L2035",
                                     original_file_uri=os.path.join(category_path(), "Grapes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Grapes_detailed.json"))
    
    LEMONS_AND_GRAPEFRUIT = StaticAisle(name="Lemons and grapefruit",  url="https://www.dia.es/frutas/limones-y-pomelos/c/L2037",
                                     original_file_uri=os.path.join(category_path(), "Lemons_and_grapefruit.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Lemons_and_grapefruit_detailed.json"))
    
    FOREST_FRUITS = StaticAisle(name="Forest fruits",  url="https://www.dia.es/frutas/frutas-del-bosque/c/L2038",
                                     original_file_uri=os.path.join(category_path(), "Forest_fruits.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Forest_fruits_detailed.json"))
    
    TROPICAL_FRUITS = StaticAisle(name="Tropical fruits",  url="https://www.dia.es/frutas/frutas-tropicales/c/L2039",
                                     original_file_uri=os.path.join(category_path(), "Tropical_fruits.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tropical_fruits_detailed.json"))
    
    DRIED_FRUIT = StaticAisle(name="Dried fruit",  url="https://www.dia.es/frutas/frutas-deshidratadas/c/L2041",
                                     original_file_uri=os.path.join(category_path(), "Dried_fruit.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Dried_fruit_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [SEASONAL_FRUITS, APPLES, BANANAS, PEARS, ORANGES_AND_TANGERINES, GRAPES, LEMONS_AND_GRAPEFRUIT, FOREST_FRUITS, TROPICAL_FRUITS, DRIED_FRUIT]
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
                case "SEASONAL_FRUITS":
                    aisles = [cls.SEASONAL_FRUITS]
                case "APPLES":
                    aisles = [cls.APPLES]
                case "BANANAS":
                    aisles = [cls.BANANAS]
                case "PEARS":
                    aisles = [cls.PEARS]
                case "ORANGES_AND_TANGERINES":
                    aisles = [cls.ORANGES_AND_TANGERINES]
                case "GRAPES":
                    aisles = [cls.GRAPES]
                case "LEMONS_AND_GRAPEFRUIT":
                    aisles = [cls.LEMONS_AND_GRAPEFRUIT]
                case "FOREST_FRUITS":
                    aisles = [cls.FOREST_FRUITS]
                case "TROPICAL_FRUITS":
                    aisles = [cls.TROPICAL_FRUITS]
                case "DRIED_FRUIT":
                    aisles = [cls.DRIED_FRUIT]
               
        return aisles
    
class DiaMilkEggsAndButterAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Milk_Eggs_And_Butter")

    MILK = StaticAisle(name="Milk",  url="https://www.dia.es/leche-huevos-y-mantequilla/leche/c/L2051",
                                     original_file_uri=os.path.join(category_path(), "Milk.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Milk_fruits_detailed.json"))
    
    VEGETABLE_DRINKS = StaticAisle(name="Vegetable drinks", url="https://www.dia.es/leche-huevos-y-mantequilla/bebidas-vegetales/c/L2052",
                                     original_file_uri=os.path.join(category_path(), "Vegetable_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vegetable_drinks_detailed.json"))
    
    MILKSHAKES_AND_HORCHATAS = StaticAisle(name="Milkshakes and horchatas",  url="https://www.dia.es/leche-huevos-y-mantequilla/batidos-y-horchatas/c/L2053",
                                     original_file_uri=os.path.join(category_path(), "Milkshakes_and_horchatas.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Milkshakes_and_horchatas_detailed.json"))
    
    EGGS = StaticAisle(name="Eggs",  url="https://www.dia.es/leche-huevos-y-mantequilla/huevos/c/L2055",
                                     original_file_uri=os.path.join(category_path(), "Eggs.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Eggs_detailed.json"))
    
    BUTTER_AND_MARGARINE = StaticAisle(name="Butter and margarine", url="https://www.dia.es/leche-huevos-y-mantequilla/mantequilla-y-margarina/c/L2056",
                                     original_file_uri=os.path.join(category_path(), "Butter_and_margarine.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Butter_and_margarine_detailed.json"))
    
    BORN = StaticAisle(name="Cream",  url="https://www.dia.es/leche-huevos-y-mantequilla/nata/c/L2054",
                                     original_file_uri=os.path.join(category_path(), "Cream.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cream_detailed.json"))
    
   
    aisles: Final[List[StaticAisle]] = [MILK, VEGETABLE_DRINKS, MILKSHAKES_AND_HORCHATAS, EGGS, BUTTER_AND_MARGARINE, BORN]
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
                case "MILK":
                    aisles = [cls.MILK]
                case "VEGETABLE_DRINKS":
                    aisles = [cls.VEGETABLE_DRINKS]
                case "MILKSHAKES_AND_HORCHATAS":
                    aisles = [cls.MILKSHAKES_AND_HORCHATAS]
                case "EGGS":
                    aisles = [cls.EGGS]
                case "BUTTER_AND_MARGARINE":
                    aisles = [cls.BUTTER_AND_MARGARINE]
                case "BORN":
                    aisles = [cls.BORN]
           
        return aisles
    
class DiaYoghurtsAndDessertsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Yoghurts_And_Desserts")

    GREEK_YOGURTS_AND_MOUSSE = StaticAisle(name="Greek yogurts and mousse",  url="https://www.dia.es/yogures-y-postres/griegos-y-mousse/c/L2082",
                                     original_file_uri=os.path.join(category_path(), "Greek_yogurts_and_mousse.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Greek_yogurts_and_mousse_detailed.json"))
    
    NATURAL_YOGHURTS = StaticAisle(name="Natural yoghurts", url="https://www.dia.es/yogures-y-postres/yogures-naturales/c/L2079",
                                     original_file_uri=os.path.join(category_path(), "Natural_yoghurts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Natural_yoghurts_detailed.json"))
    
    FLAVOURED_AND_FRUIT_YOGHURTS = StaticAisle(name="Flavoured and fruit yoghurts",  url="https://www.dia.es/yogures-y-postres/yogures-de-sabores-y-frutas/c/L2081",
                                     original_file_uri=os.path.join(category_path(), "Flavoured_and_fruit_yoghurts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Flavoured_and_fruit_yoghurts_detailed.json"))
    
    CHILDRENS_YOGHURTS = StaticAisle(name="Children's yoghurts",  url="https://www.dia.es/yogures-y-postres/yogures-infantiles/c/L2083",
                                     original_file_uri=os.path.join(category_path(), "Children's_yoghurts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Children's_yoghurts_detailed.json"))
    
    SKIMMED_YOGHURTS = StaticAisle(name="Skimmed yoghurts", url="https://www.dia.es/yogures-y-postres/yogures-desnatados/c/L2080",
                                     original_file_uri=os.path.join(category_path(), "Skimmed_yoghurts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Skimmed_yoghurts_detailed.json"))
    
    BIFIDUS_YOGHURTS_AND_CHOLESTEROL = StaticAisle(name="Bifidus yoghurts and cholesterol",  url="https://www.dia.es/yogures-y-postres/yogures-bifidus-y-colesterol/c/L2078",
                                     original_file_uri=os.path.join(category_path(), "Bifidus_yoghurts_and_cholesterol.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Bifidus_yoghurts_and_cholesterol_detailed.json"))
    
    SOY_AND_ENRICHED_YOGHURTS = StaticAisle(name="Soy and enriched yogurts",  url="https://www.dia.es/yogures-y-postres/yogures-de-soja-y-enriquecidos/c/L2084",
                                     original_file_uri=os.path.join(category_path(), "Soy_and_enriched_yogurts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Greek_yogurts_and_mousse_detailed.json"))
    
    KEFIR_AND_OTHER_YOGHURTS = StaticAisle(name="Kefir and other yogurts", url="https://www.dia.es/yogures-y-postres/kefir-y-otros-yogures/c/L2085",
                                     original_file_uri=os.path.join(category_path(), "Kefir_and_other_yogurts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Kefir_and_other_yogurts_detailed.json"))
    
    PROTEIN_DESSERTS_AND_YOGHURTS = StaticAisle(name="Protein desserts and yogurts",  url="https://www.dia.es/yogures-y-postres/postres-y-yogures-de-proteinas/c/L2229",
                                     original_file_uri=os.path.join(category_path(), "Protein_desserts_and_yogurts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Protein_desserts_and_yogurts_detailed.json"))
    
    CUSTARD_AND_PUDDING = StaticAisle(name="Custard and pudding",  url="https://www.dia.es/yogures-y-postres/natillas-y-flan/c/L2088",
                                     original_file_uri=os.path.join(category_path(), "Custard_and_pudding.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Custard_and_pudding_detailed.json"))
    
    RICE_PUDDING_AND_TRADITIONAL_DESSERTS = StaticAisle(name="Rice pudding and traditional desserts", url="https://www.dia.es/yogures-y-postres/arroz-con-leche-y-postre-tradicional/c/L2087",
                                     original_file_uri=os.path.join(category_path(), "Rice_pudding_and_traditional_desserts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Rice_pudding_and_traditional_desserts_detailed.json"))
    
    CURD = StaticAisle(name="Curd",  url="https://www.dia.es/yogures-y-postres/cuajada/c/L2086",
                                     original_file_uri=os.path.join(category_path(), "Curd.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Curd_detailed.json"))
    
    GELATINS_AND_OTHER_DESSERTS = StaticAisle(name="Gelatins and other desserts",  url="https://www.dia.es/yogures-y-postres/gelatinas-y-otros-postres/c/L2089",
                                     original_file_uri=os.path.join(category_path(), "Gelatins_and_other_desserts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Gelatins_and_other_desserts_detailed.json"))
   
    aisles: Final[List[StaticAisle]] = [GREEK_YOGURTS_AND_MOUSSE, NATURAL_YOGHURTS, FLAVOURED_AND_FRUIT_YOGHURTS, CHILDRENS_YOGHURTS, SKIMMED_YOGHURTS, BIFIDUS_YOGHURTS_AND_CHOLESTEROL, SOY_AND_ENRICHED_YOGHURTS, KEFIR_AND_OTHER_YOGHURTS, PROTEIN_DESSERTS_AND_YOGHURTS, CUSTARD_AND_PUDDING, RICE_PUDDING_AND_TRADITIONAL_DESSERTS, CURD, GELATINS_AND_OTHER_DESSERTS] 
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
                case "GREEK_YOGURTS_AND_MOUSSE":
                    aisles = [cls.GREEK_YOGURTS_AND_MOUSSE]
                case "NATURAL_YOGHURTS":
                    aisles = [cls.NATURAL_YOGHURTS]
                case "FLAVOURED_AND_FRUIT_YOGHURTS":
                    aisles = [cls.FLAVOURED_AND_FRUIT_YOGHURTS]
                case "CHILDRENS_YOGHURTS":
                    aisles = [cls.CHILDRENS_YOGHURTS]
                case "SKIMMED_YOGHURTS":
                    aisles = [cls.SKIMMED_YOGHURTS]
                case "BIFIDUS_YOGHURTS_AND_CHOLESTEROL":
                    aisles = [cls.BIFIDUS_YOGHURTS_AND_CHOLESTEROL]
                case "SOY_AND_ENRICHED_YOGHURTS":
                    aisles = [cls.SOY_AND_ENRICHED_YOGHURTS]
                case "KEFIR_AND_OTHER_YOGHURTS":
                    aisles = [cls.KEFIR_AND_OTHER_YOGHURTS]
                case "PROTEIN_DESSERTS_AND_YOGHURTS":
                    aisles = [cls.PROTEIN_DESSERTS_AND_YOGHURTS]
                case "CUSTARD_AND_PUDDING":
                    aisles = [cls.CUSTARD_AND_PUDDING]
                case "RICE_PUDDING_AND_TRADITIONAL_DESSERTS":
                    aisles = [cls.RICE_PUDDING_AND_TRADITIONAL_DESSERTS]
                case "CURD":
                    aisles = [cls.CURD]
                case "GELATINS_AND_OTHER_DESSERTS":
                    aisles = [cls.GELATINS_AND_OTHER_DESSERTS]
           
        return aisles
    
class DiaRicePastaAndPulsesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Rice_Pasta_And_Pulses")

    RICE = StaticAisle(name="Rice",  url="https://www.dia.es/arroz-pastas-y-legumbres/arroz/c/L2042",
                                     original_file_uri=os.path.join(category_path(), "Rice.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Rice_detailed.json"))
    
    PASTA = StaticAisle(name="Pasta", url="https://www.dia.es/arroz-pastas-y-legumbres/pastas/c/L2044",
                                     original_file_uri=os.path.join(category_path(), "Pasta.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pasta_yoghurts_detailed.json"))
    
    CHICKPEAS = StaticAisle(name="Chickpeas",  url="https://www.dia.es/arroz-pastas-y-legumbres/garbanzos/c/L2191",
                                     original_file_uri=os.path.join(category_path(), "Chickpeas.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chickpeas_detailed.json"))
    
    BEANS = StaticAisle(name="Beans",  url="https://www.dia.es/arroz-pastas-y-legumbres/alubias/c/L2178",
                                     original_file_uri=os.path.join(category_path(), "Beans.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Beans_detailed.json"))
    
    LENTILS = StaticAisle(name="Lentils", url="https://www.dia.es/arroz-pastas-y-legumbres/lentejas/c/L2193",
                                     original_file_uri=os.path.join(category_path(), "Lentils.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Lentils_detailed.json"))
    
    QUINOA_AND_COUSCOUS = StaticAisle(name="Quinoa and couscous",  url="https://www.dia.es/arroz-pastas-y-legumbres/quinoa-y-couscous/c/L2043",
                                     original_file_uri=os.path.join(category_path(), "Quinoa_and_couscous.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Quinoa_and_couscous_detailed.json"))
    
   
    aisles: Final[List[StaticAisle]] = [RICE, PASTA, CHICKPEAS, BEANS, LENTILS, QUINOA_AND_COUSCOUS] 
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
                case "PASTA":
                    aisles = [cls.PASTA]
                case "CHICKPEAS":
                    aisles = [cls.CHICKPEAS]
                case "BEANS":
                    aisles = [cls.BEANS]
                case "LENTILS":
                    aisles = [cls.LENTILS]
                case "QUINOA_AND_COUSCOUS":
                    aisles = [cls.QUINOA_AND_COUSCOUS]
             
        
        return aisles
    
class DiaOilSaucesAndSpicesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Oil_Sauces_And_Spicess")

    OILS = StaticAisle(name="Oils",  url="https://www.dia.es/aceites-salsas-y-especias/aceites/c/L2046",
                                     original_file_uri=os.path.join(category_path(), "Oils.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Oils_detailed.json"))
    
    VINEGARS_AND_DRESSINGS = StaticAisle(name="Vinegars and dressings", url="https://www.dia.es/aceites-salsas-y-especias/vinagres-y-alinos/c/L2047",
                                     original_file_uri=os.path.join(category_path(), "Vinegars_and_dressings.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vinegars_and_dressings_detailed.json"))
    
    FRIED_TOMATO = StaticAisle(name="Fried tomato",  url="https://www.dia.es/aceites-salsas-y-especias/tomate/c/L2208",
                                     original_file_uri=os.path.join(category_path(), "Fried_tomato.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fried_tomato_detailed.json"))
    
    MAYONNAISE_KETCHUP_AND_OTHER_SAUCES = StaticAisle(name="Mayonnaise, ketchup and other sauces",  url="https://www.dia.es/aceites-salsas-y-especias/mayonesa-ketchup-y-otras-salsas/c/L2050",
                                     original_file_uri=os.path.join(category_path(), "Mayonnaise_ketchup_and_other_sauces.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mayonnaise_ketchup_and_other_sauces_detailed.json"))
    
    SALT_AND_SPICES = StaticAisle(name="Salt and spices", url="https://www.dia.es/aceites-salsas-y-especias/sal-y-especias/c/L2048",
                                     original_file_uri=os.path.join(category_path(), "Salt_and_spices.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Salt_and_spices_detailed.json"))
    

    aisles: Final[List[StaticAisle]] = [OILS, VINEGARS_AND_DRESSINGS, FRIED_TOMATO, MAYONNAISE_KETCHUP_AND_OTHER_SAUCES, SALT_AND_SPICES] 
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
                case "VINEGARS_AND_DRESSINGS":
                    aisles = [cls.VINEGARS_AND_DRESSINGS]
                case "FRIED_TOMATO":
                    aisles = [cls.FRIED_TOMATO]
                case "MAYONNAISE_KETCHUP_AND_OTHER_SAUCES":
                    aisles = [cls.MAYONNAISE_KETCHUP_AND_OTHER_SAUCES]
                case "SALT_AND_SPICES":
                    aisles = [cls.SALT_AND_SPICES]
        
        return aisles
    
class DiaCannedFoodBrothsAndCreamsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Canned_Food_Broths_And_Creams")

    TUNA_BONITO_AND_MACKEREL = StaticAisle(name="Tuna, bonito and mackere",  url="https://www.dia.es/conservas-caldos-y-cremas/atun-bonito-y-caballa/c/L2179",
                                     original_file_uri=os.path.join(category_path(), "Tuna_bonito_and_mackere.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tuna_bonito_and_mackere_detailed.json"))
    
    COCKLES = StaticAisle(name="Cockles", url="https://www.dia.es/conservas-caldos-y-cremas/berberechos/c/L2180",
                                     original_file_uri=os.path.join(category_path(), "Cockles.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cockles_detailed.json"))
    
    MUSSELS = StaticAisle(name="Mussels",  url="https://www.dia.es/conservas-caldos-y-cremas/mejillones/c/L2195",
                                     original_file_uri=os.path.join(category_path(), "Mussels.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Mussels_detailed.json"))
    
    SARDINES = StaticAisle(name="Sardines",  url="https://www.dia.es/conservas-caldos-y-cremas/sardinas-y-sardinillas/c/L2207",
                                     original_file_uri=os.path.join(category_path(), "Sardines.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sardines_detailed.json"))
    
    OTHER_CANNED_FISH = StaticAisle(name="Other canned fish", url="https://www.dia.es/conservas-caldos-y-cremas/otras-conservas-de-pescado/c/L2197",
                                     original_file_uri=os.path.join(category_path(), "Other_canned_fish.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_canned_fish_detailed.json"))
    
    CANNED_VEGETABLES = StaticAisle(name="Canned vegetables",  url="https://www.dia.es/conservas-caldos-y-cremas/conservas-vegetales/c/L2092",
                                     original_file_uri=os.path.join(category_path(), "Canned_vegetables.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Canned_vegetables_detailed.json"))
    
    DEHYDRATED_SOUPS_BROTHS_AND_PUREES = StaticAisle(name="Dehydrated soups broths and purees",  url="https://www.dia.es/conservas-caldos-y-cremas/sopas-caldos-y-pures-deshidratados/c/L2093",
                                     original_file_uri=os.path.join(category_path(), "Dehydrated_soups_broths_and_purees.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Dehydrated_soups_broths_and_purees_detailed.json"))
    
    CREAMS_AND_LIQUID_BROTHS = StaticAisle(name="Creams and liquid broths", url="https://www.dia.es/conservas-caldos-y-cremas/cremas-y-caldos-liquidos/c/L2094",
                                     original_file_uri=os.path.join(category_path(), "Creams_and_liquid_broths.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Creams_and_liquid_broths_detailed.json"))
    

    aisles: Final[List[StaticAisle]] = [TUNA_BONITO_AND_MACKEREL, COCKLES, MUSSELS, SARDINES, OTHER_CANNED_FISH, CANNED_VEGETABLES, DEHYDRATED_SOUPS_BROTHS_AND_PUREES, CREAMS_AND_LIQUID_BROTHS] 
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
                case "TUNA_BONITO_AND_MACKEREL":
                    aisles = [cls.TUNA_BONITO_AND_MACKEREL]
                case "COCKLES":
                    aisles = [cls.VINEGARS_AND_DRESSINGS]
                case "MUSSELS":
                    aisles = [cls.MUSSELS]
                case "SARDINES":
                    aisles = [cls.SARDINES]
                case "OTHER_CANNED_FISH":
                    aisles = [cls.OTHER_CANNED_FISH]
                case "CANNED_VEGETABLES":
                    aisles = [cls.CANNED_VEGETABLES]
                case "DEHYDRATED_SOUPS_BROTHS_AND_PUREES":
                    aisles = [cls.DEHYDRATED_SOUPS_BROTHS_AND_PUREES]
                case "CREAMS_AND_LIQUID_BROTHS":
                    aisles = [cls.CREAMS_AND_LIQUID_BROTHS]
        
        return aisles
    
class DiaBreadsFloursAndDoughsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Breads_Flours_And_Doughs")

    FRESHLY_BAKED_BREAD = StaticAisle(name="Freshly baked bread",  url="https://www.dia.es/panes-harinas-y-masas/pan-recien-horneado/c/L2070",
                                     original_file_uri=os.path.join(category_path(), "Freshly_baked_bread.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Freshly_baked_bread_detailed.json"))
    
    SLICED_BREAD_HOTDOGS_AND_HAMBURGERS = StaticAisle(name="Sliced bread, hotdogs and hamburgers", url="https://www.dia.es/panes-harinas-y-masas/pan-de-molde-perritos-y-hamburguesas/c/L2069",
                                     original_file_uri=os.path.join(category_path(), "Sliced_bread_hotdogs_and_hamburgers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sliced_bread_hotdogs_and_hamburgers_detailed.json"))
    
    PEAKS_AND_TOASTED_BREADS = StaticAisle(name="Peaks and toasted breads",  url="https://www.dia.es/panes-harinas-y-masas/picos-y-panes-tostados/c/L2071",
                                     original_file_uri=os.path.join(category_path(), "Peaks_and_toasted_breads.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Peaks_and_toasted_breads_detailed.json"))
    
    BREADCRUMBS = StaticAisle(name="Breadcrumbs",  url="https://www.dia.es/panes-harinas-y-masas/pan-rallado/c/L2072",
                                     original_file_uri=os.path.join(category_path(), "Breadcrumbs.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Breadcrumbs_detailed.json"))
    
    FLOURS_AND_YEASTS = StaticAisle(name="Flours and yeasts", url="https://www.dia.es/panes-harinas-y-masas/harinas-y-levaduras/c/L2075",
                                     original_file_uri=os.path.join(category_path(), "Flours_and_yeasts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Flours_and_yeasts_detailed.json"))
    
    DOUGHS_AND_PASTRIES = StaticAisle(name="Doughs and pastries",  url="https://www.dia.es/panes-harinas-y-masas/masas-y-hojaldres/c/L2076",
                                     original_file_uri=os.path.join(category_path(), "Doughs_and_pastries.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Doughs_and_pastries_detailed.json"))
    
    DESSERT_PREPARATIONS = StaticAisle(name="Dessert preparations",  url="https://www.dia.es/panes-harinas-y-masas/preparados-para-postres/c/L2077",
                                     original_file_uri=os.path.join(category_path(), "Dessert_preparations.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Dessert_preparations_detailed.json"))
    
    
    aisles: Final[List[StaticAisle]] = [FRESHLY_BAKED_BREAD, SLICED_BREAD_HOTDOGS_AND_HAMBURGERS, PEAKS_AND_TOASTED_BREADS, BREADCRUMBS, FLOURS_AND_YEASTS, DOUGHS_AND_PASTRIES, DESSERT_PREPARATIONS] 
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
                case "FRESHLY_BAKED_BREAD":
                    aisles = [cls.FRESHLY_BAKED_BREAD]
                case "SLICED_BREAD_HOTDOGS_AND_HAMBURGERS":
                    aisles = [cls.SLICED_BREAD_HOTDOGS_AND_HAMBURGERS]
                case "PEAKS_AND_TOASTED_BREADS":
                    aisles = [cls.PEAKS_AND_TOASTED_BREADS]
                case "BREADCRUMBS":
                    aisles = [cls.BREADCRUMBS]
                case "FLOURS_AND_YEASTS":
                    aisles = [cls.FLOURS_AND_YEASTS]
                case "DOUGHS_AND_PASTRIES":
                    aisles = [cls.DOUGHS_AND_PASTRIES]
                case "DESSERT_PREPARATIONS":
                    aisles = [cls.DESSERT_PREPARATIONS]
            
        return aisles
    
class DiaCoffeeCocoaAndInfusionsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Coffee_Cocoa_And_Infusions")

    COFFEE = StaticAisle(name="Coffee",  url="https://www.dia.es/cafe-cacao-e-infusiones/cafe/c/L2057",
                                     original_file_uri=os.path.join(category_path(), "Coffee.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Coffee_detailed.json"))
    
    COCOA = StaticAisle(name="Cocoa", url="https://www.dia.es/cafe-cacao-e-infusiones/cacao/c/L2058",
                                     original_file_uri=os.path.join(category_path(), "Cocoa.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cocoa_detailed.json"))
    
    TEA_AND_INFUSIONS = StaticAisle(name="Tea and infusions",  url="https://www.dia.es/cafe-cacao-e-infusiones/te-e-infusiones/c/L2059",
                                     original_file_uri=os.path.join(category_path(), "Tea_and_infusions.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tea_and_infusions_breads_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [COFFEE, COCOA, TEA_AND_INFUSIONS] 
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
                case "COFFEE":
                    aisles = [cls.COFFEE]
                case "COCOA":
                    aisles = [cls.COCOA]
                case "TEA_AND_INFUSIONS":
                    aisles = [cls.TEA_AND_INFUSIONS]
           
        return aisles
    
class DiaSugarChocolatesAndCandiesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Sugar_Chocolates_And_Candies")

    SUGAR_AND_SWEETENERS = StaticAisle(name="Sugar and sweeteners",  url="https://www.dia.es/azucar-chocolates-y-caramelos/azucar-y-edulcorantes/c/L2060",
                                     original_file_uri=os.path.join(category_path(), "Sugar_and_sweeteners.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sugar_and_sweeteners_detailed.json"))
    
    HONEY = StaticAisle(name="Honey", url="https://www.dia.es/azucar-chocolates-y-caramelos/miel/c/L2061",
                                     original_file_uri=os.path.join(category_path(), "Honey.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Honey_detailed.json"))
    
    JAMS_AND_FRUIT_IN_SYRUP = StaticAisle(name="Jams and fruit in syrup",  url="https://www.dia.es/azucar-chocolates-y-caramelos/mermeladas-y-frutas-en-almibar/c/L2062",
                                     original_file_uri=os.path.join(category_path(), "Jams_and_fruit_in_syrup.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Jams_and_fruit_in_syrup_detailed.json"))
    
    COCOA_CREAMS = StaticAisle(name="Cocoa creams",  url="https://www.dia.es/azucar-chocolates-y-caramelos/cremas-de-cacao/c/L2228",
                                     original_file_uri=os.path.join(category_path(), "Cocoa_creams.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cocoa_creams_detailed.json"))
    
    CHOCOLATES_AND_SWEETS = StaticAisle(name="Chocolates and sweets", url="https://www.dia.es/azucar-chocolates-y-caramelos/chocolates-y-bombones/c/L2063",
                                     original_file_uri=os.path.join(category_path(), "Chocolates_and_sweets.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chocolates_and_sweets_detailed.json"))
    
    SWEETS_CHEWING_GUM_AND_CANDIES = StaticAisle(name="Sweets, chewing gum and candies",  url="https://www.dia.es/azucar-chocolates-y-caramelos/caramelos-chicles-y-golosinas/c/L2064",
                                     original_file_uri=os.path.join(category_path(), "Sweets_chewing_gum_and_candies.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Sweets_chewing_gum_and_candies_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [SUGAR_AND_SWEETENERS, HONEY, JAMS_AND_FRUIT_IN_SYRUP, COCOA_CREAMS, CHOCOLATES_AND_SWEETS, SWEETS_CHEWING_GUM_AND_CANDIES] 
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
                case "HONEY":
                    aisles = [cls.HONEY]
                case "JAMS_AND_FRUIT_IN_SYRUP":
                    aisles = [cls.JAMS_AND_FRUIT_IN_SYRUP]
                case "COCOA_CREAMS":
                    aisles = [cls.COCOA_CREAMS]
                case "CHOCOLATES_AND_SWEETS":
                    aisles = [cls.CHOCOLATES_AND_SWEETS]
                case "SWEETS_CHEWING_GUM_AND_CANDIES":
                    aisles = [cls.SWEETS_CHEWING_GUM_AND_CANDIES]
           
        return aisles
    
class DiaBiscuitsBrunsAndCerealsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Biscuits_Bruns_And_Cereals")

    BISCUITS = StaticAisle(name="Biscuits",  url="https://www.dia.es/galletas-bollos-y-cereales/galletas/c/L2065",
                                     original_file_uri=os.path.join(category_path(), "Biscuits.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Biscuits_detailed.json"))
    
    PRETZELS = StaticAisle(name="Pretzels", url="https://www.dia.es/galletas-bollos-y-cereales/galletas-saladas/c/L2066",
                                     original_file_uri=os.path.join(category_path(), "Pretzels.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pretzels_detailed.json"))
    
    PASTRIES = StaticAisle(name="Pastries",  url="https://www.dia.es/galletas-bollos-y-cereales/bolleria/c/L2067",
                                     original_file_uri=os.path.join(category_path(), "Pastries.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pastries_detailed.json"))
    
    CEREALS = StaticAisle(name="Cereals",  url="https://www.dia.es/galletas-bollos-y-cereales/cereales/c/L2068",
                                     original_file_uri=os.path.join(category_path(), "Cereals.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cereals_detailed.json"))
    
    CAKES = StaticAisle(name="Cakes", url="https://www.dia.es/galletas-bollos-y-cereales/tortitas/c/L2216",
                                     original_file_uri=os.path.join(category_path(), "Cakes.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cakes_detailed.json"))
    
   
    
    aisles: Final[List[StaticAisle]] = [BISCUITS, PRETZELS, PASTRIES, CEREALS, CAKES] 
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
                case "BISCUITS":
                    aisles = [cls.BISCUITS]
                case "PRETZELS":
                    aisles = [cls.PRETZELS]
                case "PASTRIES":
                    aisles = [cls.PASTRIES]
                case "CEREALS":
                    aisles = [cls.CEREALS]
                case "CAKES":
                    aisles = [cls.CAKES]
                
           
        return aisles
    
class DiaChipsPicklesAndNutsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Chips_Pickles_And_Nuts")

    CHIPS_AND_SNACKS = StaticAisle(name="Chips and snacks",  url="https://www.dia.es/patatas-fritas-encurtidos-y-frutos-secos/patatas-fritas-y-aperitivos/c/L2098",
                                     original_file_uri=os.path.join(category_path(), "Chips_and_snacks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Chips_and_snacks_detailed.json"))
    
    OLIVES_AND_PICKLES = StaticAisle(name="Olives and pickles", url="https://www.dia.es/patatas-fritas-encurtidos-y-frutos-secos/aceitunas-y-encurtidos/c/L2096",
                                     original_file_uri=os.path.join(category_path(), "Olives_and_pickles.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Olives_and_pickles_detailed.json"))
    
    NUTS = StaticAisle(name="Nuts",  url="https://www.dia.es/patatas-fritas-encurtidos-y-frutos-secos/frutos-secos/c/L2097",
                                     original_file_uri=os.path.join(category_path(), "Nuts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Nuts_detailed.json"))
    
    
   
    
    aisles: Final[List[StaticAisle]] = [CHIPS_AND_SNACKS , OLIVES_AND_PICKLES, NUTS] 
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
                case "CHIPS_AND_SNACKS":
                    aisles = [cls.CHIPS_AND_SNACKS]
                case "OLIVES_AND_PICKLES":
                    aisles = [cls.OLIVES_AND_PICKLES]
                case "NUTS":
                    aisles = [cls.NUTS]
          
        return aisles
    
class DiaPizzasAndPreparedDishesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Pizzas_And_Prepared_Dishes")

    PIZZAS = StaticAisle(name="Pizzas",  url="https://www.dia.es/pizzas-y-platos-preparados/pizzas/c/L2101",
                                     original_file_uri=os.path.join(category_path(), "Pizzas.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pizzas_detailed.json"))
    
    PRECOOKED_PACKAGED_PRODUCTS = StaticAisle(name="Precooked packaged products", url="https://www.dia.es/pizzas-y-platos-preparados/precocinados-envasados/c/L2102",
                                     original_file_uri=os.path.join(category_path(), "Precooked_packaged_products.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Precooked_packaged_products_detailed.json"))
    
    INTERNATIONAL_CUISINE = StaticAisle(name="International cuisine",  url="https://www.dia.es/pizzas-y-platos-preparados/comida-internacional/c/L2103",
                                     original_file_uri=os.path.join(category_path(), "International_cuisine.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "International_cuisine_detailed.json"))
    
    TORTILLAS_AND_PIES = StaticAisle(name="Tortillas and pies", url="https://www.dia.es/pizzas-y-platos-preparados/tortillas-y-empanadas/c/L2105",
                                     original_file_uri=os.path.join(category_path(), "Tortillas_and_pies.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tortillas_and_pies_detailed.json"))
    
    GAZPACHOS_AND_SALMOREJOS = StaticAisle(name="Gazpachos and salmorejos",  url="https://www.dia.es/pizzas-y-platos-preparados/gazpachos-y-salmorejos/c/L2106",
                                     original_file_uri=os.path.join(category_path(), "Gazpachos_and_salmorejos.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Gazpachos_and_salmorejos_detailed.json"))
                                    
    
    aisles: Final[List[StaticAisle]] = [PIZZAS, PRECOOKED_PACKAGED_PRODUCTS, INTERNATIONAL_CUISINE, TORTILLAS_AND_PIES, GAZPACHOS_AND_SALMOREJOS] 
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
                case "PIZZAS":
                    aisles = [cls.PIZZAS]
                case "PRECOOKED_PACKAGED_PRODUCTS":
                    aisles = [cls.OLIVES_AND_PICKLES]
                case "INTERNATIONAL_CUISINE":
                    aisles = [cls.INTERNATIONAL_CUISINE]
                case "TORTILLAS_AND_PIES":
                    aisles = [cls.TORTILLAS_AND_PIES]
                case "GAZPACHOS_AND_SALMOREJOS":
                    aisles = [cls.GAZPACHOS_AND_SALMOREJOS]
          
        return aisles
    
class DiaFrozenFoodAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Frozen_Food")

    ICE_CREAMS_AND_ICE = StaticAisle(name="Ice creams and ice",  url="https://www.dia.es/congelados/helados-y-hielo/c/L2130",
                                     original_file_uri=os.path.join(category_path(), "Ice_creams_and_ice.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Ice_creams_and_ice_detailed.json"))
    
    PIZZAS_BASES_AND_DOUGHS = StaticAisle(name="Pizzas, bases and doughs", url="https://www.dia.es/congelados/pizzas-bases-y-masas/c/L2131",
                                     original_file_uri=os.path.join(category_path(), "Pizzas_bases_and_doughs.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pizzas_bases_and_doughs_detailed.json"))
    
    FISH_AND_SEAFOOD = StaticAisle(name="Fish and seafood",  url="https://www.dia.es/congelados/pescado-y-marisco/c/L2132",
                                     original_file_uri=os.path.join(category_path(), "Fish_and_seafood.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Fish_and_seafood_detailed.json"))
    
    MEAT_AND_CHICKEN = StaticAisle(name="Meat and chicken", url="https://www.dia.es/congelados/carne-y-pollo/c/L2133",
                                     original_file_uri=os.path.join(category_path(), "Meat_and_chicken.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Meat_and_chicken_detailed.json"))
    
    VEGETABLES_AND_STIR_FRIES = StaticAisle(name="Vegetables and stir-fries",  url="https://www.dia.es/congelados/verduras-hortalizas-y-salteados/c/L2210",
                                     original_file_uri=os.path.join(category_path(), "Vegetables_and_stir_fries.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vegetables_and_stir_fries_detailed.json"))
    
    FRENCH_FRIES = StaticAisle(name="French fries", url="https://www.dia.es/congelados/patatas-fritas/c/L2213",
                                     original_file_uri=os.path.join(category_path(), "French_fries.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "French_fries_detailed.json"))
    
    CROQUETTES_AND_BATTERS = StaticAisle(name="Croquettes and batters",  url="https://www.dia.es/congelados/croquetas-y-rebozados/c/L2135",
                                     original_file_uri=os.path.join(category_path(), "Croquettes_and_batters.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Croquettes_and_batters_detailed.json"))
    
    CHURROS_AND_DESSERTS = StaticAisle(name="Churros and desserts", url="https://www.dia.es/congelados/churros-y-postres/c/L2136",
                                     original_file_uri=os.path.join(category_path(), "Churros_and_desserts.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Churros_and_desserts_detailed.json"))
    
    LASAGNE_AND_PASTA = StaticAisle(name="Lasagne and pasta",  url="https://www.dia.es/congelados/lasanas-y-pasta/c/L2137",
                                     original_file_uri=os.path.join(category_path(), "Lasagne_and_pasta.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Lasagne_and_pasta_detailed.json"))
                                    
    
    aisles: Final[List[StaticAisle]] = [ICE_CREAMS_AND_ICE , PIZZAS_BASES_AND_DOUGHS, FISH_AND_SEAFOOD, MEAT_AND_CHICKEN, VEGETABLES_AND_STIR_FRIES, FRENCH_FRIES, CROQUETTES_AND_BATTERS, CHURROS_AND_DESSERTS, LASAGNE_AND_PASTA] 
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
                case "ICE_CREAMS_AND_ICE":
                    aisles = [cls.ICE_CREAMS_AND_ICE]
                case "PIZZAS_BASES_AND_DOUGHS":
                    aisles = [cls.PIZZAS_BASES_AND_DOUGHS]
                case "FISH_AND_SEAFOOD":
                    aisles = [cls.FISH_AND_SEAFOOD]
                case "MEAT_AND_CHICKEN":
                    aisles = [cls.MEAT_AND_CHICKEN]
                case "VEGETABLES_AND_STIR_FRIES":
                    aisles = [cls.VEGETABLES_AND_STIR_FRIES]
                case "FRENCH_FRIES":
                    aisles = [cls.FRENCH_FRIES]
                case "CROQUETTES_AND_BATTERS":
                    aisles = [cls.CROQUETTES_AND_BATTERS]
                case "CHURROS_AND_DESSERTS":
                    aisles = [cls.CHURROS_AND_DESSERTS]
                case "LASAGNE_AND_PASTA":
                    aisles = [cls.LASAGNE_AND_PASTA]
          
        return aisles
    
class DiaWaterSoftDrinksAndJuicesAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Water_Soft_Drinks_And_Juices")

    WATER = StaticAisle(name="Water",  url="https://www.dia.es/agua-refrescos-y-zumos/agua/c/L2107",
                                     original_file_uri=os.path.join(category_path(), "Water.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Water_detailed.json"))
    
    COLA = StaticAisle(name="Cola", url="https://www.dia.es/agua-refrescos-y-zumos/cola/c/L2108",
                                     original_file_uri=os.path.join(category_path(), "Cola.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cola_detailed.json"))
    
    ORANGES = StaticAisle(name="Oranges",  url="https://www.dia.es/agua-refrescos-y-zumos/naranja/c/L2212",
                                     original_file_uri=os.path.join(category_path(), "Oranges.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Oranges_detailed.json"))
    
    LEMON_LEMON_LIME = StaticAisle(name="Lemon, lemon lime", url="https://www.dia.es/agua-refrescos-y-zumos/limon-lima-limon/c/L2109",
                                     original_file_uri=os.path.join(category_path(), "Lemon_lemon_lime.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Lemon_lemon_lime_detailed.json"))
    
    COLD_TEAS_ICED_COFFEES = StaticAisle(name="Cold teas, iced coffees",  url="https://www.dia.es/agua-refrescos-y-zumos/tes-frios-cafes-frios/c/L2111",
                                     original_file_uri=os.path.join(category_path(), "Cold_teas_iced_coffees.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cold_teas_iced_coffees_detailed.json"))
    
    TÓNICAS = StaticAisle(name="Tónicas", url="https://www.dia.es/agua-refrescos-y-zumos/tonicas/c/L2112",
                                     original_file_uri=os.path.join(category_path(), "Tónicas.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Tónicas_detailed.json"))
    
    SODA = StaticAisle(name="Soda",  url="https://www.dia.es/agua-refrescos-y-zumos/gaseosa/c/L2192",
                                     original_file_uri=os.path.join(category_path(), "Soda.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Soda_detailed.json"))
    
    ENERGY_DRINKS = StaticAisle(name="Energy drinks", url="https://www.dia.es/agua-refrescos-y-zumos/bebidas-energeticas/c/L2217",
                                     original_file_uri=os.path.join(category_path(), "Energy_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Energy_drinks_detailed.json"))
    
    ISOTONIC_DRINKS = StaticAisle(name="Isotonic drinks",  url="https://www.dia.es/agua-refrescos-y-zumos/bebidas-isotonicas/c/L2114",
                                     original_file_uri=os.path.join(category_path(), "Isotonic_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Isotonic_drinks_detailed.json"))
                                    
    JUICES = StaticAisle(name="Juices", url="https://www.dia.es/agua-refrescos-y-zumos/zumos/c/L2113",
                                     original_file_uri=os.path.join(category_path(), "Juices.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Juices_detailed.json"))
    
    OTHER_DRINKS = StaticAisle(name="Other drinks",  url="https://www.dia.es/agua-refrescos-y-zumos/otras-bebidas/c/L2110",
                                     original_file_uri=os.path.join(category_path(), "Other_drinks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_drinks_detailed.json"))
                                    
    
    aisles: Final[List[StaticAisle]] = [WATER, COLA, ORANGES, LEMON_LEMON_LIME, COLD_TEAS_ICED_COFFEES, TÓNICAS, SODA, ENERGY_DRINKS, ISOTONIC_DRINKS, JUICES, OTHER_DRINKS] 
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
                case "COLA":
                    aisles = [cls.COLA]
                case "ORANGES":
                    aisles = [cls.ORANGES]
                case "LEMON_LEMON_LIME":
                    aisles = [cls.LEMON_LEMON_LIME]
                case "COLD_TEAS_ICED_COFFEES":
                    aisles = [cls.COLD_TEAS_ICED_COFFEES]
                case "TÓNICAS":
                    aisles = [cls.TÓNICAS]
                case "SODA":
                    aisles = [cls.SODA]
                case "ENERGY_DRINKS":
                    aisles = [cls.ENERGY_DRINKS]
                case "ISOTONIC_DRINKS":
                    aisles = [cls.ISOTONIC_DRINKS]
                case "JUICES":
                    aisles = [cls.JUICES]
                case "OTHER_DRINKS":
                    aisles = [cls.OTHER_DRINKS]
          
        return aisles
    
class DiaBeersWinesAndSpiritsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Beers_Wines_And_Spirits")

    BEERS = StaticAisle(name="Beers",  url="https://www.dia.es/cervezas-vinos-y-bebidas-con-alcohol/cervezas/c/L2115",
                                     original_file_uri=os.path.join(category_path(), "Beers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Beers_detailed.json"))
    
    SPECIAL_BEERS = StaticAisle(name="Special beers", url="https://www.dia.es/cervezas-vinos-y-bebidas-con-alcohol/cervezas-especiales/c/L2117",
                                     original_file_uri=os.path.join(category_path(), "Special_beers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Special_beers_detailed.json"))
    
    BEERS_WITH_LEMON = StaticAisle(name="Beers with lemon",  url="https://www.dia.es/cervezas-vinos-y-bebidas-con-alcohol/cervezas-con-limon/c/L2182",
                                     original_file_uri=os.path.join(category_path(), "Beers_with_lemon.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Beers_with_lemon_detailed.json"))
    
    NON_ALCOHOLIC_BEERS = StaticAisle(name="Non-alcoholic beers", url="https://www.dia.es/cervezas-vinos-y-bebidas-con-alcohol/cervezas-sin-alcohol/c/L2118",
                                     original_file_uri=os.path.join(category_path(), "Non_alcoholic_beers.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Non_alcoholic_beers_detailed.json"))
    
    SUMMER_RED_WINE_AND_SANGRIA = StaticAisle(name="Summer red wine and sangria",  url="https://www.dia.es/cervezas-vinos-y-bebidas-con-alcohol/tinto-de-verano-y-sangria/c/L2119",
                                     original_file_uri=os.path.join(category_path(), "Summer_red_wine_and_sangria.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Summer_red_wine_and_sangria_detailed.json"))
    
    RED_WINE = StaticAisle(name="Red wine", url="https://www.dia.es/cervezas-vinos-y-bebidas-con-alcohol/vino-tinto/c/L2120",
                                     original_file_uri=os.path.join(category_path(), "Red_wine.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Red_wine_detailed.json"))
    
    WHITE_WINE = StaticAisle(name="White wine",  url="https://www.dia.es/cervezas-vinos-y-bebidas-con-alcohol/vino-blanco/c/L2121",
                                     original_file_uri=os.path.join(category_path(), "White_wine.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "White_wine_detailed.json"))
    
    CAVAS_AND_CIDER = StaticAisle(name="Cavas and cider", url="https://www.dia.es/cervezas-vinos-y-bebidas-con-alcohol/cavas-y-sidra/c/L2122",
                                     original_file_uri=os.path.join(category_path(), "Cavas_and_cider.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cavas_and_cider_detailed.json"))
    
    ROSE_WINE = StaticAisle(name="Rose wine",  url="https://www.dia.es/cervezas-vinos-y-bebidas-con-alcohol/vino-rosado/c/L2124",
                                     original_file_uri=os.path.join(category_path(), "Rose_wine.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Rose_wine_detailed.json"))
                                    
    GIN_AND_VODKA = StaticAisle(name="Gin and vodka", url="https://www.dia.es/cervezas-vinos-y-bebidas-con-alcohol/ginebra-y-vodka/c/L2125",
                                     original_file_uri=os.path.join(category_path(), "Gin_and_vodka.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Gin_and_vodka_detailed.json"))
    
    RON_AND_WHISKY = StaticAisle(name="Ron and whisky",  url="https://www.dia.es/cervezas-vinos-y-bebidas-con-alcohol/ron-y-whisky/c/L2128",
                                     original_file_uri=os.path.join(category_path(), "Ron_and_whisky.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Ron_and_whisky_detailed.json"))
    
    VERMOUTH = StaticAisle(name="Vermouth",  url="https://www.dia.es/cervezas-vinos-y-bebidas-con-alcohol/vermouth/c/L2127",
                                     original_file_uri=os.path.join(category_path(), "Vermouth.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Vermouth_detailed.json"))
                                    
    CREAMS_AND_LIQUEURS = StaticAisle(name="Creams and liqueurs", url="https://www.dia.es/cervezas-vinos-y-bebidas-con-alcohol/cremas-y-licores/c/L2129",
                                     original_file_uri=os.path.join(category_path(), "Creams_and_liqueurs.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Creams_and_liqueurs_detailed.json"))
    
    BRANDY = StaticAisle(name="Brandy",  url="https://www.dia.es/cervezas-vinos-y-bebidas-con-alcohol/brandy/c/L2126",
                                     original_file_uri=os.path.join(category_path(), "Brandy.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Brandy_detailed.json"))
                                    
    
    aisles: Final[List[StaticAisle]] = [BEERS, SPECIAL_BEERS, BEERS_WITH_LEMON, NON_ALCOHOLIC_BEERS, SUMMER_RED_WINE_AND_SANGRIA, RED_WINE, WHITE_WINE, CAVAS_AND_CIDER, ROSE_WINE, GIN_AND_VODKA, RON_AND_WHISKY, VERMOUTH, CREAMS_AND_LIQUEURS, BRANDY] 
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
                case "BEERS":
                    aisles = [cls.BEERS]
                case "SPECIAL_BEERS":
                    aisles = [cls.SPECIAL_BEERS]
                case "BEERS_WITH_LEMON":
                    aisles = [cls.BEERS_WITH_LEMON]
                case "NON_ALCOHOLIC_BEERS":
                    aisles = [cls.NON_ALCOHOLIC_BEERS]
                case "SUMMER_RED_WINE_AND_SANGRIA":
                    aisles = [cls.SUMMER_RED_WINE_AND_SANGRIA]
                case "RED_WINE":
                    aisles = [cls.RED_WINE]
                case "WHITE_WINE":
                    aisles = [cls.WHITE_WINE]
                case "CAVAS_AND_CIDER":
                    aisles = [cls.CAVAS_AND_CIDER]
                case "ROSE_WINE":
                    aisles = [cls.ROSE_WINE]
                case "GIN_AND_VODKA":
                    aisles = [cls.GIN_AND_VODKA]
                case "RON_AND_WHISKY":
                    aisles = [cls.RON_AND_WHISKY]
                case "VERMOUTH":
                    aisles = [cls.VERMOUTH]
                case "CREAMS_AND_LIQUEURS":
                    aisles = [cls.CREAMS_AND_LIQUEURS]
                case "BRANDY":
                    aisles = [cls.BRANDY]
          
        return aisles
    
class DiaBabyAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Baby")

    PAP = StaticAisle(name="Pap",  url="https://www.dia.es/bebe/papilla/c/L2138",
                                     original_file_uri=os.path.join(category_path(), "Pap.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Pap_detailed.json"))
    
    INFANT_MILK = StaticAisle(name="Infant milk", url="https://www.dia.es/bebe/leche-infantil/c/L2139",
                                     original_file_uri=os.path.join(category_path(), "Infant_milk.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Infant_milk_detailed.json"))
    
    BABY_FOODS_AND_JARS = StaticAisle(name="Baby foods and jars",  url="https://www.dia.es/bebe/potitos-y-tarritos/c/L2141",
                                     original_file_uri=os.path.join(category_path(), "Baby_foods_and_jars.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Baby_foods_and_jars_detailed.json"))
    
    YOGURTS_FRUIT_BAGS_AND_SNACKS = StaticAisle(name="Yogurts, fruit bags and snacks", url="https://www.dia.es/bebe/yogures-bolsitas-de-frutas-y-snacks/c/L2140",
                                     original_file_uri=os.path.join(category_path(), "Yogurts_fruit_bags_and_snacks.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Yogurts_fruit_bags_and_snacks_detailed.json"))
  

    aisles: Final[List[StaticAisle]] = [PAP, INFANT_MILK, BABY_FOODS_AND_JARS, YOGURTS_FRUIT_BAGS_AND_SNACKS]
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
                case "PAP":
                    aisles = [cls.PAP]
                case "INFANT_MILK":
                    aisles = [cls.INFANT_MILK]
                case "BABY_FOODS_AND_JARS":
                    aisles = [cls.BABY_FOODS_AND_JARS]
                case "YOGURTS_FRUIT_BAGS_AND_SNACKS":
                    aisles = [cls.YOGURTS_FRUIT_BAGS_AND_SNACKS]
      
        return aisles
    
class DiaPetsAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "Pets")

    DOGS = StaticAisle(name="Dogs",  url="https://www.dia.es/mascotas/perros/c/L2174",
                                     original_file_uri=os.path.join(category_path(), "Dogs.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Dogs_detailed.json"))
    
    CATS = StaticAisle(name="Cats", url="https://www.dia.es/mascotas/gatos/c/L2175",
                                     original_file_uri=os.path.join(category_path(), "Cats.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Cats_detailed.json"))
    
    OTHER_ANIMALS = StaticAisle(name="Other animals",  url="https://www.dia.es/mascotas/otros-animales/c/L2176",
                                     original_file_uri=os.path.join(category_path(), "Other_animals.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "Other_animals_detailed.json"))
    
    aisles: Final[List[StaticAisle]] = [DOGS, CATS, OTHER_ANIMALS] 
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
                case "DOGS":
                    aisles = [cls.DOGS]
                case "CATS":
                    aisles = [cls.CATS]
                case "OTHER_ANIMALS":
                    aisles = [cls.OTHER_ANIMALS]

        return aisles
    
Dia_categories_with_uris: Final[list[StaticCategory]] = [
    StaticCategory(name="Air Fryer - Airfryer", url="https://www.dia.es/freidora-de-aire-airfryer/c/L125", aisles=DiaAirFryerAlimentations.aisles),
    
    StaticCategory(name="Charcuterie and cheeses", url="https://www.dia.es/charcuteria-y-quesos/c/L101", aisles=DiaCharcuterieAndCheesesAlimentations.aisles),
    
    StaticCategory(name="Butchery", url="https://www.dia.es/carniceria/c/L102", aisles=DiaButcheryAlimentations.aisles),
    
    StaticCategory(name="Fish smoked fish and seafood", url="https://www.dia.es/pescados-mariscos-y-ahumados/c/L103", aisles=DiaFishSmockedFishAndSeafoodAlimentations.aisles),
    
    StaticCategory(name="Vegetables", url="https://www.dia.es/verduras/c/L104", aisles=DiaVegetablesAlimentations.aisles),
    
    StaticCategory(name="Fruits", url="https://www.dia.es/frutas/c/L105", aisles=DiaFruitsAlimentations.aisles),
    
    StaticCategory(name="Milk eggs and butter", url="https://www.dia.es/leche-huevos-y-mantequilla/c/L108", aisles=DiaMilkEggsAndButterAlimentations.aisles),
    
    StaticCategory(name="Yoghurts and desserts", url="https://www.dia.es/yogures-y-postres/c/L113", aisles=DiaYoghurtsAndDessertsAlimentations.aisles),
    
    StaticCategory(name="Rice pasta and pulses", url="https://www.dia.es/arroz-pastas-y-legumbres/c/L106", aisles=DiaRicePastaAndPulsesAlimentations.aisles),
    
    StaticCategory(name="Oils sauces and spices", url="https://www.dia.es/aceites-salsas-y-especias/c/L107", aisles=DiaOilSaucesAndSpicesAlimentations.aisles),
    
    StaticCategory(name="Canned food, broths and creams", url="https://www.dia.es/conservas-caldos-y-cremas/c/L114", aisles=DiaCannedFoodBrothsAndCreamsAlimentations.aisles),
    
    StaticCategory(name="Breads flours and doughs", url="https://www.dia.es/panes-harinas-y-masas/c/L112", aisles=DiaBreadsFloursAndDoughsAlimentations.aisles),
    
    StaticCategory(name="Coffee, cocoa and infusions", url="https://www.dia.es/cafe-cacao-e-infusiones/c/L109", aisles=DiaCoffeeCocoaAndInfusionsAlimentations.aisles),
    
    StaticCategory(name="Sugar chocolates and candies", url="https://www.dia.es/azucar-chocolates-y-caramelos/c/L110", aisles=DiaSugarChocolatesAndCandiesAlimentations.aisles),
    
    StaticCategory(name="Biscuits buns and cereals", url="https://www.dia.es/galletas-bollos-y-cereales/c/L111", aisles=DiaBiscuitsBrunsAndCerealsAlimentations.aisles),
    
    StaticCategory(name="Chips pickles and nuts", url="https://www.dia.es/patatas-fritas-encurtidos-y-frutos-secos/c/L115", aisles=DiaChipsPicklesAndNutsAlimentations.aisles),
    
    StaticCategory(name="Pizzas and prepared dishes", url="https://www.dia.es/pizzas-y-platos-preparados/c/L116", aisles=DiaPizzasAndPreparedDishesAlimentations.aisles),
    
    StaticCategory(name="Frozen food", url="https://www.dia.es/congelados/c/L119", aisles=DiaFrozenFoodAlimentations.aisles),
    
    StaticCategory(name="Water soft drinks and juices", url="https://www.dia.es/agua-refrescos-y-zumos/c/L117", aisles=DiaWaterSoftDrinksAndJuicesAlimentations.aisles),
    
    StaticCategory(name="Beers wines and spirits", url="https://www.dia.es/cervezas-vinos-y-bebidas-con-alcohol/c/L118", aisles=DiaBeersWinesAndSpiritsAlimentations.aisles),
        
    StaticCategory(name="Baby", url="https://www.dia.es/bebe/c/L120", aisles=DiaBabyAlimentations.aisles),
    
    StaticCategory(name="Pets", url="https://www.dia.es/mascotas/c/L123", aisles=DiaPetsAlimentations.aisles)
   
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
        for category in Dia_categories_with_uris:
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
                case "DiaAirFryerAlimentations":
                    aisles = DiaAirFryerAlimentations.get_aisles(cmdargs[1])
                case "DiaCharcuterieAndCheesesAlimentations":
                    aisles = DiaCharcuterieAndCheesesAlimentations.get_aisles(cmdargs[1])
                case "DiaButcheryAlimentations":
                    aisles = DiaButcheryAlimentations.get_aisles(cmdargs[1])
                case "DiaFishSmockedFishAndSeafoodAlimentations":
                    aisles = DiaFishSmockedFishAndSeafoodAlimentations.get_aisles(cmdargs[1])
                case "DiaVegetablesAlimentations":
                    aisles = DiaVegetablesAlimentations.get_aisles(cmdargs[1])
                case "DiaFruitsAlimentations":
                    aisles = DiaFruitsAlimentations.get_aisles(cmdargs[1])
                case "DiaMilkEggsAndButterAlimentations":
                    aisles = DiaMilkEggsAndButterAlimentations.get_aisles(cmdargs[1])
                case "DiaYoghurtsAndDessertsAlimentations":
                    aisles = DiaYoghurtsAndDessertsAlimentations.get_aisles(cmdargs[1])
                case "DiaRicePastaAndPulsesAlimentations":
                    aisles = DiaRicePastaAndPulsesAlimentations.get_aisles(cmdargs[1])
                case "DiaOilSaucesAndSpicesAlimentations":
                    aisles = DiaOilSaucesAndSpicesAlimentations.get_aisles(cmdargs[1])
                case "DiaCannedFoodBrothsAndCreamsAlimentations":
                    aisles = DiaCannedFoodBrothsAndCreamsAlimentations.get_aisles(cmdargs[1])
                case "DiaBreadsFloursAndDoughsAlimentations":
                    aisles = DiaBreadsFloursAndDoughsAlimentations.get_aisles(cmdargs[1])
                case "DiaCoffee_Cocoa_And_Infusions_Alimentations":
                    aisles = DiaCoffeeCocoaAndInfusionsAlimentations.get_aisles(cmdargs[1])
                case "DiaSugarChocolatesAndCandiesAlimentations":
                    aisles = DiaSugarChocolatesAndCandiesAlimentations.get_aisles(cmdargs[1])
                case "DiaBiscuitsBrunsAndCerealsAlimentations":
                    aisles = DiaBiscuitsBrunsAndCerealsAlimentations.get_aisles(cmdargs[1])
                case "DiaChipsPicklesAndNutsAlimentations":
                    aisles = DiaChipsPicklesAndNutsAlimentations.get_aisles(cmdargs[1])
                case "DiaPizzasAndPreparedDishesAlimentations":
                    aisles = DiaPizzasAndPreparedDishesAlimentations.get_aisles(cmdargs[1])
                case "DiaFrozenFoodAlimentations":
                    aisles = DiaFrozenFoodAlimentations.get_aisles(cmdargs[1])
                case "DiaWaterSoftDrinksAndJuicesAlimentations":
                    aisles = DiaWaterSoftDrinksAndJuicesAlimentations.get_aisles(cmdargs[1])
                case "DiaBeersWinesAndSpiritsAlimentations":
                    aisles = DiaBeersWinesAndSpiritsAlimentations.get_aisles(cmdargs[1])
                case "DiaBabyAlimentations":
                    aisles = DiaBabyAlimentations.get_aisles(cmdargs[1])
                case "DiaPetsAlimentations":
                    aisles = DiaPetsAlimentations.get_aisles(cmdargs[1])
                case _:
                    logging.error(f"args source not found: {cmdargs[1]}")
                    sys.exit()

    return aisles
