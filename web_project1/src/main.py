"""Main entry point for the Twitter data collection and analysis application."""

import logging
from datetime import datetime, timedelta, timezone

from collection.collector import generate_mock_tweets
from processing.processor import process_tweets, save_to_parquet
from analysis.analyzer import perform_sentiment_analysis, visualize_sentiment_distribution

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """Main function to run the data pipeline."""
    logging.info("Starting the data collection and analysis pipeline.")

    # 1. Data Collection
    hashtags_to_scrape = ["#nifty50", "#sensex", "#intraday", "#banknifty"]
    start_date = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")
    tweet_limit = 2000

    raw_tweets_df = generate_mock_tweets(hashtags_to_scrape, start_date, tweet_limit)

    if raw_tweets_df.empty:
        logging.error("No tweets were collected. Exiting pipeline.")
        return

    # 2. Data Processing
    processed_tweets_df = process_tweets(raw_tweets_df)

    if processed_tweets_df.empty:
        logging.error("No tweets remaining after processing. Exiting pipeline.")
        return

    # 3. Data Storage
    processed_data_path = "data/processed_tweets.parquet"
    save_to_parquet(processed_tweets_df, processed_data_path)

    # 4. Analysis
    analyzed_df = perform_sentiment_analysis(processed_tweets_df)

    # 5. Visualization
    visualization_path = "data/sentiment_distribution.png"
    visualize_sentiment_distribution(analyzed_df, visualization_path)

    logging.info("Pipeline finished successfully.")

if __name__ == "__main__":
    # Create data directory if it doesn't exist
    import os
    if not os.path.exists("data"):
        os.makedirs("data")

    main()
