import os

def remplacer_superfixe(dossier, ancien_suffixe="ingredients_extracted", nouveau_suffixe="iAdetailed"):
    # Parcours tous les sous-dossiers et fichiers du dossier spécifié
    for root, dirs, files in os.walk(dossier):
        for nom_fichier in files:
            # Vérifie si le fichier est un fichier JSON et contient l'ancien suffixe
            if nom_fichier.endswith(".json") and ancien_suffixe in nom_fichier:
                # Créer le nouveau nom de fichier en remplaçant l'ancien suffixe
                nouveau_nom = nom_fichier.replace(ancien_suffixe, nouveau_suffixe)
                ancien_chemin = os.path.join(root, nom_fichier)
                nouveau_chemin = os.path.join(root, nouveau_nom)

                # Renommer le fichier
                os.rename(ancien_chemin, nouveau_chemin)
                print(f"✅ Renommé : {ancien_chemin} → {nouveau_chemin}")

# Demande à l'utilisateur d'entrer le chemin du dossier
dossier_cible = input("Entrez le chemin du dossier contenant les fichiers à renommer : ")

# Vérifie si le dossier existe
if os.path.isdir(dossier_cible):
    remplacer_superfixe(dossier_cible)
else:
    print("Le dossier spécifié n'existe pas.")
