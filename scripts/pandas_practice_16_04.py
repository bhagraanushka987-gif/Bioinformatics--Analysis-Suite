"""
PANDAS DATA IMPUTATION & LAB LOGISTICS - DAY 04
Focus: Missing Value Handling (Fillna), Type Casting, and Deque Operations
Project: Student Records, Regional Sales, and Gene Docking Strength
"""
import pandas as pd
# ==========================================
# SECTION 1: DATA CLEANING & TYPE CONVERSION
# ==========================================
data = {'name': ['Anushka', 'Priya', 'Riya', 'Sneha'],
        'age': [22, None, 25, None],
        'marks': [91, 85, None, 78]}
df = pd.DataFrame(data)
# Imputing missing age with the mean and filling marks with zero
df["age"] = df["age"].fillna(df["age"].mean())
#print(f"filling the missing age in the column of age:", missing_age)
df["marks"] = df["marks"].fillna(0)
#print(f"filling missing marks with:", missing_marks)
# Converting age to integer for standardized reporting
df["age"] = df["age"].astype(int)
#print(f"converting age into integer:", convert_age)
print(df)

# ==========================================
# SECTION 2: CUSTOMER AGE STANDARDIZATION
# ==========================================
import numpy as np

data = {
    'Customer': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25.0, np.nan, 30.0, np.nan, 22.0]
}
df = pd.DataFrame(data)
# Handling NaN values and casting to int
df["Age"] = df["Age"].fillna(df["Age"].mean())
print("--- Before ---")
print(df)

df["Age"] = df["Age"].astype(int)
print("--- After ---")
print(df)

# ==========================================
# SECTION 3: REGIONAL PERFORMANCE METRICS
# ==========================================
data = {
    'Region': ['North', 'South', 'North', 'East', 'South', 'East'],
    'Salesperson': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Sales': [250, 400, 150, 300, 200, 500]
}
df = pd.DataFrame(data)
# Aggregating sales totals by region
region_total = df.groupby("Region").Sales.sum()
print(f"sum of the sales for each region:", region_total)

# ==========================================
# SECTION 4: LAB TASK MANAGEMENT & GENE ANALYSIS
# ==========================================
from collections import deque

# Initializing the lab task list
# Utilizing Deque for high-efficiency task prioritization
lab_tasks = deque(["Cleaning", "Docking", "Writing"])
lab_tasks.appendleft("Morning Coffee")
# Evaluating Binding Affinity for Pippali Research
df_genes = pd.DataFrame({
    'Gene': ['Pippali_1', 'Pippali_2', 'Pippali_3', 'Pippali_4'],
    'Docking_Score': [-8.2, -7.1, -9.5, -6.8]
})
# Vectorized Boolean comparison for gene strength
df_genes['is_strong'] = df_genes["Docking_Score"] < -7.5
print(df_genes)