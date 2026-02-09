# ============================================================
# Python Package & Module Execution Summary
#
# Topics covered:
# - Package structure (__init__.py)
# - __all__ usage
# - Different import styles
# - __name__ == "__main__" execution pattern
#
# This file summarizes what I learned about how Python
# distinguishes between:
# 1) running a module directly
# 2) importing a module from another file
# ============================================================


# ------------------------------------------------------------
# 1. What is a package and why __init__.py is needed
# ------------------------------------------------------------
# A folder becomes a Python package when it contains __init__.py.
# This allows Python to treat the folder as a logical module group.

# Inside travel/__init__.py, we define __all__:

# __all__ = ["vietnam", "thailand"]

# This controls what gets imported when using:
# from travel import *
#
# Only modules listed in __all__ are exposed.
# This works like a "public API" for the package.


# ------------------------------------------------------------
# 2. Different import styles and what they mean
# ------------------------------------------------------------

# (1) Import the full module path
# import travel.thailand
# trip = travel.thailand.ThailandPackage()
#
# - Very explicit
# - Long and less convenient
# - Good for understanding package structure


# (2) Import a specific class from a module
# from travel.thailand import ThailandPackage
# trip = ThailandPackage()
#
# - Most commonly used in real projects
# - Clean and readable


# (3) Import the module itself
# from travel import vietnam
# trip = vietnam.VietnamPackage()
#
# - Avoids name collisions
# - Makes module boundaries clear


# (4) Import everything defined in __all__
from travel import *

trip = thailand.ThailandPackage()
trip.detail()

# This works because:
# - thailand is listed in __all__
# - Python imports only those approved modules


# ------------------------------------------------------------
# 3. Understanding __name__ == "__main__"
# ------------------------------------------------------------
# Every Python file has a built-in variable called __name__.
# Python automatically sets its value depending on how the file is used.

# Case 1:
# If the file is executed directly:
#   python thailand.py
# then:
#   __name__ == "__main__"

# Case 2:
# If the file is imported from another module:
#   import travel.thailand
# then:
#   __name__ == "travel.thailand"


# ------------------------------------------------------------
# 4. Why this pattern is important
# ------------------------------------------------------------
# This allows one file to serve two purposes:
#
# 1) Act as a standalone test file
# 2) Act as a reusable module without side effects
#
# Test code is placed under:
# if __name__ == "__main__":
#
# Reusable logic stays outside this block


# ------------------------------------------------------------
# 5. Example: thailand.py
# ------------------------------------------------------------

class ThailandPackage:
    def detail(self):
        print("[Thailand Package 3 Nights 5 Days] Bangkok & Pattaya Tour (Night Market) USD $380")


if __name__ == "__main__":
    # This block runs ONLY when the file is executed directly
    print("Thailand module is being run directly")
    print("This message appears only in direct execution")

    trip = ThailandPackage()
    trip.detail()

else:
    # This block runs when the module is imported
    print("Thailand module is imported from another file")


# ------------------------------------------------------------
# 6. Key takeaway
# ------------------------------------------------------------
# __name__ == "__main__" is not just syntax.
# It is a design pattern used to:
#
# - Separate test code from reusable logic
# - Prevent unwanted execution during imports
# - Make modules safe and clean to reuse
#
# This concept becomes essential when building
# larger Python projects and packages.
# ============================================================
