from ai_recommendation import AIRecommendationEngine
import pandas as pd

def train_initial_model():
    df = pd.read_csv("data/historical_data.csv")
    X = df[['current_ratio', 'net_margin', 'roa', 'pe_ratio']].values
    y = df['outcome'].values
    
    ai = AIRecommendationEngine()
    ai.train_model(X, y)
    print("Initial model trained and saved")

if __name__ == "__main__":
    train_initial_model()