# app.py

import streamlit as st
import requests
import logging
import os

# Setup logging to append to a file in the logs directory
logs_dir = os.path.join(os.getcwd(), "logs")
try:
    os.makedirs(logs_dir, exist_ok=True)
except OSError as e:
    print(f'Error creating directory {logs_dir}: {e}')
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler(os.path.join(logs_dir, "app.log"), mode='a'),
                        logging.StreamHandler()
                    ])

st.title('LangChain-based Web Scraping with ScrapeGraphAI')

def validate_input(prompt, source):
    """
    Validates the input prompt and source URL.
    
    Args:
        prompt: The prompt input to be validated.
        source: The source URL input to be validated.
    
    Returns:
        bool: True if both prompt and source are provided, False otherwise.
    """
    if not prompt:
        st.error("Prompt is required.")
        return False
    if not source:
        st.error("Source URL is required.")
        return False
    return True

prompt = st.text_input('Enter the prompt:')
source = st.text_input('Enter the source URL:')

if st.button('Scrape'):
    if validate_input(prompt, source):
        logging.info(f"Scraping requested with...\nprompt: {prompt}\nsource: {source}")
        with st.spinner('Scraping in progress...'):
            try:
                response = requests.post("http://127.0.0.1:8000/scrape/", json={"prompt": prompt, "source": source})
                response.raise_for_status()  # Raise an HTTPError for bad responses
                try:
                    response_data = response.json()
                except requests.exceptions.JSONDecodeError as e:
                    st.error(f'Error decoding JSON: {e}')
                    logging.error(f'Error decoding JSON: {e}')
                    response_data = None

                if response_data is not None:
                    if 'error' in response_data:
                        st.error(f'Error occurred: {response_data["error"]}')
                        logging.error(f'Error occurred: {response_data["error"]}')
                    else:
                        st.success('Scraping successful!')
                        st.json(response_data['result'])
                        logging.info('Scraping successful!')
            except requests.exceptions.RequestException as e:
                st.error(f'Request failed: {e}')
                logging.error(f'Request failed: {e}')
