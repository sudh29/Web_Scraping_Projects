import logging
import os
from datetime import datetime, timedelta, timezone
from collection.collector import DataCollector
from processing.processor import DataProcessor
from analysis.analyzer import DataAnalyzer, Visualizer

# Setup logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

class Pipeline:
    """A class to run the data collection, processing, and analysis pipeline."""

    def __init__(self, hashtags: list[str], since_date: str, limit: int, data_dir: str = "data"):
        """
        Initializes the Pipeline.
        Args:
            hashtags: A list of hashtags for mock tweets.
            since_date: The start date for mock tweets (YYYY-MM-DD).
            limit: The number of mock tweets to generate.
            data_dir: The directory to store output files.
        """
        self.hashtags = hashtags
        self.since_date = since_date
        self.limit = limit
        self.data_dir = data_dir
        self.processed_data_path = os.path.join(self.data_dir, "processed_tweets.parquet")
        self.visualization_path = os.path.join(self.data_dir, "sentiment_distribution.png")

    def run(self):
        """Executes the entire data pipeline."""
        logging.info("Starting the data pipeline.")
        os.makedirs(self.data_dir, exist_ok=True)

        # Data Collection
        collector = DataCollector(self.hashtags, self.since_date, self.limit)
        raw_tweets_df = collector.generate_mock_tweets()
        if raw_tweets_df.empty:
            logging.error("No tweets were collected. Exiting.")
            return

        # Data Processing
        processor = DataProcessor(raw_tweets_df)
        processed_tweets_df = processor.process_tweets()
        if processed_tweets_df.empty:
            logging.error("No tweets left after processing. Exiting.")
            return
        processor.save_to_parquet(self.processed_data_path)

        # Analysis and Visualization
        analyzer = DataAnalyzer(processed_tweets_df)
        analyzed_df = analyzer.perform_sentiment_analysis()
        visualizer = Visualizer(analyzed_df)
        visualizer.visualize_sentiment_distribution(self.visualization_path)

        logging.info("Pipeline finished successfully.")

if __name__ == "__main__":
    hashtags_to_scrape = ["#nifty50", "#sensex", "#intraday", "#banknifty"]
    start_date = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")
    tweet_limit = 2000

    pipeline = Pipeline(hashtags_to_scrape, start_date, tweet_limit)
    pipeline.run()
