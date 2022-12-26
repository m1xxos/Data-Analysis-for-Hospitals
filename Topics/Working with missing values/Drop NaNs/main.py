import pandas as pd


students = pd.read_csv("./data/dataset/input.txt")

rows1 = students.shape[0]
students.dropna(axis=0, inplace=True)
rows2 = students.shape[0]

print(rows1, rows2)
