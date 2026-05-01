# 🛒 Alcampo Product Enrichment Pipeline

Ce projet permet d'automatiser l'extraction, la transformation, l'enrichissement et l'insertion des produits du site **Alcampo** dans une base MongoDB, avec l'aide de modèles LLM locaux exécutés via **Ollama**.

---

## ⚙️ Prérequis

- **Python** ≥ 3.12  
- **Ollama** installé et actif localement :  
  - `ollama run mistral`  
  - `ollama run llama3`
- **MongoDB** opérationnelle (locale ou distante)

---

## 🔧 Installation

```bash
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
```

---

## 🧱 Étape 1 — Données statiques Alcampo

Un fichier `StaticAisle` est préparé pour représenter la hiérarchie des catégories Alcampo (rayons, sous-rayons, types).  
Il sert de référence pour structurer les produits pendant le scraping.

---

## 🛰️ Étape 2 — Scraping des produits Alcampo

Un script dédié collecte les fiches produits depuis le site Alcampo, par catégorie ou rayon.  
Les produits sont convertis dans un format JSON structuré compatible avec l’enrichissement.

### ▶️ Lancer le scraping :

```bash
# Pour lancer l'extraction complète d'une catégorie :
.venv/Scripts/python.exe src/countries/spain/AlcampoV3/robots/alcampo_aisles_products_scanner.py AlcampoFrescoesFruitsAlimentations

# Pour extraire un seul rayon spécifique :
.venv/Scripts/python.exe src/countries/spain/AlcampoV3/robots/alcampo_aisles_products_scanner.py AlcampoFrescoesFruitsAlimentations --only_one_aisle PLANTAINS_AND_BANANAS

.venv/Scripts/python.exe src/countries/spain/AlcampoV3/robots/calculate_nutriscore.py
```

📁 Les fichiers `.json` sont enregistrés dans `robots/products/`.

---

## 🤖 Étape 3 — Enrichissement IA via Ollama

Le script d'enrichissement applique un modèle LLM pour extraire :
- les **ingrédients nettoyés**
- leur **traduction anglaise**
- les **données nutritionnelles estimées**

Un cache (`alcampo_cache_enrichment.json`) stocke les résultats déjà enrichis.

### ▶️ Lancer l’enrichissement :

```bash
.venv/Scripts/python.exe src/countries/spain/AlcampoV3/robots/alcampo_IA_ingredients.py

#Enrichment IA 
.venv/Scripts/python.exe src/countries/spain/AlcampoV3/robots/alcampo_ia_enrichment.py

.venv/Scripts/python.exe src/countries/spain/AlcampoV3/robots/predict.py

.venv/Scripts/python.exe src/countries/spain/Alcampo/robots/enrich_cache.py
```

📥 Le script vous demandera le chemin :
- d’un dossier (`robots/products/`), 
- d’un sous-dossier, 
- ou d’un ou plusieurs fichiers `.json`

📄 Les fichiers enrichis seront suffixés :  
`*_iAdetailed.json`

---

## ⬆️ Étape 4 — Insertion dans MongoDB

Ce script lit les fichiers enrichis et insère ou met à jour les produits en base via le use case `CreateOrUpdateEvolutionUseCase`.

### ▶️ Lancer l’upload :

```bash
.venv/Scripts/python.exe src/countries/spain/AlcampoV3/db/alcampo_uploader.py src/countries/spain/AlcampoV3/robots/products/
```

📦 Tous les fichiers contenant `_iAdetailed.json` sont automatiquement traités.

---

## 🧠 Cache IA (`alcampo_cache_enrichment.json`)

Ce fichier permet d’éviter les appels redondants à l’IA pour un produit déjà enrichi.

### 🔄 Supprimer le cache manuellement :

```bash
del alcampo_cache_enrichment.json  # Windows
rm alcampo_cache_enrichment.json   # Linux / macOS
```

---

## 👨‍💻 Auteur

- **Nadhir** — Projet de fin d’études (PFE), Data & AI @ ONRTECH – 2025
