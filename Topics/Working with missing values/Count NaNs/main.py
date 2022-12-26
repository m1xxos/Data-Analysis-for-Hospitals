import pandas as pd


students = pd.read_csv("./data/dataset/input.txt")
print(students.isna().sum())

