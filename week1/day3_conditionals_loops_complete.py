# Day 3: Conditionals & Loops - Complete Guide
# ==============================================

# ============================================
# 1. COMPLETE EXPLANATION
# ============================================

"""
WHAT ARE CONDITIONALS?
- Conditionals allow your program to make decisions
- Execute different code based on conditions
- Use if, elif, else keywords

WHAT ARE LOOPS?
- Loops repeat code multiple times
- for loop: Iterate over sequences
- while loop: Repeat while condition is True

WHY ARE THEY IMPORTANT?
- Control program flow
- Avoid code repetition
- Process collections of data
- Implement complex logic

KEY CONCEPTS:
- Indentation matters in Python (4 spaces)
- Conditions evaluate to True or False
- break: Exit loop early
- continue: Skip to next iteration
"""

# ============================================
# 2. EXAMPLES (3 Required)
# ============================================

# --- EXAMPLE 1: Basic Conditionals & Loops (Simple) ---
print("=== EXAMPLE 1: Basic Conditionals & Loops ===")

# Simple if-else
age = 20
if age >= 18:
    print(f"Age {age}: You are an adult")
else:
    print(f"Age {age}: You are a minor")

# Simple for loop
print("\nCounting 1 to 5:")
for i in range(1, 6):
    print(f"Count: {i}")

# Simple while loop
print("\nCountdown:")
count = 3
while count > 0:
    print(count)
    count -= 1
print("Go!")

# --- EXAMPLE 2: Grade Calculator (Intermediate) ---
print("\n=== EXAMPLE 2: Grade Calculator ===")

students = [
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 85},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 65},
    {"name": "Eve", "score": 58}
]

for student in students:
    name = student["name"]
    score = student["score"]
    
    # Determine grade
    if score >= 90:
        grade = "A"
        status = "Excellent"
    elif score >= 80:
        grade = "B"
        status = "Good"
    elif score >= 70:
        grade = "C"
        status = "Average"
    elif score >= 60:
        grade = "D"
        status = "Below Average"
    else:
        grade = "F"
        status = "Fail"
    
    print(f"{name}: {score} -> Grade {grade} ({status})")

# --- EXAMPLE 3: Number Pattern Generator (Advanced) ---
print("\n=== EXAMPLE 3: Pattern Generator ===")

# Pattern 1: Right triangle
print("Pattern 1: Right Triangle")
for i in range(1, 6):
    print('*' * i)

# Pattern 2: Pyramid
print("\nPattern 2: Pyramid")
n = 5
for i in range(1, n + 1):
    spaces = ' ' * (n - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)

# Pattern 3: Number pyramid
print("\nPattern 3: Number Pyramid")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

# ============================================
# 3. CONDITIONALS IN DETAIL
# ============================================

print("\n=== Conditionals in Detail ===")

# Single if
temperature = 30
if temperature > 25:
    print(f"Temperature {temperature}°C: It's hot!")

# if-else
is_raining = True
if is_raining:
    print("Take an umbrella")
else:
    print("Enjoy the sunshine")

# if-elif-else chain
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Nested conditionals
age = 25
has_license = True
if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("Too young to drive")

# Multiple conditions
age = 20
is_student = True
if age >= 18 and is_student:
    print("Adult student discount available")

# Ternary operator (one-line if-else)
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# ============================================
# 4. FOR LOOPS IN DETAIL
# ============================================

print("\n=== For Loops in Detail ===")

# Loop through range
print("Range(5):")
for i in range(5):
    print(i, end=' ')
print()

# Range with start and end
print("\nRange(2, 7):")
for i in range(2, 7):
    print(i, end=' ')
print()

# Range with step
print("\nRange(0, 10, 2):")
for i in range(0, 10, 2):
    print(i, end=' ')
print()

# Loop through list
fruits = ["apple", "banana", "orange"]
print("\nFruits:")
for fruit in fruits:
    print(f"- {fruit}")

# Loop with enumerate (index + value)
print("\nEnumerated fruits:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Loop with enumerate starting from 1
print("\nEnumerated (start=1):")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# Loop through string
word = "Python"
print(f"\nLetters in '{word}':")
for char in word:
    print(char, end=' ')
print()

# Nested loops
print("\nMultiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end='\t')
    print()

# ============================================
# 5. WHILE LOOPS IN DETAIL
# ============================================

print("\n=== While Loops in Detail ===")

# Basic while loop
count = 1
print("Count to 5:")
while count <= 5:
    print(count, end=' ')
    count += 1
print()

# While with condition
number = 1
print("\nDouble until > 100:")
while number <= 100:
    print(number, end=' ')
    number *= 2
print()

# While with user input simulation
attempts = 0
max_attempts = 3
print(f"\nAttempts (max {max_attempts}):")
while attempts < max_attempts:
    attempts += 1
    print(f"Attempt {attempts}")
print("Done!")

# Infinite loop with break
print("\nFind first number divisible by 7:")
num = 50
while True:
    if num % 7 == 0:
        print(f"Found: {num}")
        break
    num += 1

# ============================================
# 6. LOOP CONTROL (break, continue, pass)
# ============================================

print("\n=== Loop Control ===")

# break: Exit loop
print("Break example (stop at 5):")
for i in range(1, 11):
    if i == 5:
        break
    print(i, end=' ')
print()

# continue: Skip iteration
print("\nContinue example (skip even):")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=' ')
print()

# pass: Do nothing (placeholder)
print("\nPass example:")
for i in range(3):
    if i == 1:
        pass  # TODO: implement later
    else:
        print(f"Processing {i}")

# else with loops (executes if loop completes normally)
print("\nLoop else:")
for i in range(3):
    print(i, end=' ')
else:
    print("Loop completed!")

# ============================================
# 7. EXERCISES
# ============================================

print("\n=== EXERCISES ===")

# --- EASY EXERCISES ---
print("\n--- Easy Exercises ---")

# Exercise 1: Check positive/negative/zero
num = -5
if num > 0:
    result = "positive"
elif num < 0:
    result = "negative"
else:
    result = "zero"
print(f"1. {num} is {result}")

# Exercise 2: Print numbers 1 to 10
print("2. Numbers 1-10:", end=' ')
for i in range(1, 11):
    print(i, end=' ')
print()

# Exercise 3: Sum of numbers 1 to 10
total = 0
for i in range(1, 11):
    total += i
print(f"3. Sum 1-10: {total}")

# Exercise 4: Print even numbers 1 to 20
print("4. Even numbers 1-20:", end=' ')
for i in range(2, 21, 2):
    print(i, end=' ')
print()

# Exercise 5: Countdown from 10 to 1
print("5. Countdown:", end=' ')
count = 10
while count > 0:
    print(count, end=' ')
    count -= 1
print()

# --- MEDIUM EXERCISES ---
print("\n--- Medium Exercises ---")

# Exercise 6: Multiplication table
num = 7
print(f"6. Multiplication table for {num}:")
for i in range(1, 11):
    print(f"   {num} x {i} = {num * i}")

# Exercise 7: Find factorial
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"7. Factorial of {n}: {factorial}")

# Exercise 8: Count vowels in string
text = "Hello World"
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(f"8. Vowels in '{text}': {count}")

# Exercise 9: FizzBuzz (1-15)
print("9. FizzBuzz:")
for i in range(1, 16):
    if i % 15 == 0:
        print("FizzBuzz", end=' ')
    elif i % 3 == 0:
        print("Fizz", end=' ')
    elif i % 5 == 0:
        print("Buzz", end=' ')
    else:
        print(i, end=' ')
print()

# Exercise 10: Find largest in list
numbers = [23, 45, 12, 67, 34]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(f"10. Largest in {numbers}: {largest}")

# --- HARD EXERCISES ---
print("\n--- Hard Exercises ---")

# Exercise 11: Prime number checker
num = 17
is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
print(f"11. {num} is prime: {is_prime}")

# Exercise 12: Fibonacci sequence (first 10)
print("12. Fibonacci (10 terms):", end=' ')
a, b = 0, 1
for _ in range(10):
    print(a, end=' ')
    a, b = b, a + b
print()

# Exercise 13: Nested loop - find pairs that sum to target
numbers = [1, 2, 3, 4, 5]
target = 7
print(f"13. Pairs in {numbers} that sum to {target}:")
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(f"   {numbers[i]} + {numbers[j]} = {target}")

# ============================================
# 8. BONUS CHALLENGES
# ============================================

print("\n=== Bonus Challenges ===")

# Bonus 1: List comprehension (alternative to loops)
squares = [x**2 for x in range(1, 6)]
print(f"Bonus 1. Squares: {squares}")

# Bonus 2: Nested list comprehension
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(f"Bonus 2. Matrix: {matrix}")

# Bonus 3: Filter with condition
evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Bonus 3. Evens: {evens}")

# ============================================
# 9. PRACTICE EXERCISES (Write Code Yourself!)
# ============================================

print("\n=== Practice Exercises (No Solutions - You Code!) ===")
print("""
Exercise 1: Number classifier
  - Ask user for a number (simulate with variable)
  - Print if it's: positive/negative, even/odd, divisible by 5
  - Example: 15 -> "Positive, Odd, Divisible by 5"

Exercise 2: Print all prime numbers from 1 to 50
  - Use nested loops to check each number
  - A prime number is only divisible by 1 and itself
  - Print all primes in one line

Exercise 3: Pattern - Diamond shape
  - Print a diamond pattern with * (size = 5)
  - Example:
      *
     ***
    *****
     ***
      *

Exercise 4: Sum of digits
  - Given number = 12345
  - Calculate sum of all digits (1+2+3+4+5 = 15)
  - Use a while loop to extract digits

Exercise 5: Reverse a number
  - Given number = 12345
  - Reverse it to get 54321
  - Use loop to extract and build reversed number

Exercise 6: Find all Armstrong numbers between 1-1000
  - Armstrong number: sum of cubes of digits equals the number
  - Example: 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
  - Print all Armstrong numbers found

Exercise 7: Guess the number game
  - Secret number = 42
  - User has 5 attempts (simulate with loop)
  - For each guess, print "Too high", "Too low", or "Correct!"
  - Use break when correct
""")

# ============================================
# 10. COMMON MISTAKES
# ============================================

print("\n=== Common Mistakes ===")

# Mistake 1: Wrong indentation
print("1. Indentation matters!")
for i in range(3):
    print(f"  Inside loop: {i}")
print("  Outside loop")

# Mistake 2: Infinite loop
# while True:  # Never ends!
#     print("Forever")
print("2. Always ensure loop can exit")

# Mistake 3: Modifying list while iterating
numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     numbers.remove(num)  # BAD!
# Use list copy instead
numbers_copy = numbers.copy()
print(f"3. Use copy when modifying: {numbers_copy}")

# Mistake 4: Off-by-one errors
print("4. range(5) gives 0-4, not 1-5")

# ============================================
# 11. QUICK REFERENCE
# ============================================

print("\n=== Quick Reference ===")
print("""
CONDITIONALS:
  if condition:
  elif condition:
  else:
  
  # Ternary
  x = a if condition else b

FOR LOOPS:
  for i in range(5):
  for item in list:
  for i, item in enumerate(list):

WHILE LOOPS:
  while condition:
  
CONTROL:
  break     # Exit loop
  continue  # Skip iteration
  pass      # Do nothing
""")