from selenium import webdriver

from config import USER_AGENT


# ---------------------------------------------------------------
# NAVIGATEUR
# ---------------------------------------------------------------
def creer_driver():
    """Crée et retourne un navigateur Chrome configuré."""
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={USER_AGENT}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    return webdriver.Chrome(options=options)
