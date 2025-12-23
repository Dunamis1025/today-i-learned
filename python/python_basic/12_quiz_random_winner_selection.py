
# Quiz Description:
# Create a giveaway program.
#
# From users numbered 1 to 20, randomly select 4 winners:
# - 1 winner receives a chicken prize
# - 3 winners receive coffee prizes
#
# Requirements:
# - Use Python's random module
# - No duplicate winners
# - Print the result in a clear format
#
# This file includes both the quiz description
# and the solution with expected outputs.
# ============================================


from random import *


# ----------------------------
# Step 1: Create users
# ----------------------------

users = range(1, 21)  # Generate numbers from 1 to 20
users = list(users)

print(users)
# Result -> [1, 2, 3, ..., 20]


# ----------------------------
# Step 2: Shuffle users
# ----------------------------

shuffle(users)
print(users)
# Result -> [17, 11, 6, 8, 9, 15, 4, 14, 3, 16, 20, 5, 18, 19, 10, 2, 1, 13, 12, 7]
# (Order will vary every time)


# ----------------------------
# Step 3: Select winners
# ----------------------------

winners = sample(users, 4)  # Pick 4 unique winners

# First winner -> Chicken
# Remaining 3 winners -> Coffee


# ----------------------------
# Step 4: Print result
# ----------------------------

print(" -- Winner Announcement -- ")
print("Chicken Winner : {0}".format(winners[0]))
print("Coffee Winners : {0}".format(winners[1:]))
print(" -- Congratulations! -- ")

# Example Result:
#  -- Winner Announcement --
#  Chicken Winner : 8
#  Coffee Winners : [10, 11, 15]
#  -- Congratulations! --
