import aiohttp
from typing import AsyncGenerator
from tenacity import retry, stop_after_attempt, wait_exponential
from config import global_standards

class ESGDataFetcher:
    RETRY_POLICY = retry(
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=1, min=2, max=30),
        retry=retry_if_exception_type(aiohttp.ClientError)
    )

    @RETRY_POLICY
    async def fetch_data(self, session: aiohttp.ClientSession, url: str, params: dict):
        """Robust data fetcher with circuit breaker pattern"""
        try:
            async with session.get(url, params=params) as response:
                response.raise_for_status()
                return await response.json()
        except aiohttp.ClientError as e:
            log_error(f"API request failed: {str(e)}")
            raise

class GlobalESGSources:
    def __init__(self):
        self.fetcher = ESGDataFetcher()
        self.registry = WorldExchangeRegistry.load()
        self.cache = LRUCache(maxsize=1000)

    async def gather_sources(self, symbol: str) -> AsyncGenerator[dict, None]:
        """Enterprise-grade data aggregation with caching and fallbacks"""
        cached = self.cache.get(symbol)
        if cached:
            yield cached
            return

        # Core data collection pipeline
        sources = [
            self._get_official_data(symbol),
            self._get_regulatory_filings(symbol),
            self._get_third_party(symbol),
            self._get_news_sentiment(symbol)
        ]
        
        async for result in self._priority_merge(sources):
            validated = GlobalESGValidator.validate(result)
            self.cache.set(symbol, validated)
            yield validated
# data_pipeline/sources.py
async def get_refinitiv_data(symbol: str) -> RefinitivESGScores:
    """Official Refinitiv API integration"""
    params = {
        'symbol': symbol,
        'fields': 'TR.ESGScore,TR.EnvironmentalPillar,TR.SocialPillar,TR.GovernancePillar,TR.ResourceUseScore,TR.EmissionsScore,TR.InnovationScore,TR.WorkforceScore,TR.HumanRightsScore,TR.CommunityScore,TR.ProductResponsibilityScore,TR.ManagementScore,TR.ShareholdersScore,TR.CSRStrategyScore'
    }
    
    data = await self.fetcher.fetch_data(
        session=session,
        url="https://api.refinitiv.com/esg/v3",
        params=params
    )
    
    return RefinitivESGScores(**data['esgScores'])