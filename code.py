import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# FIX: Use read_excel instead of read_csv for .xlsx files
file_path = '/Users/earltavera/Desktop/MSE803/Data_set_w1A1.xlsx'
df = pd.read_excel(file_path)

# Proceed with the rest of your code
print(df.head())

# 2. Descriptive Analysis / Aggregation
# Since the file you shared earlier was already aggregated, 
# you can proceed directly to visualization or further summary.
summary = df.describe()
print(summary)
