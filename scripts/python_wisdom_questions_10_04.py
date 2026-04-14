# Dataset of student results for logic practice
results = [
    {"name": "Anushka", "score": 95},
    {"name": "Priya", "score": 82},
    {"name": "Amit", "score": 75},
    {"name": "Sneha", "score": 88}
]
# Filtering for specific criteria (Name starts with 'A' and Score > 80)
score_above = []
for student in results:
    name = student["name"]
    score = student["score"]
    if score > 80 and name.startswith("A"):
        score_above.append(name)
print(f"students name starting with a and score above 80:", score_above)

# # Raw gene affinity data from Piper longum research
raw_data = "SIRT1:8.5, PTGS2:6.1, TP53:9.2, TNF:5.4"
# Parsing string into structured gene information

genes = raw_data.split(", ")
for gene in genes:
    parts = gene.split(":")
    name = parts[0]
    score = float(parts[1])
    if score > 7.0:
        print(f"high affinity gene found: {name} (score:{score})")
# Real-time pH readings from a bioreactor
# Wisdom: In bioprocessing, a sudden jump to pH 14 is likely a sensor error,
# not a biological reality. We 'impute' using the last known valid state
ph_readings = [6.5, 6.6, 14.0, 6.7, 6.5]
for i in range (1,len(ph_readings)):
    if ph_readings[i] > 9:
        ph_readings[i] = ph_readings[i-1]

print(f"corrected list:", ph_readings)
