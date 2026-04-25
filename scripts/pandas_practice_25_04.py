"""
PANDAS RELATIONAL MAPPING & JOIN LOGIC - DAY 11
Focus: pd.merge (Inner Joins), Multi-Condition Filtering, and Aggregation Pipelines
Project: Pharmaceutical Pricing, Corporate Staffing, and Regional Revenue Analytics
"""
import pandas as pd
# ==========================================
# SECTION 1: PHARMACEUTICAL STRATIFICATION
# ==========================================
data = {'drug': ['Aspirin', 'Ibuprofen', 'Paracetamol', 'Metformin'],
        'category': ['Pain', 'Pain', 'Fever', 'Diabetes'],
        'price': [25, 45, 15, 35]}
df = pd.DataFrame(data)
# 1.1 Categorical & Pricing Filters
filter_pain = df[df["category"] == "Pain"]
print(f"filtering category where psin is their:", filter_pain)
filter_price = df[df["price"] > 20]
print(f"filter where price is above 20:", filter_price)
# 1.2 Multi-Condition Logical AND
# Isolating premium pain-relief medication (>30)
filter_both = df[(df["category"] == "Pain") & (df["price"] > 30)]
print(f"filter wherer category and price is both present:", filter_both)
# 1.3 Statistical Mean Performance
avg_price = df.groupby("category").price.mean()
print(f"avergae price per category:", avg_price)
sorting = avg_price.sort_values(ascending = False)
print(f"sorting average values from highest to lowest:", sorting)

# ==========================================
# SECTION 2: RELATIONAL DATA MERGING (JOINS)
# ==========================================

# 2.1 Corporate Directory Integration
staff_data = {
    'Emp_ID': [101, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana']
}
staff_df = pd.DataFrame(staff_data)

dept_data = {
    'Emp_ID': [102, 104, 101, 103], # Notice the IDs are jumbled!
    'Department': ['IT', 'Sales', 'HR', 'Engineering']
}
dept_df = pd.DataFrame(dept_data)

print("--- Staff Table ---")
print(staff_df, "\n")
# Performing an Inner Join on the unique Employee Identifier
complete_df = pd.merge(staff_df, dept_df, on = "Emp_ID")
print(f"merging both tables: {complete_df}")

# 2.2 Logistics & Inventory Synchronization
stock_data = {
    'SKU': ['A1', 'B2', 'C3'],
    'Quantity': [50, 10, 100]
}
stock_df = pd.DataFrame(stock_data)

category_data = {
    'SKU': ['C3', 'A1', 'B2'],
    'Category': ['Office', 'Electronics', 'Breakroom']
}
category_df = pd.DataFrame(category_data)

merging_data = pd.merge(stock_df, category_df , on = "SKU")
print(f"merging both the data frames: {merging_data}")

# ==========================================
# SECTION 3: REVENUE PIPELINE & GEOMAPPING
# ==========================================

# 3.1 Transactional and Spatial Data Definition
# Table 1: The Transactions
sales_data = {
    'Transaction_ID': ['T1', 'T2', 'T3', 'T4', 'T5'],
    'Store_ID': ['S101', 'S102', 'S101', 'S103', 'S102'],
    'Revenue': [400, 1200, 800, 300, 950]
}
sales_df = pd.DataFrame(sales_data)

# Table 2: The Store Map
location_data = {
    'Store_ID': ['S103', 'S101', 'S102'],
    'City': ['Chicago', 'New York', 'Seattle']
}
locations_df = pd.DataFrame(location_data)

merged_df = pd.merge(sales_df, locations_df, on = "Store_ID")
print(f"merging the data:{merged_df}")
# 3.2 Join & Filter Pipeline
# Linking revenue to city locations and filtering for high-value outliers (>500)
high_value_df = merged_df[merged_df["Revenue"] >500]
print(f"filtering the revenue:{high_value_df}")
# 3.3 Regional Revenue Aggregation
filtering_columns = high_value_df.groupby("City").Revenue.sum().sort_values(ascending = False).reset_index()
print(f"filtering the data: {filtering_columns}")