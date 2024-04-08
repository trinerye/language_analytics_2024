import os
import gensim
import pandas as pd
import argparse
import spacy
import gensim.downloader as api

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--word",
                        "-w",
                        required = True)

    parser.add_argument("--artist",
                        "-a",
                        required = True)

    return parser.parse_args()

# This function loads the word embedding model and the en_core_web_md model from spacy
def load_models():
    print("Loading models") 
    model = api.load("glove-wiki-gigaword-50")
    nlp = spacy.load("en_core_web_md")
    return model, nlp

# This function reads the data from the spotify_million_song_dataset_exported.csv
def load_data(in_folderpath):
    print("Loading the data")
    return pd.read_csv(os.path.join(in_folderpath, "spotify_million_song_dataset_exported.csv")) 

# This function filters the dataframe by the artist column, only including rows where the name of the artist matches the argparse argument 
def filtered_by_artist(df, args):
    return df[df['artist'].str.lower() == args.artist.lower()]

# This function finds the 10 (default) most similar words to the argparse 'word' argument without their similarity score 
def find_similar_words(model, args):

    print(f"Searching for similar words to '{args.word.lower()}'")
    # The 'most_similar' method returns a list of tuples (a word + similarity score)
    similar_words_list = model.most_similar(args.word.lower())

    similar_words = []

# Iterates over the list of tuples in the similar_words_list, appending only the first element (the word) from each tuple to a new list, similar_words"
    for word in similar_words_list:

        similar_words.append(word[0])
    
    print(similar_words)

    return similar_words


# This function return a number of songs by a given artist which contains any of the words from the similar_words list
def find_songs_with_similar_words(similar_words, args, filtered_by_artist_df, nlp):
    
    print(f"Finding songs that contains words similar to '{args.word.lower()}'")

    songs = []

    # For each row in the filtered_by_artist_df
    for i, row in filtered_by_artist_df.iterrows():

        # tokinize the text in the dataframe 'text' column
        doc = nlp(row['text'])

        tokens = []

        # For each token in doc (the text in the 'text' column)
        for token in doc:
            # If the token is not punctuation or a new line (\n) then...
            if not token.is_punct and "\n" not in token.text:
                # convert the tokenized text to lowercase and add it to the tokens list

                cleaned_token = token.text.lower().replace("'", "")

                tokens.append(cleaned_token)

        # Checks if words from the similar_words list is in the tokens list after processing all tokens
        if any(word in similar_words for word in tokens):
            # Append the song to the corresponding list if a word from the extended query is found within the tokenized text
            songs.append(row['song'])
    
    print(tokens)
    
    return songs

def calculate_and_save_result(songs, filtered_by_artist_df, args, out_folderpath):

    percentage = round(len(songs) / len(filtered_by_artist_df) * 100)

    print(f"Result: {percentage}% of {args.artist}'s songs contains words similar to the search word '{args.word.lower()}'")

    result_df = pd.DataFrame(songs, columns=["Song (A-Z)"])

    result_df.to_csv(os.path.join(out_folderpath, f"{args.artist.lower()}_songs_related_to_{args.word.lower()}.csv"))


def main():
    
    args = parser()

    # Creates a filepath for each directory 
    in_folderpath = os.path.join("in")
    out_folderpath = os.path.join("out")

    # If the directory does not exist, make the directory
    os.makedirs(out_folderpath, exist_ok=True)

    model, nlp = load_models()

    df = load_data(in_folderpath)

    filtered_by_artist_df = filtered_by_artist(df, args)

    similar_words = find_similar_words(model, args)

    songs = find_songs_with_similar_words(similar_words, args, filtered_by_artist_df, nlp)

    calculate_and_save_result(songs, filtered_by_artist_df, args, out_folderpath)
  
if __name__ == "__main__":
    main()


