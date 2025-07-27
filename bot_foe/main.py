import pyautogui as pg
import time
import os
from bot_foe.config import IMAGES, CHECK_INTERVAL, CONFIDENCE
from bot_foe.utils import check_assets

if not check_assets(IMAGES):
    exit(1)

print("[INFO] Bot FOE démarré - Appuyez sur Ctrl+C pour arrêter")

while True:
    found = False
    for image_path in IMAGES:
        try:
            pos = pg.locateCenterOnScreen(image_path, confidence=CONFIDENCE)
            if pos:
                img_name = os.path.basename(image_path)

                pg.moveTo(pos)
                pg.click()
                print(f"[OK] {img_name} trouvé à {pos}")

                if img_name == "outils.png" or img_name == "outils_etoile.png":
                    time.sleep(CHECK_INTERVAL + 0.5)
                    pg.click()
                    time.sleep(CHECK_INTERVAL)
                    pg.press('1')

                found = True
                break

        except pg.ImageNotFoundException:
            pass
    if not found:
        time.sleep(CHECK_INTERVAL)
