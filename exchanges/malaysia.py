# exchanges/malaysia.py
from ..config import exchanges_config
from ..utils.validation import ESGValidationModel
import requests

class MYExchange:
    def __init__(self, symbol: str):
        self.config = exchanges_config['MY']
        self.symbol = symbol
        
    def validate_ticker(self):
        return re.match(self.config['ticker_format'], self.symbol)
    
    def fetch_esg(self) -> ESGValidationModel:
        url = self.config['esg_endpoint'].format(symbol=self.symbol)
        response = requests.get(url)
        return self._parse_esg_data(response.json())
    
    def _parse_esg_data(self, raw_data: dict) -> ESGValidationModel:
        return ESGValidationModel(
            exchange_code='MY',
            symbol=self.symbol,
            scores={
                'environment': raw_data.get('environment_score'),
                'social': raw_data.get('social_score'),
                'governance': raw_data.get('governance_score')
            },
            sources=[self.config['name']],
            last_updated=raw_data.get('as_of_date')
        )