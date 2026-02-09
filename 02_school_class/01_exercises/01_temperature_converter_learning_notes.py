"""
📌 Exercise 1: Temperature Converter (Fahrenheit → Celsius)

This file contains a basic temperature conversion program written
during Python fundamentals study.

Rather than focusing only on producing the correct answer,
this file documents the learning process and the reasoning behind
each change made along the way.

✔ input() and type conversion (int → float)
✔ Arithmetic operations
✔ Decimal formatting (.2f vs round)
✔ Variable naming improvement (Fahrenheit → Celsius)
✔ Comparison with the school-provided model answer
"""

# ==================================================
# 1️⃣ Getting user input
# ==================================================
# Initially, int() was used to convert the input.
# However, Fahrenheit temperatures can include decimals (e.g. 98.6),
# so float() is more appropriate and was adopted.

Fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

# ==================================================
# 2️⃣ Fahrenheit → Celsius conversion formula
# ==================================================
# Formula:
# Celsius = (Fahrenheit - 32) * 5 / 9
#
# At first, int(32) was used, but since 32 is already
# an integer literal, wrapping it with int() is unnecessary.

Celsius = (Fahrenheit - 32) * 5 / 9

# ==================================================
# 3️⃣ Output (decimal formatting)
# ==================================================
# The calculation result can contain many decimal places.
# The f-string format :.2f is used to display the result
# rounded to two decimal places.
#
# Meaning of :.2f:
#  - Display up to two decimal places
#  - Controls output formatting only
#  - Does NOT change the actual value stored in the variable

print(f"{Celsius:.2f} Celsius")

# ==================================================
# 4️⃣ Difference between .2f and round()
# ==================================================
# round(Celsius, 2):
#  - Rounds the value itself and stores the rounded number
#
# Example:
# Celsius = round(Celsius, 2)
# print(Celsius)
#
# In this case, only clean output formatting is required,
# so the :.2f formatting approach is preferred.

# ==================================================
# 5️⃣ Variable naming improvement
# ==================================================
# Initially, only the variable name Fahrenheit was used.
# Since the calculated result represents Celsius,
# a separate variable named Celsius was introduced.
#
# Benefits:
#  - Improved readability
#  - Clearer meaning of calculations
#  - Closer to real-world and professional coding style

# ==================================================
# 6️⃣ Comparison with the school-provided Model Answer
# ==================================================
"""
[School Model Answer]

fahrenheit_string = input("Enter temperature in Fahrenheit: ")
fahrenheit = float(fahrenheit_string)
celsius = (fahrenheit - 32) * 5 / 9
print(f"The temperature in Celsius is: {celsius:.2f}")

[Comparison with my implementation]

✔ Similarities
- Uses input()
- Converts input to float
- Uses the same conversion formula
- Uses :.2f formatting

✔ Differences
- The model answer separates string input and float conversion
- My code combines input() and float() in one line for simplicity

👉 Both approaches are correct.
👉 My version focuses on understanding and clean structure
   rather than strictly following the model answer format.
"""

# ==================================================
# ✅ Conclusion
# ==================================================
# This code is not just a solution to a problem,
# but a learning record that explains why each decision was made.
#
# It is suitable for GitHub as a study log and makes
# future review and reflection much easier.
