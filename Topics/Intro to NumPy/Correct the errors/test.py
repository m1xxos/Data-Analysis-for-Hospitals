import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/GitHub/Data Analysis for Hospitals/Topics/Intro to NumPy/2015.csv")
df.plot(y=["Family", "Freedom", "Trust (Government Corruption)"], kind='box', showmeans=True)
plt.show(bbox_inches='tight')

