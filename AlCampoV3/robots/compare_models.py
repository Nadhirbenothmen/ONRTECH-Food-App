import json
import glob
import os

# --- Utils ---
def normalize(lst):
    return sorted(set(x.lower().strip() for x in lst if x and isinstance(x, str)))

def compare_lists(gt, pred):
    gt_set, pred_set = set(gt), set(pred)
    tp = len(gt_set & pred_set)
    fp = len(pred_set - gt_set)
    fn = len(gt_set - pred_set)

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    jaccard = tp / len(gt_set | pred_set) if (gt_set | pred_set) else 0
    exact_match = int(gt_set == pred_set)

    return {
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }

def avg_metrics(results):
    return {k: sum(r[k] for r in results)/len(results) for k in results[0]}

# --- Paths ---
ref_file = r"src\countries\spain\AlCampoV3\robots\All_products_reference_complete.json"
base_dir = r"src\countries\spain\AlCampoV3\robots\products\Baby_Infant_nutrition"

# Charger référence
with open(ref_file, encoding="utf-8") as f:
    ref_data = {p["ean"]: p for p in json.load(f)}

# Chercher fichiers HF et iA dans le dossier
hf_files = glob.glob(os.path.join(base_dir, "*_HFdetailed*.json"))
ia_files = glob.glob(os.path.join(base_dir, "*_iAdetailed*.json"))

# Associer par préfixe
def get_prefix(fname):
    if "_HFdetailed" in fname:
        return os.path.basename(fname).split("_HFdetailed")[0]
    elif "_iAdetailed" in fname:
        return os.path.basename(fname).split("_iAdetailed")[0]
    return None

hf_map = {get_prefix(f): f for f in hf_files}
ia_map = {get_prefix(f): f for f in ia_files}

common_prefixes = set(hf_map.keys()) & set(ia_map.keys())

results_hf, results_ia = [], []

# Comparer pour chaque paire
for prefix in common_prefixes:
    with open(hf_map[prefix], encoding="utf-8") as f:
        hf_data = {p["ean"]: p for p in json.load(f)}
    with open(ia_map[prefix], encoding="utf-8") as f:
        ia_data = {p["ean"]: p for p in json.load(f)}

    common_eans = set(ref_data.keys()) & set(hf_data.keys()) & set(ia_data.keys())

    for ean in common_eans:
        ref_ing = normalize(ref_data[ean].get("ingredients_ia", []))
        hf_ing  = normalize(hf_data[ean]["evolutions"][0].get("ingredients_ia", []))
        ia_ing  = normalize(ia_data[ean]["evolutions"][0].get("ingredients_ia", []))

        if ref_ing:
            results_hf.append(compare_lists(ref_ing, hf_ing))
            results_ia.append(compare_lists(ref_ing, ia_ing))

# Résultats globaux
if results_hf:
    total_hf = avg_metrics(results_hf)
    print("📊 Résultats globaux HF :")
    for k, v in total_hf.items():
        print(f"{k:15s}: {v:.3f}")

if results_ia:
    total_ia = avg_metrics(results_ia)
    print("\n📊 Résultats globaux Llama3 :")
    for k, v in total_ia.items():
        print(f"{k:15s}: {v:.3f}")
