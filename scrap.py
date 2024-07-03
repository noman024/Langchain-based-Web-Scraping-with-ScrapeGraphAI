# '''
# Author: Md Mutasim Billah Abu Noman Akanda, Machine Learning Engineer  
# Date: 12 June 2024
# '''

# from scrapegraphai.graphs import SmartScraperGraph, SmartScraperMultiGraph
# from scrapegraphai.utils import prettify_exec_info
# import json

# graph_config = {
#    "llm": {
#       "model": "ollama/mistral",
#       "temperature": 1,
#       "format": "json",  # Ollama needs the format to be specified explicitly
#       "model_tokens": 2000, #  depending on the model set context length
#       "base_url": "http://127.0.0.1:11434",  # set ollama URL of the local host (YOU CAN CHANGE IT, if you have a different endpoint
#    },
#    "embeddings": {
#       "model": "ollama/nomic-embed-text",
#       "temperature": 0,
#       "base_url": "http://127.0.0.1:11434",  # set ollama URL
#    }
#    # "verbose": True,
#    # "headless": False
# }

# # ************************************************
# # Create the SmartScraperGraph instance and run it
# # ************************************************

# smart_scraper_graph = SmartScraperGraph(
#    prompt="Scrap the information about the product name, price and description",
#    # also accepts a string with the already downloaded HTML code
#    source="https://www.daraz.com.bd/products/bogesi-i132914772-s1054216188.html?spm=a2a0e.home.flashSale.3.735212f7UWKDNp",
#    # source="https://bstock.com/supplystore/auctions/cell-phones/samsung-galaxy-s23-ultra/id/619076/",
#    # source="https://www.daraz.com.bd/featurephones/?spm=a2a0e.home.cate_6.2.735212f7idOF4z",
#    config=graph_config
# )

# result = smart_scraper_graph.run()

# # Define the file path
# file_path = "test.json"

# # Dump the JSON data to the file
# try:
#     with open(file_path, 'w') as file:
#         json.dump(result, file, indent=4)
# except (IOError, OSError) as e:
#     print(f'Error occurred while writing to the file: {e}')

# # print(result)

# modified code for passing cmd arguments

'''
Author: Md Mutasim Billah Abu Noman Akanda, Machine Learning Engineer  
Date: 12 June 2024
'''

import argparse
from scrapegraphai.graphs import SmartScraperGraph, SmartScraperMultiGraph
from scrapegraphai.utils import prettify_exec_info
import json

# Command-line argument parsing
parser = argparse.ArgumentParser(description='Run the web scraper with given prompt and source URL.')
parser.add_argument('--prompt', type=str, required=True, help='The prompt for the scraper.')
parser.add_argument('--source', type=str, required=True, help='The source URL to scrape.')

args = parser.parse_args()

graph_config = {
   "llm": {
      "model": "ollama/mistral",
      "temperature": 1,
      "format": "json",  # Ollama needs the format to be specified explicitly
      "model_tokens": 2000, #  depending on the model set context length
      "base_url": "http://127.0.0.1:11434",  # set ollama URL of the local host (YOU CAN CHANGE IT, if you have a different endpoint
   },
   "embeddings": {
      "model": "ollama/nomic-embed-text",
      "temperature": 0,
      "base_url": "http://127.0.0.1:11434",  # set ollama URL
   }
   # "verbose": True,
   # "headless": False
}

# ************************************************
# Create the SmartScraperGraph instance and run it
# ************************************************

smart_scraper_graph = SmartScraperGraph(
   prompt=args.prompt,
   source=args.source,
   config=graph_config
)

result = smart_scraper_graph.run()

# Define the file path
file_path = "test.json"

# Dump the JSON data to the file
try:
    with open(file_path, 'w') as file:
        json.dump(result, file, indent=4)
except (IOError, OSError) as e:
    print(f'Error occurred while writing to the file: {e}')

# print(result)
