# Operators & Math Functions

# print(2 ** 3)      # Exponentiation: 2^3 = 8
# print(5 % 3)       # Modulo (remainder): 2
# print(10 % 3)      # 1
# print(5 // 3)      # Floor division: 1
# print(10 // 3)     # 3

# print(1 != 3)                  # True
# print(not (1 != 3))            # False
# print((3 > 0) & (3 < 5))        # True
# print((3 > 0) | (3 > 5))        # True

print(2 + 3 * 4)
number = 2 + 3 * 4
print(number)

number *= 2
print(number)

number /= 2
print(number)

number %= 2
print(number)

print(abs(-5))          # Absolute value: 5
print(pow(4, 2))        # Power: 4^2 = 16
print(max(5, 12))       # Maximum value: 12
print(min(5, 12))       # Minimum value: 5
print(round(3.14))      # Round to nearest integer: 3
print(round(4.99))      # Round to nearest integer: 5

from math import *
print(floor(4.99))      # Floor (round down): 4
print(ceil(3.14))       # Ceil (round up): 4
print(sqrt(16))         # Square root: 4
