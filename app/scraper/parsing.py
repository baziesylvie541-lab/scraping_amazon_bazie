# ---------------------------------------------------------------
# EXTRACTION
# ---------------------------------------------------------------
def extraire_produit(carte):
    """Extrait les infos d'une carte produit. Retourne None si pas de nom."""
    nom_tag = carte.select_one("h2 span")
    if not nom_tag:
        return None
    nom = nom_tag.get_text(strip=True)

    prix_tag = carte.select_one("span.a-price span.a-offscreen")
    prix = prix_tag.get_text(strip=True) if prix_tag else "Prix non trouvé"

    img = carte.select_one("img.s-image")
    image = img.get("src") if img else "Image non trouvée"

    note_tag = carte.select_one("span.a-icon-alt")
    note = note_tag.get_text(strip=True) if note_tag else "Pas de note"

    return {"nom": nom, "prix": prix, "image": image, "note": note}
