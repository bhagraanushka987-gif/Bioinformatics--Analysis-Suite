"""
BIO-DATA WRANGLING & STRING PARSING - DAY 09
Focus: String Normalization (.upper/.lower), Extremum Search, and Data Cleaning
Project: Genomic ID Standardization, Linguistic Analysis, and Student Performance
"""

# ==========================================
# SECTION 1: GENOMIC & LINGUISTIC PROCESSING
# ==========================================

# 1.1 Standardizing Genomic Identifiers (Strip & Uppercase)
genes = ["  BRCA1  ", "tp53", "  EGFR  ", "kras", "  MYC  "]
new_list = []
for gene in genes:
    new_list.append(gene.strip().upper())
print(f"new list with uppercase:", new_list)

# 1.2 Linguistic Analysis: Term Frequency and Pivot
text = "python is used in bioinformatics and python is used in data science and python is powerful"
counting = text.count("python")
print(f"counting python in text:", counting)
# Transitioning technology context (Python to R)
replacing = text.replace("python", "R")
print(f"replacing python to R:", replacing)

# ==========================================
# SECTION 2: QUANTITATIVE EXTREMUMS
# ==========================================

# 2.1 Identifying Range Boundaries
numbers = [23, 56, 11, 78, 42, 95, 34, 67]
largest_number = numbers[0]
for number in numbers:
    if number > largest_number:
        largest_number = number
print(f"largest number in the list:", largest_number)
smallest_number = numbers[0]
for number in numbers:
    if number < smallest_number:
        smallest_number = number
print(f"smalllest number in the list:", smallest_number)

# ==========================================
# SECTION 3: RAW DATA SANITIZATION
# ==========================================

# 3.1 Tag Cleanup: Handling Delimited Messy Strings
raw_tags_string = "  pyThon , panDas,  NUMpy ,  DaTa  "
clean_tags = []
tags = raw_tags_string.split(',')
for tag in tags:
    clean_tags.append(tag.strip().lower())
print(f"cleaning the messy data:", clean_tags)

# 3.2 Automated Registry: Parsing Multi-Value Strings
# Identifying top-tier performance from raw CSV-style data
raw_data = ["  Alice , 85", "Bob, 95 ", "  Charlie, 100", "Diana , 88  "]
top_students = {}
for data in raw_data:
    parts= data.split(',')
    name = parts[0].strip()
    score = int(parts[1])
    if score > 90:
        top_students[name] = score
print(f"top scoring students in list:",top_students)

