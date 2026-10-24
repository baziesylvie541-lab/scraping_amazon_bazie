
# Amazon Scraper

Application console en Python qui récupère des produits sur une page de résultats Amazon (nom, prix, note, image), les affiche, puis les exporte en **CSV** 
Le projet suit une architecture **MVC** (Modèle - Vue - Contrôleur).

## Technologies

- Python 3
- Selenium (pilotage de Chrome)
- BeautifulSoup4 (analyse du HTML)
- Pandas + OpenPyXL (export Excel)

## Structure du projet


amazon_scraper/
├── README.md
├── main.py                  
├── config.py                
├── requirements.txt
├── app/
│   ├── controllers/
│   │   └── scraping_controller.py   
│   ├── models/
│   │   ├── depot.py                 
│   │   └── produit.py               
│   ├── scraper/
│   │   ├── amazon_scraper.py        
│   │   ├── driver.py                
│   │   └── parsing.py              
│   └── views/
│       ├── console_view.py          
│       └── export_view.py          
├── data/                    
├── exports/                 
└── tests/

## Installation

1. Installer Google Chrome.
2. Installer les dépendances depuis la racine du projet :
py -m pip install -r requirements.txt

## Utilisation

Depuis la racine du projet (là où se trouve `main.py`) :

py main.py


Menu :

| Choix | Action |
|-------|--------|
| 1 | Scraper la page Amazon |
| 2 | Afficher les produits |
| 3 | Exporter vers CSV (et Excel) |
| 4 | Quitter |

## Fichiers générés

- `data/ama.html` : copie de la page scrapée
- `exports/produits.csv` : produits au format CSV



