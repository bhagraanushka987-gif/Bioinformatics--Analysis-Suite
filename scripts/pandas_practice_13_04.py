"""
BIOINFORMATICS DATA ANALYSIS SUITE - DAY 01
Focus: Grouping, Sorting, and Conditional Mapping in Pandas
Author: Anushka Bhagra
Date: April 13, 2026
"""
import pandas as pd
# ==========================================
# SECTION 1: Business Revenue Analysis
# Goal: Aggregate revenue by category and classify performance.
# ==========================================
data = {'category': ['Food', 'Tech', 'Food', 'Fashion', 'Tech', 'Fashion'],
        'revenue': [12000, 95000, 18000, 45000, 110000, 52000]}
df = pd.DataFrame(data)
# Grouping and calculating total revenue per category
total_revenue = df.groupby("category").revenue.sum()
print(f"total revenue per category:", total_revenue)
sorting = total_revenue.sort_values(ascending = False)
print(f"sorting highest to lowest:", sorting)
# Using Lambda to classify performance based on a 50k threshold
df["performance"] = df['revenue'].map(lambda p:
    "Strong" if p > 50000 else
    "Weak"
)
print(f"new column:", df["performance"])
# ==========================================
# SECTION 2: Regional Profit Analysis
# Goal: Calculate average profit and identify profitability status.
# ==========================================
data = {'region': ['North', 'South', 'North', 'East', 'South', 'East'],
        'profit': [25000, 72000, 31000, 48000, 85000, 53000]}
df = pd.DataFrame(data)
# Calculating mean profit per region
avg_profit = df.groupby("region").profit.mean()
print(f"mean profit per region:", avg_profit)
sorting = avg_profit.sort_values()
print(f"sorting lowest to highest:", sorting)
# Mapping status using a 60k profitability threshold
df['status'] = df['profit'].map(lambda p:
    "Profit" if p > 60000 else
    "Loss"
)
print(f"new column for checking status:", df['status'])

# ==========================================
# SECTION 3: Bioinformatics - Gene Affinity Filtering
# Goal: Isolate top gene candidates for the Piper longum study.
# ==========================================
data = {
    'Gene_Name': ['COX-2', 'IL-6', 'TNF-alpha', 'SIRT1', 'PTGS2'],
    'Affinity_Score': [-7.2, -8.5, -6.8, -9.1, -8.2]
}
df = pd.DataFrame(data)
# Filtering for high-affinity candidates (Scores less than -8.0 kcal/mol)
top_candidates = df[df["Affinity_Score"] < -8.0]
print(f"top candidates based on their affinity:", top_candidates)