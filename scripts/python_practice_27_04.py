"""
BIO-AUTOMATION & METADATA NORMALIZATION - DAY 13
Focus: Conditional Dictionary Filtering, Linguistic Pivot, and Tracking ID Sanitization
Project: Research Publication Audits and Transactional Logistics
"""

# ==========================================
# SECTION 1: RESEARCH METRICS & LINGUISTICS
# ==========================================

# 1.1 High-Impact Research Filtering
# Isolating fields with > 40 publication hits
research_papers = {'Genomics': 45, 'Proteomics': 28, 'Metabolomics': 63, 'Transcriptomics': 31, 'Bioinformatics': 72}
subject_count = []
for subject, marks in research_papers.items():
    if marks > 40:
        subject_count.append(subject)
print(f"subjects where count is above 40:", subject_count)
# 1.2 Linguistic Analysis: Term Frequency & Modernization
text = "machine learning is transforming healthcare and machine learning is used in drug discovery and machine learning is powerful"
counting = text.count("machine learning")
print(f"counting machine learning in the text:", counting)
# 1.2 Linguistic Analysis: Term Frequency & Modernization
replacing = text.replace("machine learning", "deep learning")
print(f"replacing the text:", replacing)

# ==========================================
# SECTION 2: PARITY & CODE NORMALIZATION
# ==========================================

# 2.1 Quantitative Aggregation: Even Parity Summation
numbers = [17, 42, 8, 63, 25, 54, 31, 76]
sum_even = 0
for number in numbers:
    if number % 2 == 0:
        sum_even += number
print(f"sum of all even numbers:", sum_even)
#2.2 Standardizing Alpha-Numeric Identifiers
raw_codes = ["  aB123 ", "xY987  ", "  Mn456", " qR000  "]
clean_codes = []
for code in raw_codes:
    # Standardizing for unique database indexing (Strip & Uppercase)
    clean_codes.append(code.strip().upper())
print(f"cleaning the messy code:", clean_codes)

# ==========================================
# SECTION 3: RELATIONAL DATA PROCESSING
# ==========================================

# 3.1 VIP Protocol: Attendance Verification from RSVP Data
rsvp_data = [
    {"Name": "Alice", "Status": "Yes"},
    {"Name": "Bob", "Status": "No"},
    {"Name": "Charlie", "Status": "Yes"},
    {"Name": "Diana", "Status": "Pending"}
]
attending_vips = []

for guest in rsvp_data:
    if guest["Status"] == "Yes":
        attending_vips.append(guest["Name"])
print(f"names of vip who are coming:", attending_vips)

# 3.2 Supply Chain Audit: Logistics Tracking Normalization
# Goal: Isolate tracking numbers for Shipped orders and standardize for carrier APIs
order_database = [
    {"Order_ID": 101, "Status": "Pending", "Tracking": "  ab123 "},
    {"Order_ID": 102, "Status": "Shipped", "Tracking": "xy987  "},
    {"Order_ID": 103, "Status": "Shipped", "Tracking": "  mn456"},
    {"Order_ID": 104, "Status": "Canceled", "Tracking": " none "}
]
shipped_tracking = []
for order in order_database:
    if order["Status"] == "Shipped":
        # Extracting and cleaning tracking metadata
        shipped_tracking.append(order["Tracking"].strip().upper())
print(f"cleaning the code:{shipped_tracking}")
