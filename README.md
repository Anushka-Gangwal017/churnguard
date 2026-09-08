# ChurnGuard: An Explainable Customer Retention Intelligence Platform

Customer churn can lead to significant revenue loss when businesses identify
at-risk customers only after they have already left.

ChurnGuard is an explainable machine learning platform designed to identify
customers who are likely to churn, understand the factors contributing to
their risk, and prioritize suitable retention actions.

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
