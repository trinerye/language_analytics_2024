import os
import spacy
import pandas as pd
import re
from codecarbon import EmissionsTracker
from tqdm import tqdm

def load_model():

    # Loads the en_core_web_md model from spacy
    nlp = spacy.load("en_core_web_md")
    return nlp


def open_and_clean_text(filepath):

    # Opens and reads the text using a latin1 encoding which contains 191 characters from the latin script, including Finnish letters    
    with open(filepath, encoding='latin1') as f:
        text = f.read()

        # Uses the re.sub function to remove occurrences which matches the regular expression, specifically everything between the tags including empty tags.   
        cleaned_text = re.sub(r'\<[^>]*\>', "", text)
    return cleaned_text

def extract_text_entities(doc):

    # Iterates over each token in doc, appending the pos tags to a list
    annotations = [(token.pos_) for token in doc if not token.is_punct]

    # Converting the annotations list into a data frame
    df = pd.DataFrame(annotations, columns=["pos"])

    # Returns a dataframe with only the nouns, verbs, adj, and adv if they are present in the pos column, making the boolean vector true.
    df_filtered = df[df['pos'].isin(["NOUN", "VERB", "ADJ", "ADV"])] 

    # Groups the elements in pos and counts the size of each group
    df_pos_count = df_filtered.groupby("pos").size()

    # Calculates the length of the dataframe as it represents the total amount of words in the text
    total_words = len(df)

    # Calculates the frequency of nouns, verbs, adjectives, and adverbs per 10,000 words
    noun = round((df_pos_count["NOUN"]/total_words) * 10000, 2)
    verb = round((df_pos_count["VERB"]/total_words) * 10000, 2)
    adj = round((df_pos_count["ADJ"]/total_words) * 10000, 2)
    adv = round((df_pos_count["ADV"]/total_words) * 10000, 2)

    # Creates an empthy set for each unique entity
    person, loc, org = set(), set(), set()

    # Iterates over each entity in doc.ents, which is a tuple containing the document entities 
    for entity in doc.ents:

        # Checks whether the label is a PERSON, LOC, or ORG, converts it to a string, and adds it to the corresponding set.
        if entity.label_ == "PERSON":
            person.add(str(entity))

        elif entity.label_ == "LOC":
            loc.add(str(entity))
        
        elif entity.label_ == "ORG":
            org.add(str(entity))

    # Returns an int for each pos and unique entity 
    return noun, verb, adj, adv, len(person), len(loc), len(org)

def process_files(directory, nlp, in_folderpath, out_folderpath): 

    # Empty list of dictionaries 
    results = []
    
    # Creates a sorted list of all the filenames within each directory in the in directory 
    filenames = sorted(os.listdir(os.path.join(in_folderpath, directory)))

    # Iterates over each file in the list of filenames.
    for file in tqdm(filenames):

        # Constructs the filepath for each text file
        filepath = os.path.join(in_folderpath, directory, file)

        # Calls the function which opens and cleans the text files 
        cleaned_text = open_and_clean_text(filepath)
        
        # Processes the cleaned text using the nlp model 
        doc = nlp(cleaned_text)

        # Calls the function that extracts text entities from the document
        noun, verb, adj, adv, person, loc, org = extract_text_entities(doc)

        # Adds the extracted information to a dictionary and appends it to a list
        results.append({"Filename": file, "NOUN": noun,"VERB": verb, "ADJ": adj, "ADV": adv, "PERSON": person, "LOC": loc, "ORG": org})
        
        # Turns the list of dictionaries into a dataframe
        df_results = pd.DataFrame(results)

    # Saves the results as a csv file in the out directory 
    df_results.to_csv(f"{os.path.join(out_folderpath, directory)}.table.csv", index=False)

def process_directories(in_folderpath, nlp, out_folderpath):

    # Creates a sorted list of all the directories within the in directory
    dirs = sorted(os.listdir(in_folderpath))

    # Iterates over each directory in the list of directories and process each file within in
    for directory in dirs:
        process_files(directory, nlp, in_folderpath, out_folderpath)

def main():

    # Creates a folderpath for the CO2 emissions and makes the directory if it does not exsist
    emissions_folderpath = os.path.join("emissions")
    os.makedirs(emissions_folderpath, exist_ok=True)

    # Initializes the emissions tracker by codecarbon
    with EmissionsTracker(project_name="linguistic_analysis",
                          output_dir=emissions_folderpath) as tracker:

        # Creates a filepath for each directory and makes the out directory if does not exist
        in_folderpath = os.path.join("in")
        out_folderpath = os.path.join("out")
        os.makedirs(os.path.join(out_folderpath), exist_ok=True)

        # Tracks loading the model
        tracker.start_task("load_spacy_model")
        nlp = load_model()
        tracker.stop_task()

        # Tracks the spacy analysis 
        tracker.start_task("perform_spacy_analysis")
        process_directories(in_folderpath, nlp, out_folderpath)
        tracker.stop_task()

if __name__ == "__main__":
    main()
  