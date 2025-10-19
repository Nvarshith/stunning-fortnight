#Topic 1: Text Preprocessing & Tokenization. 
#Below are starter + intermediate questions, followed by answers and explanations. 
# Work through them, and I’ll also point out common pitfalls and variations.
#A. Given a paragraph string, write Python code to:

#Lowercase

#Remove punctuation

#Tokenize into words

#Remove stopwords

#(Bonus) Lemmatize each token

import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('omw-1.4')


stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
# Example A
paragraph = "I love programming in Python! It's fun and exciting."

def preprocessing(para):
    text = para.lower()
    
    rem_punc = text.translate(str.maketrans("","",string.punctuation))
    
    tokens = word_tokenize(rem_punc)
    
    rem_stopwords = [t for t in tokens if t not in stop_words]
    
    lematize = [lemmatizer.lemmatize(t) for t in rem_stopwords]
    
    return tokens, rem_stopwords, lematize
    
tokens, rem_stopwords, lematize = preprocessing(paragraph)
print("Tokens: ",tokens )
print("\nAfter Removing Stopwords: ",rem_stopwords)
print("\nlematized: ",lematize)

# Example B: show difference between naive split vs NLTK
text2 = "This is Alice's cat. She's sleeping."
naive = text2.translate(str.maketrans("","",string.punctuation)).split()
nltk_tok = word_tokenize(text2)
print("\nNaive: ",naive)
print("Nltk token: ",nltk_tok)

# Example C: compare stemming vs lemmatization
words = ["running", "runs", "ran", "easily", "fairly"]

lema=[lemmatizer.lemmatize(w)for w in words]
stema=[stemmer.stem(w)for w in words]

print("\n Words:",words)
print("Lemma:", lema)
print("Stemmer:", stema)



