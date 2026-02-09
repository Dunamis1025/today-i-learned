from tkinter import *

# Create the main application window
root = Tk()
root.title("Nado GUI")
root.geometry("640x480")  # width x height

# Create two buttons
btn1 = Button(root, text="Button 1")
btn2 = Button(root, text="Button 2")

# --------------------------------------------------
# pack() examples (commented out)
# btn1.pack()
# btn2.pack()

# btn1.pack(side="left")
# btn2.pack(side="right")

# btn1.pack(side="left")
# btn2.pack(side="left")

# --------------------------------------------------
# grid() example
# grid places widgets in a table-like structure (row, column)
btn1.grid(row=0, column=0)
btn2.grid(row=1, column=1)

# Start the Tkinter event loop
root.mainloop()
