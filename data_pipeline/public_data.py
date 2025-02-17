import pandas_datareader.data as web
from datetime import datetime

class PublicESGData:
    def __init__(self):
        self.start_date = datetime(2020, 1, 1)
        self.end_date = datetime.now()

    def get_financial_data(self, symbol: str):
        """Fetch financial data from a public source like Yahoo Finance"""
        try:
            data = web.DataReader(symbol, 'yahoo', self.start_date, self.end_date)
            return data
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            return None
