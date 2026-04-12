import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Use read_excelfor .xlsx filesn for the exact location
file_path = '/Users/earltavera/Desktop/MSE803/Data_set_w1A1.xlsx'
df = pd.read_excel(file_path)

print(df.head())

# 2. Descriptive Analysis / Aggregation
# Since the file was already aggregated, 
# we can proceed to visualization or further summary.
summary = df.describe()
print(summary)
