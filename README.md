# LLM-based Web Scraping using ScrapeGraphAI

Author: Md Mutasim Billah Abu Noman Akanda, Machine Learning Engineer  
Date: 12 June 2024

## Project Description

This project demonstrates how to perform Langchain-based web scraping using ScrapeGraphAI. The script `scrap.py` allows users to scrape data from specified URLs using customizable graph pipelines and prompts, and saves the results in a JSON file (`result.json`).

## Folder Structure

```
langchain-based-web-scraping-with-scrapegraphai
├── install.sh
├── install.bat
├── requirements.txt
├── scrap.py
├── result.json
├── README.md
```


## Cloning the Repository

To clone this repository, run the following command in your terminal or command prompt:

```sh
git clone https://github.com/noman024/Langchain-based-Web-Scraping-with-ScrapeGraphAI.git
cd Langchain-based-Web-Scraping-with-ScrapeGraphAI
```

## Setup
- Python 3.9.16
- ScrapeGraphAI
- langChain
- WebKit
- Ollama
- Playwright, and so on.

For all the dependencies, please refer to `requirements.txt` and you won't need to install required dependencies manually. I have already do the automation in `install.sh` for linux and macos user and in `install.bat` for windows user.

## Automated Installation

To automate the environment setup and installation of requirements, follow these steps:

### For Unix-like systems (Linux, macOS)

```sh
sh install.sh
conda activate scrap-noman
```

### For Windows

- No need to create virtual environment
- Download ollama.exe manually from https://ollama.com/download/windows and then back to the terminal again:
```
install.bat
```

### Install Requirements

```
pip install -r requirements.txt
```

## Customizing and Running the `scrap.py` Script

- Edit `scrap.py` to change the graph pipeline, prompt, and URLs based on your requirements.
- Run the script
  ```
  python scrap.py
  ```

  ## Output

  The result of the scraping operation will be saved in `result.json` like below:

  ```
    {
      "Projects": [
          {
              "Title": "Neural Network for Digit Recognition",
              "Architecture": "Neural Network",
              "Tech": [
                  "Tensorflow",
                  "Keras",
                  "Scikit-learn",
                  "Seaborn",
                  "Matplotlib",
                  "Numpy",
                  "Pandas"
              ],
              "Git Link": "https://github.com/noman024/MNIST-digit-recognition-with-neuralNet-from-scratch.git",
              "Accuracy": "99.81%"
          },
          {
              "Title": "News Classification with Naive Bayes Theorem",
              "Architecture": "Multinomial Naive Bayes classifier",
              "Tech": [
                  "Scikit-learn",
                  "Numpy",
                  "Pandas"
              ],
              "Git Link": "https://github.com/noman024/news-classification-with-naive-bayes.git",
              "Accuracy": "98.85%"
          },
          {
              "Title": "Diabetic Classification with Support Vector Machine",
              "Architecture": "Support Vector Machine",
              "Tech": [
                  "Scikit-learn",
                  "Seaborn",
                  "Matplotlib",
                  "Numpy",
                  "Pandas"
              ],
              "Git Link": "https://github.com/noman024/diabetic-classification-with-svm.git",
              "Accuracy": "80.51%"
          },
          {
              "Title": "Parking Spot Tracking",
              "Tech": [
                  "Python",
                  "OpenCV",
                  "Torch",
                  "Ultralytics",
                  "YOLOv9",
                  "Numpy",
                  "JSON"
              ],
              "Git Link": "https://github.com/noman024/parking-spot-tracking.git"
          },
          {
              "Title": "Web Scraper",
              "Tech": [
                  "Streamlit",
                  "FastAPI",
                  "JSON",
                  "BeautifulSoup4",
                  "Python Request Module"
              ],
              "Git Link": "https://github.com/noman024/web-scraper.git"
          },
          {
              "Title": "Game Addiction Analysis with Neural Network (Deep Learning)",
              "Architecture": "Neural Network",
              "Tech": [
                  "Tensorflow",
                  "Keras",
                  "Scikit-learn",
                  "Seaborn",
                  "Matplotlib",
                  "Numpy",
                  "Pandas"
              ],
              "Git Link": "https://github.com/noman024/game-addiction-analysis-neuralnet.git"
          },
          {
              "Title": "MNIST Digit Recognition with Neural Network from Scratch (Deep Learning)",
              "Architecture": "Neural Network",
              "Tech": [
                  "Python",
                  "Tensorflow",
                  "Keras"
              ],
              "Git Link": "Not Shared"
          }
      ],
      "Personal Information": {
          "Name": "Md. Noman",
          "Positions": [
              {
                  "Position": "Developer",
                  "Institution": "Not Specified",
                  "Tenure": "Present"
              },
              {
                  "Position": "Data Scientist",
                  "Institution": "Not Specified",
                  "Tenure": "Past"
              }
          ],
          "Academics": [
              {
                  "Degree": "Master of Science in Computer Science",
                  "Institution": "University of ABC",
                  "Year": "20XX"
              },
              {
                  "Degree": "Bachelor of Science in Computer Science",
                  "Institution": "University of XYZ",
                  "Year": "20XX"
              }
          ]
      }
  }
  ```

## Feel Free to Contribute

Feel free to contribute to this project by forking it and creating pull requests for any improvements or fixes. If you encounter any issues or have suggestions, please raise them in the Issues section of the repository. Your contributions and feedback are greatly appreciated!