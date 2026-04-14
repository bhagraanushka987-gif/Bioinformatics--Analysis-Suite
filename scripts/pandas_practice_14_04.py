"""
BIOINFORMATICS DATA MANIPULATION - DAY 02
Focus: Multi-condition Filtering and Thesis-specific Data Labeling
Project: Piper longum (Pippali) Molecular Docking Study
"""
import pandas as pd
# ==========================================
# SECTION 1: CORE PANDAS FILTERING (HR/FINANCE)
# ==========================================
data = {'name': ['Alice', 'Bob', 'Carol', 'Dave', 'Eve'],
        'department': ['HR', 'IT', 'IT', 'HR', 'Finance'],
        'salary': [40000, 85000, 72000, 45000, 60000]}
df = pd.DataFrame(data)
filter_rows = df[df["department"] == "IT"]
print(f"filtering rows where department id IT:", filter_rows)
filter_salary = df[df["salary"]> 60000]
print(f"rows where salary is above 60000:", filter_salary)
filter_department = df[(df["department"] == "HR") & (df['salary']>42000)]
print(f" filter rows where department is HR and salary is above 42000:", filter_department)
filter_departments = df[df["department"].isin(["IT", "Finance"])]
print(f" filter rows where department is IT or Finance:", filter_departments)
filter_salarys = df[df['salary'].between (50000,80000)]
print(f"rows salary is between 50000 and 80000:", filter_salarys)
# ==========================================
# SECTION 2: DEMOGRAPHIC DATASET (DELHI/MUMBAI)
# ==========================================
data = {'name': ['Alice', 'Bob', 'Carol', 'Dave', 'Eve'],
        'city': ['Delhi', 'Mumbai', 'Delhi', 'Chennai', 'Mumbai'],
        'age': [25, 32, 28, 35, 22]}
df = pd.DataFrame(data)
filter_city = df[df["city"] == "Delhi"]
print(f"rows where city is delhi:", filter_city)
filter_age = df[df["age"] > 27]
print(f"rows where age is avove 27:", filter_age)
filter_rows = df[(df["city"] == "Mumbai") & (df["age"] <30)]
print(f"rows where city is Mumbai AND age below 30:", filter_rows)
city_rows = df[df["city"] .isin(["Delhi", "Chennai"])]
print(f"rows where city is delhi or chennai", city_rows)
filter_ages = df[df["age"].between(25,32)]
print(f" rows where age is between 25 and 32:", filter_ages)
# ==========================================
# SECTION 3: THESIS RESEARCH - PIPER LONGUM DOCKING
# ==========================================
df = pd.DataFrame({
    'gene': ['Pippali_1', 'Pippali_2', 'Adhatoda_1'],
    'docking_score': [-7.2, -8.1, -6.5],
    'status': ['Pending', 'Pending', 'Pending']
})
# PROFESSIONAL TIP: Using .loc for direct dataframe modification
# Logic: If binding affinity (docking_score) is strong (below -7.0), mark as complete.
changing = df.loc[df["docking_score"] < -7.0, "status"] = "complete"
print(f"changing status :", changing)


