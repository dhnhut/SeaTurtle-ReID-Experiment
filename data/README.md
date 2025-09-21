# Data Directory

This directory contains all datasets used in the SeaTurtle Re-Identification experiments.

⚠️ **Important**: This directory is excluded from git tracking to avoid committing large dataset files.

## 📁 Structure

- **raw/**: Original, unmodified datasets
- **processed/**: Preprocessed and cleaned datasets ready for training
- **annotations/**: Label files, bounding boxes, and metadata

## 📋 Dataset Guidelines

### Raw Data (`raw/`)
- Keep original datasets unchanged
- Use descriptive folder names (e.g., `seaturtle_dataset_2023/`)
- Include dataset documentation and licenses

### Processed Data (`processed/`)
- Store preprocessed versions of datasets
- Include train/validation/test splits
- Document preprocessing steps in notebooks

### Annotations (`annotations/`)
- Store identity labels and metadata
- Include bounding box annotations if available
- Use standard formats (JSON, CSV, XML)

## 🔗 Data Sources

Document your data sources here:
- Dataset name and version
- Download links or contact information
- Citation requirements
- License information

## 📝 Data Format

Describe the expected data format:
```
data/
├── raw/
│   └── dataset_name/
│       ├── images/
│       └── labels.csv
├── processed/
│   └── dataset_name/
│       ├── train/
│       ├── val/
│       └── test/
└── annotations/
    └── identity_mapping.json
```