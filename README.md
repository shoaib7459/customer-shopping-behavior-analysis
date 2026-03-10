# Customer Activity & Trends Analysis Insights

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-green.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

## 📋 Project Overview

A complete end-to-end data analytics project that transforms raw customer transaction data into actionable business insights. This project demonstrates the full data analytics workflow: data cleaning, exploratory analysis, SQL querying, and interactive dashboard creation.

**Live Dashboard:** [Add Power BI Service Link Here]
**Project Report:** [Add PDF Report Link Here]

## 🎯 Key Business Questions Answered

- Which customer segments generate the highest revenue?
- What products drive sales in each category?
- How do discounts and promotions impact purchase behavior?
- Which seasons perform best for different product categories?
- What are the spending patterns across age groups and genders?

## 📊 Dataset Overview

| Metric | Value |
|--------|-------|
| **Total Records** | 3,900 transactions |
| **Total Features** | 18 columns |
| **Customer Age Range** | 18-70 years |
| **Purchase Range** | $20 - $100 |

### Features Included

| Category | Features |
|----------|----------|
| **Customer Info** | Age, Gender, Location, Subscription Status |
| **Product Details** | Item Purchased, Category, Size, Color, Season |
| **Transaction Data** | Purchase Amount, Discount Applied, Promo Code Used, Shipping Type |
| **Customer Behavior** | Previous Purchases, Purchase Frequency, Review Rating |

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python** | Data cleaning, preprocessing, EDA |
| **Pandas/NumPy** | Data manipulation |
| **Matplotlib/Seaborn** | Data visualization |
| **MySQL** | Data storage and querying |
| **Power BI** | Interactive dashboard |
| **Jupyter Notebook** | Development environment |

## 📁 Project Structure
```
customer-behavior-analysis/
│
├── data/
│ ├── raw/
│ │ └── customer_shopping_behavior.csv
│ └── processed/
│ └── clean_customer_data.csv
│
├── notebooks/
│ ├── 01_data_cleaning.ipynb
│ ├── 02_eda_analysis.ipynb
│ └── 03_sql_queries.ipynb
│
├── sql/
│ ├── create_tables.sql
│ └── business_queries.sql
│
├── dashboard/
│ └── powerbi_dashboard.pbix
│
├── reports/
│ └── Project_Report.pdf
│
├── src/
│ ├── init.py
│ ├── main.py
│
├── logs/
│ └── pipeline.log
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```
