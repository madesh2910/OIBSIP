# Email Spam Detection Using Machine Learning

## Project Overview

This project develops a machine learning-based text classification system using Natural Language Processing (NLP) to identify spam and legitimate (ham) messages.

The SMS Spam Collection dataset is used to train and evaluate two classification algorithms.

## Objectives

- Analyze spam and ham message distributions.
- Perform text preprocessing.
- Convert text into numerical features using TF-IDF.
- Train and compare two machine learning classifiers.
- Evaluate model performance using classification metrics.
- Predict whether new messages are spam or ham.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Matplotlib
- Seaborn
- WordCloud
- Jupyter Notebook

## Dataset

**SMS Spam Collection Dataset**

Source: https://archive.ics.uci.edu/dataset/228/sms+spam+collection

The dataset contains approximately 5,574 messages categorized as spam or ham.

## Machine Learning Algorithms

1. Multinomial Naive Bayes
2. Logistic Regression

Both algorithms are compared using accuracy, precision, recall, F1-score, and confusion matrices.

## Project Workflow

1. Dataset collection and loading
2. Exploratory Data Analysis
3. Text preprocessing
4. TF-IDF feature extraction
5. Training and testing
6. Model evaluation and comparison
7. Final model selection
8. New message prediction
9. WordCloud visualization

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

## Project Files

- `notebooks/`: Jupyter Notebook containing the complete implementation.
- `images/`: Project visualization outputs.
- `saved_model/`: Trained model and TF-IDF vectorizer, if included.
- `requirements.txt`: Required Python libraries.

## Limitation

The dataset contains SMS messages rather than full-length emails. Therefore, this project demonstrates SMS spam classification using NLP.

## Author

Madesh P.

## Conclusion

This project demonstrates the application of NLP and machine learning techniques for automated spam message classification.
