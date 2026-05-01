# check if the given argument is aan aisle or a path
# if it is a path then check if it is a folder or a file
# if file, then return a list with file as a unique item
# if folder, then return a list of files (havind "details" substring)

# read the list of files one by one and load its content.
# the content if a list of products. for each product call the func A()

import json
import os
import sys
from typing import List

import dacite

from src.countries.france.carrefour.model.product_carrefour import EvolutionCarrefour
from src.dbV2.create_or_update_evolution_useCase import CreateOrUpdateEvolutionUseCase
from src.dbV2.get_products_by_filter_useCase import GetProductsByFilterUseCase
from src.model.product import Category, Product
from src.model.product_filter import ProductFilter
from src.utils.my_utils import extract_file_name, extract_folder_path, get_files_with_substring_ordered_by_mtime
from src.countries.france.carrefour.robots.carrefour_static_ailes import get_static_aisles_from_user_cmdargs
from src.model.static_category_aisle import StaticAisle
from src.countries.france.carrefour.db.CarrefourMongoRepoSetup import carrefour_product_repository


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
    # Output: {'evolutions.ingredients_ia': {
    #         '$exists': True
    #     }, 'categories.id': {'$in': [123, 456]}}

    useCase = GetProductsByFilterUseCase(
        product_repository=carrefour_product_repository)
    products = useCase.execute(filter=filter_query)
    return products

if __name__ == "__main__":
    print("carrefour uploader my main")
    # Get the arguments list
    cmdargs = sys.argv

    # Print it
    print(f"The total numbers of args passed to the script: {len(cmdargs)}, Args list: + {cmdargs}")
    # first arg section, second arg aisle
    if len(cmdargs) > 1:
        aisles: List[StaticAisle] = get_static_aisles_from_user_cmdargs(
            cmdargs=cmdargs)
        print(f"number of aisles to parse: {len(aisles)}")
        if not aisles:
            print("empty aisles")
            sys.exit()
        for aisle1 in aisles:
            aisle: StaticAisle = aisle1
            print(f"aisle to upload: {aisle.name}, original_file_uri: {aisle.original_file_uri}")
            files = []
            if os.path.isfile(cmdargs[1]):
                files = [aisle.original_file_uri]
            else:
                folder = extract_folder_path(file_path=aisle.original_file_uri)
                file_name = extract_file_name(file_path=aisle.original_file_uri)
                # extract all files in folder containg "details"
                file_name_substring = f"{file_name.lower()}_iAdetailed"
                files = get_files_with_substring_ordered_by_mtime(folder_path=folder, substring=file_name_substring)
                print(f"folder: {folder}")
                print(f"files: {files}")
                if not files:
                    print(f"no files found under aisle: {aisle.name}")
                    continue
                # for now we should limit the files to 2 since we have only two parsing dates
                # and to avoid sending a lot of useless iA queries and db queries
                files = files[:2]
                if "get_latest_parsed_products" in cmdargs:
                    files = files[0] if files else None
                    print(f"get_latest_parsed_products found, files:{files}")
                #end
            for file in files or []:
                print(f"file to upload: {file}")
                json_file = open(file, encoding='utf-8')
                products = json.load(json_file)
                for product in products:
                    product = dacite.from_dict(data_class=Product, data=product, config=dacite.Config(strict=True))
                    useCase = CreateOrUpdateEvolutionUseCase(product_repository=carrefour_product_repository, productSubClassType=EvolutionCarrefour)
                    useCase.execute(product = product)

                                