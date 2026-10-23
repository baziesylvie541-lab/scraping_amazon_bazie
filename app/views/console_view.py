from app.models.depot import produits


# ---------------------------------------------------------------
# AFFICHAGE
# ---------------------------------------------------------------
def afficher_produits():
    if not produits:
        print("\nAucun produit. Lance d'abord le scraping.")
        return

    for p in produits:
        print("\nNom   :", p["nom"])
        print("Prix  :", p["prix"])
        print("Note  :", p["note"])
        print("Image :", p["image"])
        print("-" * 50)


def afficher_menu():
    print("""
        1-Scraper un site web
        2-Afficher les produits
        3-Exporter vers csv
        4-Quitter
""")
    return input("Votre choix : ")
