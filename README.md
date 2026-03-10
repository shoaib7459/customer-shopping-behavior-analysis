# Customer Activity & Trends Analysis Insights

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-green.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

## 📋 Project Overview

A complete end-to-end data analytics project that transforms raw customer transaction data into actionable business insights. This project demonstrates the full data analytics workflow: data cleaning, exploratory analysis, SQL querying, and interactive dashboard creation.

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
├── src/
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

## 🔄 Data Pipeline Workflow

### Key Pipeline Features:
- ✅ Automated logging for error tracking
- ✅ Configurable file paths
- ✅ Modular functions for reusability
- ✅ Error handling at each stage
- ✅ Database integration

## 📈 Key Findings

### Revenue by Category
- **Clothing** dominates with **$104,264** (44.7% of total revenue)
- **Accessories** follows at **$74,200** (31.8%)
- **Footwear** and **Outerwear** contribute remaining 23.5%

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

## 💻 Getting Started

### Prerequisites
- Python 3.9+
- MySQL 8.0+
- Power BI Desktop (for dashboard)

## 📊 Dashboard Preview
  ### Executive Overview Dashboard
  ![Executive Overview](images/executive_overview.png)
  ## 📈 Key Insights
   - **Total Revenue:** 233K
   - **Total Customers:** 3900
   - **Average Order Value:**  59.76
  ## Clothing contributes the largest revenue share at 104K, followed by Accessories at 74K.Male customers contribute 68% of total revenue.

  ### Customer Analysis Dashboard
  ![Executive Overview](images/customer_analysis.png)
  ## 📈 Key Insights
    - ## Loyal customers generate the majority of revenue, contributing 186K, which indicates strong customer retention
    - ## Middle-aged customers generate the highest revenue contribution among age groups.

  ### Product & Promotion Analysis
  ![Executive Overview](images/product_promotion.png)
  ## 📈 Key Insights
  ## Blouse, Shirt, and Dress are among the top revenue-generating products.
  ## Promo codes are used in 43% of orders, but they slightly reduce average order value.
  ## Footwear has the highest customer satisfaction rating.

## 🗄️ SQL Business Queries
```Category Revenue Analysis
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
  ## Loyal Customers are Gold
  - **Finding:** 79.9% of customers are loyal, contributing 80%+ of revenue
  - **Action:** Implement VIP program with exclusive perks
  
## Clothing Drives Business
 - **Finding:** 44.7% of revenue from clothing
 - **Action:** Expand clothing inventory, featured placements
 
## Discount Strategy Needs Review
  **Finding:** Discounts don't increase order value ($0.85 difference)
  **Action:** Use discounts for acquisition, not upselling

## Seasonal Planning
  **Finding:** Fall is peak season ($60K), Summer low ($55.8K)
  **Action:** Plan major campaigns in Fall, clearance in Summer
  
## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 📬 Contact
**Shoaib Alam** - [https://www.linkedin.com/in/shoaib-alam-769827265/]

**Project Link:** https://github.com/Shoaib-Alam-Ansari/customer-behavior-analysis
 



