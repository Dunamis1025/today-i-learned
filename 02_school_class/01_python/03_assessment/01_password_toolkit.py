# GM1 – Password Security Toolkit
# Cyber Security Python Portfolio
# Author: Yunho Shin

import hashlib
import random
import string


# ---------------------------------------------------------
# 1. Password Strength Checker
# ---------------------------------------------------------
def check_password_strength():
    """
    Checks whether the user's password meets basic security requirements.
    Requirements:
    - At least 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one number
    - At least one special character
    """

    requirements = """
Password must be at least 8 characters long and include:
- At least one uppercase letter
- At least one lowercase letter
- At least one number
- At least one special character
"""

    while True:
        password = input("Enter password: ")

        # Check password length
        if len(password) < 8:
            print("Weak password")
            print(requirements)
            continue

        # Check for lowercase letter
        has_lower = False
        for letter in password:
            if letter.islower():
                has_lower = True
                break

        # Check for uppercase letter
        has_upper = False
        for letter in password:
            if letter.isupper():
                has_upper = True
                break

        # Check for numbers
        has_number = False
        for letter in password:
            if letter.isdigit():
                has_number = True
                break

        # Check for special characters
        has_symbol = False
        for letter in password:
            if letter in string.punctuation:
                has_symbol = True
                break

        # Final decision
        if has_lower and has_upper and has_number and has_symbol:
            print("Strong password\n")
            break
        else:
            print("Password is not strong enough.")
            print(requirements)
            continue


# ---------------------------------------------------------
# 2. Secure Password Generator
# ---------------------------------------------------------
def generate_password(length):
    """
    Generates a random secure password using:
    - Uppercase letters
    - Lowercase letters
    - Numbers
    - Special characters
    """

    if length < 8:
        print("Password length should be at least 8 characters.")
        return

    # Characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    password = []  # list to store password characters

    # Select random characters based on the desired length
    for i in range(length):
        password.append(random.choice(characters))

    # Convert the list into a string
    final_password = "".join(password)

    print("Generated password:", final_password)


# ---------------------------------------------------------
# 3. Password Hashing (SHA-256)
# ---------------------------------------------------------
def hash_password(password):
    """
    Converts the input password into a SHA-256 hash.
    Hashing is one-way and cannot be reversed.
    """

    # Convert password into bytes
    encoded_password = password.encode()

    # Create SHA-256 hash object
    hash_object = hashlib.sha256(encoded_password)

    # Convert hash into readable hexadecimal string
    hashed = hash_object.hexdigest()

    print("SHA-256 Hash:", hashed)


# ---------------------------------------------------------
# 4. Main Program Loop
# ---------------------------------------------------------
while True:

    print("\nPassword Security Toolkit")
    print("1. Check password strength")
    print("2. Generate secure password")
    print("3. Hash a password")
    print("4. Exit")

    option = input("Choose an option (1-4): ")

    if option == "1":
        check_password_strength()

    elif option == "2":
        length_input = input("Enter desired password length: ")

        # Check if the input is a number
        if length_input.isdigit():
            length = int(length_input)
            generate_password(length)
        else:
            print("Please enter a valid number.")

    elif option == "3":
        password = input("Enter password: ")
        hash_password(password)

    elif option == "4":
        print("Exiting program")
        break

    else:
        print("Invalid option. Please choose 1, 2, 3, or 4.")