"""
BIOCHEMICAL BOUNDARY ANALYSIS & METADATA FILTRATION - DAY 34
Focus: Array-Based Storage Compilation, Multi-Branch Dispersions, and Range Windows
Project: Proteomic Mass Benchmarks, Clinical Condition Classification, and Mutation Audits
"""

# ==========================================
# SECTION 1: AMINO ACID MASS BOUNDARY ANALYSIS
# ==========================================

# 1.1 Initializing Residue Molecular Weights (g/mol)
amino_acids = {'Glycine': 75, 'Alanine': 89, 'Valine': 117, 'Leucine': 131, 'Isoleucine': 131}
heavist_amino_acid = ""
molecular_weight = 0
for amino_acid, weight in amino_acids.items():
    if weight > molecular_weight:
        molecular_weight = weight
        heavist_amino_acid = amino_acid
print(f"the heaviest amino acid and its molecular weight:{heavist_amino_acid} {molecular_weight}")

# ==========================================
# SECTION 2: CLINICAL PATHOLOGICAL CLASSIFICATION
# ==========================================

# 2.1 Quantifying Chronic Condition Prevalence
diseases = {'Diabetes': 'Chronic', 'Flu': 'Acute', 'Cancer': 'Chronic', 'Cold': 'Acute', 'Asthma': 'Chronic'}
count = 0
for disease, serious in diseases.items():
    if serious == "Chronic":
        count += 1
print(f"chronic disease count in the text:{count}")

# ==========================================
# SECTION 3: GENOMIC STRUCTURE THRESHOLD FILTERING
# ==========================================

# 3.1 Screening Targets Exceeding Critical Nucleotide Thresholds (bp)
# Flawless use of array collection to capture multi-hit thresholds!
genes = {'BRCA1': 81189, 'TP53': 19149, 'EGFR': 188307, 'KRAS': 45000, 'MYC': 5919}
gene_name = []
for gene, length in genes.items():
    if length > 40000:
        gene_name.append(gene)
print(f"gene whose length is above 40000:{gene_name}")

# ==========================================
# SECTION 4: REAGENT PROCUREMENT BOUNDARY AUDIT
# ==========================================

# 4.1 Comparative Price Ceiling and Floor Localization
vitamins = {'Vitamin A': 286, 'Vitamin B': 337, 'Vitamin C': 176, 'Vitamin D': 384, 'Vitamin E': 430}
expensive_vitamin = ""
most_expensive = 0
cheapest_vitamin = ""
# Initializing with Infinity to ensure immediate lower boundary capture
most_cheapest = float('inf')
for vitamin, cost in vitamins.items():
    if cost > most_expensive:
        most_expensive = cost
        expensive_vitamin = vitamin
    elif cost < most_cheapest:
        most_cheapest = cost
        cheapest_vitamin = vitamin
print(f"most expensive vitamin:{expensive_vitamin} {most_expensive}")
print(f"cheapest vitamin:{cheapest_vitamin} {most_cheapest}")

# ==========================================
# SECTION 5: MUTATION CLUSTERED BINNING
# ==========================================

# 5.1 Binary Distribution Screening of Clinical Transcripts
mutations = {'BRCA1': 'Pathogenic', 'TP53': 'Benign', 'EGFR': 'Pathogenic', 'KRAS': 'Pathogenic', 'MYC': 'Benign'}
pathogenic_mutations = 0
benign_mutations = 0
for gene, mutation in mutations.items():
    if mutation == "Pathogenic":
        pathogenic_mutations += 1
    else:
        benign_mutations += 1
print(f"counting pathogenic mutations:{pathogenic_mutations}")
print(f"counting bengin mutations:{benign_mutations}")

# ==========================================
# SECTION 6: PROTEOMIC MASS-WINDOW FILTRATION
# ==========================================

# 6.1 Isolating Intermediary Molecular Weight Brackets (Daltons)
proteins = {'Insulin': 5808, 'Hemoglobin': 64500, 'Collagen': 300000, 'Albumin': 66000, 'Myosin': 480000}
protein_name = []
for protein, weight in proteins.items():
    if 50000 < weight < 100000:
        protein_name.append(protein)
print(f"only proteins where molecular weight is between 50000 and 100000:{protein_name}")