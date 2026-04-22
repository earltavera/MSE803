# Beijing Multi-Site Air Quality Analysis
MSE803 - Week 2 Activity 2

This project provides a data processing and analysis pipeline for hourly air quality data across 12 monitoring sites in Beijing. The script automates the merging of large datasets, performs essential data cleaning, and generates statistical insights into air pollution patterns.

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
## 📖 What This Script Does
The script handles the transition from raw, fragmented CSV data to a cleaned, visualized dataset. It is divided into six logical tasks:
1.  **Consolidation:** Merges 12 separate station files into one master DataFrame.
2.  **Structural Audit:** Checks the dimensions and data types of the combined data.
3.  **Data Cleaning:** Fixes missing values and prepares time-series data for analysis.
4.  **Dynamic Station Ranking:** Calculates the worst overall air quality and ranks all stations.
5.  **Visualization:** Generates line plots to track pollution trends over time.
6.  **Correlation Analysis:** Investigates how weather (temperature, wind) affects pollution levels (PM2.5).

## 🛠️ Data Handling Process
Air quality data is often "noisy" or incomplete due to sensor failures. This script handles data using the following logic:

* **Forward Filling (`ffill`):** Instead of deleting rows with missing data (which breaks the timeline), the script carries the last known valid reading forward. This is a standard practice for hourly environmental monitoring.
* **Datetime Engineering:** It converts four separate integer columns (`year`, `month`, `day`, `hour`) into a single `datetime` object. This allows the computer to understand the linear progression of time for more accurate plotting.
* **Targeting the Worst Pollution:** Instead of randomly selecting a station, the script uses `.groupby()` to calculate the 4-year PM2.5 average for all locations, automatically targeting the most polluted station for the final visualizations.

## 🚀 How to Run the Script

### 1. Prerequisites
Ensure you have Python installed along with the necessary data science libraries:
```bash
pip install pandas matplotlib seaborn

## 🚀 How to Run the Project

### 1. Requirements
You will need Python 3.x installed along with these libraries:
### 2. The Dataset
Download the official dataset from the UCI Machine Learning Repository:

Dataset Link: [[Beijing Multi-Site Air Quality Data](https://archive.ics.uci.edu/dataset/501/beijing+multi+site+air+quality+data)
Unzip the folder so the CSV files are accessible.

### 3. Update the Script Path
Open Week2A2.py and update the path variable to point to the folder where you unzipped the CSVs:
path = r'/Your/Local/Folder/Path'

### 4. Execute
Run the script through your terminal or IDE:
python Week2A2.py


🔗 Script Location
The source code for this analysis can be found here:
[Week2A2.py](https://github.com/earltavera/MSE803/blob/main/Week2A2/Week2A2.py)


