"""
BIO-DATA SANITIZATION & LOGISTICS AUTOMATION - DAY 15
Focus: Sequence Normalization, Range Extremums (Min/Max), and String Refactoring
Project: DNA Sequence Cleanup, Clinical Email Registry, and Server Infrastructure Audit
"""

# ==========================================
# SECTION 1: GENOMIC & QUANTITATIVE AUDITS
# ==========================================

# 1.1 DNA Sequence Normalization
# Cleaning raw sequence reads for downstream bioinformatics tools
sequences = ["  ATCG  ", "gcta", "  TTAG  ", "ccga", "  AATC  "]
new_list = []
for sequence in sequences:
    # Standardizing for unique database indexing (Strip & Uppercase)
    new_list.append(sequence.strip().upper())
print(f"creating a new list cleaning the messy data:", new_list)
# 1.2 Parity Aggregation: Summation of Even Observations
numbers = [33, 8, 71, 44, 19, 56, 82, 27]
sum_even = 0
for number in numbers:
    if number % 2 == 0:
        sum_even += number
print(f"sum of all even numbers in the squence:", sum_even)
# 1.3 Extremum Detection: Identifying Boundary Values
# Professional approach to finding Min and Max in a dataset
numbers = [12, 45, 23, 67, 34, 89, 56, 11]
largest_number = numbers[0]
for number in numbers:
    if number > largest_number:
        largest_number = number
print(f"largest number in the sequencce:", largest_number)
smallest_number = numbers[0]
for number in numbers:
    if number < smallest_number:
        smallest_number = number
print(f"smallest number in the list is:", smallest_number)
# ==========================================
# SECTION 2: MARKETING & COMMUNICATION REFACTORING
# ==========================================

# 2.1 Promo Code Sanitization: Removing Hyphens & Normalizing Case
messy_codes = ["  save20 ", "WINTER-sale", "  halfOFF ", "SPRinG-break  "]
clean_codes = []
for code in messy_codes:
    # Logic: Remove dashes and unify case for database looku
    clear_code = code.strip().replace("-", "")
    clean_codes.append(clear_code.upper())
print(f"cleaned promo codes:{clean_codes}")
# 2.2 Clinical Email Registry: Lowercase Normalization
messy_emails = [" ALICE@gmail.com", "bob@YAHOO.com ", "  CHARLIE@hotmail.com  "]
valid_emails = []

for email in messy_emails:
    valid_emails.append(email.strip().lower())
print(f"clenaned data:{valid_emails}")

# ==========================================
# SECTION 3: SYSTEM INFRASTRUCTURE AUDIT
# ==========================================

# 3.1 Server Identity Normalization: Character Pivot (Hyphen to Underscore)
raw_server_logs = ["  srv-delta01 ", "SRV-alpha99  ", "  srv-omega55"]
quarantined_servers = []

for log in raw_server_logs:
    # Logic: Convert to uppercase and use underscores for POSIX compatibility
    quarantined_servers.append(log.strip().replace("-", "_").upper())
print(f"fully cleaned data:{quarantined_servers}")