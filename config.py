# API Keys and Configuration Settings
FINANCIAL_DATA_API = "moneycontrol"  # Alternatives: "yfinance", "alpha_vantage"
NEWS_API = "63f3bd501374404fbd6d8e378e578ff6"  # Register at newsapi.org for free tier

# SEBI Compliance Parameters
MAX_PROMOTER_PLEDGE = 30  # Percentage
MAX_RELATED_PARTY_TRANSACTIONS = 10  # Percentage of revenue

# Model Training Parameters
TRAINING_DATA_PATH = "data/historical_data.csv"
MODEL_SAVE_PATH = "data/trained_model.pkl"
SCALER_SAVE_PATH = "data/scaler.pkl"