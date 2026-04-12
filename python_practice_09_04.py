# --- TASK 1: WORD FREQUENCY COUNT ---
sentence = "banana apple mango apple banana apple"
words = sentence.split()
count = {}
for word in words:
    if word not in count:
        count[word] = 1
    else:
        count[word] += 1
print(f"1. counting each fruit in the sentence:", count)
print("\n" + "-"*30 + "\n")

# --- TASK 2: STUDENT NAME CLEANING ---
students = ["  alice  ", "BOB", "  charlie  ", "DIANA"]
new_list = []
for student in students:
    new_list.append(student.strip().title())
print(f"2. new list:",new_list)
print("\n" + "-"*30 + "\n")

# --- TASK 3: DICTIONARY FILTERING (MARKS) ---
marks = {'Anushka': 91, 'Priya': 78, 'Riya': 85, 'Sneha': 62}
student_scored = []
for students,mark in marks.items():
    if mark > 80:
        student_scored.append(students)
print(f"3. only students who scored above 80:", student_scored)