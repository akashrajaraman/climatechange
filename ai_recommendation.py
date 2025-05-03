import yfinance as yf
import pandas as pd
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib
import numpy as np

class AIRecommendationEngine:
    def __init__(self):
        try:
            self.model = joblib.load('data/trained_model.pkl')
            self.scaler = joblib.load('data/scaler.pkl')
        except:
            self.model = RandomForestClassifier()
            self.scaler = StandardScaler()
    
    def get_realtime_analysis(self, ticker):
        """Get live market data"""
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1mo")
        info = stock.info
        
        # Calculate technical indicators
        hist['SMA_50'] = hist['Close'].rolling(50).mean()
        hist['RSI'] = self._calculate_rsi(hist['Close'])
        
        latest = hist.iloc[-1]
        
        return {
            'price': latest['Close'],
            'pe_ratio': info.get('trailingPE', 0),
            'profit_margins': info.get('profitMargins', 0),
            'sma_50': latest['SMA_50'],
            'rsi': latest['RSI'],
            'market_cap': info.get('marketCap', 0)
        }
    
    def _calculate_rsi(self, prices, window=14):
        deltas = prices.diff()
        gain = deltas.where(deltas > 0, 0)
        loss = -deltas.where(deltas < 0, 0)
        avg_gain = gain.rolling(window).mean()
        avg_loss = loss.rolling(window).mean()
        rs = avg_gain / avg_loss
        return 100 - (100 / (1 + rs)).iloc[-1]
    
    def generate_realtime_recommendation(self, ticker):
        """Generate dynamic recommendation"""
        analysis = self.get_realtime_analysis(ticker)
        
        # Feature vector
        features = [
            analysis['pe_ratio'],
            analysis['profit_margins'],
            analysis['price']/analysis['sma_50'],
            analysis['rsi'],
            np.log(analysis['market_cap'])
        ]
        
        # Score calculation (0-100)
        score = min(100, max(0, (
            30 * (1 if 10 < analysis['pe_ratio'] < 25 else 0) +
            25 * (1 if analysis['profit_margins'] > 0.1 else 0) +
            20 * (1 if 0.95 < analysis['price']/analysis['sma_50'] < 1.2 else 0) +
            15 * (1 if 30 < analysis['rsi'] < 70 else 0) +
            10 * (1 if analysis['market_cap'] > 1e11 else 0)
        ))
        
        # Recommendation logic
        if score >= 70:
            return "STRONG BUY", score
        elif score >= 55:
            return "BUY", score
        elif score >= 40:
            return "HOLD", score
        else:
            return "SELL", score