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
✅ Automated data pipeline using Python  
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

### Customer Segmentation
| Segment | Count | % of Total |
|---------|-------|------------|
| Loyal | 3,116 | 79.9% |
| Returning | 701 | 18.0% |
| New | 83 | 2.1% |

### Seasonal Performance
- **Fall** is peak season: $60,018 revenue
- **Summer** is slowest: $55,777 revenue
- Clothing is top category in ALL seasons

### Gender Analysis
- Male customers contribute **68%** of total revenue
- Male:Female spending ratio is approximately **2.1:1** across all categories

---

## 📊 Results Summary

| Metric | Value |
|--------|-------|
| Total Revenue | $233,000 |
| Total Customers | 3,900 |
| Average Order Value | $59.76 |
| Loyal Customers | 79.9% |
| Top Category | Clothing ($104K) |
| Peak Season | Fall ($60K) |
| Gender Split | 68% Male / 32% Female |

---

## 📊 Dashboard Preview

### Executive Overview Dashboard

![Executive Overview Dashboard](./images/executive_overview.png)

**Key Insights:**
- **Total Revenue:** $233,000
- **Total Customers:** 3,900
- **Average Order Value:** $59.76
- Clothing dominates revenue ($104K), followed by Accessories ($74K)
- Male customers contribute 68% of total revenue

---

### Customer Analysis Dashboard

![Customer Analysis Dashboard](./images/customer_analysis.png)

**Key Insights:**
- Loyal customers drive 80%+ of revenue ($186K) – strong retention
- Middle-aged customers are the highest spending age group

---

### Product & Promotion Analysis

![Product & Promotion Dashboard](./images/product_promotion.png)

**Key Insights:**
- Top products: Blouse, Shirt, Dress lead in revenue
- Promo codes used in 43% of orders but slightly reduce average order value
- Footwear has highest customer satisfaction ratings

---

## 🗄️ SQL Business Queries

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

## 📝 Key Insights & Recommendations

### 👑 Loyal Customers are Gold
- **Finding:** 79.9% of customers are loyal, contributing 80%+ of revenue
- **Action:** Implement VIP program with exclusive perks

### 👕 Clothing Drives Business
- **Finding:** 44.7% of revenue from clothing
- **Action:** Expand clothing inventory, featured placements

### 🏷️ Discount Strategy Needs Review
- **Finding:** Discounts don't increase order value ($0.85 difference)
- **Action:** Use discounts for acquisition, not upselling

### 📅 Seasonal Planning
- **Finding:** Fall is peak season ($60K), Summer low ($55.8K)
- **Action:** Plan major campaigns in Fall, clearance in Summer
  
## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 📬 Contact
**Shoaib Alam** - [https://www.linkedin.com/in/shoaib-alam-769827265/]

**Project Link:** https://github.com/shoaib7459/customer-behavior-analysis
 



