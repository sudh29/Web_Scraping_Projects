"""Data collection module for scraping and processing Twitter data.

This module handles the collection and processing of Indian stock market related tweets.
"""

from datetime import datetime, timedelta

import pandas as pd
import snscrape.modules.twitter as sntwitter

# Query parameters
hashtags = ["#nifty50", "#sensex", "#intraday", "#banknifty"]
since_date = (datetime.utcnow() - timedelta(days=1)).strftime("%Y-%m-%d")
query = " OR ".join(hashtags) + f" since:{since_date}"

tweets = []
limit = 2000  # target number of tweets


for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i >= limit:
        break
    tweets.append(
        [
            tweet.user.username,
            tweet.date,
            tweet.content,
            tweet.likeCount,
            tweet.retweetCount,
            tweet.replyCount,
            tweet.quoteCount,
            list(tweet.hashtags) if tweet.hashtags else [],
            [u.username for u in tweet.mentionedUsers] if tweet.mentionedUsers else [],
        ]
    )

# Save to DataFrame
df = pd.DataFrame(
    tweets,
    columns=[
        "username",
        "timestamp",
        "content",
        "likes",
        "retweets",
        "replies",
        "quotes",
        "hashtags",
        "mentions",
    ],
)

print(df.head())
df.to_csv("stock_tweets.csv", index=False)
