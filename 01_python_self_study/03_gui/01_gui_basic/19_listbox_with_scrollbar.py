from tkinter import *

# Create the main application window
root = Tk()
root.title("Nado GUI")
root.geometry("640x480")  # width x height

# --------------------------------------------------
# Frame to group Listbox and Scrollbar together
frame = Frame(root)
frame.pack()

# Vertical scrollbar
scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# --------------------------------------------------
# Listbox with scrollbar connection
# yscrollcommand=scrollbar.set is required
# Without this, the scrollbar moves but immediately snaps back
listbox = Listbox(
    frame,
    selectmode="extended",
    height=10,
    yscrollcommand=scrollbar.set
)

# Insert sample data (days of the month)
for i in range(1, 32):  # 1 ~ 31
    listbox.insert(END, f"{i} day")

listbox.pack(side="left")

# --------------------------------------------------
# Connect scrollbar back to the listbox
# This allows the scrollbar to control the listbox view
scrollbar.config(command=listbox.yview)

# Start the Tkinter event loop
root.mainloop()
