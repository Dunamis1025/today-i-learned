# Random Functions
from random import *

# print(random())            # Generate a random float between 0.0 and 1.0
# print(random() * 10)       # Generate a random float between 0.0 and 10.0
# print(int(random() * 10))  # Generate a random integer from 0 to 9
# print(int(random() * 10) + 1)  # Generate a random integer from 1 to 10

# Lottery example
# print(int(random() * 45) + 1)  # Generate a random number from 1 to 45
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)

# print(randrange(1, 46))    # Generate a random number from 1 to 45
# print(randint(1, 45))      # Generate a random number from 1 to 45 (inclusive)


# Practice
date = randint(4, 28)
print("The offline study meeting will be held on the " + str(date) + "th of each month.")
