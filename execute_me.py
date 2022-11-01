
from pathlib import Path


EXTENSIONS_MAPPING = {".mp3": "Musique",
                      ".wav": "Musique",
                      ".mp4": "Videos",
                      ".avi": "Videos",
                      ".gif": "Videos",
                      ".bmp": "Images",
                      ".png": "Images",
                      ".jpg": "Images",
                      ".txt": "Documents",
                      ".pptx": "Documents",
                      ".csv": "Documents",
                      ".xls": "Documents",
                      ".odp": "Documents",
                      ".pages": "Documents"}

BASE_DIR = Path('/Users/soufianebelhabibe/Downloads')# choisissez le chemin 

# On récupère tous les fichiers dans le dossier de base
files = [f for f in BASE_DIR.iterdir() if f.is_file()]
for file in files:  # On boucle sur chaque fichier
    dossier_cible = EXTENSIONS_MAPPING.get(file.suffix, "Divers")
    dossier_cible_absolu = BASE_DIR / dossier_cible
    dossier_cible_absolu.mkdir(exist_ok=True)
    fichier_cible = dossier_cible_absolu / file.name
    # On déplace le fichier
    file.rename(fichier_cible)
