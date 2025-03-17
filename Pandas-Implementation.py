import pandas as pd

# Load dataset
df = pd.read_csv("C:/Users/SAI/Downloads/Titanic-Dataset.csv")

# 1. Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head(), "\n")

# 2. Get basic info about dataset
print("Basic info about the dataset:")
print(df.info(), "\n")

# 3. Check for missing values
print("Missing values in each column:")
print(df.isnull().sum(), "\n")

# 4. Describe the dataset (summary statistics)
print("Summary statistics of the dataset:")
print(df.describe(), "\n")

# 5. Select specific columns
print("Selected columns (Name, Age, Survived):")
print(df[['Name', 'Age', 'Survived']], "\n")

# 6. Filter passengers who survived
survived_passengers = df[df['Survived'] == 1]
print("First 5 rows of survived passengers:")
print(survived_passengers.head(), "\n")

# 7. Grouping and Aggregation (Average age of survivors vs non-survivors)
grouped_data = df.groupby('Survived')['Age'].mean()
print("Average Age of Survivors vs Non-Survivors:")
print(grouped_data, "\n")

# 8. Sorting passengers by fare
sorted_df = df.sort_values(by='Fare', ascending=False)
print("Top 5 passengers sorted by Fare:")
print(sorted_df.head(), "\n")

# 9. Handling missing values (Fill missing Age with median)
df['Age'].fillna(df['Age'].median(), inplace=True)
print("Missing values in 'Age' column filled with median.")
