

import pandas as pd

# --- TASK 1: SETUP DATA ---
data = {
    'name': ['Alice', 'Bob', 'Carol', 'Dave'],
    'age': [25, None, 30, None],
    'salary': [50000, 40000, None, 35000]
}
df = pd.DataFrame(data)
print("1. Original DataFrame with Missing Values:")
print(df)

print("\n" + "-"*30 + "\n")

# --- TASK 2: HANDLING MISSING AGE ---
# Using your mean logic
missing_age = df['age'].fillna(df['age'].mean())
# Using your integer conversion logic
converting_age = missing_age.astype("int")

print("2. Age column after Mean Imputation and Integer Conversion:")
print(converting_age)

print("\n" + "-"*30 + "\n")

# --- TASK 3: HANDLING MISSING SALARY ---
# Using your 0-fill logic
missing_salary_zero = df['salary'].fillna(0)
# Using your median logic
median_salary = df['salary'].fillna(df['salary'].median())

print("3a. Salary filled with 0:")
print(missing_salary_zero)
print("\n3b. Salary filled with Median:")
print(median_salary)

# --- ANALYST TIP ---
# To make this "complete," you would eventually assign these back:
# df['age'] = converting_age
# df['salary'] = median_salary