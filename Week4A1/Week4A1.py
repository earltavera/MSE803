import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'world_happiness_dataset.csv'
df = pd.read_csv(file_path)

# 1. Basic Audit
initial_shape = df.shape
initial_missing = df.isnull().sum().sum()
initial_dupes = df.duplicated().sum()

# 2. Data Cleaning
# Handle missing values and duplicates
df_cleaned = df.dropna().drop_duplicates()

# 3. Outlier Detection & Removal (IQR Method)
numeric_df = df_cleaned.select_dtypes(include=[np.number])
outliers_detected = {}
all_outlier_indices = set()

for col in numeric_df.columns:
    Q1 = numeric_df[col].quantile(0.25)
    Q3 = numeric_df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outlier_mask = (numeric_df[col] < lower_bound) | (numeric_df[col] > upper_bound)
    outlier_count = outlier_mask.sum()
    outliers_detected[col] = outlier_count
    all_outlier_indices.update(numeric_df[outlier_mask].index)

# Remove outliers for final analysis
df_final = df_cleaned.drop(index=list(all_outlier_indices))
numeric_final = df_final.select_dtypes(include=[np.number])

# 4. Data Visualization
# Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_final.corr(method='pearson'), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Pearson Correlation Heatmap: Happiness Drivers (Post-Cleaning)')
plt.savefig('correlation_viz.png')
plt.close()

# Boxplots for Outlier Identification (using pre-outlier removal data to show them)
plt.figure(figsize=(12, 6))
sns.boxplot(data=numeric_df, orient='h', palette='Set2')
plt.title('Distribution and Outlier Identification (Pre-Removal)')
plt.savefig('boxplot_viz.png')
plt.close()

# Summary Tables
cleaning_summary = pd.DataFrame({
    "Step": ["Initial Load", "After Dropping Nulls/Dupes", "Outliers Removed", "Final Dataset"],
    "Count": [initial_shape[0], df_cleaned.shape[0], len(all_outlier_indices), df_final.shape[0]]
})

outliers_table = pd.Series(outliers_detected).reset_index()
outliers_table.columns = ['Feature', 'Outlier Count']

print("CLEANING_SUMMARY")
print(cleaning_summary.to_markdown(index=False))
print("\nOUTLIERS_BY_FEATURE")
print(outliers_table.to_markdown(index=False))


import os

# Check for the correct filename in the current directory
files = os.listdir('.')
print(f"Files in directory: {files}")
