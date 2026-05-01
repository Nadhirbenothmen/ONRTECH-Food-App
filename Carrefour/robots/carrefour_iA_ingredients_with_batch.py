# check if the given argument is aan aisle or a path
# if it is a path then check if it is a folder or a file
# if file, then return a list with file as a unique item
# if folder, then return a list of files (havind "details" substring)

# read the list of files one by one and load its content.
# the content if a list of products. for each product call the func A()

import json
import sys
from typing import List

import dacite

from src.countries.france.carrefour.model.product_content_carrefour import ProductContentCarrefour
from src.utils.iA_ingredients import clean_ingredients, replace_text_with_first_matching_keyword
from src.model.product import Evolution, Product
from src.utils.my_utils import extract_file_name, extract_folder_path, get_files_with_substring_ordered_by_mtime, keep_text_after, remove_extra_dots, remove_keyword_if_first, remove_keywords_and_empty_texts, remove_substrings_and_clean, rephrase_text_if_parenthesis_exists, write_output_to_file
from src.countries.france.carrefour.robots.carrefour_static_ailes import get_static_aisles_from_user_cmdargs
from src.model.static_category_aisle import StaticAisle
from src.model.product_content import iA_keywords_for_ingredients_groups, iA_keywords_to_remove

if __name__ == "__main__":
    print("my main")
    # Get the arguments list
    cmdargs = sys.argv

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
        for aisle1 in aisles:
            aisle: StaticAisle = aisle1
            print(f"aisle to upload: {aisle.name}, original_file_uri: {
                  aisle.original_file_uri}")
            
            folder: str | None = extract_folder_path(file_path=aisle.original_file_uri)
            file_name: str | None = extract_file_name(
                file_path=aisle.original_file_uri)

            # extract all files in folder containg "details"
            files = get_files_with_substring_ordered_by_mtime(
                folder_path=folder, substring=f"{file_name.lower()}_detailed")
            print(f"folder: {folder}")
            print(f"files: {files}")
            # for now we should limit the files to 2 since we have only two parsing dates
            # and to avoid sending a lot of useless iA queries and db queries
            files = files[:2]
            if "get_latest_parsed_products" in cmdargs:
                files = files[0]
                print(f"get_latest_parsed_products found, files:{files}")
            for file in files:
                print(f"file to upload: {file}")
                json_file = open(file, encoding='utf-8')
                products = json.load(json_file)
                productsV2: List[Product] = []
                for product in products:
                    product = dacite.from_dict(
                        data_class=Product, data=product, config=dacite.Config(strict=True))
                    # if product.ean != "8445225121758":
                    #    continue
                    evolsV2: List[Evolution] = []
                    for evol in product.evolutions or []:
                        if evol.ingredients and len(evol.ingredients) > 2:
                            print(f"ean: {product.ean}")
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
                                ingredients, substrings=ProductContentCarrefour.INGREDIENTS_SUBSTRINGS)
                            ingredients = rephrase_text_if_parenthesis_exists(
                                ingredients)
                            evol.ingredients_clean = remove_extra_dots(
                                ingredients) if len(ingredients) > 2 else None
                            # ingredients_ia = clean_ingredients(evol.ingredients_clean)
                            # Iterate over each text in the list and apply the replace function
                            # not used ingredients_ia = [replace_text_with_first_matching_keyword(text, iA_keywords_for_ingredients_groups) for text in ingredients_ia]
                            # ingredients_ia = remove_keywords_and_empty_texts(texts=ingredients_ia, keywords=iA_keywords_to_remove)
                            # evol.ingredients_ia = ingredients_ia

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
