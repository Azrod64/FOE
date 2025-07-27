import pyautogui as pg
import time
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(SCRIPT_DIR, "assets")
IMAGES = [
    os.path.join(ASSETS_DIR, "epees.png"),
    os.path.join(ASSETS_DIR, "coins.jpg"),
    os.path.join(ASSETS_DIR, "outils.png")
]

CHECK_INTERVAL = 1

# Vérifie que les fichiers existent
for img in IMAGES:
    if not os.path.isfile(img):
        print(f"[ERREUR] Fichier manquant : {img}")
        exit(1)

print("[INFO] Script démarré - Appuyez sur Ctrl+C pour arrêter")

while True:
    found = False
    for image_path in IMAGES:
        try:
            pos = pg.locateCenterOnScreen(image_path, confidence=0.7, grayscale=False)
            if pos:
                img_name = os.path.basename(image_path)

                if img_name == "outils.png":
                    pg.moveTo(pos)
                    pg.click()
                    print(f"[OK] {img_name} trouvé à {pos}")
                    time.sleep(2)
                    pg.click()
                    time.sleep(1)
                    pg.press('1')
                    found = True
                    break

                elif img_name == "coins.jpg":
                    pg.moveTo(pos)
                    pg.click()
                    print(f"[OK] {img_name} trouvé à {pos}")
                    found = True
                    break

                elif img_name == "epees.png":
                    pg.moveTo(pos)
                    pg.click()
                    print(f"[OK] {img_name} trouvé à {pos}")
                    found = True
                    break

        except pg.ImageNotFoundException:
            pass  # Image non trouvée
    if not found:
        time.sleep(CHECK_INTERVAL)
