# Customer Shopping Behavior Analysis for Retail Growth

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-green.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

---

## 📋 Project Overview

This project analyzes customer shopping behavior to identify patterns in purchasing trends, customer demographics, product performance, and seasonal sales. The goal is to generate actionable insights that can help businesses improve marketing strategies, customer retention, and product planning.
The project includes a complete data analytics workflow, starting from raw data processing to business intelligence dashboard creation.

---

## 🎯 Key stages of the project include:
  ✅ Data cleaning and preprocessing 
  ✅ Feature engineering 
 - ✅ Automated data pipeline using Python  
✅ SQL analysis for business insights 
✅ Exploratory Data Analysis (EDA)
✅ Interactive dashboard development using Power BI

---
## 🎯 Project Objectives 
### The primary objectives of this project are:
 - Understand **customer purchasing behavior**
 - Identify **top performing product categories**
 - Analyze **customer segments and loyalty**
 - Evaluate **seasonal sales trends**
 - Measure the impact of **promotions and discounts**
 - Build a **business dashboard** for decision making


### 🛠 Tools & Technologies
The following tools and technologies were used in this project:
### Programming & Data Processing
 - Python
 - Pandas
 - Numpy
### Data Visualization
 - Matplotlib
 - Seaborn
 - Power BI
### Database
 - MySQL
### Development Environment
 - Jupyter Notebook
     
---

## 📁 Project Structure

```
customer-behavior-analysis/
│
├── data/
│ ├── raw/
│ │ └── customer_shopping_behavior.csv
│
├── notebooks/
│ ├── data_cleaning.ipynb
│ └── sql.ipynb
│
├── dashboard/
│ └── powerbi_dashboard.pbix
│
├── reports/
│ └── Project_Report.pdf
│
├── script/
│ ├── main.py
│
├── logs/
│ └── pipeline.log
|
├── images/
│ └── customer_analysis.png
│ └── executive_overview.png
│ └── product_promotion.png
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## 🔄 Data Pipeline Workflow
A Python-based **data pipeline** was developed to automate the data preparation process.

### Key Pipeline Features:
- ✅ Load raw dataset from CSV
- ✅ Clean and standardize column names
- ✅ Perform feature engineering
- ✅ Segment customers based on purchase history
- ✅ Store the cleaned dataset into a MySQL database
- ✅ Log pipeline execution for monitoring
### Pipeline technologies:
 - Python
 - Pandas
 - MYSQL
 - Logging
   
---

## 🧹 Data Cleaning
### Several preprocessing steps were applied to ensure data quality:
 - Standardized column names
 - Handled missing values using:
   - Median imputation for numeric columns
   - Mode imputation for categorical columns
 - Converted data types where necessary
 - Removed inconsistencies in categorical values
These steps ensure the dataset is analysis-ready.

## 🧠 Feature Engineering
Additional features were created to enhance analysis.
### Age Group
Customers were categorized into age groups:
| Age Range| Group |
|---------|-------|
| 0-25 | Young Adult | 
| 26-40 | Young |
| 41-60 |Middle Aged |
| 60+ | Senior |

### Customer Segmentation
Customers were segmented based on previous purchase behavior:
|Segment|	Criteria|
|-------|---------|
New|	1 purchase|
Returning|	2–10 purchases|
Loyal	|More than 10 purchases|

This segmentation helps analyze customer loyalty and revenue contribution.

## 📊 Exploratory Data Analysis (EDA)
Exploratory analysis was performed using Python and visualization libraries to identify patterns and trends.
### Key analyses included:
 - Revenue by product category
 - Revenue by customer gender
 - Customer segmentation analysis
 - Average purchase amount by age group
 - Seasonal sales trends
 - Promotion and discount impact
 - Purchase frequency patterns
 - Visualizations were created using Matplotlib and Seaborn.

---

## 🗃 SQL Analysis
SQL queries were written to perform additional analysis on the cleaned dataset stored in MySQL.
### Examples of SQL analysis include:
  - Top revenue generating products
  - Revenue by customer segment
  - Category performance analysis
  - City-wise revenue ranking
 - Purchase frequency analysis
SQL window functions and aggregations were used to derive insights.
```sql
-- Category Revenue Analysis
SELECT category, SUM(purchase_amount) AS total_revenue
FROM clean_customer_data
GROUP BY category
ORDER BY total_revenue DESC;

-- Top Products by Category
WITH top_ranked_items AS (
    SELECT category, item_purchased, SUM(purchase_amount) AS total_revenue,
           RANK() OVER (PARTITION BY category ORDER BY SUM(purchase_amount) DESC) AS rank
    FROM clean_customer_data
    GROUP BY category, item_purchased
)
SELECT category, item_purchased, total_revenue
FROM top_ranked_items
WHERE rank = 1;
```

---

## 📈 Power BI Dashboard
A multi-page Power BI dashboard was created to present business insights visually.
### Dashboard pages include:
### 1️⃣ Executive Overview
  - Total Revenue
  - Total Customers
  - Total Transactions
  - Revenue by Category
  - Revenue by Season
  - Revenue by Gender

![Executive Overview Dashboard](./images/executive_overview.png)

---

### 2️⃣ Customer Analysis
 - Revenue by Customer Segment
 - Customer Distribution
 - Revenue by Age Group
 - Average Purchase Amount by Age Group
 - Promotion Impact Analysis

![Customer Analysis Dashboard](./images/customer_analysis.png)

---

### 3️⃣ Product & Promotion Analysis
  - Top Products by Revenue
  - Category Ratings
  - Promotion vs Non-Promotion Revenue
  - Average Order Value by Category

![Product & Promotion Dashboard](./images/product_promotion.png)

---

## 🔍 Key Insights
### The analysis revealed several important insights:
  - Clothing is the highest revenue generating category.
  - Loyal customers contribute the majority of total revenue.
  - Middle-aged customers represent the largest spending segment.
  - Fall season generates the highest sales volume.
  - Promotions have limited impact on increasing average purchase value.
  - Footwear has the highest average customer satisfaction rating.

## 💡 Business Recommendations
### Based on the analysis, the following recommendations can be made:
 - Focus marketing efforts on loyal customers to maximize retention.
 - Expand inventory for high-performing product categories like clothing.
 - Improve promotional strategies to increase their effectiveness.
 - Develop targeted campaigns for high-value age groups.
 - Increase marketing activity during lower-performing seasons.
  
## 🚀 Future Improvements
### Potential future enhancements include:
 - Customer churn prediction using machine learning
 - Recommendation system for personalized product suggestions
 - Real-time data pipeline integration
 - Advanced customer lifetime value analysis


## 📬 Contact
 **Shoaib Alam** - [https://www.linkedin.com/in/shoaib-alam-769827265/]
 **Email** - [shoaibalam7459@gmail.com]



