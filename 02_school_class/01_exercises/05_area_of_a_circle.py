"""
📌 Exercise: Area of a Circle

This file is a learning note created by comparing:
- My self-written solution
- The model answer provided on the school website

The goal is not just to copy code,
but to understand programming as a language by designing
the flow: Input → Process → Output.
"""

# ==================================================
# 1️⃣ User Input (input() always returns a string)
# ==================================================
# No matter what the user types,
# input() always returns a string (str).
# To perform calculations, we must convert it to a number.

radius = float(input("Enter the radius (cm): "))

# 👉 In the model answer, this was written in two steps
#    to clearly show that input is a string:
#
# radius_string = input("Enter the radius of the circle: ")
# radius = float(radius_string)

# ==================================================
# 2️⃣ Constants and Variables
# ==================================================
# pi (π) is a constant value.
# In Python, variables are usually written in lowercase.
# Using uppercase for variables may look like a class name.

pi = 3.141592

# Formula for the area of a circle:
# Area = π × radius × radius
area = pi * radius * radius

# ==================================================
# 3️⃣ Output
# ==================================================
# Instead of showing only the final number,
# displaying the formula and substituted values
# makes the calculation process easier to understand.

print("Area = pi x radius x radius")
print(f"Area = pi x {radius} x {radius} = {area:.2f}")

# 👉 f-strings allow:
# - inserting variables directly into strings
# - formatting numbers (:.2f = 2 decimal places)

# ==================================================
# ✅ Key Takeaways from This Exercise
# ==================================================
# 1. input() always returns a string.
# 2. Convert input values using float() or int() before calculation.
# 3. Follow Python naming conventions (lowercase variable names).
# 4. Showing calculation steps improves readability and learning.
# 5. Writing your own code first and then comparing it with
#    the model answer leads to real understanding.
