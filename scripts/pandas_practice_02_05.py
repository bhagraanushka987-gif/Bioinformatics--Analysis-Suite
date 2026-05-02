"""
GENOMIC STRATIFICATION & TIME-SERIES REVENUE ANALYSIS - DAY 18
Focus: Chromosomal Filtering, Vectorized Price Discounts, and Temporal Resampling
Project: Multi-Gene Expression Audits and Q1 Financial Reporting
"""

import pandas as pd

# ==========================================
# SECTION 1: GENOMIC EXPRESSION STRATIFICATION
# ==========================================


data = {'gene': ['BRCA1', 'TP53', 'EGFR', 'KRAS', 'MYC'],
        'chromosome': [17, 17, 7, 12, 8],
        'expression': [8.5, 12.3, 6.7, 9.1, 15.2]}
df = pd.DataFrame(data)
# 1.1 Targeted Chromosomal Audit (Chromosome 17 focus)
filtering_chromosome = df[df["chromosome"] == 17]
print(f"filtering:{filtering_chromosome}")
# 1.2 Potency Threshold: High-expression (>9) isolation
filtering_expression = df[df["expression"] >9]
print(f"filtering:{filtering_expression}")
# 1.3 Advanced Set Filtering: Multi-chromosome selection
filtering_chromo = df[df["chromosome"].isin([7, 12])]
print(f"filtering chromosome:{filtering_chromo}")
# 1.4 Range-Based Filtering: Mid-range expression bracket (8-13)
filter_exp = df[df["expression"].between(8,13)]
print(f"filtering expression:{filter_exp}")
# 1.5 Chromosomal Benchmarking: Mean expression sorted by density
avg_mean = df.groupby("chromosome").expression.mean().sort_values(ascending = False)
print(f"avg expression by chromosome sorting from highest to lowest:{avg_mean}")

# ==========================================
# SECTION 2: CONDITIONAL PRICE ENGINEERING
# ==========================================
store_data = {
    'Product': ['Headphones', 'Mouse', 'Keyboard', 'Monitor', 'Mousepad'],
    'Price': [150.0, 45.0, 120.0, 300.0, 15.0]
}
df = pd.DataFrame(store_data)
def calculate_discount(price):
    if price > 100:
        return price * 0.8
    else:
        return price * 0.9
# Applying the discount logic across the Price column
df["Sale_Price"] = df['Price'].apply(calculate_discount)
print(f"sale price of products:{df}")

# ==========================================
# SECTION 3: TIME-SERIES REVENUE REPORTING
# ==========================================
sales_data = {
    'Date': ['2023-01-15', '2023-01-28', '2023-02-05', '2023-02-14', '2023-03-01'],
    'Revenue': [500, 300, 450, 600, 1200]
}
df = pd.DataFrame(sales_data)
# 3.1 Object Conversion: String to Datetime
df["Date"] = pd.to_datetime(df["Date"])
# 3.2 Feature Engineering: Extracting Month for Resampling
df["Month"] = df["Date"].dt.month_name()
# 3.3 Aggregation: Total Revenue per Calender Month
monthly_report = df.groupby("Month").Revenue.sum()
print("--- Q1 Monthly Revenue ---")
print(monthly_report)