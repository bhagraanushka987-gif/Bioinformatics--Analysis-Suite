"""
PANDAS AGGREGATION & PROFIT PIPELINES - DAY 13
Focus: Multi-level Grouping, Feature Engineering (Profit/Sale Price), and Data Sorting
Project: Academic Productivity, Platform Metrics, and Global Retail Finance
"""
import pandas as pd
# ==========================================
# SECTION 1: ACADEMIC PRODUCTIVITY METRICS
# ==========================================

data = {'researcher': ['Alice', 'Bob', 'Carol', 'Dave', 'Eve'],
        'department': ['Genomics', 'Proteomics', 'Genomics', 'Metabolomics', 'Proteomics'],
        'publications': [12, 8, 15, 6, 11]}
df = pd.DataFrame(data)
# 1.1 Total Output per Department
total_publication = df.groupby("department").publications.sum()
print(f"total publication per department:", total_publication)
sorting = total_publication.sort_values(ascending = False)
print(f"sorting from highest to lowest:", sorting)
# 1.2 Mean Productivity (Average Publications)
avg_pub = df.groupby("department").publications.mean()
print(f"average publication per department:", avg_pub)
sorting_mean = avg_pub.sort_values()
print(f"sorting from lowest to highest:", sorting_mean)

# ==========================================
# SECTION 2: MARKET PENETRATION (PLATFORM DOWNLOADS)
# ==========================================
data = {
    'Region': ['North', 'North', 'South', 'East', 'South', 'East'],
    'Platform': ['iOS', 'Android', 'Android', 'iOS', 'iOS', 'Android'],
    'Downloads': [5000, 7000, 8500, 3000, 4000, 6000]
}
df = pd.DataFrame(data)

print("--- Raw Download Data ---")
print(df, "\n")
# Aggregating global reach by platform
total_downloads =  df.groupby("Platform").Downloads.sum().sort_values(ascending = False)
print(f"total downloads from each platforms:{total_downloads}")

# ==========================================
# SECTION 3: RETAIL STRATEGY (FEATURE ENGINEERING)
# ==========================================
data = {
    'Product': ['Laptop', 'Desk Chair', 'Headphones', 'Coffee Mug', 'Monitor'],
    'Category': ['Electronics', 'Furniture', 'Electronics', 'Kitchen', 'Electronics'],
    'Price': [1000, 150, 200, 15, 300]
}
df = pd.DataFrame(data)
# 3.1 Targeted Filtering & Data Security
# Using .copy() to ensure we don't modify the original master inventory
electronics_df = df[df["Category"] == "Electronics"].copy()
print(f"rows where the category is electronics:{electronics_df}")
# 3.2 Calculating Sale Price (20% Discount)
electronics_df["Sale_Price"] = electronics_df["Price"] * 0.80
print(f"sale on electronics:{electronics_df}")
# 3.3 Sorting by Promotional Pricing
sorting = electronics_df.sort_values("Sale_Price", ascending = True)
print(f"sorting the values:{sorting}")

# ==========================================
# SECTION 4: GLOBAL OPERATIONAL FINANCE
# ==========================================
data = {
    'Country': ['USA', 'Canada', 'USA', 'UK', 'Canada', 'UK'],
    'Store_Type': ['Drive-Thru', 'Cafe', 'Drive-Thru', 'Drive-Thru', 'Drive-Thru', 'Cafe'],
    'Revenue': [5000, 3000, 7000, 4000, 4500, 2500],
    'Costs': [2000, 1500, 3000, 1800, 2000, 1200]
}
df = pd.DataFrame(data)
# 4.1 Stratification: Isolating Drive-Thru Operations
drive_thru_df = df[df["Store_Type"] == "Drive-Thru"].copy()
print(f"rows where the category is drive thru:{drive_thru_df}")
# 4.2 Calculating Net Profit
drive_thru_df["Profit"] = drive_thru_df["Revenue"] - drive_thru_df["Costs"]
print(f"calculating the profit:{drive_thru_df}")
# 4.3 Aggregating Global Profit by Country
global_profit = drive_thru_df.groupby("Country").Profit.sum().sort_values(ascending = False).reset_index()
print(f"calculating the global profit:{global_profit}")

