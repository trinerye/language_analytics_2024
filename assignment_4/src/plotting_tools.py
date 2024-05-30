import os
import pandas as pd
import matplotlib.pyplot as plt


def plot_results(df_filtered, seasons_folderpath, emotions_folderpath):

    # Iterates over the filtered dataframe, using the season column as an index (starting from season 1)
    for i, season in enumerate(df_filtered.index, start=1):
        
        # Creates a plot for each season
        plt.figure(figsize=(12,8))
        df_filtered.loc[season].plot(kind='bar')
        plt.title(f'Relative Emotion Score Frequency for {season}', weight='bold')
        plt.ylabel('Relative Frequency', weight='bold')
        plt.xlabel('Emotion Label', weight='bold')
        plt.xticks(rotation = 0)
        plt.savefig(os.path.join(seasons_folderpath, f"season_{i}_emotion_distribution.jpg"))
        plt.close() 

    # Creates a plot for each emotion
    for emotion in df_filtered:
        plt.figure(figsize=(12,8))
        df_filtered[emotion].plot()
        plt.title(f'Relative Frequency of {emotion.capitalize()} Across All Seasons', weight='bold')
        plt.ylabel('Relative Frequency', weight='bold')
        plt.xlabel('Season', weight='bold')
        plt.xticks(rotation=0)
        plt.savefig(os.path.join(emotions_folderpath, f"{emotion}_distribution_across_seasons.jpg"))
        plt.close()  

