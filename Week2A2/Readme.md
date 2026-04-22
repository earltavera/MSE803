Beijing Multi-Site Air Quality Analysis
This repository contains a comprehensive Exploratory Data Analysis (EDA) and data processing pipeline for the Beijing Multi-Site Air Quality Dataset. The project involves merging disparate data sources, cleaning time-series gaps, and analyzing the relationship between various air pollutants and meteorological factors.

🚀 Project Workflow
1. Data Integration
Source: 12 hourly air-quality monitoring sites in Beijing.

Action: Dynamically merges multiple CSV files into a single unified Pandas DataFrame for global analysis.

2. Data Cleaning & Preprocessing
To ensure high-quality analysis, the following cleaning steps were performed:

Missing Value Imputation: Utilized Forward Fill (ffill). In time-series air quality data, a sensor failure for an hour is best represented by the previous hour's reading to maintain continuity.

Temporal Conversion: Converted separate year, month, day, and hour columns into a single datetime object for advanced time-series plotting.

Feature Selection: Dropped redundant columns (e.g., No row ID) to streamline the dataset.

3. Station-Specific Filtering
The script dynamically identifies all unique monitoring stations (e.g., Aotizhongxin, Dongsi, Wanshouxigong).

Allows for targeted filtering to isolate trends in specific geographic locations.

4. Data Visualization
Implemented using Seaborn and Matplotlib.

Visualizes hourly trends of PM2.5 levels to identify peak pollution times and seasonal shifts.

5. Correlation Analysis
Identifies the statistical relationship between pollutants and weather variables.

Focus on PM2.5: Analyzes how variables like Temperature, Pressure, and Wind Speed correlate with fine particulate matter.

Includes a Correlation Heatmap for a visual overview of how all numeric features interact.
