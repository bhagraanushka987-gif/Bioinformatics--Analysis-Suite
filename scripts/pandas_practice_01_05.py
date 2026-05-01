"""
PANDAS RELATIONAL INTEGRATION & AGGREGATE MODELING - DAY 17
Focus: Vertical Concatenation, Horizontal Inner Merging, and Grouped Statistics
Project: Multi-Source Genomic Tables, Retail Regional Audits, and HR Salary Metrics
"""
import pandas as pd
# ==========================================
# SECTION 1: GENOMIC DATA INTEGRATION
# ==========================================

# 1.1 Vertical Growth: Combining disparate gene expression cohorts
df1 = pd.DataFrame({'gene': ['BRCA1', 'TP53', 'EGFR'],
                    'expression': [8.5, 12.3, 6.7]})

df2 = pd.DataFrame({'gene': ['KRAS', 'MYC'],
                    'expression': [9.1, 15.2]})
# Concatenating cohorts and resetting index to ensure a continuous data range
concating = pd.concat([df1, df2]).reset_index(drop=True)
print(f"concating both the data frames:{concating}")
# 1.2 Horizontal Enrichment: Merging Expression with Functional Metadata
df_expression = pd.DataFrame({'gene': ['BRCA1', 'TP53', 'EGFR'],
                               'expression': [8.5, 12.3, 6.7]})

df_function = pd.DataFrame({'gene': ['BRCA1', 'TP53', 'EGFR'],
                             'function': ['Tumor Suppressor', 'Tumor Suppressor', 'Oncogene']})
# Merging on the unique 'gene' identifier (Inner Join logic)
joining = pd.merge(df_expression, df_function, on='gene')
print(f"joining both the data frame:{joining}")
# Renaming for publication-ready terminology
renaming = joining.rename(columns={"expression":"exp_level"})
print(f"renaming the column:{renaming}")
# ==========================================
# SECTION 2: RETAIL & ADVERTISING LOGISTICS
# ==========================================

# 2.1 Regional Sales Consolidation
north_sales = pd.DataFrame({'Store_ID': [1, 2], 'Rev': [5000, 7500]})
south_sales = pd.DataFrame({'Store_ID': [3, 4], 'Rev': [6200, 4100]})
region_map = pd.DataFrame({'Store_ID': [1, 2, 3, 4], 'Location': ['NY', 'BOS', 'ATL', 'MIA']})
# Pipeline: Concat -> Merge -> Rename
all_sales = pd.concat([north_sales, south_sales])
final_report = pd.merge(all_sales, region_map, on ="Store_ID")
renaming = final_report.rename(columns={"Rev":"Revenue"})
print(f"printing the final report:{renaming}")

# 2.2 Advertising Conversion Analysis
q1_ads = pd.DataFrame({'Camp_ID': ['A1', 'B2'], 'Conv': [150, 200]})
q2_ads = pd.DataFrame({'Camp_ID': ['C3', 'D4'], 'Conv': [300, 100]})
campaign_names = pd.DataFrame({'Camp_ID': ['A1', 'B2', 'C3', 'D4'], 'Name': ['Holiday', 'Spring', 'Summer', 'Fall']})

all_ads = pd.concat([q1_ads, q2_ads]).reset_index(drop =True)
final_report = pd.merge(all_ads, campaign_names, on="Camp_ID")
rename = final_report.rename(columns={"Conv":"Conversion"})
print(f"making the final report:{rename}")

# ==========================================
# SECTION 3: HR ANALYTICS & GROUPED STATS
# ==========================================
hr_data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT'],
    'Status': ['Active', 'Terminated', 'Active', 'Active', 'Active', 'On Leave'],
    'Salary': [90000, 60000, 95000, 120000, 65000, 80000]
}
df = pd.DataFrame(hr_data)
# 3.1 Targeted Filtering: Active Personnel Only
active_df = df[df["Status"] == "Active"]
print(f"filtering the data:{active_df}")
# 3.2 Departmental Benchmarking: Mean Salary calculation for active staff
filtering_salary = active_df.groupby("Department").Salary.mean()
print(f"filtering department based on salary:{filtering_salary}")