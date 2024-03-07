# %%
# Logistic Regression Classifier
import os
import pandas as pd

import sys
sys.path.append("..")
import utils.classifier_utils as clf

# Machine learning stuff
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, ShuffleSplit
from sklearn import metrics

# Visualisation
import matplotlib.pyplot as plt

# %%

# Loading data
data = pd.read_csv(os.path.join("data","fake_or_real_news.csv"))

X_train, X_test, y_train, y_test = train_test_split(data["text"], # X
                                                    data["label"], # y
                                                    test_size=0.2, random_state=42) 
# Fitting the model
vectorizer = TfidfVectorizer(ngram_range = (1,2),
                             lowercase =  True,       
                             max_df = 0.95,          
                             min_df = 0.05,           
                             max_features = 1835) # 1835   


X_train_feats = vectorizer.fit_transform(X_train)

X_test_feats = vectorizer.transform(X_test)

classifier = LogisticRegression(random_state=42).fit(X_train_feats, y_train)

# Report
y_pred = classifier.predict(X_test_feats)

classifier_metrics = metrics.classification_report(y_test, y_pred)

with open('classification_report.txt', 'w') as file:
   
    file.write(classifier_metrics)

# "with" is best python practice for file handling, as it makes the code cleaner and avoids common pitfalls such as forgetting to close files.
# "open" does as it says and opens/creates the text file in write mode "w" and saves it as file
# Writes the classification_report in the text file
