# 🛠 FOE Bot (Forge of Empires)

Un bot simple pour automatiser certaines actions dans **Forge of Empires** en utilisant **PyAutoGUI**.

## ✅ Fonctionnalités
- Détection des production d'or et de marchandises
- Clic automatique sur les éléments trouvés
- Ajout automatique en file d'attentes pour les marchandises

---

## 📦 Installation

### 1. Cloner le projet

```bash
git clone https://github.com/ton-username/foe-bot.git
cd FOE
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## ▶️ Utilisation

Ouvre le jeu : `Forge Of Empire`

Lance le bot :

```bash
python -m bot_foe.main
```

---

## ⚙️ Configuration

Modifier les paramètres dans `bot_foe/config.py` :

```python
CHECK_INTERVAL = 1  # Intervalle entre les checks
CONFIDENCE = 0.7    # Niveau de précision pour la détection
```

---

## 🖼 Assets

Le bot se base sur PyAutoGUI pour détecter les images fournies dans `assets/`.

---

## ⚠️ Avertissement

L'utilisation de bots peut violer les conditions d'utilisation du jeu. Utilisez ce script à vos risques et périls.

---

## 📜 Licence

MIT License
