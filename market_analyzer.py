from textblob import TextBlob
from collections import defaultdict
from config import Config
from trend_extractor import TrendExtractor

class MarketAnalyzer:
    def __init__(self):
        self.companies = Config.DEFAULT_COMPANIES
        self.trend_keywords = Config.TREND_KEYWORDS
        self.trend_extractor = TrendExtractor()

    def analyze(self, articles):
        insights = {
            'articles_analyzed': len(articles),
            'sentiment': {'positive': 0, 'neutral': 0, 'negative': 0},
            'companies': defaultdict(int),
            'trends': defaultdict(int),
            'top_trend': None,  # NEW: Track dominant trend
            'top_company': None  # NEW: Track most mentioned company
        }

        for article in articles:
            self._analyze_article(insights, article)

        trends = self.trend_extractor.extract_trends(articles)
        insights['trends'].update(trends)
        
        # NEW: Identify top trend and company
        if insights['trends']:
            insights['top_trend'] = max(insights['trends'].items(), key=lambda x: x[1])[0]
        if insights['companies']:
            insights['top_company'] = max(insights['companies'].items(), key=lambda x: x[1])[0]

        return insights

    def _analyze_article(self, insights, article):
        # Sentiment analysis
        blob = TextBlob(article['title'])
        polarity = blob.sentiment.polarity
        if polarity > 0.1:
            insights['sentiment']['positive'] += 1
        elif polarity < -0.1:
            insights['sentiment']['negative'] += 1
        else:
            insights['sentiment']['neutral'] += 1

        # Company mentions
        title_lower = article['title'].lower()
        for company in self.companies:
            if company.lower() in title_lower:
                insights['companies'][company] += 1
