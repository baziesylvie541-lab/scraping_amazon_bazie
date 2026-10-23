from app.scraper.amazon_scraper import scraper
from app.views.console_view import afficher_menu, afficher_produits
from app.views.export_view import exporter_excel
from app.models.depot import exporter_csv


# ---------------------------------------------------------------
# MENU
# ---------------------------------------------------------------
def menu():
    while True:
        choix = afficher_menu()

        if choix == "1":
            scraper()
        elif choix == "2":
            afficher_produits()
        elif choix == "3":
            exporter_csv()
            exporter_excel()
        elif choix == "4":
            print("\nMerci d'avoir utilisé l'application !")
            break
        else:
            print("\nChoix invalide. Réessayez.")
