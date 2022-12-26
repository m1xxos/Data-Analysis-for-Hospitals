import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 8)

general = pd.read_csv("C:/Users/bulyn/Downloads/files/test/general.csv")
prenatal = pd.read_csv("C:/Users/bulyn/Downloads/files/test/prenatal.csv")
sports = pd.read_csv("C:/Users/bulyn/Downloads/files/test/sports.csv")

prenatal.rename(columns={"Sex": "gender", "HOSPITAL": "hospital"}, inplace=True)
sports.rename(columns={"Male/female": "gender", "Hospital": "hospital"}, inplace=True)

hospital = pd.concat([general, prenatal, sports], ignore_index=True)
hospital.drop(columns="Unnamed: 0", inplace=True)

hospital.dropna(axis=0, thresh=1, inplace=True)

hospital["gender"].replace(["female", "woman"], "f", inplace=True)
hospital["gender"].replace(["male", "man"], "m", inplace=True)

hospital.loc[(hospital["hospital"] == "prenatal") & hospital["gender"].isna(), "gender"] = "f"

hospital.loc[:, "bmi":"months"] = hospital.loc[:, "bmi":"months"].fillna(0)

max_patients = hospital["hospital"].value_counts().idxmax()
general_patients = hospital["hospital"].value_counts()["general"]
sports_patients = hospital["hospital"].value_counts()["sports"]

general_stomach = hospital.loc[hospital["hospital"] == "general", "diagnosis"].value_counts()["stomach"] \
                  / general_patients
sports_dislocation = hospital.loc[hospital["hospital"] == "sports", "diagnosis"].value_counts()["dislocation"] \
                     / sports_patients

age_diff = hospital.loc[hospital["hospital"] == "general", "age"].median() - \
           hospital.loc[hospital["hospital"] == "sports", "age"].median()

blood_tests = hospital.groupby('hospital')["blood_test"].value_counts()

bins = [0, 15, 35, 55, 70, 80]

plt.figure()
hospital["age"].plot(kind="hist", bins=bins)
plt.figure()
hospital["diagnosis"].value_counts().plot(kind="pie", autopct='%.1f%%')
plt.figure()
plt.violinplot(hospital['height'])

plt.show()
print("The answer to the 1st question: 15-35")
print("The answer to the 2nd question: pregnancy")
print("The answer to the 3rd question: bigger numbers = more deviation")
