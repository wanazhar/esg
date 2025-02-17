# exchanges/_template.py
from __future__ import annotations
from ..config import exchanges_config
from ..utils.validation import ESGValidationModel
import aiohttp

class ExchangeTemplate(BaseExchange):
    
    @classmethod
    def get_exchange_code(cls) -> str:
        return "TEMPLATE"
    
    async def fetch_esg(self) -> ESGValidationModel:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                self.config['esg_endpoint'].format(symbol=self.symbol),
                headers={"Authorization": f"Bearer {self._get_api_key()}"}
            ) as response:
                return self._parse_esg(await response.json())