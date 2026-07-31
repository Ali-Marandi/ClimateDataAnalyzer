# ClimateDataAnalyzer

![GitHub stars](https://img.shields.io/github/stars/Ali-Marandi/ClimateDataAnalyzer?style=social)
![License](https://img.shields.io/github/license/Ali-Marandi/ClimateDataAnalyzer)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

A professional Python-based tool for analyzing and visualizing historical climate data. This project focuses on identifying long-term trends in global temperature anomalies using data science workflows.

## Features

- **Data Acquisition:** Scripts for fetching and generating climate datasets.
- **Statistical Analysis:** Calculation of moving averages and trend identification.
- **Advanced Visualization:** High-quality plots using Seaborn and Matplotlib.
- **Modular Structure:** Clean separation between data loading, analysis, and visualization.

## Installation

```bash
git clone https://github.com/Ali-Marandi/ClimateDataAnalyzer.git
cd ClimateDataAnalyzer
pip install -r requirements.txt
```

## Usage

1. **Fetch Data:**
   ```bash
   python src/data_loader.py
   ```
2. **Run Analysis:**
   ```bash
   python src/analysis.py
   ```
   The results will be saved in the `results/` directory.

## Scientific Context

Temperature anomalies are defined as the deviation from a long-term average (baseline). A positive anomaly indicates that the observed temperature was warmer than the baseline, while a negative anomaly indicates it was cooler. This project helps visualize the clear upward trend in global temperatures over the last century.

## Requirements

- Python 3.8+
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Requests

## License

MIT License
