# Day 6: Sets & When to Use Each Data Structure
# ================================================

# ============================================
# 1. COMPLETE EXPLANATION
# ============================================

"""
WHAT IS A SET?
- A set is an UNORDERED collection of UNIQUE elements
- No duplicates allowed — adding a duplicate is silently ignored
- Like a bag of unique items: you can check what's inside, add, or remove
- Uses curly braces {} but NO key-value pairs (that's a dict)

WHY USE SETS?
- Remove duplicates instantly
- Super fast membership testing: "is X in this set?" → O(1)
- Mathematical operations: union, intersection, difference
- Great for comparing groups of data

SYNTAX: {value1, value2, value3}
NOTE:   empty set = set()  (NOT {} — that creates an empty dict!)

WHEN TO USE WHICH DATA STRUCTURE?
┌──────────┬───────────┬──────────┬───────────┬──────────────────────────┐
│ Feature  │ List      │ Tuple    │ Dict      │ Set                      │
├──────────┼───────────┼──────────┼───────────┼──────────────────────────┤
│ Ordered  │ ✅ Yes    │ ✅ Yes   │ ✅ Yes*   │ ❌ No                    │
│ Mutable  │ ✅ Yes    │ ❌ No    │ ✅ Yes    │ ✅ Yes                   │
│ Dupes    │ ✅ Yes    │ ✅ Yes   │ ❌ Keys   │ ❌ No                    │
│ Indexed  │ ✅ Yes    │ ✅ Yes   │ By key    │ ❌ No                    │
│ Use for  │ Ordered   │ Fixed    │ Key-value │ Unique items,            │
│          │ items     │ data     │ lookups   │ membership testing       │
└──────────┴───────────┴──────────┴───────────┴──────────────────────────┘
* Dicts preserve insertion order since Python 3.7
"""

# ============================================
# 2. EXAMPLES (3 Required)
# ============================================

# --- EXAMPLE 1: Basic Set Operations (Simple) ---
print("=== EXAMPLE 1: Basic Set Operations ===")

# Creating sets
fruits = {"apple", "banana", "cherry"}
print(f"Fruits: {fruits}")

# Adding elements
fruits.add("orange")
print(f"After add: {fruits}")

# Adding duplicate — nothing happens
fruits.add("apple")
print(f"After adding duplicate 'apple': {fruits}")  # still same size

# Removing elements
fruits.remove("banana")       # raises error if not found
print(f"After remove: {fruits}")

fruits.discard("mango")       # NO error if not found — safer
print(f"After discard 'mango': {fruits}")

# Membership testing (very fast)
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'banana' in fruits: {'banana' in fruits}")

# Length
print(f"Number of fruits: {len(fruits)}")

# Creating set from a list (removes duplicates)
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = set(numbers)
print(f"Original list: {numbers}")
print(f"As set (no dupes): {unique_numbers}")

# --- EXAMPLE 2: Set Math Operations (Intermediate) ---
print("\n=== EXAMPLE 2: Set Math Operations ===")

# Two groups of students
python_students = {"Alice", "Bob", "Charlie", "David"}
java_students = {"Charlie", "David", "Eve", "Frank"}

# Union — students in EITHER class (all unique students)
all_students = python_students | java_students  # or .union()
print(f"All students: {all_students}")

# Intersection — students in BOTH classes
both = python_students & java_students  # or .intersection()
print(f"In both classes: {both}")

# Difference — in Python but NOT Java
only_python = python_students - java_students  # or .difference()
print(f"Only Python: {only_python}")

# Symmetric difference — in one OR the other, but NOT both
exclusive = python_students ^ java_students  # or .symmetric_difference()
print(f"Exclusive to one class: {exclusive}")

# Subset / Superset
small = {"Alice", "Bob"}
print(f"{small} is subset of python_students: {small.issubset(python_students)}")
print(f"python_students is superset of {small}: {python_students.issuperset(small)}")

# Disjoint — no common elements
math_students = {"Grace", "Henry"}
print(f"Math & Python share students: {not math_students.isdisjoint(python_students)}")

# --- EXAMPLE 3: Real-World Application (Advanced) ---
print("\n=== EXAMPLE 3: Finding Common & Unique Website Visitors ===")

# Daily website visitors
monday = {"user1", "user2", "user3", "user4", "user5"}
tuesday = {"user3", "user4", "user5", "user6", "user7"}
wednesday = {"user1", "user5", "user6", "user7", "user8"}

# Total unique visitors across all days
total_unique = monday | tuesday | wednesday
print(f"Total unique visitors: {len(total_unique)} → {total_unique}")

# Visited EVERY day (loyal users)
loyal = monday & tuesday & wednesday
print(f"Visited all 3 days: {loyal}")

# Visited only on Monday
only_monday = monday - tuesday - wednesday
print(f"Only visited Monday: {only_monday}")

# New visitors on Wednesday (not seen before)
new_wednesday = wednesday - monday - tuesday
print(f"New on Wednesday: {new_wednesday}")

# ============================================
# 3. WHEN TO USE EACH DATA STRUCTURE
# ============================================

print("\n=== When to Use What ===")

# LIST — ordered, allows duplicates, indexed
# Use when: order matters, you need duplicates, you access by position
shopping_list = ["milk", "eggs", "milk", "bread"]  # duplicates OK, order matters
print(f"List (shopping): {shopping_list}")

# TUPLE — ordered, immutable, allows duplicates
# Use when: data shouldn't change, returning multiple values, dict keys
coordinates = (40.7128, -74.0060)  # lat/long shouldn't change
rgb_color = (255, 128, 0)
print(f"Tuple (coordinates): {coordinates}")

# DICTIONARY — key-value pairs, fast lookup by key
# Use when: you need to look up values by a label/name
user = {"name": "Alice", "age": 25, "email": "alice@example.com"}
print(f"Dict (user): {user}")

# SET — unordered, unique elements, fast membership testing
# Use when: you need unique items, checking if something exists, math operations
tags = {"python", "ml", "data-science", "python"}  # auto-deduped
print(f"Set (tags): {tags}")

# DECISION GUIDE:
print("""
CHOOSING THE RIGHT DATA STRUCTURE:
┌─ Need key-value pairs?          → DICT
├─ Need unique items only?        → SET
├─ Need to keep order + dupes?    → LIST
├─ Need immutable ordered data?   → TUPLE
└─ Need fast "is X in here?"     → SET (or DICT for key lookup)
""")

# ============================================
# 4. FROZENSET (Immutable Set)
# ============================================

print("=== Frozenset (Immutable Set) ===")

# A frozenset is a set that CANNOT be changed after creation
# Useful as dictionary keys or elements of another set
frozen = frozenset([1, 2, 3])
print(f"Frozenset: {frozen}")

# frozen.add(4)  # ERROR! Can't modify a frozenset

# Use as dict key (regular sets can't be dict keys)
permissions = {
    frozenset(["read"]): "viewer",
    frozenset(["read", "write"]): "editor",
    frozenset(["read", "write", "delete"]): "admin"
}
user_perms = frozenset(["read", "write"])
print(f"Role: {permissions[user_perms]}")

# ============================================
# 5. EXERCISES WITH SOLUTIONS
# ============================================

print("\n=== EXERCISES ===")

# --- EASY EXERCISES ---
print("\n--- Easy Exercises ---")

# Exercise 1: Create a set and add/remove elements
colors = {"red", "green", "blue"}
colors.add("yellow")
colors.discard("green")
print(f"1. Colors: {colors}")

# Exercise 2: Remove duplicates from a list
nums = [1, 1, 2, 3, 3, 4, 5, 5, 5]
unique = list(set(nums))
print(f"2. Unique numbers: {unique}")

# Exercise 3: Check membership
languages = {"python", "java", "javascript", "rust"}
print(f"3. 'python' in set: {'python' in languages}")
print(f"   'go' in set: {'go' in languages}")

# Exercise 4: Find length of a set
letters = set("mississippi")
print(f"4. Unique letters in 'mississippi': {letters} → count: {len(letters)}")

# Exercise 5: Create set from user input (simulated)
csv_data = "apple,banana,apple,cherry,banana"
items = set(csv_data.split(","))
print(f"5. Unique items: {items}")

# --- MEDIUM EXERCISES ---
print("\n--- Medium Exercises ---")

# Exercise 6: Find common elements between two lists
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
common = set(list_a) & set(list_b)
print(f"6. Common elements: {common}")

# Exercise 7: Find elements in list_a but not in list_b
only_a = set(list_a) - set(list_b)
print(f"7. Only in list_a: {only_a}")

# Exercise 8: Check if one set is a subset of another
required_skills = {"python", "sql"}
candidate_skills = {"python", "sql", "docker", "aws"}
has_required = required_skills.issubset(candidate_skills)
print(f"8. Candidate has required skills: {has_required}")

# Exercise 9: Remove duplicates from list while preserving order
ordered_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
seen = set()
ordered_unique = []
for item in ordered_list:
    if item not in seen:
        seen.add(item)
        ordered_unique.append(item)
print(f"9. Order-preserved unique: {ordered_unique}")

# Exercise 10: Count unique words in a sentence
sentence = "the cat sat on the mat the cat"
unique_words = set(sentence.split())
print(f"10. Unique words: {unique_words} → count: {len(unique_words)}")

# --- HARD EXERCISES ---
print("\n--- Hard Exercises ---")

# Exercise 11: Find elements that appear in exactly 2 out of 3 sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = {4, 5, 6, 7}
# Element must be in exactly 2 sets
in_exactly_two = set()
for item in a | b | c:
    count = (item in a) + (item in b) + (item in c)
    if count == 2:
        in_exactly_two.add(item)
print(f"11. In exactly 2 sets: {in_exactly_two}")

# Exercise 12: Choosing the right data structure
# Problem: Track unique IP addresses and count total visits
visits = [
    "192.168.1.1", "10.0.0.1", "192.168.1.1",
    "172.16.0.1", "10.0.0.1", "192.168.1.1"
]
unique_ips = set(visits)          # SET for unique IPs
total_visits = len(visits)        # LIST length for total count
print(f"12. Unique IPs: {unique_ips}")
print(f"    Total visits: {total_visits}, Unique visitors: {len(unique_ips)}")

# Exercise 13: Set comprehension + data structure conversion
# Find all unique first letters from a list of names
names = ["Alice", "Bob", "Anna", "Charlie", "Ben", "Catherine"]
first_letters = {name[0] for name in names}  # set comprehension
# Convert to sorted list for display
print(f"13. Unique first letters: {sorted(first_letters)}")

# ============================================
# 6. PRACTICE EXERCISES (No Solutions — You Code!)
# ============================================

print("\n=== Practice Exercises (No Solutions - You Code!) ===")
print("""
Exercise 1: Symmetric difference
  - Given: set_x = {1, 2, 3, 4, 5} and set_y = {4, 5, 6, 7, 8}
  - Find elements that are in set_x OR set_y but NOT in both
  - Print the result

Exercise 2: Unique characters
  - Given two strings: "hello" and "world"
  - Find characters that appear in both strings
  - Find characters unique to each string
  - Print all results

Exercise 3: Data structure choice
  - You have a list of 1000 student IDs (with duplicates)
  - Task 1: Find how many UNIQUE students there are
  - Task 2: Check if student ID "S500" exists (use the fastest method)
  - Task 3: Store each student's name with their ID (pick the right structure)
  - Write code for all 3 tasks, explain WHY you chose each structure

Exercise 4: Set operations on dictionaries
  - dict1 = {"a": 1, "b": 2, "c": 3}
  - dict2 = {"b": 20, "c": 30, "d": 40}
  - Use set operations on dict KEYS to find:
    - Keys in both dicts
    - Keys only in dict1
    - All unique keys across both dicts

Exercise 5: Playlist manager
  - Create 3 playlists (sets) with song names
  - Find songs that appear in ALL playlists
  - Find songs unique to each playlist
  - Find total unique songs across all playlists
  - Recommend songs from playlist2 that aren't in playlist1

Exercise 6: List vs Set performance
  - Create a list and a set, both with numbers 0 to 99999
  - Check if 99999 exists in both
  - Use time module to measure which is faster
  - Print the time difference

Exercise 7: Data cleaning
  - Given: ["Apple", "apple", "APPLE", "Banana", "banana", "Cherry"]
  - Normalize to lowercase and remove duplicates
  - Store result as a sorted list
  - Print the clean list
""")

# ============================================
# 7. COMMON MISTAKES TO AVOID
# ============================================

print("\n=== Common Mistakes ===")

# Mistake 1: Creating empty set wrong
empty_dict = {}       # This is a DICT, not a set!
empty_set = set()     # THIS is an empty set
print(f"type({{}}): {type(empty_dict)}")
print(f"type(set()): {type(empty_set)}")

# Mistake 2: Trying to index a set
my_set = {10, 20, 30}
# my_set[0]  # ERROR! Sets are unordered, no indexing
# Fix: convert to list first if you need indexing
print(f"First element (via list): {list(my_set)[0]}")

# Mistake 3: Adding mutable items to a set
# my_set.add([1, 2])  # ERROR! Lists are mutable, can't be in sets
# Fix: use tuples instead
my_set.add((1, 2))    # Tuples are immutable, OK in sets
print(f"Set with tuple: {my_set}")

# Mistake 4: Assuming set order
# Sets are UNORDERED — don't rely on element order
s = {3, 1, 2}
print(f"Set order not guaranteed: {s}")  # might print in any order

# Mistake 5: Using remove() on missing element
# my_set.remove(999)  # ERROR! KeyError
# Fix: use discard() — no error if missing
my_set.discard(999)
print(f"discard() is safe: {my_set}")

# ============================================
# 8. QUICK REFERENCE
# ============================================

print("\n=== Quick Reference ===")
print("""
CREATE:         s = {1, 2, 3} or s = set()
ADD:            s.add(item)
REMOVE:         s.remove(item)     ← error if missing
SAFE REMOVE:    s.discard(item)    ← no error if missing
POP:            s.pop()            ← removes random element
CLEAR:          s.clear()
LENGTH:         len(s)
MEMBERSHIP:     item in s          ← O(1) fast!

UNION:          a | b              or a.union(b)
INTERSECTION:   a & b              or a.intersection(b)
DIFFERENCE:     a - b              or a.difference(b)
SYM DIFF:       a ^ b              or a.symmetric_difference(b)
SUBSET:         a <= b             or a.issubset(b)
SUPERSET:       a >= b             or a.issuperset(b)
DISJOINT:       a.isdisjoint(b)

COMPREHENSION:  {x for x in iterable if condition}
FROZENSET:      frozenset([1, 2, 3])  ← immutable set

DATA STRUCTURE CHEAT SHEET:
  List  → ordered, duplicates OK, indexed       → [1, 2, 3]
  Tuple → ordered, immutable, duplicates OK     → (1, 2, 3)
  Dict  → key-value pairs, fast key lookup      → {"a": 1}
  Set   → unordered, unique only, fast lookup   → {1, 2, 3}
""")
