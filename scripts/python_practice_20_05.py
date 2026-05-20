"""
SEQUENCE SANITIZATION & METADATA TOKEN AUDITS - DAY 35
Focus: Chained Method String Normalization, Substring Replacement, and Selective Numeric Accumulation
Project: Genomic Sequence Cleaning, CRISPR Textual Density, and Proteomic Metadata Unification
"""

# ==========================================
# SECTION 1: GENOMIC SEQUENCE SANITIZATION
# ==========================================

# 1.1 Removing Extraneous Whitespace and Enforcing Capitalization
dna_sequences = ["  ATCGGCTA  ", "gctatcga", "  TTAACCGG  ", "ccgaattc", "  AATCGGTA  "]
new_list = []
for sequence in dna_sequences:
    # Chaining strip() and upper() for database standardization compliance
    new_list.append(sequence.strip().upper())
print(f"new list with uppercase and strip:{new_list}")

# ==========================================
# SECTION 2: GENOMIC NOMENCLATURE TEXT MINING (SET A)
# ==========================================
text = "CRISPR is revolutionizing gene editing and CRISPR is used in medicine and CRISPR is powerful"
# 2.1 Quantifying Key Technology Density
count = text.count("CRISPR")
print(f"counting CRISPR in the text:{count}")
# 2.2 Terminology Refactoring: Global Substring Substitution
replacing = text.replace("CRISPR","gene therapy")
print(f"replacing CRISPR with the gene therapy:{replacing}")

# ==========================================
# SECTION 3: NUMERICAL BOUNDARY ISOLATION
# ==========================================
numbers = [12, 45, 23, 67, 89, 34, 56, 11]
# 3.1 Independent Maximum Scan: Finding the highest upper bound
largest_number = numbers[0]
for number in numbers:
    if number > largest_number:
        largest_number = number
print(f"finding the largest number:{largest_number}")
# 3.2 Independent Minimum Scan: Finding the lowest lower bound
smallest_number = numbers[0]
for number in numbers:
    if number < smallest_number:
        smallest_number = number
print(f"finding the smallest number:{smallest_number}")

# ==========================================
# SECTION 4: PROTEOMIC METADATA UNIFICATION
# ==========================================

# 4.1 Case Normalization: Applying Title Case formatting for publication logs
proteins = ["  INSULIN  ", "hemoglobin", "  COLLAGEN  ", "albumin", "  MYOSIN  "]
news_list = []
for protein in proteins:
    news_list.append(protein.strip().title())
print(f"new list for the proteins:{news_list}")

# ==========================================
# SECTION 5: GENOMIC NOMENCLATURE TEXT MINING (SET B)
# ==========================================
text = "bioinformatics is the future and bioinformatics uses python and bioinformatics is growing fast"
# 5.1 Technology Term Frequency Analysis
counting = text.count("bioinformatics")
print(f"counting bioinformatics in the text:{counting}")
# 5.2 Paradigm Shift Substitution: Mapping fields
replace = text.replace("bioinformatics", "data science")
print(f"replacing the bioinformatics with data science:{replace}")

# ==========================================
# SECTION 6: SELECTIVE NUMERICAL ACCUMULATION
# ==========================================

# 6.1 Threshold-Gated Compressions: Accumulating only records exceeding baseline criteria
numbers = [34, 7, 91, 23, 56, 44, 78, 15]
sum_numbers = 0
for number in numbers:
    if number > 40:
        sum_numbers += number
print(f"sum of all the numbers above 40 :{sum_numbers}")
