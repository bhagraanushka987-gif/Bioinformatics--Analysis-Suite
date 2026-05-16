"""
PANDAS DATA IMPUTATION, STRATIFIED DROPSTAGE, AND RELATIONAL JOINING - DAY 32
Focus: Statistical Imputation (Mean/Median), Missing Segment Dropping, and Faceted Aggregations
Project: Genomic Integrity Audits, Human Resources Portfolios, and CRM Financial Pipelines
"""
import pandas as pd
import numpy as np

# ==========================================
# SECTION 1: GENOMIC DATA IMPUTATION
# ==========================================
data = {'gene': ['BRCA1', 'TP53', 'EGFR', 'KRAS'],
        'expression': [8.5, None, 6.7, None],
        'chromosome': [17, 17, None, 12]}
df = pd.DataFrame(data)
# 1.1 Statistical Imputation: Filling expression with Mean and locus with Median
df["expression"] = df["expression"].fillna(df["expression"].mean())
df["chromosome"] = df["chromosome"].fillna(df["chromosome"].median())
print(df)

# ==========================================
# SECTION 2: CATEGORICAL BENCHMARKING & MAPPING
# ==========================================
data = {'gene': ['BRCA1', 'TP53', 'EGFR', 'KRAS', 'MYC'],
        'expression': [8.5, 12.3, 6.7, 9.1, 15.2],
        'category': ['Low', 'High', 'Low', 'Low', 'High']}
df = pd.DataFrame(data)
# 2.1 Stratified Slicing: Mean expression per expression category
exp_avg = df.groupby("category").expression.mean().sort_values(ascending=False)
print(f"group by the category for the average of expression:{exp_avg}")
# 2.2 Vectorized Scalar Transformation: Doubling expression values via Lambda Map
exp_double = df["expression"].map(lambda p : p * 2)
print(f"doubling the expression data:{exp_double}")

# ==========================================
# SECTION 3: REPLICATE COHORT CONCATENATION
# ==========================================
df1 = pd.DataFrame({'gene': ['BRCA1', 'TP53'],
                    'expression': [8.5, 12.3]})
df2 = pd.DataFrame({'gene': ['EGFR', 'KRAS'],
                    'expression': [6.7, 9.1]})

# 3.1 Vertical Axis Integration with Index Reset
joining = pd.concat([df1, df2]).reset_index(drop=True)
print(f"joining both the data frames:{joining}")
renaming = joining.rename(columns={"expression":"exp_level"})
print(f"renaming the column:{renaming}")

# ==========================================
# SECTION 4: HR METRIC DROPNATION STAGE
# ==========================================
hr_data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Department': ['IT', np.nan, 'Finance', 'HR', np.nan],
    'Salary': [90000.0, 60000.0, np.nan, 120000.0, 65000.0]
}
df = pd.DataFrame(hr_data)
# 4.1 Categorical Imputation: Defaulting missing organizational tags to string label
df["Department"] = df["Department"].fillna("Unassigned")
# 4.2 Critical Value Isolation: Dropping records lacking core salary parameters
clean_df = df.dropna(subset=["Salary"])
print(clean_df)

# ==========================================
# SECTION 5: COMMERCIAL TRANSACTION AGGREGATION
# ==========================================
data = {
    'OrderID': [1, 2, 3, 4, 5],
    'Region': ['North', np.nan, 'South', 'North', 'East'],
    'Status': ['Completed', 'Completed', 'Pending', 'Completed', 'Cancelled'],
    'Amount': [250.0, 100.0, 300.0, 150.0, 50.0]
}
df = pd.DataFrame(data)
df["Region"] = df["Region"].fillna("Unknown")
# 5.2 Filter & Grouped Sum Pipeline: Regional revenue for fulfilled logs only
completed_orders = df[df["Status"] == "Completed"]
final_report = completed_orders.groupby("Region").Amount.sum()
print(final_report)

# ==========================================
# SECTION 6: RELATIONAL METADATA MERGING
# ==========================================
# Table 1: Customer Database
customers = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

# Table 2: Sales Database
orders = pd.DataFrame({
    'OrderID': [101, 102, 103, 104],
    'CustomerID': [2, 1, 1, 3],
    'Amount': [50.0, 120.0, 75.0, 200.0]
})
# 6.1 Horizontal Structural Enrichment: Inner Match Join via Key ID
final_report = pd.merge(customers, orders, on="CustomerID")
print(final_report)