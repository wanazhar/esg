# tools/generate_exchanges.py
import os
import yaml
from pathlib import Path

TEMPLATE = '''from __future__ import annotations
from ..config import exchanges_config
from ..utils.validation import ESGValidationModel
import aiohttp

class {exchange_class}(BaseExchange):
    """Automated ESG module for {exchange_name}"""

    @classmethod
    def get_exchange_code(cls) -> str:
        return "{exchange_code}"
    
    async def fetch_esg(self) -> ESGValidationModel:
        config = exchanges_config["{exchange_code}"]
        async with aiohttp.ClientSession() as session:
            async with session.get(
                config["esg_endpoint"].format(symbol=self.symbol),
                headers={{"Authorization": f"Bearer {{self._get_api_key()}}"}}
            ) as response:
                return self._parse_esg(await response.json())
    
    def _parse_esg(self, data: dict) -> ESGValidationModel:
        return ESGValidationModel(
            exchange_code="{exchange_code}",
            symbol=self.symbol,
            scores={score_mapping},
            sources=[config["name"]],
            last_updated=data.get("as_of_date")
        )
'''

def generate_exchanges():
    with open("config/exchanges.yaml") as f:
        config = yaml.safe_load(f)
    
    exchange_dir = Path("exchanges")
    exchange_dir.mkdir(exist_ok=True)
    
    for code in config["exchanges"]:
        class_name = f"{code}Exchange"
        with open(exchange_dir / f"{code.lower()}.py", "w") as f:
            f.write(TEMPLATE.format(
                exchange_class=class_name,
                exchange_code=code,
                exchange_name=config["exchanges"][code]["name"],
                score_mapping="data['esg_scores']"  # Simplified mapping
            ))
            
if __name__ == "__main__":
    generate_exchanges()