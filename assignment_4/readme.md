# Assignment 4: Emotion analysis with pretrained language models


## About

This project uses the pre-trained ``Emotion English DistilRoBERTa-base`` classifier by ``j-hartmann``, which is available on ``Hugging Face``. It predicts emotion labels for each of the lines in the ``Game of Thrones Script`` dataset to see if the emotional profile changes through the series. *(See assignment description [here](https://github.com/CDS-AU-DK/cds-language/tree/main/assignments/assignment4))*

The ``src`` directory contains two scripts: 

- **query_expansion.py:** Produces the predictions made by the emotion classifier and extracts the emotion labels, which are then processed and saved as two separate csv files in the ``out`` directory. 

- **plotting_tools.py:** Plots the distribution of emotion labels for each season and the relative frequency of emotions across seasons and saves it in the ``out`` directory.


### Data

Download the dataset used for this project [here](https://www.kaggle.com/datasets/albenft/game-of-thrones-script-all-seasons?select=Game_of_Thrones_Script.csv), unzip the folder and place the ``Game_of_Thrones_Script.csv"`` in the ``in`` directory.


### Model

You can set up the [Emotion English DistilRoBERTa-base](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base) classifier for text classification as follows:

```sh
from transformers import pipeline

classifier = pipeline("text-classification",
                          model="j-hartmann/emotion-english-distilroberta-base",
                          top_k=1)

```

By setting ``top_k= 1, ``, the classifier only returns the top prediction, e.g., the emotion label with the highest score for each line.

##  File Structure

```
└── assignment_4
        |
        |
        ├── in
        │   └── Game_of_Thrones_Script.csv
        |
        ├── out
        |   ├── emotions
        |   |   ├── anger_distribution_across_seasons.jpg
        |   |   └── ...
        |   |
        |   ├── seasons
        |   |   ├── season_1_emotion_distribution.jpg
        |   |   └── ...
        |   |
        |   ├── emotion_distribution.csv
        |   └── emotions_across_seasons.csv
        |
        ├── src
        |   ├──emotion_analysis.py
        │   └── plotting_tools.py
        │     
        ├── readme.md
        ├── requirements.txt
        ├── run.sh
        └── setup.sh

```

## Usage

If you want to reproduce this project, please follow the steps below. The instructions will help you set up the environment and run the script. 

### Pre-Requisites

*Please make sure to install the following requirements before running the script.*

**Python**: version 3.12.3

### Installation

**1.** Clone the repository using Git.
```sh
git clone https://github.com/trinerye/language_analytics_2024.git 
```

**2.** Change directory to the assignment folder.
```sh
cd assignment_4
```

**3.** Run ``setup.sh`` to create an environment and install the dependencies needed for this project. 

```sh
bash setup.sh
```
**4.** Run ``run.sh`` to activate the environment and run the main script. 
  
```sh
bash run.sh
```
```sh
...
# Activate the environment (Unix/macOS)
source ./LA_A4_env/bin/activate

# Run the code
python src/emotion_analysis.py

# Deactivate the environment
deactivate
```

## Results 

In the ``out`` directory, you can find a filtered and unfiltered version of the Game of Thrones predictions. It also holds the ``emotions`` and ``seasons`` folders, which contain the plots showing the distribution of emotion labels for each season and the relative frequency of emotions across seasons.

| Season   | Anger | Disgust | Fear | Joy | Neutral | Sadness | Surprise |
|----------|-------|---------|------|-----|---------|---------|----------|
| Season 1 | 0.17  | 0.11    | 0.04 | 0.04| 0.45    | 0.06    | 0.12     |
| Season 2 | 0.16  | 0.11    | 0.05 | 0.04| 0.48    | 0.05    | 0.11     |
| Season 3 | 0.14  | 0.12    | 0.05 | 0.04| 0.48    | 0.05    | 0.12     |
| Season 4 | 0.16  | 0.11    | 0.05 | 0.04| 0.46    | 0.06    | 0.12     |
| Season 5 | 0.15  | 0.10    | 0.05 | 0.05| 0.48    | 0.06    | 0.12     |
| Season 6 | 0.16  | 0.09    | 0.04 | 0.04| 0.50    | 0.07    | 0.10     |
| Season 7 | 0.15  | 0.08    | 0.05 | 0.04| 0.52    | 0.04    | 0.11     |
| Season 8 | 0.18  | 0.07    | 0.04 | 0.04| 0.50    | 0.06    | 0.12     |

Based on this overview of the emotion distribution across seasons, Game of Thrones is not a very joyful series - as in - many lines in the script are not associated with the emotion label joy.

On the other hand, emotions such as anger and disgust score high across the dataset, with anger having the highest relative frequency of lines besides that of neutral emotions. Looking at anger specifically, it makes sense that season eight is the angriest, as this is where the final battle between good and evil occurs. It also makes sense that the relative frequency of lines that express surprise is somewhat uniform across all seasons, as the show was known for its suspenseful cliffhangers and the kill-your-darlings concept. 

Although all emotions are present within the dataset, it is no surprise that lines containing neutral emotion appear much more often than any other emotion, likely due to filler words, monotone language, or the lack of adjectives.

In conclusion, while the distribution of emotions across each season stays pretty much the same, the progression of each emotion changes throughout the series. 

### Limitations and future improvments 

- Since we do not know why the lines are associated with specific emotions, as the classifier black-boxes this, we could perform a linguistic analysis on the dataset, counting the frequency of adjectives which carry many emotions versus more neutral adverbs to uncover this.  


## Code Carbon

Please ignore the code related to ``Code Carbon``, as it is part of another assignment and, therefore, unnecessary to reproduce this project. 

*For more information about this project's environmental impact, see [assignment_5](../assignment_5/readme.md).*



