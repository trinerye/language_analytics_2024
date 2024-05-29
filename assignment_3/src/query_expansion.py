import os
import gensim
import pandas as pd
import argparse
import spacy
import gensim.downloader as api
from codecarbon import EmissionsTracker
import matplotlib.pyplot as plt
from colorama import Fore


def parser():

  # Creates an argparse object 
    parser = argparse.ArgumentParser()

    # Defines the CLI argument that specifies the word used for the query exspansion 
    parser.add_argument("--word",
                        "-w",
                        type=str,
                        required=True,
                        help="Specify the word you want to use for the query exspansion")
    
    # Defines the CLI argument that specifies the encoding used to open the text 
    parser.add_argument("--artist",
                        "-a",
                        type=str,
                        required=True,
                        help="Specify the artist you want to search for")

    return parser.parse_args()  # Parses and returns the CLI arguments


def load_models():

    print("Loading models") 

    # Loads the the genism word embedding model
    model = api.load("glove-wiki-gigaword-50")

    # Loads the spaCy pipeline
    nlp = spacy.load("en_core_web_md")

    return model, nlp


def load_data(in_folderpath):
    
    print("Loading the data")

    # Loads the spotify dataset
    df =  pd.read_csv(os.path.join(in_folderpath, "Spotify Million Song Dataset_exported.csv")) 

    return df


def filter_by_artist(df, args):

    print(f"Finding songs by {args.artist}")
    
    # Filters the dataframe by artist if the name of the artist matches the argparse argument 
    df_filtered = df[df['artist'].str.lower().isin([args.artist.lower()])]

    return df_filtered


def query_expansion(model, args):
   
    print(f"Finding words similar to '{args.word.lower()}'")

    # Returns a list of tuples containing the ten most similar words and their similarity scores
    similar_words = model.most_similar(args.word.lower()) 

    # Iterates over the list of tuples, taking only the word and appending it to a new list
    words = [index[0] for index in similar_words]

    return words


def find_songs(words, args, df_filtered, nlp):
    
    print(f"Finding songs by {args.artist} that contains words similar to '{args.word.lower()}'")

    songs = []

    # Iterates over each row in the dataframe using the index to do so.
    for i, row in df_filtered.iterrows():

        # Tokinizes the text in the 'text' column
        doc = nlp(row['text'])
        
        # Converts every token in the document to lowercase, replaces the apostrophes with an empty string and removes punctuation and new lines.
        tokens = [token.text.lower().replace("'", "") for token in doc if not token.is_punct and "\n" not in token.text]

        # Checks if any word from the words list is in the tokens list
        if any(word in words for word in tokens):

            # Appends the song to the corresponding list if a word from the extended query is found within the tokenized text
            songs.append(row['song'])
    
    return songs


def save_csv(songs, df_filtered, args, out_folderpath):

    # Calculate the percentage of songs from a given artist that contains one of the words from the query expansion 
    percentage = round(len(songs) / len(df_filtered) * 100, 2)

    # The color code makes the end result green
    print(f"\033[1;32mResult: {percentage}% of {args.artist}'s songs contains words similar to '{args.word.lower()}'\033[0m") 

    # Creates a new dataframe that only contains the songs where words from the query expansion appear
    df_results = pd.DataFrame(songs, columns=["Song (A-Z)"])

    # Saves the results as a csv file in the out directory 
    df_results.to_csv(os.path.join(out_folderpath, f"{args.artist.lower()}_songs_about_{args.word.lower()}.csv"))

    return percentage


def save_plot(args, percentage, df_filtered, out_folderpath):

    # Creates a label for each 'slice'
    labels = f"Songs that contain words \nsimilar to '{args.word.lower()}'", 'Other songs'
    
    # Determines the size for each 'slice'
    sizes = [percentage, (100-percentage)]

    # Creates a piechart displaying the percentage of songs by the artist that contains a word from the query expansion 
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_title(f"Percentage of {args.artist} songs that contain words similar to {args.word.lower()}", weight='bold')
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#ffde57', '#306998'])
    plt.savefig(os.path.join(out_folderpath, f"percentage_of_{args.artist.lower()}_songs_about_{args.word.lower()}.png")) 
    plt.close()

def main():
    
    # Creates a folderpath for each directory and makes the directory if it does not exist
    in_folderpath = os.path.join("in")
    out_folderpath = os.path.join("out")
    emissions_folderpath = os.path.join("emissions")
    os.makedirs(out_folderpath, exist_ok=True)
    os.makedirs(emissions_folderpath, exist_ok=True)

    # Initializes the emissions tracker by codecarbon
    tracker = EmissionsTracker(project_name="logistic_regression_classification",
                               output_file="emissions.csv",
                               output_dir=emissions_folderpath) 

    tracker.start_task("initialize_argparse")
    args = parser()
    tracker.stop_task()

    tracker.start_task("load_spacy_and_gensim_models")
    model, nlp = load_models()
    tracker.stop_task()

    tracker.start_task("load_dataset")
    df = load_data(in_folderpath)
    tracker.stop_task()

    tracker.start_task("load_spacy_and_gensim_models")
    df_filtered = filter_by_artist(df, args)
    tracker.stop_task()

    tracker.start_task("query_expansion")
    words = query_expansion(model, args)
    tracker.stop_task()

    tracker.start_task("find_songs")
    songs = find_songs(words, args, df_filtered, nlp)
    tracker.stop_task()

    tracker.start_task("save_to_csv")
    percentage = save_csv(songs, df_filtered, args, out_folderpath)
    tracker.stop_task()

    tracker.start_task("save_plot")
    save_plot(args, percentage, df_filtered, out_folderpath)
    tracker.stop_task()

    tracker.stop()
  
if __name__ == "__main__":
    main()
