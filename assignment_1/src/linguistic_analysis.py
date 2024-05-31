import os
import spacy
import pandas as pd
import argparse
import re
from codecarbon import EmissionsTracker
from tqdm import tqdm


def parser():

    # Creates an argparse object 
    parser = argparse.ArgumentParser()

    # Defines the CLI argument that specifies the spaCy pipeline 
    parser.add_argument("--pipeline",
                        "-p",
                        type=str,
                        required=True,
                        help="Specify the name of spaCy pipeline you want to work with. Go to https://spacy.io/models to read more about spaCy pipelines")
    
    # Defines the CLI argument that specifies the encoding used to open the text 
    parser.add_argument("--encoding",
                        "-e",
                        type=str,
                        required=True,
                        help="Specify which encoding to use to open the texts from the dataset. Go to https://docs.python.org/3/library/codecs.html#standard-encodings to see the standard encodings for python")

    return parser.parse_args()  # Parses and returns the CLI arguments


def load_model(args):

    # Loads the en_core_web_md model from spacy
    nlp = spacy.load(args.pipeline) 
    return nlp


def open_and_clean_text(filepath, args):

    # Opens and reads the text using a latin1 encoding which contains 191 characters from the latin script, including Swedish letters    
    with open(filepath, encoding=args.encoding) as f:
        text = f.read()

        # Uses the re.sub function to remove occurrences which matches the regular expression, specifically everything between the tags including empty tags.   
        cleaned_text = re.sub(r'\<[^>]*\>', "", text)
    return cleaned_text


def extract_text_entities(doc):

    # Iterates over each token in doc, appending the pos tags to a list
    annotations = [(token.pos_) for token in doc if not token.is_punct and not token.is_space]

    # Converts the annotations list into a data frame
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


def process_files(directory, nlp, args, in_folderpath, out_folderpath): 

    # Empty list of dictionaries 
    results = []
    
    # Creates a sorted list of all the filenames within each directory in the in directory 
    filenames = sorted(os.listdir(os.path.join(in_folderpath, directory)))

    # Iterates over each file in the list of filenames.
    for file in tqdm(filenames):

        # Constructs the filepath for each text file
        filepath = os.path.join(in_folderpath, directory, file)

        # Calls the function which opens and cleans the text files 
        cleaned_text = open_and_clean_text(filepath, args)
        
        # Processes the cleaned text using the nlp model 
        doc = nlp(cleaned_text)

        # Calls the function that extracts text entities from the document
        noun, verb, adj, adv, person, loc, org = extract_text_entities(doc)

        # Adds the extracted information to a dictionary and appends it to a list
        results.append({"Filename": file, "NOUN": noun,"VERB": verb, "ADJ": adj, "ADV": adv, "PERSON": person, "LOC": loc, "ORG": org})
        
        # Turns the list of dictionaries into a dataframe
        df_results = pd.DataFrame(results)

    # Saves the results as a csv file in the out directory 
    df_results.to_csv(os.path.join(out_folderpath, f"{directory}_linguistic_analysis.csv"), index=False)


def process_directories(in_folderpath, nlp, args, out_folderpath):

    # Creates a sorted list of all the directories within the in directory
    dirs = sorted(os.listdir(in_folderpath))

    # Iterates over each directory in the list of directories and process each file within in
    for directory in dirs:
        
        process_files(directory, nlp, args, in_folderpath, out_folderpath)

    return directory
    

def main():

    # Creates a folderpath for each directory and makes the directory if it does not exist
    in_folderpath = os.path.join("in", "USEcorpus")
    out_folderpath = os.path.join("out")
    emissions_folderpath = os.path.join("..", "assignment_5", "emissions")
    os.makedirs(os.path.join(out_folderpath), exist_ok=True)
    os.makedirs(emissions_folderpath, exist_ok=True)

    # Initializes the emissions tracker by codecarbon
    tracker = EmissionsTracker(project_name="linguistic_analysis",
                               output_file="emissions.csv",
                               output_dir=emissions_folderpath) 

    # Tracks the initialization of the argument parser
    tracker.start_task("initialize_argparse")
    args = parser()
    tracker.stop_task()

    # Tracks the function that loads the model
    tracker.start_task("load_spacy_model")
    nlp = load_model(args)
    tracker.stop_task()

    # Tracks the function which does the spacy analysis 
    tracker.start_task("perform_spacy_analysis")
    directory = process_directories(in_folderpath, nlp, args, out_folderpath)
    tracker.stop_task()
    
    tracker.stop()

if __name__ == "__main__":
    main()
  