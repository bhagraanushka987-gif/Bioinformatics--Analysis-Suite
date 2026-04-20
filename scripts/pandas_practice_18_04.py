"""
PANDAS DATA STRATIFICATION & HIT IDENTIFICATION - DAY 06
Focus: Multi-Condition Filtering, Grouped Aggregations, and Subset Integrity
Project: Corporate Payroll, Urban Metrics, and Genomic Screening
"""

import pandas as pd

# ==========================================
# SECTION 1: CORPORATE PAYROLL ANALYSIS
# ==========================================

data_payroll = {
    'name': ['Alice', 'Bob', 'Carol', 'Dave', 'Eve'],
    'department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'salary': [42000, 95000, 67000, 88000, 51000]
}
df_payroll = pd.DataFrame(data_payroll)

# Targeted Department Filtering
filter_department = df_payroll[df_payroll["department"] == "IT"]
print(f"IT Department Roster:\n{filter_department}\n")

# Salary Threshold Filtering
filter_salary = df_payroll[df_payroll["salary"] > 60000]
print(f"High-Salary Tier (> 60k):\n{filter_salary}\n")

# Logical AND Filtering (HR Personnel above 45k)
filter_both = df_payroll[(df_payroll["department"] == "HR") & (df_payroll["salary"] > 45000)]
print(f"Priority HR Personnel Filter:\n{filter_both}\n")

# Aggregation: Total Expenditure by Department
total_salary = df_payroll.groupby("department").salary.sum()
print(f"Total Expenditure per Department:\n{total_salary}\n")

# Ranking Departments by Financial Impact
sorting_payroll = total_salary.sort_values(ascending=False)
print(f"Departmental Expenditure Ranking (High to Low):\n{sorting_payroll}\n")

# ==========================================
# SECTION 2: URBAN PERFORMANCE METRICS
# ==========================================

data_urban = {
    'name': ['Alice', 'Bob', 'Carol', 'Dave', 'Eve'],
    'city': ['Delhi', 'Mumbai', 'Delhi', 'Chennai', 'Mumbai'],
    'score': [85, 92, 78, 65, 88]
}
df_urban = pd.DataFrame(data_urban)

# Regional Filtering
filter_city = df_urban[df_urban["city"] == "Mumbai"]
print(f"Mumbai Regional Data:\n{filter_city}\n")

# Performance Thresholding
filter_score = df_urban[df_urban["score"] > 80]
print(f"Top Performance Metrics (> 80):\n{filter_score}\n")

# Targeted Regional Analysis (Delhi High Scorers)
filter_city_score = df_urban[(df_urban["city"] == "Delhi") & (df_urban["score"] > 80)]
print(f"Delhi High-Score Filter:\n{filter_city_score}\n")

# Statistical Mean: Performance by City
avg_score = df_urban.groupby("city").score.mean()
print(f"Regional Average Performance Score:\n{avg_score}\n")

# Ordinal Sorting: Ascending Performance
sorting_urban = avg_score.sort_values()
print(f"City Rankings by Average Score (Ascending):\n{sorting_urban}\n")

# ==========================================
# SECTION 3: BIOINFORMATICS - HIT IDENTIFICATION
# ==========================================

df_results = pd.DataFrame({
    'Gene': ['G1', 'G2', 'G3'],
    'Score': [-9.1, -8.5, -6.2]
})

# Professional Data Integrity: Using .copy() to decouple from original DataFrame
# Highlighting genes with significant binding affinity (Score < -8.0)
strong_hits = df_results[df_results["Score"] < -8.0].copy()
strong_hits['Status'] = 'Priority'

print("--- Genomic Screening: Priority Hit Report ---")
print(strong_hits)