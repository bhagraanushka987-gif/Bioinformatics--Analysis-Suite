Python
"""
BIOINFORMATICS DATA ANALYSIS SUITE - DAY 01
Focus: String Manipulation, Data Filtering, and Bioreactor Monitoring
Author: Anushka Bhagra
Date: April 13, 2026
"""

# ==========================================
# SECTION 1: String Cleaning & Normalization
# Goal: Standardize text data (Stripping whitespace and fixing casing).
# ==========================================
words = ["  SHIMLA  ", "delhi", "  MUMBAI  ", "bangalore"]
# Example 1: City List Normalization
new_list = []
for word in words:
     new_list.append(word.strip().title())
print(f"creating new list with title case and stripped:", new_list)
# ==========================================
# SECTION 2: Text Analysis & Transformation
# Goal: Pattern counting and string replacement logic.
# ==========================================
text = "python is great and python is fun and python is powerful"
counting = text.count("python")
print(f"counting python in the lsit:", counting)
replacing_python = text.replace("python", "coding")
print(f"replacing python with coding:", replacing_python)
# ==========================================
# SECTION 3: Mathematical Logic & Filtering
# Goal: Summation of specific data points based on conditions.
# ==========================================
numbers = [15, 3, 42, 8, 27, 61, 9]
# Task: Sum of all odd numbers
odd_numbers = 0
for number in numbers:
    if number % 2 != 0:
        odd_numbers+= number
print(f"sum of all odd numbers:", odd_numbers)
products = {'Apple': 120, 'Banana': 40, 'Cherry': 200, 'Mango': 80}
# Task: Identifying high-cost items
products_above100 = []
for product, cost in products.items():
    if cost > 100:
        products_above100.append(product)
print(f" products which have price above 100:", products_above100)
# Example 2: Email Standardization (Critical for database merging)
emails = ["  ANUSHKA@GMAIL.COM  ", "priya@gmail.com", "  RIYA@YAHOO.COM  ", "sneha@gmail.com"]
new_email = []
for email in emails:
    new_email.append(email.strip().lower())
print(f"new list with email in lowercase:", new_email)

numbers = [4, 9, 2, 7, 5, 8, 1, 6, 3]
sum_number = 0
for number in numbers:
    if number > 5:
        sum_number += number
print(f"sum of all numbers greater than five", sum_number)
# ==========================================
# SECTION 4: Bioreactor Temperature Monitor
# Goal: Real-time safety auditing for biotechnological batches.
# ==========================================
temps = [33.5, 37.8, 38.2, 31.5, 34.0, 39.1, 32.5]
print("--- Bioreactor Temperature Audit--")
for temp in temps:
    if temp > 38:
        print(f"{temp}: Overheating")
    elif temp < 32:
        print(f"{temp}: Too Cold")
    else:
        print(f"{temp}: Normal Range")
