# count_iadetailed_products.py
import os, sys, json

def count_in_json(data):
    if isinstance(data, list):
        return len(data)
    if isinstance(data, dict):
        if isinstance(data.get("products"), list):
            return len(data["products"])
        return 1
    return 0

def main():
    if len(sys.argv) < 2:
        print("Usage: python count_iadetailed_products.py <dossier> [--debug]")
        sys.exit(1)

    root = sys.argv[1]
    debug = "--debug" in sys.argv

    total = 0
    files_scanned = 0
    files_ok = 0
    examples = []

    for dp, _, fns in os.walk(root):
        for fn in fns:
            low = fn.lower()
            # ✅ matche aussi ...iAdetailed.json_25_08_10_17_13.json
            if not (low.endswith(".json") and "iadetailed" in low):
                continue
            files_scanned += 1
            path = os.path.join(dp, fn)
            if len(examples) < 5:
                examples.append(path)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                total += count_in_json(data)
                files_ok += 1
            except Exception as e:
                print(f"⚠️  Ignoré (JSON invalide) : {path} — {e}")

    print(f"Dossier racine : {os.path.abspath(root)}")
    print(f"Fichiers scannés : {files_scanned}")
    print(f"Fichiers valides : {files_ok}")
    if debug and examples:
        print("Exemples matchés :")
        for x in examples:
            print("  -", x)
    print(f"Total produits (tous iAdetailed) : {total}")

if __name__ == "__main__":
    main()
