# Indian Stock Market Intelligence System

## Project Overview

This project is a real-time data collection and analysis system for Indian stock market intelligence. It is designed to collect tweets related to the Indian stock market, process them, perform sentiment analysis, and visualize the results. The system is built with a modular architecture, separating concerns into data collection, processing, and analysis.

### Key Features:

- **Modular Design:** The project is structured into distinct modules for collection, processing, and analysis, making it easy to maintain and extend.
- **Data Processing:** The system includes a robust data processing pipeline that cleans, normalizes, and deduplicates the tweet data.
- **Efficient Storage:** The processed data is stored in the efficient Parquet format.
- **Sentiment Analysis:** A rule-based sentiment analysis is performed on the tweets to classify them as positive, negative, or neutral.
- **Visualization:** The sentiment distribution is visualized as a bar chart.

### Data Collection Workaround

Due to the current technical challenges and restrictions with scraping Twitter/X data without a paid API, the data collection module has been implemented with a mock data generator. This allows the rest of the system's functionality to be demonstrated. The mock data generator creates a realistic dataset of tweets with the required fields.

## Project Structure

```
web_project1/
├── data/
│   ├── processed_tweets.parquet
│   └── sentiment_distribution.png
├── src/
│   ├── __init__.py
│   ├── analysis/
│   │   ├── __init__.py
│   │   └── analyzer.py
│   ├── collection/
│   │   ├── __init__.py
│   │   └── collector.py
│   ├── processing/
│   │   ├── __init__.py
│   │   └── processor.py
│   └── main.py
├── README.md
└── requirements.txt
```

## Setup Instructions

### 1. Install `uv` (Python package manager)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Create and initialize a virtual environment

```bash
uv venv
uv init
```

### 3. Activate the virtual environment

```bash
source .venv/bin/activate
```

### 4. Install project dependencies

```bash
uv pip install -r requirements.txt
```

Or, to sync with `pyproject.toml`:

```bash
uv sync
```

### 5. (Optional) Freeze current dependencies

```bash
uv pip freeze > requirements.txt
```

### Running the Pipeline

To run the entire data collection, processing, and analysis pipeline, execute the `main.py` script from the root of the `web_project1` directory:

```bash
python web_project1/src/main.py
```

This will:

1.  Generate mock tweet data.
2.  Process the data.
3.  Save the processed data to `web_project1/data/processed_tweets.parquet`.
4.  Perform sentiment analysis.
5.  Save a visualization of the sentiment distribution to `web_project1/data/sentiment_distribution.png`.

## Sample Output

The following image shows the distribution of sentiment in the generated mock data:

![Sentiment Distribution](data/sentiment_distribution.png)
