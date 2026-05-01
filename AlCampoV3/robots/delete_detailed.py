import os
import sys

def supprimer_fichiers(dossier):
    # Mots-clés à rechercher dans le nom du fichier (minuscule pour simplifier)
    mots_cles = ["iadetailed", "hfdetailed", "ollamadetailed", "gptdetailed"]

    total_supprimes = 0
    for root, _, files in os.walk(dossier):
        for nom_fichier in files:
            nom_minuscule = nom_fichier.lower()
            if any(mot in nom_minuscule for mot in mots_cles):
                chemin_fichier = os.path.join(root, nom_fichier)
                try:
                    os.remove(chemin_fichier)
                    print(f"🗑️ Supprimé : {chemin_fichier}")
                    total_supprimes += 1
                except Exception as e:
                    print(f"⚠️ Erreur suppression {chemin_fichier} : {e}")

    print(f"\n✅ Suppression terminée — {total_supprimes} fichier(s) supprimé(s).")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python supprimer_detailed.py <dossier>")
        sys.exit(1)

    dossier_cible = sys.argv[1]
    if not os.path.isdir(dossier_cible):
        print(f"❌ Dossier introuvable : {dossier_cible}")
        sys.exit(1)

    supprimer_fichiers(dossier_cible)
