"""

This file contains foundational exercises learned in class.

Topics:
- for loop
- range()
- random module
- while loop
- break
- counter (attempts)
- tkinter basics (Label, Button, Entry)
- pack() vs grid()
- command functions
"""

# ==========================================
# 1️⃣ FOR LOOP
# ==========================================

numbers = [10, 20, 30, 40, 50]

for x in numbers:
    square = x * x
    print(f"The square of {x} is {square}")


# ==========================================
# 2️⃣ RANGE FUNCTION
# ==========================================

# Print even numbers from 0 to 20
for i in range(0, 21, 2):
    print(i)


# ==========================================
# 3️⃣ RANDOM MODULE
# ==========================================

import random

secret_number = random.randint(1, 100)
print(f"Random number: {secret_number}")


# ==========================================
# 4️⃣ WHILE LOOP + BREAK
# ==========================================

"""
Basic infinite loop structure.
break is used to exit the loop.
"""

# myNumber = random.randint(1, 10)

# while True:
#     user_guess = int(input("Enter a number: "))
#     if user_guess == myNumber:
#         print("Correct!")
#         break
#     elif user_guess > myNumber:
#         print("Too high!")
#     else:
#         print("Too low!")


# ==========================================
# 5️⃣ LIMITED ATTEMPTS
# ==========================================

"""
Using a counter to limit attempts.
"""

# attempts = 0
# while attempts < 3:
#     attempts += 1
#     print("Attempt:", attempts)


# ==========================================
# 6️⃣ TKINTER BASICS
# ==========================================

"""
Basic GUI elements:
- Window creation
- Label
- Button
- Entry
- pack() vs grid()
"""

# from tkinter import *

# main = Tk()
# main.title("My First GUI")

# Label
# myLabel = Label(main, text="Hello World")
# myLabel.pack()

# Entry (input field)
# input_box = Entry(main)
# input_box.pack()

# Button with function
# def myClick():
#     user_input = input_box.get()
#     print("User entered:", user_input)
#     myLabel.config(text="You typed: " + user_input)

# myButton = Button(main, text="Click Me", command=myClick)
# myButton.pack()

# main.mainloop()


# ==========================================
# 🎯 SUMMARY
# ==========================================

"""
What I learned:
- Loop structures
- Random number generation
- Condition logic
- Event-driven GUI basics
- Layout management in Tkinter
"""