import json
import sys
from typing import List

from src.countries.france.carrefour.robots import carrefour_static_ailes
from src.model.static_category_aisle import StaticAisle
from src.utils.my_utils import write_output_to_file

class MinifyOriginalJSONList:
    def __init__(self):
        self.total_products_number = 0
        self.firstAccess = True
        self.brands = []

    def get_products_from_json(self, file_uri: str):
        product_data_list = []
        # Opening JSON file with
        json_file = open(file_uri, encoding='UTF-8')
        # all pages of 30 products each
        all_pages = json.load(json_file)

        # Print the data of dictionary
        for page in all_pages:
            page_data = page["data"]
            for product in page_data:
                product_data = product["attributes"]
                product_data_dict = dict(product_data)
                if product_data_dict["businessType"] == "non-food":
                    continue

                categories = product_data_dict["categories"]
                exclude_labels = ["Plats bébé",
                                  "Tétines", "Biberons et Accessoires"]
                exclude_product = False
                # Filter by categories:
                for category in categories:
                    label = category.get("label")
                    if label in exclude_labels:
                        exclude_product = True
                if exclude_product:
                    continue
                # reduce categories:
                new_categories_structure = []
                for category in categories:
                    category.pop('level', None)
                    category.pop('code', None)
                    category.pop('type', None)
                    category.pop('sellerId', None)
                    category.pop('slug', None)
                    category.pop('uri', None)
                    new_categories_structure.append(category)
                product_data_dict["categories"] = new_categories_structure

                product_data_dict.pop('moreOffers', None)
                # product_data_dict.pop('offers', None)
                product_data_dict.pop('guarantee_general_document', None)
                product_data_dict.pop('flags', None)
                product_data_dict.pop('isDonation', None)
                product_data_dict.pop('isBestSeller', None)
                product_data_dict.pop('traceability', None)
                product_data_dict.pop('isRecoverable', None)
                product_data_dict.pop('keyFeatures', None)
                product_data_dict.pop('clubs', None)
                product_data_dict.pop('variants', None)
                product_data_dict.pop('uri', None)
                product_data_dict.pop('slug', None)
                product_data_dict.pop('topCategoryName', None)

                print(f"product_data_dict: {product_data_dict}")

                imageLargest = product_data_dict["images"]["formats"]["largest"]
                imagePaths = product_data_dict["images"]["paths"]
                new_image_paths: List[str] = []
                for imagePath in imagePaths:
                    imagePath1 = str(imagePath)
                    imagePath1 = imagePath1.replace(
                        "p_FORMAT", "p_" + imageLargest)
                    new_image_paths.append(imagePath1)
                product_data_dict["new_images"] = new_image_paths
                product_data_dict.pop('images', None)
                product_data_dict["links"] = product["links"]

                # reduce offers:
                ean = product_data_dict["ean"]
                offerServiceId = product_data_dict["offerServiceId"]
                offer = product_data_dict["offers"][ean][offerServiceId]["attributes"]

                # availability
                availability_tree = offer["availability"]
                product_data_dict["availability"] = True if availability_tree["purchasable"] is True and availability_tree[
                    "stopped"] is False and availability_tree["suspended"] is False else False

                price = offer["price"]["price"]
                unit_of_mesure = offer["price"]["unitOfMeasure"]
                perUnit = offer["price"]["perUnit"]

                weightsAndMeasures: list = product_data["weightsAndMeasures"]
                weightsAndMeasures = weightsAndMeasures if len(
                    weightsAndMeasures) > 0 else None
                product_data_dict = self.add_key_value_to_dict(
                    product_data_dict, "weightsAndMeasures", weightsAndMeasures)

                brand_carrefour_found = "carrefour" in product_data["title"].lower(
                )
                brand = product_data["brand"]
                brand = brand if brand is not None else "carrefour" if brand_carrefour_found is True else None
                product_data_dict = self.add_key_value_to_dict(
                    product_data_dict, "brand", brand)
                product_data_dict = self.add_key_value_to_dict(
                    product_data_dict, "price", price)
                product_data_dict = self.add_key_value_to_dict(
                    product_data_dict, "unit_of_mesure", unit_of_mesure)
                product_data_dict = self.add_key_value_to_dict(
                    product_data_dict, "perUnit", perUnit)

                freshness_value = offer["freshness"]["value"] if offer["freshness"] is not None else None
                freshness_period = offer["freshness"]["period"] if offer["freshness"] is not None else None
                product_data_dict = self.add_key_value_to_dict(
                    product_data_dict, "freshness_value", freshness_value)
                product_data_dict = self.add_key_value_to_dict(
                    product_data_dict, "freshness_period", freshness_period)

                product_data_dict.pop('offers', None)

                # reduce nuttriscore
                nutriscore = product_data_dict["nutriscore"]["value"] if product_data_dict["nutriscore"] is not None else None
                product_data_dict = self.add_key_value_to_dict(
                    product_data_dict, "nutriscore", nutriscore)

                # customerReviews
                reviews = product_data_dict["customerReviews"][
                    "average"] if product_data_dict["customerReviews"] is not None else None
                print(f"reviews: {reviews}")
                product_data_dict = self.add_key_value_to_dict(
                    product_data_dict, "customerReviews", product_data_dict["customerReviews"] if reviews is not None else None)

                # print(product_data_dict)
                product_data_list.append(product_data_dict)

        return product_data_list

    def add_key_value_to_dict(self, my_dict: dict, key: str, value: str | None) -> dict:
        if value is None:
            my_dict.pop(key, None)
            return my_dict
        else:
            my_dict[key] = value
            return my_dict

    def fix_JSON(self, json_message=None):
        result = None
        try:
            result = json.loads(json_message) if json_message else None
        except Exception as e:
            # Find the offending character index:
            idx_to_replace = int(str(e).split(' ')[-1].replace(')', ''))
            # Remove the offending character:
            json_message = list(json_message) if json_message else None
            json_message[idx_to_replace] = ' '
            new_message = ''.join(json_message)
            return self.fix_JSON(json_message=new_message)
        return result


if __name__ == "__main__":
    # Get the arguments list
    cmdargs = sys.argv
    if len(cmdargs) == 2:
        formatter = MinifyOriginalJSONList()
        aisles = carrefour_static_ailes.get_static_aisles_from_user_cmdargs(
            cmdargs=cmdargs)
        print(f"aisles count: {len(aisles)}")
        # json_object1 = json.dumps(aisles[0])
        # print("json_object1: " + str(json_object1))
        print(f"aisles[0]: {aisles[0]}")
        for aisle in aisles:
            aisle1: StaticAisle = aisle
            print(f"aisle.original_file_uri: {aisle.original_file_uri}")
            print(f"aisle1: {aisle1}")
            file_uri = aisle1.original_file_uri  # aisle["heavy_file_uri"]
            file_uri_output = file_uri.replace(".json", "") if file_uri else None
            print(f"original_file_uri: {aisle1.original_file_uri}, file_uri_output: {file_uri_output}")
            products_data = formatter.get_products_from_json(file_uri) if file_uri or None  
            print(f"product_data_list length: {len(products_data)}, url: {file_uri_output}")
            json_object = json.dumps(products_data, ensure_ascii=False)
            write_output_to_file(json_object, file_name=file_uri_output, path_includes_in_file_name=True,
                                 add_file_date=True, include_seconds_in_date=False, extension='.json')

    else:
        print("wrong args number")
        sys.exit()
