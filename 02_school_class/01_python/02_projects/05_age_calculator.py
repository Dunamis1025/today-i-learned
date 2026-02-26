"""
📌 Exercise 6: Age Calculator

This file is a learning exercise that combines:
1) My own implementation (considering whether the birthday has passed)
2) The school-provided model answer (basic age calculation)
3) Improvements for clarity, realism, and robustness

The goal is to practice thinking in programming logic,
not just copying solutions.
"""

# ==================================================
# 0️⃣ Set the current year
# ==================================================
# In the school model answer, the current year is fixed (e.g. 2024).
# For practice purposes, using a fixed year is acceptable.
# Wrapping an integer with int() is unnecessary.

current_year = 2026

# Note:
# A more realistic approach (for later learning) would be:
# from datetime import date
# current_year = date.today().year


# ==================================================
# 1️⃣ User Input
# ==================================================
# input() always returns a string.
# To perform numeric calculations, we must convert it to an integer.

birth_year_string = input("Enter your year of birth: ")  # e.g. 1998
birth_year = int(birth_year_string)

# Ask whether the user's birthday has already passed this year.
# This is required for a realistic age calculation.
birthday_passed = input("Has your birthday passed this year? (y/n): ")


# ==================================================
# 2️⃣ Process (Age Calculation Logic)
# ==================================================
# School model answer logic:
# age = current_year - birth_year
# → This assumes the birthday has already passed.
#
# Improved logic:
# - If birthday has passed: current_year - birth_year
# - If birthday has not passed: current_year - birth_year - 1

# Normalize user input to handle spaces and uppercase letters.
birthday_passed = birthday_passed.strip().lower()

if birthday_passed == "y":
    current_age = current_year - birth_year
else:
    # If the birthday has not passed yet
    current_age = current_year - birth_year - 1


# ==================================================
# 3️⃣ Output
# ==================================================
# f-strings allow clean and readable string formatting.

print(f"Your current age is {current_age} years old.")


# ==================================================
# ✅ Key Takeaways from This Exercise
# ==================================================
# 1. input() always returns a string.
# 2. Convert user input using int() or float() before calculations.
# 3. The school model answer demonstrates the minimum logic required.
# 4. Real-world problems often require additional conditions (if/else).
# 5. Cleaning user input with strip() and lower() makes code more robust.
# 6. Writing your own solution first leads to deeper understanding.
