
import pandas as pd
import numpy as np
# ==========================================
# SECTION 1: GENOMIC EXPRESSION PROFILING
# ==========================================
data = {'gene': ['BRCA1', 'TP53', 'EGFR', 'KRAS', 'MYC'],
        'expression': [8.5, 12.3, 6.7, 9.1, 15.2],
        'chromosome': [17, 17, 7, 12, 8]}
df = pd.DataFrame(data)
# 1.1 Targeted Chromosomal Filtering (Chromosome 17)
filter_chromosome = df[df["chromosome"] == 17]
print(f"filter where chromosome is 17 in the dataframe:", filter_chromosome)
# 1.2 High-Expression Outlier Detection (> 9)
filter_exp = df[df["expression"] > 9]
print(f"filter where chromosome is above 9:", filter_exp)
# 1.3 Set-Based Filtering (.isin)
# Ideal for selecting multiple specific biological pathways
filter_chrom = df[df["chromosome"].isin([7, 12])]
print(f" filter where chromosome is 7 or 12:", filter_chrom)
# 1.4 Range-Based Filtering (.between)
# Defining a 'Normal Range' for gene expression
filter_between = df[df["expression"].between(8,13)]
print(f"filter where expression is between 8 and 13:", filter_between)
# 1.5 Multi-Condition Logical AND
# Identifying significant expression on specific chromosomes
filter_both = df[(df["chromosome"] == 17) & (df["expression"] > 10)]
print(f"filter where chromosome is 17 and expression above 10:", filter_both)

# ==========================================
# SECTION 2: CLINICAL RISK STRATIFICATION
# ==========================================
data = {
    'Patient': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
    'Age': [45, 32, 60, 25, 55],
    'Blood_Pressure': [130, 115, 145, 110, 140]
}
df = pd.DataFrame(data)

print("--- Raw Records ---")
print(df, "\n")
# Professional Technique: Using .loc for simultaneous filtering and feature selection
# Identifying at-risk patients: Age > 40 AND BP > 125
atrisk_patients = df.loc[(df["Age"] > 40) & (df["Blood_Pressure"] > 125),["Patient", "Blood_Pressure"]]
print(f"filtering patients whose age is above 40 and have BP of 125:", atrisk_patients)

# ==========================================
# SECTION 3: MARKET VALUE FILTERING
# ==========================================
data = {
    'Fruit': ['Apple', 'Mango', 'Banana', 'Dragonfruit'],
    'Price': [20, 80, 15, 120]
}
df = pd.DataFrame(data)
# Feature selection for high-value inventory
expensive_list = df.loc[df['Price'] >50, ["Fruit", "Price"]]
print(f"filter fruits whose price is above 50:", expensive_list)