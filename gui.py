import tkinter as tk
from tkinter import messagebox
import joblib

# Load the trained model and vectorizer
model = joblib.load('spam_detector_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Function to classify the message
def classify_message():
    message = entry.get()
    if message:
        message_vect = vectorizer.transform([message])
        prediction = model.predict(message_vect)
        result = "Spam" if prediction[0] == 'spam' else "Not Spam"
        messagebox.showinfo("Prediction Result", f"The message is: {result}")
    else:
        messagebox.showwarning("Input Error", "Please enter a message to classify.")

# Create the main window
root = tk.Tk()
root.title("Spam Detector")

# Create and place the input field
entry = tk.Entry(root, width=50)
entry.pack(pady=20)

# Create and place the classify button
classify_button = tk.Button(root, text="Classify Message", command=classify_message)
classify_button.pack(pady=10)

# Run the application
root.mainloop()
