import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
# Update the path as needed for your local environment
file_path = '/Users/earltavera/Desktop/MSE803/Week 1 A2/Housing.csv'
df = pd.read_csv(file_path)

# --- NEW: Check for Missing Data ---
print("--- Data Integrity Check ---")
missing_values = df.isnull().sum()
if missing_values.sum() == 0:
    print("Success: No missing data found in the dataset.\n")
else:
    print("Warning: Missing values detected:")
    print(missing_values[missing_values > 0])
    print("\n")

# Set a professional visual style
sns.set_theme(style="whitegrid")

# --- CHART 1: Area vs Price (For Slide 2) ---
plt.figure(figsize=(10, 6))
sns.scatterplot(x='area', y='price', data=df, alpha=0.6, color='teal')
plt.title('Relationship Between Land Area and House Price', fontsize=14)
plt.xlabel('Area (sq. ft)')
plt.ylabel('Price')
plt.savefig('chart_area_vs_price.png')
print("Chart 1 saved.")

# --- CHART 2: AC & Furnishing Impact (For Slide 3) ---
plt.figure(figsize=(10, 6))
# Using hue to show the interaction between furnishing and AC
sns.barplot(x='furnishingstatus', y='price', hue='airconditioning', data=df, palette='viridis')
plt.title('Price Premium: AC vs. Furnishing Status', fontsize=14)
plt.ylabel('Average Price')
plt.savefig('chart_ac_furnishing.png')
print("Chart 2 saved.")

# --- CHART 3: Preferred Area Impact (For Slide 4) ---
plt.figure(figsize=(10, 6))
# Setting hue=x to avoid warnings and removing redundant legend
sns.barplot(x='prefarea', y='price', hue='prefarea', data=df, palette='magma', legend=False)
plt.title('Location Value: Preferred vs. Non-Preferred Areas', fontsize=14)
plt.ylabel('Average Price')
plt.savefig('chart_location_premium.png')
print("Chart 3 saved.")

plt.show()
