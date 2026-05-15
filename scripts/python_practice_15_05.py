"""
BIOMOLECULAR AUDITING & SEQUENCE SANITIZATION - DAY 31
Focus: Experimental Success Rates, Protein Mass Extremums, and Genomic Normalization
Project: High-Throughput Screening (HTS) and Proteomic Data Cleanup
"""

# ==========================================
# SECTION 1: EXPERIMENTAL SUCCESS AUDIT
# ==========================================

# 1.1 Quantifying Trial Failure Rates
# Objective: Identify protocol deviations or assay failures in HTS
experiments = {'Exp1': 'Success', 'Exp2': 'Failed', 'Exp3': 'Success', 'Exp4': 'Failed', 'Exp5': 'Success'}
count = 0
for experiment in experiments.values():
    if experiment == "Failed":
        count += 1
print(f"conting experiments which get failed:{count}")

# ==========================================
# SECTION 2: PROTEOMIC MASS BOUNDARIES
# ==========================================

# 2.1 Identifying Extremum Molecular Weights (Daltons)
# Initializing with Infinity to ensure the first real value is captured as the minimum
proteins = {'Insulin': 5808, 'Hemoglobin': 64500, 'Collagen': 300000, 'Albumin': 66000, 'Myosin': 480000}
heaviest_protein = ""
weight_of_heavy_protein = 0
lightest_protein = ""

weight_of_light_protein = float('inf')
for protein, weight in proteins.items():
    if weight > weight_of_heavy_protein:
        weight_of_heavy_protein = weight
        heaviest_protein = protein
    if weight < weight_of_light_protein:
        weight_of_light_protein = weight
        lightest_protein = protein
print(f"the heaviest protein is {heaviest_protein} {weight_of_heavy_protein}")
print(f"the lightest protein is {lightest_protein} {weight_of_light_protein}")

# ==========================================
# SECTION 3: GENOMIC SEQUENCE NORMALIZATION
# ==========================================

# 3.1 Sanitizing Raw Sequence Reads
# Objective: Remove extraneous whitespace and unify case for database compatibility
sequences = ["  ATCG  ", "gcta", "  TTAG  ", "ccga", "  AATC  "]
new_list = []
for sequence in sequences:
    new_list.append(sequence.strip().title())
print(f" new list with strip and title case:{new_list}")

# ==========================================
# SECTION 4: DIAGNOSTIC SAMPLE STRATIFICATION
# ==========================================

# 4.1 Binary Categorization of Clinical Samples
samples = {'S1': 'Positive', 'S2': 'Negative', 'S3': 'Positive', 'S4': 'Positive', 'S5': 'Negative', 'S6': 'Positive'}
count_positive = 0
count_negative = 0
for sample in samples.values():
    if sample == "Positive":
        count_positive += 1
    elif sample == "Negative":
        count_negative += 1
print(f"counting positive sample:{count_positive}")
print(f"counting negative sample: {count_negative}")

# ==========================================
# SECTION 5: ENZYME PROCUREMENT AUDIT
# ==========================================

# 5.1 Financial Boundary Analysis for Reagent Benchmarking
enzymes = {'Amylase': 55000, 'Lipase': 48000, 'Protease': 72000, 'Catalase': 60000, 'Pepsin': 34000}
most_exp = ""
cost_exp = 0
most_cheap = ""
cost_cheap = float('inf')
for enzyme, cost in enzymes.items():
    if cost > cost_exp:
        cost_exp = cost
        most_exp = enzyme
    if cost < cost_cheap:
        cost_cheap = cost
        most_cheap = enzyme
print(f"most expensive enzyme:{most_exp} {cost_exp}")
print(f"most cheap enzyme:{most_cheap} {cost_cheap}")

# ==========================================
# SECTION 6: BIOMOLECULE METADATA UNIFICATION
# ==========================================

# 6.1 Final String Sanitization Pipeline
# Objective: Upper-case normalization for publication-ready figures
words = ["  PROTEIN  ", "lipid", "  CARBOHYDRATE  ", "nucleic acid", "  VITAMIN  "]
news_list = []
for word in words:
    news_list.append(word.strip().upper())
print(f"new_list:{news_list}")
