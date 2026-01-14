"""
Python Module Basics (Australia Context)

This file demonstrates how Python modules work using
an Australian movie ticket pricing example.

Key concepts covered:
- What a module is
- Different import styles in Python
- Using aliases (as)
- Importing specific functions
- Common NameError scenario
"""

# ==================================================
# 1. What is a module?
# ==================================================
# A module is a Python file (.py) that contains reusable code,
# such as functions, variables, or classes.
#
# Modules help you:
# - Organize code logically
# - Avoid duplication
# - Maintain and scale projects more easily


# ==================================================
# 2. Example module: theater_module.py
# ==================================================
# Assume the following functions exist in theater_module.py:
#
# def price_regular(people):
#     print(f"{people} people regular price is ${people * 22}.")
#
# def price_morning(people):
#     print(f"{people} people morning session price is ${people * 16}.")
#
# def price_student(people):
#     print(f"{people} people student discount price is ${people * 14}.")


# ==================================================
# 3. Basic import (recommended)
# ==================================================
import theater_module

theater_module.price_regular(3)
theater_module.price_morning(4)
theater_module.price_student(2)


# ==================================================
# 4. Import with alias
# ==================================================
import theater_module as cinema

cinema.price_regular(2)
cinema.price_morning(3)
cinema.price_student(1)


# ==================================================
# 5. Import everything from a module (not recommended)
# ==================================================
from theater_module import *

price_regular(1)
price_morning(2)
price_student(3)


# ==================================================
# 6. Import specific functions (best practice)
# ==================================================
from theater_module import price_regular, price_morning

price_regular(4)
price_morning(2)


# ==================================================
# 7. NameError example
# ==================================================
# price_student was NOT imported above,
# so calling it will raise a NameError
#
# price_student(2)


# ==================================================
# 8. Import with alias for a function
# ==================================================
from theater_module import price_student as student_price

student_price(3)


# ==================================================
# Summary
# ==================================================
# - A module is a reusable Python file
# - import module_name → module_name.function()
# - import module_name as alias → alias.function()
# - from module import function → function()
# - Import only what you need for clarity
# - NameError occurs when a function was not imported

"""
==================
Program Output
==================

3 people regular price is $66.
4 people morning session price is $64.
2 people student discount price is $28.

2 people regular price is $44.
3 people morning session price is $48.
1 people student discount price is $14.

1 people regular price is $22.
2 people morning session price is $32.
3 people student discount price is $42.

4 people regular price is $88.
2 people morning session price is $32.

3 people student discount price is $42.
"""

