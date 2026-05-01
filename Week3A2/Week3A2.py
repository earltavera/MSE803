import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
# Note: Path simplified to relative path as per standard environment usage
file_path = 'messy_dataset.csv'
df = pd.read_csv(file_path)

# --- 1. INITIAL EXPLORATION ---
print("--- Initial Info ---")
df.info()
print("\n--- Initial Head ---")
print(df.head())
print("\n--- Missing Values Before Cleaning ---")
print(df.isnull().sum())

# --- 2. DATA CLEANING ---
df_cleaned = df.copy()

# A. Handle Age: Convert text 'thirty-eight' to 38, handle non-numerics, fill NaNs with median
df_cleaned['Age'] = df_cleaned['Age'].replace('thirty-eight', 38)
df_cleaned['Age'] = pd.to_numeric(df_cleaned['Age'], errors='coerce')
df_cleaned['Age'] = df_cleaned['Age'].fillna(df_cleaned['Age'].median())

# B. Handle Salary: Convert to numeric, fill NaNs with median
df_cleaned['Salary'] = pd.to_numeric(df_cleaned['Salary'], errors='coerce')
df_cleaned['Salary'] = df_cleaned['Salary'].fillna(df_cleaned['Salary'].median())

# C. Handle ID: Ensure numeric and fill missing IDs (max + 1)
df_cleaned['ID'] = pd.to_numeric(df_cleaned['ID'], errors='coerce')
df_cleaned['ID'] = df_cleaned['ID'].fillna(df_cleaned['ID'].max() + 1)

# D. Remove Duplicates: Based on core descriptive columns
df_cleaned = df_cleaned.drop_duplicates(subset=['Name', 'Age', 'Country', 'Salary'], keep='first')

# --- 3. CORRELATION ANALYSIS (PEARSON) ---
# Select only numeric columns for correlation
numeric_cols = ['ID', 'Age', 'Salary']
numeric_df = df_cleaned[numeric_cols]

plt.figure(figsize=(8, 6))
correlation_matrix = numeric_df.corr(method='pearson')
sns.heatmap(correlation_matrix, annot=True, cmap='RdBu_r', center=0, fmt='.2f')
plt.title('Pearson Correlation Heatmap (Cleaned Data)')
plt.savefig('combined_correlation_heatmap.png')
plt.show()

# --- 4. OUTLIER DETECTION (IQR METHOD) ---
outliers_report = {}
for col in numeric_cols:
    Q1 = numeric_df[col].quantile(0.25)
    Q3 = numeric_df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    count = ((numeric_df[col] < lower_bound) | (numeric_df[col] > upper_bound)).sum()
    outliers_report[col] = count

print("\n--- Outlier Count (IQR Method) ---")
print(outliers_report)

print("\n--- Descriptive Statistics (Cleaned Data) ---")
print(numeric_df.describe())