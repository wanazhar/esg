# config/api_config.py
from pydantic import BaseSettings, ValidationError
from typing import Dict

class APIConfig(BaseSettings):
    alpha_vantage: str
    nyse: Optional[str] = None
    jpx: Optional[str] = None
    
    class Config:
        env_prefix = "ESG_"
        case_sensitive = False

def validate_api_keys(exchange_code: str) -> bool:
    required_keys = exchanges_config[exchange_code]['required_keys']
    try:
        config = APIConfig()
        return all(getattr(config, key) for key in required_keys)
    except ValidationError:
        return False
# Add to api_config.py
from cryptography.fernet import Fernet

class SecureAPIConfig:
    _ENCRYPTION_KEY = os.getenv('CONFIG_ENCRYPTION_KEY')
    
    @classmethod
    def get_key(cls, provider: str) -> str:
        """Secure API key retrieval with symmetric encryption"""
        encrypted_key = os.getenv(f'ESG_{provider.upper()}_KEY')
        return Fernet(cls._ENCRYPTION_KEY).decrypt(encrypted_key.encode()).decode()