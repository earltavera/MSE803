# Define the README content based on the user's specific script and dataset requirements
readme_v3 = """# Beijing Multi-Site Air Quality Analysis

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

Dataset Link: Beijing Multi-Site Air Quality Data

Unzip the folder so the CSV files are accessible.

###3. Update the Script Path
Open Week2A2.py and update the path variable to point to the folder where you unzipped the CSVs:
