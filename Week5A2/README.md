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

## Key Features
* **Executive KPI Summary**: High-level tracking of total revenue and profit margins.
* **Category Breakdown**: Comparative analysis of how different product lines perform.
* **Segment Insights**: Visualizations showing which customer segments drive the most value.
* **Regional Tracking**: Breakdown of sales across different geographic regions.

## The dashboard is designed to guide the viewer from high-level summaries down to specific segment breakdowns.

* **KPI (Key Performance Indicator) Cards: These are the large numbers at the top of the report. They provide an immediate "pulse check" on the business. We track Total Sales, Total Profit, Total Quantity Sold, and Average Profit Margin. This prevents the viewer from having to do mental math.

* **Bar Chart (Total Sales by Category): This vertical bar chart compares the three main product lines side-by-side. Bar charts are the best visual tool for comparing distinct categories because the human eye can easily judge the differences in bar height to determine which category is performing best.

* **Pie Chart (Sales by Customer Segment): This visual shows how your total revenue is divided among different types of buyers. A pie chart is used here because it perfectly illustrates "parts of a whole" (how the 100% of your sales are split).

## The Full Insights (What the Data is Telling Us)
After analyzing your underlying dataset, here are the exact insights your dashboard reveals:

1. Executive Summary (The Big Picture)
Your retail operation is healthy and profitable.

Total Revenue: The store generated $50,967.84 in total sales.

Total Profit: From those sales, the business took home $8,557.71 in pure profit.

Volume: A total of 568 items were sold.

Profit Margin: Your average profit margin sits at an excellent 16.79%, meaning for every $100 in sales, the company keeps roughly $16.79 in profit after costs.

2. Product Category Performance
Not all product lines are contributing equally.

Top Performer: Clothing is your biggest revenue driver, bringing in $21,557.56 (over 42% of all sales).

Strong Second: Electronics follows closely behind with $19,395.59.

Weak Link: Furniture is lagging significantly, bringing in only $10,014.69. This indicates that furniture either has lower demand, or the inventory isn't moving as fast as clothing and tech.

3. Customer Segmentation
Understanding who is buying is just as important as knowing what they are buying.

Everyday Consumers are the backbone of your business, generating the lion's share of revenue at $22,438.96.

Home Office buyers make up the middle tier, spending $15,432.36.

Corporate clients are currently your lowest spending segment at $13,096.52.

4. Regional Footprint
Your sales map shows a clear divide between the West/North and the East/South.

The Powerhouses: The West ($16,362 in sales / $2,894 profit) and the North ($15,668 in sales / $2,643 profit) are your most lucrative territories by far.

Underperforming Areas: The East ($9,883 in sales) and South ($9,053 in sales) are generating roughly half the volume of your top regions. The South is the weakest link, bringing in the lowest sales and the lowest profit ($1,350).

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
