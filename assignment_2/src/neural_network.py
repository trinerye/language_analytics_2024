import os
from sklearn.neural_network import MLPClassifier
from sklearn import metrics
import joblib
from vectorizer import parser, load_data, vectorize_data

# This function trains the neural network model on the transformed training data and its corresponding labels.
def train_model(X_train_feats, y_train):
    print("Training the neural network classifier")
    return MLPClassifier(hidden_layer_sizes = (128,), max_iter=1000, random_state = 42).fit(X_train_feats, y_train)

# This function evaluates the performance of the trained classifier on the test dataset and produces a classification report contaning metrics like precision, recall, and F1-score.
def evaluate_model(classifier, X_test_feats, y_test):
    print("Creating the classification report")
    return metrics.classification_report(y_test, classifier.predict(X_test_feats)) # the second parameter is the prediction (y_pred)

# This function saves the classification report
def save_report(classifier_metrics, report_path):
    # Opens the file in the out folder in write mode and writes the classification metrics to it.
    with open(report_path, "w") as file:
        file.write(classifier_metrics)
   
def main():
     
    # Creates a filepath for each directory 
    out_folderpath = os.path.join("out", "neural_network")
    models_folderpath = os.path.join("models", "neural_network")

    # If the directory does not exist, make the directory
    os.makedirs(out_folderpath, exist_ok=True)
    os.makedirs(models_folderpath, exist_ok=True)

    # Filepath for each saved file
    classifier_path = os.path.join(models_folderpath, "neural_network_classifier.joblib")
    vectorizer_path = os.path.join(models_folderpath, "tfidf_vectorizer.joblib")
    report_path = os.path.join(out_folderpath, "classification_report.txt")

    # Calling all functions, saving them as variables 
    X_train, X_test, y_train, y_test = load_data()
    vectorizer, X_train_feats, X_test_feats = vectorize_data(X_train, X_test)
    classifier = train_model(X_train_feats, y_train)
    classifier_metrics = evaluate_model(classifier, X_test_feats, y_test)
    save_report(classifier_metrics, report_path)

    # Saving the logistic regression classifier and the vectorizer
    print("Saving the classifier and the vectorizer")
    joblib.dump(classifier, classifier_path)
    joblib.dump(vectorizer, vectorizer_path)

if __name__ == "__main__":
    main()

