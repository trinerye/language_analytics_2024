# Assignment 1: Linguistic Analysis with spaCy

## About

This project uses ``spaCy`` to extract linguistic features from ``The Uppsala Student English Corpus (USE)`` to *calculate the relative frequency of nouns, verbs, adjectives, and adverbs per 10,000 words and the total number of unique PER, LOC, and ORG entities for each text*. 

The ``src`` directory contains one script: 

- **linguistic_analysis:** Uses the ``en_core_web_md`` pipeline from spaCy to extract linguistic features from the dataset and saves the results as a csv file in the ``out`` directory 


### Data

Download the [The Uppsala Student English Corpus (USE)]( https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457) from the Oxford Text Archive. You should download the USEcorpus.zip file, unzip it and place the ``USEcorpus`` folder in the in directory. 

This project opens the files using the ``latin-1 encoding`` as the dataset contains Finnish letters.

### Model

This project uses the English [en_core_web_md](https://spacy.io/models/en) pipeline from spaCy, optimized for CPUs, to tokenize the USE dataset and perform part-of-speech (POS) tagging and named entity recognition (NER) on it. 

Go to https://spacy.io/models to find the spaCy pipeline you want to work with and add it as a command-line argument when running the script. However, remember to change the encoding accordingly to ensure the text is readable. See standard encodings for python [here](https://docs.python.org/3/library/codecs.html#standard-encodings)


##  File Structure

```
└── assignment_1
        |
        ├── emissions
        |   ├── emissions_base_id
        |   └── emissions.csv
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
*You may notice that the script also produces a csv file that contains the CO2 emissions for each sub-task. Please ignore this folder, as it is part of another assignment and, therefore, unnecessary to reproduce this project.*

## Usage

If you want to reproduce this project, please follow the steps below. The instructions will help you set up the environment, run the script and understand the available command-line options. 

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
python src/linguistic_analysis.py

# Deactivate the environment
deactivate
```

### Command Line Interface  

This project supports the following command-line options to customize the script. *See table for reference.*

|Flag      |Shorthand|Description                                                                |Type |Required|
|----------|---------|---------------------------------------------------------------------------|-----|--------|
|--pipeline|-p       |Specifies the spaCy pipeline used for the linguistic analysis              |str  |TRUE    |
|--encoding|-e       |Specifies which encoding to use to open the texts from the dataset|str  |TRUE    |

## Results 

This project produces a csv file containing the results from the linguistic analysis, specifically the relative frequency of nouns, verbs, adjectives, and adverbs per 10,000 words and the total number of unique PER, LOC, and ORG entities for each text in the USE dataset, which you can find in the ``out`` directory. 

### Limitations and future improvements 

?







