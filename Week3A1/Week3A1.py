import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# Load the dataset
file_path = '/Users/earltavera/Desktop/MSE803/Week 3/age_networth.csv'
df = pd.read_csv(file_path)

# Display the first few rows and info to understand the structure
print(df.head())
print(df.info())


# Calculate the correlation coefficient
correlation = df['Age'].corr(df['Net Worth'])
print(f"Correlation Coefficient: {correlation}")

# Visualize the relationship with a scatter plot and regression line
plt.figure(figsize=(10, 6))
sns.regplot(x='Age', y='Net Worth', data=df, scatter_kws={'s': 100}, line_kws={'color': 'red'})
plt.title(f'Relationship between Age and Net Worth (Correlation: {correlation:.4f})')
plt.xlabel('Age')
plt.ylabel('Net Worth ($)')
plt.grid(True)
plt.savefig('correlation_plot.png')


#Analysis Results
#Correlation Coefficient: Approximately 0.8824.
#Interpretation: A value of 0.8824 indicates a strong positive linear relationship. This suggests that as age increases, net worth generally tends to increase significantly as well.
#Observations: The scatter plot shows that while the trend is strongly upward, there are minor fluctuations (e.g., the dip at age 50 and the peak at age 75 followed by a lower value at 85), which is common in real-world financial data.

# 1. Load the data
# Assuming the file is named 'age_networth.csv'
df = pd.read_csv('age_networth.csv')

# 2. Calculate the Pearson Correlation Coefficient
correlation = df['Age'].corr(df['Net Worth'])
print(f"The Pearson Correlation Coefficient is: {correlation:.4f}")

# 3. Visualize the relationship
plt.figure(figsize=(10, 6))
# Create a scatter plot with a regression line
sns.regplot(x='Age', y='Net Worth', data=df, 
            scatter_kws={'s': 100, 'alpha': 0.7, 'color': 'blue'}, 
            line_kws={'color': 'red', 'label': f'Regression Line (r={correlation:.2f})'})

# Adding labels and title
plt.title('Analysis of Age vs. Net Worth', fontsize=15)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Net Worth ($)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Save and show results
plt.savefig('correlation_analysis.png')
plt.show()

#Outcome Explanation
#Direction: The positive sign of the correlation (0.8824) means the variables move in the same direction.
#Strength: The magnitude (closer to 1.0 than to 0.5) confirms that age is a very strong predictor of net worth within this specific group of data.
#Visualization: The red regression line in the plot represents the "line of best fit." The closer the blue data points are to this line, the higher the correlation. In this case, most points cluster tightly around the line, illustrating the strong predictive power of the model.
#The Pearson Correlation Coefficient scale ranges from -1 to 1, where 1 is a perfect positive correlation, 0 is no correlation, and -1 is a perfect negative correlation. Our result of 0.8824 falls in the "Strong" category.