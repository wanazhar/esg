# data_pipeline.py
import aiohttp
from tenacity import retry, stop_after_attempt, wait_exponential

class GlobalESGPipeline:
    def __init__(self):
        self.semaphore = asyncio.Semaphore(100)  # Rate limiting
        
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1))
    async def fetch_esg(self, symbol: str):
        async with self.semaphore:
            async with aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=30),
                connector=aiohttp.TCPConnector(ssl=False)
            ) as session:
                # Try primary source
                try:
                    return await self._fetch_primary(session, symbol)
                except Exception as primary_error:
                    # Fallback to secondary sources
                    return await self._fetch_fallback(session, symbol)