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