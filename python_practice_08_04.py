
fruits = ["apple", "  Banana  ", "mango", "GRAPES", "kiwi"]
fruit_list = []
for fruit in fruits:
    fruit_list.append(fruit.title().strip())
print("--- Question 1: Cleaned Fruit List ---")
print(fruit_list)
print("\n")


sentence = "data science is the future of science and data"
total = sentence.count("science")
print(f"count total times science is in sentence:", total)
replacing = sentence.replace("science" ,"analytics")
print(f"replacing old word with new:", replacing)

numbers = [4, 7, 2, 9, 1, 5, 8, 3, 6]
current_max = numbers[0]
for number in numbers:
    if number > current_max:
        current_max = number
print(f"largest number in the series:", current_max)
current_min = numbers[0]
for number in numbers:
    if number < current_min:
        current_min = number
print(f"smallest number in the series:", current_min)


words = ["  hello  ", "WORLD", "python", "  DATA  ", "science"]
new_list =[]
for word in words:
    new_list.append(word.strip().upper())
print(f"new list:", new_list)


text = "the cat sat on the mat and the cat sat again"
count = text.count("cat")
print(f"count how many many times cat appears:", count)
replacing = text.replace('cat', 'dog')
print(f"replace cat from dog:", replacing)


scores = [45, 82, 13, 67, 91, 38, 74, 56]
current_max = scores[0]
for score in scores:
    if score > current_max:
        current_max = score
print(f"highest score in the scores:", current_max)
current_min = scores[0]
for score in scores:
    if score < current_min:
        current_min = score
print(f"lowest score in the scores:", current_min)
