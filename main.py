import pandas as pd

# Load the dataset
data = pd.read_csv('IMDB Dataset.csv')


reviews = data['review']

print(reviews.head(10))

# print(data.describe())
