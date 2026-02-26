"""
📌 Exercise 3: Simple Calculator (Comparison & Learning Notes)

This file documents a simple calculator program while comparing:
- My own implementation
- The model answer provided on the school website

The goal is not just to solve the problem,
but to clearly understand *why* different approaches work.

Key learning points:
1️⃣ input() always returns a string
2️⃣ Numeric calculations require type conversion (float or int)
3️⃣ Input and conversion can be combined in one line
4️⃣ f-strings improve readability and clarity of output
5️⃣ Understanding intent is more important than copying a model answer
"""

# ==================================================
# 1️⃣ My implementation
# ==================================================
# ✔ Uses float(input()) directly for concise code
# ✔ Displays the full calculation process for better readability
# ✔ Uses f-strings, which are the recommended modern Python approach

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

print(f"Addition(+): {first_number} + {second_number} = {first_number + second_number}")
print(f"Subtraction(-): {first_number} - {second_number} = {first_number - second_number}")
print(f"Multiplication(*): {first_number} * {second_number} = {first_number * second_number}")
print(f"Division(/): {first_number} / {second_number} = {first_number / second_number}")


# ==================================================
# 2️⃣ School website model answer (for comparison)
# ==================================================
# The following is the model answer provided by the school.
# It is commented out to avoid execution.

"""
num1_string = input("Enter the first number: ")  # e.g., "5.0"
num1 = float(num1_string)                       # convert string to float

num2_string = input("Enter the second number: ") # e.g., "3.0"
num2 = float(num2_string)                        # convert string to float

print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")
"""

# ✔ Purpose of the model answer:
# - To clearly demonstrate that input() returns a string
# - To show the type conversion process step by step
# - Suitable for explaining data types to beginners

# ✔ Strengths:
# - Easy to understand the input → conversion flow
# - Educational and beginner-friendly

# ❌ Limitations:
# - Uses extra intermediate variables
# - Output shows results only, not the calculation process


# ==================================================
# 3️⃣ Key takeaways
# ==================================================
# ✔ input() always returns a string
# ✔ Numeric operations require explicit type conversion
# ✔ float(input()) is functionally identical to multi-step conversion
# ✔ f-strings produce clearer and more user-friendly output
# ✔ A model answer explains concepts, but real learning comes from comparison
