import tkinter.ttk as ttk
from tkinter import *

# ==================================================
# Main Window Setup
# ==================================================

# Create the main Tkinter window
root = Tk()
root.title("Nado GUI")  # Window title


# ==================================================
# File Frame
# (Add File / Delete Selected buttons)
# ==================================================

# Frame to group file-related buttons together
file_frame = Frame(root)
file_frame.pack(fill="x")  # Stretch horizontally

# Add File button
btn_add_file = Button(
    file_frame,
    text="Add File",
    width=12,
    padx=5,
    pady=5
)
btn_add_file.pack(side="left")  # Align to the left

# Delete Selected button
btn_del_file = Button(
    file_frame,
    text="Delete Selected",
    width=12,
    padx=5,
    pady=5
)
btn_del_file.pack(side="right")  # Align to the right


# ==================================================
# List Frame
# (Listbox + Scrollbar)
# ==================================================

# Frame to hold Listbox and Scrollbar together
list_frame = Frame(root)
list_frame.pack(fill="both")  # Expand both horizontally & vertically

# Vertical scrollbar
scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

# Listbox to display selected files
list_file = Listbox(
    list_frame,
    selectmode="extended",      # Allow multi-select (Ctrl / Shift)
    height=15,
    yscrollcommand=scrollbar.set
)
list_file.pack(side="left", fill="both", expand=True)

# Connect scrollbar to listbox scrolling
scrollbar.config(command=list_file.yview)

# NOTE:
# - yscrollcommand → Listbox controls scrollbar position
# - scrollbar.config(command=...) → Scrollbar controls listbox view
# Both are required for proper two-way scrolling


# ==================================================
# Destination Path Frame
# ==================================================

# LabelFrame visually groups related widgets
path_frame = LabelFrame(root, text="Destination Path")
path_frame.pack(fill="x")

# Entry widget to display selected destination folder
txt_dest_path = Entry(path_frame)
txt_dest_path.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=4  # Increase internal vertical padding
)

# Browse button (folder selection)
btn_dest_path = Button(
    path_frame,
    text="Browse",
    width=10
)
btn_dest_path.pack(side="right")


# ==================================================
# Option Frame
# ==================================================

frame_option = LabelFrame(root, text="Options")
frame_option.pack(padx=5, pady=5)

# ---------- Width Option ----------
Label(frame_option, text="Width", width=8).pack(side="left")

opt_width = ["Original", "1024", "800", "640"]
cmb_width = ttk.Combobox(
    frame_option,
    state="readonly",   # Prevent manual typing
    values=opt_width,
    width=10
)
cmb_width.current(0)  # Default selection
cmb_width.pack(side="left")

# ---------- Space Option ----------
Label(frame_option, text="Space", width=8).pack(side="left")

opt_space = ["None", "Small", "Medium", "Large"]
cmb_space = ttk.Combobox(
    frame_option,
    state="readonly",
    values=opt_space,
    width=10
)
cmb_space.current(0)
cmb_space.pack(side="left")

# ---------- Format Option ----------
Label(frame_option, text="Format", width=8).pack(side="left")

opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(
    frame_option,
    state="readonly",
    values=opt_format,
    width=10
)
cmb_format.current(0)
cmb_format.pack(side="left")


# ==================================================
# Progress Bar Frame
# ==================================================

frame_progress = LabelFrame(root, text="Progress")
frame_progress.pack(fill="x", padx=5, pady=5)

# DoubleVar allows smooth floating-point progress updates
p_var = DoubleVar()
progress_bar = ttk.Progressbar(
    frame_progress,
    maximum=100,
    variable=p_var
)
progress_bar.pack(fill="x")


# ==================================================
# Run Frame (Start / Close buttons)
# ==================================================

frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(
    frame_run,
    text="Close",
    width=12,
    padx=5,
    pady=5,
    command=root.quit
)
btn_close.pack(side="right")

btn_start = Button(
    frame_run,
    text="Start",
    width=12,
    padx=5,
    pady=5
)
btn_start.pack(side="right")


# ==================================================
# Window Settings
# ==================================================

# Disable window resizing (X-axis, Y-axis)
root.resizable(False, False)

# Start the Tkinter event loop
root.mainloop()
