import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
sns.set_theme(style="whitegrid")

# Create a figure with two subplots
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Total Sales per Category
# Added hue='category' and legend=False to fix the warning
sns.barplot(x='category', y='sales_sum', data=df, ax=ax[0], hue='category', palette='viridis', legend=False)
ax[0].set_title('Total Sales by Category', fontsize=14)
ax[0].set_ylabel('Sum of Sales ($)')

# Plot 2: Total Quantity per Category
# Added hue='category' and legend=False to fix the warning
sns.barplot(x='category', y='quantity_sum', data=df, ax=ax[1], hue='category', palette='magma', legend=False)
ax[1].set_title('Total Quantity Sold by Category', fontsize=14)
ax[1].set_ylabel('Sum of Quantity')

plt.tight_layout()
plt.show() 
