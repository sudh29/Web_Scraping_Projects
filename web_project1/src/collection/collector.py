"""Data collection module for generating mock Twitter data."""

import logging
import random
from datetime import datetime, timedelta, timezone

import pandas as pd

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_mock_tweets(hashtags: list[str], since_date: str, limit: int) -> pd.DataFrame:
    """
    Generates a DataFrame of mock tweets.

    Args:
        hashtags: A list of hashtags to include in the mock tweets.
        since_date: The start date for the mock tweets (YYYY-MM-DD).
        limit: The number of mock tweets to generate.

    Returns:
        A pandas DataFrame containing the mock tweets.
    """
    logging.info("Generating mock tweet data due to issues with Twitter scraping libraries.")

    tweets = []
    start_date_obj = datetime.strptime(since_date, "%Y-%m-%d").replace(tzinfo=timezone.utc)

    positive_words = ['buy', 'bullish', 'profit', 'up', 'high', 'rally']
    negative_words = ['sell', 'bearish', 'loss', 'down', 'low', 'crash']

    for i in range(limit):
        timestamp = start_date_obj + timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59))
        hashtag = random.choice(hashtags)

        sentiment_type = random.choice(['positive', 'negative', 'neutral'])
        if sentiment_type == 'positive':
            extra_word = random.choice(positive_words)
            content = f'This is a mock tweet about {hashtag}. I am feeling very {extra_word} about this! #stockmarket #{hashtag.strip("#")}'
        elif sentiment_type == 'negative':
            extra_word = random.choice(negative_words)
            content = f'This is a mock tweet about {hashtag}. I am feeling very {extra_word} about this! #stockmarket #{hashtag.strip("#")}'
        else:
            content = f'This is a mock tweet about {hashtag}. #stockmarket #{hashtag.strip("#")}'

        tweets.append({
            'username': f'user_{random.randint(1, 1000)}',
            'timestamp': timestamp,
            'content': content,
            'likes': random.randint(0, 1000),
            'retweets': random.randint(0, 500),
            'replies': random.randint(0, 100),
            'quotes': random.randint(0, 50),
            'hashtags': ['stockmarket', hashtag.strip('#')],
            'mentions': [f'expert_{random.randint(1,10)}']
        })

    df = pd.DataFrame(tweets)
    logging.info(f"Successfully generated {len(df)} mock tweets.")
    return df

if __name__ == '__main__':
    # Example usage
    hashtags_to_scrape = ["#nifty50", "#sensex", "#intraday", "#banknifty"]
    start_date = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")
    tweet_limit = 2000

    tweets_df = generate_mock_tweets(hashtags_to_scrape, start_date, tweet_limit)

    if not tweets_df.empty:
        print(tweets_df.head())
        # Save to a temporary file for inspection
        tweets_df.to_csv("temp_mock_tweets.csv", index=False)
