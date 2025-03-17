#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# Load dataset
df = pd.read_csv("C:/Users/SAI/Downloads/Titanic-Dataset.csv")

# 1. Display first 5 rows
print(df.head())

# 2. Get basic info about dataset
print(df.info())

# 3. Check for missing values
print(df.isnull().sum())

# 4. Describe the dataset (summary statistics)
print(df.describe())

# 5. Select specific columns
print(df[['Name', 'Age', 'Survived']])

# 6. Filter passengers who survived
survived_passengers = df[df['Survived'] == 1]
print(survived_passengers.head())

# 7. Grouping and Aggregation (Average age of survivors vs non-survivors)
grouped_data = df.groupby('Survived')['Age'].mean()
print(grouped_data)

# 8. Sorting passengers by fare
sorted_df = df.sort_values(by='Fare', ascending=False)
print(sorted_df.head())

# 9. Handling missing values (Fill missing Age with median)
df['Age'].fillna(df['Age'].median(), inplace=True)

# 10. Save modified DataFrame
df.to_csv("processed_titanic.csv", index=False)


# In[ ]:




