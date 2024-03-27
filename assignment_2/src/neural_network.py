import os
from sklearn.neural_network import MLPClassifier
from sklearn import metrics
import joblib
from vectorizer import file_loader, load_data, vectorize_data

# This function trains the neural network model on the transformed training data and its corresponding labels.
def train_model(X_train_feats, y_train):
    print("Training the neural network classifier")
    return MLPClassifier(hidden_layer_sizes = (128,), max_iter=1000, random_state = 42).fit(X_train_feats, y_train)

# This function evaluates the performance of the trained classifier on the test dataset and produces a classification report contaning metrics like precision, recall, and F1-score.
def evaluate_model(classifier, X_test_feats, y_test):
    print("Creating the classification report")
    return metrics.classification_report(y_test, classifier.predict(X_test_feats)) # the second parameter is the prediction (y_pred)

# This function saves the classification report
def save_report(classifier_metrics, out_path):
    # Opens the file in the out folder in write mode and writes the classification metrics to it.
    with open(out_path, "w") as file:
        file.write(classifier_metrics)
   
def main():
     # If the directory does not exist, make the directory
    os.makedirs(os.path.join("out", "neural_network"), exist_ok=True)
    os.makedirs(os.path.join("models", "neural_network"), exist_ok=True)

    # Filepath for each used file or saved file
    data_path = os.path.join(file_loader().input)
    model_path = os.path.join("models", "neural_network", "neural_network_classifier.joblib")
    vectorizer_path = os.path.join("models", "neural_network", "tfidf_vectorizer.joblib")
    out_path = os.path.join("out", "neural_network", "classification_report.txt")

    # Calling all functions, saving them as variables 
    X_train, X_test, y_train, y_test = load_data(data_path)
    vectorizer, X_train_feats, X_test_feats = vectorize_data(X_train, X_test)
    classifier = train_model(X_train_feats, y_train)
    classifier_metrics = evaluate_model(classifier, X_test_feats, y_test)
    save_report(classifier_metrics, out_path)

    # Saving the logistic regression classifier and the vectorizer
    print("Saving the classifier and the vectorizer")
    joblib.dump(classifier, model_path)
    joblib.dump(vectorizer, vectorizer_path)

if __name__ == "__main__":
    main()

