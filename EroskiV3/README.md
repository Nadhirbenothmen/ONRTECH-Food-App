
# 🛒 Eroski Product Enrichment Pipeline

Ce projet automatise la collecte, le traitement, l’enrichissement et le chargement des produits du site Eroski dans une base MongoDB, avec l’aide de modèles LLM exécutés localement via **Ollama**.

---

## ⚙️ Prérequis

- **Python** ≥ 3.12  
- **Ollama** installé et actif localement :  
  - `ollama run mistral`  
  - `ollama run llama3`
- **MongoDB** accessible et configurée (localement ou à distance)

---

## 🔧 Installation

```bash
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
```

---

## 🧱 Étape 1 — Données statiques (hiérarchie Eroski)

Avant tout scraping, un fichier `StaticAisle` est préparé. Il contient la hiérarchie des rayons, sous-rayons et catégories du site **Eroski**, servant de référence pour organiser les données collectées.

---

## 🛰️ Étape 2 — Scraping des produits Eroski

Ce script collecte les fiches produits à partir du site **Eroski**, en ciblant une catégorie complète ou un rayon spécifique, et convertit les données dans un format JSON structuré.

### ▶️ Lancer le scraping :

```bash
# Pour lancer l'extraction complète d'une catégorie :
.venv/Scripts/python.exe src/countries/spain/EroskiV3/robots/eroski_aisles_products_scanner.py EroskiFeedingOilVinegarSaltFlourAndBreadcrumbsAlimentations

# Pour ne scraper qu’un rayon spécifique :
.venv/Scripts/python.exe src/countries/spain/EroskiV3/robots/eroski_aisles_products_scanner.py EroskiFeedingOilVinegarSaltFlourAndBreadcrumbsAlimentations --only_one_aisle SUNFLOWER_OIL


.venv/Scripts/python.exe src/countries/spain/EroskiV3/robots/eroski_calculate_nutriscore.py

.venv/Scripts/python.exe src/countries/spain/EroskiV3/robots/eroski_nettoyageBI.py

```

📁 Les fichiers `.json` sont ensuite enregistrés dans `robots/products/`.

---

## 🤖 Étape 3 — Enrichissement IA des produits

Le script d'enrichissement utilise un modèle LLM (via **Ollama**) pour analyser et compléter chaque produit avec :
- une **liste nettoyée des ingrédients**
- une **traduction en anglais**
- des **valeurs nutritionnelles estimées**

Un cache `eroski_cache_enrichment.json` évite les appels redondants à l’IA.

### ▶️ Lancer l’enrichissement :

```bash
.venv/Scripts/python.exe src/countries/spain/EroskiV3/robots/eroski_IA_ingredients.py

.venv/Scripts/python.exe src/countries/spain/EroskiV3/robots/eroski_ia_enrichment.py

```

💬 Le script vous demandera de spécifier :
- un **dossier complet**
- un **sous-dossier**
- ou un ou plusieurs fichiers JSON séparés par des virgules

🗃️ Les fichiers enrichis seront nommés automatiquement avec un timestamp :  
`*_iAdetailed.json`

---

## ⬆️ Étape 4 — Upload vers MongoDB

Ce script lit les fichiers enrichis, applique les règles de validation, et insère ou met à jour les documents dans MongoDB à l’aide d’un `CreateOrUpdateEvolutionUseCase`.

### ▶️ Lancer l’upload :

```bash
.venv/Scripts/python.exe src/countries/spain/EroskiV3/db/eroski_uploader.py src/countries/spain/EroskiV3/robots/products/
```

🔁 Tous les fichiers contenant `_iAdetailed.json` seront automatiquement détectés et traités.

---

## 🧠 Cache IA (`eroski_cache_enrichment.json`)

Le cache enregistre les enrichissements réalisés par Ollama pour chaque produit (clé = `title + poids`).  
Cela permet de relancer le script sans refaire les requêtes IA déjà effectuées.

### 🔄 Vider manuellement le cache :

```bash
del eroski_cache_enrichment.json  # Windows
rm eroski_cache_enrichment.json   # Linux / macOS
```
---

## 👨‍💻 Auteur

- **Nadhir** — Projet de fin d’études (PFE), Data & AI @ ONRTECH – 2025


.venv/Scripts/python.exe src/countries/spain/EroskiV3/robots/predict.py src/countries/spain/EroskiV3/robots/missing_ingredients_ia_v2.json