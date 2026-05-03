import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Load the dataset
file_path = 'world_happiness_dataset.csv'
df = pd.read_csv(file_path)

# Display state before cleaning
before_cleaning = {
    "head": df.head(),
    "shape": df.shape,
    "missing_values": df.isnull().sum().sum(),
    "duplicates": df.duplicated().sum()
}

# Perform cleaning (Deduplication and dropping non-numeric for specific analysis)
df_clean = df.drop_duplicates()
# For the purpose of the user's specific request, we focus on numeric cleaning 
# but keep the dataframe structure for the "after" display.
df_after = df_clean.copy()

# Display state after cleaning
after_cleaning = {
    "head": df_after.head(),
    "shape": df_after.shape,
    "missing_values": df_after.isnull().sum().sum(),
    "duplicates": df_after.duplicated().sum()
}

print("--- BEFORE CLEANING ---")
print(f"Shape: {before_cleaning['shape']}")
print(f"Total Missing Values: {before_cleaning['missing_values']}")
print(f"Duplicate Rows: {before_cleaning['duplicates']}")
print(before_cleaning['head'])

print("\n--- AFTER CLEANING ---")
print(f"Shape: {after_cleaning['shape']}")
print(f"Total Missing Values: {after_cleaning['missing_values']}")
print(f"Duplicate Rows: {after_cleaning['duplicates']}")
print(after_cleaning['head'])


# Load the dataset
df = pd.read_csv('world_happiness_dataset.csv')

# --- DATA CLEANING & PREP ---
# Drop any potential duplicates and non-numeric columns for correlation
df_clean = df.drop_duplicates()
numeric_cols = df_clean.select_dtypes(include=[np.number])

# --- VISUALIZATION: CORRELATION HEATMAP ---
plt.figure(figsize=(10, 8))
# Using Pearson algorithm for linear correlation
correlation_matrix = numeric_cols.corr(method='pearson')
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Pearson Correlation Heatmap: Happiness Drivers')
plt.show()

# --- OUTLIER DETECTION: BOXPLOTS ---
plt.figure(figsize=(12, 6))
sns.boxplot(data=numeric_cols, orient='h', palette='Set2')
plt.title('Distribution and Outlier Identification')
plt.show()

# --- OUTLIER CALCULATION (IQR Method) ---
for col in numeric_cols.columns:
    Q1 = numeric_cols[col].quantile(0.25)
    Q3 = numeric_cols[col].quantile(0.75)
    IQR = Q3 - Q1
    outliers = numeric_cols[(numeric_cols[col] < (Q1 - 1.5 * IQR)) | (numeric_cols[col] > (Q3 + 1.5 * IQR))]
    print(f"Outliers in {col}: {len(outliers)}")