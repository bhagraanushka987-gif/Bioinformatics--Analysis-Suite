"""
PANDAS PERFORMANCE METRICS & STRATIFIED FILTERING - DAY 14
Focus: .loc Operator, Boolean Indexing (.isin, .between), and Ratio Engineering
Project: Academic Salaries, HR Performance, and Social Media Engagement
"""
import pandas as pd

# ==========================================
# SECTION 1: ACADEMIC SALARY STRATIFICATION
# ==========================================
data = {'name': ['Alice', 'Bob', 'Carol', 'Dave', 'Eve'],
        'department': ['Bio', 'Chem', 'Bio', 'Physics', 'Chem'],
        'salary': [55000, 82000, 61000, 47000, 93000]}
df = pd.DataFrame(data)
# 1.1 Targeted Departmental Filtering
filter_dept = df[df["department"]== "Bio"]
print(f"filtering rows where department is bio:", filter_dept)
filter_rows = df[df["salary"] > 60000]
print(f"filter rows where salary is above 60000:", filter_rows)
# 1.2 Multi-Condition Logical AND
# Isolating high-earning Chemistry personnel
filter_both = df[(df["department"] == "Chem") & (df["salary"] > 85000)]
print(f"filter rows where departmenr is chemand salary is above 85000:", filter_both)
# 1.3 Advanced Set & Range Filtering (.isin, .between)
# Filtering for multiple core departments
filter_department = df[df["department"].isin(["Bio", "Chem"])]
print(f"filtering department based on two subjects:", filter_department)
# Identifying salary within a specific research grant range
filter_salary = df[df["salary"].between(50000, 85000)]
print(f"filtering salary:", filter_salary)

# ==========================================
# SECTION 2: HR PERFORMANCE STRATIFICATION
# ==========================================
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'IT'],
    'Performance': [90, 88, 75, 95, 92]
}
df = pd.DataFrame(data)

print("--- Raw HR Data ---")
print(df, "\n")

# 2.1 Identifying Bonus Candidates using .loc
# Professional habit: Using .loc for explicit label-based indexing
bonus_df = df.loc[(df["Department"] == "IT") & (df["Performance"] > 85)]
print(f"bonus to the soecific list of people:{bonus_df}")

# ==========================================
# SECTION 3: SOCIAL MEDIA ENGAGEMENT ANALYSIS
# ==========================================

data = {
    'Post_ID': ['P1', 'P2', 'P3', 'P4', 'P5'],
    'Post_Type': ['Video', 'Image', 'Video', 'Text', 'Video'],
    'Views': [10000, 8000, 20000, 3000, 5000],
    'Likes': [1500, 400, 2000, 100, 1000]
}
df = pd.DataFrame(data)

print("--- Raw Social Media Data ---")
print(df, "\n")

# 3.1 Feature Engineering: Engagement Rate Calculation
video_df = df[df["Post_Type"] == "Video"].copy()
print(f"filtering video from the data:{video_df}")
video_df["engagement_rate"] = video_df["Likes"]/video_df["Views"]
print(f"calculating the engagement pf post:video_df{"engagement_rate"}")
# 3.2 Ranking Video Content by Performance
sorting = video_df.sort_values("engagement_rate", ascending = False)
print(f"sorting from highest to lowest:{sorting}")

# ==========================================
# SECTION 4: INVENTORY PROFITABILITY (GOLDEN GOOSE)
# ==========================================

data = {
    'Product_ID': ['SKU1', 'SKU2', 'SKU3', 'SKU4', 'SKU5'],
    'Category': ['Clothing', 'Tech', 'Tech', 'Clothing', 'Tech'],
    'Rating': [4.8, 3.9, 4.9, 4.1, 4.7],
    'Cost': [10, 50, 200, 15, 120],
    'Price': [25, 90, 350, 30, 250]
}
df = pd.DataFrame(data)

print("--- Raw Inventory Data ---")
print(df, "\n")
# 4.1 Stratification: High-Rated Tech Assets
# Filtering for Category and Rating thresholds simultaneously
golden_goose_df = df.loc[(df["Category"] == "Tech") & (df["Rating"] > 4.5)].copy()
print(f"filtering the data based on category and rating:{golden_goose_df}")
# 4.2 Profit Margin Engineering
golden_goose_df["Profit"] = golden_goose_df["Price"] - golden_goose_df["Cost"]
print(f"calculating profut from the data frame:{golden_goose_df["Profit"]}")
# 4.2 Profit Margin Engineering
sorting_data = golden_goose_df.sort_values("Profit", ascending = False)
print(f"sorting values highest_from lowest:{sorting_data}")