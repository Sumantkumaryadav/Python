# Day 7: Functions — Parameters, Return, Default Args
# ====================================================

# ============================================
# 1. COMPLETE EXPLANATION
# ============================================

"""
WHAT IS A FUNCTION?
- A reusable block of code that performs a specific task
- You define it once, call it as many times as you want
- Like a recipe: give it ingredients (parameters), it gives you a dish (return value)

WHY USE FUNCTIONS?
- Avoid repeating code (DRY — Don't Repeat Yourself)
- Break complex problems into smaller, manageable pieces
- Make code readable and organized
- Easier to test and debug

SYNTAX:
    def function_name(parameters):
        '''docstring — what the function does'''
        # code here
        return result

KEY CONCEPTS:
- Parameters: variables listed in the function definition
- Arguments: actual values passed when calling the function
- Return: sends a value back to the caller
- Default args: parameters with pre-set values (used if no argument given)
- None: returned if no explicit return statement
"""

# ============================================
# 2. EXAMPLES (3 Required)
# ============================================

# --- EXAMPLE 1: Basic Functions (Simple) ---
print("=== EXAMPLE 1: Basic Functions ===")

# Function with no parameters, no return
def greet():
    print("Hello, World!")

greet()  # Call the function

# Function with parameter
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

# Function with return value
def add(a, b):
    return a + b

result = add(3, 5)
print(f"3 + 5 = {result}")

# Return vs Print — IMPORTANT DIFFERENCE
def add_print(a, b):
    print(a + b)  # prints but returns None

def add_return(a, b):
    return a + b  # returns value, doesn't print

add_print(3, 5)           # prints 8, but can't use the result
x = add_return(3, 5)      # doesn't print, but x = 8
print(f"Stored result: {x}")

# What happens without return?
def no_return():
    x = 10  # does something but doesn't return

result = no_return()
print(f"No return gives: {result}")  # None

# --- EXAMPLE 2: Default Arguments & Multiple Returns (Intermediate) ---
print("\n=== EXAMPLE 2: Default Args & Multiple Returns ===")

# Default arguments — used when no value is provided
def power(base, exponent=2):
    """Raise base to exponent. Defaults to squaring."""
    return base ** exponent

print(f"power(3): {power(3)}")        # uses default exponent=2 → 9
print(f"power(3, 3): {power(3, 3)}")  # overrides default → 27
print(f"power(2, 10): {power(2, 10)}")  # 1024

# Multiple default arguments
def create_profile(name, age=25, city="Unknown", active=True):
    return {
        "name": name,
        "age": age,
        "city": city,
        "active": active
    }

# Different ways to call it
print(create_profile("Alice"))                          # all defaults
print(create_profile("Bob", 30))                        # override age
print(create_profile("Charlie", city="NYC"))             # skip age, set city
print(create_profile("David", 28, "London", False))     # override all

# Returning multiple values (actually returns a tuple)
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 7, 2, 9])
print(f"Min: {low}, Max: {high}")

# Returning different types based on condition
def divide(a, b):
    if b == 0:
        return None  # can't divide by zero
    return a / b

print(f"10 / 3 = {divide(10, 3)}")
print(f"10 / 0 = {divide(10, 0)}")

# --- EXAMPLE 3: Real-World Application (Advanced) ---
print("\n=== EXAMPLE 3: Grade Calculator ===")

def calculate_grade(scores, curve=0, passing=60):
    """
    Calculate average grade with optional curve.
    Returns: (average, letter_grade, passed)
    """
    if not scores:
        return 0, "N/A", False

    average = sum(scores) / len(scores) + curve

    if average >= 90:
        letter = "A"
    elif average >= 80:
        letter = "B"
    elif average >= 70:
        letter = "C"
    elif average >= 60:
        letter = "D"
    else:
        letter = "F"

    passed = average >= passing
    return round(average, 1), letter, passed

# Student grades
alice_scores = [85, 92, 78, 90, 88]
bob_scores = [55, 62, 48, 70, 58]

avg, grade, passed = calculate_grade(alice_scores)
print(f"Alice: {avg}% ({grade}) — {'Passed' if passed else 'Failed'}")

avg, grade, passed = calculate_grade(bob_scores)
print(f"Bob: {avg}% ({grade}) — {'Passed' if passed else 'Failed'}")

# With curve
avg, grade, passed = calculate_grade(bob_scores, curve=10)
print(f"Bob (with +10 curve): {avg}% ({grade}) — {'Passed' if passed else 'Failed'}")

# ============================================
# 3. POSITIONAL vs KEYWORD ARGUMENTS
# ============================================

print("\n=== Positional vs Keyword Arguments ===")

def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

# Positional — order matters
describe_pet("dog", "Rex")

# Keyword — order doesn't matter
describe_pet(name="Whiskers", animal="cat")

# Mix — positional first, then keyword
describe_pet("hamster", name="Tiny")

# ============================================
# 4. COMMON PATTERNS
# ============================================

print("\n=== Common Function Patterns ===")

# Pattern 1: Early return (guard clause)
def get_discount(age):
    if age < 0:
        return 0  # invalid age, return early
    if age < 12:
        return 50  # kids: 50% off
    if age >= 65:
        return 30  # seniors: 30% off
    return 0  # everyone else: no discount

print(f"Age 8 discount: {get_discount(8)}%")
print(f"Age 30 discount: {get_discount(30)}%")
print(f"Age 70 discount: {get_discount(70)}%")

# Pattern 2: Function calling another function
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def format_temperature(celsius):
    f = celsius_to_fahrenheit(celsius)
    return f"{celsius}°C = {f}°F"

print(format_temperature(0))
print(format_temperature(100))
print(format_temperature(37))

# Pattern 3: Functions with lists
def filter_passing(students, threshold=60):
    """Return list of students who passed."""
    return [s for s in students if s["score"] >= threshold]

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 55},
    {"name": "Charlie", "score": 72},
    {"name": "David", "score": 48}
]

passed = filter_passing(students)
print(f"Passed: {[s['name'] for s in passed]}")

passed_70 = filter_passing(students, threshold=70)
print(f"Passed (70+): {[s['name'] for s in passed_70]}")

# ============================================
# 5. EXERCISES WITH SOLUTIONS
# ============================================

print("\n=== EXERCISES ===")

# --- EASY EXERCISES ---
print("\n--- Easy Exercises ---")

# Exercise 1: Write a function that returns the square of a number
def square(n):
    return n ** 2

print(f"1. square(5) = {square(5)}")
print(f"   square(12) = {square(12)}")

# Exercise 2: Write a function that checks if a number is even
def is_even(n):
    return n % 2 == 0

print(f"2. is_even(4) = {is_even(4)}")
print(f"   is_even(7) = {is_even(7)}")

# Exercise 3: Write a function that returns the larger of two numbers
def maximum(a, b):
    return a if a > b else b

print(f"3. maximum(10, 20) = {maximum(10, 20)}")
print(f"   maximum(50, 30) = {maximum(50, 30)}")

# Exercise 4: Write a greeting function with default name
def hello(name="World"):
    return f"Hello, {name}!"

print(f"4. hello() = {hello()}")
print(f"   hello('Alice') = {hello('Alice')}")

# Exercise 5: Write a function that counts vowels in a string
def count_vowels(text):
    return sum(1 for c in text.lower() if c in "aeiou")

print(f"5. count_vowels('Hello World') = {count_vowels('Hello World')}")

# --- MEDIUM EXERCISES ---
print("\n--- Medium Exercises ---")

# Exercise 6: Temperature converter with default direction
def convert_temp(temp, to_unit="F"):
    if to_unit.upper() == "F":
        return round((temp * 9/5) + 32, 1)
    return round((temp - 32) * 5/9, 1)

print(f"6. 100°C to F: {convert_temp(100)}")
print(f"   212°F to C: {convert_temp(212, 'C')}")

# Exercise 7: Function that returns stats about a list
def list_stats(numbers):
    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "average": round(sum(numbers) / len(numbers), 2),
        "min": min(numbers),
        "max": max(numbers)
    }

stats = list_stats([10, 20, 30, 40, 50])
print(f"7. Stats: {stats}")

# Exercise 8: Password validator with configurable rules
def validate_password(password, min_length=8, require_digit=True):
    if len(password) < min_length:
        return False, f"Too short (min {min_length})"
    if require_digit and not any(c.isdigit() for c in password):
        return False, "Must contain a digit"
    return True, "Valid"

valid, msg = validate_password("hello")
print(f"8. 'hello': {msg}")
valid, msg = validate_password("hello123")
print(f"   'hello123': {msg}")
valid, msg = validate_password("hi", min_length=2, require_digit=False)
print(f"   'hi' (relaxed): {msg}")

# Exercise 9: Function that builds a formatted receipt
def create_receipt(items, tax_rate=0.08):
    subtotal = sum(price for _, price in items)
    tax = round(subtotal * tax_rate, 2)
    total = round(subtotal + tax, 2)
    return subtotal, tax, total

items = [("Coffee", 4.50), ("Sandwich", 8.00), ("Cookie", 2.50)]
sub, tax, total = create_receipt(items)
print(f"9. Subtotal: ${sub}, Tax: ${tax}, Total: ${total}")

# Exercise 10: Fibonacci function
def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

print(f"10. First 10 Fibonacci: {fibonacci(10)}")

# --- HARD EXERCISES ---
print("\n--- Hard Exercises ---")

# Exercise 11: Function composition — apply multiple functions
def apply_all(value, *functions):
    for func in functions:
        value = func(value)
    return value

result = apply_all(5, square, lambda x: x + 1, lambda x: x * 2)
print(f"11. apply_all(5, square, +1, *2) = {result}")  # 5→25→26→52

# Exercise 12: Memoized function (manual caching)
def make_counter():
    counts = {}
    def count_calls(name):
        counts[name] = counts.get(name, 0) + 1
        return counts[name]
    return count_calls, counts

counter, all_counts = make_counter()
counter("login")
counter("login")
counter("logout")
counter("login")
print(f"12. Call counts: {all_counts}")

# Exercise 13: Build a simple calculator using functions
def calculator(a, b, operation="add"):
    ops = {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b if b != 0 else None
    }
    return ops.get(operation, "Invalid operation")

print(f"13. calc(10, 3, 'add') = {calculator(10, 3, 'add')}")
print(f"    calc(10, 3, 'multiply') = {calculator(10, 3, 'multiply')}")
print(f"    calc(10, 0, 'divide') = {calculator(10, 0, 'divide')}")

# ============================================
# 6. PRACTICE EXERCISES (No Solutions — You Code!)
# ============================================

print("\n=== Practice Exercises (No Solutions - You Code!) ===")
print("""
Exercise 1: BMI Calculator
  - Write a function bmi(weight_kg, height_m)
  - Return the BMI value rounded to 1 decimal
  - Add a default parameter for unit system ("metric" or "imperial")
  - For imperial: weight in lbs, height in inches, formula: (weight / height^2) * 703

Exercise 2: Word counter
  - Write a function that takes a sentence and returns a dictionary
  - Keys = words, values = how many times each word appears
  - Add a default parameter ignore_case=True

Exercise 3: Tip calculator
  - Write a function tip(bill, tip_percent=15, split=1)
  - Return: tip amount, total, and per-person amount
  - Handle edge cases: negative bill, zero split

Exercise 4: Number classifier
  - Write a function that takes a number and returns a string:
    "positive even", "positive odd", "negative even", "negative odd", or "zero"
  - Use early returns (guard clauses)

Exercise 5: List processor
  - Write a function process_grades(grades, drop_lowest=False, curve=0)
  - If drop_lowest is True, remove the lowest grade before averaging
  - Apply curve to the final average
  - Return: (average, letter_grade, original_count, final_count)

Exercise 6: String formatter
  - Write a function format_name(first, last, style="full")
  - style="full" → "John Smith"
  - style="formal" → "Smith, John"
  - style="initial" → "J. Smith"
  - Handle empty strings gracefully

Exercise 7: Shopping cart
  - Write a function add_item(cart, item, price, quantity=1)
  - Write a function cart_total(cart, discount=0)
  - Write a function cart_summary(cart) that prints a formatted receipt
  - cart is a list of dictionaries
""")

# ============================================
# 7. COMMON MISTAKES TO AVOID
# ============================================

print("\n=== Common Mistakes ===")

# Mistake 1: Mutable default argument (CLASSIC PYTHON TRAP)
# BAD:
def append_to_bad(item, lst=[]):
    lst.append(item)
    return lst

print(f"Bad: {append_to_bad(1)}")  # [1]
print(f"Bad: {append_to_bad(2)}")  # [1, 2] — NOT [2]! Same list reused!

# GOOD:
def append_to_good(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(f"Good: {append_to_good(1)}")  # [1]
print(f"Good: {append_to_good(2)}")  # [2] — fresh list each time

# Mistake 2: Forgetting return
def add_no_return(a, b):
    a + b  # calculates but doesn't return!

result = add_no_return(3, 5)
print(f"\nForgot return: {result}")  # None

# Mistake 3: Modifying a list inside a function (side effect)
def remove_negatives(numbers):
    # This modifies the ORIGINAL list!
    numbers[:] = [n for n in numbers if n >= 0]
    return numbers

original = [1, -2, 3, -4, 5]
cleaned = remove_negatives(original)
print(f"\nOriginal after function: {original}")  # [1, 3, 5] — modified!

# Better: return a new list
def remove_negatives_safe(numbers):
    return [n for n in numbers if n >= 0]

# Mistake 4: Putting default args before non-default args
# def bad_func(x=10, y):  # SyntaxError!
# def good_func(y, x=10):  # Correct — defaults come last

# ============================================
# 8. QUICK REFERENCE
# ============================================

print("\n=== Quick Reference ===")
print("""
DEFINE:       def func_name(params):
CALL:         func_name(args)
RETURN:       return value
MULTIPLE:     return a, b, c  →  x, y, z = func()
DEFAULT:      def func(x, y=10):
KEYWORD:      func(y=20, x=5)
DOCSTRING:    '''Description of function'''
NONE:         returned if no explicit return

RULES:
  - Default args must come AFTER non-default args
  - Never use mutable defaults (lists, dicts) — use None instead
  - Functions should do ONE thing well
  - Use descriptive names: calculate_tax() not ct()
  - Add docstrings for complex functions

PATTERNS:
  - Early return (guard clause) for edge cases
  - Functions calling other functions
  - Return dict/tuple for multiple values
  - Default args for optional configuration
""")
