"""
PYTHON FOUNDATIONS & BIOINFORMATICS UTILITIES - DAY 02
Focus: Dictionary Iteration, Data Cleaning, and Recursive-safe Functions
"""

# ==========================================
# SECTION 1: DATA FILTERING & AGGREGATION
# ==========================================
students = {'Anushka': 91, 'Priya': 65, 'Riya': 78, 'Sneha': 88, 'Tanya': 55}
for student , scores in students.items():
    if scores < 70:
        print(f"students who scored below 70:", student)
products = {'Laptop': 55000, 'Phone': 25000, 'Tablet': 35000, 'Watch': 8000}
most_expensive_name = ""
most_expensive_price = 0
for product, price in products.items():
    if price > most_expensive_price:
        most_expensive_price = price
        most_expensive_name = product
print(f"most expensive product in the list:", most_expensive_name, most_expensive_price)
inventory = {'Apple': 50, 'Banana': 0, 'Mango': 30, 'Cherry': 0, 'Grapes': 20}
stock_greater = []
for fruits, stock in inventory.items():
    if  stock > 0:
        stock_greater.append(fruits)
print(f"only items where stock is greater than 0:", stock_greater)
employees = {'Anushka': 85000, 'Priya': 32000, 'Riya': 67000, 'Sneha': 41000, 'Tanya': 95000}
employee_name = ""
highest_salary = 0

for employee, salary in employees.items():
    if salary > highest_salary:
        highest_salary = salary
        employee_name = employee
print(f"highest paid employee and their salary:",  employee_name, highest_salary)
# ==========================================
# SECTION 2: DATA CLEANING & STRING FORMATTING
# ==========================================
sentences = ["  DATA SCIENCE  ", "python", "  MACHINE LEARNING  ", "statistics"]
new_list = []
for sentence in sentences:
    new_list.append(sentence.strip().title())
print(f"new list with stripped and titled case:", new_list)
marks = {'Maths': 45, 'Science': 82, 'English': 91, 'History': 38, 'Hindi': 76}
marks_above = []
for subject, score in marks.items():
    if score > 75:
        marks_above.append(subject)
print(f"subjects eith marks above 50:", marks_above)
# ==========================================
# SECTION 3: BIOINFORMATICS GENE TRACKING
# ==========================================
def collect_genes(gene_name, current_list = None):
    if current_list is None:
        current_list = []
    current_list.append(gene_name)
    return current_list
print(collect_genes("PIK3CA"))
print(collect_genes("TP53"))
