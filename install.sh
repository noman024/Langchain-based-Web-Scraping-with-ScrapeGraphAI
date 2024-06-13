#!/bin/bash

# Create and activate conda environment
conda create -y -n scrap-noman python=3.9.16
conda activate scrap-noman

# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull necessary models from Ollama
ollama pull llama3
ollama pull nomic-embed-text
ollama pull mistral

# Install Playwright
playwright install

echo "Setup completed. Now you can run 'conda activate scrap-noman' for activating the conda environment and run 'pip install -r requirements.txt' to install necessary dependencies."
