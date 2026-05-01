import os
import sys
import json
from typing import List
import dacite

# Ajout des chemins si nécessaire
sys.path.append('./')
sys.path.append('src')

# Imports internes
from src.model.product import Product , Category
from src.model.product_filter import ProductFilter
from src.dbV3.get_products_by_filter_useCase import GetProductsByFilterUseCase
from src.model.static_category_aisle import StaticAisle
from src.dbV3.create_or_update_evolution_useCase import CreateOrUpdateEvolutionUseCase
from src.countries.spain.MercadonaV3.model.product_mercadona import EvolutionMercadona
from src.utils.my_utils import extract_file_name, extract_folder_path, get_files_with_substring_ordered_by_mtime
from src.countries.spain.MercadonaV3.robots.static_data_V3 import get_static_aisles_from_user_cmdargs
from src.countries.spain.MercadonaV3.db.mercadonaMongoRepoSetup import mercadona_product_repository

def process_file(file_path: str):
    print(f"📄 Processing file: {file_path}")
    try:
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
            for product_data in data:
                try:
                    product = dacite.from_dict(data_class=Product, data=product_data, config=dacite.Config(strict=True))
                    use_case = CreateOrUpdateEvolutionUseCase(
                        product_repository=mercadona_product_repository,
                        productSubClassType=EvolutionMercadona
                    )
                    use_case.execute(product=product)
                except Exception as pe:
                    print(f"❌ Error processing product in {file_path}: {pe}")
    except Exception as fe:
        print(f"❌ Failed to open {file_path}: {fe}")

def get_all_products_from_mongodb_by_category_with_ia_ingredient(category_id: int) -> List[Product] | None:
    # filter = {
    #     'categories.id': category_id or 27070,
    #     'evolutions.ingredients_ia': {
    #         '$exists': True
    #     }
    # }
    product_filter = ProductFilter()
    filter_query = (
        product_filter
        .add_category_ids([Category(id=category_id)])
        .with_or_without_ia_ingredients(without=False)
        .build()
    )

    print(f"filter_query: {filter_query}")
    useCase = GetProductsByFilterUseCase(
        product_repository=mercadona_product_repository)
    products = useCase.execute(filter=filter_query)
    return products

if __name__ == "__main__":
    print("mercadona uploader my main")
    cmdargs = sys.argv
    print(f"The total numbers of args passed to the script: {len(cmdargs)}, Args list: + {cmdargs}")

    if len(cmdargs) < 2:
        print("⛔ Please provide a file, folder, or StaticAisle file.")
        sys.exit(1)

    input_path = cmdargs[1]

    # --- MODE 1 : dossier brut de JSONs ---
    if os.path.isdir(input_path):
        print(f"📁 Folder mode detected → parsing all *_iAdetailed.json in: {input_path}")
        json_files = [
            os.path.join(root, fname)
            for root, _, files in os.walk(input_path)
            for fname in files
            # on cherche le motif "_iadetailed.json" n'importe où dans le nom
            if "iadetailed" in fname.lower() and fname.lower().endswith(".json")
        ]
        if not json_files:
            print(f"❌ Aucun fichier '*_iAdetailed.json' trouvé dans : {input_path}")
            sys.exit(1)

        for json_path in json_files:
            process_file(json_path)
        sys.exit(0)

    # --- MODE 2 : StaticAisle JSON or chemin individuel ---
    aisles: List[StaticAisle] = get_static_aisles_from_user_cmdargs(cmdargs=cmdargs)
    print(f"number of aisles to parse: {len(aisles)}")
    if not aisles:
        print("⚠️ Aucune allée valide détectée.")
        sys.exit(1)

    for aisle in aisles:
        print(f"🛒 Aisle: {aisle.name}, original_file_uri: {aisle.original_file_uri}")
        files = []

        if os.path.isfile(cmdargs[1]):
            files = [aisle.original_file_uri]
        else:
            folder = extract_folder_path(aisle.original_file_uri)
            file_name = extract_file_name(aisle.original_file_uri)
            files = get_files_with_substring_ordered_by_mtime(folder_path=folder, substring=file_name.lower())
            if not files:
                print(f"❌ No files found for aisle: {aisle.name}")
                continue
            files = files[:2]

        for file in files or []:
            print(f"📄 Uploading file: {file}")
            process_file(file)
