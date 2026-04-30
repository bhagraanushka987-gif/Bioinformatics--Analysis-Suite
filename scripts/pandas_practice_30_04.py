"""
PANDAS DATA IMPUTATION & TYPE CASTING - DAY 16
Focus: Handling NaN (Missing Values), Statistical Filling (Mean/Median), and Integer Casting
Project: Laboratory Sample Audits, Warehouse Logistics, and Fraud Detection
"""
import pandas as pd
# ==========================================
# SECTION 1: LABORATORY SAMPLE AUDIT
# ==========================================
data = {'sample': ['S1', 'S2', 'S3', 'S4'],
        'temperature': [37.5, None, 38.2, None],
        'ph': [7.4, 6.8, None, 7.1]}
df = pd.DataFrame(data)
# 1.1 Statistical Imputation: Filling gaps with Mean and Median
# Using Mean for temperature and Median for pH to maintain data distribution
df["temperature"] = df["temperature"].fillna(df["temperature"].mean())
df["ph"] = df["ph"].fillna(df["ph"].median())
# 1.2 Type Casting: Converting temperature to integer for discrete analysis
df["temperature"] = df["temperature"].astype(int)
print(df)


import numpy as np
# ==========================================
# SECTION 2: WAREHOUSE & SENSOR LOGISTICS
# ==========================================

# 2.1 Warehouse Inventory Recovery
data = {
    'SKU': ['A100', 'B200', 'C300', 'D400'],
    'Quantity': [15.0, np.nan, 22.0, np.nan] # np.nan creates a true "missing" value
}
df = pd.DataFrame(data)

print("--- Raw Warehouse Data ---")
print(df, "\n")
# Defaulting missing quantities to zero and normalizing to integers
df["Quantity"] = df["Quantity"].fillna(0).astype(int)
print(f"filling none value with 0:{df["Quantity"]}")

# 2.2 Industrial Sensor Error Correction
data = {
    'Machine_ID': ['M-1', 'M-2', 'M-3', 'M-4'],
    'Error_Count': [np.nan, 5.0, np.nan, 2.0]
}
df = pd.DataFrame(data)

print("--- Raw Sensor Data ---")
print(df, "\n")
# Assuming no error count (0) where data was not recorded
df["Error_Count"] = df["Error_Count"].fillna(0).astype(int)
print(f"corrected data:{df['Error_Count']}")

# ==========================================
# SECTION 3: FRAUD ANALYTICS & NORMALIZATION
# ==========================================

data = {
    'Email': ['  ADMIN@bank.com', 'user22@YAHOO.com  ', '  CEO@corp.com  '],
    'Account_Type': ['B', 'P', 'B'],
    'Amount': [np.nan, 450.0, np.nan]
}
df = pd.DataFrame(data)

print("--- Raw Fraud Data ---\n", df, "\n")
# 3.1 Financial Imputation: Zero-filling missing transaction amounts
df["Amount"] = df["Amount"].fillna(0).astype(int)
print(f"cleaned data:{df['Amount']}")
# 3.2 Categorical Mapping: Account Type Expansion
account_status = {"B":"Business", "P":"Personal"}
df["Account_Type"] = df["Account_Type"].map(account_status)
print(f"filling the full forms:{df['Account_Type']}")
# 3.3 String Sanitization: Identity Normalization (Strip & Lowercase)
df["Email"] = df["Email"].apply(lambda p: p.strip().lower())
print(f"cleaned email data:{df['Email']}")
