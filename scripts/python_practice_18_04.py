
"""
PYTHON ALGORITHMIC LOGIC - DAY 06
Focus: Iterative Maximums, String Mining, and Mutable Default Arguments
Project: Market Analytics, Text Processing, and Genomic Mutation Tracking
"""

# ==========================================
# SECTION 1: MARKET DATA & ITERATIVE SEARCH
# ==========================================

# 1.1 Finding the Maximum Value in a Key-Value Store
stocks = {'Apple': 150, 'Google': 280, 'Microsoft': 95, 'Tesla': 320, 'Amazon': 180}
most_expensive_company = ""
highest_price = 0

for company, stock in stocks.items():
    if stock > highest_price:
        highest_price = stock
        most_expensive_company = company

print(f"Market Analysis: Most expensive asset is {most_expensive_company} at ${highest_price}")

# ==========================================
# SECTION 2: TEXT MINING & NORMALIZATION
# ==========================================

# 2.1 Keyword Frequency and Substitution
text = "machine learning is powerful and machine learning is the future of machine learning"
counting = text.count("machine learning")
print(f"Term Frequency ('machine learning'): {counting}")

replacing = text.replace("machine learning", "deep learning")
print(f"Refactored Content: {replacing}")

# 2.2 List Normalization (Strip and Title Case)
words = ["  BIOLOGY  ", "chemistry", "  PHYSICS  ", "maths", "  ENGLISH  "]
standardized_list = []
for word in words:
    standardized_list.append(word.strip().title())
print(f"Standardized Domain Registry: {standardized_list}")

# ==========================================
# SECTION 3: QUANTITATIVE FILTERING & STATS
# ==========================================

# 3.1 Parity Filtering and Aggregation
numbers_list = [14, 27, 36, 53, 42, 61, 18, 75]
odd_numbers = []
for number in numbers_list:
    if number % 2 == 1:
        odd_numbers.append(number)
print(f"Statistical Metric: Sum of all odd numbers: {sum(odd_numbers)}")

# 3.2 Dictionary Filtering (Demographic Threshold)
employees = {'Riya': 25, 'Sneha': 32, 'Priya': 28, 'Tanya': 19, 'Anushka': 35}
senior_employees = []
for employee, age in employees.items():
    if age > 25:
        senior_employees.append(employee)
print(f"Demographic Filter (Age > 25): {senior_employees}")

# 3.3 Manual Extremum Identification
series = [5, 12, 8, 23, 16, 7, 19, 30, 11]

# Finding Largest
largest_number = series[0]
for number in series:
    if number > largest_number:
        largest_number = number
print(f"Algorithm Result: Largest number in series: {largest_number}")

# Finding Smallest
smallest_number = series[0]
for number in series:
    if number < smallest_number:
        smallest_number = number
print(f"Algorithm Result: Smallest number in series: {smallest_number}")

# ==========================================
# SECTION 4: RESEARCH INTEGRITY & MEMORY SAFETY
# ==========================================

def record_mutation(gene, mutation_list=None):
    """
    Standardized function for mutation tracking.
    Uses 'None' as default to avoid mutable argument side effects.
    """
    if mutation_list is None:
        mutation_list = []
    mutation_list.append(gene)
    return mutation_list

# Note: Corrected the function names to match the definition for execution
print("Genomic Log 1:", record_mutation("Pippali_A"))
print("Genomic Log 2:", record_mutation("Pippali_B"))