from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import nltk

# Download stopwords for trend extraction
nltk.download('stopwords')

class TrendExtractor:
    def __init__(self):
        self.stopwords = set(stopwords.words('english'))

    def extract_trends(self, articles):
        texts = [article['content'] for article in articles if article['content']]

        # Use CountVectorizer for extracting n-grams (unigrams and bigrams)
        vectorizer = CountVectorizer(stop_words='english', max_features=1000, ngram_range=(1, 2))
        X = vectorizer.fit_transform(texts)
        word_freq = X.sum(axis=0)
        freq_dict = {word: word_freq[0, idx] for word, idx in vectorizer.vocabulary_.items()}

        # Sort terms by frequency
        sorted_terms = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

        # Select top 5 emerging trends
        emerging_trends = {term: count for term, count in sorted_terms[:5]}
        return emerging_trends
