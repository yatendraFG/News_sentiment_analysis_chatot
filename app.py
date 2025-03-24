from idlelib.rpc import response_queue

import streamlit as st
from langchain_configuration import llm_chain, analyze_sentiment

st.title("News Sentiment analysis Tool")

st.write("Enter a query to get the sentiment of the news articles")

query = st.text_input("Query")

if st.button("Ananlysze sentiment"):
    if query:
        articles = analyze_sentiment(query)
        if articles:
            article_content = articles[0]
            response = llm_chain.run({'article':article_content})

            st.write(response)
        else:
            st.write("No relevant articles found for this query")
    else:
        st.write("Please enter a query")







