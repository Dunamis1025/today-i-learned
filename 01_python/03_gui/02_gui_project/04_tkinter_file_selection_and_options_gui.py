import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog

# ==================================================
# About ttk (Themed Tkinter)
# ==================================================
# ttk provides modern, theme-aware widgets.
# Widgets like Combobox and Progressbar are part of ttk,
# offering better UI consistency across platforms.

# ==================================================
# Main Window Setup
# ==================================================

# Create the main Tkinter window
root = Tk()
root.title("Nado GUI")  # Window title displayed on the title bar


# ==================================================
# File Handling Functions
# ==================================================

def add_file():
    """
    filedialog.askopenfilenames():
    - Opens a file selection dialog
    - Allows selecting multiple files at once
    - Returns a tuple of selected file paths
    """

    files = filedialog.askopenfilenames(
        title="Select image files",
        filetypes=(
            ("PNG files", "*.png"),
            ("All files", "*.*")
        ),
        # initialdir defines the folder shown when the dialog opens
        # Raw string (r"...") prevents issues with backslashes on Windows
        initialdir=r"C:\Users\yunho\OneDrive\Desktop\today_i_learned\today-i-learned\01_python\02_pygame\02_pygame_project_pang_game\images"
    )

    # The dialog returns multiple file paths as a tuple
    # Example: ('C:/img/a.png', 'C:/img/b.png')

    # A for-loop is required because:
    # - Listbox.insert() can only add one item at a time
    # - Each file path must be inserted individually
    for file in files:
        # END means "append to the last position in the list"
        list_file.insert(END, file)


def del_file():
    """
    list_file.curselection():
    - Returns indices of selected items
    - Example: (0, 2, 3)
    """

    # Delete items in reverse order to prevent index shifting
    for index in reversed(list_file.curselection()):
        list_file.delete(index)


# ==================================================
# File Button Frame
# ==================================================

file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(
    file_frame,
    text="Add File",
    width=12,
    padx=5,
    pady=5,
    command=add_file
)
btn_add_file.pack(side="left")

btn_del_file = Button(
    file_frame,
    text="Delete Selected",
    width=12,
    padx=5,
    pady=5,
    command=del_file
)
btn_del_file.pack(side="right")


# ==================================================
# File List Frame (Listbox + Scrollbar)
# ==================================================

list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(
    list_frame,
    selectmode="extended",  # Enable Ctrl / Shift multi-selection
    height=15,
    yscrollcommand=scrollbar.set
)
list_file.pack(side="left", fill="both", expand=True)

# Connect scrollbar and listbox (two-way binding)
scrollbar.config(command=list_file.yview)


# ==================================================
# Destination Path Frame
# ==================================================

path_frame = LabelFrame(root, text="Destination Path")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(
    side="left",
    fill="x",
    expand=True,
    padx=5,
    pady=5,
    # ipady adds internal vertical padding
    # This increases the widget height without changing font size
    ipady=4
)

btn_dest_path = Button(
    path_frame,
    text="Browse",
    width=10
)
btn_dest_path.pack(side="right", padx=5, pady=5)


# ==================================================
# Options Frame
# ==================================================

frame_option = LabelFrame(root, text="Options")
frame_option.pack(padx=5, pady=5, ipady=5)

# ---------- Width Option ----------
lbl_width = Label(frame_option, text="Width", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

opt_width = ["Original", "1024", "800", "640"]
cmb_width = ttk.Combobox(
    frame_option,
    state="readonly",  # Prevent manual text input
    values=opt_width,
    width=10
)

# current(0) selects the first item (index starts at 0)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# ---------- Space Option ----------
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

# DoubleVar supports floating-point progress values
p_var = DoubleVar()

progress_bar = ttk.Progressbar(
    frame_progress,
    maximum=100,
    variable=p_var
)
progress_bar.pack(fill="x", padx=5, pady=5)


# ==================================================
# Run Frame (Start / Close)
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
btn_close.pack(side="right", padx=5, pady=5)

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

# Disable window resizing (width, height)
root.resizable(False, False)

# Start the Tkinter event loop
root.mainloop()
