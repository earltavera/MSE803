# World Happiness SQL Analysis

This repository contains SQL queries used to aggregate and analyze the World Happiness Dataset. The analysis is divided into two main parts: GDP categorization and Corruption Perception impact.

## Part 1: GDP Categorization, Happiness Averages, and Rankings

**Objective:** Group countries into High, Medium, and Low GDP per capita brackets, calculate the average happiness score for each bracket, and assign a happiness rank to every country within its specific category.

### SQL Query
```sql
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
    Rank_in_Category;
