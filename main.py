from spam_detector import load_data, preprocess_data, train_model

# Load and preprocess the data
df = load_data()
X, y = preprocess_data(df)

# Train the model
vectorizer, model = train_model(X, y)

# Save the trained model and vectorizer for later use if needed
import joblib

joblib.dump(vectorizer, 'vectorizer.pkl')
joblib.dump(model, 'model.pkl')
