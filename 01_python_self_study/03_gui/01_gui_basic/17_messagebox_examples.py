import tkinter.messagebox as msgbox
from tkinter import *

# Create the main application window
root = Tk()
root.title("Nado GUI")
root.geometry("640x480")  # width x height

# --------------------------------------------------
# Example scenario:
# This program simulates a train ticket booking system
# and demonstrates different types of Tkinter message boxes.

def info():
    # Information dialog (used for successful actions)
    msgbox.showinfo("Information", "Your reservation has been completed successfully.")

def warn():
    # Warning dialog (used when something is not ideal but not fatal)
    msgbox.showwarning("Warning", "This seat is already sold out.")

def error():
    # Error dialog (used when a critical problem occurs)
    msgbox.showerror("Error", "A payment error has occurred.")

def okcancel():
    # OK / Cancel dialog
    # Returns True if OK is clicked, False if Cancel is clicked
    msgbox.askokcancel(
        "Confirm",
        "This seat is reserved for passengers with infants.\nDo you want to continue?"
    )

def retrycancel():
    # Retry / Cancel dialog
    # Useful for temporary issues such as network or system errors
    msgbox.askretrycancel(
        "Retry",
        "A temporary error occurred.\nWould you like to try again?"
    )

def yesno():
    # Yes / No dialog
    # Returns True for Yes, False for No
    msgbox.askyesno(
        "Direction Notice",
        "This seat is facing backward.\nDo you want to proceed with the booking?"
    )

def yesnocancel():
    # Yes / No / Cancel dialog
    # Returns:
    # True  -> Yes
    # False -> No
    # None  -> Cancel
    response = msgbox.askyesnocancel(
        title=None,
        message="Your reservation has not been saved.\nDo you want to save before exiting?"
    )

    print("Response:", response)

    if response is True:
        print("Yes: Save and exit")
    elif response is False:
        print("No: Exit without saving")
    else:
        print("Cancel: Return to the program")

# --------------------------------------------------
# Buttons to trigger each message box example

Button(root, text="Info", command=info).pack()
Button(root, text="Warning", command=warn).pack()
Button(root, text="Error", command=error).pack()

Button(root, text="OK / Cancel", command=okcancel).pack()
Button(root, text="Retry / Cancel", command=retrycancel).pack()
Button(root, text="Yes / No", command=yesno).pack()
Button(root, text="Yes / No / Cancel", command=yesnocancel).pack()

# Start the Tkinter event loop
root.mainloop()
