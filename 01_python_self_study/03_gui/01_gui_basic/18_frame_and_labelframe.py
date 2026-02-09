from tkinter import *

# Create the main application window
root = Tk()
root.title("Nado GUI")
root.geometry("640x480")  # width x height

# --------------------------------------------------
# Top label: instruction message
Label(root, text="Please select a menu").pack(side="top")

# Bottom button: order action
Button(root, text="Place Order").pack(side="bottom")

# --------------------------------------------------
# Burger menu frame (plain Frame with border)
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="Hamburger").pack()
Button(frame_burger, text="Cheeseburger").pack()
Button(frame_burger, text="Chicken Burger").pack()

# --------------------------------------------------
# Drink menu frame (LabelFrame with a visible title)
frame_drink = LabelFrame(root, text="Drinks")
frame_drink.pack(side="right", fill="both", expand=True)

Button(frame_drink, text="Cola").pack()
Button(frame_drink, text="Sprite").pack()

# Start the Tkinter event loop
root.mainloop()
