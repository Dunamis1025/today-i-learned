# ==================================================
# Custom Exception: BigNumberError
# ==================================================
# This class defines a custom exception.
# It inherits from the built-in Exception class so that
# it can be properly raised and caught in try-except blocks.
# ==================================================

class BigNumberError(Exception):

    def __init__(self, msg):
        """
        Constructor (__init__):
        - Automatically called when a BigNumberError object is created.
        - Stores a custom error message inside the exception object.
        """
        self.msg = msg

    def __str__(self):
        """
        __str__ method:
        - Defines what message is shown when the exception object
          is printed using print().
        """
        return self.msg


# ==================================================
# Single-Digit Division Calculator
# ==================================================

try:
    print("This calculator only supports single-digit division.")

    # Convert user input into integers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # If either number has more than one digit,
    # raise a custom exception
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("Input values: {0}, {1}".format(num1, num2))

    # Perform division if inputs are valid
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))


# ==================================================
# Exception Handling
# ==================================================

except ValueError:
    # Triggered when input cannot be converted to an integer
    print("Invalid input. Please enter single-digit numbers only.")

except BigNumberError as err:
    # Triggered when numbers are 10 or greater
    print("An error occurred. Only single-digit numbers are allowed.")
    print(err)


# ==================================================
# Final block (always executed)
# ==================================================

finally:
    print("Thank you for using the calculator.")


✅ Execution Results
🔹 Case 1: Two-digit number input
This calculator only supports single-digit division.
Enter the first number: 10
Enter the second number: 5
An error occurred. Only single-digit numbers are allowed.
Input values: 10, 5
Thank you for using the calculator.

🔹 Case 2: Division by zero attempt
This calculator only supports single-digit division.
Enter the first number: 5
Enter the second number: 0
Thank you for using the calculator.


Note:
ZeroDivisionError is not handled yet, so the program terminates when division by zero occurs.
However, the finally block is always executed regardless of whether an exception is raised.
