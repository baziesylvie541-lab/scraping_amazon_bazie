import csv
import os

from config import FICHIER_CSV

produits = []


def exporter_csv():
    """Génère le fichier CSV à partir de la liste `produits`."""
    if not produits:
        print("\nAucun produit à exporter.")
        return

    os.makedirs(os.path.dirname(FICHIER_CSV), exist_ok=True)
    with open(FICHIER_CSV, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=["nom", "prix", "image", "note"])
        writer.writeheader()
        writer.writerows(produits)
    print(f"\nFichier {FICHIER_CSV} créé avec succès !")
