import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog
from PIL import Image

# ==================================================
# About ttk (Themed Tkinter)
# ==================================================
# ttk is an enhanced version of tkinter widgets.
# It provides a modern, native-looking UI that adapts
# automatically to the operating system's theme.
#
# Common ttk widgets used in this project:
# - Combobox    : dropdown selection widget
# - Progressbar : visual indicator of task progress

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
    Open a file selection dialog that allows the user
    to select multiple image files at once.
    Selected file paths are added to the Listbox.
    """

    files = filedialog.askopenfilenames(
        title="Select image files",
        filetypes=(
            ("PNG files", "*.png"),
            ("All files", "*.*")
        ),
        # Default directory when the dialog opens
        initialdir=r"C:\Users\yunho\OneDrive\Desktop\today_i_learned\today-i-learned"
    )

    # Listbox.insert() accepts only one item at a time,
    # so we insert each file path individually
    for file in files:
        list_file.insert(END, file)


def del_file():
    """
    Remove selected items from the Listbox.
    """

    # curselection() returns selected indices as a tuple.
    # Deleting from the end prevents index shifting issues.
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
    Merge selected images vertically into a single image.
    User-defined Width, Spacing, and Format options
    are applied before saving the result.
    """

    # ---------------------------
    # Width option handling
    # ---------------------------

    img_width = cmb_width.get()

    # Use -1 as a sentinel value to indicate
    # that the original image width should be preserved
    if img_width == "Original":
        img_width = -1
    else:
        # Combobox values are returned as strings,
        # so conversion to int is required for calculations
        img_width = int(img_width)

    # ---------------------------
    # Spacing option handling
    # ---------------------------

    img_space = cmb_space.get()

    # Convert spacing labels into actual pixel values
    if img_space == "Small":
        img_space = 30
    elif img_space == "Medium":
        img_space = 60
    elif img_space == "Large":
        img_space = 90
    else:  # None
        img_space = 0

    # ---------------------------
    # Format option handling
    # ---------------------------

    # Convert format string to lowercase for compatibility
    # with PIL.Image.save() conventions (e.g., "jpg", "png")
    img_format = cmb_format.get().lower()

    # ---------------------------
    # Load images
    # ---------------------------

    # Retrieve all file paths from the Listbox and open them
    images = [Image.open(x) for x in list_file.get(0, END)]

    # ---------------------------
    # Calculate image sizes
    # ---------------------------

    image_sizes = []

    if img_width > -1:
        # Maintain aspect ratio using proportional scaling:
        # new_height = (new_width * original_height) / original_width
        #
        # int() is required because image dimensions
        # must be integer values
        image_sizes = [
            (int(img_width), int(img_width * x.size[1] / x.size[0]))
            for x in images
        ]
    else:
        # Use original image dimensions
        image_sizes = [(x.size[0], x.size[1]) for x in images]

    # Unpack (width, height) tuples into separate sequences
    widths, heights = zip(*image_sizes)

    # Final image dimensions
    max_width = max(widths)
    total_height = sum(heights) + img_space * (len(images) - 1)

    # ---------------------------
    # Create result canvas
    # ---------------------------

    # Create a blank white canvas in RGB mode
    result_img = Image.new(
        "RGB",
        (max_width, total_height),
        (255, 255, 255)
    )

    y_offset = 0

    # ---------------------------
    # Paste images & update progress
    # ---------------------------

    for idx, img in enumerate(images):
        result_img.paste(img, (0, y_offset))
        y_offset += img.size[1] + img_space

        # Calculate and update progress percentage
        progress = (idx + 1) / len(images) * 100
        p_var.set(progress)
        progress_bar.update()

    # ---------------------------
    # Save final image
    # ---------------------------

    dest_path = os.path.join(
        txt_dest_path.get(),
        f"nado_photo.{img_format}"
    )

    result_img.save(dest_path)

    msgbox.showinfo("Notice", "Image merging completed successfully.")

# ==================================================
# Start Button Logic
# ==================================================

def start():
    """
    Triggered when the Start button is clicked.
    Validates inputs before starting the merge process.
    """

    if list_file.size() == 0:
        msgbox.showwarning("Warning", "Please add at least one image file.")
        return

    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("Warning", "Please select a destination folder.")
        return

    merge_image()
