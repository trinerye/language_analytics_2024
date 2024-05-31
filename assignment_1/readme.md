# Assignment 1: Linguistic Analysis with spaCy

## About

This project uses ``spaCy`` to extract linguistic features from ``The Uppsala Student English Corpus (USE)`` to *calculate the relative frequency of nouns, verbs, adjectives, and adverbs per 10,000 words and the total number of unique PER, LOC, and ORG entities for each text*. 

The ``src`` directory contains one script: 

- **linguistic_analysis.py:** Uses the ``en_core_web_md`` pipeline from spaCy to extract linguistic features from the dataset and saves the results as a csv file in the ``out`` directory.


### Data

According to the USE manual, the dataset consists of "1,489 essays written by 440 Swedish university students" (Axelsson, 2003) over three semesters. Hence, each folder contains essays that vary in language and topics, reflecting the progression of the course. 

Download the [The Uppsala Student English Corpus (USE)]( https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457) from the Oxford Text Archive, specifically the USEcorpus.zip file, unzip it and place the ``USEcorpus`` folder in the ``in`` directory. 


### Model

This project uses the English [en_core_web_md](https://spacy.io/models/en) pipeline from spaCy to tokenize the USE dataset and perform part-of-speech (POS) tagging and named entity recognition (NER) on it. 

##  File Structure

```
└── assignment_1
        |
        |
        ├── in
        │   └── USEcorpus 
        │       ├── a1 (contains 303 files)
        |       ├── a2 (contains 344 files)
        |       ├── ...
        |       └── c1 (contains 7 files)
        |
        ├── out
        |   ├── a1_linguistic_analysis.csv
        |   ├── a2_linguistic_analysis.csv
        |   ├── ...
        |   └── c1_linguistic_analysis.csv
        |
        ├── src
        │   └── lingustic_analysis.py
        │     
        ├── readme.md
        ├── requirements.txt
        ├── run.sh
        └── setup.sh
```

## Usage

If you want to reproduce this project, please follow the steps below. The instructions will help you set up the environment, run the script and explain the available command-line options. 

### Pre-Requisites

*Please make sure to install the following requirements before running the script.*

**Python**: version 3.12.3

### Installation

**1.** Clone the repository using Git.
```sh
git clone https://github.com/trinerye/language_analytics_2024.git 
```

**2.** Change directory to the assignment folder.
```sh
cd assignment_1
```

**3.** Run ``setup.sh`` to create an environment and install the dependencies needed for this project. 
```sh
bash setup.sh
```
**4.** Run ``run.sh`` to activate the environment and run the main script. 
  
```sh
bash run.sh
```
```sh
...
# Activate the environment (Unix/macOS)
source ./LA_A1_env/bin/activate

# Run the code
python src/linguistic_analysis.py -p "en_core_web_md" -e "latin1"

# Deactivate the environment
deactivate
```

### Command Line Interface  

This project supports the following command-line options to customize the script. *See table for reference.*

|Flag      |Shorthand|Description                                                                |Type |Required|
|----------|---------|---------------------------------------------------------------------------|-----|--------|
|--pipeline|-p       |Specifies the spaCy pipeline used for the linguistic analysis              |str  |TRUE    |
|--encoding|-e       |Specifies which encoding to use to open the texts from the dataset|str  |TRUE    |

Go to https://spacy.io/models to find the spaCy pipeline you want to work with and add it as a command-line argument when running the script. Remember to change the encoding accordingly to ensure the text is readable. 

*See standard encodings for python [here](https://docs.python.org/3/library/codecs.html#standard-encodings). This project uses the ``latin-1 encoding``.*

## Results 

You can find a csv of the results from the linguistic analysis in the ``out`` directory, which contains the relative frequency of nouns, verbs, adjectives, and adverbs per 10,000 words and the total number of unique PER, LOC, and ORG entities.

This type of analysis is useful for examining the use of language across different literary genres or periods or for determining how students' language progresses over time as they expand their vocabulary.

### Limitations and future improvements 

- Without some form of visualization, the results may be difficult to understand. Hence, a histogram might be a better solution to improve readability. 

- Also, the USE dataset contains a few inconsistencies (e.g., some students left the English program between semesters), which may affect future analyses. 


## References

Axelsson, M. W. (2003). Manual: The Uppsala Student English corpus (USE). Uppsala University Department of English. https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457










