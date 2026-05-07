import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/earltavera/Desktop/MSE803/Week 4/Week4A1/Week4A2/world_happiness_dataset.csv')
conn = sqlite3.connect(':memory:')
df.to_sql('happiness', conn, index=False)

query1 = """
WITH CategorizedData AS (
    SELECT 
        Country, 
        Happiness_Score,
        GDP_per_Capita,
        CASE 
            WHEN GDP_per_Capita >= 1.39 THEN 'High'
            WHEN GDP_per_Capita >= 0.90 THEN 'Medium'
            ELSE 'Low'
        END AS GDP_Category
    FROM happiness
)
SELECT 
    Country,
    GDP_Category,
    Happiness_Score,
    ROUND(AVG(Happiness_Score) OVER (PARTITION BY GDP_Category), 2) AS Category_Avg_Happiness,
    RANK() OVER (PARTITION BY GDP_Category ORDER BY Happiness_Score DESC) AS Rank_in_Category
FROM CategorizedData
ORDER BY 
    CASE GDP_Category 
        WHEN 'High' THEN 1 
        WHEN 'Medium' THEN 2 
        WHEN 'Low' THEN 3 
    END, 
    Rank_in_Category
LIMIT 20;
"""

query2 = """
SELECT 
    Corruption_Level,
    COUNT(*) as Country_Count,
    ROUND(AVG(Happiness_Score), 2) AS Avg_Happiness,
    ROUND(AVG(GDP_per_Capita), 2) AS Avg_GDP,
    ROUND(AVG(Healthy_Life_Expectancy), 2) AS Avg_Life_Expectancy
FROM (
    SELECT 
        Happiness_Score, 
        GDP_per_Capita, 
        Healthy_Life_Expectancy,
        CASE 
            WHEN Perceptions_of_Corruption >= (SELECT AVG(Perceptions_of_Corruption) FROM happiness) 
            THEN 'Above Avg Corruption Perception'
            ELSE 'Below Avg Corruption Perception'
        END AS Corruption_Level
    FROM happiness
) AS sub
GROUP BY Corruption_Level;
"""

df1 = pd.read_sql_query(query1, conn)
df2 = pd.read_sql_query(query2, conn)

def save_df_as_image(df, filename):
    fig, ax = plt.subplots(figsize=(10, len(df)*0.4 + 1))
    ax.axis('tight')
    ax.axis('off')
    the_table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(10)
    the_table.scale(1.2, 1.2)
    
    # Header color
    for (row, col), cell in the_table.get_celld().items():
        if row == 0:
            cell.set_text_props(weight='bold', color='white')
            cell.set_facecolor('#4c72b0')
        else:
            cell.set_facecolor('#f2f2f2' if row % 2 == 0 else '#ffffff')
            
    plt.savefig(filename, bbox_inches='tight', dpi=150)
    plt.close()

save_df_as_image(df1, 'query1_results.png')
save_df_as_image(df2, 'query2_results.png')