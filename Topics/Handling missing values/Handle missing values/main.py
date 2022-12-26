import pandas as pd


city = pd.read_csv("./data/dataset/input.txt")
city.dropna(axis=1, thresh=7, inplace=True)
for i in city.columns:
    city[i].fillna(city[i].median(), inplace=True)

print(city.head(5))
