# String Formatting Examples in Python
# Each example shows the code first, then the actual output right below.

# --------------------------------------------------
# Right-align the number within a width of 10 spaces
print("{0: >10}".format(500))
# Output:
#        500

# --------------------------------------------------
# Show + sign for positive numbers and - for negative numbers
# Right-aligned within a width of 10
print("{0: >+10}".format(500))
# Output:
#       +500

print("{0: >+10}".format(-500))
# Output:
#       -500

# --------------------------------------------------
# Left-align the number and fill remaining space with underscores (_)
print("{0:_<10}".format(500))
# Output:
# 500_______

# --------------------------------------------------
# Add commas every three digits for large numbers
print("{0:,}".format(1000000000000000))
# Output:
# 1,000,000,000,000,000

# --------------------------------------------------
# Add commas and always display the sign (+ or -)
print("{0:+,}".format(1000000000000000))
# Output:
# +1,000,000,000,000,000

print("{0:+,}".format(-1000000000000000))
# Output:
# -1,000,000,000,000,000

# --------------------------------------------------
# Combine multiple formatting options:
# - show sign
# - use commas
# - left-align (^<)
# - fill empty space with ^
# - total width of 30 characters
print("{0:^<+30,}".format(-1000000000000000))
# Output:
# -1,000,000,000,000,000^^^^^^^^

# --------------------------------------------------
# Default floating-point output
print("{0:f}".format(5 / 3))
# Output:
# 1.666667

# --------------------------------------------------
# Limit decimal places to 2 (rounded at the 3rd decimal place)
print("{0:.2f}".format(5 / 3))
# Output:
# 1.67
