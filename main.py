# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from subprocess import run, PIPE
import json
import os
import time
import logging

app = FastAPI()
logs_dir = os.path.join(os.getcwd(), "logs")
try:
    os.makedirs(logs_dir, exist_ok=True)
except OSError as e:
    logging.error(f"Error creating directory {logs_dir}: {e}")
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler(os.path.join(logs_dir, "main.log"), mode='a'),
                        logging.StreamHandler()
                    ])

class ScrapeRequest(BaseModel):
    prompt: str
    source: str

RETRIES = 5
WAIT_TIME = 1

@app.post("/scrape/")
def scrape_data(request: ScrapeRequest):
    """
    Scrape data based on the given request.

    Parameters:
        request (ScrapeRequest): The request object containing the prompt and source.

    Returns:
        dict: A dictionary containing the scraped data if successful, or an error message if there was an issue.

    Raises:
        None

    Notes:
        - The function logs the received request details.
        - It executes the `scrap.py` script with the provided prompt and source.
        - It checks the return code of the subprocess and logs any errors.
        - It retrieves the output lines from the subprocess.
        - It checks if the output lines are empty and logs an error if so.
        - It retrieves the file path from the last line of the output lines.
        - It retries the file existence check for a maximum of `RETRIES` times.
        - If the file is found, it breaks the loop.
        - If the file is not found after `RETRIES` retries, it logs an error and returns an error message.
        - It reads the JSON data from the file and logs it.
        - If there is an error reading the JSON file, it logs the error and returns an error message.
        - It returns the scraped data as a dictionary.

    """
    logging.info(f"Received scrape request with...\nprompt: {request.prompt}\nsource: {request.source}")
    cmd = ['python', 'scrap.py', '--prompt', request.prompt, '--source', request.source]
    result = run(cmd, stdout=PIPE, stderr=PIPE, text=True)
    logging.info(f"Subprocess result: {result}")

    if result.returncode != 0:
        logging.error(f"Command failed with exit code {result.returncode}: {result.stderr}")
        return {"error": f"Command failed with exit code {result.returncode}: {result.stderr}"}

    output_lines = result.stdout.splitlines()
    logging.info(f"Output lines: {output_lines}")

    if not output_lines:
        logging.error("No output from scrap.py")
        return {"error": "No output from scrap.py"}

    file_path = output_lines[-1]
    logging.info(f"File path: {file_path}")

    for i in range(RETRIES):
        if os.path.exists(file_path):
            logging.info(f"File {file_path} found after {i + 1} retries.")
            break
        time.sleep(WAIT_TIME * (i + 1))
    else:
        logging.error(f"File {file_path} not found after {RETRIES} retries.")
        return {"error": f"File {file_path} not found after {RETRIES} retries."}

    try:
        with open(file_path, 'r') as f:
            output = json.load(f)
            logging.info(f"Output: {output}")
    except (IOError, OSError) as e:
        logging.error(f'Error reading JSON file: {e}')
        return {"error": f'Error reading JSON file: {e}'}

    return {"result": output}
