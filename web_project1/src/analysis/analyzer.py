"""
Data analysis module for performing sentiment analysis and generating visualizations.
"""

import logging
import pandas as pd
import matplotlib.pyplot as plt

# Setup logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def perform_sentiment_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """
    Performs sentiment analysis on the tweet content.
    Since we don't have labeled data, we'll create a simple rule-based sentiment score.
    A more advanced approach would use a pre-trained model.

    Args:
        df: A pandas DataFrame with a 'content' column.

    Returns:
        A pandas DataFrame with an added 'sentiment' column.
    """
    if "content" not in df.columns:
        logging.error("DataFrame must contain a 'content' column.")
        return df

    # Simple rule-based sentiment
    positive_words = ["buy", "bullish", "profit", "up", "high", "rally"]
    negative_words = ["sell", "bearish", "loss", "down", "low", "crash"]

    def get_sentiment(text):
        score = 0
        for word in positive_words:
            if word in text:
                score += 1
        for word in negative_words:
            if word in text:
                score -= 1

        if score > 0:
            return "positive"
        elif score < 0:
            return "negative"
        else:
            return "neutral"

    df["sentiment"] = df["content"].apply(get_sentiment)
    logging.info("Performed sentiment analysis.")
    return df


def visualize_sentiment_distribution(df: pd.DataFrame, output_path: str):
    """
    Visualizes the distribution of sentiment scores.

    Args:
        df: A pandas DataFrame with a 'sentiment' column.
        output_path: The path to save the output plot.
    """
    if "sentiment" not in df.columns:
        logging.error("DataFrame must contain a 'sentiment' column for visualization.")
        return

    sentiment_counts = df["sentiment"].value_counts()

    plt.figure(figsize=(8, 6))
    sentiment_counts.plot(kind="bar", color=["green", "red", "blue"])
    plt.title("Sentiment Distribution of Tweets")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Tweets")
    plt.xticks(rotation=0)
    plt.savefig(output_path)
    logging.info(f"Sentiment distribution plot saved to {output_path}")
    plt.close()


if __name__ == "__main__":
    # Example usage
    # Load the processed data
    try:
        processed_df = pd.read_parquet("processed_tweets.parquet")

        # Perform analysis
        analyzed_df = perform_sentiment_analysis(processed_df)
        print(analyzed_df[["content", "sentiment"]].head())

        # Visualize
        visualize_sentiment_distribution(analyzed_df, "sentiment_distribution.png")

    except FileNotFoundError:
        logging.error(
            "processed_tweets.parquet not found. Please run the processing script first."
        )
    except Exception as e:
        logging.error(f"An error occurred: {e}")
