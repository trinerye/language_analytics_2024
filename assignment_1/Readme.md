# Assignment 1: Linguistic Analysis with spaCy

## Description of the assignment
This project uses spaCy to extract linguistic features from The Uppsala Student English Corpus (USE) in the in folder, including the relative frequency of nouns, verbs, adjectives, and adverbs per 10.000 words and the total number of unique PER, LOC, and ORG entities for each text. Lastly, the extracted information is transformed into a data frame using pandas and saved as a CSV file in the ``out`` folder. 

## Installation

 1. Open a terminal and clone the repository using Git 
```sh
git clone https://github.com/trinerye/visual_analytics_2024.git
```

2. Change directory to the assignment folder 
```sh
cd assignment_1
```

3. Run the setup script to install pandas and spacy. It simultaneously creates a virtual environment containing the specific versions used to develop this project. 
```sh
bash setup.sh
```

4. Activate the environment and run the main script. Be aware that it deactivates the environment again after running the  script.
```sh
bash run.sh
```
```sh
# Activate the environment (Unix/macOS)
source ./A1_env/bin/activate
# Run the code
python src/linguistic_analysis.py 
# Deactivate the enviroment
deactivate
```

