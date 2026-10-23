from dataclasses import dataclass


@dataclass
class Produit:
    nom: str
    prix: str
    image: str
    note: str

    def to_dict(self):
        return {"nom": self.nom, "prix": self.prix,
                "image": self.image, "note": self.note}
