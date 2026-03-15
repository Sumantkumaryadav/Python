# Day 2: Strings & Input/Output - Complete Guide
# ================================================

# ============================================
# 1. COMPLETE EXPLANATION
# ============================================

"""
WHAT ARE STRINGS?
- Strings are sequences of characters enclosed in quotes
- Can use single ('') or double ("") quotes
- Immutable: cannot be changed after creation

WHY ARE THEY IMPORTANT?
- Text processing and manipulation
- User input/output
- Data formatting and display
- File operations

KEY CONCEPTS:
- Indexing: Access individual characters (0-based)
- Slicing: Extract substrings [start:end:step]
- Methods: Built-in functions for string manipulation
- Formatting: Display data in readable format
"""

# ============================================
# 2. EXAMPLES (3 Required)
# ============================================

# --- EXAMPLE 1: Basic String Operations (Simple) ---
print("=== EXAMPLE 1: Basic String Operations ===")
# Creating and manipulating strings
greeting = "Hello, World!"
print(f"String: '{greeting}'")
print(f"Length: {len(greeting)}")
print(f"Uppercase: {greeting.upper()}")
print(f"Lowercase: {greeting.lower()}")
print(f"Title Case: {greeting.title()}")
print(f"Replace: {greeting.replace('World', 'Python')}")

# --- EXAMPLE 2: Email Validator (Intermediate) ---
print("\n=== EXAMPLE 2: Email Validator ===")
email = "user@example.com"

# Validation checks
has_at = '@' in email
has_dot = '.' in email
at_position = email.find('@')
dot_position = email.rfind('.')
valid_structure = has_at and has_dot and at_position < dot_position

# Extract parts
username = email[:at_position]
domain = email[at_position+1:]

print(f"Email: {email}")
print(f"Valid structure: {valid_structure}")
print(f"Username: {username}")
print(f"Domain: {domain}")
print(f"Starts with 'user': {email.startswith('user')}")
print(f"Ends with '.com': {email.endswith('.com')}")

# --- EXAMPLE 3: Text Analyzer (Advanced) ---
print("\n=== EXAMPLE 3: Text Analyzer ===")
text = "Python is powerful. Python is easy. Python is fun!"

# Analysis
word_count = len(text.split())
char_count = len(text)
char_no_spaces = len(text.replace(' ', ''))
sentence_count = text.count('.')
python_count = text.lower().count('python')

# Vowel counting
vowels = 'aeiouAEIOU'
vowel_count = sum(1 for char in text if char in vowels)

print(f"Text: {text}")
print(f"Words: {word_count}")
print(f"Characters: {char_count} (with spaces), {char_no_spaces} (without)")
print(f"Sentences: {sentence_count}")
print(f"'Python' appears: {python_count} times")
print(f"Vowels: {vowel_count}")

# ============================================
# 3. STRING INDEXING & SLICING
# ============================================

print("\n=== String Indexing & Slicing ===")
# Visual representation:
# Index:  0   1   2   3   4   5
# String: P   y   t   h   o   n
# Index: -6  -5  -4  -3  -2  -1

word = "Python"
print(f"Word: '{word}'")
print(f"First character [0]: '{word[0]}'")
print(f"Last character [-1]: '{word[-1]}'")
print(f"Second character [1]: '{word[1]}'")
print(f"Second from end [-2]: '{word[-2]}'")

print(f"\nSlicing [start:end:step]:")
print(f"First 3 [:3]: '{word[:3]}'")
print(f"Last 3 [-3:]: '{word[-3:]}'")
print(f"Middle [1:5]: '{word[1:5]}'")
print(f"Every 2nd [::2]: '{word[::2]}'")
print(f"Reverse [::-1]: '{word[::-1]}'")
print(f"Skip first & last [1:-1]: '{word[1:-1]}'")

# ============================================
# 4. STRING METHODS
# ============================================

print("\n=== String Methods ===")

# Case methods
text = "hello WORLD"
print(f"Original: '{text}'")
print(f"upper(): '{text.upper()}'")
print(f"lower(): '{text.lower()}'")
print(f"capitalize(): '{text.capitalize()}'")
print(f"title(): '{text.title()}'")
print(f"swapcase(): '{text.swapcase()}'")

# Whitespace methods
spaced = "  hello world  "
print(f"\nOriginal: '{spaced}'")
print(f"strip(): '{spaced.strip()}'")
print(f"lstrip(): '{spaced.lstrip()}'")
print(f"rstrip(): '{spaced.rstrip()}'")

# Search methods
sentence = "Python is awesome"
print(f"\nSentence: '{sentence}'")
print(f"find('is'): {sentence.find('is')}")
print(f"rfind('is'): {sentence.rfind('is')}")
print(f"index('awesome'): {sentence.index('awesome')}")
print(f"count('o'): {sentence.count('o')}")

# Check methods
print(f"\nCheck methods:")
print(f"'123'.isdigit(): {'123'.isdigit()}")
print(f"'abc'.isalpha(): {'abc'.isalpha()}")
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")
print(f"'HELLO'.isupper(): {'HELLO'.isupper()}")
print(f"'hello'.islower(): {'hello'.islower()}")
print(f"'   '.isspace(): {'   '.isspace()}")

# Split and join
csv = "apple,banana,orange"
fruits = csv.split(',')
print(f"\nSplit: {fruits}")
joined = ' | '.join(fruits)
print(f"Join: {joined}")

# ============================================
# 5. STRING FORMATTING
# ============================================

print("\n=== String Formatting ===")
name = "Alice"
age = 25
score = 95.567

# Method 1: f-strings (Python 3.6+, recommended)
print(f"1. f-string: {name} is {age} years old")
print(f"   Score: {score:.2f}")  # 2 decimal places
print(f"   Score: {score:.0f}")  # No decimals
print(f"   Padded: {age:05d}")   # Pad with zeros

# Method 2: format()
print("2. format(): {} is {} years old".format(name, age))
print("   Named: {n} scored {s:.1f}".format(n=name, s=score))

# Method 3: % formatting (old style)
print("3. %% format: %s is %d years old" % (name, age))

# Alignment
print(f"\n{'Left':<10}|")
print(f"{'Center':^10}|")
print(f"{'Right':>10}|")

# ============================================
# 6. INPUT/OUTPUT
# ============================================

print("\n=== Input/Output ===")
# Note: input() always returns a string
print("Input examples (commented for automation):")
print("# name = input('Enter name: ')")
print("# age = int(input('Enter age: '))")
print("# height = float(input('Enter height: '))")

# Simulated input
user_input = "42"
number = int(user_input)
print(f"String '{user_input}' converted to int: {number}")

# ============================================
# 7. EXERCISES
# ============================================

print("\n=== EXERCISES ===")

# --- EASY EXERCISES ---
print("\n--- Easy Exercises ---")

# Exercise 1: String length and case
word = "Programming"
print(f"1. '{word}' - Length: {len(word)}, Upper: {word.upper()}, Lower: {word.lower()}")

# Exercise 2: Extract first and last name
full_name = "John Doe"
parts = full_name.split()
first = parts[0]
last = parts[1]
print(f"2. Full: '{full_name}', First: '{first}', Last: '{last}'")

# Exercise 3: Check substring
sentence = "I love Python programming"
contains_python = "Python" in sentence
print(f"3. '{sentence}' contains 'Python': {contains_python}")

# Exercise 4: Reverse a string
original = "Hello"
reversed_str = original[::-1]
print(f"4. Original: '{original}', Reversed: '{reversed_str}'")

# Exercise 5: Count specific character
text = "Mississippi"
char = 's'
count = text.lower().count(char)
print(f"5. '{char}' appears {count} times in '{text}'")

# --- MEDIUM EXERCISES ---
print("\n--- Medium Exercises ---")

# Exercise 6: Palindrome checker
word = "radar"
is_palindrome = word == word[::-1]
print(f"6. '{word}' is palindrome: {is_palindrome}")

# Exercise 7: Count vowels and consonants
text = "Hello World"
vowels = "aeiouAEIOU"
vowel_count = sum(1 for c in text if c in vowels)
consonant_count = sum(1 for c in text if c.isalpha() and c not in vowels)
print(f"7. '{text}' - Vowels: {vowel_count}, Consonants: {consonant_count}")

# Exercise 8: Title case converter
sentence = "the quick brown fox"
title_case = sentence.title()
print(f"8. Original: '{sentence}', Title: '{title_case}'")

# Exercise 9: Remove spaces
text = "H e l l o"
no_spaces = text.replace(' ', '')
print(f"9. '{text}' -> '{no_spaces}'")

# Exercise 10: Extract domain from email
email = "user@example.com"
domain = email.split('@')[1]
print(f"10. Email: '{email}', Domain: '{domain}'")

# --- HARD EXERCISES ---
print("\n--- Hard Exercises ---")

# Exercise 11: Word frequency counter
text = "hello world hello python world"
words = text.split()
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1
print(f"11. Word frequency: {word_freq}")

# Exercise 12: Caesar cipher (shift by 3)
text = "abc"
shifted = ''.join(chr(ord(c) + 3) if c.isalpha() else c for c in text)
print(f"12. Original: '{text}', Shifted: '{shifted}'")

# Exercise 13: Validate password strength
password = "Pass123!"
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(not c.isalnum() for c in password)
is_long = len(password) >= 8
is_strong = all([has_upper, has_lower, has_digit, has_special, is_long])
print(f"13. Password: '{password}', Strong: {is_strong}")
print(f"    Upper: {has_upper}, Lower: {has_lower}, Digit: {has_digit}, Special: {has_special}, Length: {is_long}")

# ============================================
# 8. BONUS CHALLENGES
# ============================================

print("\n=== Bonus Challenges ===")

# Bonus 1: Remove duplicates preserving order
text = "programming"
seen = set()
unique = ''.join(c for c in text if not (c in seen or seen.add(c)))
print(f"Bonus 1. '{text}' -> '{unique}'")

# Bonus 2: Acronym generator
phrase = "Portable Network Graphics"
acronym = ''.join(word[0].upper() for word in phrase.split())
print(f"Bonus 2. '{phrase}' -> '{acronym}'")

# Bonus 3: String compression
text = "aaabbbccc"
compressed = ''.join(f"{c}{text.count(c)}" for c in dict.fromkeys(text))
print(f"Bonus 3. '{text}' -> '{compressed}'")

# ============================================
# 9. PRACTICE EXERCISES (Write Code Yourself!)
# ============================================

print("\n=== Practice Exercises (No Solutions - You Code!) ===")
print("""
Exercise 1: Username validator
  - Check if username is 5-15 characters long
  - Check if it contains only letters and numbers
  - Print validation result

Exercise 2: Extract file extension
  - Given filename = "document.pdf"
  - Extract and print the extension (.pdf)
  - Check if it's a valid document type (.pdf, .doc, .txt)

Exercise 3: Sentence statistics
  - Given: "Python programming is fun and powerful"
  - Count: total words, words starting with 'p', average word length
  - Print all statistics

Exercise 4: Phone number formatter
  - Given: "1234567890"
  - Format as: "(123) 456-7890"
  - Print formatted number

Exercise 5: Password generator
  - Take a word like "hello"
  - Replace: a->@, e->3, i->1, o->0
  - Add "!" at the end
  - Print generated password

Exercise 6: Title case converter (manual)
  - Given: "the lord of the rings"
  - Capitalize first letter of each word (don't use .title())
  - Print result

Exercise 7: String rotation checker
  - Check if "python" is a rotation of "thonpy"
  - Hint: If s2 is rotation of s1, then s2 will be substring of s1+s1
  - Print True or False
""")

# ============================================
# 10. COMMON MISTAKES
# ============================================

print("\n=== Common Mistakes ===")

# Mistake 1: Strings are immutable
text = "hello"
# text[0] = 'H'  # ERROR! Can't modify
new_text = 'H' + text[1:]
print(f"1. Can't modify strings directly. Use: '{new_text}'")

# Mistake 2: Index out of range
word = "hi"
# print(word[5])  # ERROR!
print(f"2. '{word}' has length {len(word)}, max index is {len(word)-1}")

# Mistake 3: Forgetting string methods return new strings
original = "hello"
original.upper()  # This doesn't change original
result = original.upper()  # Need to assign
print(f"3. Original: '{original}', Result: '{result}'")

# ============================================
# 11. QUICK REFERENCE
# ============================================

print("\n=== Quick Reference ===")
print("""
INDEXING:
  s[0]    # First char
  s[-1]   # Last char

SLICING:
  s[1:4]  # Index 1 to 3
  s[:3]   # First 3
  s[3:]   # From index 3
  s[::-1] # Reverse

METHODS:
  upper(), lower(), title()
  strip(), split(), join()
  replace(), find(), count()
  startswith(), endswith()
  isdigit(), isalpha()

FORMATTING:
  f"{var}"
  f"{num:.2f}"
""")