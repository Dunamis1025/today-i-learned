"""
📌 Naming Conventions Summary (for Python & General Programming)

This file is a study note that summarizes
commonly used naming conventions in programming.

It explains the differences between snake_case, camelCase,
PascalCase, and other styles mentioned during class,
with the goal of building a habit of writing clean and readable code.

※ Naming conventions are not strict syntax rules,
   but they are widely accepted conventions within each language
   and programming community.
"""

# ==================================================
# 1️⃣ What is a Naming Convention?
# ==================================================
# A naming convention refers to
# commonly agreed-upon ways of naming variables, functions, and classes.
#
# Code will still run even if you don’t follow them,
# but naming conventions are extremely important for:
# - readability
# - collaboration
# - long-term maintenance
#
# Instructor’s phrase:
# "It’s convention." → Not a strict rule, but a common agreement


# ==================================================
# 2️⃣ snake_case
# ==================================================
# Words are separated by underscores (_)
# Lowercase letters are used by default

# Common usage:
# - Python variables
# - Python functions
# - Frequently used in C / C++ style languages

# Examples
user_name = "Alex"
total_score = 100

def get_user_data():
    pass


# ==================================================
# 3️⃣ camelCase
# ==================================================
# The first word starts with a lowercase letter,
# and each following word starts with an uppercase letter.
# The capital letters in the middle resemble a camel’s hump,
# which is why it’s sometimes called "camel hump".

# Common usage:
# - Java
# - JavaScript
# - C#

# Example (not recommended in Python)
userName = "Alex"
totalScore = 100

def getUserData():
    pass


# ==================================================
# 4️⃣ PascalCase (a variation of CamelCase)
# ==================================================
# Every word starts with an uppercase letter,
# including the first word.

# Common usage:
# - Python class names
# - Java / C# class names

# Example
class UserProfile:
    pass


# ==================================================
# 5️⃣ ALL_CAPS (Constants)
# ==================================================
# All uppercase letters with underscores
# Used to clearly indicate values that should not change

# Examples
MAX_SIZE = 100
DEFAULT_TIMEOUT = 30


# ==================================================
# 6️⃣ Recommended Naming Rules in Python (PEP 8)
# ==================================================
# - Variables / functions: snake_case
# - Classes: PascalCase
# - Constants: ALL_CAPS
# - "caps" in spoken language usually means capital letters

# Combined Python example
class UserAccount:
    MAX_LOGIN_ATTEMPTS = 5

    def get_user_name(self):
        pass


# ==================================================
# 7️⃣ Key Takeaways
# ==================================================
# - Naming conventions are conventions, not syntax rules
# - Each language has preferred and widely accepted styles
# - Writing names that match the language style is the first step
#   toward writing good code
# - Useful explanation in exams or interviews:
#   "Because it's the naming convention in this language."
