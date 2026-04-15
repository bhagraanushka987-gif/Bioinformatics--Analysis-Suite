"""
PANDAS ADVANCED MANIPULATION - DAY 03
Focus: Grouping, Lambda Operations, and Data Cleaning (Coercion)
Project: Student Analytics, HR Reporting, and Gene Score Normalization
"""
import pandas as pd
# ==========================================
# SECTION 1: STUDENT PERFORMANCE ANALYTICS
# ==========================================
data = {'student': ['Anushka', 'Priya', 'Riya', 'Sneha', 'Tanya'],
        'subject': ['Bio', 'Chem', 'Bio', 'Chem', 'Bio'],
        'marks': [91, 65, 78, 88, 72]}
df = pd.DataFrame(data)
# Aggregation and Sorting Logic
avg_marks = df.groupby("subject").marks.mean()
print(f"average marks per subject:", avg_marks)
sorting = df.sort_values("marks", ascending = False)
print(f"sort highest to lowest:", sorting)
# Multi-Condition Filtering
filter_bio = df[df["subject"] == "Bio"]
print(f"filter rows where subject is bio:", filter_bio)
filter_marks = df[df["marks"] > 75]
print(f"filter where marks are above 75:", filter_marks)
filter_subject = df[(df["subject"] == "Chem") & (df["marks"]>70)]
print(f"Filter rows where subject is Chem AND marks above 70:", filter_subject)
# ==========================================
# SECTION 2: HR DATA MAPPING & TRANSFORMATION
# ==========================================


data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Department Code': ['HR', 'IT', 'IT', 'MKT'],
    'Base Salary': [60000, 75000, 72000, 65000],
    'Bonus Rating': [1.2, 1.0, 1.5, 1.1]
}
df = pd.DataFrame(data)
# Dictionary-Based Mapping
dept_mapping = {
       "HR": "Human Resources",
       "IT": "Information Tech",
      "MKT": "Marketing"
}
df["Department Name"] = df["Department Code"].map(dept_mapping)
print(f"final report:", df["Department Name"])
# Salary Adjustment using Lambda
df["Proposed Salary"] = df["Base Salary"].apply(lambda p: p + 5000)
print(f"new raised salary:", df["Proposed Salary"])


import numpy as np
# ==========================================
# SECTION 3: BIOINFORMATICS - DATA CLEANING
# ==========================================

# Handling non-numeric 'Missing' entries in Gene Docking scores
data = {'Gene': ['A', 'B', 'C', 'D'],
        'Score': ['-8.5', '-9.2', 'Missing', '-7.4']} # 'Missing' is text!
df = pd.DataFrame(data)
# Professional Technique: Coercing errors to NaN for statistical continuity
df["Score"] = pd.to_numeric(df["Score"], errors = "coerce")
mean_score = df["Score"].mean()
print(f"average score of genes:", mean_score)