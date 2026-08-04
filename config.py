from pathlib import Path

# Root Directory
ROOT_DIR = Path(__file__).parent

# Project Paths
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODELS_DIR = ROOT_DIR / "models"

RESULTS_DIR = ROOT_DIR / "results"

REPORTS_DIR = ROOT_DIR / "reports"

ASSETS_DIR = ROOT_DIR / "assets"
IMAGES_DIR = ASSETS_DIR / "images"
ICONS_DIR = ASSETS_DIR / "icons"
STYLES_DIR = ASSETS_DIR / "styles"