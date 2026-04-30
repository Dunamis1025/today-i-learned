import hashlib
import getpass

# ---------------------------------------------------------
# Stored account information (username + hashed password)
# ---------------------------------------------------------

stored_username = "admin"

# 1) Original password (plain text)
original_password = "password123"

# 2) Convert the password into bytes
encoded_password = original_password.encode()

# 3) Apply SHA-256 hashing algorithm
hash_object = hashlib.sha256(encoded_password)

# 4) Convert the hash value into a readable string
stored_password = hash_object.hexdigest()


# ---------------------------------------------------------
# Login attempts (maximum 3 tries)
# ---------------------------------------------------------

login_attempts = 0

while login_attempts < 3:

    # Get user input
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    # Hash the entered password using the same method
    encoded_input = password.encode()
    hash_input = hashlib.sha256(encoded_input)
    hashed_password = hash_input.hexdigest()

    # -----------------------------------------------------
    # Check username and password separately
    # -----------------------------------------------------

    if username != stored_username:
        print("Username does not exist")
        login_attempts += 1

    elif hashed_password != stored_password:
        print("Incorrect password")
        login_attempts += 1

    else:
        print("Login successful")
        break


# ---------------------------------------------------------
# Lock the account after 3 failed attempts
# ---------------------------------------------------------

if login_attempts == 3:
    print("Account locked")