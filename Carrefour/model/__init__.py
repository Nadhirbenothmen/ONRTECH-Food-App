import datetime
import json
from dataclasses import dataclass
import os
from pathlib import Path
from typing import List, Optional

import dacite

from src.model.static_category_aisle import StaticAisle, StaticCategory
from src.utils.my_utils import get_latest_file_in_folder
print("fom model init get brands latest file...")
#folder_path = f"{Path.cwd()}/src/countries/france/carrefour/robots/brands"
current_working_dir = os.getcwd()  # or Path.cwd() for pathlib
folder_path = f"{current_working_dir}/src/countries/france/carrefour/robots/brands"
brands_latest_file = get_latest_file_in_folder(
    folder_path=folder_path, file_name_prefix="brands", during_last_x_days=150)
print(current_working_dir)
print(f"brands_latest_file:{brands_latest_file}, folder_path:{folder_path}")
brands_file = open(brands_latest_file, encoding='utf-8')
categories_with_brands = json.load(brands_file)

all_categories: List[StaticCategory] = [dacite.from_dict(data_class=StaticCategory, data=obj, config=dacite.Config(strict=True)) for obj in categories_with_brands]

all_aisles: List[str] = []
all_brands: List[str] = []
for cat in all_categories:
    # print(f"cat.name: {cat.name}, aisles: {str(len(cat.aisles))}")
    all_aisles.extend(cat.aisles)
    for ray in cat.aisles:
        all_brands.extend(ray.brands)
# print(f"all_brands.count: {len(all_brands)}")
# print(f"all_aisles.count: {len(all_aisles)}")
