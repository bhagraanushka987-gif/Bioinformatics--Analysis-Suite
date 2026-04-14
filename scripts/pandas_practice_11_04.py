"""
BIOINFORMATICS TRANSFORMATION DRILLS
Focus: Aggregations, Lambda Mapping, and Dataset Normalization
"""

import pandas as pd
#SECTION 1: BUSINESS LOGIC AGGREGATION
# Wisdom: Summarizing sales performance and categorizing records.
data = {'city': ['Delhi', 'Mumbai', 'Delhi', 'Chennai', 'Mumbai'],
        'sales': [5000, 8000, 6000, 4000, 9000]}
df = pd.DataFrame(data)
# Aggregating and sorting results for performance review
total_sales = df.groupby("city").sales.sum()
print(f"total city per city:", total_sales)
sort_values = total_sales.sort_values( ascending = False)
print(f"sort highest to lowest:", sort_values)
# Categorizing performance using Lambda functions
df["sales_category"] = df["sales"].map(lambda p:
    "High" if p > 6000  else
    "Low"
)
print(f"creating a column:", df["sales_category"])

# SECTION 2: LABORATORY REVENUE & SALARY ANALYSIS
# Wisdom: Calculating department averages and assigning experience levels.
data = {'department': ['HR', 'IT', 'HR', 'Finance', 'IT', 'Finance'],
        'salary': [40000, 80000, 45000, 60000, 90000, 65000]}
df = pd.DataFrame(data)
# Grouping by department to find mean resource allocation
avg_salary = df.groupby('department').salary.mean()
print(f"average salary per department:", avg_salary)
sort_salary = avg_salary.sort_values()
print(f"sorting lowest to highest", sort_salary)
# Applying experience mapping
df["level"] = df["salary"].map(lambda p:
    "Senior" if p > 70000 else
    "Junior"
)
print(f"new column called level:", df["level"])

# SECTION 3: GENOMIC DATA NORMALIZATION
# Wisdom: Stripping whitespace and standardizing CASE to ensure
# successful relational merges in bioinformatics.
# 1. Create the messy data
data_genes = {'Gene_Name': ['cox-2', 'IL-6 ', ' TNF-alpha'], 'Binding_Score': [-7.2, -8.1, -6.5]}
data_master = {'Gene_Name': ['COX-2', 'IL-6', 'TNF-ALPHA'], 'Function': ['Inflammation', 'Immune Response', 'Cytokine']}

df_genes = pd.DataFrame(data_genes)
df_master = pd.DataFrame(data_master)
# Standardizing 'Gene_Name' across both DataFrames
# Wisdom: ' IL-6 ' will never match 'IL-6' without .strip()
df_genes['Gene_Name'] = df_genes['Gene_Name'].str.strip().str.upper()
df_master['Gene_Name'] = df_master['Gene_Name'].str.strip().str.upper()
df_final = pd.merge(df_genes, df_master , on = 'Gene_Name', how='left')
# Merging research datasets with a 'left join' logic
print("--- Cleaned and Merged Research Data ---")
print(df_final)