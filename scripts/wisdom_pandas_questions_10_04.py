"""
BIOINFORMATICS DATA CLEANING DRILLS
Date: April 10, 2026
Focus: Data Merging, String Parsing, and Duplicate Management
"""
import pandas as pd

#SECTION 1: RELATIONAL DATA MERGING
# Wisdom: Combining student IDs with grades to create a master record.
names_data = {
    'st_id': [101, 102, 103],
    'st_name': ['Anushka', 'Priya', 'Amit']
}

# Data for DataFrame 2
marks_data = {
    'id': [101, 102, 103],
    'grade': ['A+', 'A', 'B']
}


df_names = pd.DataFrame(names_data)
print(f"creating dataframe for name:", df_names)
df_marks = pd.DataFrame(marks_data)
print(f"creating dataframe for marks:", df_marks)
# Aligning column names is crucial before a merge
renaming = df_marks.rename(columns={'id':'st_id'})
print(f"Rename 'id' to 'st_id' in df_marks:", renaming)
final_df = pd.merge(df_names, renaming, on='st_id')
print(f"merging both:", final_df)

#SECTION 2: PHARMACEUTICAL CONCENTRATION CLEANING
# Wisdom: Converting textual lab readings into numeric floats for calculation.

concentration = ['10.5mg', '12.0mg', 'NaN', '9.8mg']
df_conc = pd.DataFrame(concentration, columns =['value'])
#print(f"creating a dataframe:", df_conc)
#Strip unit strings to allow mathematical operations
df_conc['value'] = df_conc['value'].str.replace('mg', '')
#print(f"removing mg from the dataframe:", removing)
df_conc['value'] = df_conc['value'].astype(float)
#print(f"converting the column to float:",converting)
avg_conc = df_conc['value'].mean()
print("Cleaned DataFrame:")
print(df_conc)
print(f"finding average concentration:", avg_conc)



# SECTION 3: CLINICAL TRIAL DE-DUPLICATION
# Wisdom: Ensuring each patient is counted only once for statistical integrity.
data = {
    'Patient_ID': [101, 102, 101, 103],
    'Effectiveness_Score': [8.5, 7.0, 8.5, 9.0]
}
df_trials = pd.DataFrame(data)

# 2. Logic: Drop duplicates but keep the first occurrence
# The 'subset' tells Pandas to only look for duplicates in the ID column
df_unique = df_trials.drop_duplicates(subset='Patient_ID', keep='first')

# 3. Final Math: Calculate the average of the CLEAN data
final_avg = df_unique['Effectiveness_Score'].mean()

print("Cleaned Data (No Duplicates):")
print(df_unique)
print(f"\nFinal Average Score: {final_avg}")