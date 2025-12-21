# Random Functions

from random import *

# print(random())             # Generates a random float between 0.0 and 1.0
# print(random() * 10)        # Generates a random float between 0.0 and 10.0
# print(int(random() * 10))   # Generates a random integer between 0 and 9
# print(int(random() * 10) + 1)  # Generates a random integer between 1 and 10

# Lottery example
# print(int(random() * 45) + 1)  # Random number between 1 and 45
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)

# print(randrange(1, 46))  # Generates a random number from 1 to 45
# print(randint(1, 45))    # Generates a random number from 1 to 45 (inclusive)


# Practice
from random import *

date = randint(4, 28)
print("The offline study meeting date has been set to the "
      + str(date) + "th of every month.")

The offline study meeting date has been set to the 17th of every month.
