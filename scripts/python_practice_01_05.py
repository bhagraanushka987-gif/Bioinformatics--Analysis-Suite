"""
BIO-LOGIC & DICTIONARY COMPREHENSIONS - DAY 17
Focus: Dictionary Iteration, Extremum Detection, and Conditional Comprehensions
Project: Genomic Role Audits, Clinical VIP Mapping, and Performance Tracking
"""

# ==========================================
# SECTION 1: GENOMIC & QUANTITATIVE AUDITS
# ==========================================

# 1.1 Null-Value Detection in Experimental Samples
samples = {'Sample1': 0, 'Sample2': 45, 'Sample3': 0, 'Sample4': 78, 'Sample5': 0}
count = 0
for sample, value in samples.items():
    if value == 0:
        count += 1
print(F"counting sample having 0 value:{count}")
# 1.2 Boundary Value Detection: Min/Max Range
numbers = [15, 28, 43, 62, 71, 34, 89, 56]
largest_number = numbers[0]
smallest_number = numbers[0]
for number in numbers:
    if number > largest_number:
        largest_number = number

    if number < smallest_number:
        smallest_number = number
print(f"smallest number in sequence:{largest_number, smallest_number}")
# 1.3 Pathological Role Classification
# Categorizing 22-gene targets by functional oncogenic activity
genes = {'BRCA1': 'Tumor Suppressor', 'TP53': 'Tumor Suppressor', 'EGFR': 'Oncogene', 'KRAS': 'Oncogene', 'MYC': 'Oncogene'}
count = 0
for gene, role in genes.items():
    if role == "Oncogene":
        count += 1
print(f"counting genes which are oncogenes:{count}")

# ==========================================
# SECTION 2: ADVANCED DICTIONARY COMPREHENSIONS
# ==========================================

# 2.1 Financial Stratification: VIP Mapping

customer_spend = {
    "Alice": 1200,
    "Bob": 450,
    "Charlie": 2500,
    "David": 800
}
# Professional shorthand for creating a filtered sub-dictionary
# Syntax: {key: value for item in iterable if condition}
vip_customers = {name: amount for name, amount in customer_spend.items()if amount > 1000}
print(f"VIPlist:{vip_customers}")
# 2.2 Performance Metrics: Bonus Eligibility
performance_scores = {
    "Alice": 95,
    "Bob": 72,
    "Charlie": 91,
    "David": 85,
    "Eve": 99
}

bonus_list = {name: score for name, score in performance_scores.items()if score >= 90}
print(f"bonus list:{bonus_list}")

