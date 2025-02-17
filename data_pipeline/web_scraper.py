import requests
from bs4 import BeautifulSoup

class ESGWebScraper:
    def __init__(self, urls):
        self.urls = urls

    def scrape(self):
        esg_data = {}
        for url in self.urls:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            # Example: Extracting ESG scores from a table
            table = soup.find('table', {'id': 'esg-scores'})
            if table:
                esg_data[url] = self._parse_table(table)
        return esg_data

    def _parse_table(self, table):
        data = {}
        for row in table.find_all('tr'):
            cols = row.find_all('td')
            if len(cols) == 2:
                category, score = cols[0].text.strip(), cols[1].text.strip()
                data[category] = float(score)
        return data
