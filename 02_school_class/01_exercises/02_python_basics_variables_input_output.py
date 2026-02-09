"""
📌 Python Basics Practice: Variables, Input, and Output

This file contains basic Python practice code written during class.
It focuses on understanding fundamental concepts such as:

- variables
- data types
- user input using input()
- output using print()
- basic arithmetic operations

The purpose of this file is not to solve a specific problem,
but to become familiar with Python syntax and core concepts.
"""

# ==================================================
# 1️⃣ Basic Python data types
# ==================================================
# int    : whole numbers (e.g. 1, 10, -5)
# float  : decimal numbers (e.g. 3.14, 98.6)
# bool   : boolean values (True / False)
# str    : strings (words, text)

# ==================================================
# 2️⃣ Basic operators
# ==================================================
# +  : addition
# -  : subtraction
# *  : multiplication
# /  : division (always returns a float)

# ==================================================
# 3️⃣ Getting user input
# ==================================================
# input() always returns a string (str).
# To perform numerical calculations,
# the input must be converted using int() or float().

firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")
yourAge = int(input("Please enter your age: "))

# ==================================================
# 4️⃣ Printing output
# ==================================================
# f-strings allow variables to be embedded directly
# inside a string in a clean and readable way.

print(f"Your first name is {firstName}")
print(f"Your last name is {lastName}")

# When combining strings and numbers,
# the number must be converted to a string.
print("Your age is " + str(yourAge))

# Using f-strings avoids the need for explicit conversion.
print(f"Your age is {yourAge}")

# ==================================================
# 5️⃣ Basic numeric operations
# ==================================================
# Adding two integers results in a numeric calculation.
print(yourAge + yourAge)

# ==================================================
# 6️⃣ Commented examples from class
# ==================================================
# The following examples were discussed during class
# and are kept here as reference.
# They are commented out so they do not execute.

# a = 5
# b = 10

# firstName = "mark"
# lastName = "Ovenden"

# print(a / b)
# print("The first name is ", firstName)
# print(firstName + lastName)
# print(f"The name is {firstName} {lastName}")

# print("Hello World", "5")
# print("Don't look into the sun")

# ==================================================
# 7️⃣ Multiline strings
# ==================================================
# Triple quotes (""" """) allow strings to span multiple lines.
# They are often used for documentation, messages, or ASCII art.

"""
multiple lines
exactly as it
appears
or do cool ascii art
"""

# ==================================================
# ✅ Summary
# ==================================================
# This file serves as a foundational practice file
# for understanding Python basics before moving on to:
# - lists
# - loops
# - conditionals
# - more complex programs
