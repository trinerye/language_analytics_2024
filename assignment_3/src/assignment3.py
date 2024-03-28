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

def main():
    args = parser()

    print("Loading models") 
    model = api.load("glove-wiki-gigaword-50")
    nlp = spacy.load("en_core_web_md")

    print("Loading the data")
    df = pd.read_csv(os.path.join("in", "spotify_million_song_dataset_exported.csv")) 
   
    filtered_by_artist_df = df[df['artist'].str.lower() == args.artist.lower()]

    print(f"Searching for similar words to '{args.word.lower()}'")
    similar_words_lists = model.most_similar(args.word.lower())

    similar_words = []

    for word in similar_words_lists:

        similar_words.append(word[0])
    
    print(f"Finding songs that contains words similar to '{args.word.lower()}'")
    songs = []

    for i, row in filtered_by_artist_df.iterrows():

        doc = nlp(row['text'])

        # Creates an empty list for the tokens
        tokens = []

        for token in doc:
            # If the token is not punctuation then...
            if not token.is_punct:
                # convert the tokenized text to lowercase and add it to the tokens list
                tokens.append(token.text.lower())

        # Check if  words from the  is in the tokens list after processing all tokens
        if any(word in similar_words for word in tokens):
            # Append the song to the corresponding list if a word from the extended query is found within the tokenized text
            songs.append(row['song'])
        
    percentage = round(len(songs) / len(filtered_by_artist_df) * 100)

    print(f"Result: {percentage}% of {args.artist}'s songs contains words similar to the search word '{args.word.lower()}'")

    result_df = pd.DataFrame(songs, columns=["Song (A-Z)"])

    os.makedirs(os.path.join("out"), exist_ok=True)

    result_df.to_csv(f"{'out', args.artist.lower()}_songs_related_to_{args.word.lower()}.csv")

if __name__ == "__main__":
    main()


