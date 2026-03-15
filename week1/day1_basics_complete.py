# Day 1: Variables, Data Types & Operators - Complete Guide
# ===========================================================
# OVERVIEW
# ===========================================================
"""
📅 Day 1 of 70 — Week 1: Python Fundamentals
📌 Topic: Variables, Data Types & Operators

🎯 WHAT YOU WILL LEARN TODAY:
  1. What Python is and how it works
  2. What print() is and how to display text on screen
  3. What quotes are and why we use them
  4. What variables are and how to create them
  5. What = (assignment) means
  6. The 5 basic data types: int, float, str, bool, None
  7. What f-strings are and how to use them
  8. What type() and .__name__ are
  9. Arithmetic operators: + - * / // % **
  10. Comparison operators: == != > < >= <=
  11. Logical operators: and, or, not
  12. Type conversion: int(), float(), str(), bool()
  13. Chained comparisons: 18 <= age <= 65
  14. Multiple assignment: x = y = z = 10

💡 WHY IT MATTERS:
  - Variables are the foundation of ALL programming
  - Every program stores and manipulates data
  - Operators let you do math, compare values, and make decisions
  - You will use these concepts EVERY SINGLE DAY as a developer

⏱️ ESTIMATED TIME: 2-3 hours
"""

# ============================================
# 1. COMPLETE EXPLANATION
# ============================================

"""
WHAT IS PYTHON?
- Python is a programming language — a way to give instructions to a computer
- You write instructions (called "code"), and the computer follows them
- Think of it like writing a recipe — step by step, the computer does what you say

WHAT IS print()?
- print() is a FUNCTION (a ready-made tool Python gives you)
- It displays text on the screen
- The parentheses () are like a mouth — you put what you want to say inside them
- Example: print("Hello") → shows: Hello

WHAT ARE QUOTES (" " or ' ')?
- Quotes tell Python: "this is text, not code"
- Without quotes, Python thinks it's a variable or command
- You can use double quotes "hello" or single quotes 'hello' — both work the same

WHAT IS A VARIABLE?
- A variable is a NAME that stores a VALUE
- Think of it like a labeled jar:
    - The label is the variable name
    - What's inside the jar is the value
- Example: name = "Alice"
    - "name" is the label (variable name)
    - "Alice" is what's inside (value)
    - "=" means "put this value into this variable" (assignment)

WHAT IS = (EQUALS SIGN)?
- In Python, = does NOT mean "is equal to"
- It means "ASSIGN" — put the value on the right INTO the variable on the left
- Think of it like: name ← "Alice" (put Alice into name)
- Example: age = 25 means "store 25 inside the variable called age"

WHAT ARE DATA TYPES?
- Every value in Python has a TYPE — what kind of data it is
- Just like in real life: a number, a word, a yes/no answer are different types
- Python figures out the type automatically (called "dynamic typing")

THE 5 BASIC DATA TYPES:
- int   → Integer → Whole numbers (no decimal point)
         Examples: 1, 42, -10, 0, 1000
         Real life: age, year, count of items

- float → Floating point → Numbers WITH a decimal point
         Examples: 3.14, -0.5, 100.0
         Real life: price, height, temperature

- str   → String → Text (letters, words, sentences)
         Examples: "hello", 'world', "123" (yes, numbers in quotes are strings!)
         Real life: name, address, message
         MUST be inside quotes!

- bool  → Boolean → Only two values: True or False
         Examples: True, False (capital T and F!)
         Real life: is_student? yes/no, is_raining? yes/no

- None  → NoneType → Means "nothing" or "no value"
         Example: None (capital N!)
         Real life: a form field left blank

WHAT IS AN f-STRING?
- f-string = "formatted string" — a special string that lets you put variables inside it
- You add the letter f before the quotes: f"..."
- Then use curly braces {} to insert variables
- Example:
    name = "Alice"
    print(f"Hello {name}")  → shows: Hello Alice
- Without f: print("Hello {name}") → shows: Hello {name} (literally!)

WHAT IS type()?
- type() is a function that tells you WHAT TYPE a value is
- Example: type("hello") → <class 'str'>
- The output <class 'str'> looks ugly, so we use .__name__ to get just "str"

WHAT IS .__name__?
- It's a special attribute (a property) that every type has
- It gives you just the CLEAN NAME of the type
- type("hello").__name__ → "str" (clean!)
- The dot (.) means "go inside this thing and get something from it"
- __name__ (with double underscores) is a built-in property Python creates automatically
- You ALWAYS use .__name__ — it never changes to match your variable name

WHAT ARE OPERATORS?
- Operators are SYMBOLS that perform actions on values
- Just like math symbols: + adds, - subtracts
- Three main types:
    1. Arithmetic operators: do math (+, -, *, /, //, %, **)
    2. Comparison operators: compare values (==, !=, >, <, >=, <=)
    3. Logical operators: combine True/False values (and, or, not)

ARITHMETIC OPERATORS:
- +   Addition        → 5 + 3 = 8
- -   Subtraction     → 5 - 3 = 2
- *   Multiplication  → 5 * 3 = 15
- /   Division        → 5 / 3 = 1.6667 (always gives float/decimal)
- //  Floor Division  → 5 // 3 = 1 (cuts off the decimal, rounds DOWN)
- %   Modulus         → 5 % 3 = 2 (gives the REMAINDER after division)
- **  Exponent/Power  → 5 ** 3 = 125 (5 × 5 × 5)

COMPARISON OPERATORS (always return True or False):
- ==  Equal to        → 5 == 5 → True   (is 5 equal to 5? yes!)
- !=  Not equal to    → 5 != 3 → True   (is 5 not equal to 3? yes!)
- >   Greater than    → 5 > 3  → True
- <   Less than       → 5 < 3  → False
- >=  Greater or equal → 5 >= 5 → True
- <=  Less or equal   → 5 <= 3 → False
NOTE: == (double equals) checks equality. = (single equals) assigns a value. Don't mix them!

LOGICAL OPERATORS (combine True/False):
- and → Both must be True     → True and False → False
- or  → At least one is True  → True or False  → True
- not → Flips the value       → not True → False
"""

# ============================================
# 2. MULTIPLE EXAMPLES (Minimum 3)
# ============================================

# --- EXAMPLE 1: Basic Variables (Simple) ---

# print() displays text on screen
# "===" is just decoration to make output look nice
print("=== EXAMPLE 1: Basic Variables ===")

# Creating variables — storing values in named containers
# variable_name = value
name = "Alice"          # str (string) — text inside quotes
age = 25               # int (integer) — whole number, no decimal
height = 5.6           # float — number WITH a decimal point
is_student = True      # bool (boolean) — True or False (capital T/F!)
middle_name = None     # NoneType — means "no value" or "empty"

# Now let's print each variable with its type
# f"..." = f-string, lets us put variables inside {} curly braces
# {name} = replaced with the VALUE of name → "Alice"
# {type(name).__name__} = gets the TYPE name → "str"
#   - type(name) → <class 'str'> (ugly)
#   - .__name__ → "str" (clean)
print(f"Name: {name} (type: {type(name).__name__})")
# Output: Name: Alice (type: str)

print(f"Age: {age} (type: {type(age).__name__})")
# Output: Age: 25 (type: int)

print(f"Height: {height} (type: {type(height).__name__})")
# Output: Height: 5.6 (type: float)

print(f"Is Student: {is_student} (type: {type(is_student).__name__})")
# Output: Is Student: True (type: bool)

print(f"Middle Name: {middle_name} (type: {type(middle_name).__name__})")
# Output: Middle Name: None (type: NoneType)


# --- EXAMPLE 2: Real-World Scenario (Intermediate) ---

# \n = "new line" — adds a blank line before the text (for spacing)
print("\n=== EXAMPLE 2: Shopping Calculator ===")

# Imagine you're buying items at a store
item_price = 29.99     # float — price of one item ($29.99)
quantity = 3           # int — how many items you're buying
tax_rate = 0.08        # float — 8% tax (8 ÷ 100 = 0.08)

# * means multiply
subtotal = item_price * quantity    # 29.99 × 3 = 89.97
tax = subtotal * tax_rate           # 89.97 × 0.08 = 7.1976
total = subtotal + tax              # 89.97 + 7.1976 = 97.1676

# $ is just a text character — Python doesn't treat it as money
# :.2f means "show only 2 decimal places" (f = float format)
#   - 89.97 → 89.97 (already 2 decimals)
#   - 7.1976 → 7.20 (rounded to 2 decimals)
#   - 97.1676 → 97.17 (rounded to 2 decimals)
print(f"Item Price: ${item_price}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (8%): ${tax:.2f}")
print(f"Total: ${total:.2f}")


# --- EXAMPLE 3: Advanced Application (Complex) ---

print("\n=== EXAMPLE 3: Student Report Card ===")

# All 5 data types used together in one real scenario
student_name = "Bob"       # str
student_age = 17           # int
gpa = 3.85                 # float
is_graduated = False       # bool
nickname = None            # NoneType — no nickname assigned yet

# Arithmetic operators — calculating scores
math_score = 88
science_score = 92
english_score = 79
total = math_score + science_score + english_score   # + addition
average = total / 3                                   # / division → float
highest = math_score if math_score > science_score else science_score  # > comparison

# Comparison operators — checking performance
is_passing = average >= 60          # >= greater or equal
is_honor_roll = average >= 90       # >= greater or equal
is_failing = average < 60           # < less than
is_average_student = average != 100 # != not equal

# Logical operators — combining conditions
# and → both must be True
can_graduate = is_passing and student_age >= 17
# or → at least one must be True
need_support = is_failing or gpa < 2.0
# not → flips True to False
is_not_graduated = not is_graduated

# Chained comparison — is average between 80 and 90?
is_good_student = 80 <= average <= 90

# Type conversion — converting types
age_as_string = str(student_age)         # int → str: 17 → "17"
gpa_as_int = int(gpa)                    # float → int: 3.85 → 3 (cuts decimal!)
score_from_string = int("95")            # str → int: "95" → 95

# \n = new line (blank line for spacing)
print(f"Student: {student_name} (type: {type(student_name).__name__})")
print(f"Age: {student_age} (type: {type(student_age).__name__})")
print(f"GPA: {gpa} (type: {type(gpa).__name__})")
print(f"Graduated: {is_graduated} (type: {type(is_graduated).__name__})")
print(f"Nickname: {nickname} (type: {type(nickname).__name__})")
print(f"\nAverage Score: {average:.2f}")   # :.2f → 2 decimal places
print(f"Is Passing: {is_passing}")
print(f"Is Honor Roll: {is_honor_roll}")
print(f"Can Graduate: {can_graduate}")
print(f"Needs Support: {need_support}")
print(f"Not Yet Graduated: {is_not_graduated}")
print(f"Is Good Student (80-90): {is_good_student}")
print(f"\nType Conversion:")
print(f"  Age as string: '{age_as_string}' (type: {type(age_as_string).__name__})")
print(f"  GPA as int: {gpa_as_int} (type: {type(gpa_as_int).__name__})")
print(f"  Score from string: {score_from_string} (type: {type(score_from_string).__name__})")


# ============================================
# 3. COMPREHENSIVE EXERCISES (Easy + Medium + Hard + Bonus)
# ============================================

print("\n=== EXERCISES ===")

# --- EASY EXERCISES (Basic Understanding) ---
print("\n--- Easy Exercises ---")

# Exercise 1: Create variables for personal info and calculate age
first_name = "John"        # str — first name
last_name = "Doe"          # str — last name
birth_year = 2000          # int — year of birth
current_year = 2024        # int — current year

# {current_year - birth_year} → Python does the math INSIDE the curly braces
# 2024 - 2000 = 24
print(f"1. Full Name: {first_name} {last_name}, Age: {current_year - birth_year}")

# Exercise 2: Calculate rectangle area and perimeter
length = 5   # int — length of rectangle
width = 3    # int — width of rectangle

# Area = length × width
area = length * width              # 5 × 3 = 15

# Perimeter = 2 × (length + width)
# () makes Python add first, then multiply
perimeter = 2 * (length + width)   # 2 × (5 + 3) = 2 × 8 = 16

print(f"2. Rectangle - Area: {area}, Perimeter: {perimeter}")

# Exercise 3: Check if a number is even
number = 8

# % (modulus) gives the remainder after division
# 8 ÷ 2 = 4 remainder 0 → so 8 % 2 = 0
# If remainder is 0, the number is even
# == checks "is equal to?" → 0 == 0 → True
is_even = number % 2 == 0   # True

print(f"3. {number} is even: {is_even}")

# Exercise 4: Swap two variables
x, y = 10, 20
print(f"4. Before swap: x={x}, y={y}")

# Python lets you swap in one line!
# It reads the right side first (y=20, x=10), then assigns
x, y = y, x   # Now x=20, y=10

print(f"   After swap: x={x}, y={y}")

# Exercise 5: Calculate average of 3 numbers
num1, num2, num3 = 85, 90, 88

# Average = sum of all numbers ÷ count of numbers
# (85 + 90 + 88) = 263, then 263 ÷ 3 = 87.6667
average = (num1 + num2 + num3) / 3

# :.2f → show 2 decimal places → 87.67
print(f"5. Average of {num1}, {num2}, {num3}: {average:.2f}")


# --- MEDIUM EXERCISES (Apply Concepts) ---
print("\n--- Medium Exercises ---")

# Exercise 6: BMI Calculator
# BMI = weight (kg) ÷ height (meters) squared
weight_kg = 70     # float — weight in kilograms
height_m = 1.75    # float — height in meters

# ** 2 means "to the power of 2" (squared)
# height_m ** 2 = 1.75 × 1.75 = 3.0625
# 70 ÷ 3.0625 = 22.857...
bmi = weight_kg / (height_m ** 2)

print(f"6. BMI: {bmi:.2f}")

# Exercise 7: Compound interest
# Formula: Amount = Principal × (1 + rate) ^ time
principal = 1000   # Starting money ($1000)
rate = 0.05        # 5% interest (5 ÷ 100 = 0.05)
time = 3           # 3 years

# (1 + 0.05) = 1.05
# 1.05 ** 3 = 1.05 × 1.05 × 1.05 = 1.157625
# 1000 × 1.157625 = 1157.625
amount = principal * (1 + rate) ** time
interest = amount - principal   # 1157.625 - 1000 = 157.625

print(f"7. Principal: ${principal}, Interest: ${interest:.2f}, Total: ${amount:.2f}")

# Exercise 8: Check voting eligibility
age = 18
is_citizen = True

# AND → both conditions must be True
# Is age >= 18? → 18 >= 18 → True
# Is is_citizen True? → True
# True AND True → True
can_vote = age >= 18 and is_citizen

print(f"8. Age: {age}, Citizen: {is_citizen}, Can vote: {can_vote}")

# Exercise 9: Calculate discount
original_price = 100
discount_percent = 20

# 20 / 100 = 0.2, then 100 × 0.2 = 20
discount_amount = original_price * (discount_percent / 100)

# 100 - 20 = 80
final_price = original_price - discount_amount

print(f"9. Original: ${original_price}, Discount: {discount_percent}%, Final: ${final_price}")

# Exercise 10: Time conversion (seconds → hours, minutes, seconds)
total_seconds = 3665

# // (floor division) gives whole number, % (modulus) gives remainder
# 3665 // 3600 = 1 (1 full hour)
hours = total_seconds // 3600

# 3665 % 3600 = 65 (leftover seconds after removing hours)
# 65 // 60 = 1 (1 full minute)
minutes = (total_seconds % 3600) // 60

# 3665 % 60 = 5 (leftover seconds after removing minutes)
seconds = total_seconds % 60

print(f"10. {total_seconds} seconds = {hours}h {minutes}m {seconds}s")


# --- HARD EXERCISES (Combine Concepts) ---
print("\n--- Hard Exercises ---")

# Exercise 11: Quadratic equation solver (ax² + bx + c = 0)
# A quadratic equation looks like: 1x² + (-5)x + 6 = 0
a, b, c = 1, -5, 6

# Discriminant tells us if the equation has real solutions
# Formula: b² - 4ac
# (-5)² - 4(1)(6) = 25 - 24 = 1
discriminant = b**2 - 4*a*c

# If discriminant >= 0, real roots exist
has_real_roots = discriminant >= 0   # 1 >= 0 → True

print(f"11. Equation: {a}x² + {b}x + {c} = 0")
print(f"    Discriminant: {discriminant}, Has real roots: {has_real_roots}")

# if = "only run this code IF the condition is True"
if has_real_roots:
    # ** 0.5 means "square root" (raising to power 0.5)
    # root1 = (-(-5) + √1) / (2×1) = (5 + 1) / 2 = 3.0
    root1 = (-b + discriminant**0.5) / (2*a)
    # root2 = (-(-5) - √1) / (2×1) = (5 - 1) / 2 = 2.0
    root2 = (-b - discriminant**0.5) / (2*a)
    print(f"    Roots: {root1}, {root2}")

# Exercise 12: Leap year checker
year = 2024

# A year is a leap year if:
#   - Divisible by 4 AND NOT divisible by 100
#   - OR divisible by 400
# "divisible by 4" means year % 4 == 0 (no remainder)
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
# 2024 % 4 == 0 → True, 2024 % 100 != 0 → True → True AND True → True

print(f"12. {year} is a leap year: {is_leap}")

# Exercise 13: Circle calculations
# import = bring in a ready-made toolbox
# math = Python's math toolbox (has pi, square root, etc.)
import math

radius = 5

# math.pi = 3.14159... (the dot means "get pi FROM the math toolbox")
# Circumference = 2 × π × radius = 2 × 3.14159 × 5 = 31.42
circumference = 2 * math.pi * radius

# Area = π × radius² = 3.14159 × 25 = 78.54
area = math.pi * radius ** 2

diameter = 2 * radius   # 2 × 5 = 10

print(f"13. Circle (radius={radius}): Area={area:.2f}, Circumference={circumference:.2f}")


# --- BONUS CHALLENGES ---
print("\n--- Bonus Challenges ---")

# Bonus 1: Multiple assignment — give the SAME value to multiple variables
# This is a shortcut for: x = 10, y = 10, z = 10
x = y = z = 10
print(f"Bonus 1. x={x}, y={y}, z={z}")

# Bonus 2: Chained comparison
# Python lets you chain comparisons like in math: 18 ≤ 25 ≤ 65
age = 25
is_adult_range = 18 <= age <= 65   # Is 25 between 18 and 65? → True
print(f"Bonus 2. Age {age} in adult range (18-65): {is_adult_range}")

# Bonus 3: Type conversion — changing one type to another
# int() converts to integer, float() converts to float
str_num = "42"              # This is a STRING (text), not a number!
int_num = int(str_num)      # Convert string "42" → integer 42
float_num = float(str_num)  # Convert string "42" → float 42.0
print(f"Bonus 3. String '{str_num}' -> int: {int_num}, float: {float_num}")


# ============================================
# 4. PRACTICE TIPS
# ============================================

print("\n=== Practice Tips ===")
print("""
TIP 1 — Naming variables:
  - Use lowercase with underscores: first_name, not FirstName or firstname
  - Make names descriptive: total_price, not tp
  - Don't use Python keywords as names: (if, for, while, print, etc.)

TIP 2 — Order of operations (PEMDAS):
  - Python follows math rules: () first, then **, then * / // %, then + -
  - When in doubt, use () to be explicit: (a + b) * c

TIP 3 — Floats are not always exact:
  - 0.1 + 0.2 = 0.30000000000000004 (not exactly 0.3!)
  - Use :.2f to round when displaying: print(f"{0.1 + 0.2:.2f}") → 0.30

TIP 4 — None is not zero:
  - None means "no value" — it's NOT 0, NOT False, NOT empty string
  - None == 0 → False
  - None == False → False

COMMON MISTAKES:
  1. Never divide by zero — always check first
  2. Always create (define) a variable BEFORE using it
  3. 5 / 2 = 2.5 (decimal),  5 // 2 = 2 (whole number) — don't mix them
  4. '5' == 5 → False — string vs int are never equal
  5. Use = to assign, == to compare — don't mix them!
  6. Always put quotes around text (strings)

QUICK REFERENCE:
  Variable:   name = "Alice"        age = 25
  Types:      int  float  str  bool  None
  Arithmetic: +  -  *  /  //  %  **
  Comparison: ==  !=  >  <  >=  <=
  Logical:    and  or  not
  Convert:    int()  float()  str()  bool()
  f-string:   f"Hello {name}"
  Type name:  type(x).__name__
  Decimals:   f"{value:.2f}"
  New line:   \\n

NEXT TOPICS:
  - Day 2: Strings — slicing, methods, formatting
  - Day 3: Conditionals — if / elif / else
  - Day 4: Lists — storing multiple values
""")


# ============================================
# 5. PRACTICE EXERCISES (Write Code Yourself — No Solutions!)
# ============================================

print("\n=== Practice Exercises (No Solutions - You Code!) ===")
print("""
Exercise 1: Variables + All 5 Data Types + f-string + type()
  - Create 5 variables: product_name (str), price (float),
    quantity (int), in_stock (bool), discount_code (None)
  - Print each variable with its value AND type using type().__name__

Exercise 2: Arithmetic Operators (all 7)
  - Given a = 20, b = 6
  - Calculate and print: +, -, *, /, //, %, **
  - Show the result of each with a label

Exercise 3: Comparison Operators (all 6)
  - Given score = 75
  - Use all 6 operators (==, !=, >, <, >=, <=) to compare score with 75 and 80
  - Print each result with a label

Exercise 4: Logical Operators (and, or, not)
  - has_passport = True, has_visa = False, is_banned = False
  - Can travel? → needs passport AND visa
  - Can enter? → passport OR visa
  - Is allowed? → not is_banned
  - Print all 3 results

Exercise 5: Type Conversion
  - Start with: user_age = "28", temperature = 36.9, is_active = 1
  - Convert user_age to int, temperature to int, is_active to bool
  - Print each before and after conversion with types

Exercise 6: Chained Comparison + None
  - Given speed = 85
  - Check if speed is in safe range: 60 <= speed <= 120
  - Create a variable fine = None (no fine yet)
  - Print speed, safe range result, and fine with its type

Exercise 7: Combine Everything
  - Create a student: name (str), grade (float), age (int),
    passed (bool), notes (None)
  - Calculate: is grade between 50 and 100? (chained comparison)
  - Check: passed AND age >= 18 (logical and)
  - Check: grade < 50 OR grade > 100 (logical or)
  - Convert grade to int
  - Print everything with types using f-strings and :.2f
""")

