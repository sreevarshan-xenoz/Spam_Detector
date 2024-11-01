import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Load your dataset
# Make sure to replace 'spam_dataset.csv' with the path to your actual dataset
data = pd.read_csv('spam_dataset.csv')  # Ensure you have this dataset

# Preprocess the dataset
X = data['message']  # Column containing messages
y = data['label']    # Column containing labels (spam/ham)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the vectorizer
vectorizer = CountVectorizer()

# Fit and transform the training data
X_train_vect = vectorizer.fit_transform(X_train)

# Train the model
model = MultinomialNB()
model.fit(X_train_vect, y_train)

# Save the model and the vectorizer
joblib.dump(model, 'spam_detector_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Model and vectorizer saved successfully.")
