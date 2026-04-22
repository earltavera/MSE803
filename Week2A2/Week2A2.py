import pandas as pd
import glob
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Path to the dataset
path = r'/Users/earltavera/Desktop/MSE803/Week 2/Week2A1/beijing+multi+site+air+quality+data/PRSA_Data_20130301-20170228'

# 1. Load the dataset
all_files = glob.glob(os.path.join(path, "*.csv"))
df_list = [pd.read_csv(f) for f in all_files]
df = pd.concat(df_list, ignore_index=True)

# 2. Basic Inspection
print("--- Dataset Dimensions ---")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# 3 Data Cleaning
print("\n--- Task 3: Data Cleaning ---")

# Checking for missing values
missing_values = df.isnull().sum()
print("Missing values per column:\n", missing_values[missing_values > 0])

# Handling Missing Values
# I used 'forward fill' (ffill) because air quality data is a time series. 
# If a sensor fails for one hour, it's likely the air is similar to the hour before.
df = df.ffill()

# Converting Date Components to Datetime
# This makes (Visualization) much easier.
df['datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])

# Drop unnecessary columns (optional, like 'No' which is just a row ID)
df.drop(columns=['No'], inplace=True)

print(f"Cleaned Dimensions: {df.shape}")
print("Data Cleaning Complete.")

# 4. Data Filtering by Station
print("\n--- Task 4: Available Stations ---")
stations = df['station'].unique()
for i, station in enumerate(stations, 1):
    print(f"{i}. {station}")

# Selecting a station (e.g., the first one in the list)
target_station = stations[0] 
df_filtered = df[df['station'] == target_station]
print(f"\nSuccessfully filtered data for: {target_station} ({len(df_filtered)} records)")

# 5. Data Visualization
print("\n--- Task 5: Generating Visualization ---")
plt.figure(figsize=(12, 6))
# Plotting a subset (first 500 hours) for clarity
sns.lineplot(data=df_filtered.iloc[:500], x='hour', y='PM2.5', hue='month', palette='viridis')
plt.title(f'Hourly PM2.5 Trends at {target_station} (Sample)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# 6. Correlation Analysis
print("\n--- Task 6: Correlation Analysis ---")
# Selecting only numeric columns and dropping NaNs for the calculation
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
corr_matrix = df[numeric_cols].corr()

# Focusing on PM2.5 correlations
print("\nCorrelation of PM2.5 with other variables:")
print(corr_matrix['PM2.5'].sort_values(ascending=False))

# Heatmap Visualization
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=False, cmap='RdBu_r', center=0)
plt.title('Global Feature Correlation Heatmap')
plt.show()