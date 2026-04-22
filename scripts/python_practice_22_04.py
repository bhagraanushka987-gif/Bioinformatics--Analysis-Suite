"""
BIO-STATISTICAL LOGIC SUITE
Focus: Iterative Maximums, Feature Filtering, and Dictionary Safety
Project: Protein Molecular Weights, Gene Length Analysis, and Sample Verification
"""

# ==========================================
# SECTION 1: PROTEOMICS & GENOMIC METRICS
# ==========================================

# 1.1 Identifying the Largest Macro-molecule
proteins = {'Hemoglobin': 64500, 'Insulin': 5808, 'Collagen': 300000, 'Myosin': 480000, 'Albumin': 66000}
largest_proteins = ""
molecular_weight = 0
for protein, weight in proteins.items():
    if weight > molecular_weight:
        molecular_weight = weight
        largest_proteins = protein
print(f"largest protein by molecular weight is:", largest_proteins)

# 1.2 Genomic Stratification by Length
genes = {'BRCA1': 81189, 'TP53': 19149, 'EGFR': 188307, 'KRAS': 45000, 'MYC': 5919}
gene_length = []
for gene,length in genes.items():
    if length > 20000:
        gene_length.append(gene)
print(f"only genes where length is above 20000:", gene_length)

# ==========================================
# SECTION 2: LABORATORY LOGISTICS & INVENTORY
# ==========================================

# 2.1 Diagnostic Result Aggregation
samples = {'Sample1': 'Positive', 'Sample2': 'Negative', 'Sample3': 'Positive', 'Sample4': 'Negative', 'Sample5': 'Positive'}
count = 0
for sample, result in samples.items():
    if result == "Positive":
        count += 1
print(f"counting samples which are positive:", count)
# 2.2 Budget-Driven Inventory Selection
menu = {'Burger': 8, 'Fries': 3, 'Steak': 25, 'Soda': 2, 'Salad': 12}
new_dict = {}
for food, price in menu.items():
    if price < 10:
        new_dict[food] = price
print(f"new dictionary where price is less than 10:", new_dict)

# ==========================================
# SECTION 3: DATA INTEGRITY & ERROR HANDLING
# ==========================================

# 3.1 Dictionary Safety: Utilizing .get() for Robust Retrieval
# This prevents KeyError when querying missing keys in genomic databases
gene_status = {"Gene_1": "Verified", "Gene_5": "In-Review"}
# Try to get Gene_10 safely
status_check = gene_status.get("Gene_10", "Pending")
print(f"Gene_10 Status: {status_check}")
