import re

# ==================================================
# Regular Expression (Regex) Practice Notes
# - Differences between match(), search(), and findall()
# - Understanding the match object and its methods
# ==================================================


# --------------------------------------------------
# 1) Regex pattern explanation
# --------------------------------------------------
# Pattern: "ca.e"
#
# Meaning:
# - Starts with 'c'
# - Second character is 'a'
# - '.' matches exactly ONE character
# - Ends with 'e'
#
# This pattern matches words with the exact form: ca?e
# (Total length must be exactly 4 characters)
#
# Matching examples:
# care, cafe, case, cave, cake
#
# Non-matching examples:
# caffe  → too many characters
# cae    → too few characters
#
p = re.compile("ca.e")


# --------------------------------------------------
# 2) Common regex symbols (quick reference)
# --------------------------------------------------
# .  : matches exactly one character
#
# ^  : start of a string
#      ^de → desk, destination (O)
#      fade (X)
#
# $  : end of a string
#      se$ → case, base (O)
#      face (X)
#


# --------------------------------------------------
# 3) Helper function to inspect match results
# --------------------------------------------------
# This function prints detailed information about
# where and how the regex matched the string.
def print_match(m):
    if m:
        # The exact substring that matched the pattern
        print("m.group():", m.group())

        # The original input string
        print("m.string:", m.string)

        # Starting index of the match (0-based)
        print("m.start():", m.start())

        # Ending index of the match (index AFTER the last character)
        print("m.end():", m.end())

        # (start, end) as a tuple
        print("m.span():", m.span())
    else:
        print("No match found")


# ==================================================
# 4) match() vs search() vs findall()
# ==================================================
#
# match()
# - Checks for a match ONLY at the beginning of the string
# - Succeeds if the pattern matches from index 0
#
# search()
# - Scans the entire string
# - Succeeds if the pattern appears anywhere
#
# findall()
# - Finds ALL matching substrings
# - Returns a list of strings (not match objects)
#
# ==================================================


# --------------------------------------------------
# 5) Test examples (uncomment to run)
# --------------------------------------------------

# ▶ match() example
# "careless" = "care" + "less"
# Since the string starts with "care",
# match() succeeds.
#
# m = p.match("careless")
# print_match(m)
#
# Expected output:
# m.group(): care
# m.string: careless
# m.start(): 0
# m.end(): 4
# m.span(): (0, 4)


# ▶ search() example
# Finds the pattern anywhere in the string
#
# m = p.search("good care")
# print_match(m)
#
# Expected output:
# m.group(): care
# m.string: good care
# m.start(): 5
# m.end(): 9
# m.span(): (5, 9)


# ▶ findall() example
# Returns all matches as a list
#
# lst = p.findall("good care cafe cake")
# print(lst)
#
# Expected output:
# ['care', 'cafe', 'cake']


# ==================================================
# 6) Summary (for quick review)
# ==================================================
# 1. re.compile(pattern)      → prepare a regex pattern
# 2. match(string)            → match only from the start
# 3. search(string)           → search anywhere in the string
# 4. findall(string)          → return all matches as a list
#
# match() and search() return:
# - a match object if successful
# - None if no match is found
#
# Important match object methods:
# - group() : matched substring
# - string  : original input string
# - start() : start index
# - end()   : end index (exclusive)
# - span()  : (start, end)
# ==================================================
