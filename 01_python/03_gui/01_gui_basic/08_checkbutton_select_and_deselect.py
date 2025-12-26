from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")  # width x height

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

def btncmd():
    pass

btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()
