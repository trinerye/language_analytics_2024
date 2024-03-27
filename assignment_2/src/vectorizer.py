import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import argparse

def file_loader():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",
                        "-i",
                        required = True)
    return parser.parse_args()

def load_data(data_path):
    print("Loading the data")
    data = pd.read_csv(data_path) 
    # The first to parameters are X and y and a fixed random state is added for reproducibility.
    return train_test_split(data["text"], data["label"], test_size=0.2, random_state=42) 

def vectorize_data(X_train, X_test):
    print("Vectorizing the data")
    vectorizer = TfidfVectorizer(ngram_range=(1,2), lowercase=True, max_df=0.95, min_df=0.05, max_features=1835)
    X_train_feats = vectorizer.fit_transform(X_train)
    X_test_feats = vectorizer.transform(X_test)
    return vectorizer, X_train_feats, X_test_feats