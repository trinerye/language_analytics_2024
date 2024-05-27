# Assignment 1: Linguistic Analysis with spaCy

## About

This project uses ``spaCy`` to extract linguistic features from ``The Uppsala Student English Corpus (USE)`` to *calculate the relative frequency of nouns, verbs, adjectives, and adverbs per 10,000 words and the total number of unique PER, LOC, and ORG entities for each text*. The extracted information is saved as a CSV file in the ``out`` folder, with an additional plot of the results if the command-line flag ``--print`` is added when running the script. 

The ``src`` directory contains two scripts:

- **linguistic_analysis:** 

- **plotting_tools:** 


### Data

**Describe the finnish dataset here**

***Write something about the encoding***

Download the [17 Category Flower Dataset](https://www.robots.ox.ac.uk/~vgg/data/flowers/17) dataset from the Visual Geometry Group at the University of Oxford, rename the ``jpg`` folder to ``flowers`` and save it in the ``in`` directory. 

### Model

***Describe the spacy model here***

According to the documentation, the [cv2.compareHist()](https://docs.opencv.org/3.4/d8/dc8/tutorial_histogram_comparison.html) uses chi-square statistics to measure the distances between the target image and the dataset. On the other hand, the [NearestNeighbors()](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.kneighbors) model compares the target image with the dataset by calculating the Euclidean distance between the one-dimensional vectors to find the nearest neighbors.

Before calculating the Euclidian distance, the image features are extracted using VGG16, a Convolutional Neural Network with the following parameters. 

| Parameter      | Value        | Type | 
|----------------|--------------|------|
| weights        | imagenet     | str  |
| include_top    | False        | bool |
| pooling        | avg          | str  |        
| input_shape    | (224, 224, 3)| int  |

##  File Structure

```
└── assignment_1
        |
        ├── in
        │   └── flowers (contains 1360 images)
        │      
        ├── out
        |   ├── cv2_image_comparison.csv
        |   ├── cv2_image_comparison_plot.png
        |   ├── knn_image_comparison.csv
        |   └── knn_image_comparison_plot.png
        |
        ├── src
        │   ├── image_search_with_cv2.py
        │   └── image_search_with_knn.py
        │     
        ├── readme.md
        ├── requirements.txt
        ├── run.sh
        └── setup.sh
```
## Usage

If you want to replicate this project, follow the steps outlined below. The instructions will guide you through setting up the environment, running the script, and plotting the results while helping you understand the available command-line options for customization.  

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

# Deactivate the enviroment
deactivate
```

### Command Line Interface  

*This project supports the following command-line options to customize the script. *See table for reference.*

|Flag   |Shorthand|Description                                                   |Type |Required|
|-------|---------|--------------------------------------------------------------|-----|--------|
|--print|-p       |Saves an unedited version of the csv file in the out directory|bool |FALSE   |

## Results 

You can find a CSV file and a plot of lingustic analysis in the ``out`` directory.

![plot](out/plot_of_analysis.png)




### CO2 Emissions

|Something |Something|
|----------|---------|
|          |         |







