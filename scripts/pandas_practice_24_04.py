"""
PANDAS DATA CLEANING & IMPUTATION SUITE - DAY 10
Focus: Missing Value Handling (.fillna), Type Casting (.astype), and Pipeline Aggregation
Project: Clinical Records, Inventory Management, and Regional Revenue Analytics
"""
import pandas as pd
# ==========================================
# SECTION 1: CLINICAL DATA IMPUTATION
# ==========================================
data = {'patient': ['Alice', 'Bob', 'Carol', 'Dave'],
        'age': [None, 45, None, 38],
        'blood_pressure': [120, None, 135, None]}
df = pd.DataFrame(data)
# Professional Technique: Imputing with Central Tendency
# Filling Age with Median (Robust to outliers) and BP with Mean
df["age"] = df["age"].fillna(df["age"].median())
df["blood_pressure"] = df["blood_pressure"].fillna(df["blood_pressure"].mean())
# Casting to Integer for clean reporting
df["age"] = df["age"].astype(int)
print(df)

import numpy as np
# ==========================================
# SECTION 2: INVENTORY LOGISTICS
# ==========================================
data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'Quantity': [5.0, np.nan, 12.0, np.nan]
}
df = pd.DataFrame(data)

print("--- Raw Inventory ---")
print(df, "\n")

df["Quantity"] = df["Quantity"].fillna(0).astype(int)
print(df)
# ==========================================
# SECTION 3: REGIONAL PERFORMANCE PIPELINE
# ==========================================
data = {
    'Store_ID': ['S1', 'S2', 'S3', 'S4', 'S5'],
    'Region': ['North', 'South', 'North', 'East', 'South'],
    'Customers': [600, np.nan, 800, 450, 1200],
    'Revenue': [50000, 20000, 80000, 30000, 100000]
}
df = pd.DataFrame(data)
# 3.1 Data Cleaning & Feature Engineering
df["Customers"] = df["Customers"].fillna(0).astype(int)
print(df)
# Calculating Net Revenue (5% Tax Deduction)
df["net_revenue"] = df["Revenue"].apply(lambda p : p * 0.95)
print(f"new column to calculate the net revenue:", df["net_revenue"])
# 3.2 High-Traffic Stratification
# Identifying stores with > 500 customers
high_traffic_df = df[df["Customers"] > 500]
print(f"new column filtering where customers are greater than 500:", high_traffic_df)
# 3.3 Regional Revenue Aggregation
# Grouping by region and ranking by total net revenue
new_column = high_traffic_df.groupby("Region").net_revenue.sum().sort_values(ascending = False).reset_index()
print(f"new column:", new_column)