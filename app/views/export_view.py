import os
import pandas as pd

from config import FICHIER_EXCEL
from app.models.depot import produits


# ---------------------------------------------------------------
# EXPORT EXCEL
# ---------------------------------------------------------------
def exporter_excel():
    if not produits:
        print("\nAucun produit à exporter.")
        return

    os.makedirs(os.path.dirname(FICHIER_EXCEL), exist_ok=True)
    df = pd.DataFrame(produits)
    df.to_excel(FICHIER_EXCEL, index=False, sheet_name="Produits Amazon")
    print(f"\nFichier {FICHIER_EXCEL} créé avec succès !")
