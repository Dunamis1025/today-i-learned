"""
📌 Generate Student Message

This program prompts the user for a student's full name and student ID,
then generates a welcome message using string formatting.

Concepts covered in this file:
1️⃣ Using input() to receive user input
2️⃣ Storing input values in variables
3️⃣ Formatting strings using format()
4️⃣ Understanding the difference between f-strings and format()

⚠️ Important lesson learned:
When using format(), the string must NOT be prefixed with 'f'.
f-strings and format() are two different formatting mechanisms and
should never be mixed together.
"""

# ==================================================
# 1️⃣ Get user input
# ==================================================
# The input() function always returns a string (str),
# even if the user enters numbers.

student_name = input("Enter your Full name: ")
student_id = input("Enter your Student ID: ")


# ==================================================
# 2️⃣ Output using format()
# ==================================================
# {0} and {1} refer to the index positions of the values
# passed into the format() method.
#
# {0} → first argument  (student_name)
# {1} → second argument (student_id)
#
# ⚠️ Do NOT use 'f' before the string when using format().

print("Welcome, {0} (ID: [{1}])".format(student_name, student_id))


# ==================================================
# 3️⃣ Reference: f-string version (not used here)
# ==================================================
# The following is an alternative solution using f-strings.
# In f-strings, variables are placed directly inside {}.
#
# print(f"Welcome, {student_name} (ID: [{student_id}])")
#
# ✔ Never mix f-strings and format() in the same statement.
