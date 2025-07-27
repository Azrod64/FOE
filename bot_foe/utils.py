import os

def check_assets(images):
    for img in images:
        if not os.path.isfile(img):
            print(f"[ERREUR] Fichier manquant : {img}")
            return False
    return True
