"""
📌 Topic: Python Built-in Functions and Exploring Objects with dir()

In this lesson, I learned that Python provides many built-in functions by default,
and that we can explore what functions and attributes an object has using dir().

The goal of this file is not to memorize functions,
but to understand how to discover and explore them when needed.
"""

# ------------------------------------------------------------
# 1. input() – A built-in function for user input
# ------------------------------------------------------------

# input() receives user input as a string (str)
language = input("Which programming language do you like? ")

# format() is a string method used to insert values into a string
print("{0} is a great language!".format(language))


# ------------------------------------------------------------
# 2. dir() – Inspecting the current namespace
# ------------------------------------------------------------

# Importing external modules
import random
print(dir())  # Shows currently available names in the environment

import pickle
print(dir())  # Confirms that 'pickle' is now included


# ------------------------------------------------------------
# 3. Using dir() on an object (string example)
# ------------------------------------------------------------

name = "Jim"

# dir() shows all attributes and methods available for the string object
print(dir(name))


"""
Example output (trimmed for readability):

[
 '__add__', '__class__', '__contains__', '__eq__', '__len__',
 '__str__', '__repr__',
 'capitalize', 'count', 'find', 'format',
 'isalnum', 'isalpha', 'islower', 'isupper',
 'join', 'lower', 'replace', 'split', 'strip',
 'upper', 'zfill'
]

This output shows that a string is not just text,
but an object with many built-in methods.
"""


# ------------------------------------------------------------
# Key Takeaway
# ------------------------------------------------------------

"""
- Python comes with many built-in functions.
- Everything in Python is an object, including strings.
- dir() helps explore what an object can do.
- You don’t need to memorize methods — you need to know how to find them.
"""
