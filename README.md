# ChurnGuard: An Explainable Customer Retention Intelligence Platform

An end-to-end machine learning system that predicts customer churn, explains *why* each
customer is at risk using SHAP, and recommends a retention action — built for a
5th-semester Project Based Learning (PBL) project.

## Team
- Aryan Patle
- Anushka Gangwal
- Aaditi Deshmukh
- Aryan Kamthe

**Faculty Guide:** Dr. Vinodpuri R. Gosavi
**Group ID:** TYAIA209

## Problem
Businesses often only realize a customer is about to leave after they've already
disengaged. This project predicts churn risk in advance, explains the key drivers behind
each prediction, and estimates the revenue at risk — so retention teams can act early
and prioritize the right customers.

## Tech Stack
- Python 3.10+
- pandas, NumPy, scikit-learn, XGBoost
- imbalanced-learn (SMOTE)
- SHAP (explainability)
- Streamlit (dashboard)

## Project Structure
```
churnguard-pbl/
├── data/
│   ├── raw/            # original, unmodified dataset (e.g. Telco churn CSV)
│   └── processed/       # cleaned/encoded data, train-test splits
├── notebooks/            # Jupyter notebooks for EDA and experiments
├── src/                  # reusable Python scripts (preprocessing, training, etc.)
├── models/               # saved trained models (.pkl files)
├── reports/
│   └── figures/          # saved plots (SHAP charts, ROC curves, etc.)
├── dashboard/             # Streamlit app code
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup Instructions
1. Clone this repository:
   ```
   git clone <your-repo-url>
   cd churnguard-pbl
   ```
2. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS/Linux
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Place the dataset CSV inside `data/raw/`.
5. Run the Streamlit dashboard (once built):
   ```
   streamlit run dashboard/app.py
   ```

## Dataset
IBM Telco Customer Churn Dataset (Kaggle):
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

## Status
In development - see project tracker for current phase.
