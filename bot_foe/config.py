import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(SCRIPT_DIR, "../assets")
IMAGES = [
    os.path.join(ASSETS_DIR, "epees.png"),
    os.path.join(ASSETS_DIR, "coins.jpg"),
    os.path.join(ASSETS_DIR, "outils.png"),
    os.path.join(ASSETS_DIR, "outils_etoile.png"),
]
CHECK_INTERVAL = 1
CONFIDENCE = 0.7
