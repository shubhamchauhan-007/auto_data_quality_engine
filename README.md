# Automated Data Quality & Cleaning Engine

A config-driven, scalable data quality and cleaning engine built in Python.
This system is designed to work with any dataset, supports large-scale data (lakhs & crores of rows) using chunk processing, and requires minimal configuration to adapt across projects.

## Features

- Schema-driven data cleaning
- Automatic schema inference (if schema not provided)
- Data profiling and quality checks
- Handles missing values, duplicates, and data validations
- Chunk-based processing for large datasets
- Centralized logging for every cleaning action
- Resusable across multiple projects and domains
- Easing extendable.

## Structure

AutoDataCleaner/
│
├── engine/
│ ├── cleaner.py # Config-driven cleaning logic
│ ├── loader.py # Standard data loading
│ ├── config_loader.py # YAML schema loader
│ ├── logger.py # Central logging
│ ├── profiler.py # Data profiling & stats
│ ├── rule_engine.py # Rule evaluation engine
│ ├── schema_infer.py # Automatic schema inference
│
├── config/
│ └── schema.yaml # Cleaning rules configuration
│
├── data/
│ ├── incoming/ # Raw input data
│ └── cleaned/ # Cleaned output data
│
├── main.py # Pipeline entry point
├── requirements.txt
├── README.md
└── .gitignore

## Usage

1. Drop your CSV in `data/incoming/`
2. Update rules in `config/schema.yaml`
3. Run `python main.py`
