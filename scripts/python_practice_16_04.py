"""
ADVANCED PYTHON DATA PARSING - DAY 04
Focus: Word Frequency Mapping, String Manipulation, and Memory Identity
Project: Academic Filtering, Text Mining, and Genomic Sequence Integrity
"""

# ==========================================
# SECTION 1: DICTIONARY FILTERING & ANALYSIS
# ==========================================

# 1.1 Academic Performance Assessment
scores = {'Biology': 92, 'Chemistry': 68, 'Physics': 85, 'Maths': 45, 'English': 78}
subject_score = []
for subject, marks in scores.items():
    if marks > 75:
        subject_score.append(subject)
print(f"subject where score is above 75:", subject_score)

# ==========================================
# SECTION 2: TEXT MINING & NORMALIZATION
# ==========================================

# 2.1 Keyword Frequency and Content Substitution
text = "bioinformatics is the future of biology and bioinformatics is growing fast"
counting = text.count("bioinformatics")
print(f"counting bioinformatics appear in text:", counting)
replacing = text.replace("bioinformatics", "data science")
print(f"replacing words in sentence:", replacing)
# 2.2 String Sanitization and Title Case Formatting
names = ["  ANUSHKA  ", "priya", "  RIYA  ", "sneha", "  TANYA  "]
new_list = []
for name in names:
    new_list.append(name.strip().title())
print(f" creating a new list:", new_list)
# 2.3 Frequency Mapping (Word Count Algorithm)
messages = "Hello there hello how are you are you ready"
words = messages.split()
word_counts ={}
for word in words:
    clean_word = word.lower()
    if clean_word in word_counts:
        word_counts[clean_word] +=1
    else:
        word_counts[clean_word] =1
print(f"word count for the text:", word_counts)
# ==========================================
# SECTION 3: FUNCTIONAL LOGISTICS & MEMORY
# ==========================================

# 3.1 Inventory Procurement Logic
inventory = {'Apples': 12, 'Bananas': 0, 'Oranges': 5, 'Grapes': 0, 'Mangoes': 2}
def get_empty_stock(inv_dict):
    out_of_stock = []
    for fruit, stock in inventory.items():
        if stock == 0:
            out_of_stock.append(fruit)

    return out_of_stock
result = get_empty_stock(inventory)
print(f"items to reorder:", result)
# 3.2 Genomic Sequence Integrity: Equality vs. Identity
# Comparing base pairs for logical match vs. physical memory location
sequence_1 = ["A", "T", "G"]
sequence_2 = sequence_1.copy()
# Checking Value Equality (Are the letters the same?)
if sequence_1 == sequence_2:
    print("the sequence is same")
else:
    print("the letters are different")
# Checking Reference Identity (Are they the same physical object in RAM?)
if sequence_1 is sequence_2:
    print("they are same physical object")
else:
    print("but stored in differnent places")

