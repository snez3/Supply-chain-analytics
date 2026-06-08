# Supply Chain Disruption Analytics & Forecasting Pipeline

## Overview
An end-to-end data engineering and analytics project analyzing 180,000+ supply chain records to identify disruption patterns and predict delivery delays with 97% accuracy.

## Tech Stack
- **Python** - ETL, EDA, ML
- **Pandas & NumPy** - Data cleaning & feature engineering
- **Scikit-learn** - Random Forest delay prediction model
- **SQLite** - Local data warehouse
- **Matplotlib & Seaborn** - Data visualization
- **GitHub Actions** - CI/CD automation
- **Power BI** - Business intelligence dashboard

## Key Results
- 🚨 **54.83% late delivery rate** identified across all markets
- 🎯 **97% accuracy** Random Forest model for delay prediction
- 📊 **Shipping Delay** is the #1 factor (64.9% importance)
- 💰 Profit and sales analysis across global markets

## Project Structure
supply-chain-analytics/
├── etl/
│   ├── extract.py      # Data extraction
│   ├── transform.py    # Data cleaning & feature engineering
│   └── load.py         # Load to data warehouse
├── models/
│   ├── eda.py          # Exploratory data analysis
│   ├── predict.py      # ML delay prediction model
│   └── delay_model.pkl # Saved trained model
├── dashboard/          # Generated charts
└── data/               # Raw and cleaned datasets

## How to Run
pip install pandas numpy scikit-learn matplotlib seaborn
python etl/extract.py
python etl/transform.py
python etl/load.py
python models/eda.py
python models/predict.py
