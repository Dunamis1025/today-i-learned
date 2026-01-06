import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog
from PIL import Image

# ==================================================
# About ttk (Themed Tkinter)
# ==================================================
# ttk is a themed version of tkinter widgets.
# It provides a more modern and native-looking UI
# that automatically matches the operating system style.
#
# Common ttk widgets used in this project:
# - Combobox     : dropdown selection widget
# - Progressbar  : visual indicator of task progress

# ==================================================
# Main Window Setup
# ==================================================

# Create the main Tkinter window (entry point of the GUI app)
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
        # Initial directory when the dialog opens
        initialdir=r"C:\Users\yunho\OneDrive\Desktop\today_i_learned\today-i-learned"
    )

    # Insert each selected file path into the Listbox
    # Listbox.insert() only accepts one item at a time
    for file in files:
        list_file.insert(END, file)


def del_file():
    """
    Delete selected items from the Listbox.
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

    # Get all file paths from the Listbox and open them as images
    # Here, x represents a single image file path (string)
    images = [Image.open(x) for x in list_file.get(0, END)]

    # Each image size is a tuple: (width, height)
    # size[0] = width, size[1] = height
    widths = [x.size[0] for x in images]
    heights = [x.size[1] for x in images]

    # Final image dimensions:
    # - Width: maximum width among all images
    # - Height: sum of all image heights
    max_width, total_height = max(widths), sum(heights)

    # Create a blank canvas image
    # "RGB" means a color image (Red, Green, Blue)
    # (255, 255, 255) represents a white background
    result_img = Image.new(
        "RGB",
        (max_width, total_height),
        (255, 255, 255)
    )

    # y_offset represents the vertical position
    # where the next image will be pasted
    y_offset = 0

    # Paste images one by one from top to bottom
    for img in images:
        # Paste the image at position (0, y_offset)
        result_img.paste(img, (0, y_offset))

        # Move the y position down by the height of the current image
        y_offset += img.size[1]

    # Build the final output file path
    dest_path = os.path.join(
        txt_dest_path.get(),
        "nado_photo.jpg"
    )

    # Save the merged image
    result_img.save(dest_path)

    # Show completion message
    msgbox.showinfo("Notice", "Image merging completed successfully.")


def start():
    """
    Triggered when the Start button is clicked.
    This function validates inputs and starts the merge process.
    """

    # Print selected options (for debugging / future use)
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

    # Start image merge
    merge_image()

# ==================================================
# File Control Buttons Frame
# ==================================================

file_frame = Frame(root)

# fill="x" means the frame expands horizontally
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

# Bind scrollbar to Listbox
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
# Options Frame (Currently for learning / future use)
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
# Progress Bar Frame (Placeholder for future logic)
# ==================================================

frame_progress = LabelFrame(root, text="Progress")
frame_progress.pack(fill="x", padx=5, pady=5)

# DoubleVar can store floating-point values
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
