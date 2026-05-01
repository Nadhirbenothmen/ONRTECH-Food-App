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

class CarrefourBebeAlimentations(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "bebe")

    BEBE_ALIMENTATIONS = StaticAisle(name="Alimentation", aisle_id="36922", url="https://www.carrefour.fr/r/bebe/alimentation",
                                     original_file_uri=os.path.join(category_path(), "bebe_alimentations.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "bebe_alimentations_detailed.json"))
    # 3 résultats
    BOISSONS = StaticAisle(name="Boissons", aisle_id="36922", url="https://www.carrefour.fr/r/bebe/alimentation/boissons",
                           original_file_uri=os.path.join(category_path(), "boissons.json"),
                           mini_file_detailed_uri=os.path.join(category_path(), "boissons_detailed.json"))
    # 43 résultats
    CEREALES = StaticAisle(name="cereales", aisle_id="36922", url="https://www.carrefour.fr/r/bebe/alimentation/cereales",
                           original_file_uri=os.path.join(category_path(), "cereales.json"),
                           mini_file_detailed_uri=os.path.join(category_path(), "cereales_detailed.json"))

    # 207 résultats
    DESSERTS = StaticAisle(name="Desserts", aisle_id="36922", url="https://www.carrefour.fr/r/bebe/alimentation/desserts",
                           original_file_uri=os.path.join(category_path(), "desserts.json"),
                           mini_file_detailed_uri=os.path.join(category_path(), "desserts_detailed.json"))

    # 127 résultats
    LAITS_INFANTILES = StaticAisle(name="Laits infantiles", aisle_id="36922", url="https://www.carrefour.fr/r/bebe/alimentation/laits-infantiles",
                                   original_file_uri=os.path.join(category_path(), "laits_infantiles.json"),
                                   mini_file_detailed_uri=os.path.join(category_path(), "laits_infantiles_detailed.json"))
    # 335 résultats
    PLATS = StaticAisle(name="plats", aisle_id="36922", url="https://www.carrefour.fr/r/bebe/alimentation/plats-bebe",
                        original_file_uri=os.path.join(category_path(), "plats.json"),
                        mini_file_detailed_uri=os.path.join(category_path(), "plats_detailed.json"))

    aisles: Final[List[StaticAisle]] = [BOISSONS, CEREALES, LAITS_INFANTILES, DESSERTS, PLATS]

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
                case "BEBE_ALIMENTATIONS":
                    aisles = [cls.BEBE_ALIMENTATIONS]
                case "LAITS_INFANTILES":
                    aisles = [cls.LAITS_INFANTILES]
                case "CEREALES":
                    aisles = [cls.CEREALES]
                case "PLATS":
                    aisles = [cls.PLATS]
                case "DESSERTS":
                    aisles = [cls.DESSERTS]
                case "BOISSONS":
                    aisles = [cls.BOISSONS]
        return aisles

class CarrefourBioEcologie(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "bio_ecologie")
    # 256 résultats
    BEBE = StaticAisle(name="Bébé", url="https://www.carrefour.fr/r/bio-et-ecologie/bebe",
                       original_file_uri=os.path.join(category_path(), "bebe.json"),
                       mini_file_detailed_uri=os.path.join(category_path(), "bebe_detailed.json"))

    # 484 résultats
    BIO_PETIT_PRIX = StaticAisle(name="Bio à Petit prix", url="https://www.carrefour.fr/r/bio-et-ecologie/bio-petit-prix",
                                 original_file_uri=os.path.join(category_path(), "bio_petit_prix.json"),
                                 mini_file_detailed_uri=os.path.join(category_path(), "bio_petit_prix_detailed.json"))
    # 1747 résultats
    BOISSONS = StaticAisle(name="Boissons", url="https://www.carrefour.fr/r/bio-et-ecologie/boissons",
                           original_file_uri=os.path.join(category_path(), "boissons.json"),
                           mini_file_detailed_uri=os.path.join(category_path(), "boissons_detailed.json"))

    # 293 résultats
    CREMERIE = StaticAisle(name="Crèmerie", url="https://www.carrefour.fr/r/bio-et-ecologie/cremerie",
                           original_file_uri=os.path.join(category_path(), "cremerie.json"),
                           mini_file_detailed_uri=os.path.join(category_path(), "cremerie_detailed.json"))

    # 1379 résultats
    EPICERIE_SUCREE = StaticAisle(name="Epicerie sucrée", url="https://www.carrefour.fr/r/bio-et-ecologie/epicerie-sucree",
                                  original_file_uri=os.path.join(category_path(), "epicerie_sucree.json"),
                                  mini_file_detailed_uri=os.path.join(category_path(), "epicerie_sucree_detailed.json"))

    # 226 résultats
    FRAIS_SURGELES = StaticAisle(name="Frais et Surgelés", url="https://www.carrefour.fr/r/bio-et-ecologie/frais-et-surgeles",
                                 original_file_uri=os.path.join(category_path(), "frais_surgeles.json"),
                                 mini_file_detailed_uri=os.path.join(category_path(), "frais_surgeles_detailed.json"))

    # 559 résultats
    MARCHE = StaticAisle(name="Le Marché", url="https://www.carrefour.fr/r/bio-et-ecologie/le-marche",
                         original_file_uri=os.path.join(category_path(), "marche.json"),
                         mini_file_detailed_uri=os.path.join(category_path(), "marche_detailed.json"))

    aisles: Final[List[StaticAisle]] = [FRAIS_SURGELES, BEBE, CREMERIE, BIO_PETIT_PRIX, MARCHE, EPICERIE_SUCREE, BOISSONS]

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
                case "BIO_PETIT_PRIX":
                    aisles = [cls.BIO_PETIT_PRIX]
                case "MARCHE":
                    aisles = [cls.MARCHE]
                case "CREMERIE":
                    aisles = [cls.CREMERIE]
                case "FRAIS_SURGELES":
                    aisles = [cls.FRAIS_SURGELES]
                case "BEBE":
                    aisles = [cls.BEBE]
                case "EPICERIE_SUCREE":
                    aisles = [cls.EPICERIE_SUCREE]
                case "BOISSONS":
                    aisles = [cls.BOISSONS]
        return aisles

class CarrefourBoissons(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "boissons")

    # products 220
    BOISSONS_VEGETALES = StaticAisle(name="Boissons végétales", url="https://www.carrefour.fr/r/dietetique-preferences-alimentaires/vegetal/boissons-vegetales",
                                     original_file_uri=os.path.join(category_path(), "boissons_vegetales.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "boissons_vegetales_detailed.json"))
    # products 772
    COLAS_THES_GLACES_SOFT_DRINKS = StaticAisle(name="Colas, Thés glacés, Sirops et Sodas", url="https://www.carrefour.fr/r/boissons/colas-thes-glaces-et-soft-drinks",
                                             original_file_uri=os.path.join(category_path(), "colas_thes_glaces_soft_drinks.json"),
                                             mini_file_detailed_uri=os.path.join(category_path(), "colas_thes_glaces_soft_drinks_detailed.json"))
    # products 228
    EAUX = StaticAisle(name="Eaux", url="https://www.carrefour.fr/r/boissons/eaux",
                       original_file_uri=os.path.join(category_path(), "eaux.json"),
                       mini_file_detailed_uri=os.path.join(category_path(), "eaux_detailed.json"))
    # products 478
    JUS_FRUIT_LEGUME = StaticAisle(name="jus fruits légumes", url="https://www.carrefour.fr/r/boissons/jus-fruits-legumes",
                                   original_file_uri=os.path.join(category_path(), "jus_fruits_legumes.json"),
                                   mini_file_detailed_uri=os.path.join(category_path(), "jus_fruits_legumes_detailed.json"))
    aisles: Final[List[StaticAisle]] = [BOISSONS_VEGETALES, EAUX, JUS_FRUIT_LEGUME, COLAS_THES_GLACES_SOFT_DRINKS]

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
                case "aisles_part1":
                    aisles = [cls.BOISSONS_VEGETALES,
                              cls.COLAS_THES_GLACES_SOFT_DRINKS]
                case "aisles_part2":
                    aisles = [cls.EAUX]
                case "BOISSONS_VEGETALES":
                    aisles = [cls.BOISSONS_VEGETALES]
                case "COLAS_THES_GLACES_SOFT_DRINKS":
                    aisles = [cls.COLAS_THES_GLACES_SOFT_DRINKS]
                case "EAUX":
                    aisles = [cls.EAUX]
                case "JUS_FRUIT_LEGUME":
                    aisles = [cls.JUS_FRUIT_LEGUME]
        return aisles

class CarrefourCharcuterieTraiteur(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "charcuterie_traiteur")

    # 278 résultats
    APERITIFS = StaticAisle(name="Apéritifs", url="https://www.carrefour.fr/r/charcuterie-traiteur/aperitifs",
                            original_file_uri=os.path.join(category_path(), "aperitifs.json"),
                            mini_file_detailed_uri=os.path.join(category_path(), "aperitifs_detailed.json"))

    # 1830
    CHARCUTERIE = StaticAisle(name="Charcuterie", url="https://www.carrefour.fr/r/charcuterie-traiteur/charcuterie",
                              original_file_uri=os.path.join(category_path(), "charcuterie.json"),
                              mini_file_detailed_uri=os.path.join(category_path(), "charcuterie_detailed.json"))
    # 228 résultats
    COUPE_CHARCUTERIE = StaticAisle(name="Charcuterie à la coupe", url="https://www.carrefour.fr/r/charcuterie-traiteur/charcuterie-coupe",
                                         original_file_uri=os.path.join(category_path(), "coupe_charcuterie.json"),
                                         mini_file_detailed_uri=os.path.join(category_path(), "coupe_charcuterie_detailed.json"))
    # 370 résultats
    ENTREES_SALADES = StaticAisle(name="Entrées et Salades", url="https://www.carrefour.fr/r/charcuterie-traiteur/entrees-salades",
                                  original_file_uri=os.path.join(category_path(), "entrees_salades.json"),
                                  mini_file_detailed_uri=os.path.join(category_path(), "entrees_salades_detailed.json"))
    # 93 résultats
    PATES_TARTES_CREPES = StaticAisle(name="Pâtes à pizza, Pâtes à tartes et Crêpes", url="https://www.carrefour.fr/r/charcuterie-traiteur/pates-tartes-crepes",
                                      original_file_uri=os.path.join(category_path(), "pates_tartes_crepes.json"),
                                      mini_file_detailed_uri=os.path.join(category_path(), "pates_tartes_crepes_detailed.json"))
    # 366 résultats
    PIZZAS_TARTES_PATES_FRAICHES = StaticAisle(name="Pizzas, Tartes, Pâtes fraîches", url="https://www.carrefour.fr/r/charcuterie-traiteur/pizzas-tartes-pates-fraiches",
                                               original_file_uri=os.path.join(category_path(), "pizzas_tartes_pates_fraiches.json"),
                                               mini_file_detailed_uri=os.path.join(category_path(), "pizzas_tartes_pates_fraiches_detailed.json"))
    # 573 résultats
    PLATS_CUSINES = StaticAisle(name="Plats cuisinés et Cuisine du monde", url="https://www.carrefour.fr/r/charcuterie-traiteur/plats-cuisines",
                                original_file_uri=os.path.join(category_path(), "plats_cuisines.json"),
                                mini_file_detailed_uri=os.path.join(category_path(), "plats_cuisines_detailed.json"))
    # 315
    SANDWICH_REPAS_EXPRESS = StaticAisle(name="Sandwichs et Repas express", url="https://www.carrefour.fr/r/charcuterie-traiteur/sandwich-repas-express",
                                         original_file_uri=os.path.join(category_path(), "sandwich_repas_express.json"),
                                         mini_file_detailed_uri=os.path.join(category_path(), "sandwich_repas_express_detailed.json"))
    # 508 résultats
    TRAITEUR_TRADITIONNEL = StaticAisle(name="Traiteur traditionnel", url="https://www.carrefour.fr/r/charcuterie-traiteur/traiteur-traditionnel",
                                        original_file_uri=os.path.join(category_path(), "traiteur_traditionnel.json"),
                                        mini_file_detailed_uri=os.path.join(category_path(), "traiteur_traditionnel_detailed.json"))
    # 304 résultats
    TRAITEUR_VEGETAL = StaticAisle(name="Traiteur végétal", url="https://www.carrefour.fr/r/dietetique-preferences-alimentaires/vegetal/traiteur-vegetal",
                                   original_file_uri=os.path.join(category_path(), "traiteur_vegetal.json"),
                                   mini_file_detailed_uri=os.path.join(category_path(), "traiteur_vegetal_detailed.json"))

    aisles: Final[List[StaticAisle]] = [PATES_TARTES_CREPES, COUPE_CHARCUTERIE, APERITIFS, TRAITEUR_VEGETAL, TRAITEUR_TRADITIONNEL,
                                  SANDWICH_REPAS_EXPRESS, PIZZAS_TARTES_PATES_FRAICHES, ENTREES_SALADES, PLATS_CUSINES, CHARCUTERIE
                                  ]

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
                case "COUPE_CHARCUTERIE":
                    aisles = [cls.COUPE_CHARCUTERIE]
                case "CHARCUTERIE":
                    aisles = [cls.CHARCUTERIE]
                case "TRAITEUR_TRADITIONNEL":
                    aisles = [cls.TRAITEUR_TRADITIONNEL]
                case "TRAITEUR_VEGETAL":
                    aisles = [cls.TRAITEUR_VEGETAL]
                case "APERITIFS":
                    aisles = [cls.APERITIFS]
                case "ENTREES_SALADES":
                    aisles = [cls.ENTREES_SALADES]
                case "PATES_TARTES_CREPES":
                    aisles = [cls.PATES_TARTES_CREPES]
                case "PIZZAS_TARTES_PATES_FRAICHES":
                    aisles = [cls.PIZZAS_TARTES_PATES_FRAICHES]
                case "SANDWICH_REPAS_EXPRESS":
                    aisles = [cls.SANDWICH_REPAS_EXPRESS]
                case "PLATS_CUSINES":
                    aisles = [cls.PLATS_CUSINES]
        return aisles

class CarrefourCremerieProduitsLaitiers(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "cremerie")

    # 352 products
    BEURRES_CREMES = StaticAisle(name="Beurres et Crèmes", url="https://www.carrefour.fr/r/cremerie/beurres-cremes",
                                 original_file_uri=os.path.join(category_path(), "beurres_cremes.json"),
                                 mini_file_detailed_uri=os.path.join(category_path(), "beurres_cremes_detailed.json"))
    # 519 products
    DESSERTS_COMPOTES = StaticAisle(name="Desserts et Compotes", url="https://www.carrefour.fr/r/cremerie/desserts-compotes",
                                    original_file_uri=os.path.join(category_path(), "desserts_compotes.json"),
                                    mini_file_detailed_uri=os.path.join(category_path(), "desserts_compotes_detailed.json"))
    # 1215 products
    FORMAGES = StaticAisle(name="Fromages", url="https://www.carrefour.fr/r/cremerie/fromages",
                           original_file_uri=os.path.join(category_path(), "fromages.json"),
                           mini_file_detailed_uri=os.path.join(category_path(), "fromages_detailed.json"))
    # 238 products
    LAITS = StaticAisle(name="Laits", url="https://www.carrefour.fr/r/cremerie/laits",
                        original_file_uri=os.path.join(category_path(), "lait.json"),
                        mini_file_detailed_uri=os.path.join(category_path(), "lait_detailed.json"))

    # 121 products
    OEUFS = StaticAisle(name="Œufs", url="https://www.carrefour.fr/r/cremerie/oeufs",
                        original_file_uri=os.path.join(category_path(), "oeufs.json"),
                        mini_file_detailed_uri=os.path.join(category_path(), "oeufs_detailed.json"))

    # 1178 products
    YAOURTS_FROMAGES_BLANCS = StaticAisle(name="Yaourts et Fromages blancs", aisle_id="36995", url="https://www.carrefour.fr/r/cremerie/yaourts-fromages-blancs",
                                          original_file_uri=os.path.join(category_path(), "yaourts_fromages_blancs.json"),
                                          mini_file_detailed_uri=os.path.join(category_path(), "yaourts_fromages_blancs_detailed.json"))

    aisles: Final[List[StaticAisle]] = [OEUFS,
                                  LAITS,
                                  FORMAGES,
                                  BEURRES_CREMES,
                                  DESSERTS_COMPOTES,
                                  YAOURTS_FROMAGES_BLANCS]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles = List[StaticAisle]
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")

        if len(split_list) == 1:
            aisles = cls.aisles
        else:
            match selected_aisle:
                case "FORMAGES":
                    aisles = [
                        cls.FORMAGES]  # 1170
                case "YAOURTS_FROMAGES_BLANCS":
                    # 822 products
                    aisles = [
                        cls.YAOURTS_FROMAGES_BLANCS]
                case "BEURRES_CREMES":
                    # 327 products
                    aisles = [cls.BEURRES_CREMES]
                case "LAITS":
                    # 114 products
                    aisles = [cls.LAITS]
                case "OEUFS":
                    # 123 products
                    aisles = [cls.OEUFS]
                case "DESSERTS_COMPOTES":
                    # 272 products
                    aisles = [
                        cls.DESSERTS_COMPOTES]
                case _:
                    aisles = []
        print(f"{type(cls).__name__} get_aisles for string: {args} aisles found: {len(aisles)}")
        return aisles

class CarrefourEpicerieSalee(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "epicerie_salee")

    # products 1299
    APERITIF_CHIPS = StaticAisle(name="Apéritifs et Chips", url="https://www.carrefour.fr/r/epicerie-salee/pour-laperitif",
                                 original_file_uri=os.path.join(category_path(), "aperitif_chips.json"),
                                 mini_file_detailed_uri=os.path.join(category_path(), "aperitif_chips_detailed.json"))

    # products 1951
    CONSERVES_BOCAUX = StaticAisle(name="Conserves et Bocaux", url="https://www.carrefour.fr/r/epicerie-salee/conserves-et-bocaux",
                                   original_file_uri=os.path.join(category_path(), "conserves_bocaux.json"),
                                   mini_file_detailed_uri=os.path.join(category_path(), "conserves_bocaux_detailed.json"))

    # products 737
    HUILES_VINAIGRES_VINAIGRETTES = StaticAisle(name="Huiles, Vinaigres et Vinaigrettes", url="https://www.carrefour.fr/r/epicerie-salee/huiles-vinaigres-et-vinaigrettes",
                                                original_file_uri=os.path.join(category_path(), "huiles_vinaigres_vinaigrettes.json"),
                                                mini_file_detailed_uri=os.path.join(category_path(), "huiles_vinaigres_vinaigrettes_detailed.json"))

    # products 1049
    PATES_RIZ_FECULENTS = StaticAisle(name="Pâtes, Riz, Purées et Féculents", url="https://www.carrefour.fr/r/epicerie-salee/pates-riz-feculents",
                                      original_file_uri=os.path.join(category_path(), "pates_riz_feculents.json"),
                                      mini_file_detailed_uri=os.path.join(category_path(), "pates_riz_feculents_detailed.json"))

    # products 520
    PLATS_CUSINES = StaticAisle(name="Plats cuisinés", url="https://www.carrefour.fr/r/epicerie-salee/les-plats-cuisines",
                                original_file_uri=os.path.join(category_path(), "plats_cuisines.json"),
                                mini_file_detailed_uri=os.path.join(category_path(), "plats_cuisines_detailed.json"))

    # products 1756
    SAUCES_CONDIMENTS = StaticAisle(name="Sauces et Condiments", url="https://www.carrefour.fr/r/epicerie-salee/sauces-et-condiments",
                                    original_file_uri=os.path.join(category_path(), "sauces_condiments.json"),
                                    mini_file_detailed_uri=os.path.join(category_path(), "sauces_condiments_detailed.json"))
    # products 2468
    SEL_EPICES_BOUILLONS = StaticAisle(name="Sel, Epices et Bouillons", url="https://www.carrefour.fr/r/epicerie-salee/sel-epices-et-bouillons",
                                       original_file_uri=os.path.join(category_path(), "sel_epices_bouillons.json"),
                                       mini_file_detailed_uri=os.path.join(category_path(), "sel_epices_bouillons_detailed.json"))
    # products 298
    SOUPES_CROUTONS = StaticAisle(name="Soupes et Croutons", url="https://www.carrefour.fr/r/epicerie-salee/soupes-et-croutons",
                                  original_file_uri=os.path.join(category_path(), "soupes_croutons.json"),
                                  mini_file_detailed_uri=os.path.join(category_path(), "soupes_croutons_detailed.json"))
    aisles: Final[List[StaticAisle]] = [SAUCES_CONDIMENTS, SOUPES_CROUTONS, PLATS_CUSINES, HUILES_VINAIGRES_VINAIGRETTES, PATES_RIZ_FECULENTS, APERITIF_CHIPS, CONSERVES_BOCAUX, SEL_EPICES_BOUILLONS]

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
                case "AISLES_PART1":
                    aisles = [cls.APERITIF_CHIPS,
                              cls.SOUPES_CROUTONS]
                case "AISLES_PART2":
                    aisles = [cls.CONSERVES_BOCAUX]
                case "AISLES_PART3":
                    aisles = [cls.SEL_EPICES_BOUILLONS]
                case "RAYONS_PART4":
                    aisles = [cls.PATES_RIZ_FECULENTS]
                case "RAYONS_PART5":
                    aisles = [cls.HUILES_VINAIGRES_VINAIGRETTES, cls.PLATS_CUSINES]
                case "APERITIF_CHIPS":
                    aisles = [cls.APERITIF_CHIPS]
                case "HUILES_VINAIGRES_VINAIGRETTES":
                    aisles = [cls.HUILES_VINAIGRES_VINAIGRETTES]
                case "CONSERVES_BOCAUX":
                    aisles = [cls.CONSERVES_BOCAUX]
                case "PLATS_CUSINES":
                    aisles = [cls.PLATS_CUSINES]
                case "PATES_RIZ_FECULENTS":
                    aisles = [cls.PATES_RIZ_FECULENTS]
                case "SAUCES_CONDIMENTS":
                    aisles = [cls.SAUCES_CONDIMENTS]
                case "SEL_EPICES_BOUILLONS":
                    aisles = [cls.SEL_EPICES_BOUILLONS]
                case "SOUPES_CROUTONS":
                    aisles = [cls.SOUPES_CROUTONS]

        return aisles

class CarrefourEpicerieSucree(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "epicerie_sucree")

    # products 1039
    BISCUITS = StaticAisle(name="Biscuits", url="https://www.carrefour.fr/r/epicerie-sucree/biscuits",
                           original_file_uri=os.path.join(category_path(), "biscuits.json"),
                           mini_file_detailed_uri=os.path.join(category_path(), "biscuits_detailed.json"))
    # products 793
    BOISSONS_CHAUDES = StaticAisle(name="Thés, Infusions et Boissons chaudes", url="https://www.carrefour.fr/r/epicerie-sucree/boissons-chaudes",
                                   original_file_uri=os.path.join(category_path(), "boissons_chaudes.json"),
                                   mini_file_detailed_uri=os.path.join(category_path(), "boissons_chaudes_detailed.json"))
    # prodcts 851
    CAFES = StaticAisle(name="Cafés", url="https://www.carrefour.fr/r/epicerie-sucree/cafes",
                        original_file_uri=os.path.join(category_path(), "cafes.json"),
                        mini_file_detailed_uri=os.path.join(category_path(), "cafes_detailed.json"))

    # products 1457
    CHOCOLATS_BONBONS = StaticAisle(name="Chocolats et Bonbons", url="https://www.carrefour.fr/r/epicerie-sucree/chocolats-et-bonbons",
                                    original_file_uri=os.path.join(category_path(), "chocolats_bonbons.json"),
                                    mini_file_detailed_uri=os.path.join(category_path(), "chocolats_bonbons_detailed.json"))

    # products 348
    COMPOTES_FRUITS_SIRROP_CREMES_DESSERTS = StaticAisle(name="Compotes, Fruits au sirop et Crèmes desserts", url="https://www.carrefour.fr/r/epicerie-sucree/compotes-fruits-au-sirop-et-cremes-desserts",
                                                         original_file_uri=os.path.join(category_path(), "compotes_fruits_sirop_cremes_desserts.json"),
                                                         mini_file_detailed_uri=os.path.join(category_path(), "compotes_fruits_sirop_cremes_desserts_detailed.json"))
    # products 538
    GATEAUX_MOELLEUX = StaticAisle(name="Gâteaux moelleux", url="https://www.carrefour.fr/r/epicerie-sucree/gateaux-moelleux",
                                   original_file_uri=os.path.join(category_path(), "gateaux_moelleux.json"),
                                   mini_file_detailed_uri=os.path.join(category_path(), "gateaux_moelleux_detailed.json"))

    # products 0
    PETIT_DEJEUNER = StaticAisle(name="Petit déjeuner", url="https://www.carrefour.fr/r/petit-dejeuner",
                                 original_file_uri=os.path.join(category_path(), "petit_dejeuner.json"),
                                 mini_file_detailed_uri=os.path.join(category_path(), "petit_dejeuner_detailed.json"))

    # products 1663
    SUCRE_FARINE_AIDE_PATISSERIE = StaticAisle(name="Sucres, Farines et Aide à la pâtisserie", url="https://www.carrefour.fr/r/epicerie-sucree/sucres-farines-coulis-et-preparation-gateaux",
                                               original_file_uri=os.path.join(category_path(), "sucres_farines_gateaux.json"),
                                               mini_file_detailed_uri=os.path.join(category_path(), "sucres_farines_gateaux_detailed.json"))

    aisles: Final[List[StaticAisle]] = [PETIT_DEJEUNER, COMPOTES_FRUITS_SIRROP_CREMES_DESSERTS, GATEAUX_MOELLEUX, BOISSONS_CHAUDES,
                                  CAFES, BISCUITS, CHOCOLATS_BONBONS, SUCRE_FARINE_AIDE_PATISSERIE]

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
                case "CAFES":
                    aisles = [cls.CAFES]
                case "BOISSONS_CHAUDES":
                    aisles = [
                        cls.BOISSONS_CHAUDES]
                case "PETIT_DEJEUNER":
                    aisles = [cls.PETIT_DEJEUNER]
                case "BISCUITS":
                    aisles = [cls.BISCUITS]
                case "GATEAUX_MOELLEUX":
                    aisles = [cls.GATEAUX_MOELLEUX]
                case "CHOCOLATS_BONBONS":
                    aisles = [cls.CHOCOLATS_BONBONS]
                case "SUCRE_FARINE_AIDE_PATISSERIE":
                    aisles = [
                        cls.SUCRE_FARINE_AIDE_PATISSERIE]
                case "COMPOTES_FRUITS_SIRROP_CREMES_DESSERTS":
                    aisles = [
                        cls.COMPOTES_FRUITS_SIRROP_CREMES_DESSERTS]

        return aisles

class CarrefourFruitsEtLegumes(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "fruits_legumes")

    # 560 résultats
    FRUITS_ONLY = StaticAisle(name="Fruits", url="https://www.carrefour.fr/r/fruits-et-legumes/fruits",
                         original_file_uri=os.path.join(category_path(), "fruits_only.json"),
                         mini_file_detailed_uri=os.path.join(category_path(), "fruits_only_detailed.json"))

    # 293 résultats
    FRUITS_LEGUMES_BIO = StaticAisle(name="Fruits et légumes bio", url="https://www.carrefour.fr/r/fruits-et-legumes/fruits-et-legumes-bio",
                                     original_file_uri=os.path.join(category_path(), "fruits_legumes_bio.json"),
                                     mini_file_detailed_uri=os.path.join(category_path(), "fruits_legumes_bio_detailed.json"))

    # 667 résultats
    FRUITS_LEGUMES_SECS = StaticAisle(name="Fruits secs et Graines", url="https://www.carrefour.fr/r/fruits-et-legumes/fruits-et-legumes-secs",
                                      original_file_uri=os.path.join(category_path(), "fruits_legumes_secs.json"),
                                      mini_file_detailed_uri=os.path.join(category_path(), "fruits_legumes_secs_detailed.json"))

    # 202 résultats
    JUS_FRUITS_LEGUMES_FRAIS = StaticAisle(name="Jus de fruits frais et Gaspachos", url="https://www.carrefour.fr/r/fruits-et-legumes/jus-de-fruits-et-legumes-frais",
                                           original_file_uri=os.path.join(category_path(), "jus_de_fruits_legumes_frais.json"),
                                           mini_file_detailed_uri=os.path.join(category_path(), "jus_de_fruits_legumes_frais_detailed.json"))

    # 730 résultats
    LEGUMES = StaticAisle(name="Légumes", url="https://www.carrefour.fr/r/fruits-et-legumes/legumes",
                          original_file_uri=os.path.join(category_path(), "legumes.json"),
                          mini_file_detailed_uri=os.path.join(category_path(), "legumes_detailed.json"))
    # 288 résultats
    PRET_A_CONSOMMER = StaticAisle(name="Prêt à consomme", url="https://www.carrefour.fr/r/fruits-et-legumes/pret-a-consommer",
                                   original_file_uri=os.path.join(category_path(), "pret_a_consommer.json"),
                                   mini_file_detailed_uri=os.path.join(category_path(), "pret_a_consommer_detailed.json"))

    aisles: Final[List[StaticAisle]] = [JUS_FRUITS_LEGUMES_FRAIS, PRET_A_CONSOMMER, FRUITS_LEGUMES_BIO, FRUITS_ONLY, LEGUMES, FRUITS_LEGUMES_SECS]

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
                case "FRUITS_LEGUMES_BIO":
                    aisles = [cls.FRUITS_LEGUMES_BIO]
                case "FRUITS_ONLY":
                    aisles = [cls.FRUITS_ONLY]
                case "LEGUMES":
                    aisles = [cls.LEGUMES]
                case "PRET_A_CONSOMMER":
                    aisles = [cls.PRET_A_CONSOMMER]
                case "JUS_FRUITS_LEGUMES_FRAIS":
                    aisles = [CarrefourFruitsEtLegumes.JUS_FRUITS_LEGUMES_FRAIS]
                case "FRUITS_LEGUMES_SECS":
                    aisles = [CarrefourFruitsEtLegumes.FRUITS_LEGUMES_SECS]

        return aisles

class CarrefourPainsEtPatisseries(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "pains_patisseries")

    # 2
    GALETTES_ROIS = StaticAisle(name="galettes des rois", url="https://www.carrefour.fr/r/pains-et-patisseries/galettes-des-rois",
                                original_file_uri=os.path.join(category_path(), "galettes_des_rois.json"),
                                mini_file_detailed_uri=os.path.join(category_path(), "galettes_des_rois_detailed.json"))

    # 166 résultats
    PAINS_DE_MIE = StaticAisle(name="pains de mie", url="https://www.carrefour.fr/r/pains-et-patisseries/pains-de-mie",
                               original_file_uri=os.path.join(category_path(), "pains_de_mie.json"),
                               mini_file_detailed_uri=os.path.join(category_path(), "pains_de_mie_detailed.json"))

    # 125 résultats
    PAINS_FRAIS = StaticAisle(name="Pains frais", url="https://www.carrefour.fr/r/pains-et-patisseries/pains-frais",
                              original_file_uri=os.path.join(category_path(), "pains_frais.json"),
                              mini_file_detailed_uri=os.path.join(category_path(), "pains_frais_detailed.json"))
    # 245 résultats
    PATISSERIE = StaticAisle(name="Pâtisseries", url="https://www.carrefour.fr/r/pains-et-patisseries/patisserie",
                             original_file_uri=os.path.join(category_path(), "patisserie.json"),
                             mini_file_detailed_uri=os.path.join(category_path(), "patisserie_detailed.json"))
    # 86 résultats
    VENNOISERIES_BRIOCHES_FRAICHES = StaticAisle(name="Viennoiseries et Brioches fraîches", url="https://www.carrefour.fr/r/pains-et-patisseries/viennoiseries-brioches-fraiches",
                                                 original_file_uri=os.path.join(category_path(), "viennoiseries_brioches_fraiches.json"),
                                                 mini_file_detailed_uri=os.path.join(category_path(), "viennoiseries_brioches_fraiches_detailed.json"))
    # 151 résultats
    VIENNOISERIES_ET_BRIOCHES = StaticAisle(name="Viennoiseries et Brioches", url="https://www.carrefour.fr/r/pains-et-patisseries/viennoiseries-brioches",
                                         original_file_uri=os.path.join(category_path(), "viennoiseries_et_brioches.json"),
                                         mini_file_detailed_uri=os.path.join(category_path(), "viennoiseries_et_brioches_detailed.json"))
    aisles: Final[List[StaticAisle]] = [GALETTES_ROIS, VENNOISERIES_BRIOCHES_FRAICHES, VIENNOISERIES_ET_BRIOCHES,
                                  PAINS_FRAIS, PAINS_DE_MIE, PATISSERIE]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = CarrefourPainsEtPatisseries.aisles
        else:
            match selected_aisle:
                case "GALETTES_ROIS":
                    aisles = [CarrefourPainsEtPatisseries.GALETTES_ROIS]
                case "PAINS_FRAIS":
                    aisles = [CarrefourPainsEtPatisseries.PAINS_FRAIS]
                case "PATISSERIE":
                    aisles = [CarrefourPainsEtPatisseries.PATISSERIE]
                case "VENNOISERIES_BRIOCHES_FRAICHES":
                    aisles = [CarrefourPainsEtPatisseries.VENNOISERIES_BRIOCHES_FRAICHES]
                case "VIENNOISERIES_ET_BRIOCHES":
                    aisles = [
                        CarrefourPainsEtPatisseries.VIENNOISERIES_ET_BRIOCHES]
                case "PAINS_DE_MIE":
                    aisles = [CarrefourPainsEtPatisseries.PAINS_DE_MIE]
        return aisles

class CarrefourSurgeles(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "surgeles")

    # products 106
    APERITIFS_ENTREES_SNACKING = StaticAisle(name="Apéritifs, Entrées et Snacking", url="https://www.carrefour.fr/r/surgeles/aperitifs-entrees-snacking",
                                             original_file_uri=os.path.join(category_path(), "aperitifs_entrees_snacking.json"),
                                             mini_file_detailed_uri=os.path.join(category_path(), "aperitifs_entrees_snacking_detailed.json"))

    # products 97
    FRITES_POMMES_TERRE = StaticAisle(name="Frites et Pommes de terre", url="https://www.carrefour.fr/r/surgeles/frites-pommes-de-terre",
                                      original_file_uri=os.path.join(category_path(), "frites_pommes_de_terre.json"),
                                      mini_file_detailed_uri=os.path.join(category_path(), "frites_pommes_de_terre_detailed.json"))

    # products 376
    GLACES_SORBETS = StaticAisle(name="Glaces et Sorbets", url="https://www.carrefour.fr/r/surgeles/glaces-et-sorbets",
                                 original_file_uri=os.path.join(category_path(), "glaces_sorbets.json"),
                                 mini_file_detailed_uri=os.path.join(category_path(), "glaces_sorbets_detailed.json"))

    # products 181
    LEGUMES_FRUITS = StaticAisle(name="légumes et fruits", url="https://www.carrefour.fr/r/surgeles/viandes",
                                 original_file_uri=os.path.join(category_path(), "legumes_fruits.json"),
                                 mini_file_detailed_uri=os.path.join(category_path(), "legumes_fruits_detailed.json"))

    # products 59
    PAIN_PATISSERIES_VIENNOISERIES = StaticAisle(name="Pains, Pâtisseries et Viennoiseries", url="https://www.carrefour.fr/r/surgeles/pain-patisseries-viennoiseries",
                                                 original_file_uri=os.path.join(category_path(), "pain_patisseries_viennoiseries.json"),
                                                 mini_file_detailed_uri=os.path.join(category_path(), "pain_patisseries_viennoiseries_detailed.json"))

    # products 91
    PIZZAS_QUICHES_TARTES = StaticAisle(name="Pizzas, Quiches et Tartes", url="https://www.carrefour.fr/r/surgeles/pizzas-quiches-tartes",
                                        original_file_uri=os.path.join(category_path(), "pizzas_quiches_tartes.json"),
                                        mini_file_detailed_uri=os.path.join(category_path(), "pizzas_quiches_tartes_detailed.json"))
    # products 246
    PLATS_CUSINES = StaticAisle(name="Plats cuisinés", url="https://www.carrefour.fr/r/surgeles/plats-cuisines",
                                original_file_uri=os.path.join(category_path(), "plats_cuisines.json"),
                                mini_file_detailed_uri=os.path.join(category_path(), "plats_cuisines_detailed.json"))

    # products 160
    POISSONS_FRUITS_MER = StaticAisle(name="Poissons et Fruits de mer", url="https://www.carrefour.fr/r/surgeles/poissons-fruits-de-mer",
                                      original_file_uri=os.path.join(category_path(), "poissons_fruits_de_mer.json"),
                                      mini_file_detailed_uri=os.path.join(category_path(), "poissons_fruits_de_mer_detailed.json"))

    # products 181
    VIANDES = StaticAisle(name="Viandes", url="https://www.carrefour.fr/r/surgeles/viandes",
                          original_file_uri=os.path.join(category_path(), "viandes.json"),
                          mini_file_detailed_uri=os.path.join(category_path(), "viandes_detailed.json"))

    aisles: Final[List[StaticAisle]] = [PAIN_PATISSERIES_VIENNOISERIES, PIZZAS_QUICHES_TARTES, POISSONS_FRUITS_MER,
                                  FRITES_POMMES_TERRE, APERITIFS_ENTREES_SNACKING,
                                  VIANDES, LEGUMES_FRUITS, PLATS_CUSINES, GLACES_SORBETS]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = CarrefourSurgeles.aisles
        else:
            match selected_aisle:
                case "aisles_part1":
                    aisles = [CarrefourSurgeles.GLACES_SORBETS,
                              CarrefourSurgeles.APERITIFS_ENTREES_SNACKING]
                case "aisles_part2":
                    aisles = [CarrefourSurgeles.PIZZAS_QUICHES_TARTES,
                              CarrefourSurgeles.PLATS_CUSINES]
                case "aisles_part3":
                    aisles = [CarrefourSurgeles.FRITES_POMMES_TERRE,
                              CarrefourSurgeles.VIANDES]
                case "aisles_part4":
                    aisles = [CarrefourSurgeles.POISSONS_FRUITS_MER,
                              CarrefourSurgeles.PAIN_PATISSERIES_VIENNOISERIES]
                case "aisles_part5":
                    aisles = [CarrefourSurgeles.LEGUMES_FRUITS]
                case "GLACES_SORBETS":
                    aisles = [CarrefourSurgeles.GLACES_SORBETS]
                case "APERITIFS_ENTREES_SNACKING":
                    aisles = [CarrefourSurgeles.APERITIFS_ENTREES_SNACKING]
                case "PIZZAS_QUICHES_TARTES":
                    aisles = [CarrefourSurgeles.PIZZAS_QUICHES_TARTES]
                case "PLATS_CUSINES":
                    aisles = [CarrefourSurgeles.PLATS_CUSINES]
                case "FRITES_POMMES_TERRE":
                    aisles = [CarrefourSurgeles.FRITES_POMMES_TERRE]
                case "VIANDES":
                    aisles = [CarrefourSurgeles.VIANDES]
                case "POISSONS_FRUITS_MER":
                    aisles = [CarrefourSurgeles.POISSONS_FRUITS_MER]
                case "PAIN_PATISSERIES_VIENNOISERIES":
                    aisles = [CarrefourSurgeles.PAIN_PATISSERIES_VIENNOISERIES]
                case "LEGUMES_FRUITS":
                    aisles = [CarrefourSurgeles.LEGUMES_FRUITS]
        return aisles

class CarrefourPromotions(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "promotions")

    # 1338 résultats
    BOISSONS = StaticAisle(name="BOISSONS", url="https://www.carrefour.fr/promotions?filters%5Bproduct.categories.id%5D%5B0%5D=27070",
                            original_file_uri=os.path.join(category_path(), "boissons.json"),
                            mini_file_detailed_uri=os.path.join(category_path(), "boissons_detailed.json"))
    # 1279
    BIO_ECOLOGIE = StaticAisle(name="BIO_ECOLOGIE", url="https://www.carrefour.fr/promotions?filters%5Bproduct.categories.id%5D=1838&noRedirect=0",
                            original_file_uri=os.path.join(category_path(), "bio_ecologie.json"),
                            mini_file_detailed_uri=os.path.join(category_path(), "bio_ecologie_detailed.json"))
    # 1230
    EPICERIE_SALEE = StaticAisle(name="EPICERIE_SALEE", url="https://www.carrefour.fr/promotions?filters%5Bproduct.categories.id%5D=2112",
                            original_file_uri=os.path.join(category_path(), "epicerie_salee.json"),
                            mini_file_detailed_uri=os.path.join(category_path(), "epicerie_salee_detailed.json"))
    # 1124
    EPICERIE_SUCREE = StaticAisle(name="EPICERIE_SUCREE", url="https://www.carrefour.fr/promotions?filters%5Bproduct.categories.id%5D=2183",
                            original_file_uri=os.path.join(category_path(), "epicerie_sucree.json"),
                            mini_file_detailed_uri=os.path.join(category_path(), "epicerie_sucree_detailed.json"))
    # 519
    CREMERIE_LAITIER = StaticAisle(name="cremerie laitier", url="https://www.carrefour.fr/promotions?filters%5Bproduct.categories.id%5D=36993",
                            original_file_uri=os.path.join(category_path(), "cremerie_laitier.json"),
                            mini_file_detailed_uri=os.path.join(category_path(), "cremerie_laitier_detailed.json"))
    #652
    PRODUITS_MONDE = StaticAisle(name="PRODUITS_MONDE", url="https://www.carrefour.fr/promotions?filters%5Bproduct.categories.id%5D=29650",
                            original_file_uri=os.path.join(category_path(), "produits_monde.json"),
                            mini_file_detailed_uri=os.path.join(category_path(), "produits_monde_detailed.json"))

    #791
    CHARCUTERIE_TRAITEUR = StaticAisle(name="charcuterie traiteur", url="https://www.carrefour.fr/promotions?filters%5Bproduct.categories.id%5D=36993",
                            original_file_uri=os.path.join(category_path(), "charcuterie_traiteur.json"),
                            mini_file_detailed_uri=os.path.join(category_path(), "charcuterie_traiteur_detailed.json"))
    # 308
    SURGELES = StaticAisle(name="SURGELES", url="https://www.carrefour.fr/promotions?filters%5Bproduct.categories.id%5D=2074",
                            original_file_uri=os.path.join(category_path(), "surgeles.json"),
                            mini_file_detailed_uri=os.path.join(category_path(), "surgeles_detailed.json"))
    # 255
    FRUITS_LEGUMES = StaticAisle(name="fruits legumes", url="https://www.carrefour.fr/promotions?filters%5Bproduct.categories.id%5D=1882",
                            original_file_uri=os.path.join(category_path(), "fruits_legumes.json"),
                            mini_file_detailed_uri=os.path.join(category_path(), "fruits_legumes_detailed.json"))

    NUTRITION_VEGETALE = StaticAisle(name="nutrition vegetale", url="https://www.carrefour.fr/promotions?filters%5Bproduct.categories.id%5D=30350",
                            original_file_uri=os.path.join(category_path(), "nutrition_vegetale.json"),
                            mini_file_detailed_uri=os.path.join(category_path(), "nutrition_vegetale_detailed.json"))
    # 202
    VIANDES_POISSONS = StaticAisle(name="viandes poissons", url="https://www.carrefour.fr/promotions?filters%5Bproduct.categories.id%5D=1921",
                                original_file_uri=os.path.join(category_path(), "viandes_poissons.json"),
                                mini_file_detailed_uri=os.path.join(category_path(), "viandes_poissons_detailed.json"))
    # 152
    PRODUITS_REGIONAUX_LOCAUX = StaticAisle(name="produits regionaux locaux", url="https://www.carrefour.fr/promotions?filters%5Bproduct.categories.id%5D=3887",
                                original_file_uri=os.path.join(category_path(), "produits_regionaux_locaux.json"),
                                mini_file_detailed_uri=os.path.join(category_path(), "produits_regionaux_locaux_detailed.json"))
    # 128
    PAINS_PATISSERIES = StaticAisle(name="pains patisseries", url="https://www.carrefour.fr/promotions?filters%5Bproduct.categories.id%5D=1952",
                                original_file_uri=os.path.join(category_path(), "pains_patisseries.json"),
                                mini_file_detailed_uri=os.path.join(category_path(), "pains_patisseries_detailed.json"))
    aisles: Final[List[StaticAisle]] = [BOISSONS, BIO_ECOLOGIE, EPICERIE_SALEE, EPICERIE_SUCREE,
    PRODUITS_MONDE, CHARCUTERIE_TRAITEUR, SURGELES, FRUITS_LEGUMES, NUTRITION_VEGETALE, 
    VIANDES_POISSONS, PRODUITS_REGIONAUX_LOCAUX, PAINS_PATISSERIES]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: Union[List[StaticAisle], None] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = CarrefourPromotions.aisles
        else:
            match selected_aisle:
                case "BOISSONS":
                    aisles = [CarrefourPromotions.BOISSONS]
                case "BIO_ECOLOGIE":
                    aisles = [CarrefourPromotions.BIO_ECOLOGIE]
                case "EPICERIE_SALEE":
                    aisles = [CarrefourPromotions.EPICERIE_SALEE]
                case "EPICERIE_SUCREE":
                    aisles = [CarrefourPromotions.EPICERIE_SUCREE]
                case "CREMERIE_LAITIER":
                    aisles = [CarrefourPromotions.CREMERIE_LAITIER]
                case "PRODUITS_MONDE":
                    aisles = [CarrefourPromotions.PRODUITS_MONDE]
                case "CHARCUTERIE_TRAITEUR":
                    aisles = [CarrefourPromotions.CHARCUTERIE_TRAITEUR]
                case "SURGELES":
                    aisles = [CarrefourPromotions.SURGELES]
                case "FRUITS_LEGUMES":
                    aisles = [CarrefourPromotions.FRUITS_LEGUMES]
                case "NUTRITION_VEGETALE":
                    aisles = [CarrefourPromotions.NUTRITION_VEGETALE]
                case "VIANDES_POISSONS":
                    aisles = [CarrefourPromotions.VIANDES_POISSONS]
                case "PRODUITS_REGIONAUX_LOCAUX":
                    aisles = [CarrefourPromotions.PRODUITS_REGIONAUX_LOCAUX]
                case "PAINS_PATISSERIES":
                    aisles = [CarrefourPromotions.PAINS_PATISSERIES]
        return aisles

class CarrefourViandesPoissons(CategoryParser):
    @staticmethod
    @override
    def category_path() -> str:
        return os.path.join(FOLDER_PATH, "viandes_poissons")

    # 1196 résultats
    BOUCHERIE = StaticAisle(name="Boucherie", url="https://www.carrefour.fr/r/viandes-et-poissons/boucherie",
                            original_file_uri=os.path.join(category_path(), "boucherie.json"),
                            mini_file_detailed_uri=os.path.join(category_path(), "boucherie_detailed.json"))
    # 312 résultats
    POISSONNERIE = StaticAisle(name="Poissonnerie", url="https://www.carrefour.fr/r/viandes-et-poissons/poissonnerie",
                               original_file_uri=os.path.join(category_path(), "poissonnerie.json"),
                               mini_file_detailed_uri=os.path.join(category_path(), "poissonnerie_detailed.json"))

    # 38 résultats
    SAUCES_ACCOMPAGNEMENT = StaticAisle(name="Sauces d'accompagnement", url="https://www.carrefour.fr/r/viandes-et-poissons/sauces-daccompagnement",
                                        original_file_uri=os.path.join(category_path(), "sauces_daccompagnement.json"),
                                        mini_file_detailed_uri=os.path.join(category_path(), "sauces_daccompagnement_detailed.json"))

    # 678 résultats
    TRAITEUR_MER = StaticAisle(name="Traiteur de la mer", url="https://www.carrefour.fr/r/viandes-et-poissons/traiteur-mer",
                               original_file_uri=os.path.join(category_path(), "traiteur_mer.json"),
                               mini_file_detailed_uri=os.path.join(category_path(), "traiteur_mer_detailed.json"))

    # 647 résultats
    VOLAILLE_ROTISSERIE = StaticAisle(name="Volaille et Rôtisserie", url="https://www.carrefour.fr/r/viandes-et-poissons/volaille-et-rotisserie",
                                      original_file_uri=os.path.join(category_path(), "volaille_rotisserie.json"),
                                      mini_file_detailed_uri=os.path.join(category_path(), "volaille_rotisserie_detailed.json"))
    aisles: Final[List[StaticAisle]] = [SAUCES_ACCOMPAGNEMENT, POISSONNERIE, TRAITEUR_MER, VOLAILLE_ROTISSERIE, BOUCHERIE]

    @classmethod
    @override
    def get_aisles(cls, args: str) -> List[StaticAisle]:
        aisles: List[StaticAisle] = []
        split_list = args.split(".")
        selected_aisle = split_list[1].upper() if len(split_list) > 1 else None
        print(f"selected_aisle: {selected_aisle}")
        if len(split_list) == 1:
            aisles = CarrefourViandesPoissons.aisles
        else:
            match selected_aisle:
                case "BOUCHERIE":
                    aisles = [CarrefourViandesPoissons.BOUCHERIE]
                case "POISSONNERIE":
                    aisles = [CarrefourViandesPoissons.POISSONNERIE]
                case "VOLAILLE_ROTISSERIE":
                    aisles = [CarrefourViandesPoissons.VOLAILLE_ROTISSERIE]
                case "TRAITEUR_MER":
                    aisles = [CarrefourViandesPoissons.TRAITEUR_MER]
                case "SAUCES_ACCOMPAGNEMENT":
                    aisles = [CarrefourViandesPoissons.SAUCES_ACCOMPAGNEMENT]
        return aisles

carrefour_categories_with_uris: Final[list[StaticCategory]] = [
    StaticCategory(name="Crèmerie et Produits laitiers", category_id="36993",
                   url="https://www.carrefour.fr/r/cremerie", aisles=CarrefourCremerieProduitsLaitiers.aisles),
    StaticCategory(name="Epicerie sucrée", url="https://www.carrefour.fr/r/epicerie-sucree",
                   aisles=CarrefourEpicerieSucree.aisles),
    StaticCategory(name="Epicerie salée", url="https://www.carrefour.fr/r/epicerie-salee",
                   aisles=CarrefourEpicerieSalee.aisles),
    StaticCategory(name="Boissons", url="https://www.carrefour.fr/r/boissons",
                   aisles=CarrefourBoissons.aisles),
    StaticCategory(name="Surgelés", url="https://www.carrefour.fr/r/surgeles",
                   aisles=CarrefourSurgeles.aisles),
    StaticCategory(name="Viandes et poissons", url="https://www.carrefour.fr/r/viandes-et-poissons",
                   aisles=CarrefourViandesPoissons.aisles),
    StaticCategory(name="Pains et Pâtisseries", url="https://www.carrefour.fr/r/pains-et-patisseries",
                   aisles=CarrefourPainsEtPatisseries.aisles),
    StaticCategory(name="Fruits et Légumes", url="https://www.carrefour.fr/r/fruits-et-legumes",
                   aisles=CarrefourFruitsEtLegumes.aisles),
    StaticCategory(name="Charcuterie et Traiteur", url="https://www.carrefour.fr/r/charcuterie-traiteur",
                   aisles=CarrefourCharcuterieTraiteur.aisles),
    StaticCategory(name="Bio et Ecologie", url="https://www.carrefour.fr/r/bio-et-ecologie",
                   aisles=CarrefourBioEcologie.aisles),
    StaticCategory(name="bebe", category_id="26953",
                   url="https://www.carrefour.fr/r/bebe", aisles=CarrefourBebeAlimentations.aisles)
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
        for category in carrefour_categories_with_uris:
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
                case "CarrefourEpicerieCremerie":
                    aisles = CarrefourCremerieProduitsLaitiers.get_aisles(cmdargs[1])
                case "CarrefourCremerieProduitsLaitiers":
                    aisles = CarrefourCremerieProduitsLaitiers.get_aisles(
                        cmdargs[1])
                case "CarrefourEpicerieSucree":
                    aisles = CarrefourEpicerieSucree.get_aisles(cmdargs[1])
                case "CarrefourEpicerieSalee":
                    aisles = CarrefourEpicerieSalee.get_aisles(cmdargs[1])
                case "CarrefourBoissons":
                    aisles = CarrefourBoissons.get_aisles(cmdargs[1])
                case "CarrefourSurgeles":
                    aisles = CarrefourSurgeles.get_aisles(cmdargs[1])
                case "CarrefourViandesPoissons":
                    aisles = CarrefourViandesPoissons.get_aisles(cmdargs[1])
                case "CarrefourFruitsEtLegumes":
                    aisles = CarrefourFruitsEtLegumes.get_aisles(cmdargs[1])
                case "CarrefourPainsEtPatisseries":
                    aisles = CarrefourPainsEtPatisseries.get_aisles(cmdargs[1])
                case "CarrefourCharcuterieTraiteur":
                    aisles = CarrefourCharcuterieTraiteur.get_aisles(cmdargs[1])
                case "CarrefourBioEcologie":
                    aisles = CarrefourBioEcologie.get_aisles(cmdargs[1])
                case "CarrefourBebeAlimentations":
                    aisles = CarrefourBebeAlimentations.get_aisles(cmdargs[1])
                case "CarrefourPromotions":
                    aisles = CarrefourPromotions.get_aisles(cmdargs[1])
                case _:
                    logging.error(f"args source not found: {cmdargs[1]}")
                    sys.exit()

    return aisles
