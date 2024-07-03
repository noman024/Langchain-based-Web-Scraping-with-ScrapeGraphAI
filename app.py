# app.py

import streamlit as st
import requests

st.title('LangChain-based Web Scraping with ScrapeGraphAI')

# User input fields
prompt = st.text_input('Enter your prompt:')
source = st.text_input('Enter the source URL:')

# Button to trigger scraping
if st.button('Scrape Data'):
    # API endpoint for FastAPI app
    endpoint = 'http://localhost:8000/scrape/'
    data = {'prompt': prompt, 'source': source}

    # Make POST request to FastAPI
    response = requests.post(endpoint, json=data)

    # Display results
    if response.status_code == 200:
        result = response.json()
        st.json(result)
    else:
        st.error(f'Error occurred: {response.json()["error"]}')
