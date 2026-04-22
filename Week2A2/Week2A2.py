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

# 3. Data Cleaning
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

# --- 4. Data Filtering by Station ---
print("\n--- Task 4: Identifying the Worst Air Quality Station ---")

# 1. Group the data by station and calculate the mean PM2.5
# We use sort_values(ascending=False) to put the worst station at the very top
station_pm25_means = df.groupby('station')['PM2.5'].mean().sort_values(ascending=False)

# 2. Extract the worst station (which is now the first one in our sorted list)
target_station = station_pm25_means.index[0]
worst_pm25_avg = station_pm25_means.iloc[0]

print("Ranking of Stations by Average PM2.5 (Worst to Best):")
for i, (station, avg_pm25) in enumerate(station_pm25_means.items(), 1):
    print(f"{i}. {station}: {avg_pm25:.2f}")

print(f"\nTargeting Data for: {target_station}")
print(f"Reason: Highest overall PM2.5 average ({worst_pm25_avg:.2f})")

# 3. Filter the dataset for that specific station
df_filtered = df[df['station'] == target_station]

# 4. VISUAL DISPLAY: Bar Chart Ranking
plt.figure(figsize=(10, 6))
# Using a Red color palette where the darkest red is the worst pollution
sns.barplot(x=station_pm25_means.values, y=station_pm25_means.index, hue=station_pm25_means.index, palette='Reds_r', legend=False)
plt.title("Average PM2.5 Concentration by Station (2013-2017)")
plt.xlabel("Average PM2.5")
plt.ylabel("Monitoring Station")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 5. Data Visualization
print("\n--- Task 5: Generating Visualization ---")
plt.figure(figsize=(12, 6))
# Plotting a subset (first 500 hours) using 'datetime' for a continuous timeline
sns.lineplot(data=df_filtered.iloc[:500], x='datetime', y='PM2.5', color='#e74c3c')
plt.title(f'Hourly PM2.5 Trends at {target_station} (First 500 Hours)')
plt.xticks(rotation=45) # Rotates the dates so they don't overlap
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
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
