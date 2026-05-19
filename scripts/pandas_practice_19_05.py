"""
PANDAS VECTORIZED FILTERING & TARGETED STRATIFICATION - DAY 34
Focus: Bitwise Compound Conditions (&), Set Membership (.isin), and Inclusive Bounds (.between)
Project: Corporate Capital Allocation and Multi-Tissue Transcriptomic Expression Matrices
"""
import pandas as pd
# ==========================================
# SECTION 1: CLINICAL PERSONNEL REGISTRIES
# ==========================================

# 1.1 SETUP: Initializing corporate human capital portfolio
data = {'name': ['Alice', 'Bob', 'Carol', 'Dave', 'Eve'],
        'department': ['Bio', 'Chem', 'Bio', 'Physics', 'Chem'],
        'salary': [55000, 82000, 61000, 47000, 93000]}
df = pd.DataFrame(data)
# 1.2 Categorical Isolation: Filtering strictly for the Chemical sector
dept_chem = df[df["department"] == "Chem"]
print(f"department is chem:{dept_chem}")
# 1.3 Threshold Auditing: High-earning personnel classification (>70,000)
above_salary = df[df["salary"] > 70000]
print(f"salary is above 70000:{above_salary}")
# 1.4 Compound Matrix Slicing: Multi-criteria evaluation using bitwise operators
# Combined constraint requires both Department match AND strict salary threshold
dept_salary = df[(df["department"] == "Bio") & (df["salary"]>58000)]
print(f"filter department is bio and salary is above 58000:{dept_salary}")
# 1.5 Set Membership Mapping: Vectorized retrieval across multiple target categories
dpt = df[df["department"].isin(["Bio", "Chem"])]
print(f"where department is either bio or chem:{dpt}")
# 1.6 Continuous Interval Bracket: Extracting defined compensation bands
salary_between = df[df["salary"].between(55000, 85000)]
print(f"where salary is between 55000 and 85000:{salary_between}")

# ==========================================
# SECTION 2: TRANSCRIPTOMIC TISSUE BIOMARKERS
# ==========================================

# 2.1 SETUP: Initializing tissue-specific quantitative expression matrices
data = {'sample': ['S1', 'S2', 'S3', 'S4', 'S5'],
        'tissue': ['Brain', 'Liver', 'Brain', 'Kidney', 'Liver'],
        'expression': [8.5, 12.3, 6.7, 9.1, 15.2]}
df = pd.DataFrame(data)
# 2.2 Anatomical Location Isolation: Extracting baseline neurology profiles
tissue_brain = df[df["tissue"] == "Brain"]
print(f"where tissue is brain:{tissue_brain}")
# 2.3 Potency Thresholding: Isolating high-expression biomarkers (>10)
exp = df[df["expression"] > 10]
print(f"where expression is above 10:{exp}")
# 2.4 Compound Kinetic Slicing: Liver targets matching strict activation threshold
tissue_exp = df[(df["tissue"] == "Liver") & (df["expression"] > 13)]
print(f"where tissue is liver and expression is above 13:{tissue_exp}")
# 2.5 Set Membership Mapping: Isolating specific tissue lineages concurrently
tissues = df[df["tissue"].isin(["Brain", "Kidney"])]
print(f"where tissue is brain or kidney:{tissues}")
# 2.6 Continuous Range Evaluation: Mid-range expression bracket normalization
exp_btw = df[df["expression"].between(8, 13)]
print(f"where expression is between 8 and 13:{exp_btw}")