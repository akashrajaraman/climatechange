import yfinance as yf
import pandas as pd
from transformers import pipeline

class CompanyAnalyzer:
    def __init__(self):
        self.sentiment_analyzer = pipeline("sentiment-analysis")
        
    def get_company_data(self, ticker):
        """Fetch basic company data from Yahoo Finance"""
        stock = yf.Ticker(ticker)
        info = stock.info
        return {
            'name': info.get('longName', ''),
            'sector': info.get('sector', ''),
            'industry': info.get('industry', ''),
            'current_price': info.get('currentPrice', 0),
            'market_cap': info.get('marketCap', 0),
            'pe_ratio': info.get('trailingPE', 0)
        }
    
    def analyze_news_sentiment(self, news_articles):
        """Analyze sentiment of news articles about the company"""
        sentiments = []
        for article in news_articles:
            result = self.sentiment_analyzer(article['title'] + " " + article['summary'])[0]
            sentiments.append(result['label'])
        
        positive = sentiments.count('POSITIVE')
        negative = sentiments.count('NEGATIVE')
        
        return {
            'positive_news': positive,
            'negative_news': negative,
            'sentiment_score': (positive - negative) / len(sentiments) if sentiments else 0
        }