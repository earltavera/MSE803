# Retail Sales Performance Dashboard 📊

**Project**: Week 5 Assignment 2

## Overview
This repository contains a Power BI dashboard (`Week5A2.pbix`) designed to analyze and visualize retail sales data. It provides interactive insights into total sales volume, profitability, product category performance, and customer segmentation.

## Dataset
The data model is built upon the `Retail_Sales_sample-Dataset.csv` file. 

**Key Data Points Analyzed:**
* **Order Details**: Date, Quantity Sold
* **Product Info**: Category (Electronics, Furniture, Clothing), Product Name
* **Financials**: Sales Amount, Discount (%), Profit
* **Customer Demographics**: Region, Customer Segment (Consumer, Corporate, Home Office)
  
* The dashboard is designed to guide the viewer from high-level summaries down to specific segment breakdowns.

KPI (Key Performance Indicator) Cards: These are the large numbers at the top of the report. They provide an immediate "pulse check" on the business. We track Total Sales, Total Profit, Total Quantity Sold, and Average Profit Margin. This prevents the viewer from having to do mental math.

Bar Chart (Total Sales by Category): This vertical bar chart compares the three main product lines side-by-side. Bar charts are the best visual tool for comparing distinct categories because the human eye can easily judge the differences in bar height to determine which category is performing best.

Pie Chart (Sales by Customer Segment): This visual shows how your total revenue is divided among different types of buyers. A pie chart is used here because it perfectly illustrates "parts of a whole" (how the 100% of your sales are split).

## Key Features
* **Executive KPI Summary**: High-level tracking of total revenue and profit margins.
* **Category Breakdown**: Comparative analysis of how different product lines perform.
* **Segment Insights**: Visualizations showing which customer segments drive the most value.
* **Regional Tracking**: Breakdown of sales across different geographic regions.

## How to View (macOS / Cloud Users)
Because Power BI Desktop does not have a native macOS application, this `.pbix` file is best viewed using the cloud-based Power BI Service:

1. Navigate to [app.powerbi.com](https://app.powerbi.com/) and log in with your Microsoft 365 credentials.
2. Go to **My Workspace** (or your designated shared workspace).
3. Click **Upload** -> **Browse** and select the `Week5A2.pbix` file.
4. Once the upload completes, click on the report to interact with the dashboard.

## Repository Structure
* `Week5A2.pbix`: The core Power BI report and data model.
* `Retail_Sales_sample-Dataset.csv`: The raw dataset used to populate the visuals.

## Technologies
* **Power BI** (Data Visualization & Reporting)
* **Power Query** (Data Transformation & Cleaning)
