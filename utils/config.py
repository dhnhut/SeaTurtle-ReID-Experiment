"""
Configuration file for SeaTurtle Re-Identification Experiment
"""

import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
ANNOTATIONS_DIR = DATA_DIR / "annotations"
MODELS_DIR = PROJECT_ROOT / "models"
RESULTS_DIR = PROJECT_ROOT / "results"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
UTILS_DIR = PROJECT_ROOT / "utils"

# Create directories if they don't exist
for directory in [DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR, 
                  ANNOTATIONS_DIR, MODELS_DIR, RESULTS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# Image processing settings
IMAGE_SIZE = (224, 224)  # Standard input size for many CNN models
SUPPORTED_FORMATS = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']

# Model settings
BATCH_SIZE = 32
LEARNING_RATE = 0.001
NUM_EPOCHS = 100
DEVICE = "cuda" if os.path.exists("/dev/nvidia0") else "cpu"

# Re-identification specific settings
EMBEDDING_DIM = 512  # Feature embedding dimension
NUM_IDENTITIES = None  # Will be set based on dataset
TRIPLET_MARGIN = 0.3  # Margin for triplet loss

# Data augmentation settings
AUGMENTATION_PARAMS = {
    'horizontal_flip_prob': 0.5,
    'rotation_range': (-10, 10),
    'brightness_range': (0.8, 1.2),
    'contrast_range': (0.8, 1.2),
    'saturation_range': (0.8, 1.2),
}

# Evaluation settings
EVAL_METRICS = ['mAP', 'CMC@1', 'CMC@5', 'CMC@10']
QUERY_GALLERY_SPLIT = 0.5  # Ratio for query vs gallery split

# Logging settings
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Random seed for reproducibility
RANDOM_SEED = 42