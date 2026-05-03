# World Happiness Data Analysis

This project provides an analysis of the `world_happiness_dataset.csv` file, focusing on data cleaning, outlier detection, and visualization to uncover insights into global happiness drivers.

## 1. Data Cleaning and Preparation

To ensure the quality of the analysis, a comprehensive audit and cleaning process was performed on the raw data.

### Initial Audit
- **Total Records:** 20 rows
- **Total Features:** 8 columns

### Cleaning Process
- **Missing Values & Duplicates:** A thorough check revealed no missing values or duplicate entries within the dataset.
- **Outlier Detection:** The Interquartile Range (IQR) method was employed to identify potential anomalies. Any value falling outside $1.5 \times$ the IQR from the first and third quartiles was considered an outlier.
- **Result:** No statistical outliers were detected across any of the features, ensuring a robust and consistent dataset for analysis.

### Cleaning Summary
| Step | Count |
| :--- | :--- |
| Initial Load | 20 |
| After Dropping Nulls/Dupes | 20 |
| Outliers Removed | 0 |
| **Final Dataset** | **20** |

## 2. Visualization Insights

The study utilized visual tools to interpret the complex relationships between socioeconomic factors and happiness scores.

### Correlation Analysis (Pearson Heatmap)
A Pearson correlation heatmap was generated to measure the linear relationships between features:
- **Corruption and Social Support:** Observed a moderate positive correlation (**0.41**).
- **Generosity and Freedom:** Revealed a strong negative correlation (**-0.56**), indicating these factors often move in opposite directions in this sample.
- **Corruption and Happiness:** A negative correlation (**-0.34**) suggests that higher perceived corruption typically aligns with lower happiness scores.
- **GDP and Happiness:** Surprisingly, GDP per Capita showed almost no linear correlation (**0.01**) with the overall Happiness Score for this specific subset.

### Distribution and Outlier Identification (Boxplots)
Boxplots were used to confirm data spread and validate the outlier audit:
- **Healthy Life Expectancy:** This feature exhibited the widest range, with values spanning from approximately **41 to 81 years**.
- **Consistency:** The visual "whiskers" of the boxplots confirmed that all data points reside within acceptable statistical ranges.

## Summary of Findings

The analysis reveals a highly consistent dataset free from anomalies. In this 20-country sample, the primary drivers of happiness appear more closely linked to **social factors**—such as perceptions of freedom and corruption—than to purely economic indicators like GDP.
