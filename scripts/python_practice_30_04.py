"""
BIO-METADATA TRANSFORMATION & DICTIONARY MAPPING - DAY 16
Focus: High-Throughput Sequence Filtering, Key-Value Pair Construction, and Regex-lite Sanitization
Project: Genomic Length Analysis, HR Roster Management, and Logistics Labeling
"""

# ==========================================
# SECTION 1: GENOMIC & LINGUISTIC AUDITS
# ==========================================

# 1.1 Genomic Scale Filtering
# Identifying significant gene structures based on base-pair length
genes = {'BRCA1': 81189, 'TP53': 19149, 'EGFR': 188307, 'KRAS': 45000, 'MYC': 5919}
gene_list = []
for gene, length in genes.items():
    if length > 50000:
        gene_list.append(gene)
print(f"gene where length is above 50000:{gene_list}")

text = "DNA sequencing is revolutionizing medicine and DNA sequencing is becoming cheaper and DNA sequencing is powerful"
# 1.2 Textual Evolution: Methodology Updates
counting = text.count("DNA sequencing")
print(f"counting number of  appearance of DNA sequence in text:{counting}")
# Methodology Pivot: Modernizing nomenclature
replacing = text.replace("DNA sequencing", "genome analysis")
print(f"replacing text:{replacing}")

# 1.3 Threshold-Based Quantitative Summation
numbers = [23, 56, 11, 78, 42, 95, 34, 67]
sum_number = 0
for number in numbers:
    if number > 50:
        sum_number += number
print(f"sum of all number greater than 50:{sum_number}")

# ==========================================
# SECTION 2: METADATA NORMALIZATION (DICTIONARIES)
# ==========================================

# 2.1 HR Roster Reconstruction
# Converting raw employee list to a Name:Role dictionary with Title Case
raw_hires = [
    {"Name": "  alice smith ", "Role": "admin  "},
    {"Name": "BOB JONES", "Role": "  staff "},
    {"Name": "  charlie brown", "Role": "manager"}
]

clean_roster = {}
for person in raw_hires:
    clean_name = person["Name"].strip().title()
    clean_role = person["Role"].strip().title()
    clean_roster[clean_name] = clean_role
print(f"cleaned data:{clean_roster}")

# 2.2 Support Logic: Category Normalization
raw_tickets = [
    {"Ticket_ID": "T-901", "Category": "  LOGIN_issue  "},
    {"Ticket_ID": "T-902", "Category": " BILLING "},
    {"Ticket_ID": "T-903", "Category": "  password_reset"}
]

clean_queue = {}

for query in raw_tickets:
    # Converting categories to lowercase for system consistency
    clean_category = query["Category"].strip().lower()
    clean_queue[query["Ticket_ID"]] = clean_category
print(f"cleaning the data:{clean_queue}")

# ==========================================
# SECTION 3: LOGISTICS & CHARACTER REFACTORING
# ==========================================

# 3.1 Shipping Label Generation: Multi-Character Cleanup
# Stripping specific symbols (#) and replacing separators (-) for human readability
raw_cart = [
    {"Order_ID": " #1001 ", "Product": "  gaming-LAPTOP  "},
    {"Order_ID": " #1002", "Product": "WIRELESS-mouse "},
    {"Order_ID": "  #1003 ", "Product": "  desk-CHAIR"}
]

shipping_labels = {}

for order in raw_cart:
    # Character pivot: Removing '#' and converting '-' to spaces
    clean_order_id = order["Order_ID"].strip().replace("#", "")
    clean_product = order["Product"].strip().replace("-", " ").title()
    shipping_labels[clean_order_id] = clean_product
print(f"cleaned the raw cart:{shipping_labels}")