import pandas as pd
from bs4 import BeautifulSoup
data = pd.read_csv('IMDB Dataset.csv')


reviews = data['review']
# print(reviews.head(10))



print("Cleaning the first review:")
clean_text = BeautifulSoup(reviews[1], 'html.parser').get_text()
print(clean_text)
# print(data.describe())
