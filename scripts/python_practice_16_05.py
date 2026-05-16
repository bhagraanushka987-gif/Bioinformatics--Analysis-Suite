"""
BIOMEDICAL LOGIC, PARITY AGGREGATION, AND STATE MUTATION - DAY 32
Focus: Dual Boundary Traversal, Parity Partitioning, Exception-Lite Sanitization, and Dictionary State Mutation
Project: Hematological Cell Count Audits, Textual Nomology, and Commercial Logistics Tracking
"""

# ==========================================
# SECTION 1: HEMATOLOGICAL AUDITING
# ==========================================

# 1.1 Dual-Extremum Optimization: Identifying Cell Population Boundaries
cell_counts = {'RBC': 5000000, 'WBC': 7000, 'Platelets': 250000, 'Neutrophils': 4000, 'Lymphocytes': 2000}
highest_count = 0
cell_name = ""
lowest_count = float('inf')
cells_name = ""
# Initializing with Infinity to guarantee the first comparison establishes the lower bound
for cell, count in cell_counts.items():
    if count > highest_count:
        highest_count = count
        cell_name = cell
    if count < lowest_count:
        lowest_count = count
        cells_name = cell
print(f"highest cell count:{cell_name}  {highest_count}")
print(f"lowest cell count:{cells_name} {lowest_count}")

# ==========================================
# SECTION 2: TEXTUAL NOMENCLATURE FREQUENCY
# ==========================================

# 2.1 Quantifying Domain-Specific Term Density
text = "protein folding is complex and protein folding causes diseases and protein folding is studied worldwide"
count = text.count("protein folding")
print(f"counting protein folding in the text:{count}")

# ==========================================
# SECTION 3: PARITY PARTITIONING SUMS
# ==========================================

# 3.1 Separate Accumulation of Even and Odd Metrics
numbers = [45, 12, 78, 33, 91, 56, 24, 67]
even_numbers = 0
odd_numbers = 0
for number in numbers:
    if number % 2 == 0:
        even_numbers += number
    else:
        odd_numbers += number
print(f"sum of all even numbers:{even_numbers}")
print(f"sum of all odd numbers:{odd_numbers}")

# ==========================================
# SECTION 4: IDENTITY SANITIZATION PIPELINE
# ==========================================

# 4.1 String Normalization: Removing Extraneous Spacing and Enforcing Lowercase
raw_emails = [" ALICE@gmail.com", "bob@YAHOO.com ", "  CHarlie@Hotmail.com"]
# 1. Set up your empty list
clean_emails = []

for email in raw_emails:
    clean_emails.append(email.strip().lower())
print(f"cleaned database:{clean_emails}")

# ==========================================
# SECTION 5: CONDITIONAL TAX COEFFICIENT SCALING
# ==========================================

# 5.1 Category-Specific Financial Engineering
shopping_cart = [
    {"name": "Laptop", "price": 1000.0, "category": "Electronics"},
    {"name": "Apple", "price": 2.0, "category": "Food"},
    {"name": "Headphones", "price": 150.0, "category": "Electronics"},
    {"name": "Book", "price": 20.0, "category": "Books"}
]

# 1. Set up your total_cost variable
total_cost = 0.0

for item in shopping_cart:
    if item["category"] == "Electronics":
        total_cost += item["price"] * 1.1
    else:
        total_cost += item["price"]
print(f"final cart total:{total_cost}")

# ==========================================
# SECTION 6: DYNAMIC DICTIONARY STATE MUTATION
# ==========================================

# 6.1 Event-Driven Depletion of Asset Stock
# Starting Data
inventory = {"Laptops": 10, "Monitors": 25, "Keyboards": 15}
sales = ["Monitors", "Laptops", "Monitors", "Monitors", "Keyboards", "Laptops"]

for item in sales:
# Mutating the value bound to the active key iteratively
    inventory[item] -= 1
print(f"end of day inventory:{inventory}")