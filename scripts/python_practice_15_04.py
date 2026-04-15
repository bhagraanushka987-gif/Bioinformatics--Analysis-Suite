"""
ADVANCED PYTHON DATA PROCESSING - DAY 03
Focus: Dictionary Filtering, String Parsing, and List Integrity
Project: Academic Scoring, Geographical Data Cleaning, and Metadata Extraction
"""

# ==========================================
# SECTION 1: DICTIONARY FILTERING & AGGREGATION
# ==========================================

# 1.1 Academic Performance Filtering
courses = {'Python': 95, 'SQL': 88, 'Pandas': 72, 'Excel': 45, 'Tableau': 60}
sub_score = []
for subject, score in courses.items():
    if score >70:
        sub_score.append(subject)
print(f"only courses where score is above 70:", sub_score)

# ==========================================
# SECTION 2: STRING NORMALIZATION & DATA CLEANING
# ==========================================
# 2.1 Geographical Data Standardization
cities = ["  SHIMLA  ", "delhi", "  MUMBAI  ", "bangalore", "  CHENNAI  "]
new_list = []
for city in cities:
    new_list.append(city.strip().title())
print(f"new list every city stripped and title case:", new_list)
#Quantitative Analysis: Parity-Based Summation
numbers = [11, 24, 37, 42, 55, 68, 73, 86]
even_num = 0
for number in numbers:
    if number % 2 == 0:
        even_num +=number
print(f" sum of all even numbers:", even_num)
# Delimited String Decomposition
messy_string = "   Apple|||BANANA|||  cherry  |||  DaTe  "
words = messy_string.split("|||")
clean_string = []
for word in words:
    clean_word = word.strip().lower()
    clean_string.append(clean_word)
print(f"clean string with indiviual lowercase:", clean_string)
# ==========================================
# SECTION 3: METADATA EXTRACTION & LIST SECURITY
# ==========================================

# 3.1 Social Media Metadata (Hashtag Extraction)
posts = ["loving the #sunshine today", "my #cat is being weird", "just ate a great #burger"]
new_list = []
for post in posts:
    words = post.split()
    for word in words:
        if word.startswith("#"):
            clean_word = word[1:]
            new_list.append(clean_word)
print(f"extracted hashtags:", new_list)
# 3.2 Research Data Integrity: Deep vs. Shallow Copying
# Ensuring the original gene repository remains untouched
original_genes = ["Pippali", "Adhatoda", "Tulsi"]
backup_genes = original_genes.copy()
backup_genes.append("neem")
print(f"old gene list:", original_genes)