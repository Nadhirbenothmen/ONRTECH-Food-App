# 🍽️ ONRTECH Food Analytics

![Project Screenshot](FoodApp.png)

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-green.svg)](https://www.mongodb.com/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow.svg)](https://powerbi.microsoft.com/)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-black.svg)](https://ollama.com/)
[![License](https://img.shields.io/badge/License-Academic-orange.svg)](LICENSE)

---

## 📋 Table des Matières

- [Aperçu](#-aperçu)
- [Objectifs](#-objectifs)
- [Structure du Projet](#-structure-du-projet)
- [Technologies](#-technologies)
- [Fonctionnalités](#-fonctionnalités)
- [Pipeline ETL](#-pipeline-etl)
- [Architecture](#-architecture)
- [Prérequis](#-prérequis)
- [Démonstration](#-démonstration)

---

## 📌 Aperçu

ONRTECH Food Analytics est un projet de Data Engineering basé sur un pipeline **ETL (Extract, Transform, Load)** permettant de collecter, traiter, enrichir et analyser des données alimentaires issues de sites e-commerce.

Le projet intègre également des modèles **LLM (Large Language Models)** pour améliorer la qualité des données et fournir une analyse intelligente.

---

## 🎯 Objectifs

- Automatiser la collecte de données produits (web scraping)
- Nettoyer et structurer des données massives (plusieurs GB)
- Enrichir les données avec l’intelligence artificielle
- Stocker les données dans une base NoSQL scalable (MongoDB)
- Fournir des visualisations interactives avec Power BI
- Développer une interface web pour explorer les données

---

## 🏗 Structure du Projet

- **scraping/** : Scripts de web scraping (collecte des données)
- **etl/** : Pipeline ETL (nettoyage, transformation, enrichissement)
- **data/** : Fichiers JSON bruts et transformés
- **mcp-server/** : Serveur MCP exposant les services data
- **web-app/** : Interface utilisateur (frontend + backend)
- **powerbi/** : Rapports et dashboards Power BI

---

## 🛠 Technologies

- **Python** : Web scraping & traitement des données
- **MongoDB Atlas** : Base de données NoSQL
- **Power BI** : Visualisation et dashboards
- **OpenAI API (LLM)** : Enrichissement intelligent
- **FastAPI / Flask** : Backend API
- **React.js / HTML-CSS-JS** : Interface web

---

## 📊 Fonctionnalités

1. **Extraction des données**
   - Scraping de sites e-commerce
   - Génération de fichiers JSON volumineux

2. **Transformation des données**
   - Nettoyage (nulls, doublons)
   - Normalisation (prix, catégories)

3. **Enrichissement via LLM**
   - Classification automatique
   - Génération de descriptions
   - Correction sémantique

4. **Stockage MongoDB**
   - Insertion en collections structurées
   - Gestion de gros volumes de données

5. **Visualisation**
   - Dashboards Power BI interactifs

6. **Interface Web**
   - Recherche de produits
   - Filtrage dynamique
   - Consultation des données

---

## 🔄 Pipeline ETL

### 1️⃣ Extraction des données
- Scraping via Python (BeautifulSoup / Selenium)
- Collecte : nom, prix, catégorie, description, etc.
- Output : fichiers JSON

### 2️⃣ Transformation et normalisation
- Nettoyage des données
- Uniformisation des formats
- Structuration des champs

### 3️⃣ Enrichissement via LLM
- Classification intelligente
- Génération de contenu enrichi
- Normalisation des catégories

### 4️⃣ Chargement dans MongoDB
- Connexion MongoDB Atlas
- Insertion des documents JSON

### 5️⃣ Exploitation
- Power BI
- Interface Web
- MCP Server

---

## 🏗 Architecture

![Project Screenshot](architecture-etl.png)

**Flux global :**
