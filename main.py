import pandas as pd
from bs4 import BeautifulSoup
import re
data = pd.read_csv('IMDB Dataset.csv')
import nltk as nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

reviews = data['review']
# print(reviews.head(10))

print("Cleaning the first review:")

# removing html tags
clean_text = BeautifulSoup(reviews[1], 'html.parser').get_text()

# remove special characters and numbers
clean_text = re.sub('[^A-Za-z]+', ' ', clean_text)

# machine learning algorithms recognize words that start with a capital letter as different words, and we will convert them to lowercase. Thus, our machine learning algorithms will not perceive words that start with a capital letter as a different word.
clean_text = clean_text.lower()

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# tokenization 
clean_text = clean_text.split()
# print(clean_text)

# removing stopwords
for i in clean_text:
    if i in stopwords.words('english'):
        clean_text.remove(i)

print(clean_text)