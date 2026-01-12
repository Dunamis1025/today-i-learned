try:
    print("Single-digit division calculator.")

    # The input() function always returns user input as a string (str).
    # For example, even if the user types 6, the value received is "6".
    # Since mathematical operations like division cannot be performed on strings,
    # we must convert the input into an integer using int().
    num1 = int(input("Enter the first number: "))

    # The same conversion is required for the second number.
    # This converts the string input into an integer
    # so it can be used in arithmetic operations.
    num2 = int(input("Enter the second number: "))

    # Allow only single-digit numbers (0–9).
    # If either number is 10 or greater, raise a ValueError manually.
    if num1 >= 10 or num2 >= 10:
        raise ValueError

    # Display the division result as an integer
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))

except ValueError:
    # This block runs if the input is not a number
    # or if the single-digit rule is violated.
    print("Invalid input. Please enter single-digit numbers only.")
