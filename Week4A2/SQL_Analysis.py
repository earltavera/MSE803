import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('/Users/earltavera/Desktop/MSE803/Week 4/Week4A1/Week4A2/world_happiness_dataset.csv')

# Create SQLite DB
conn = sqlite3.connect(':memory:')
df.to_sql('happiness', conn, index=False)

# Analyze GDP to set thresholds
gdp_min = df['GDP_per_Capita'].min()
gdp_max = df['GDP_per_Capita'].max()
gdp_mean = df['GDP_per_Capita'].mean()
gdp_q3 = df['GDP_per_Capita'].quantile(0.75)
gdp_q1 = df['GDP_per_Capita'].quantile(0.25)

print(f"GDP Min: {gdp_min}, Max: {gdp_max}, Mean: {gdp_mean}, Q1: {gdp_q1}, Q3: {gdp_q3}")