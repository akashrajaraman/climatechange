from bs4 import BeautifulSoup
import requests
import numpy as np

class FinancialAnalyzer:
    def get_financial_statements(self, ticker):
        """Fetch financial statements from Moneycontrol"""
        url = f"https://www.moneycontrol.com/financials/{ticker}/consolidated-profit-lossVI/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract data from tables (simplified example)
        tables = soup.find_all('table', class_='mctable1')
        balance_sheet = self._parse_table(tables[0]) if tables else {}
        income_statement = self._parse_table(tables[1]) if len(tables) > 1 else {}
        
        return {
            'balance_sheet': balance_sheet,
            'income_statement': income_statement
        }
    
    def _parse_table(self, table):
        """Helper to parse HTML tables into structured data"""
        rows = table.find_all('tr')
        data = {}
        for row in rows[1:]:  # Skip header
            cells = row.find_all('td')
            if len(cells) > 1:
                key = cells[0].text.strip()
                values = [cell.text.strip() for cell in cells[1:]]
                data[key] = values
        return data
    
    def calculate_financial_ratios(self, statements):
        """Calculate key financial ratios"""
        # Simplified ratio calculations
        bs = statements['balance_sheet']
        is_ = statements['income_statement']
        
        try:
            current_assets = float(bs.get('Total Current Assets', [0])[0].replace(',', ''))
            current_liabilities = float(bs.get('Total Current Liabilities', [0])[0].replace(',', ''))
            net_income = float(is_.get('Net Profit', [0])[0].replace(',', ''))
            revenue = float(is_.get('Total Revenue', [0])[0].replace(',', ''))
            total_assets = float(bs.get('Total Assets', [0])[0].replace(',', ''))
            
            return {
                'current_ratio': current_assets / current_liabilities,
                'net_margin': net_income / revenue,
                'roa': net_income / total_assets
            }
        except:
            return {}