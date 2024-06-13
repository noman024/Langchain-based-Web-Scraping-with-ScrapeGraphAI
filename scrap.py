from scrapegraphai.graphs import SmartScraperGraph, SmartScraperMultiGraph
from scrapegraphai.utils import prettify_exec_info
import json

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
   prompt="List me the projects name with other necessary information",
   # also accepts a string with the already downloaded HTML code
   source="https://noman024.github.io/",
   # source="https://bstock.com/supplystore/auctions/cell-phones/samsung-galaxy-s23-ultra/id/619076/",
   # source="https://www.daraz.com.bd/featurephones/?spm=a2a0e.home.cate_6.2.735212f7idOF4z",
   config=graph_config
)

result = smart_scraper_graph.run()

# Define the file path
file_path = "result.json"

# Dump the JSON data to the file
try:
    with open(file_path, 'w') as file:
        json.dump(result, file, indent=4)
except (IOError, OSError) as e:
    print(f'Error occurred while writing to the file: {e}')

# print(result)