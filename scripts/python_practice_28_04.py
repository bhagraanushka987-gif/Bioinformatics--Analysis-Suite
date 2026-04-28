"""
BIO-AUTOMATION & SECURITY AUDIT - DAY 14
Focus: Minimum-Value Search (inf), Threshold Inventory Management, and Cyber-Threat Logic
Project: Proteomic Filtering, Pharmaceutical Procurement, and Network Traffic Analysis
"""

# ==========================================
# SECTION 1: PROTEOMICS & LABORATORY AUDIT
# ==========================================

# 1.1 High-Molecular Weight Protein Filtering
proteins = {'Insulin': 5808, 'Hemoglobin': 64500, 'Collagen': 300000, 'Albumin': 66000, 'Myosin': 480000}
proteins_only = []
for protein, molecular_weight in proteins.items():
    if molecular_weight > 60000:
        proteins_only.append(protein)
print(f"only proteins where molecular weight is above 60000:", proteins_only)

# 1.2 Diagnostic Frequency: Positive Control Count
lab_results = {'Sample1': 'Positive', 'Sample2': 'Negative', 'Sample3': 'Positive', 'Sample4': 'Negative', 'Sample5': 'Positive'}
count = 0
for sample, result in lab_results.items():
    if result == "Positive":
        count += 1
print(f"counting result with positive result:", count)

# ==========================================
# SECTION 2: PROCUREMENT & INVENTORY LOGIC
# ==========================================

# 2.1 Procurement Optimization: Finding the Cheapest Unit
medicines = {'Aspirin': 25, 'Paracetamol': 15, 'Ibuprofen': 45, 'Amoxicillin': 120, 'Metformin': 35}
# Initializing with Infinity ensures the first entry always triggers the comparison
cheapest_medicine_name = ""
price = float('inf')
for medicine, cost in medicines.items():
    if cost < price:
        price = cost
        cheapest_medicine_name = medicine
print(f"cheaest medicine and its price:", cheapest_medicine_name, price)

store_prices = {
    "Smartwatch": 199,
    "Headphones": 89,
    "Tablet": 299,
    "Charger": 25
}
updated_prices = {}
for electronic, price in store_prices.items():
    updated_prices[electronic] = price + 15
print(f"new prices:{updated_prices}")

# 2.2 Inventory Reorder Logic: Threshold-Based Supply Chain
inventory = {
    "Laptops": 5,
    "Mice": 45,
    "Keyboards": 8,
    "Monitors": 12,
    "Webcams": 2
}
reorder_list = []

for electronics, stock in inventory.items():
    if stock < 10:
        reorder_list.append(electronics)
print(f"products to reorder:{reorder_list}")

# ==========================================
# SECTION 3: CYBER-SECURITY THREAT DETECTION
# ==========================================

# 3.1 Network Traffic Audit: Identifying Policy Violations
# Goal: Detect High-Threat IPs that bypassed automated blocks
network_traffic = [
    {"IP": "192.168.1.1", "Threat_Level": 95, "Action": "Allow"},
    {"IP": "10.0.0.5", "Threat_Level": 40, "Action": "Allow"},
    {"IP": "172.16.0.8", "Threat_Level": 98, "Action": "Block"},
    {"IP": "192.168.1.20", "Threat_Level": 99, "Action": "Allow"}
]
breached_ips = []

for connection in network_traffic:
    # Logic: High threat (>90) combined with 'Allow' status indicates a breach
    if connection["Threat_Level"] > 90 and connection["Action"] == "Allow":
        breached_ips.append(connection["IP"])
print(f"critical level alert:{breached_ips}")