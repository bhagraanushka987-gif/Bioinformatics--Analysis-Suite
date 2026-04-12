"""
CORE PYTHON LOGIC & SENSOR DATA INTEGRITY
Focus: String Manipulation, Iterative Filtering, and Algorithmic Imputation
"""

text = "dog sat on the log and the dog ran away"
dog_counts = text.count('dog')
print(f"count for dogs in the sentence:", dog_counts)
replacing = text.replace('dog', 'cat')
print(f"repacing dog with the cat in the sentence:", replacing)
#========================================
# SECTION 1: STRING DATA NORMALIZATION
# Wisdom: Cleaning inconsistent user input (Whitespace and Casing).
# ======================================
# Drill: Standardizing names for a clean database
names = ["  PRIYA  ", "anushka", "  RIYA  ", "sneha"]
# Using .strip() to remove 'noise' and .title() for proper name formatting
new_list = []
for name in names:
    new_list.append(name.strip().title())
print(f"new list:", new_list)
# ==========================================
# SECTION 2: ALGORITHMIC DATA PROCESSING
# Wisdom: Calculating thresholds and sums manually to understand internal logic.
# ==========================================
numbers = [12, 45, 7, 89, 23, 56, 34]
current_max = numbers[0]
for number in numbers:
    if number > current_max:
        current_max = number
print(f"finding the largest number in the list:", current_max)
current_min = numbers[0]
for number in numbers:
    if number < current_min:
        current_min = number
print(f"finding the smallest number in the list:", current_min)

scores = {'Maths': 85, 'Science': 92, 'English': 78, 'History': 65}
for subject , marks in scores.items():
    if marks > 80:
        print(f"only those subjects where score is above 80:", subject)
# Logic: Modulo Operator (%) for identifying even/odd batches
numbers = [3, 7, 2, 8, 1, 9, 4, 6, 5]
sum_even_numbers = 0
for number in numbers:
    if number %2 == 0:
        sum_even_numbers += number
print(f"sum of all even numbers", sum_even_numbers)

words = ["  DATA  ", "  science  ", "PYTHON", "  analysis  "]
new_list = []
for word in words:
    new_list.append(word.strip().upper())
print(f"new list:", new_list)
# ==========================================
# SECTION 3: BIOREACTOR SENSOR INTEGRITY
# Wisdom: Forward-fill imputation for 'out-of-range' sensor errors.
# ==========================================
ph_log = [6.8, 7.0, 14.5, 6.9, 3.2, 7.1]

for i in range (1,len(ph_log)):
    if ph_log[i] > 9.0 or ph_log[i] < 4.0:
        ph_log[i] = ph_log[i-1]
print(f'corrected_readings of bioreactor:', ph_log)