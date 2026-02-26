"""
📌 List and for Loop Basics: Dangerous Animals in Australia

This file demonstrates the basic usage of Python lists and
for loops using a simple example.

The goal is to understand how multiple values can be stored
in a list and how each element can be accessed sequentially
using a for loop.

✔ Python list fundamentals
✔ String lists
✔ Basic for loop structure
✔ Clean and readable output formatting
"""

# ==================================================
# 1️⃣ What is a list?
# ==================================================
# A list is a data structure that allows multiple values
# to be stored in a single variable in a specific order.
#
# Lists are defined using square brackets [] and
# each element is separated by a comma.

dangerous_animals = [
    "Saltwater Crocodile",
    "Box Jellyfish",
    "Great White Shark",
    "Eastern Brown Snake",
    "Sydney Funnel-web Spider"
]

# ==================================================
# 2️⃣ Print a header message
# ==================================================
# This line informs the user what kind of information
# will be displayed before printing the list items.

print("Dangerous animals in Australia:")

# ==================================================
# 3️⃣ for loop
# ==================================================
# A for loop is used to iterate over each element
# in the list from beginning to end.
#
# Syntax:
# for variable in list:
#     code to execute
#
# In this case, the variable 'animal' temporarily
# stores each element of the list during each iteration.

for animal in dangerous_animals:
    # Print each animal name with a dash for readability
    print("-", animal)

# ==================================================
# ✅ Summary
# ==================================================
# This example practices:
# 1. Grouping multiple values using a list
# 2. Iterating through list elements with a for loop
# 3. Producing clean, readable console output
#
# This concept is fundamental and will later be combined with:
# - conditional statements (if)
# - list modification (append, remove)
# - enumerate() and range()
