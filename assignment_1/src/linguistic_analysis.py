import os
import spacy
import pandas as pd
import re

# Function that open and cleans the text files
def open_and_clean_text(filepath):

    # Opens the files using a latin1 encoding which contains 191 characters from the latin script, including Finnish letters    
    with open(filepath, encoding='latin1') as f:
        text = f.read()

        # The re.sub function finds matching occurrences of a specified pattern and replaces it with an empty string
        # r'\<[^>]*\>' is a regular expression which removes everything between the tags including empty tags     
        cleaned_text = re.sub(r'\<[^>]*\>', "", text)

    return cleaned_text

# Function that extracts the noun, verbs, adjectives, adverbs and the three unique entities person, loc, and org
def extract_text_entities(doc):

    # Iterates over each token in doc, appending the text and pos tags to the annotations list
    annotations = []
    for token in doc: 
        annotations.append([token.text, token.pos_])

    # Converting the annotations list into a data frame
    df = pd.DataFrame(annotations, columns=["text", "pos"])

    # Filtrates the df using a boolean vector (the boolean vector is created from a conditional statement, 
    # checking if each element in pos is part of the list ["NOUN", "VERB", "ADJ", "ADV"])
    df_keep = df[df['pos'].isin(["NOUN", "VERB", "ADJ", "ADV"])] 

    # Groups the elements in pos and counts the size of each group
    pos_count = df_keep.groupby("pos").count()

     # The same as before but this time, the "-" inverts the boolean vector removing the elements 
    # from pos which is found in the list ["SPACE", "SYM", "PUNCT", "NUM"]
    df_removed = df[-df['pos'].isin(["SPACE", "SYM", "PUNCT", "NUM"])] 

    # Calculates the normalization factor of df_removed divided by 10000
    total_words = len(df_removed)/10000 

    # Calculates the frequency of nouns, verbs, adjectives, and adverbs and rounds the number to a whole number 
    # Each pos frequency is normalized against the total word count for comparison
    noun = round(pos_count["text"]["NOUN"]/total_words)
    verb = round(pos_count["text"]["VERB"]/total_words)
    adj = round(pos_count["text"]["ADJ"]/total_words)
    adv = round(pos_count["text"]["ADV"]/total_words)

    # Creates an empthy set for each unique entities (set can only hold unique values)
    person, loc, org = set(), set(), set()

    # Iterates over each entity in doc, using a conditional statement to filter the entities, 
    # then adding each entity to the sets (person, loc, org) based on their labels
    for entity in doc.ents:

        if entity.label_ == "PERSON":
            person.add(str(entity))

        elif entity.label_ == "LOC":
            loc.add(str(entity))
        
        elif entity.label_ == "ORG":
            org.add(str(entity))

    # Returns an int for each pos and unique entity 
    return noun, verb, adj, adv, len(person), len(loc), len(org)

# Function that process each file in the different directories 
def process_files(directory, nlp): 

    # Creating an empty dataframe for the final results
    final_results = pd.DataFrame(columns=["Filename","NOUN", "VERB", "ADJ", "ADV", "PERSON", "LOC", "ORG"])
    
    # Creates a sorted list of all the filenames within each directory in the in-folder 
    filenames = sorted(os.listdir(os.path.join("in", directory)))
    
    # Iterates over each file in the sorted filenames list.
    for file in filenames:

        # Constructs the file path for each text file
        filepath = os.path.join("in", directory, file)

        # Calls the open_and_clean_text(filenames) function 
        cleaned_text = open_and_clean_text(filepath)
        
        # Processes the cleaned text using the nlp model (en_core_web_md)
        doc = nlp(cleaned_text)

        # Calls the extract_text_entities(doc) fucntion
        noun, verb, adj, adv, person, loc, org = extract_text_entities(doc)

        # Creates a list containing the results 
        results = [file, noun, verb, adj, adv, person, loc, org]

        # Turns the results list into a dataframe using the columns from the final_results dataframe
        df_results = pd.DataFrame([results], columns=final_results.columns)
        
        # Appends the results dataframe to the final_results dataframe
        final_results = pd.concat([final_results, df_results])
    
    # Saves the final results dataframe as a csv file in the out folder
    final_results.to_csv(f"{os.path.join('out', directory)}.table.csv", index=False)

def main():

    # If the directory does not exist, make the directory
    os.makedirs(os.path.join("out"), exist_ok=True)

    # Creates a sorted list of all the directories within the given folder path
    dirs = sorted(os.listdir("in"))

    # Loads the en_core_web_md model from spacy
    nlp = spacy.load("en_core_web_md")

    # Iterates over each directory in the sorted list 'dirs' and process each file
    for directory in dirs:
        process_files(directory, nlp)
        
if __name__ == "__main__":
    main()
  