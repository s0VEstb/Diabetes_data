import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('diabetes/diabetes_hw6_dataset.csv')
#print(df.head())
#print(df.tail(10))
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
#df.corr(numeric_only=True)
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()
df.loc[0, 'smoking_history']
df.iloc[0, 4]
df[df['age'] > 50]
df[(df['diabetes'] == 'Possitive') & (df['body_mass_index'] < 25)]
df[(df['gender'] == 'Female') & (df['heart_disease'] == 1)]
df[(df['diabetes'] == 'Positive') | (df['hypertension'] == 1)]
df[(df['age'] > 40) & (df['hypertension'] == 1) | (df['diabetes'] == 'Positive') & (df['body_mass_index'] < 30)]
def classify_HbA1c_level(HbA1c_level):
    if HbA1c_level < 5:
        return 'low'
    elif HbA1c_level >= 5 and HbA1c_level <= 7:
        return 'medium'
    else:
        return 'high'

df['HbA1c_level_category'] = df['HbA1c_level'].apply(classify_HbA1c_level)
classify_HbA1c_level(7.5)
plt.hist(df['age'], bins=10, color='skyblue', edgecolor='black')
df['diabetes'].value_counts().plot(kind='bar')
plt.scatter(df['body_mass_index'], df['blood_glucose_level'], color='red')
plt.boxplot(df['HbA1c_level'])
plt.boxplot(df['HbA1c_level'])
df.boxplot(column='age', by='diabetes')
#sns.distplot(df['body_mass_index'])
sns.pairplot(df[['age', 'diabetes']])
sns.boxplot(x='diabetes', y='HbA1c_level', data=df)
