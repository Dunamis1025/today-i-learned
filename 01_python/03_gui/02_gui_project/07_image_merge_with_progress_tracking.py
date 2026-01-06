import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog
from PIL import Image

# ==================================================
# About ttk (Themed Tkinter)
# ==================================================
# ttk is a themed extension of tkinter widgets.
# It provides a more modern and native-looking UI
# that automatically adapts to the operating system style.
#
# Common ttk widgets used in this project:
# - Combobox    : dropdown selection widget
# - Progressbar : visual indicator of task progress

# ==================================================
# Main Window Setup
# ==================================================

# Create the main Tkinter window (entry point of the GUI application)
root = Tk()

# Title displayed on the window title bar
root.title("Nado GUI")

# ==================================================
# File Handling Functions
# ==================================================

def add_file():
    """
    Open a file selection dialog and allow the user
    to select multiple image files at once.

    The selected file paths are added to the Listbox.
    """

    files = filedialog.askopenfilenames(
        title="Select image files",
        filetypes=(
            ("PNG files", "*.png"),
            ("All files", "*.*")
        ),
        # Initial directory shown when the dialog opens
        initialdir=r"C:\Users\yunho\OneDrive\Desktop\today_i_learned\today-i-learned"
    )

    # Insert each selected file path into the Listbox
    # Listbox.insert() only accepts one item at a time
    for file in files:
        list_file.insert(END, file)


def del_file():
    """
    Remove selected items from the Listbox.
    """

    # curselection() returns selected indices as a tuple
    # Deleting from the end prevents index shifting issues
    for index in reversed(list_file.curselection()):
        list_file.delete(index)


def browse_dest_path():
    """
    Open a directory selection dialog and
    set the selected folder as the destination path.
    """

    folder_selected = filedialog.askdirectory()

    # If the user clicks Cancel, an empty string is returned
    if folder_selected == "":
        return

    # Clear existing text and insert the selected path
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

# ==================================================
# Image Merge Logic (Core Feature)
# ==================================================

def merge_image():
    """
    Merge selected images vertically into a single image
    and save the result to the destination folder.
    """

    # Retrieve all file paths from the Listbox and open them as Image objects
    # Here, 'x' represents a single image file path (string)
    images = [Image.open(x) for x in list_file.get(0, END)]

    # Each image has a size tuple: (width, height)
    widths = [img.size[0] for img in images]
    heights = [img.size[1] for img in images]

    # Determine final image dimensions
    # - Width  : maximum width among all images
    # - Height : sum of all image heights
    max_width = max(widths)
    total_height = sum(heights)

    # Create a blank canvas for the merged image
    # "RGB" represents a color image (Red, Green, Blue)
    # (255, 255, 255) sets a white background
    result_img = Image.new(
        "RGB",
        (max_width, total_height),
        (255, 255, 255)
    )

    # y_offset keeps track of the vertical paste position
    y_offset = 0

    # Paste images one by one from top to bottom
    for idx, img in enumerate(images):
        result_img.paste(img, (0, y_offset))
        y_offset += img.size[1]

        # Calculate and update progress percentage
        progress = (idx + 1) / len(images) * 100
        p_var.set(progress)
        progress_bar.update()

    # Build the output file path
    dest_path = os.path.join(
        txt_dest_path.get(),
        "nado_photo.jpg"
    )

    # Save the merged image
    result_img.save(dest_path)

    # Notify the user that the process is complete
    msgbox.showinfo("Notice", "Image merging completed successfully.")


def start():
    """
    Triggered when the Start button is clicked.

    This function:
    - Validates user input
    - Prints selected options (for debugging / future expansion)
    - Starts the image merge process
    """

    # Print selected options (currently for learning purposes)
    print("Width :", cmb_width.get())
    print("Spacing :", cmb_space.get())
    print("Format :", cmb_format.get())

    # Validate image file list
    if list_file.size() == 0:
        msgbox.showwarning("Warning", "Please add at least one image file.")
        return

    # Validate destination path
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("Warning", "Please select a destination folder.")
        return

    # Start merging images
    merge_image()

# ==================================================
# File Control Buttons Frame
# ==================================================

file_frame = Frame(root)

# fill="x" allows horizontal expansion
# padx / pady add outer spacing
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(
    file_frame,
    text="Add File",
    width=12,
    command=add_file
)
btn_add_file.pack(side="left")

btn_del_file = Button(
    file_frame,
    text="Delete Selected",
    width=12,
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

# Bind scrollbar to the Listbox
scrollbar.config(command=list_file.yview)

# ==================================================
# Destination Path Frame
# ==================================================

path_frame = LabelFrame(root, text="Destination Path")
path_frame.pack(fill="x", padx=5, pady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(
    side="left",
    fill="x",
    expand=True,
    padx=5
)

btn_dest_path = Button(
    path_frame,
    text="Browse",
    width=10,
    command=browse_dest_path
)
btn_dest_path.pack(side="right", padx=5)

# ==================================================
# Options Frame (Prepared for future feature expansion)
# ==================================================

frame_option = LabelFrame(root, text="Options")
frame_option.pack(padx=5, pady=5)

# Width option
Label(frame_option, text="Width", width=8).pack(side="left")
cmb_width = ttk.Combobox(
    frame_option,
    state="readonly",
    values=["Original", "1024", "800", "640"],
    width=10
)
cmb_width.current(0)
cmb_width.pack(side="left")

# Spacing option
Label(frame_option, text="Spacing", width=8).pack(side="left")
cmb_space = ttk.Combobox(
    frame_option,
    state="readonly",
    values=["None", "Small", "Medium", "Large"],
    width=10
)
cmb_space.current(0)
cmb_space.pack(side="left")

# Format option
Label(frame_option, text="Format", width=8).pack(side="left")
cmb_format = ttk.Combobox(
    frame_option,
    state="readonly",
    values=["PNG", "JPG", "BMP"],
    width=10
)
cmb_format.current(0)
cmb_format.pack(side="left")

# ==================================================
# Progress Bar Frame
# ==================================================

frame_progress = LabelFrame(root, text="Progress")
frame_progress.pack(fill="x", padx=5, pady=5)

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
    command=root.quit
)
btn_close.pack(side="right")

btn_start = Button(
    frame_run,
    text="Start",
    width=12,
    command=start
)
btn_start.pack(side="right")

# ==================================================
# Window Settings
# ==================================================

# Disable window resizing
root.resizable(False, False)

# Start the Tkinter event loop
root.mainloop()
