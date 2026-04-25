"""
TEMPORAL DATA PROCESSING & OMICS NORMALIZATION - DAY 11
Focus: Datetime Parsing (strptime), Longitudinal Filtering, and Parity Summation
Project: Pharmaceutical Inventory, Omics Registry, and User Adoption Trends
"""
# ==========================================
# SECTION 1: PHARMACEUTICAL & OMICS METRICS
# ==========================================

# 1.1 Pharmaceutical Procurement: Identifying Price Extremums
medicines = {'Aspirin': 25, 'Paracetamol': 15, 'Ibuprofen': 45, 'Amoxicillin': 120, 'Metformin': 35}
most_expensive_med = ""
cost_of_med = 0
for medicine, price in medicines.items():
    if price > cost_of_med:
        cost_of_med = price
        most_expensive_med = medicine
print(f"most expensive medicine and its price:", most_expensive_med, cost_of_med)
# 1.2 Quantitative Parity: Odd Integer Accumulation
numbers = [18, 35, 42, 7, 63, 24, 51, 9]
sum_odd_no = 0
for number in numbers:
    if number % 2 != 0:
        sum_odd_no += number
print(f"sum of all odd numbers:",sum_odd_no)
# 1.3 Omics Registry Standardization (Strip & Title Case)
# Standardizing common biological study fields
words = ["  GENOME  ", "proteome", "  TRANSCRIPTOME  ", "metabolome", "  MICROBIOME  "]
new_list = []
for word in words:
    new_list.append(word.strip().title())
print(f"new list:", new_list)

from datetime import datetime
# ==========================================
# SECTION 2: DATETIME PARSING & EXTRACTION
# ==========================================

# 2.1 ISO-Standard Date Extraction (YYYY-MM-DD)
string_dates = ["2019-05-14", "2021-11-01", "2023-01-20"]
start_years = []

for date in string_dates:
    # Converting string to datetime object for chronological logic
    real_date = datetime.strptime(date, "%Y-%m-%d")
    start_years.append(real_date.year)
print(f"start years: {start_years}")

# 2.2 European Format Parsing (DD/MM/YYYY)
eu_dates = ["25/12/2025", "01/01/2026", "15/08/2026"]
months_list = []
for date in eu_dates:
    real_date = datetime.strptime(date, "%d/%m/%Y")
    months_list.append(real_date.month)

print(f"Extracted Months: {months_list}")

# ==========================================
# SECTION 3: INTEGRATED DATA WRANGLING
# ==========================================

# 3.1 Longitudinal Filtering: Identifying Early Adopters
# Logic: Parsing CSV-style strings and filtering by Year

raw_signups = [
    "  alice , 15/04/2023 ",
    "BOB, 22/11/2024",
    " charlie  , 05/01/2022",
    "diana , 30/08/2025"
]
early_users = {}
for signup in raw_signups:
    clear_dates= signup.split(",")
    # Cleaning identity and temporal string
    clean_names = clear_dates[0].strip().title()
    clean_date = clear_dates[1].strip()
    # Casting to Datetime object for comparison
    real_date = datetime.strptime(clean_date, "%d/%m/%Y")
    # Stratification: Isolating users prior to 2024
    if real_date.year < 2024:
        early_users[clean_names] = real_date.month
print(f"early adopter months:{early_users}")
