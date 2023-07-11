# I am using Multinomial Naive Bayes classifier to classify emails as spam or important based on their preprocessed text. 
# The preprocessed text is converted into a numerical feature vector using the TF-IDF vectorizer. 
# The performance of the classifier is evaluated on a testing set using metrics such as accuracy, precision, recall, and F1-score. 
# Then the trained classifier is used to classify a new email as spam or important.


import re
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load email data into a pandas DataFrame
emails = pd.read_csv('emails.csv')

# Define regular expression pattern to match email addresses
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Filter emails that match the pattern
filtered_emails = emails[emails['body'].str.contains(pattern, regex=True)]

# Split filtered emails into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(filtered_emails['body'], filtered_emails['label'], test_size=0.2, random_state=42)

# Preprocess email text using NLTK
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess_text(email_text):
    # Tokenize the text into individual words
    tokens = word_tokenize(email_text)
    
    # Convert all words to lowercase
    tokens = [word.lower() for word in tokens]
    
    # Remove stop words and stem the words
    tokens = [stemmer.stem(word) for word in tokens if word not in stop_words]
    
    # Join the stemmed words back into a string
    preprocessed_text = ' '.join(tokens)
    
    return preprocessed_text

# Convert preprocessed text into a numerical feature vector using Bag-of-Words or TF-IDF
vectorizer = TfidfVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train.apply(preprocess_text))
X_test_vectorized = vectorizer.transform(X_test.apply(preprocess_text))

# Train a machine learning model on the training set
model = MultinomialNB()
model.fit(X_train_vectorized, y_train)

# Evaluate the performance of the model on the testing set
y_pred = model.predict(X_test_vectorized)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label='spam')
recall = recall_score(y_test, y_pred, pos_label='spam')
f1 = f1_score(y_test, y_pred, pos_label='spam')
print('Accuracy:', accuracy)
print('Precision:', precision)
print('Recall:', recall)
print('F1-score:', f1)

# Use the trained model to classify new emails as spam or important
new_email_text = "Get a limited time offer! Buy now and get a money-back guarantee."
new_email_text_vectorized = vectorizer.transform([preprocess_text(new_email_text)])
new_email_classification = model.predict(new_email_text_vectorized)[0]
print('New email classification:', new_email_classification)
