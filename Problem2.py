# Problem 2: TF-IDF Cosine Similarity Across Speakers
# Task:
# You have a set of speakers, each with one or more messages (text). 
# Treat each speaker’s collection of messages as a “document.” 
# Compute the TF-IDF vector for each speaker, then compute pairwise cosine similarity between every pair of speakers. 
# Output those similarity scores.

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import math
from collections import defaultdict,Counter
from nltk.tokenize import word_tokenize
import string

nltk.download("punkt")
nltk.download("wordnet")
nltk.download("stopwords")

# Example data
messages = [
    "Alice: I love programming in Python",
    "Bob: Python is great and easy to learn",
    "Alice: Python is my favorite language",
    "Charlie: I prefer Java over Python",
    "Bob: I also like JavaScript"
]

# 1. Preprcesing + collection per speaker
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocessing(text):
    text = text.lower()
    # Removing the punctuation
    text = text.translate(str.maketrans("","",string.punctuation))
    # Tokens
    tokens = word_tokenize(text)
    
    # Removing stop words
    filtered = [t for t in tokens if t not in stop_words]
    
    #Lematizing
    lemmas = [lemmatizer.lemmatize(t) for t in filtered]
    
    return lemmas

print(preprocessing("Alice: I love programming in Python"))