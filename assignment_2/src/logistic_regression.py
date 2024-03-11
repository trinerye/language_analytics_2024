# %%
# system tools
import os
# data munging tools
import pandas as pd
# Machine learning stuff
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
# Pipeline stuff for saving the models
import joblib

import argparse
# %%
def file_loader():
    parser = argparse.ArgumentParser(description="Loading data")
    parser.add_argument("--input",
                        "-i",
                        required = True)
    
    args = parser.parse_args()
    return args

# This function loads the data from the data folder and returns it as a data frame
def load_data(data_path):
    print(f"running function: load_data on {data_path}")
    return pd.read_csv(data_path) 

# This function splits the dataset into training and testing sets with 20% of the data reserved for testing. A fixed random state is added for reproducibility.
def split_data(data):
    return train_test_split(data["text"], data["label"], test_size=0.2, random_state=42) # the first to parameters are X and y

# This function vectorizes the data, turning it into TF-IDF features and fitting it on both the training data and the test data.
def vectorize_data(X_train, X_test):
    vectorizer = TfidfVectorizer(ngram_range=(1,2), lowercase=True, max_df=0.95, min_df=0.05, max_features=1835)
    X_train_feats = vectorizer.fit_transform(X_train)
    X_test_feats = vectorizer.transform(X_test)
    return vectorizer, X_train_feats, X_test_feats

# This function trains the logistic regression model on the transformed training data and its corresponding labels.
def train_model(X_train_feats, y_train):
    return LogisticRegression(random_state=42).fit(X_train_feats, y_train)

# This function evaluates the performance of the trained classifier on the test dataset and produces a classification report contaning metrics like precision, recall, and F1-score.
def evaluate_model(classifier, X_test_feats, y_test):
    return metrics.classification_report(y_test, classifier.predict(X_test_feats)) # the second parameter is the prediction (y_pred)

# This function saves the classification report
def saving_report(classifier_metrics, classifier, vectorizer, out_path, model_path, vectorizer_path):
    # Opens the file in the out folder in write mode and writes the classification metrics to it.
    with open(out_path, "w") as file:
        file.write(classifier_metrics)
    # Saves the trained classifier and the vectorizer in the models folder
    joblib.dump(classifier, model_path)
    joblib.dump(vectorizer, vectorizer_path)

def main():
    # Creates a folder path for each folder
    out_folder_path = os.path.join("..", "out", "logistic_regression")
    models_folder_path = os.path.join("..","models", "logistic_regression")

    # Creates a folder for each path
    os.makedirs(models_folder_path )
    os.makedirs(out_folder_path)

    # Filepath for each used file or saved file
    data_path = os.path.join(file_loader().input)
    model_path = os.path.join("..", "models", "logistic_regression", "regression_classifier.joblib")
    vectorizer_path = os.path.join("..","models", "logistic_regression", "tfidf_vectorizer.joblib")
    out_path = os.path.join("..","out", "logistic_regression", "classification_report.txt")
  
    # Calling all functions, saving them as variables 
    data = load_data(data_path)
    X_train, X_test, y_train, y_test = split_data(data)
    vectorizer, X_train_feats, X_test_feats = vectorize_data(X_train, X_test)
    classifier = train_model(X_train_feats, y_train)
    classifier_metrics = evaluate_model(classifier, X_test_feats, y_test)
    saving_report(classifier_metrics, classifier, vectorizer, out_path, model_path, vectorizer_path)

if __name__ == "__main__":
    main()

# ../data/fake_or_real_news.csv