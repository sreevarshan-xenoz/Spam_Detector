# Spam Detector Using Naive Bayes Classifier

This project implements a spam detector using the Naive Bayes algorithm in Python. The goal is to create a spam filter that accurately classifies messages as spam or ham (non-spam) with an accuracy greater than 80%. The project serves as a practical application of machine learning techniques in text classification.

## Table of Contents

- [Project Overview](#project-overview)
- [Motivation](#motivation)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
  - [Training the Model](#training-the-model)
  - [Running the GUI](#running-the-gui)
- [Model Evaluation](#model-evaluation)
- [Additional Features](#additional-features)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

In this project, we build a spam filter that can classify SMS messages. The Naive Bayes classifier is chosen for its effectiveness and simplicity in handling text data. The spam filter aims to help users avoid unwanted messages and enhance their messaging experience.

## Motivation

With the increasing volume of unsolicited messages (spam) that people receive daily, there is a growing need for effective spam detection systems. This project aims to provide a robust solution for classifying messages, making it easier for users to manage their communication and focus on important messages.

## Dataset

The dataset used for training and testing the model consists of 5,572 SMS messages collected from various sources. The dataset is available in CSV format, with two main columns:

- **label**: Indicates whether the message is "spam" or "ham".
- **message**: Contains the actual SMS message text.

### Dataset Source
The dataset used in this project is a well-known public dataset from the UCI Machine Learning Repository. You can download it from [here](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection).

### Data Preprocessing
Before training the model, the dataset undergoes the following preprocessing steps:
- **Data Cleaning**: Removal of punctuation marks and conversion of all text to lowercase to maintain uniformity.
- **Tokenization**: Splitting messages into individual words (tokens) for further analysis.

## Installation

To set up the project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd spam-detector
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`



pip install pandas scikit-learn joblib tk



Usage
Training the Model

To train the spam detector model, run the following command:

bash

python spam_detector.py

This script will:

    Load the dataset.
    Preprocess the data (cleaning and tokenization).
    Train the Naive Bayes model on the training set.
    Save both the model and vectorizer to disk as model.pkl and vectorizer.pkl, respectively.

Running the GUI

After training the model, you can run the graphical user interface (GUI) with:

bash

python gui.py

The GUI will allow you to:

    Input SMS messages.
    Check if the message is classified as spam or ham.
    View the classification results in a user-friendly format.
