import os
import pandas as pd
from transformers import pipeline
import matplotlib.pyplot as plt
import numpy as np
from extract_emotion_scores import setup_classifier, extract_emotion_label

def sort_and_count_labels(saved_df, out_folderpath):

    sorted_df = saved_df.groupby('Season')['Emotion Label'].value_counts(normalize=True).unstack(fill_value = 0)

    sorted_df.to_csv(os.path.join(out_folderpath, "emotion_by_season.csv"))
    
    return sorted_df

def plot_emotion_labels(sorted_df, out_folderpath):

    #### Fix color palette
    colors = ['#1b9e77', '#a9f971', '#fdaa48','#6890F0','#A890F0', '#DC24CF', '#75B848']

    # Iterates over the index of 'season_df', which uses the differents seasons as identifiers after grouping the 'Season' columns together.
    # Enumerate keeps count of iterations (i) starting from 1 (season 1 etc.)
    for i, season in enumerate(sorted_df.index, start=1):
        plt.figure(figsize=(12,8))
        sorted_df.loc[season].plot(color=colors)
        plt.title(f'Average Emotion Scores for {season}', weight='bold')
        plt.ylabel('Line frequency', weight='bold')
        plt.xlabel('Label', weight='bold')
        plt.xticks(rotation = 0)
        plt.savefig(os.path.join(out_folderpath, f"season_{i}_emotion_distribution.jpg"))
        plt.close()  
        
    for emotion in sorted_df:
        plt.figure(figsize=(12,8))
        sorted_df[emotion].plot(color=colors)
        plt.title(f'Line Frequency of {emotion.capitalize()} Across All Seasons', weight='bold')
        plt.ylabel('Line frequency', weight='bold')
        plt.xlabel('Season', weight='bold')
        plt.xticks(rotation=0)
        plt.savefig(os.path.join(out_folderpath, f"{emotion}_distribution_across_seasons.jpg"))
        plt.close()  

def main():

    # Creates a filepath for each directory - if the out directory does not exist, make the directory
    in_folderpath = os.path.join("in")
    out_folderpath = os.path.join("out")
    os.makedirs(out_folderpath, exist_ok=True)

    saved_df = pd.read_csv(os.path.join(out_folderpath, "df_with_emotion_score.csv"))

    sorted_df = sort_and_count_labels(saved_df, out_folderpath)

    plot_emotion_labels(sorted_df, out_folderpath)

if __name__ == "__main__":
    main()