import os
import pandas as pd
from transformers import pipeline

def setup_classifier():
    classifier = pipeline("text-classification",
                          model="j-hartmann/emotion-english-distilroberta-base",
                          top_k=1)
    return classifier


def extract_emotion_label(in_folderpath, classifier, out_folderpath):

    test_df = pd.read_csv(os.path.join(in_folderpath, "Game_of_Thrones_Script.csv"))

    # test_df = df.sample(n=100, random_state=42)
    
    classifier = setup_classifier()

     # Removes missing values (NaN) from the 'Sentence' column, modifying the original dataframe
     # (to make a new copy of the dataframe set inplace=False)
    test_df['Sentence'].dropna(inplace=True)

    # COnvert all objects in the 'Sentence' column to a string type object
    test_df['Sentence'] = test_df['Sentence'].astype('string') 

    # Converts the dataframe column 'Sentence' into a list 
    sentences = test_df['Sentence'].tolist()

    # Applies the classifier function to the list of sentences and  
    # returns a nested list of dictionaries where each dictionary contains a 'label' and a 'score'
    predictions = classifier(sentences)

    test_df['Emotion Label'] = [dictionary[0]['label'] for dictionary in predictions]

    test_df.to_csv(os.path.join(out_folderpath, "df_with_emotion_score.csv"))


