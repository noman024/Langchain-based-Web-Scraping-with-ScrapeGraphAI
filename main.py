# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from subprocess import run, PIPE
import json

app = FastAPI()

class ScrapeRequest(BaseModel):
    prompt: str
    source: str

@app.post("/scrape/")
def scrape_data(request: ScrapeRequest):
    # Prepare command to run scrap.py with inputs
    cmd = ['python', 'scrap.py', '--prompt', request.prompt, '--source', request.source]

    # Run the command and capture output
    result = run(cmd, stdout=PIPE, stderr=PIPE, text=True)
    if result.returncode != 0:
        return {"error": result.stderr}

    # Load the JSON result from file
    try:
        with open('test.json', 'r') as f:
            output = json.load(f)
    except (IOError, OSError) as e:
        return {"error": f'Error reading JSON file: {e}'}

    return output
