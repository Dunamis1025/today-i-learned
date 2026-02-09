import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog

# ==================================================
# About ttk (Themed Tkinter)
# ==================================================
# ttk is a themed version of tkinter widgets.
# It provides a more modern, native-looking UI
# that automatically matches the operating system theme.
#
# Common ttk widgets used here:
# - Combobox     : dropdown selection widget
# - Progressbar  : visual progress indicator

# ==================================================
# Main Window Setup
# ==================================================

# Create the main application window
root = Tk()

# Title shown on the window title bar
root.title("Nado GUI")

# ==================================================
# File Handling Functions
# ==================================================

def add_file():
    """
    Opens a file selection dialog and allows the user
    to select multiple image files at once.

    filedialog.askopenfilenames():
    - Opens a file selection window
    - Allows multi-file selection
    - Returns selected file paths as a tuple

    Example return value:
    ('C:/img/a.png', 'C:/img/b.png')
    """

    files = filedialog.askopenfilenames(
        title="Select image files",
        filetypes=(
            ("PNG files", "*.png"),
            ("All files", "*.*")
        ),
        # initialdir defines the starting folder
        # Raw string (r"...") prevents Windows path issues
        initialdir=r"C:\Users\yunho\OneDrive\Desktop\today_i_learned"
    )

    # Each selected file must be inserted individually
    # because Listbox.insert() only accepts one item at a time
    for file in files:
        # END means append to the end of the list
        list_file.insert(END, file)


def del_file():
    """
    Deletes selected items from the file list.

    list_file.curselection():
    - Returns selected item indices as a tuple
    - Example: (0, 2, 3)
    """

    # Delete from the back to avoid index shifting issues
    for index in reversed(list_file.curselection()):
        list_file.delete(index)


def browse_dest_path():
    """
    Opens a folder selection dialog
    and sets the selected path as the destination folder.
    """

    folder_selected = filedialog.askdirectory()

    # If the user clicks Cancel, an empty string is returned
    if folder_selected == "":
        return

    # Clear existing text and insert the selected path
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)


def start():
    """
    Triggered when the Start button is clicked.

    This function:
    - Reads selected options
    - Validates file list and destination path
    - Shows warning messages if required inputs are missing
    """

    # Print selected option values (for debugging)
    print("Width :", cmb_width.get())
    print("Spacing :", cmb_space.get())
    print("Format :", cmb_format.get())

    # Validate file list
    if list_file.size() == 0:
        msgbox.showwarning("Warning", "Please add at least one image file.")
        return

    # Validate destination path
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("Warning", "Please select a destination folder.")
        return


# ==================================================
# File Control Buttons Frame
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

# Bind scrollbar and listbox together
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
    ipady=4  # Increase entry height without changing font size
)

btn_dest_path = Button(
    path_frame,
    text="Browse",
    width=10,
    command=browse_dest_path
)
btn_dest_path.pack(side="right", padx=5, pady=5)

# ==================================================
# Options Frame
# ==================================================

frame_option = LabelFrame(root, text="Options")
frame_option.pack(padx=5, pady=5, ipady=5)

# ---------- Width Option ----------
Label(frame_option, text="Width", width=8).pack(side="left", padx=5)

opt_width = ["Original", "1024", "800", "640"]
cmb_width = ttk.Combobox(
    frame_option,
    state="readonly",
    values=opt_width,
    width=10
)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5)

# ---------- Spacing Option ----------
Label(frame_option, text="Spacing", width=8).pack(side="left", padx=5)

opt_space = ["None", "Small", "Medium", "Large"]
cmb_space = ttk.Combobox(
    frame_option,
    state="readonly",
    values=opt_space,
    width=10
)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5)

# ---------- Format Option ----------
Label(frame_option, text="Format", width=8).pack(side="left", padx=5)

opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(
    frame_option,
    state="readonly",
    values=opt_format,
    width=10
)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5)

# ==================================================
# Progress Bar Frame
# ==================================================

frame_progress = LabelFrame(root, text="Progress")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

# DoubleVar allows floating-point progress values
p_var = DoubleVar()

progress_bar = ttk.Progressbar(
    frame_progress,
    maximum=100,
    variable=p_var
)
progress_bar.pack(fill="x", padx=5, pady=5)

# ==================================================
# Run / Close Buttons Frame
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
btn_close.pack(side="right", padx=5)

btn_start = Button(
    frame_run,
    text="Start",
    width=12,
    padx=5,
    pady=5,
    command=start
)
btn_start.pack(side="right", padx=5)

# ==================================================
# Window Settings
# ==================================================

# Disable window resizing
root.resizable(False, False)

# Start the Tkinter event loop
root.mainloop()
