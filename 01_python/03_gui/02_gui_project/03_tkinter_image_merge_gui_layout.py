import tkinter.ttk as ttk
from tkinter import *

# ==================================================
# Main Window Setup
# ==================================================

# Create the main Tkinter window
root = Tk()

# Set the title text shown on the window title bar
root.title("Nado GUI")


# ==================================================
# File Frame
# (Add File / Delete Selected buttons)
# ==================================================

# Frame:
# - A container widget used to group related widgets together
# - Makes layout management easier and more organized
file_frame = Frame(root)

# fill="x":
# - Expand the frame horizontally to match the window width
# padx / pady:
# - Add outer spacing (margin) around the frame
file_frame.pack(fill="x", padx=5, pady=5)

# Add File button
btn_add_file = Button(
    file_frame,
    text="Add File",
    width=12,     # Fixed button width (independent of text length)
    padx=5,       # Inner horizontal padding (space inside the button)
    pady=5        # Inner vertical padding
)
btn_add_file.pack(side="left")

# Delete Selected button
btn_del_file = Button(
    file_frame,
    text="Delete Selected",
    width=12,     # width keeps both buttons visually aligned
    padx=5,
    pady=5
)
btn_del_file.pack(side="right")


# ==================================================
# List Frame
# (Listbox + Scrollbar)
# ==================================================

# Frame that contains both the Listbox and the Scrollbar
list_frame = Frame(root)

# fill="both":
# - Expand in both horizontal and vertical directions
# This allows the listbox to grow with the window
list_frame.pack(fill="both", padx=5, pady=5)

# Vertical Scrollbar widget
scrollbar = Scrollbar(list_frame)

# fill="y":
# - Scrollbar should stretch vertically only
scrollbar.pack(side="right", fill="y")

# Listbox:
# - Displays multiple file paths selected by the user
list_file = Listbox(
    list_frame,
    selectmode="extended",  # Allow multiple selection (Ctrl / Shift)
    height=15,              # Number of visible rows
    yscrollcommand=scrollbar.set  # Link listbox scrolling to scrollbar
)
list_file.pack(side="left", fill="both", expand=True)

# scrollbar.config(command=...):
# - When the scrollbar is moved, it controls the listbox view
scrollbar.config(command=list_file.yview)

# NOTE:
# yscrollcommand  → Listbox updates scrollbar position
# scrollbar.command → Scrollbar controls listbox scrolling
# Both are required for proper two-way scrolling


# ==================================================
# Destination Path Frame
# ==================================================

# LabelFrame:
# - Same as Frame but with a visible border and title text
# "Destination Path" refers to the folder where the merged image will be saved
path_frame = LabelFrame(root, text="Destination Path")

# ipady:
# - Adds internal vertical space inside the LabelFrame
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

# Entry widget:
# - Used to display the selected destination folder path
# "dest" is short for "destination"
txt_dest_path = Entry(path_frame)

# expand=True:
# - Allows this widget to take up any remaining horizontal space
# This is why the Entry grows while the Browse button stays fixed
txt_dest_path.pack(
    side="left",
    fill="x",
    expand=True,
    padx=5,
    pady=5,
    ipady=4
)

# Browse button:
# - Will later open a folder selection dialog
btn_dest_path = Button(
    path_frame,
    text="Browse",
    width=10     # Fixed width for consistent UI
)
btn_dest_path.pack(side="right", padx=5, pady=5)


# ==================================================
# Option Frame
# ==================================================

# Options for width, spacing, and format
frame_option = LabelFrame(root, text="Options")
frame_option.pack(padx=5, pady=5, ipady=5)

# ---------- Width Option ----------

# Label:
# width is used to align labels evenly,
# not to control text padding
lbl_width = Label(frame_option, text="Width", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

opt_width = ["Original", "1024", "800", "640"]

# ttk.Combobox:
# - A dropdown widget provided by ttk (Themed Tkinter)
# - Looks more modern than the basic Tkinter widgets
cmb_width = ttk.Combobox(
    frame_option,
    state="readonly",   # Prevents manual typing
    values=opt_width,
    width=10
)

# current(0):
# - Selects the first option by default
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# ---------- Spacing Option ----------

lbl_space = Label(frame_option, text="Space", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

opt_space = ["None", "Small", "Medium", "Large"]

cmb_space = ttk.Combobox(
    frame_option,
    state="readonly",
    values=opt_space,
    width=10
)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# ---------- Format Option ----------

lbl_format = Label(frame_option, text="Format", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

opt_format = ["PNG", "JPG", "BMP"]

cmb_format = ttk.Combobox(
    frame_option,
    state="readonly",
    values=opt_format,
    width=10
)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)


# ==================================================
# Progress Bar Frame
# ==================================================

frame_progress = LabelFrame(root, text="Progress")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

# DoubleVar:
# - A Tkinter variable that stores floating-point values
# - Required to dynamically update the progress bar value
p_var = DoubleVar()

# ttk.Progressbar:
# - Visual indicator of task progress
# - Will be updated during image processing
progress_bar = ttk.Progressbar(
    frame_progress,
    maximum=100,
    variable=p_var
)
progress_bar.pack(fill="x", padx=5, pady=5)


# ==================================================
# Run Frame
# (Start / Close buttons)
# ==================================================

frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

# Close button:
# - Calls root.quit() to exit the application
btn_close = Button(
    frame_run,
    text="Close",
    width=12,
    padx=5,
    pady=5,
    command=root.quit
)
btn_close.pack(side="right", padx=5, pady=5)

# Start button:
# - Will later trigger the image merge process
btn_start = Button(
    frame_run,
    text="Start",
    width=12,
    padx=5,
    pady=5
)
btn_start.pack(side="right", padx=5, pady=5)


# ==================================================
# Window Settings
# ==================================================

# Disable window resizing:
# - Prevents layout breaking due to resizing
root.resizable(False, False)

# Start the Tkinter event loop
# This keeps the window open and responsive
root.mainloop()
