import re

# ==================================================
# Regular Expression (Regex) - Concept Notes
# ==================================================
#
# What is a Regular Expression?
# → A tool used to check whether a string follows a specific rule or format.
#
# Example 1) US Social Security Number (SSN)
# - Valid format: 123-45-6789
# - If the format is different, it is NOT a valid SSN.
#
# Example 2) Email address
# - Valid format: yunho1025@gmail.com
# - Invalid format: yunho1025@gmail@gmail.com
#
# In short, regex acts as a filter that answers:
# "Does this string follow the rule we defined?"
#
# --------------------------------------------------
# Instructor's analogy (Hit-and-run license plate case)
# --------------------------------------------------
#
# - Assume a license plate consists of 4 alphabet letters.
# - You remember only 3 letters; one letter is missing.
#
# Method 1:
# - Try all possibilities by inserting letters from a to z.
#
# Method 2:
# - Define a rule that says:
#   "This position can be ANY letter."
#
# → That rule is exactly what a regular expression is.
#
# ==================================================


# --------------------------------------------------
# Creating a regex pattern
# --------------------------------------------------
#
# Pattern: "ca.e"
#
# Meaning:
# - Starts with 'c'
# - Second letter is 'a'
# - '.'  → any single character
# - Ends with 'e'
#
# This pattern matches words shaped like: ca?e
#
# Matches:
# care, cafe, case, cave
#
# Does NOT match:
# caffe (5 characters)
# cake  (does not end with 'e')
#
p = re.compile("ca.e")


# --------------------------------------------------
# Common regex symbols
# --------------------------------------------------
#
# .  : matches exactly one character
#      ca.e → care, cafe (O) | caffe (X)
#
# ^  : start of the string
#      ^de → desk, destination (O) | fade (X)
#
# $  : end of the string
#      se$ → case, base (O) | face (X)
#


# --------------------------------------------------
# Helper function to display match results clearly
# --------------------------------------------------
def print_match(m):
    if m:
        # group(): returns the actual matched substring
        print("Match found:", m.group())
    else:
        print("No match found")


# --------------------------------------------------
# Explanation of match()
# --------------------------------------------------
#
# match():
# - Checks ONLY from the beginning of the string
# - If the pattern matches at the start, it succeeds
# - It does NOT require the entire string to match
#


# --------------------------------------------------
# Test 1: "care"
# --------------------------------------------------
m = p.match("care")
# Perfectly matches the pattern ca.e
print_match(m)
# Expected result: Match found → care


# --------------------------------------------------
# Test 2: "cave"
# --------------------------------------------------
m = p.match("cave")
# Also matches the pattern ca.e
print_match(m)
# Expected result: Match found → cave


# --------------------------------------------------
# Test 3: "careless"
# --------------------------------------------------
m = p.match("careless")
#
# Why does this NOT cause an error?
# → match() only checks whether the pattern matches
#   at the START of the string.
#
# "careless" =
# "care" + "less"
#
# Since "care" at the beginning matches ca.e,
# the match is considered successful.
#
print_match(m)
# Expected result: Match found → care

# result
# Match found: care
# Match found: cave
# Match found: care
