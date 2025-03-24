import os
from dotenv import load_dotenv
from langchain import OpenAI, LLMChain, PromptTemplate
from sqlalchemy import result_tuple
from newsapi import NewsApiClient

# load env variables

load_dotenv()

# access api keys

openai_api_key = os.getenv("OPENAI_API_KEY")
newsapi_key = os.getenv("NEWSAPI_KEY")

# initilize the openAI API

openai = OpenAI(api_key=openai_api_key)

# define the langchain template sentiment analysis template =
template = """
You are an AI assistant helping for finding the sentiment on news articles Given that the following news 
article, analyze it's sentiment(positive, negative and neutral)


Article:{article}"""

prompt = PromptTemplate(template=template, input_variables=['article'])

llm_chain = LLMChain(prompt=prompt, llm=openai)

# initilize NewsAPI
newsapi = NewsApiClient(api_key=newsapi_key)


def get_news_article(query):
    articles = newsapi.get_everything(q=query, sort_by='relevancy')
    return articles['articles']

def extract_article_content(articles):
    content = []
    for article in articles:
        content.append(article['content'])
    return content

def analyze_sentiment(query):
    articles = get_news_article(query)
    content = extract_article_content(articles)

    if content:
        article_text = content[0]
        result = llm_chain.run({"article":article_text})

        return result
    else:
        return "No aticles found for the given query!!! try some another query"


# usage

# query =


