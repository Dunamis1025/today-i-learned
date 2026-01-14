# ==========================================
# Custom Exception Definition
# ==========================================
# This exception represents a real-world business case:
# when all chicken stock has been sold out.
class SoldOutError(Exception):
    pass


# ==========================================
# Initial State
# ==========================================
chicken = 10     # Number of chickens available
waiting = 1      # Waiting number (starts from 1)


# ==========================================
# Order Processing Loop
# ==========================================
# The program keeps running until all chickens are sold out.
# try / except is used to prevent the program from crashing.
while True:
    try:
        print("[Remaining Chicken] : {0}".format(chicken))

        # User input
        # If the input is not a number, ValueError will occur
        order = int(input("How many chickens would you like to order? "))

        # 1️⃣ Order exceeds available stock
        if order > chicken:
            print("Sorry, we do not have enough chicken in stock.")

        # 2️⃣ Zero or negative numbers are invalid
        # These values are numbers, but violate business rules,
        # so we intentionally raise a ValueError.
        elif order <= 0:
            raise ValueError

        # 3️⃣ Valid order
        else:
            print("[Waiting No. {0}] Your order of {1} chicken(s) is complete."
                  .format(waiting, order))
            waiting += 1
            chicken -= order

        # If all chickens are sold out,
        # raise a custom exception to end the program
        if chicken == 0:
            raise SoldOutError

    # ==========================================
    # Exception Handling
    # ==========================================

    # Handles invalid numeric input or non-numeric input
    except ValueError:
        print("Invalid input. Please enter a valid number.")

    # Handles the custom sold-out situation
    except SoldOutError:
        print("The stock is sold out. We are no longer accepting orders.")
        break

[Remaining Chicken] : 10
How many chickens would you like to order? 3
[Waiting No. 1] Your order of 3 chicken(s) is complete.
[Remaining Chicken] : 7
How many chickens would you like to order? 0
Invalid input. Please enter a valid number.
[Remaining Chicken] : 7
How many chickens would you like to order? -5
Invalid input. Please enter a valid number.
[Remaining Chicken] : 7
How many chickens would you like to order? five
Invalid input. Please enter a valid number.
[Remaining Chicken] : 7
How many chickens would you like to order? 7
[Waiting No. 2] Your order of 7 chicken(s) is complete.
The stock is sold out. We are no longer accepting orders.
