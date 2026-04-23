"""
PANDAS FEATURE ENGINEERING & CATEGORICAL MAPPING - DAY 09
Focus: Lambda Functions (.map), Row-wise Operations (.apply), and Complex Logic
Project: Genomic Expression Status, Payroll Bonuses, and Elite Revenue Analytics
"""

import pandas as pd

# ==========================================
# SECTION 1: GENOMIC EXPRESSION MAPPING
# ==========================================
data = {'gene': ['BRCA1', 'TP53', 'EGFR', 'KRAS'],
        'expression': [8.5, 12.3, 6.7, 9.1]}
df = pd.DataFrame(data)

# 1.1 Rapid Classification using Lambda and .map()
# Categorizing expression levels into binary High/Low tiers
df["exp_category"] = df["expression"].map(lambda p:
    "High" if p > 9 else
    "Low"
)
print(f"new column in the table:", df["exp_category"])
# 1.2 String Normalization via Lambda
df["gene_lower"] = df["gene"].map(lambda p : p.lower())
print(f"printing genes in lower case:", df["gene_lower"])

# 1.3 Row-wise Evaluation using .apply()
# Defining clinical status based on expression thresholds
def classify_gene(row):
    if row['expression'] > 10:
        return "Overexpressed"
    else:
        return "Normal"
df['gene_status'] = df.apply(classify_gene, axis='columns')
print(f"new column:", df["gene_status"])

# ==========================================
# SECTION 2: CORPORATE PAYROLL CALCULATIONS
# ==========================================

data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Department': ['HR', 'IT', 'IT', 'HR'],
    'Salary': [60000, 85000, 90000, 65000]
}
df = pd.DataFrame(data)

print("--- Original Data ---")
print(df, "\n")
# Vectorized Lambda for financial incentive calculations (10% Bonus)
df["bonus"] = df["Salary"].apply(lambda p : p * 0.10)
print(f"bonus salary to each employee:",df["bonus"])

# ==========================================
# SECTION 3: STRATIFIED REVENUE PERFORMANCE
# ==========================================

data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Department': ['Sales', 'HR', 'IT', 'Sales', 'HR', 'IT'],
    'Certification': ['Standard', 'Pro', 'Pro', 'Pro', 'Standard', 'Standard'],
    'Revenue': [120000, 80000, 150000, 200000, 60000, 90000]
}
df = pd.DataFrame(data)

# Filtering for 'Elite' performers: Sales OR Pro-certified personnel
# Note: Using | as the 'OR' operator for Boolean Indexing
elite_df = df[(df["Department"] == "Sales") |(df["Certification"] == "Pro")]

avg_salary = elite_df.groupby("Department").Revenue.mean().sort_values(ascending = False)
print(f"average salary per department:", avg_salary)