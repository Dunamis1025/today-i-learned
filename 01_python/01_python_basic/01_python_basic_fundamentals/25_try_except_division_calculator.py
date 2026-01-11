# ==================================================
# Try / Except Practice: Division-Only Calculator
#
# When is try useful?
# - When running code that may fail due to user input or runtime conditions.
# - It prevents the program from crashing and allows graceful error handling.
#
# When is except used?
# - When an exception occurs inside the try block.
# - It catches the error and runs alternative logic instead.
# ==================================================

try:
    print("This is a division-only calculator.")

    # List to store input numbers
    nums = []

    # int(input()) can raise ValueError if the input is not a number
    nums.append(int(input("Enter the first number: ")))
    nums.append(int(input("Enter the second number: ")))

    # IMPORTANT:
    # Without this line, nums only contains two elements.
    # Accessing nums[2] later would cause an IndexError.
    nums.append(nums[0] / nums[1])

    # Print the division result
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

# Raised when int() conversion fails (non-numeric input)
except ValueError:
    print("Error: Invalid input. Please enter numeric values only.")

# Raised when attempting to divide by zero
except ZeroDivisionError as err:
    # ZeroDivisionError is a built-in Python exception.
    # "as err" stores the error message so it can be displayed.
    print(err)

# Fallback handler for any unexpected exceptions
except Exception as err:
    # Exception is the base class for most Python errors.
    print("An unknown error has occurred.")
    print(err)


Program Output (Result)
✅ Case 1: Normal input
This is a division-only calculator.
Enter the first number: 6
Enter the second number: 3
6 / 3 = 2.0

❌ Case 2: Invalid (non-numeric) input
This is a division-only calculator.
Enter the first number: 6
Enter the second number: three
Error: Invalid input. Please enter numeric values only.

❌ Case 3: Division by zero
This is a division-only calculator.
Enter the first number: 6
Enter the second number: 0
division by zero

❌ Case 4: Missing result calculation (IndexError example)
This is a division-only calculator.
Enter the first number: 6
Enter the second number: 3
An unknown error has occurred.
list index out of range
