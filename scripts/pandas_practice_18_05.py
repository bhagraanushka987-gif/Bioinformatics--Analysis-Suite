

import pandas as pd
# 1. SETUP: Create Initial Dataframe
data = {'product': ['apple', 'banana', 'cherry', 'date'],
        'price': [120, 40, 200, 80]}
fruit_df = pd.DataFrame(data)

# 2. TRANSFORMATION: Apply dynamic discount based on price
def apply_discount(row):
    if row['price'] > 100:
        return row['price'] * 0.90
    else:
        return row['price'] * 0.95
fruit_df['discounted_price'] = fruit_df.apply(apply_discount, axis=1)
#print(f"creating new column:", df['discounted_price'])


# 3. STRING MANIPULATION: Format product names
fruit_df['product_title'] = fruit_df['product'].map(lambda p: p.title())
#print(f"new columnin upper:", df['product_title'])


# 4. CATEGORIZATION: Label items by price point
fruit_df['price_category'] = fruit_df['price'].map(lambda p:
       "Expensive" if p > 100 else
       "Cheap"
)
#print(f"new column categorising price:", df['price_category'])
print("--- Fruit Analysis ---")
print(fruit_df)

# 5. BONUS: Salary Analysis Example
data = {'name': ['alice', 'bob', 'carol', 'dave'],
        'salary': [30000, 45000, 52000, 38000]}
staff_df = pd.DataFrame(data)

#Calculate 10% bonus for high earners, 5% for others
def experience_bonus(row):
    if row['salary'] > 45000:
        return row['salary'] * 1.10
    else:
          return row['salary'] * 1.05
staff_df['new_salary'] = staff_df.apply(experience_bonus, axis=1)
#print(f"creating a new column:", df['new_salary'])
print("--- Salary Analysis ---")
print(staff_df)