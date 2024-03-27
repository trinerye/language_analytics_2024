import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import joblib
import argparse

# This function takes an input from the commandline and returns it as ...
def file_loader():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",
                        "-i",
                        required = True)
    return parser.parse_args()

# This function loads the data and splits it into a training and testing dataset with 20% of the data reserved for testing. 
def load_data(data_path):
    print("Loading the data")
    data = pd.read_csv(data_path) 
    # The first to parameters are X and y and a fixed random state is added for reproducibility.
    return train_test_split(data["text"], data["label"], test_size=0.2, random_state=42) 

# This function vectorizes the data, turning it into TF-IDF features and fitting it on both the training data and the test data.
def vectorize_data(X_train, X_test):
    print("Vectorizing the data")
    vectorizer = TfidfVectorizer(ngram_range=(1,2), lowercase=True, max_df=0.95, min_df=0.05, max_features=1835)
    X_train_feats = vectorizer.fit_transform(X_train)
    X_test_feats = vectorizer.transform(X_test)
    return vectorizer, X_train_feats, X_test_feats
  
# This function trains the logistic regression classifier on the transformed training data and its corresponding labels.
def train_model(X_train_feats, y_train):
    print("Training the logistic regression classifier")
    return LogisticRegression(random_state=42).fit(X_train_feats, y_train)

# This function evaluates the performance of the trained classifier on the test dataset and produces a classification report contaning metrics like precision, recall, and F1-score.
def evaluate_model(classifier, X_test_feats, y_test):
    print("Creating the classification report")
    return metrics.classification_report(y_test, classifier.predict(X_test_feats)) # the second parameter is the prediction (y_pred)

# This function saves the classification report
def saving_report(classifier_metrics, out_path):
    print("Saving the classification report")
    # Opens the file in the out folder in write mode and writes the classification metrics to it.
    with open(out_path, "w") as file:
        file.write(classifier_metrics)
    
def main():
    # Creates a folder path for each folder
    out_folder_path = os.path.join("out", "logistic_regression")
    models_folder_path = os.path.join("models", "logistic_regression")

    # If the directory does not exist, make the directory
    os.makedirs(out_folder_path, exist_ok=True)
    os.makedirs(models_folder_path, exist_ok=True)

    # Filepath for each used file or saved file
    data_path = os.path.join(file_loader().input)
    model_path = os.path.join("models", "logistic_regression", "regression_classifier.joblib")
    vectorizer_path = os.path.join("models", "logistic_regression", "tfidf_vectorizer.joblib")
    out_path = os.path.join("out", "logistic_regression", "classification_report.txt")
  
    # Calling all functions, saving them as variables 
    X_train, X_test, y_train, y_test = load_data(data_path)
    vectorizer, X_train_feats, X_test_feats = vectorize_data(X_train, X_test)
    classifier = train_model(X_train_feats, y_train)
    classifier_metrics = evaluate_model(classifier, X_test_feats, y_test)
    saving_report(classifier_metrics, out_path)
    
    # Saving the logistic regression classifier and the vectorizer
    print("Saving the classifier and the vectorizer")
    joblib.dump(vectorizer, vectorizer_path) 
    joblib.dump(classifier, model_path)

if __name__ == "__main__":
    main()
