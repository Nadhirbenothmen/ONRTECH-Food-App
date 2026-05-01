# 🛒 Mercadona Product Enrichment Pipeline

Ce projet vise à automatiser la collecte, la transformation, l’enrichissement et l’insertion de produits Mercadona dans une base de données MongoDB, à l’aide de modèles LLM locaux via Ollama.

---

## ⚙️ Prérequis

- **Python** ≥ 3.12  
- **Ollama** installé et fonctionnel localement  
  Exemples :
  - `ollama run mistral`
  - `ollama run llama3`
- **MongoDB** configuré (local ou distant)

---

## 🔧 Installation

```bash
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
```

---

## 🧱 Étape 1 — Préparation des données statiques

Avant le scraping, un fichier de données statiques (type `StaticAisle`) est préparé manuellement. Il contient la hiérarchie des catégories produits Mercadona (rayons, sous-catégories, etc.), utilisée pour organiser et contextualiser les produits.

---

## 🛰️ Étape 2 — Scraping des produits Mercadona

Ce script permet de collecter les produits depuis le site Mercadona, en fonction d’une catégorie ou d’une sous-catégorie, puis de les transformer selon un format JSON unifié.

### ▶️ Lancer le scraping :

```bash
# Lancer tous les produits d'une catégorie complète :
.venv/Scripts/python.exe C:/PFE_ONRTECH/Project_PFE/VN_parsers2/src/countries/spain/MercadonaV3/robots/mercadona_aisles_products_scanner.py MercadonaSugarSweetsChocolateAlimentations

# Lancer seulement un aisle spécifique :
.venv/Scripts/python.exe C:/PFE_ONRTECH/Project_PFE/VN_parsers2/src/countries/spain/MercadonaV3/robots/mercadona_aisles_products_scanner.py MercadonaSugarSweetsChocolateAlimentations --only_one_aisle SUGAR_AND_SWEETENERS
```

📁 Les fichiers `.json` générés sont placés dans `robots/products/`.

---

## 🤖 Étape 3 — Enrichissement IA des produits

Ce script utilise un modèle LLM (via Ollama) pour enrichir chaque produit avec :
- une **liste nettoyée d'ingrédients**
- une **traduction IA vers l'anglais**
- des **valeurs nutritionnelles estimées**

Un cache (`mercadona_cache_enrichment.json`) est utilisé pour éviter les appels redondants à l’IA.

### ▶️ Lancer l’enrichissement :

```bash
.venv/Scripts/python.exe C:/PFE_ONRTECH/Project_PFE/VN_parsers2/src/countries/spain/MercadonaV3/robots/mercadona_IA_ingredients.py

.venv/Scripts/python.exe C:/PFE_ONRTECH/Project_PFE/VN_parsers2/src/countries/spain/MercadonaV3/robots/calculate_nutriscore.py

.venv/Scripts/python.exe C:/PFE_ONRTECH/Project_PFE/VN_parsers2/src/countries/spain/MercadonaV3/robots/mercadona_ia_enrichment.py

#Nettoyage des fichier Json Final pour BI 
.venv/Scripts/python.exe C:/PFE_ONRTECH/Project_PFE/VN_parsers2/src/countries/spain/MercadonaV3/robots/NettoyageBI.py

```

⏳ Le script vous demande ensuite :

- Le chemin vers :
  - un **dossier** (ex. `src/countries/spain/MercadonaV3/robots/products`)
  - un **sous-dossier** (ex. `src/countries/spain/MercadonaV3/robots/products/Baby`)
  - un ou plusieurs **fichiers JSON** séparés par virgule

📄 Les fichiers enrichis seront nommés `*_iAdetailed_<timestamp>.json`.

---

## ⬆️ Étape 4 — Upload vers MongoDB

Ce script lit les fichiers enrichis, valide leur contenu, et les insère ou met à jour dans MongoDB à l’aide d’un `CreateOrUpdateEvolutionUseCase`.

### ▶️ Lancer l’upload :

```bash
.venv/Scripts/python.exe src/countries/spain/MercadonaV3/db/mercadona_uploader.py src/countries/spain/MercadonaV3/robots/products/
```

Il parcourt tous les fichiers contenant `_iAdetailed.json`, traite chaque produit et envoie les données vers MongoDB.

---

## 🧠 Cache IA (`cache_enrichment.json`)

Le cache contient les enrichissements IA pour chaque combinaison `titre + poids`, afin d’éviter des appels inutiles à Ollama.

### 🔄 Pour vider le cache :

```bash
del cache_enrichment.json  # Windows
rm cache_enrichment.json   # Linux / macOS
```
---

## 👨‍💻 Auteur

- **Nadhir** — Projet de fin d'études (PFE), Data & AI @ ONRTECH – 2025
