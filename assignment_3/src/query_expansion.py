import os
import gensim
import pandas as pd
import argparse
import spacy
import gensim.downloader as api
from tqdm import tqdm


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
    df =  pd.read_csv(os.path.join(in_folderpath, "spotify_million_song_dataset_exported.csv")) 

    return df


def filter_by_artist(df, args):

    print(f"Finding songs by {args.artist}")

    # Filters the dataframe by artist if the name of the artist matches the argparse argument 
    df_filtered = df[df['artist'].str.lower() == args.artist.lower()]

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


def save_results(songs, df_filtered, args, out_folderpath):

    # Calculate the percentage of songs from a given artist that contains one of the words from the query expansion 
    percentage = round(len(songs) / len(df_filtered) * 100, 2)

    print(f"Result: {percentage}% of {args.artist}'s songs contains words similar to '{args.word.lower()}'") ### Make this some cool color

    # Creates a new dataframe that only contains the songs where words from the query expansion appear
    df_results = pd.DataFrame(songs, columns=["Song (A-Z)"])

    # Saves the results as a csv file in the out directory 
    df_results.to_csv(os.path.join(out_folderpath, f"{args.artist.lower()}_songs_related_to_{args.word.lower()}.csv"))


def main():
    
     # Creates a folderpath for each directory and makes the directory if it does not exist
    in_folderpath = os.path.join("in")
    out_folderpath = os.path.join("out")
    os.makedirs(out_folderpath, exist_ok=True)



    args = parser()

    model, nlp = load_models()

    df = load_data(in_folderpath)

    df_filtered = filter_by_artist(df, args)

    words = query_expansion(model, args)

    songs = find_songs(words, args, df_filtered, nlp)

    save_results(songs, df_filtered, args, out_folderpath)
  
if __name__ == "__main__":
    main()


