# Assignment 2: Text classification benchmarks

## About
This project uses ``scikit-learn`` to perform binary classification on the ``Fake or Real News`` dataset, determining whether the information is real or fake. It also vectorizes the data using the ``TfidfVectorizer``, transforming the text into a matrix of TF-IDF (Term Frequency-Inverse Document Frequency) features. These features are then used to train the ``LogisticRegression()`` classifier and ``MLPClassifier()``. *(See assignment description [here](https://github.com/CDS-AU-DK/cds-language/tree/main/assignments/assignment2))*

- **logistic_regression.py:** Trains the logistic regression classifier and saves a classification report in the ``out`` directory

- **neural_network.py:** Trains the neural network classifier and saves a classification report in the ``out`` directory

- **vectorizer.py:** Loads the data from the fake_or_real.csv, vectorizes it and saves the vectorized data in the /models/vectorizer directory to increase efficiency.


### Data

Download the fake_or_real_news.csv from [Kaggle](https://www.kaggle.com/datasets/jillanisofttech/fake-or-real-news), unzip the folder and place it in the ``in`` directory. 

### Model

This project uses the [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html), [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html), and [MLPClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html) from scikit-learn with the following parameters, although the classifiers primarily use their default settings.

>**TD-IDF Vectorizer**

| Parameter      | Value      | Type | 
|----------------|------------|------|
| ngram_range    | (1,2)      | int  |
| lowercase      | True       | bool |
| max_df         | 0.95       | int  |        
| min_df         | 0.05       | int  |
| max_features   | 1835       | int  |

<br>

>**Logistic Regression Classifier**

| Parameter      | Value      | Type | 
|----------------|------------|------|     
| random_state   | 42         | int  |

<br>

>**Neural Network Classifier**

| Parameter          | Value       | Type |
|--------------------|-------------|------|
| hidden_layer_sizes | (128, )     | int  |    
| random_state       | 42          | int  |
| early_stopping     | True        | bool |
| verbose            | 1           | int  |

 The ``early_stopping`` parameter stops the training process if the validation score does not improve more than tol = 0.000100 for ten consecutive epochs, which prevents overfitting and reduces run time.


##  File Structure

```
└── assignment_2
        |
        |
        ├── in
        │   └── fake_or_real_news.csv
        |
        ├── out
        |   ├── logistic_classification_report.txt
        |   └── neural_network_classification_report.txt
        |
        ├── src
        |   ├── logistic_regression.py
        │   ├── neural_network.py
        |   └── vectorizer.py
        │     
        ├── readme.md
        ├── requirements.txt
        ├── run.sh
        └── setup.sh
```

## Usage

If you want to reproduce this project, please follow the steps below. The instructions will help you set up the environment and run the scripts.

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
cd assignment_2
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
source ./LA_A2_env/bin/activate

# Run the code
python src/vectorizer.py
python src/logistic_regression.py 
python src/neural_network.py 

# Deactivate the environment
deactivate
```

## Results 

You can find the classification reports from both classifiers in the ``out`` directory.

>**Logistic Regression Classifier**

|Metrics         |Precision   |Recall|F1-Score|
|----------------|------------|------|--------|
|weighted average|0.91        |0.91  |0.91    |

<br>

>**Neural Network Classifier**

|Metrics         |Precision   |Recall|F1-Score|
|----------------|------------|------|--------|
|weighted average|0.92        |0.92  |0.92    |

The classification reports reveal that both classifiers perform well on the test data, with an F1-Score of 0.91 for the logistic regression classifier and 0.92 for the neural network classifier. Both classifiers are thus well suited for this binary classification task. However, since the neural network classifier takes much longer to run without significantly improving the result, the logistic regression classifier is preferred, as it saves time and reduces CO2 emissions. 


### Limitations and future improvements 

- While the test split seems relatively balanced, with 628 fake and 639 real news, we can not guarantee that the high performance is not the result of the train-test split. However, we can prevent this by doing cross-validation (e.g. testing different train-test splits) to find the average performance metrics. 

- Also, the script does not plot the loss curve, which makes it hard to check if the classifiers are overfitting or underfitting on the training data. 


## Code Carbon

Please ignore the code related to ``Code Carbon``, as it is part of another assignment and, therefore, unnecessary to reproduce this project. 

*For more information about this project's environmental impact, see [assignment_5](../assignment_5/readme.md).*