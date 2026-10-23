import os
import time
import random
from bs4 import BeautifulSoup

from config import URL, FICHIER_HTML
from app.models.depot import produits
from app.scraper.driver import creer_driver
from app.scraper.parsing import extraire_produit


def scraper():
    """Ouvre la page, la sauvegarde et remplit la liste `produits`."""
    produits.clear()
    driver = creer_driver()

    try:
        driver.get(URL)
        time.sleep(random.uniform(8, 12))

        html = driver.page_source
        os.makedirs(os.path.dirname(FICHIER_HTML), exist_ok=True)
        with open(FICHIER_HTML, "w", encoding="utf-8") as f:
            f.write(html)

        soup = BeautifulSoup(html, "html.parser")
        cartes = soup.select('div[data-component-type="s-search-result"]')
        print(f"Nombre de produits trouvés : {len(cartes)}")

        for carte in cartes:
            produit = extraire_produit(carte)
            if produit:
                produits.append(produit)

        print("\nScraping terminé avec succès !")

    finally:
        driver.quit()
