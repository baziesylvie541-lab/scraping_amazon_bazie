import os

# ---------------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------------
URL = (
    "https://www.amazon.com/s?i=specialty-aps&bbn=16225005011"
    "&rh=n%3A%252116225005011%2Cn%3A17726796011"
    "&ref=nav_em__nav_desktop_sa_intl_travel_gear_0_2_11_16"
)
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FICHIER_HTML = os.path.join(BASE_DIR, "data", "ama.html")
FICHIER_EXCEL = os.path.join(BASE_DIR, "exports", "produits.xlsx")
FICHIER_CSV = os.path.join(BASE_DIR, "exports", "produits.csv")
