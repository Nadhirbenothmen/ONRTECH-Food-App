# 🛒 Dia Product Enrichment Pipeline

Ce projet automatise l'extraction, la transformation, l'enrichissement par IA, et le chargement des produits depuis le site **Dia** vers une base MongoDB. Il exploite des modèles LLM (comme Mistral ou LLaMA3) exécutés en local via **Ollama**.

---

## ⚙️ Prérequis

- **Python** ≥ 3.12  
- **Ollama** installé et lancé localement :  
  - `ollama run mistral`  
  - ou `ollama run llama3`
- **MongoDB** accessible (en local ou à distance)

---

## 🔧 Installation

```bash
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
```

---

## 🧱 Étape 1 — Hiérarchie des catégories (static)

Avant de scraper les produits, un fichier `StaticAisle` est construit pour refléter la structure hiérarchique des rayons et sous-rayons du site **Dia**. Ce fichier est utilisé comme référence lors du scraping et de l'organisation des données.

---

## 🛰️ Étape 2 — Scraping des produits Dia

Le script récupère les informations produits directement depuis le site **Dia**, pour une catégorie complète ou un rayon spécifique, et les structure dans un format JSON unifié.

### ▶️ Commandes pour lancer le scraping :

```bash
# Scraper une catégorie complète :
.venv/Scripts/python.exe src/countries/spain/DiaV3/robots/dia_aisles_products_scanner.py DiaAirFryerAlimentations

# Scraper un seul rayon :
.venv/Scripts/python.exe src/countries/spain/DiaV3/robots/dia_aisles_products_scanner.py DiaAirFryerAlimentations --only_one_aisle AIR_FRYER_POTATOES

.venv/Scripts/python.exe src/countries/spain/DiaV3/robots/dia_calculate_nutriscore.py
```

🗂️ Les fichiers `.json` générés seront enregistrés dans `robots/products/`.

---

## 🤖 Étape 3 — Enrichissement IA

Chaque produit collecté est enrichi avec :
- des **ingrédients nettoyés**
- une **traduction en anglais**
- une estimation des **valeurs nutritionnelles**

Le modèle IA utilisé est exécuté via Ollama, et un fichier cache `dia_cache_enrichment.json` est utilisé pour éviter les appels répétés.

### ▶️ Lancer l’enrichissement IA :

```bash
.venv/Scripts/python.exe src/countries/spain/DiaV3/robots/dia_IA_ingredients.py

#Enrichment IA 
.venv/Scripts/python.exe src/countries/spain/DiaV3/robots/dia_ia_enrichment.py

.venv/Scripts/python.exe src/countries/spain/DiaV3/robots/dia_nettoyageBI.py

```

💬 Le script demande ensuite de spécifier :
- un dossier complet
- un sous-dossier
- ou un ou plusieurs fichiers `.json` séparés par virgule

📝 Les fichiers enrichis seront sauvegardés avec le suffixe :  
`*_iAdetailed.json`

---

## ⬆️ Étape 4 — Upload MongoDB

Le script final lit les fichiers enrichis et insère les produits dans la base de données MongoDB en appliquant les règles métiers via le `CreateOrUpdateEvolutionUseCase`.

### ▶️ Commande pour lancer l’upload :

```bash
.venv/Scripts/python.exe src/countries/spain/DiaV3/db/dia_uploader.py src/countries/spain/DiaV3/robots/products/
```

🔍 Tous les fichiers contenant `_iAdetailed.json` seront automatiquement détectés et traités.

---

## 🧠 Cache IA (`dia_cache_enrichment.json`)

Le cache mémorise les réponses IA pour chaque produit (identifié par titre + poids), permettant de relancer l’enrichissement sans duplication d'appels.

### 🗑️ Vider le cache manuellement :

```bash
del dia_cache_enrichment.json  # Windows
rm dia_cache_enrichment.json   # Linux / macOS
```

---

## 👨‍💻 Auteur

- **Nadhir** — Projet de fin d’études (PFE), Data & AI @ ONRTECH – 2025
