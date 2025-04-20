from news_fetcher import NewsFetcher
from market_analyzer import MarketAnalyzer
from report_generator import ReportGenerator
from config import Config

def main():
    print("Market Intelligence Report System")
    query = input("Enter market query: ")
    
    # Initialize components
    fetcher = NewsFetcher()
    analyzer = MarketAnalyzer()
    reporter = ReportGenerator()

    # Fetch and analyze data
    articles = fetcher.fetch_articles(query)
    insights = analyzer.analyze(articles)
    
    # Generate report
    report = reporter.generate(insights, query)
    print("\n" + report)

if __name__ == "__main__":
    main()
