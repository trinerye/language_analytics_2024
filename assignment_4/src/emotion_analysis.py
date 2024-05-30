import os
import numpy as np
import pandas as pd
from transformers import pipeline
import matplotlib.pyplot as plt
from codecarbon import EmissionsTracker
from tqdm import tqdm
from plotting_tools import plot_results


def setup_classifier():

    print("Setting up the classifier pipeline")

    # Initializes the model for text classification
    classifier = pipeline("text-classification",
                          model="j-hartmann/emotion-english-distilroberta-base",
                          top_k=1)
    return classifier


def load_data(in_folderpath):
    
    print("Loading the data")

    # Loads the data as a dataframe
    df = pd.read_csv(os.path.join(in_folderpath, "Game_of_Thrones_Script.csv"))

    return df


def extract_emotion_labels(df, classifier, out_folderpath):

    print("Preprocessing the data")

    # Drops missing NA values from the 'Sentence' column, modifying the original dataframe
    df['Sentence'].dropna(inplace=True)

    # Converts the values in the 'Sentence' column to strings
    df['Sentence'] = df['Sentence'].astype(str)

    # Converts the 'Sentence' column into a list 
    sentences = df['Sentence'].tolist()

    print("Producing classifier predictions")

    # Returns a nested list of dictionaries containing the emotion labels and their score 
    predictions = classifier(sentences)

    # Flattens the nested list to a single list containing the dictionaires 
    dictionaries = [index[0] for index in predictions]

    # Adds the emotion label from the dictionary to a new column in the dataframe 
    df['Emotion Label'] = [dictionary['label'] for dictionary in tqdm(dictionaries)]

    # Saves the dataframe 
    df.to_csv(os.path.join(out_folderpath, "emotion_distribution.csv"), index=False)

    return df


def count_emotion_labels(df):

    # Groups the dataframe by season, counts the frequency of each emotion label and normalizes the values.
    df_filtered = df.groupby('Season')['Emotion Label'].value_counts(normalize=True)

    # Pivots the columns in the dataframe, turning the values in 'Emotion Label' into columns - and converts NA values into zeros
    df_filtered = df_filtered.unstack(fill_value=0)
    
    return df_filtered


def save_results(df_filtered, out_folderpath):

    print("Saving the results as a csv")

    # Saves the filtered dataframe
    df_filtered.to_csv(os.path.join(out_folderpath, "emotions_across_seasons.csv"))
  

def main():

    # Creates a folderpath for each directory and makes the directory if it does not exist
    in_folderpath = "in"
    out_folderpath = "out"
    seasons_folderpath = os.path.join(out_folderpath, "seasons")
    emotions_folderpath = os.path.join(out_folderpath, "emotions")
    emissions_folderpath = os.path.join("emissions")
    os.makedirs(out_folderpath, exist_ok=True)
    os.makedirs(seasons_folderpath, exist_ok=True)
    os.makedirs(emotions_folderpath, exist_ok=True)
    os.makedirs(emissions_folderpath, exist_ok=True)
  

    # Initializes the emissions tracker by codecarbon
    tracker = EmissionsTracker(project_name="emotion_analysis",
                               output_file="emissions.csv",
                               output_dir=emissions_folderpath) 

    # Tracks the initialization of the argument parser
    tracker.start_task("initialize_argparse")
    classifier = setup_classifier()
    tracker.stop_task()

    # Tracks the function that loads the dataset
    tracker.start_task("load_data")
    df = load_data(in_folderpath)
    tracker.stop_task()

    # Tracks the function produces the text classification prediction and extracs the emotion labels from it
    tracker.start_task("extract_emotion_labels")
    df = extract_emotion_labels(df, classifier, out_folderpath)
    tracker.stop_task()

    # Tracks the function that groups the dataframe by season an calculates the relative frequency for each emotion label
    tracker.start_task("count_emotion_labels")
    df_filtered = count_emotion_labels(df)
    tracker.stop_task()

    # Tracks the function that saves the filtered dataframe as a csv
    tracker.start_task("save_results")
    save_results(df_filtered, out_folderpath)
    tracker.stop_task()

    # df_filtered= pd.read_csv(os.path.join(out_folderpath, ""emotion_by_season.csv""))

    # Tracks the function that plots the results 
    tracker.start_task("plot_results")
    plot_results(df_filtered, seasons_folderpath, emotions_folderpath)
    tracker.stop_task()

    tracker.stop()

if __name__ == "__main__":
    main()





