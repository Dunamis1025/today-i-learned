from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")  # width x height

# First Checkbutton
chkvar = IntVar()  # Stores the Checkbutton state as an integer (0 or 1)
chkbox = Checkbutton(root, text="Do not show again today", variable=chkvar)

# chkbox.select()
# -> Displays the Checkbutton as checked by default

# chkbox.deselect()
# -> Forces the Checkbutton to be unchecked
# -> Useful for clearing the checked state if chkbox.select() was used earlier

# By default, a Checkbutton is unchecked when created.
# deselect() can be used to explicitly reset the state if needed.
chkbox.pack()

# Second Checkbutton
chkvar2 = IntVar()  # Stores the second Checkbutton state
chkbox2 = Checkbutton(root, text="Do not show again for a week", variable=chkvar2)
chkbox2.pack()

def btncmd():
    # Print the current state of each Checkbutton
    # 0 = unchecked, 1 = checked
    print(chkvar.get())
    print(chkvar2.get())

btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()
