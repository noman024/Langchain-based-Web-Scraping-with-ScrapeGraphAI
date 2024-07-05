# scrap.py

import argparse
import json
import os
import re
from datetime import datetime
import logging
from scrapegraphai.graphs import SmartScraperGraph  # type: ignore

# Setup logging to append to a file in the logs directory
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler(os.path.join(logs_dir, "scrap.log"), mode='a'),
                        logging.StreamHandler()
                    ])

def create_safe_filename(prompt, url):
    """
    Generate a safe filename for a given prompt and URL.

    Args:
        prompt (str): The prompt for the filename.
        url (str): The URL for the filename.

    Returns:
        str: The generated safe filename in the format "{url_part}_{prompt_part}_{timestamp}.json".
    """
    url_part = re.sub(r'https?://(www\.)?', '', url)
    url_part = url_part.replace('.', '')
    url_part = url_part.split('/')[0]
    prompt_part = re.sub(r'\W+', '_', prompt)[:50]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{url_part}_{prompt_part}_{timestamp}.json"

def main():
    """
    Run the web scraper with the given prompt and source URL.

    Args:
        None

    Returns:
        None

    Raises:
        argparse.ArgumentError: If the arguments are not provided.
        Exception: If an error occurs during the execution of the SmartScraperGraph.
        IOError or OSError: If an error occurs while writing to the file.

    """
    parser = argparse.ArgumentParser(description='Run the web scraper with given prompt and source URL.')
    parser.add_argument('--prompt', type=str, required=True, help='The prompt for the scraper.')
    parser.add_argument('--source', type=str, required=True, help='The source URL to scrape.')
    args = parser.parse_args()

    logging.info(f"Starting scrape with...\nprompt: {args.prompt}\nsource: {args.source}")

    graph_config = {
        "llm": {
            "model": "ollama/mistral",
            "temperature": 1,
            "format": "json",
            "model_tokens": 2000,
            "base_url": "http://127.0.0.1:11434",
        },
        "embeddings": {
            "model": "ollama/nomic-embed-text",
            "temperature": 0,
            "base_url": "http://127.0.0.1:11434",
        }
    }

    try:
        smart_scraper_graph = SmartScraperGraph(
            prompt=args.prompt,
            source=args.source,
            config=graph_config
        )
        result = smart_scraper_graph.run()
    except Exception as e:
        logging.error(f"Error during SmartScraperGraph execution: {e}")
        return

    if not result:
        logging.info("Scraper returned an empty result.")
    else:
        file_name = create_safe_filename(args.prompt, args.source)
        results_dir = os.path.join(os.getcwd(), "results")
        os.makedirs(results_dir, exist_ok=True)
        file_path = os.path.join(results_dir, file_name)
        
        try:
            with open(file_path, 'w') as file:
                json.dump(result, file, indent=4)
            logging.info(f'Result successfully saved to {file_path}')
            print(file_path)  # For integration with main.py
        except (IOError, OSError) as e:
            logging.error(f'Error occurred while writing to the file: {e}')

if __name__ == "__main__":
    main()
