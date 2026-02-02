# Auto Data Quality Engine

A configurable, reusable, automated data cleaning and profiling engine in Python.

## Features
- Load CSV datasets
- Profile columns: missing values, duplicates, types
- Rule-driven cleaning (configurable)
- Generates data quality reports

## Structure
- `engine/`: main modules (loader, profiler, cleaner, reporter)
- `config/`: dataset-specific rules
- `data/`: input, output, and reports
- `main.py`: pipeline orchestrator

## Usage
1. Drop your CSV in `data/incoming/`
2. Update rules in `config/schema.yaml`
3. Run `python main.py`
