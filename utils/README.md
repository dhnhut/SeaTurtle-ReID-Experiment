# Utils Directory

This directory contains utility functions and helper scripts for the SeaTurtle Re-Identification project.

## 📁 Suggested Structure

- **data_utils.py**: Data loading, preprocessing, and augmentation utilities
- **model_utils.py**: Model architecture definitions and helper functions
- **eval_utils.py**: Evaluation metrics and visualization functions
- **config.py**: Configuration management and hyperparameters
- **visualization.py**: Plotting and visualization utilities

## 💡 Best Practices

1. **Modular Design**: Keep functions focused and reusable
2. **Documentation**: Add clear docstrings to all functions
3. **Type Hints**: Use type hints for better code clarity
4. **Testing**: Include unit tests for critical functions
5. **Imports**: Organize imports and dependencies clearly

## 🚀 Example Usage

```python
# In your notebooks
import sys
sys.path.append('../utils')

from data_utils import load_dataset, preprocess_images
from eval_utils import calculate_map, plot_confusion_matrix
```

## 📝 File Templates

Consider creating these utility modules:

### data_utils.py
```python
"""Data loading and preprocessing utilities."""

def load_dataset(data_path: str) -> tuple:
    """Load and return dataset splits."""
    pass

def preprocess_images(images: list) -> list:
    """Apply preprocessing to image list."""
    pass
```

### eval_utils.py
```python
"""Evaluation metrics and visualization utilities."""

def calculate_map(predictions: list, ground_truth: list) -> float:
    """Calculate mean Average Precision."""
    pass
```