"""
PANDAS DATA NORMALIZATION & CATEGORICAL MAPPING - DAY 15
Focus: .map() for Dictionary Translation, .apply() for Row-wise Logic, and String Sanitization
Project: Genomic Expression Profiling, CRM Subscriber Audits, and Inventory Management
"""
import pandas as pd
# ==========================================
# SECTION 1: GENOMIC EXPRESSION PROFILING
# ==========================================
data = {'gene': ['BRCA1', 'TP53', 'EGFR', 'KRAS', 'MYC'],
        'expression': [8.5, 12.3, 6.7, 9.1, 15.2]}
df = pd.DataFrame(data)
# 1.1 Binary Stratification: High vs. Low Expression via Lambda Map
exp_level = df["expression"].map(lambda p :
    "High" if p > 10 else
    "Low"
)
print(f"checking the expression of each gene if its high or low:", exp_level)
# 1.2 Metadata Normalization: Title Case Conversio
gene_title = df["gene"].map(lambda p : p.title())
print(f"title case of the genes:", gene_title)
# 1.3 Longitudinal Classification: Multi-tier Biological Status
def classify(row):
    if row['expression'] > 12:
        return "Overexpressed"
    elif row['expression'] > 8:
        return "Normal"
    else:
        return "Underexpressed"
# Applying row-wise logic across the 'expression' axis
df["status"] = df.apply(classify, axis="columns")
print(f"new column:", df["status"])

# ==========================================
# SECTION 2: USER TIER & IDENTITY MAPPING
# ==========================================
data = {
    'User': ['JOHN_doe', 'jane_SMITH', 'bob_JOHNSON'],
    'Tier': ['G', 'S', 'B'],
    'Spend': [120.50, 45.00, 210.75]
}
df = pd.DataFrame(data)

print("--- Raw User Data ---")
print(df, "\n")
# 2.1 Dictionary-Based Categorical Translation
tier_dict = {"G":"Gold", "S":"Silver", "B":"Bronze"}
df["Tier"] = df["Tier"].map(tier_dict)
print(f"replacing the letters with full words:{df["Tier"]}")
# 2.2 Identity Standardization: Lowercase Normalization
df["user_name"] = df["User"].apply(lambda p :p.lower())
print(f"updating the column:{df["user_name"]}")

# ==========================================
# SECTION 3: INVENTORY STATUS NORMALIZATION
# ==========================================

data = {
    'SKU': ['sku-101', 'sku-202', 'sku-303'],
    'Status': ['A', 'I', 'O'],
    'Price': [15.99, 24.50, 9.99]
}
df = pd.DataFrame(data)

print("--- Raw Inventory Data ---\n", df, "\n")
# 3.1 Status Code Expansion
status_dict = {"A":"Active", "I":"Inactive", "O":"Out of stock"}
df["Status"] = df["Status"].map(status_dict)
print(f"cleaned data with column with fill words:{df["Status"]}")
# 3.2 SKU Normalization: Uppercase Transformation
upper_sku = df["SKU"].apply(lambda p : p.upper())
print(f"upper casing the whole column:{upper_sku}")

# ==========================================
# SECTION 4: CRM SUBSCRIBER SANITIZATION
# ==========================================
data = {
    'Customer_ID': ['C-101', 'C-102', 'C-103', 'C-104'],
    'Sub_Status': ['Y', 'N', 'Y', 'Y'],
    'Promo_Code': ['  save50 ', 'welcome  ', '  FALL20', '  spring30  ']
}
df = pd.DataFrame(data)

print("--- Raw CRM Data ---")
print(df, "\n")
# 4.1 Subscription Logic Mapping
sub_status_dict = {"Y":"Active", "N":"Cancele"}
df["Sub_Status"] = df["Sub_Status"].map(sub_status_dict)
print(f"cleaned data = {df["Sub_Status"]}")
# 4.2 Promo Code Sanitization: Strip & Uppercase Pipeline
df["Promo_Code"] = df["Promo_Code"].apply(lambda p : p.strip().upper())
print(f"upper casing the promo code:{df["Promo_Code"]}")