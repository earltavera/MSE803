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

Logic and Explanation
Common Table Expression (CTE) - WITH CategorizedData AS (...): Acts as a temporary table. Cut-off points for 'High', 'Medium', and 'Low' categories are determined using the 75th percentile (1.39) and the 25th percentile (0.90) of the GDP_per_Capita values via a CASE statement.

Window Function for Average - AVG(...) OVER(...): The OVER (PARTITION BY GDP_Category) clause calculates the average happiness strictly for each category while keeping individual country rows intact.

Window Function for Ranking - RANK(...) OVER(...): Sorts the countries by Happiness_Score in descending order, but restarts the ranking sequence at 1 for every new GDP category.

Sorting Output: The ORDER BY statement ensures the final view organizes countries by High, then Medium, then Low, and sorts them by rank within those buckets.

Part 2: Corruption Perception Impact Analysis
Objective: Use a subquery to evaluate if a country is perceived to have high or low corruption relative to the global average, and then compare how these groups perform on multiple metrics.

SQL Query
SQL
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
) AS SubQuery
GROUP BY Corruption_Level;
Logic and Explanation
The Dynamic Subquery: (SELECT AVG(Perceptions_of_Corruption) FROM happiness) dynamically fetches the exact mean of corruption perception across the entire dataset.

The Inner Query: Takes every row, compares its corruption perception against the global average, and labels it as 'Above Avg Corruption Perception' or 'Below Avg Corruption Perception' using a CASE statement.

Outer Aggregation: Gathers the newly labeled rows and applies a GROUP BY Corruption_Level.

Calculations: Uses COUNT() to see how many countries fall into each bucket, alongside AVG() measurements (rounded to 2 decimal places) to compare Happiness, GDP, and Life Expectancy.
