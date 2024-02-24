# Assignment 1: Linguistic Analysis with spaCy

## Description of the assignment
This project uses spaCy to extract linguistic features from The Uppsala Student English Corpus (USE) in the data folder, including the relative frequency of nouns, verbs, adjectives, and adverbs per 10.000 words and the total number of unique PER, LOC, and ORG entities for each text. Lastly, the extracted information is transformed into a data frame using pandas and saved as a CSV file in the out folder. 

## Installation

 1. Clone the repository using Git 
```sh
git clone https://github.com/trinerye/language_analytics_2024.git/
```

2. Change directory to the assignment folder 
```sh
cd assignment_1
```

3. Before running the script make sure to install spaCy and Pandas either in the terminal or by running the setup.sh 
```sh
pip install spacy pandas 
python -m spacy download en_core_web_md
```
```sh
bash setup.sh
```
4. To run the code open assignment1.ipynb and run all
```sh
assignment1.ipynb
```

## Usage
The main function takes two parameters - the in_folderpath and the out_folderpath - representing the in folder with the corpus text and the out folder for the saved csv files. If you structure the folders differently, remember to update the file paths accordingly.

```sh
def main(in_folderpath, out_folderpath):
# code
if __name__ == "__main__":

 main("../in", "../out")
```
