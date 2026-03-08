import random

# Display the game title and basic instructions for the user
print("Welcome to guess the number")
print("Guess a number between 1 and 10")
print("You get three guesses")

# This variable keeps track of how many wrong attempts the user has made
attempt = 0

# Generate a random target number between 1 and 10
# The user must guess this number correctly to win
myNumber = random.randint(1, 10)

# Start the game loop
# The loop continues while the number of attempts is less than 3
while attempt < 3:
    
    # Print the secret number for testing purposes only
    # In a real game, this line would normally be removed
    print(myNumber)

    # This checks whether the player has already reached 3 attempts
    # In this version, it is kept as part of the class-built code
    if attempt == 3:
        print("You lost, bla bla dammit")
        exit()

    # Ask the user to enter a number and convert the input to an integer
    user_guess = int(input("Pick a number between 1 and 10: "))

    # If the guessed number matches the random number, the player wins
    # break ends the loop immediately
    if user_guess == myNumber:
        print("Winner winner chicken dinner!")
        break

    # If the guessed number is smaller than the target number,
    # tell the user it is too low and increase the attempt count
    elif user_guess < myNumber:
        print("Too low!")
        attempt += 1

    # If the guessed number is greater than the target number,
    # tell the user it is too high and increase the attempt count
    elif user_guess > myNumber:
        print("Too High!")
        attempt += 1

    # This else block is intended to handle unexpected input,
    # although int(input()) will already reject non-numeric input before this point
    else:
        print("That is not a number I recognize.")

# After the loop finishes, print the losing message with the attempt count
# This line runs when the loop ends without a winning break
print(f"You lost, you had {attempt} attempts at it")
