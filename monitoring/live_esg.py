# monitoring/live_esg.py
class LiveESGMonitor:
    def __init__(self):
        self.streams = {
            'news': NewsESGStream(),
            'regulatory': FilingStream(),
            'market_data': TickerStream()
        }
        
    async def track_esg(self, symbol: str):
        """Real-time ESG event stream"""
        async for update in self._merge_streams(symbol):
            yield ESGEvent(
                type=update['type'],
                impact_score=calculate_impact(update),
                source=update['source'],
                timestamp=datetime.utcnow()
            )