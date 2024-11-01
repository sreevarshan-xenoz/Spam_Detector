import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
import joblib

# Load the dataset
def load_data(file_path):
    data = pd.read_csv(file_path, encoding='latin-1')
    data = data[['v1', 'v2']]  # Assuming 'v1' is the label and 'v2' is the message
    data.columns = ['label', 'message']
    return data

# Train the spam detector model
def train_model(data):
    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(data['message'], data['label'], test_size=0.2, random_state=42)

    # Create a pipeline that combines a CountVectorizer with a Naive Bayes classifier
    model = make_pipeline(CountVectorizer(), MultinomialNB())

    # Fit the model on the training data
    model.fit(X_train, y_train)

    # Evaluate the model
    accuracy = model.score(X_test, y_test)
    print(f'Model Accuracy: {accuracy * 100:.2f}%')

    return model

# Save the model and vectorizer
def save_model(model, model_filename, vectorizer_filename):
    joblib.dump(model.named_steps['multinomialnb'], model_filename)
    joblib.dump(model.named_steps['countvectorizer'], vectorizer_filename)

if __name__ == "__main__":
    # Load the dataset
    dataset = load_data('spam.csv')  # Replace with your dataset path

    # Train the model
    spam_model = train_model(dataset)

    # Save the model and vectorizer
    save_model(spam_model, 'spam_detector_model.pkl', 'vectorizer.pkl')

    print("Model and vectorizer saved successfully.")
