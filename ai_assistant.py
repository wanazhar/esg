import spacy
import requests

class ESGAIAssistant:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def interpret_query(self, query: str):
        doc = self.nlp(query)
        topics = [ent.text for ent in doc.ents if ent.label_ in ["ORG", "GPE", "PRODUCT"]]
        return topics

    def search_reports(self, topics: list):
        search_results = []
        for topic in topics:
            response = requests.get(
                "https://api.bing.microsoft.com/v7.0/search",
                headers={"Ocp-Apim-Subscription-Key": "YOUR_BING_API_KEY"},
                params={"q": f"{topic} ESG report"}
            )
            search_results.extend(response.json().get("webPages", {}).get("value", []))
        return search_results
