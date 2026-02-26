from tkinter import *

# Create main window
main = Tk()
main.title("Number Guessing Game")

# Secret answer
answer = 7

# Function executed when button is pressed
def check_answer():
    user_input = input_box.get()

    try:
        guess = int(user_input)

        if guess == answer:
            result_label.config(text="Correct! 🎉")
        elif guess > answer:
            result_label.config(text="Too high! 👇")
        else:
            result_label.config(text="Too low! 👆")

    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Input field
input_box = Entry(main)
input_box.grid(row=0, column=0, columnspan=3)

# Result label
result_label = Label(main, text="Enter a number")
result_label.grid(row=1, column=0, columnspan=3)

# Check button
check_button = Button(main, text="Check", command=check_answer)
check_button.grid(row=2, column=1)

main.mainloop()