from tkinter import *

# Create the main Tkinter window
root = Tk()
root.title("Nado GUI")  # Set window title


# =========================
# File Frame
# (Add File / Delete Selection buttons)
# =========================

# Frame to group file-related buttons
file_frame = Frame(root)
file_frame.pack()

# Add File button
btn_add_file = Button(
    file_frame,
    padx=5,   # Horizontal internal padding (space inside the button)
    pady=5,   # Vertical internal padding
    width=12, # Fixed button width regardless of text length
    text="Add File"
)
btn_add_file.pack(side="left")  # Align button to the left

# Delete Selection button
btn_del_file = Button(
    file_frame,
    padx=5,
    pady=5,
    width=12,
    text="Delete Selected"
)
btn_del_file.pack(side="right")  # Align button to the right


# =========================
# List Frame
# (Listbox + Scrollbar)
# =========================

# Frame to hold the listbox and scrollbar together
list_frame = Frame(root)

# fill="both":
# Make the frame expand both horizontally and vertically
list_frame.pack(fill="both")

# Vertical scrollbar
scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")  # Attach to the right and fill vertically

# Listbox to display selected files
list_file = Listbox(
    list_frame,
    selectmode="extended",   # Allow multiple selections (Ctrl / Shift)
    height=15,               # Number of visible rows
    yscrollcommand=scrollbar.set
    # Sync listbox scrolling with the scrollbar
)

# fill="both": expand in both directions
# expand=True: take up extra available space when the window grows
list_file.pack(side="left", fill="both", expand=True)

# Link scrollbar movement to the listbox view
scrollbar.config(command=list_file.yview)

# NOTE:
# yscrollcommand=scrollbar.set  → listbox controls scrollbar position
# scrollbar.config(command=...) → scrollbar controls listbox scrolling
# Both are required for proper two-way scrolling behavior


# =========================
# Destination Path Frame
# =========================

# LabelFrame to group destination path widgets
path_frame = LabelFrame(root, text="Destination Path")
path_frame.pack()

# Entry widget to display the selected save path
txt_dest_path = Entry(path_frame)

# fill="x": expand horizontally only
# expand=True: take up remaining horizontal space
# ipady=4: increase internal vertical padding for better appearance
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4)

# Browse button to select destination folder
btn_dest_path = Button(
    path_frame,
    text="Browse",
    width=10
)
btn_dest_path.pack(side="right")


# =========================
# Window Settings
# =========================

# Disable window resizing
# First False  → disable horizontal resizing
# Second False → disable vertical resizing
root.resizable(False, False)

# Start the Tkinter event loop
# Keeps the window open and listens for user interactions
root.mainloop()
