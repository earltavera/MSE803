Beijing Multi-Site Air Quality Analysis
MSE803 - Week 2 Activity 2

This project performs a comprehensive exploratory data analysis (EDA) on hourly air quality data from multiple monitoring sites in Beijing.

📊 About the Data
The dataset captures environmental conditions from March 2013 to February 2017. Each row represents an hourly measurement including:

Pollution Levels: PM2.5, PM10, SO2, NO2, CO, O3
Weather Data: Temperature (TEMP), Pressure (PRES), Dew Point (DEWP)
Rainfall: Precipitation (RAIN)
Wind Information: Wind Direction (wd) and Wind Speed (WSPM)
Station: The name of the monitoring site

This repository contains a Python-based data pipeline for analyzing hourly air quality data from 12 monitoring sites in Beijing. The script, `Week2A2.py`, automates the transition from raw data collection to statistical insight and visualization.

## 📖 Project Overview
This script is designed to process the **Beijing Multi-Site Air Quality Data Set**. It performs high-level data wrangling to help researchers understand the relationship between environmental factors (like temperature and wind) and harmful pollutants (like PM2.5).

### How the Script Handles Data:
1.  **Consolidation:** It uses the `glob` library to find all 12 CSV files in a directory and merges them into a single unified dataset containing hundreds of thousands of records.
2.  **Cleaning (Handling Missing Data):** Air quality sensors often have "gaps." The script uses **Forward Filling (`ffill`)**, which carries the previous hour's reading into the missing slot. This preserves the time-series flow without deleting valuable context.
3.  **Feature Engineering:** It converts four separate columns (`year`, `month`, `day`, `hour`) into a single `datetime` object, enabling the script to treat the data as a continuous timeline.
4.  **Statistical Analysis:** It calculates **Pearson Correlation Coefficients** to mathematically prove which weather conditions (e.g., wind speed) are most effective at reducing pollution.

## 🚀 How to Run the Project

### 1. Requirements
You will need Python 3.x installed along with these libraries:
### 2. The Dataset
Download the official dataset from the UCI Machine Learning Repository:

Dataset Link: [Beijing Multi-Site Air Quality Data](https://archive.ics.uci.edu/dataset/501/beijing+multi+site+air+quality+data)

Unzip the folder so the CSV files are accessible.

### 3. Update the Script Path
Open Week2A2.py and update the path variable to point to the folder where you unzipped the CSVs:
path = r'/Your/Local/Folder/Path'

### 4. Execute
Run the script through your terminal or IDE:
python Week2A2.py

📊 Visualizations & Output
The script generates two primary visual insights:

Time-Series Trend: A line graph showing how PM2.5 levels fluctuate hourly at a specific station.

Correlation Heatmap: A visual matrix that identifies strong relationships (e.g., how PM2.5 moves in tandem with CO or inverse to Wind Speed).

🔗 Script Location
The source code for this analysis can be found here:
[Week2A2.py](https://github.com/earltavera/MSE803/blob/main/Week2A2/Week2A2.py)


