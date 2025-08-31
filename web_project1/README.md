# Technical Assignment – Software Developer Position

**Qode Advisors LLP**

## Overview

You are required to build a data collection and analysis system for real-time market intelligence. This assignment evaluates your Python proficiency, system design capabilities, and understanding of financial markets.

---

## Task Requirements

### 1. Data Collection

- Scrape Twitter/X for tweets containing Indian stock market discussions
- Focus on hashtags: `#nifty50`, `#sensex`, `#intraday`, `#banknifty`
- Extract: username, timestamp, content, engagement metrics, mentions, hashtags
- Target: **Minimum 2000 tweets from the last 24 hours**
- **Constraint:** No paid APIs allowed

### 2. Technical Implementation

- Implement efficient data structures for real-time processing
- Handle rate limiting and anti-bot measures creatively
- Optimize for both time and space complexity
- Include proper error handling and logging
- Code must be production-ready with appropriate documentation

### 3. Data Processing & Storage

- Clean and normalize collected data
- Design an efficient storage schema (**Parquet format preferred**)
- Implement data deduplication mechanisms
- Handle Unicode and special characters in Indian language content

### 4. Analysis & Insights

Convert textual data into quantitative signals for algorithmic trading:

- **Text-to-Signal Conversion:** Transform tweet content into numerical vectors using TF-IDF, word embeddings, or custom feature engineering
- **Memory-efficient visualization:** Create low-memory plotting solutions for large datasets (streaming plots, data sampling techniques)
- **Signal aggregation:** Combine multiple text features into composite trading signals with confidence intervals

### 5. Performance Optimization

- Implement concurrent processing where applicable
- Memory-efficient data handling for large datasets
- Consider scalability for processing 10x more data

---

## Deliverables

Submit as a GitHub repository containing:

- Complete codebase with proper structure and documentation
- README with setup instructions and project overview
- Requirements file and environment setup
- Sample output data and analysis results
- Brief technical documentation explaining your approach

Repository should demonstrate **professional software development practices**.

---

## Evaluation Criteria

- Code quality and software engineering practices
- Data structure selection and algorithmic efficiency
- Understanding of Indian market dynamics
- Problem-solving approach for technical constraints
- Scalability and maintainability of solution

---

## Time Limit

**24 hours from assignment receipt**

> **Note:** This assignment tests real-world problem-solving skills. Creative solutions to technical challenges are encouraged. Focus on demonstrating your ability to build robust, efficient systems rather than just completing the task.
