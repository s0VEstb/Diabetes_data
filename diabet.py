import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('diabetes_hw6_dataset.csv')
#print(df.head())
#print(df.info())
#print(df.describe())
#print(df.isnull().sum())
df = df.drop_duplicates()
#print(df.info())
#print(type(df))
bmi_row = df['bmi']
Hba1c_level_row = df['HbA1c_level']
male_bmi_mean = df['bmi'][(df['gender'] == 'Male')].mean()
female_bmi_mean = df['bmi'][(df['gender'] == 'Female')].mean()
male_Hba1c_mean = df['HbA1c_level'][(df['gender'] == 'Male')].mean()
female_Hba1c_mean = df['HbA1c_level'][(df['gender'] == 'Female')].mean()
df.loc[df['gender'] == 'Male', 'bmi'] = df.loc[df['gender'] == 'Male', 'bmi'].fillna(male_bmi_mean)
df.loc[df['gender'] == 'Female', 'bmi'] = df.loc[df['gender'] == 'Female', 'bmi'].fillna(female_bmi_mean)
df.loc[df['gender'] == 'Male', 'HbA1c_level'] = df.loc[df['gender'] == 'Male', 'HbA1c_level'].fillna(male_Hba1c_mean)
df.loc[df['gender'] == 'Female', 'HbA1c_level'] = df.loc[df['gender'] == 'Female', 'HbA1c_level'].fillna(female_Hba1c_mean)
print(df.isnull().sum())
df.rename(columns={'bmi': 'body_mass_index'}, inplace=True)
df['body_mass_index'].value_counts()
df['HbA1c_level'].value_counts()
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()
