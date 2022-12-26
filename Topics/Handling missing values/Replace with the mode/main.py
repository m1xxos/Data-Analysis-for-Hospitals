import pandas as pd


city = pd.read_csv("./data/dataset/input.txt")
location = city["location"].mode()[0]
city["location"].fillna(location, inplace=True)
print(city.head(5))
