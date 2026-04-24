"""
SYSTEM AUTOMATION & LOG PARSING - DAY 10
Focus: Iterative Maximums, Logical Aggregation, and Metadata Transformation
Project: Laboratory Audit, User Registry Standardization, and Transactional Filtering
"""

# ==========================================
# SECTION 1: EXPERIMENTAL & LAB METRICS
# ==========================================

# 1.1 Identifying Top Performance: Iterative Maximum Search
experiments = {'Experiment1': 45, 'Experiment2': 78, 'Experiment3': 23, 'Experiment4': 91, 'Experiment5': 56}
highest_scoring_experiment = ""
highest_score = 0
for experiment, score in experiments.items():
    if score > highest_score:
        highest_score = score
        highest_scoring_experiment = experiment
print(f"highest scoring experiment:", highest_scoring_experiment, highest_score)
# 1.2 Diagnostic Frequency: Counting Negative Controls
lab_results = {'Sample1': 'Positive', 'Sample2': 'Negative', 'Sample3': 'Positive', 'Sample4': 'Positive', 'Sample5': 'Negative'}
count = 0
for sample, result in lab_results.items():
    if result == "Negative":
        count += 1
print(f"counting negative results in the lab result:", count)
# 1.3 Threshold Summation: Conditional Integer Accumulation
numbers = [34, 7, 56, 12, 89, 23, 67, 45]
sum_numbers = 0
for number in numbers:
    if number > 40:
        sum_numbers += number
print(f"sum of all numbers greater than 40:", sum_numbers)
# ==========================================
# SECTION 2: METADATA & LOG TRANSFORMATION
# ==========================================

# 2.1 Standardized User Registry (Title Case & Slug Generation)
raw_names = ["  john DOE ", "  JANE smith", "  albert EINSTEIN  "]
system_users = {}
for name in raw_names:
    # Normalizing name for display
    clear_name = name.strip()
    clean_name = clear_name.title()
    # Generating a unique system username (lowercase_with_underscores)
    username = clean_name.lower().replace(" ", "_")
    system_users[clean_name] = username
print(f"cleaning the messy data : {system_users}")

# 2.2 Server Log Parsing: CSV-Style Extraction & Filtering
server_logs = [
    "txn01,  LAPTOP  , 1200",
    "txn02, mouse, 25",
    "txn03,   SMARTPHONE , 850 ",
    "txn04, keyboard , 75"
]
expensive_items = {}

for log in server_logs:
    new_log = log.split(",")
    # Cleaning the product name from the second column
    product_name = new_log[1].strip().title()
    # Typecasting the third column for financial logic
    price = int(new_log[2])
    # Filter: Capturing only high-value inventory items
    if price > 100:
        expensive_items[product_name] = price
print(f"cleaning the server logs: {expensive_items}")