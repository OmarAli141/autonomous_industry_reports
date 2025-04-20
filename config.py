class Config:
    # NewsAPI Configuration
    NEWS_API_KEY = "4a8246110a18468098cbe066493f71f8"
    NEWS_API_URL = "http://newsapi.org/v2/everything"
    
    # Analysis Parameters
    DEFAULT_COMPANIES = ["Tesla", "BYD", "Ford", "GM", "Rivian"]
    TREND_KEYWORDS = {
        "Technology": ["battery", "autonomous", "AI"],
        "Regulation": ["regulation", "law", "policy"],
        "Market Growth": ["growth", "increase", "expand"]
    }
