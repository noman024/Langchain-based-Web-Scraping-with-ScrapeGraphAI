@echo off

@REM REM Create and activate conda environment
@REM conda create -y -n scrap-noman python=3.9.16
@REM conda activate scrap-noman

@REM REM Install Ollama
@REM curl -fsSL https://ollama.com/install.sh | sh

REM Pull necessary models from Ollama
ollama pull llama3
ollama pull nomic-embed-text
ollama pull mistral

REM Install Playwright
playwright install

echo Setup completed. Now you can run 'conda activate scrap-noman' for activating the conda environment and run 'pip install -r requirements.txt' to install necessary dependencies.
