"""Data processing module for cleaning and normalizing tweet data."""

import logging
import pandas as pd

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_tweets(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and normalizes a DataFrame of tweets.

    Args:
        df: A pandas DataFrame containing the tweet data.

    Returns:
        A pandas DataFrame with cleaned and normalized data.
    """
    if df.empty:
        logging.warning("Input DataFrame is empty. No processing will be done.")
        return df

    # 1. Handle duplicates
    df.drop_duplicates(subset=['content', 'username', 'timestamp'], inplace=True)
    logging.info(f"Removed duplicates, {len(df)} tweets remaining.")

    # 2. Handle missing values (though mock data is clean)
    df.fillna({'content': ''}, inplace=True)

    # 3. Normalize text: lowercase
    df['content'] = df['content'].str.lower()

    # 4. Convert timestamp to datetime objects
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # 5. Handle unicode (though less relevant for mock data)
    df['content'] = df['content'].str.encode('ascii', 'ignore').str.decode('ascii')

    logging.info("Successfully processed tweets.")
    return df

def save_to_parquet(df: pd.DataFrame, filepath: str):
    """
    Saves a DataFrame to a Parquet file.

    Args:
        df: The DataFrame to save.
        filepath: The path to the output Parquet file.
    """
    try:
        df.to_parquet(filepath, index=False)
        logging.info(f"Successfully saved data to {filepath}")
    except Exception as e:
        logging.error(f"Failed to save data to Parquet file: {e}")

if __name__ == '__main__':
    # Example usage with mock data
    # In a real pipeline, this would be integrated with the collector
    from datetime import datetime, timedelta, timezone
    from web_project1.src.collection.collector import generate_mock_tweets

    hashtags = ["#nifty50", "#sensex", "#intraday", "#banknifty"]
    since = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")
    limit = 2500 # Generate more to test deduplication

    mock_df = generate_mock_tweets(hashtags, since, limit)
    processed_df = process_tweets(mock_df)

    if not processed_df.empty:
        print(processed_df.head())
        save_to_parquet(processed_df, "processed_tweets.parquet")
