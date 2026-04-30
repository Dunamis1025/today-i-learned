# random: used for picking random values (needed when generating a password)
import random

# string: contains groups of characters such as letters, digits, and punctuation
import string

# hashlib: used for hashing passwords
import hashlib

print("=== Password Security Toolkit ===")

while True:
    print("\n1. Check password strength")
    print("2. Generate secure password")
    print("3. Hash a password")
    print("4. Exit")

    option = input("Choose an option: ")

    # ---------------------------------------------------------
    # 1. Check password strength
    # ---------------------------------------------------------
    if option == "1":
        password = input("Enter password: ")

        # If the password is shorter than 8 characters, it is weak
        if len(password) < 8:
            print("Password strength: Weak (less than 8 characters)")
        else:
            # These variables will help check what kinds of characters the password contains
            has_lowercase = False   # contains lowercase letters
            has_uppercase = False   # contains uppercase letters
            has_digit = False       # contains numbers
            has_symbol = False      # contains special characters

            # Check each character in the password one by one
            for character in password:

                # Check for lowercase letters
                if character.islower():
                    has_lowercase = True

                # Check for uppercase letters
                elif character.isupper():
                    has_uppercase = True

                # Check for digits
                elif character.isdigit():
                    has_digit = True

                # Check for special characters
                elif character in string.punctuation:
                    has_symbol = True

            # If all four conditions are met, the password is strong
            if has_lowercase and has_uppercase and has_digit and has_symbol:
                print("Password strength: Strong (all recommended conditions are met)")
            else:
                # Not weak, but missing some recommended character types
                print("Password strength: Medium")
                print("The length is okay, but it does not include all of the following:")
                print("uppercase letters, lowercase letters, digits, and special characters.")

    # ---------------------------------------------------------
    # 2. Generate a secure password
    # ---------------------------------------------------------
    elif option == "2":
        length_text = input("Enter desired password length: ")

        # If the input is not a number
        if length_text.isdigit() == False:
            print("Password length must be a number. Examples: 8, 10, 12")
            continue  # go back to the menu

        length = int(length_text)

        # Characters to use: letters + digits + special characters
        characters = string.ascii_letters + string.digits + string.punctuation

        generated_password = ""

        # Pick random characters until the password reaches the desired length
        for i in range(length):
            random_character = random.choice(characters)
            generated_password = generated_password + random_character

        print("Generated password:", generated_password)

    # ---------------------------------------------------------
    # 3. Hash a password
    # ---------------------------------------------------------
    elif option == "3":
        password_to_hash = input("Enter password to hash: ")

        print("The password will be hashed using the SHA-256 method.")
        print("Hashing is a one-way transformation that makes the original password unreadable.")
        print("The same password always produces the same hash, but you cannot easily find the original password from the hash.")

        # Step 1: Convert the string into bytes
        # Computers cannot process text directly; they work with bytes (0s and 1s)
        password_bytes = password_to_hash.encode()

        # Step 2: Create a SHA-256 hash object
        # This prepares the data to be hashed using the SHA-256 algorithm
        hash_object = hashlib.sha256(password_bytes)

        # Step 3: Convert the hash result into a readable hexadecimal string
        # hexdigest() turns the hash into characters like 0-9 and a-f
        hashed_password = hash_object.hexdigest()

        print("SHA-256 hash result:", hashed_password)

    # ---------------------------------------------------------
    # 4. Exit the program
    # ---------------------------------------------------------
    elif option == "4":
        print("Exiting the program.")
        break

    else:
        print("Invalid option (please choose between 1 and 4).")
