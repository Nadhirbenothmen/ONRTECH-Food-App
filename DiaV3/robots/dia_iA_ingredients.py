import json
import os
import sys
from typing import List

import dacite
sys.path.append('src')
sys.path.append ('./')
from src.countries.spain.DiaV3.db.dia_uploader import get_all_products_from_mongodb_by_category_with_ia_ingredient
from src.utils.iA_ingredients import clean_ingredients
from src.model.product import Evolution, Product
from src.countries.spain.DiaV3.model.product_content_dia import ProductContentDia
from src.utils.my_utils import extract_file_name, extract_folder_path, get_files_with_substring_ordered_by_mtime, keep_text_after, remove_extra_dots, remove_keyword_if_first, remove_keywords_and_empty_texts, remove_substrings_and_clean, rephrase_text_if_parenthesis_exists, write_output_to_file
from src.countries.spain.DiaV3.robots.static_data_V3 import get_static_aisles_from_user_cmdargs
from src.model.static_category_aisle import StaticAisle
from src.model.product_content import iA_keywords_for_ingredients_groups, iA_keywords_to_remove


def get_most_common_category_id(products: list):
    from collections import Counter
    # Extract all category labels from the JSON data
    all_categories = [
        category["id"]
        for product in products
        for category in product.get("categories", [])
    ]
    # Count occurrences of each category
    category_counts = Counter(all_categories)
    print(f"all category_counts: {category_counts}")
    # Find the most repeated category
    most_common_category = category_counts.most_common(1)[0]
    print(f"most_common_category: {most_common_category}")
    return most_common_category[0]



if __name__ == "__main__":
    print("my main")
    # Get the arguments list
    cmdargs = sys.argv
    '''
    1- retrieve the whole carrefour prducts from mongo
    2- loop into all products, if "ingredients" field of mongo db product is equal to the new parsed product then and if ia-ingredients is empty, then add this product into the batch file.
    3- send batch file to open ia
    4- retrieve batches and send them to mongo db
    5- add a worker that listens to any changes inisde mongo db (products or users), if there is then chromaDB should import the newt list
    Work will notify chromadb and rec. sys

    cold start problem: 
    recommendation qutodienne: si a visitor without account then we will display top rating products.
    otherise, recommendation selon l'historique .

    if 2 products are belong to two different ailes then wer chousl add both aisles to the existing product 
    '''
    # Print it
    print(f"The total numbers of args passed to the script: {
          len(cmdargs)}, Args list: + {cmdargs}")
    # first arg section, second arg aisle
    if len(cmdargs) > 1:
        aisles: List[StaticAisle] = get_static_aisles_from_user_cmdargs(
            cmdargs=cmdargs)
        print(f"aisles: {len(aisles)}")
        if not aisles:
            print("empty aisles")
            sys.exit()
        for aisle in aisles:
            print(f"selected aisle: {aisle.name}, original_file_uri: {
                  aisle.original_file_uri}")
            if not aisle.created_from_file:
                folder = extract_folder_path(file_path=aisle.original_file_uri)
                file_name = extract_file_name(file_path=aisle.original_file_uri)

                # extract all files in folder containg "details"
                files = get_files_with_substring_ordered_by_mtime(
                    folder_path=folder, substring=f"{file_name.lower()}")
                print(f"folder: {folder}")
                print(f"files: {files}")                
                # for now we should limit the files to 2 since we have only two parsing dates
                # and to avoid sending a lot of useless iA queries and db queries
                files = files[:1]
            else:
                files = [aisle.original_file_uri]

            if "get_latest_parsed_products" in cmdargs:
                files = files[0]
                print(f"get_latest_parsed_products found, files:{files}")
            mongo_products: List[Product] | None = None
            if "by_category" in cmdargs:
                index = cmdargs.index(
                    "by_category")
                if len(cmdargs) > index + 1:
                    category_id = int(cmdargs[index + 1])
                    mongo_products = get_all_products_from_mongodb_by_category_with_ia_ingredient(
                        category_id=category_id)
                    # now check if one of these products don't have an ia_ingredients then search for it via open ia
                    # or do the opposit,
                else:
                    raise NameError(
                        "fatal error, by_category should be followed by category_id")
            # if by_category is not mentioned then retrieve category from aisle
            # we can achieve this by retrieving the common category id of the whole product List
            if not mongo_products:
                pass

            last_common_category_id = -1
            for file in files or []:
                print(f"file to upload: {file}")
                json_file = open(file, encoding='utf-8') if file else None
                products = json.load(json_file) if json_file else []
                category_id = get_most_common_category_id(products=products)
                if not "by_category" in cmdargs and last_common_category_id != category_id:
                    last_common_category_id = category_id
                    mongo_products = get_all_products_from_mongodb_by_category_with_ia_ingredient(
                        category_id=category_id)
                    
                productsV2: List[Product] = []
                for product in products:
                    product = dacite.from_dict(
                        data_class=Product, data=product, config=dacite.Config(strict=True))
                    # TODO: todo task
                    '''
                    from mongo_products get mongo_product having product.ean, 
                    if mongo_product has ia_ingredient then skip it otherwise query open ia
                    '''
                    all_mongo_products_ean = [
                        product1.ean for product1 in mongo_products] if mongo_products else []

                    if product.ean not in all_mongo_products_ean:
                        evolsV2: List[Evolution] = []
                        for evol in product.evolutions or []:
                            if evol.ingredients and len(evol.ingredients) > 2:
                                print(f"ean without ia_ingredients: {product.ean}")
                                # Assign the cleaned ingredients back to the 'ingredients_ia' key as a list
                                # very aweful example: https://www.carrefour.fr/p/gaspacho-espagnol-3665549084866?s=2122&t=28548
                                # ingredients = "mes ou « Gazpacho ».\n\nIngrédients :\nTomate (71 %), poivron (5 %), concombre (5 %), oignon (5 %), huile d'olive, vina"
                                ingredients = evol.ingredients.replace(
                                    "\n", ",").strip()
                                ingredients = ingredients.lower()
                                ingredients = keep_text_after(
                                    text=ingredients, keyword="ingrédients:")
                                ingredients = keep_text_after(
                                    text=ingredients, keyword="ingrédients :")
                                ingredients = remove_keyword_if_first(
                                    text=ingredients, keyword=": ")
                                ingredients = ingredients.replace(
                                    "&", ", ").replace(" et", ",").strip()
                                ingredients = remove_substrings_and_clean(
                                    ingredients, substrings=ProductContentDia.INGREDIENTS_SUBSTRINGS)
                                ingredients = rephrase_text_if_parenthesis_exists(
                                    ingredients)
                                evol.ingredients_clean = remove_extra_dots(
                                    ingredients) if len(ingredients) > 2 else None
                                ingredients_ia = clean_ingredients(evol.ingredients_clean)
                                # Iterate over each text in the list and apply the replace function
                                # not used ingredients_ia = [replace_text_with_first_matching_keyword(text, iA_keywords_for_ingredients_groups) for text in ingredients_ia]
                                ingredients_ia = remove_keywords_and_empty_texts(
                                    texts=ingredients_ia, keywords=iA_keywords_to_remove) if ingredients_ia else None
                                evol.ingredients_ia = ingredients_ia

                            evolsV2.append(evol)
                        product.evolutions = evolsV2
                    productsV2.append(product)
                print(f"len productsV2: {len(productsV2)}")
                cleaned_file_path = file.replace(
                    ".json", "").replace("_detailed", "_iAdetailed")
                json_object = json.dumps(productsV2,
                                         default=lambda o: dict(
                                             (key, value) for key, value in o.__dict__.items() if value is not None),
                                         indent=4,
                                         allow_nan=False,
                                         ensure_ascii=False)
                write_output_to_file(data=json_object, file_name=cleaned_file_path,
                                     path_includes_in_file_name=True, include_seconds_in_date=False, extension='.json')
    else:
        print("wrong args number")
        sys.exit()