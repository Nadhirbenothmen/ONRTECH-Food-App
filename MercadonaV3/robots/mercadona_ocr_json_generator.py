import json
import pytesseract
import requests
from PIL import Image
from io import BytesIO
import cv2
import numpy as np
import re
import os

# Décommente si nécessaire
# pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def download_image(url):
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content)).convert("RGB")
        return img
    except Exception as e:
        print(f"❌ Erreur téléchargement image : {url} | {e}")
        return None

def ocr_image_to_text(pil_img):
    open_cv_image = np.array(pil_img)
    gray = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2GRAY)
    text = pytesseract.image_to_string(gray, lang='spa')
    print("\n📂 TEXTE OCR BRUT:\n", text)
    return text

def detect_labels_from_text(text: str) -> dict:
    text = text.lower()
    return {
        "bio": any(word in text for word in ["ecológico", "biológico", "bio"]),
        "vegan": any(word in text for word in ["vegano", "100% vegetal", "vegetal"]),
        "gluten_free": "sin gluten" in text,
        "halal": "halal" in text,
        "kosher": "kosher" in text,
        "lactose_free": "sin lactosa" in text,
        "sugar_free": "sin azuc" in text.replace("ú", "u"),
        "additive_free": "sin conservantes" in text or "sin aditivos" in text
    }

def parse_text_to_json(ocr_text: str, ean: str, title: str, brand: str) -> dict:
    text = ocr_text.lower()

    data = {
        "ean": ean,
        "title": title,
        "brand": brand,
        "distributor": "Mercadona",
        "manufacturer": {"name": None, "address": None},
        "origin": {"ean": []},
        "ingredients": None,
        "storage": None,
        "nutrition": {
            "per": "100ml",
            "energy_kj": None,
            "energy_kcal": None,
            "fat": None,
            "saturated_fat": None,
            "carbohydrates": None,
            "sugars": None,
            "proteins": None,
            "salt": None
        },
        "vitamins": {},
        "labels": detect_labels_from_text(text),
        "price_per_kg": None,
        "net_weight": None
    }

    match = re.search(r"ingredientes\s*[:\-]?\s*(.*?)(conservaci[oó]n|mantener|mantenimiento)", text, re.DOTALL)
    if match:
        data["ingredients"] = re.sub(r"\s+", " ", match.group(1)).strip().capitalize()

    match = re.search(r"conservaci[oó]n\s*[:\-]?\s*(.*?)(\n|una vez abierto)", text, re.DOTALL)
    if match:
        data["storage"] = re.sub(r"\s+", " ", match.group(1)).strip().capitalize()

    nutrition_lines = []
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if re.search(r"100\s*(ml|g)", line):
            start = i
            break
    if start is not None:
        for j in range(start + 1, len(lines)):
            line = lines[j].strip().lower()
            if re.search(r"250\s*(ml|g)", line):
                break
            nutrition_lines.append(line)

    print("\n🧪 Bloc nutrition analysé (100 ml/g uniquement):")
    for l in nutrition_lines:
        print(" -", l)

    for line in nutrition_lines:
        if "kj" in line or "kcal" in line:
            kj_match = re.search(r"(\d+)\s*k?j", line)
            kcal_match = re.search(r"(\d+)\s*kcal", line)
            if kj_match:
                data["nutrition"]["energy_kj"] = int(kj_match.group(1))
            if kcal_match:
                data["nutrition"]["energy_kcal"] = int(kcal_match.group(1))
        elif "grasa" in line or "grasas" in line:
            fat = re.search(r"([\d,\.]+)", line)
            if fat:
                val = fat.group(1).replace(",", ".")
                if val != ".":
                    data["nutrition"]["fat"] = float(val)
        elif "saturad" in line:
            sat = re.search(r"([\d,\.]+)", line)
            if sat:
                val = sat.group(1).replace(",", ".")
                if val != ".":
                    data["nutrition"]["saturated_fat"] = float(val)
        elif "hidrato" in line:
            carb = re.search(r"([\d,\.]+)", line)
            if carb:
                val = carb.group(1).replace(",", ".")
                if val != ".":
                    data["nutrition"]["carbohydrates"] = float(val)
        elif "azuc" in line:
            sug = re.search(r"([\d,\.]+)", line)
            if sug:
                val = sug.group(1).replace(",", ".")
                if val != ".":
                    data["nutrition"]["sugars"] = val
        elif "prote" in line:
            prot = re.search(r"([\d,\.]+)", line)
            if prot:
                val = prot.group(1).replace(",", ".")
                if val != ".":
                    data["nutrition"]["proteins"] = float(val)
        elif "sal" in line:
            salt = re.search(r"([\d,\.]+)", line)
            if salt:
                val = salt.group(1).replace(",", ".")
                if val != ".":
                    data["nutrition"]["salt"] = float(val)
        elif "vitamina a" in line:
            va = re.search(r"vitamina a.*?(\d+[\.,]?\d*)\s*(µg|ug|mg)", line)
            if va:
                data["vitamins"]["vitamin_a"] = va.group(1).replace(",", ".") + " " + va.group(2)
        elif "vitamina c" in line:
            vc = re.search(r"vitamina c.*?(\d+[\.,]?\d*)\s*(µg|ug|mg)", line)
            if vc:
                data["vitamins"]["vitamin_c"] = vc.group(1).replace(",", ".") + " " + vc.group(2)
        elif "vitamina e" in line:
            ve = re.search(r"vitamina e.*?(\d+[\.,]?\d*)\s*(µg|ug|mg)", line)
            if ve:
                data["vitamins"]["vitamin_e"] = ve.group(1).replace(",", ".") + " " + ve.group(2)

    match = re.search(r"(fabricado por|jgc, s\\.a\\.)\s*(.*?)\s*(\d{5}\s+.*?)$", text, re.DOTALL)
    if match:
        data["manufacturer"]["name"] = match.group(1).strip().upper()
        data["manufacturer"]["address"] = match.group(3).strip().capitalize()

    if "españa" in text:
        data["origin"]["ean"].append("ES")

    match = re.search(r"(\d+)\s+raciones\s+de\s+(\d+)\s*(ml|g)", text)
    if match:
        count = int(match.group(1))
        vol = int(match.group(2))
        unit = match.group(3)
        data["net_weight"] = f"{count * vol} {unit}"

    return data


def process_mercadona_products(input_json, output_json):
    with open(input_json, "r", encoding="utf-8") as f:
        products = json.load(f)

    final_data = []

    for p in products:
        ean = p.get("ean")
        title = p.get("lang_desc", {}).get("es", {}).get("title", "")
        brand = p.get("brand", "")
        images = p.get("lang_desc", {}).get("es", {}).get("images", [])

        if len(images) >= 2:
            label_img_url = images[1]
        elif images:
            label_img_url = images[0]
        else:
            print(f"🛑 Pas d’image trouvée pour EAN {ean}")
            continue

        label_img_url = label_img_url.split("?")[0]

        print(f"\n🔍 Traitement produit {ean} | image: {label_img_url}")

        img = download_image(label_img_url)
        if not img:
            continue

        ocr_text = ocr_image_to_text(img)
        product_json = parse_text_to_json(ocr_text, ean, title, brand)
        final_data.append(product_json)

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Fichier JSON généré : {output_json}")

# === Exécution interactive
if __name__ == "__main__":
    input_path = input("📂 Entrez le chemin du fichier JSON d’entrée (scraping Mercadona) : ").strip()
    output_path = input("📥 Entrez le chemin du fichier de sortie souhaité : ").strip()

    if not input_path:
        print("❌ Aucun fichier d’entrée fourni.")
    else:
        process_mercadona_products(input_path, output_path or "mercadona_structured_from_ocr.json")