Sentiment Analysis on News Articles using LangChain & OpenAI

Overview

This project is an AI-powered sentiment analysis tool for news articles. It utilizes LangChain and OpenAI API to analyze the sentiment (positive, negative, or neutral) of news articles fetched from the NewsAPI.

Features

Fetches relevant news articles using NewsAPI.

Performs sentiment analysis on the article content.

Uses LangChain and OpenAI API for processing.

Prerequisites

Ensure you have Python installed (>=3.7). Install required dependencies using:

pip install langchain openai python-dotenv newsapi-python sqlalchemy

Setup

Create a .env file in the root directory and add your API keys:

OPENAI_API_KEY=your_openai_api_key
NEWSAPI_KEY=your_newsapi_key

Load the environment variables in the script by using dotenv.

How It Works

Fetches news articles related to a given query.

Extracts the article content.

Sends the content to OpenAI's API for sentiment analysis.

Returns the sentiment classification.

Usage

Run the script by providing a search query:

query = "Technology"
sentiment = analyze_sentiment(query)
print("Sentiment Analysis Result:", sentiment)

Example Output

Sentiment Analysis Result: Positive

Notes

Make sure to replace your_openai_api_key and your_newsapi_key with valid API keys.

Modify the query in analyze_sentiment(query) to analyze different topics.

License

This project is licensed under the MIT License.

