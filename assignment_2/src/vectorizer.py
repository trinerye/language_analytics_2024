#%%
import os
import sys
sys.path.append("..")
import pandas as pd
import joblib
from codecarbon import EmissionsTracker
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, ShuffleSplit
import matplotlib.pyplot as plt

def load_data():

    print("Loading the data")

    # Creates the in folderpath 
    in_folderpath = os.path.join("in")

    # Loads the dataset
    data = pd.read_csv(os.path.join(in_folderpath, "fake_or_real_news.csv")) 

    X_train, X_test, y_train, y_test = train_test_split(data["text"], data["label"], test_size=0.2, random_state=42) 
    # Splits the dataset into a train/test split with a fixed random state for reproducibility.
    return data, X_train, X_test, y_train, y_test


def vectorize_data(X_train, X_test, y_train, y_test):

    print("Vectorizing the data")

    # Creates a folderpath for the vectorizer and makes the directory if it does not exists  
    vectorizer_path = os.path.join("models", "vectorizer")
    os.makedirs(vectorizer_path, exist_ok=True)
    
    # Initializes the vectorizer 
    vectorizer = TfidfVectorizer(ngram_range=(1,2), lowercase=True, max_df=0.95, min_df=0.05, max_features=1835)

    # Fits the vectorizer to the training data and transforms it into vectors containing the features
    X_train_feats = vectorizer.fit_transform(X_train)
    
   # Uses the vectorizer to transform the test data into feature vectors
    X_test_feats = vectorizer.transform(X_test)

    # Saves the vectorizer, in the vectorizer folder in the models directory 
    joblib.dump(vectorizer, os.path.join(vectorizer_path, "tfidf_vectorizer.joblib")) 

    # Saves the vectorized texts and labels in the vectorizer folder in the models directory 
    joblib.dump((X_train_feats, X_test_feats), os.path.join(vectorizer_path, "vectorized_texts.joblib"))
    joblib.dump((y_train, y_test), os.path.join(vectorizer_path, "labels.joblib"))

    return vectorizer_path


def main():

   # Creates a folderpath for each directory and makes the directory if it does not exist
    out_folderpath = os.path.join("out")
    emissions_folderpath = os.path.join("..", "assignment_5", "emissions")
    os.makedirs(out_folderpath, exist_ok=True)  
    os.makedirs(emissions_folderpath, exist_ok=True)

    # Initializes the emissions tracker by codecarbon
    tracker = EmissionsTracker(project_name="text_classification",
                               output_file="emissions.csv",
                               output_dir=emissions_folderpath)

    # Tracks the function that loads the dataset
    tracker.start_task("load_fake_or_real_news_data")
    data, X_train, X_test, y_train, y_test = load_data()
    tracker.stop_task()

    # Tracks the function that vectorizes the data and saves it
    tracker.start_task("vectorize_data")
    vectorizer_path = vectorize_data(X_train, X_test, y_train, y_test)
    tracker.stop_task()

    tracker.stop()

if __name__ == "__main__":
    main()
  
# %%
