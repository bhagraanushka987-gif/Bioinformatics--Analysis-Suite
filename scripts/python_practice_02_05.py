"""
DEFENSIVE PROGRAMMING & NESTED DATA ANALYSIS - DAY 18
Focus: Try-Except Exception Handling, Dual-Extremum Search, and API JSON Parsing
Project: Pharmaceutical Pricing, Sensor Data Sanitization, and Customer Lifetime Value (LTV)
"""

# ==========================================
# SECTION 1: PHARMACOLOGICAL & TEXTUAL AUDITS
# ==========================================

# 1.1 Dual-Extremum Optimization: Identifying Price Boundaries
drugs = {'Aspirin': 25, 'Paracetamol': 15, 'Ibuprofen': 45, 'Amoxicillin': 120, 'Metformin': 35}
most_exp = 0
most_exp_name = ""
# Initializing with Infinity to ensure any real price is lower
cheapest_drug = float('inf')
cheapest_name = ""
for drug, cost in drugs.items():
    if cost > most_exp:
        most_exp = cost
        most_exp_name = drug
    if cost < cheapest_drug:
        cheapest_drug = cost
        cheapest_name = drug
print(f"finding the most expensive and cheapest drug in the list:{most_exp_name} {most_exp},{cheapest_name} {cheapest_drug}")
# 1.2 Linguistic Refactoring: Nomenclature Updates
text = "machine learning and deep learning are subsets of machine learning and machine learning is growing"
counting = text.count("machine learning")
print(f"counting machine learning in the text:{counting}")
# Replacing terminology for high-level technical summaries
replacing = text.replace("machine learning","AI")
print(f"replacing in the text:{replacing}")


numbers = [34, 17, 82, 45, 63, 28, 91, 56]
sum_numbers = 0
for number in numbers:
    if number > 50 :
        sum_numbers += number
print(f"sum of all numbers above 50:{sum_numbers}")

# ==========================================
# SECTION 2: DEFENSIVE SENSOR DATA CLEANING
# ==========================================

# 2.1 Exception Handling (Try-Except) for Messy API Inputs
# Objective: Convert strings to floats while ignoring invalid "Glitch" or "N/A" entries
raw_api_data = ["72.5", "68.1", "N/A", "74.0", "Glitch", "65.2"]

clean_temps = []
for data in raw_api_data:
    try:
        clean_temps.append(float(data))
    except ValueError:
        pass
print(f"Valid temperature:{clean_temps}")

# ==========================================
# SECTION 3: NESTED DATA & API ANALYTICS
# ==========================================

# 3.1 JSON Response Simulation: User Profile Parsing
# Raw JSON data from the API
api_response = {
    "user_id": 9942,
    "name": "Sarah Connor",
    "orders": [
        {"order_id": "A1", "amount": 150.0, "status": "completed"},
        {"order_id": "A2", "amount": 45.0, "status": "cancelled"},
        {"order_id": "A3", "amount": 200.0, "status": "completed"},
        {"order_id": "A4", "amount": 10.0, "status": "pending"}
    ]
}

def calculate_lifetime_value(user_profile):
    total = 0
    for order in user_profile["orders"]:
        if order["status"] == "completed":
            total += order["amount"]
    return total
ltv = calculate_lifetime_value(api_response)
print(f"lifetime value:{ltv}")