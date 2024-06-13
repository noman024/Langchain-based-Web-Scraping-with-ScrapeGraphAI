# LLM-based Web Scraping using ScrapeGraphAI

Author: Md Mutasim Billah Abu Noman Akanda, Machine Learning Engineer
Date: 12 June 2024

## Project Description

This project demonstrates how to perform LLM-based web scraping using ScrapeGraphAI. The script `scrap.py` scrapes any kind of data without the need of understading HTML or page layout from specified URLs and saves the results in a JSON file.

## Folder Structure
```
web-scrap-scrapegraphai
|------------------------------requirements.txt
|------------------------------scrap.py
|------------------------------result.json
```


## Setup

### Prerequisites

- Python 3.9.16
- ScrapeGraphAI
- Ollama
- Playwright

Please follow the `requirements.txt` for complete prerequisites.

### Steps

#### For Windows, WSL, or Linux

1. **Create a virtual environment (For WSL or Linux users only):**
    ```sh
    conda create -n scrap python=3.9.16
    ```
2. **Activate the virtual environment (For WSL or Linux users only):**
    ```sh
    conda activate scrap
    ```
3. **Check Python installation:**
    ```sh
    python --version
    ```
4. **Change the directory where you want to do the task:**
    ```sh
    cd "your/directory/path"
    ```
5. **Install ScrapeGraphAI:**
    ```sh
    pip install scrapgraphai
    ```
6. **Install Ollama:**

    For WSL or Linux users:
    ```sh
    curl -fsSL https://ollama.com/install.sh | sh
    ```

    For Windows users:
    Download and install from [Ollama](https://ollama.com/download/windows).

7. **Pull necessary models from Ollama:**
    ```sh
    ollama pull llama3
    ollama pull nomic-embed-text
    ollama pull mistral
    ```
8. **Install Playwright:**
    ```sh
    playwright install
    ```

### Running the Script

1. Code your Python script in `scrap.py` for choosing your own graph pipeline.
2. Run the script for using mine:
    ```sh
    python scrap.py
    ```
## Output
The result of the scraping is saved in `result.json`.