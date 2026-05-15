"""
PANDAS RELATIONAL INTEGRATION & METADATA NORMALIZATION - DAY 31
Focus: Vertical Concatenation (Concat), Horizontal Joins (Merge), and Column Refactoring
Project: Clinical Patient Registries, Genomic Mapping, and Pharmaceutical Audits
"""
import pandas as pd
# ==========================================
# SECTION 1: CLINICAL PATIENT REGISTRIES
# ==========================================

# 1.1 Initializing Disparate Patient Cohorts
df1 = pd.DataFrame({'patient': ['Alice', 'Bob', 'Carol'],
                    'age': [25, 32, 28]})

df2 = pd.DataFrame({'patient': ['Dave', 'Eve'],
                    'age': [35, 22]})
# 1.2 Vertical Consolidation: Merging cohorts into a unified registry
# Using reset_index(drop=True) to ensure a continuous index range

joining_both = pd.concat([df1, df2]).reset_index(drop=True)
print(f"joining both the dataframes:{joining_both}")
# 1.3 Label Normalization for Research Clarity
renaming = joining_both.rename(columns={"age":"patient_age"})
print(f"renaming the age column:{renaming}")

# ==========================================
# SECTION 2: GENOMIC EXPRESSION MAPPING
# ==========================================

# 2.1 Experimental Expression Data
df_info = pd.DataFrame({'gene': ['BRCA1', 'TP53', 'EGFR'],
                        'expression': [8.5, 12.3, 6.7]})

df_loc = pd.DataFrame({'gene': ['BRCA1', 'TP53', 'EGFR'],
                       'chromosome': [17, 17, 7]})

# 2.3 Relational Merge: Linking expression levels with chromosomal locations
merging_both = pd.merge(df_info, df_loc, on = "gene")
print(f"merging both the data frames:{merging_both}")
# 2.4 Multi-Column Renaming for Publication Standards
rename = merging_both.rename(columns={"expression":"exp_level", "chromosome":"chrom"})
print(f"renaming both columns:{rename}")

# ==========================================
# SECTION 3: PHARMACEUTICAL PRICE AUDITS
# ==========================================

# 3.1 Initializing Drug Pricing Cohorts
df3 = pd.DataFrame({'drug': ['Aspirin', 'Ibuprofen'],
                    'price': [25, 45]})

df4 = pd.DataFrame({'drug': ['Paracetamol', 'Metformin'],
                    'price': [15, 35]})
# 3.2 Vertical Consolidation: Unified Pharmaceutical Pricing List

joining_both = pd.concat([df3, df4]).reset_index(drop=True)
print(f"joining both the dataframes:{joining_both}")
renamings = joining_both.rename(columns={"price":"drug_price"})
print(f"renaimg the column:{renamings}")

# ==========================================
# SECTION 4: DRUG CATEGORIZATION PIPELINE
# ==========================================

# 4.1 Master Drug Pricing Data
df_drugs = pd.DataFrame({'drug': ['Aspirin', 'Ibuprofen', 'Paracetamol'],
                         'price': [25, 45, 15]})

df_category = pd.DataFrame({'drug': ['Aspirin', 'Ibuprofen', 'Paracetamol'],
                             'category': ['Pain', 'Pain', 'Fever']})
# 4.3 Relational Merge: Enriching prices with therapeutic categories
merge_both = pd.merge(df_drugs, df_category, on = "drug")
print(f"merging both the data fromes into one:{merge_both}")
branding = merge_both.rename(columns={"price":"drug_price", "category":"drug_category"})
print(f"renaming both the columns:{branding}")