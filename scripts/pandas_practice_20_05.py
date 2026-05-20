"""
PANDAS FEATURE ENGINEERING & PHENOTYPIC BINNING - DAY 35
Focus: Axis-Oriented Logic Mapping (axis=1), Inline Vectorized Lambdas, and Tiered Discrete Bins
Project: Genomic Abundance Classification and In Vivo Physiological Health Indices
"""
import pandas as pd
# ==========================================
# SECTION 1: GENOMIC TRANSCRIPTION CHARACTERIZATION
# ==========================================

# 1.1 SETUP: Initializing base transcriptomic expression matrices
data = {'gene': ['BRCA1', 'TP53', 'EGFR', 'KRAS', 'MYC'],
        'expression': [8.5, 12.3, 6.7, 9.1, 15.2],
        'chromosome': [17, 17, 7, 12, 8]}
df = pd.DataFrame(data)
# 1.2 Quantitative Abundance Binning: Vectorized threshold categorization
df["exp_category"] = df["expression"].map(lambda p :
    "High" if p > 10 else
    "Low"
)
print(f"finding the highest or low of the expression:{df['exp_category']}")
# 1.3 Structural Chromosomal Slicing: Discrete scale labeling based on locus numbers
df["chrom_type"] = df["chromosome"].map(lambda p :
    "Large" if p > 10 else
    "Small"
)
print(f"finding the largest or smallest of the chromosome:{df['chrom_type']}")

# 1.4 Multi-Tiered Feature Extraction: Row-wise functional tracking
def gene_status(row):
"""
    Evaluates transcript boundaries to map continuous log fold-changes
    into discrete functional activation levels.
    """
    if row['expression'] > 12:
        return "Overexpressed"
    elif row['expression'] > 8:
        return "Normal"
    else:
        return "Underexpressed"
# Executing horizontally across the series matrix via axis=1 configuration
df['status'] = df.apply(gene_status, axis = 1)
print(f"creating new column:{df['status']}")

# ==========================================
# SECTION 2: PHYSIOLOGICAL COHORT PHENOTYPING
# ==========================================

# 2.1 SETUP: Initializing clinical sample homeostatic parameters
data = {'sample': ['S1', 'S2', 'S3', 'S4', 'S5'],
        'ph': [7.4, 6.8, 7.9, 6.2, 8.1],
        'temperature': [37.5, 38.2, 36.8, 39.1, 37.0]}
df = pd.DataFrame(data)
# 2.2 Biochemical Ion Balance Classification: Mapping pH gradients
df["ph_category"] = df["ph"].map(lambda p:
    "Basic" if p > 7.5 else
    "Acidic"
)
print(f"finding the acidic or basic ph of the sample:{df['ph_category']}")
# 2.3 Thermal Homeostasis Profiling: Isolating metabolic shifts
df["temp_category"] = df["temperature"].map(lambda p :
    "High" if p > 38 else
    "Normal"
)
print(f"finding the highest or lowest tempwerature of the sample:{df['temp_category']}")

# 2.4 Cross-Variable Matrix Classification: Cross-referencing multi-feature rules
def health_status(row):
    if row['ph'] > 7.5 and row['temperature'] < 38:
        return "Healthy"
    elif row['temperature'] > 38:
        return "Fever"
    else:
        return "Monitor"
df["status"] = df.apply(health_status, axis =1)
print(f"creating a new column:{df['status']}")