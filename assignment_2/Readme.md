# Assignment 2: Text classification benchmarks

## Description of the assignment
This project uses scikit-learn to train a logistic regression and neural network classifier on the 'Fake News Dataset' in the ``in`` folder.

In the ``src`` folder, you will find three Python scripts: one that trains the logistic regression classifier, a second that trains training the neural network classifier, and a third which vectorizes the data separately for reusability. Each script produces a classification report, saved in the ``out`` folder, while the trained models and tfidf_vectorizers are saved in the ``models`` folder.  

## Installation

 1. Open a terminal and clone the repository using Git 
```sh
git clone https://github.com/trinerye/visual_analytics_2024.git
```

2. Change directory to the assignment folder 
```sh
cd assignment_2
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
source ./A2_env/bin/activate
# Run the code
python src/logistic_regression.py -i in/fake_or_real_news.csv &
python src/neural_network.py -i in/fake_or_real_news.csv 
# Deactivate the enviroment
deactivate
```

## Usage

Write something about the flags here

```sh

```
