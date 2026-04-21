"""
ADVANCED PYTHON LOGIC & DATA INTEGRITY - DAY 07
Focus: Text Mining, Standardized Normalization, and Deep vs. Shallow Copying
Project: Linguistic Analysis, Demographic Registry, and Genomic Data Security
"""

# ==========================================
# SECTION 1: TEXT MINING & NORMALIZATION
# ==========================================

# 1.1 Term Frequency and Refactoring
text = "data analyst is the best career and data analyst earns well and data analyst is growing"
counting = text.count("data analyst")
print(f"counting data analyst in text:", counting)
replacing = text.replace("data analyst", "bioinformatician")
print(f"replacing in the text:", replacing)
# 1.2 Regional Registry Standardization (Strip & Title Case)
names = ["  SHIMLA  ", "delhi", "  CHANDIGARH  ", "mumbai", "  MANALI  "]
new_list = []
for name in names:
    new_list.append(name.strip().title())
print(f"creating a new list:", new_list)

# ==========================================
# SECTION 2: QUANTITATIVE & STRING PARSING
# ==========================================

# 2.1 Numerical Parity Summation
numbers = [13, 26, 41, 58, 33, 72, 19, 84]
even_numbers = 0
for number in numbers:
    if number % 2 == 0:
        even_numbers += number
print(f"sum of all even numbers:", even_numbers)
# 2.2 Character Analysis: Vowel Frequency
quote = "Data Science is AMAZING!"
vowel_count = 0
vowels = "aeiouAEIOU"
for char in quote:
    if char in vowels:
        vowel_count += 1
print(f"counting vowels in the quote:", vowel_count)

# 2.3 Metadata Extraction: Initial Generation
full_names = ["Bruce Wayne", "Clark Kent", "Diana Prince", "Peter Parker"]
initials_list = []
for name in full_names:
    name_parts = name.split()
    first_initial = name_parts[0][0]
    last_initial = name_parts[1][0]
    initials_list.append(first_initial + last_initial)
print(f"initials all all names from the list:", initials_list)

# ==========================================
# SECTION 3: RESEARCH INTEGRITY (DEEP COPYING)
# ==========================================
import copy

# 1. The Nested Data (Score and Energy are in their own sub-list)
original = ["Pippali_A", [-9.1, 42]]

# 2. The Shallow Copy (What we've been using)
shallow = original.copy()

# 3. The Deep Copy (The 'Scientific Grade' Backup)
deep = copy.deepcopy(original)

# --- THE TEST ---
# We change the score in the shallow copy
shallow[1][0] = 0.0

print(f"Original: {original}") # Becomes 0.0! (Data corrupted!)
print(f"Shallow:  {shallow}")  # Becomes 0.0
print(f"Deep:     {deep}")     # STAYS -9.1 (Data safe!)