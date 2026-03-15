# Day 5: Dictionaries - Complete Guide
# =====================================

# ============================================
# 1. COMPLETE EXPLANATION
# ============================================

"""
WHAT IS A DICTIONARY?
- A dictionary is a collection of key-value pairs
- Like a real dictionary: word (key) -> definition (value)
- Keys must be unique and immutable (strings, numbers, tuples)
- Values can be any data type

WHY USE DICTIONARIES?
- Fast lookup by key (O(1) time complexity)
- Store related data together
- Represent real-world objects (user profiles, settings, etc.)

SYNTAX: {key1: value1, key2: value2}
"""

# ============================================
# 2. EXAMPLES (3 Required)
# ============================================

# --- EXAMPLE 1: Basic Dictionary (Simple) ---
print("=== EXAMPLE 1: Basic Dictionary ===")
# Creating a student record
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
print(f"Student: {student}")
print(f"Name: {student['name']}")  # Access by key
print(f"Age: {student['age']}")

# Adding new key-value pair
student["email"] = "alice@example.com"
print(f"Updated: {student}")

# Modifying existing value
student["age"] = 21
print(f"Age updated: {student['age']}")

# --- EXAMPLE 2: Real-World Scenario (Intermediate) ---
print("\\n=== EXAMPLE 2: Shopping Cart ===")
# E-commerce shopping cart
cart = {
    "laptop": {"price": 999, "quantity": 1},
    "mouse": {"price": 25, "quantity": 2},
    "keyboard": {"price": 75, "quantity": 1}
}

# Calculate total
total = 0
for item, details in cart.items():
    item_total = details["price"] * details["quantity"]
    total += item_total
    print(f"{item}: ${details['price']} x {details['quantity']} = ${item_total}")

print(f"Total: ${total}")

# --- EXAMPLE 3: Advanced Application (Complex) ---
print("\\n=== EXAMPLE 3: Word Frequency Counter ===")
# Count word occurrences in a sentence
text = "python is great python is powerful python is easy"
words = text.split()

# Build frequency dictionary
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Alternative using get()
frequency_v2 = {}
for word in words:
    frequency_v2[word] = frequency_v2.get(word, 0) + 1

print(f"Word frequency: {frequency}")
print(f"'python' appears {frequency['python']} times")

# ============================================
# 3. DICTIONARY METHODS & OPERATIONS
# ============================================

print("\\n=== Dictionary Methods ===")
person = {"name": "Bob", "age": 30, "city": "NYC"}

# Get all keys
print(f"Keys: {list(person.keys())}")

# Get all values
print(f"Values: {list(person.values())}")

# Get all items (key-value pairs)
print(f"Items: {list(person.items())}")

# Safe access with get() - no error if key doesn't exist
print(f"Country: {person.get('country', 'Not specified')}")

# Remove item
removed = person.pop("city")
print(f"Removed: {removed}, Dict: {person}")

# Check if key exists
print(f"'name' exists: {'name' in person}")
print(f"'email' exists: {'email' in person}")

# ============================================
# 4. EXERCISES
# ============================================

print("\\n=== EXERCISES ===")

# --- EASY EXERCISES (Basic Understanding) ---
print("\\n--- Easy Exercises ---")

# Exercise 1: Create a dictionary of your favorite things
favorites = {
    "color": "blue",
    "food": "pizza",
    "sport": "soccer"
}
print(f"1. Favorites: {favorites}")

# Exercise 2: Access and print each value
print(f"2. Color: {favorites['color']}, Food: {favorites['food']}")

# Exercise 3: Add a new favorite (movie)
favorites["movie"] = "Inception"
print(f"3. Added movie: {favorites}")

# Exercise 4: Update existing value
favorites["color"] = "green"
print(f"4. Updated color: {favorites}")

# Exercise 5: Count number of items
print(f"5. Total favorites: {len(favorites)}")

# --- MEDIUM EXERCISES (Apply Concepts) ---
print("\\n--- Medium Exercises ---")

# Exercise 6: Create a phone book and search
phonebook = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}
search_name = "Bob"
print(f"6. {search_name}'s number: {phonebook.get(search_name, 'Not found')}")

# Exercise 7: Merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print(f"7. Merged: {merged}")

# Exercise 8: Count letter frequency in a word
word = "programming"
letter_count = {}
for letter in word:
    letter_count[letter] = letter_count.get(letter, 0) + 1
print(f"8. Letter frequency in '{word}': {letter_count}")

# Exercise 9: Find the most common letter
most_common = max(letter_count, key=letter_count.get)
print(f"9. Most common letter: '{most_common}' ({letter_count[most_common]} times)")

# Exercise 10: Invert dictionary (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(f"10. Original: {original}, Inverted: {inverted}")

# --- HARD EXERCISES (Combine Concepts) ---
print("\\n--- Hard Exercises ---")

# Exercise 11: Group students by grade
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"},
    {"name": "David", "grade": "C"},
    {"name": "Eve", "grade": "B"}
]

by_grade = {}
for student in students:
    grade = student["grade"]
    if grade not in by_grade:
        by_grade[grade] = []
    by_grade[grade].append(student["name"])

print(f"11. Students by grade: {by_grade}")

# Exercise 12: Calculate average scores
scores = {
    "Alice": [85, 90, 88],
    "Bob": [78, 82, 80],
    "Charlie": [92, 95, 93]
}

averages = {}
for name, score_list in scores.items():
    averages[name] = sum(score_list) / len(score_list)

print(f"12. Average scores: {averages}")

# Exercise 13: Nested dictionary - Company structure
company = {
    "Engineering": {
        "employees": ["Alice", "Bob"],
        "budget": 500000
    },
    "Marketing": {
        "employees": ["Charlie", "David"],
        "budget": 300000
    }
}

total_budget = sum(dept["budget"] for dept in company.values())
total_employees = sum(len(dept["employees"]) for dept in company.values())
print(f"13. Total budget: ${total_budget}, Total employees: {total_employees}")

# ============================================
# 5. BONUS CHALLENGES
# ============================================

print("\\n=== Bonus Challenges ===")

# Bonus 1: Remove duplicates from list using dictionary
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(dict.fromkeys(numbers))
print(f"Bonus 1. Unique numbers: {unique}")

# Bonus 2: Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"Bonus 2. Squares: {squares}")

# Bonus 3: Filter dictionary
prices = {"apple": 0.5, "banana": 0.3, "orange": 0.8, "grape": 1.2}
expensive = {k: v for k, v in prices.items() if v > 0.5}
print(f"Bonus 3. Expensive fruits: {expensive}")

# ============================================
# 6. PRACTICE EXERCISES (Write Code Yourself!)
# ============================================

print("\\n=== Practice Exercises (No Solutions - You Code!) ===")
print("""
Exercise 1: Student grade manager
  - Create dictionary with 5 students and their scores
  - Find student with highest score
  - Calculate class average
  - Count how many students scored above 80

Exercise 2: Character frequency counter
  - Given string: "hello world"
  - Count frequency of each character (including spaces)
  - Print character and its count

Exercise 3: Dictionary merge with sum
  - dict1 = {'a': 10, 'b': 20, 'c': 30}
  - dict2 = {'b': 15, 'c': 25, 'd': 35}
  - Merge them, summing values for common keys
  - Result: {'a': 10, 'b': 35, 'c': 55, 'd': 35}

Exercise 4: Nested dictionary operations
  - Create a dictionary of 3 products with name, price, quantity
  - Calculate total inventory value
  - Find most expensive product
  - Print all products with quantity < 10

Exercise 5: Two-way dictionary (bidirectional mapping)
  - Create dict: {'a': 1, 'b': 2, 'c': 3}
  - Create reverse dict: {1: 'a', 2: 'b', 3: 'c'}
  - Print both dictionaries

Exercise 6: Group words by length
  - Given: ["cat", "dog", "elephant", "fox", "tiger"]
  - Group by word length: {3: ['cat', 'dog', 'fox'], 5: ['tiger'], 8: ['elephant']}
  - Print the grouped dictionary

Exercise 7: Dictionary key operations
  - Create a dictionary of your choice
  - Check if specific keys exist
  - Get value with default if key doesn't exist
  - Update multiple key-value pairs at once
  - Remove a key safely (without error if not exists)
""")

# ============================================
# 7. COMMON MISTAKES TO AVOID
# ============================================

print("\\n=== Common Mistakes ===")

# Mistake 1: Using mutable keys (lists)
# bad_dict = {[1, 2]: "value"}  # ERROR! Lists can't be keys

# Mistake 2: Accessing non-existent key
# print(person["email"])  # ERROR! Use .get() instead
print(f"Safe access: {person.get('email', 'N/A')}")

# Mistake 3: Modifying dict while iterating
# Use list() to create a copy
data = {"a": 1, "b": 2, "c": 3}
for key in list(data.keys()):
    if data[key] == 2:
        del data[key]
print(f"After deletion: {data}")

# ============================================
# 8. QUICK REFERENCE
# ============================================

print("\\n=== Quick Reference ===")
print("""
CREATE:     d = {"key": "value"}
ACCESS:     d["key"] or d.get("key")
ADD/UPDATE: d["new_key"] = "value"
DELETE:     del d["key"] or d.pop("key")
CHECK:      "key" in d
KEYS:       d.keys()
VALUES:     d.values()
ITEMS:      d.items()
LENGTH:     len(d)
CLEAR:      d.clear()
""")