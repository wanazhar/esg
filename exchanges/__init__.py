# exchanges/__init__.py
from abc import ABC, abstractmethod
from typing import Optional
from ..utils.validation import ESGValidationModel

class BaseExchange(ABC):
    def __init__(self, symbol: str):
        self.symbol = symbol.upper()
        
    @abstractmethod
    def fetch_esg(self) -> ESGValidationModel:
        pass
    
    @classmethod
    @abstractmethod
    def get_exchange_code(cls) -> str:
        pass
    
    @classmethod
    def detect_from_symbol(cls, symbol: str) -> Optional['BaseExchange']:
        """Auto-detect exchange based on symbol pattern"""
        for subclass in cls.__subclasses__():
            if re.match(subclass._get_ticker_pattern(), symbol):
                return subclass(symbol)
        return None