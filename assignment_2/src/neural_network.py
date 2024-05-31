import os
from codecarbon import EmissionsTracker
from sklearn.neural_network import MLPClassifier
from sklearn import metrics
import joblib

# This function loads the saved vectorized texts and labels 
def load_vectorized_data(vectorizer_path):
    X_train_feats, X_test_feats = joblib.load(os.path.join(vectorizer_path, "vectorized_texts.joblib"))
    y_train, y_test = joblib.load(os.path.join(vectorizer_path, "labels.joblib"))
    return X_train_feats, X_test_feats, y_train, y_test

# This function trains the neural network classifier and fits it to the training data
def train_model(X_train_feats, y_train):
    print("Training the neural network classifier")
    classifier = MLPClassifier(hidden_layer_sizes = (128,), random_state = 42, early_stopping=True, verbose = True)
    classifier.fit(X_train_feats, y_train)
    return classifier

# This function saves the classifier in the corresponding folder in the models directory 
def save_classifier(classifier, classifier_path):
    print("Saving the classifier")
    joblib.dump(classifier, os.path.join(classifier_path, "neural_network_classifier.joblib"))

# This function creates a classification report that evaluates the performance of the classifier
def evaluate_classifier(classifier, X_test_feats, y_test):
    print("Creating the classification report")
    return metrics.classification_report(y_test, classifier.predict(X_test_feats)) # the second parameter is the prediction (y_pred)

# This function saves the classification report in the out directory
def save_report(classifier_metrics, out_folderpath):
    print("Saving classification report")
    with open(os.path.join(out_folderpath, "neural_network_classification_report.txt"), "w") as f:
        f.write(classifier_metrics)
   
def main():
     
   # Creates a folderpath for each directory and makes the directory if it does not exist
    out_folderpath = os.path.join("out")
    vectorizer_path = os.path.join("models", "vectorizer")
    classifier_path = os.path.join("models", "classifiers")
    emissions_folderpath = os.path.join("..", "assignment_5", "emissions")
    os.makedirs(out_folderpath, exist_ok=True)  
    os.makedirs(classifier_path, exist_ok=True)
    os.makedirs(emissions_folderpath, exist_ok=True)    

    # Initializes the emissions tracker by codecarbon
    tracker = EmissionsTracker(project_name="text_classification",
                               output_file="emissions.csv",
                               output_dir=emissions_folderpath)

    # Tracks the function that loads the vectorized data
    tracker.start_task("load_vectorized_data")
    X_train_feats, X_test_feats, y_train, y_test = load_vectorized_data(vectorizer_path)
    tracker.stop_task()

    # Tracks the function that trains the neural network classifier
    tracker.start_task("train_neural_network_classifier")
    classifier = train_model(X_train_feats, y_train)
    tracker.stop_task()

    # Tracks the function that saves the neural network classifier
    tracker.start_task("save_neural_network_classifier")
    save_classifier(classifier, classifier_path)
    tracker.stop_task()

    # Tracks the function that produces the classification report
    tracker.start_task("create_neural_network_classification_report")
    classifier_metrics = evaluate_classifier(classifier, X_test_feats, y_test)
    tracker.stop_task()

    # Tracks the function that saves the classification report
    tracker.start_task("save_neural_network_classification_report")
    save_report(classifier_metrics, out_folderpath)
    tracker.stop_task()

    tracker.stop()
   
if __name__ == "__main__":
    main()

