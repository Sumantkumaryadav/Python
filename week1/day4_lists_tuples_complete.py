# Day 4: Lists & Tuples - Complete Guide
# ========================================

# ============================================
# 1. COMPLETE EXPLANATION
# ============================================

"""
WHAT ARE LISTS?
- Ordered, mutable collections of items
- Can contain different data types
- Created with square brackets []
- Items can be added, removed, or modified

WHAT ARE TUPLES?
- Ordered, immutable collections of items
- Created with parentheses ()
- Cannot be modified after creation
- Faster and more memory-efficient than lists

WHY USE THEM?
- Store multiple related values together
- Iterate over collections
- Lists: When data needs to change
- Tuples: When data should remain constant

KEY CONCEPTS:
- Indexing: Access items by position (0-based)
- Slicing: Extract portions [start:end:step]
- Methods: Built-in functions for manipulation
- Mutability: Lists can change, tuples cannot
"""

# ============================================
# 2. EXAMPLES (3 Required)
# ============================================

# --- EXAMPLE 1: Basic Lists & Tuples (Simple) ---
print("=== EXAMPLE 1: Basic Lists & Tuples ===")

# Creating a list
fruits = ["apple", "banana", "orange"]
print(f"List: {fruits}")
print(f"First: {fruits[0]}, Last: {fruits[-1]}")

# Modifying list
fruits.append("grape")
fruits[1] = "mango"
print(f"Modified: {fruits}")

# Creating a tuple
coordinates = (10, 20)
print(f"\nTuple: {coordinates}")
print(f"X: {coordinates[0]}, Y: {coordinates[1]}")

# Tuple unpacking
x, y = coordinates
print(f"Unpacked: x={x}, y={y}")

# --- EXAMPLE 2: Shopping Cart Manager (Intermediate) ---
print("\n=== EXAMPLE 2: Shopping Cart Manager ===")

# Shopping cart with prices
cart = [
    ("Laptop", 999.99),
    ("Mouse", 25.50),
    ("Keyboard", 75.00),
    ("Monitor", 299.99)
]

print("Shopping Cart:")
total = 0
for item, price in cart:
    print(f"  {item}: ${price:.2f}")
    total += price

print(f"Total: ${total:.2f}")

# Apply discount
discount_rate = 0.10
discount = total * discount_rate
final_total = total - discount
print(f"Discount (10%): -${discount:.2f}")
print(f"Final Total: ${final_total:.2f}")

# --- EXAMPLE 3: Data Analysis (Advanced) ---
print("\n=== EXAMPLE 3: Temperature Data Analysis ===")

# Weekly temperature data
temperatures = [72, 75, 68, 71, 73, 70, 74]
days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

# Statistics
avg_temp = sum(temperatures) / len(temperatures)
max_temp = max(temperatures)
min_temp = min(temperatures)
max_day = days[temperatures.index(max_temp)]
min_day = days[temperatures.index(min_temp)]

print("Weekly Temperature Report:")
for day, temp in zip(days, temperatures):
    print(f"  {day}: {temp}°F")

print(f"\nStatistics:")
print(f"  Average: {avg_temp:.1f}°F")
print(f"  Highest: {max_temp}°F ({max_day})")
print(f"  Lowest: {min_temp}°F ({min_day})")

# Days above average
above_avg = [(day, temp) for day, temp in zip(days, temperatures) if temp > avg_temp]
print(f"  Days above average: {len(above_avg)}")
for day, temp in above_avg:
    print(f"    {day}: {temp}°F")

# ============================================
# 3. LIST OPERATIONS & METHODS
# ============================================

print("\n=== List Operations & Methods ===")

# Creating lists
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []
range_list = list(range(5))

print(f"Numbers: {numbers}")
print(f"Mixed types: {mixed}")
print(f"From range: {range_list}")

# Adding elements
numbers.append(6)  # Add to end
print(f"After append(6): {numbers}")

numbers.insert(0, 0)  # Insert at index
print(f"After insert(0, 0): {numbers}")

numbers.extend([7, 8])  # Add multiple
print(f"After extend([7, 8]): {numbers}")

# Removing elements
numbers.remove(0)  # Remove first occurrence
print(f"After remove(0): {numbers}")

popped = numbers.pop()  # Remove and return last
print(f"Popped: {popped}, List: {numbers}")

popped_index = numbers.pop(0)  # Remove at index
print(f"Popped at 0: {popped_index}, List: {numbers}")

# Searching
fruits = ["apple", "banana", "orange", "banana"]
print(f"\nFruits: {fruits}")
print(f"Index of 'banana': {fruits.index('banana')}")
print(f"Count of 'banana': {fruits.count('banana')}")
print(f"'orange' in list: {'orange' in fruits}")

# Sorting
numbers = [3, 1, 4, 1, 5, 9, 2]
print(f"\nOriginal: {numbers}")
numbers.sort()  # Sort in place
print(f"Sorted: {numbers}")
numbers.sort(reverse=True)  # Descending
print(f"Reverse sorted: {numbers}")

# sorted() returns new list
original = [3, 1, 4]
sorted_list = sorted(original)
print(f"Original unchanged: {original}, Sorted copy: {sorted_list}")

# Reversing
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(f"Reversed: {numbers}")

# Copying
original = [1, 2, 3]
shallow_copy = original.copy()
deep_copy = original[:]
print(f"Original: {original}, Copy: {shallow_copy}")

# Clearing
temp = [1, 2, 3]
temp.clear()
print(f"After clear: {temp}")

# ============================================
# 4. LIST SLICING & INDEXING
# ============================================

print("\n=== List Slicing & Indexing ===")

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"List: {numbers}")

# Indexing
print(f"First [0]: {numbers[0]}")
print(f"Last [-1]: {numbers[-1]}")
print(f"Third [2]: {numbers[2]}")

# Slicing
print(f"First 3 [:3]: {numbers[:3]}")
print(f"Last 3 [-3:]: {numbers[-3:]}")
print(f"Middle [3:7]: {numbers[3:7]}")
print(f"Every 2nd [::2]: {numbers[::2]}")
print(f"Reverse [::-1]: {numbers[::-1]}")
print(f"Every 3rd from 1 [1::3]: {numbers[1::3]}")

# Modifying with slicing
numbers = [0, 1, 2, 3, 4]
numbers[1:3] = [10, 20]
print(f"After [1:3] = [10, 20]: {numbers}")

# ============================================
# 5. TUPLES IN DETAIL
# ============================================

print("\n=== Tuples in Detail ===")

# Creating tuples
point = (10, 20)
single = (42,)  # Note the comma!
no_parens = 1, 2, 3  # Parentheses optional
empty = ()

print(f"Point: {point}")
print(f"Single element: {single}")
print(f"No parentheses: {no_parens}")

# Tuple operations
t1 = (1, 2, 3)
t2 = (4, 5, 6)
combined = t1 + t2
repeated = t1 * 2
print(f"Combined: {combined}")
print(f"Repeated: {repeated}")

# Tuple methods (only 2!)
numbers = (1, 2, 2, 3, 2)
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 3: {numbers.index(3)}")

# Tuple unpacking
person = ("Alice", 25, "Engineer")
name, age, job = person
print(f"Name: {name}, Age: {age}, Job: {job}")

# Unpacking with *
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Swapping with tuples
a, b = 10, 20
a, b = b, a
print(f"After swap: a={a}, b={b}")

# ============================================
# 6. LIST COMPREHENSIONS
# ============================================

print("\n=== List Comprehensions ===")

# Basic comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# With condition
evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Evens: {evens}")

# With transformation
words = ["hello", "world", "python"]
upper_words = [w.upper() for w in words]
print(f"Uppercase: {upper_words}")

# Nested comprehension
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(f"Matrix: {matrix}")

# ============================================
# 7. EXERCISES
# ============================================

print("\n=== EXERCISES ===")

# --- EASY EXERCISES ---
print("\n--- Easy Exercises ---")

# Exercise 1: Create and print list
movies = ["Inception", "Matrix", "Interstellar"]
print(f"1. Favorite movies: {movies}")

# Exercise 2: Add and remove items
movies.append("Avatar")
movies.remove("Matrix")
print(f"2. Updated movies: {movies}")

# Exercise 3: Find max and min
numbers = [45, 23, 67, 12, 89, 34]
print(f"3. Numbers: {numbers}, Max: {max(numbers)}, Min: {min(numbers)}")

# Exercise 4: Create RGB tuple
rgb = (255, 128, 0)
print(f"4. RGB color: {rgb}")

# Exercise 5: List length and sum
numbers = [10, 20, 30, 40, 50]
print(f"5. Length: {len(numbers)}, Sum: {sum(numbers)}")

# --- MEDIUM EXERCISES ---
print("\n--- Medium Exercises ---")

# Exercise 6: Sort in descending order
numbers = [3, 7, 1, 9, 2, 5]
sorted_desc = sorted(numbers, reverse=True)
print(f"6. Original: {numbers}, Sorted desc: {sorted_desc}")

# Exercise 7: Remove duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(dict.fromkeys(numbers))
print(f"7. With duplicates: {numbers}, Unique: {unique}")

# Exercise 8: Find common elements
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = [x for x in list1 if x in list2]
print(f"8. List1: {list1}, List2: {list2}, Common: {common}")

# Exercise 9: Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
print(f"9. Nested: {nested}, Flat: {flat}")

# Exercise 10: Split list into chunks
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_size = 3
chunks = [numbers[i:i+chunk_size] for i in range(0, len(numbers), chunk_size)]
print(f"10. Original: {numbers}, Chunks: {chunks}")

# --- HARD EXERCISES ---
print("\n--- Hard Exercises ---")

# Exercise 11: Rotate list
numbers = [1, 2, 3, 4, 5]
k = 2  # Rotate right by 2
rotated = numbers[-k:] + numbers[:-k]
print(f"11. Original: {numbers}, Rotated by {k}: {rotated}")

# Exercise 12: Find second largest
numbers = [45, 23, 67, 12, 89, 34]
sorted_unique = sorted(set(numbers), reverse=True)
second_largest = sorted_unique[1] if len(sorted_unique) > 1 else None
print(f"12. Numbers: {numbers}, Second largest: {second_largest}")

# Exercise 13: Merge and sort two lists
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
merged = sorted(list1 + list2)
print(f"13. List1: {list1}, List2: {list2}, Merged: {merged}")

# ============================================
# 8. BONUS CHALLENGES
# ============================================

print("\n=== Bonus Challenges ===")

# Bonus 1: List of tuples - sort by second element
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(f"Bonus 1. Sorted by score: {sorted_students}")

# Bonus 2: Zip two lists
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
combined = list(zip(names, scores))
print(f"Bonus 2. Zipped: {combined}")

# Bonus 3: Transpose matrix
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = list(zip(*matrix))
print(f"Bonus 3. Original: {matrix}, Transposed: {transposed}")

# ============================================
# 9. PRACTICE EXERCISES (Write Code Yourself!)
# ============================================

print("\n=== Practice Exercises (No Solutions - You Code!) ===")
print("""
Exercise 1: List statistics calculator
  - Given: [12, 45, 23, 67, 34, 89, 11]
  - Calculate: sum, average, median, range (max-min)
  - Print all statistics

Exercise 2: Remove all occurrences
  - Given list: [1, 2, 3, 2, 4, 2, 5]
  - Remove all occurrences of 2
  - Print the cleaned list

Exercise 3: List intersection and union
  - list1 = [1, 2, 3, 4, 5]
  - list2 = [4, 5, 6, 7, 8]
  - Find intersection (common elements) and union (all unique elements)
  - Print both results

Exercise 4: Palindrome list checker
  - Check if list [1, 2, 3, 2, 1] is a palindrome
  - Check if list [1, 2, 3, 4, 5] is a palindrome
  - Print results for both

Exercise 5: Separate even and odd numbers
  - Given: [12, 7, 23, 8, 15, 30, 9]
  - Create two lists: one for evens, one for odds
  - Print both lists

Exercise 6: Find missing number
  - Given list: [1, 2, 4, 5, 6] (missing 3)
  - Find and print the missing number
  - Hint: Sum of 1 to n = n*(n+1)/2

Exercise 7: Tuple operations
  - Create tuple of 5 numbers
  - Find: min, max, sum, average
  - Create new tuple with numbers in reverse order
  - Print all results
""")

# ============================================
# 10. COMMON MISTAKES
# ============================================

print("\n=== Common Mistakes ===")

# Mistake 1: Modifying list while iterating
numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     numbers.remove(num)  # BAD!
print("1. Don't modify list while iterating")

# Mistake 2: Shallow copy issue
original = [[1, 2], [3, 4]]
shallow = original.copy()
shallow[0][0] = 99
print(f"2. Shallow copy issue - Original: {original}")

# Mistake 3: Single element tuple
not_tuple = (42)  # This is just an int!
is_tuple = (42,)  # Need comma
print(f"3. Not tuple: {type(not_tuple)}, Is tuple: {type(is_tuple)}")

# Mistake 4: List multiplication with mutable objects
# matrix = [[0] * 3] * 3  # BAD! All rows are same object
matrix = [[0] * 3 for _ in range(3)]  # GOOD!
print(f"4. Correct matrix: {matrix}")

# ============================================
# 11. QUICK REFERENCE
# ============================================

print("\n=== Quick Reference ===")
print("""
LISTS:
  Create:  [1, 2, 3]
  Add:     append(), insert(), extend()
  Remove:  remove(), pop(), clear()
  Search:  index(), count(), in
  Sort:    sort(), sorted(), reverse()
  Copy:    copy(), [:]

TUPLES:
  Create:  (1, 2, 3) or 1, 2, 3
  Single:  (42,)
  Methods: count(), index()
  Unpack:  a, b, c = tuple

SLICING:
  [start:end:step]
  [:3]   # First 3
  [-3:]  # Last 3
  [::2]  # Every 2nd
  [::-1] # Reverse

COMPREHENSION:
  [x**2 for x in range(5)]
  [x for x in list if x > 0]
""")