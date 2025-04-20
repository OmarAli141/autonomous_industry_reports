import requests
from config import Config

class NewsFetcher:
    def fetch_articles(self, query):
        params = {
            "q": query,
            "pageSize": 20,
            "sortBy": "relevancy",
            "apiKey": Config.NEWS_API_KEY,
            "language": "en"
        }
        
        try:
            response = requests.get(Config.NEWS_API_URL, params=params)
            return response.json().get("articles", [])
        except Exception:
            return []
