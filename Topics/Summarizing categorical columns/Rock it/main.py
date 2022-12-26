import pandas as pd

df_rock = pd.read_csv("./data/dataset/input.txt")
print(df_rock.labels.value_counts()["R"])

