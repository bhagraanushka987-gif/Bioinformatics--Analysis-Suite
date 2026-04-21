"""
PANDAS RESEARCH ANALYTICS - DAY 07
Focus: Multi-Level Aggregation, Revenue Stratification, and Genomic Vectorization
Project: Academic Performance, Literary Revenue, and 22-Gene Thesis Filtering
"""
import pandas as pd
# ==========================================
# SECTION 1: ACADEMIC PERFORMANCE METRICS
# ==========================================
data = {'category': ['Bio', 'Chem', 'Bio', 'Physics', 'Chem', 'Physics'],
        'marks': [88, 72, 91, 65, 85, 78]}
df = pd.DataFrame(data)
# Cumulative Performance by Category
total_marks = df.groupby("category").marks.sum()
print(f"total marks per category:", total_marks)
sorting = total_marks.sort_values(ascending = False)
print(f"sorting marks highest to lowest:", sorting)
# Statistical Mean: Categorical Assessment
avg_marks = df.groupby("category").marks.mean()
print(f"average marks per category:", avg_marks)
sorting_marks = avg_marks.sort_values()
print(f"sorting avergae marks lowest to highest:", sorting_marks)
# ==========================================
# SECTION 2: REVENUE STRATIFICATION
# ==========================================
data = {
    'Genre': ['Fiction', 'Non-Fiction', 'Fiction', 'Sci-Fi', 'Sci-Fi', 'Non-Fiction'],
    'Title': ['Book A', 'Book B', 'Book C', 'Book D', 'Book E', 'Book F'],
    'Revenue': [1200, 800, 1500, 3000, 500, 950]
}
df = pd.DataFrame(data)

print("--- Raw Data ---")
print(df, "\n")
# Identifying Market Leaders by Genre
total_revenue = df.groupby("Genre").Revenue.sum().sort_values(ascending = False)
print(f"which genre have highest revenue and arranged highest to lowest:", total_revenue)

# ==========================================
# SECTION 3: DEPARTMENTAL SCORE NORMALIZATION
# ==========================================
data = {
    'Department': ['Sales', 'HR', 'Engineering', 'Sales', 'HR', 'Engineering'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Score': [85, 92, 78, 88, 95, 82]
}
df = pd.DataFrame(data)
# Professional Technique: Resetting Index for DataFrame compatibility
avg_score = df.groupby("Department").Score.mean().sort_values(). reset_index
print(f"avergae score by department lowest to highest:", avg_score)

import numpy as np
# ==========================================
# SECTION 4: GENOMIC THESIS AUTOMATION (VECTORIZATION)
# ==========================================

# 4.1 Setup 22-gene research simulated data
# 1. Setup your 22-gene research data
data = {
    'Gene_ID': [f'Gene_{i}' for i in range(1, 23)],
    'Docking_Score': np.random.uniform(-10, -5, 22), # Random scores between -10 and -5
    'Binding_Energy': np.random.uniform(35, 65, 22)   # Random energy between 35 and 65
}
df_genes = pd.DataFrame(data)

# 2. THE "RULER" METHOD (Vectorization)
# We check the whole column at once. It's fast and readable.
strong_and_stable = df_genes[(df_genes['Docking_Score'] < -8.5) &
                             (df_genes['Binding_Energy'] < 45)].copy()

print("--- Filtered Results (Vectorized) ---")
print(strong_and_stable)