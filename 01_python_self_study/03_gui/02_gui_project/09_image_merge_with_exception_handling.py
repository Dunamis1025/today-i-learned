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

root = Tk()
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
        filetypes=(("PNG files", "*.png"), ("All files", "*.*")),
        initialdir=r"C:\Users\yunho\OneDrive\Desktop\today_i_learned\today-i-learned"
    )

    for file in files:
        list_file.insert(END, file)


def del_file():
    """
    Delete selected items from the Listbox.
    """
    for index in reversed(list_file.curselection()):
        list_file.delete(index)


def browse_dest_path():
    """
    Open a directory selection dialog and
    set the selected folder as the destination path.
    """
    folder_selected = filedialog.askdirectory()
    if folder_selected == "":
        return

    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

# ==================================================
# Image Merge Logic (Core Feature)
# ==================================================

def merge_image():
    """
    Merge selected images vertically into a single image.
    Apply Width / Spacing / Format options and save the result.
    """

    try:
        # ---------------------------
        # Read options from comboboxes
        # ---------------------------

        # Width option
        img_width = cmb_width.get()
        if img_width == "Original":
            img_width = -1  # Sentinel value: keep original width
        else:
            img_width = int(img_width)  # Combobox returns string

        # Spacing option
        img_space = cmb_space.get()
        if img_space == "Small":
            img_space = 30
        elif img_space == "Medium":
            img_space = 60
        elif img_space == "Large":
            img_space = 90
        else:  # None
            img_space = 0

        # Format option
        img_format = cmb_format.get().lower()  # "JPG" -> "jpg"

        # ---------------------------
        # Load images
        # ---------------------------
        img_paths = list_file.get(0, END)
        images = [Image.open(x) for x in img_paths]

        # ---------------------------
        # Resize images (keep aspect ratio)
        # ---------------------------
        resized_images = []

        if img_width > -1:
            for img in images:
                # new_height = (new_width * original_height) / original_width
                new_height = int(img_width * img.size[1] / img.size[0])
                resized_images.append(img.resize((img_width, new_height)))
        else:
            resized_images = images  # Keep original images

        # ---------------------------
        # Calculate final canvas size
        # ---------------------------
        widths, heights = zip(*(img.size for img in resized_images))
        max_width = max(widths)
        total_height = sum(heights) + img_space * (len(resized_images) - 1)

        # Prepare the canvas (apply spacing if enabled)
        if img_space > 0:
            total_height += (img_space * (len(images)) - 1)

        result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255))

        # ---------------------------
        # Paste images + update progress
        # ---------------------------
        y_offset = 0
        for idx, img in enumerate(resized_images):
            result_img.paste(img, (0, y_offset))
            y_offset += (img.size[1] + img_space)

            progress = (idx + 1) / len(resized_images) * 100
            p_var.set(progress)
            progress_bar.update()

        # ---------------------------
        # Save output
        # ---------------------------
        file_name = "nado_photo." + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path)

        msgbox.showinfo("Notice", "Image merging completed successfully.")

    except Exception as err:
        msgbox.showerror("Error", err)


def start():
    """
    Triggered when the Start button is clicked.
    Validate inputs and start merging.
    """
    if list_file.size() == 0:
        msgbox.showwarning("Warning", "Please add at least one image file.")
        return

    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("Warning", "Please select a destination folder.")
        return

    merge_image()

# ==================================================
# File Control Buttons Frame
# ==================================================

file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, text="Add File", width=12, command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, text="Delete Selected", width=12, command=del_file)
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
    selectmode="extended",
    height=15,
    yscrollcommand=scrollbar.set
)
list_file.pack(side="left", fill="both", expand=True)

scrollbar.config(command=list_file.yview)

# ==================================================
# Destination Path Frame
# ==================================================

path_frame = LabelFrame(root, text="Destination Path")
path_frame.pack(fill="x", padx=5, pady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5)

btn_dest_path = Button(path_frame, text="Browse", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5)

# ==================================================
# Options Frame
# ==================================================

frame_option = LabelFrame(root, text="Options")
frame_option.pack(padx=5, pady=5)

Label(frame_option, text="Width", width=8).pack(side="left")
cmb_width = ttk.Combobox(frame_option, state="readonly", values=["Original", "1024", "800", "640"], width=10)
cmb_width.current(0)
cmb_width.pack(side="left")

Label(frame_option, text="Spacing", width=8).pack(side="left")
cmb_space = ttk.Combobox(frame_option, state="readonly", values=["None", "Small", "Medium", "Large"], width=10)
cmb_space.current(0)
cmb_space.pack(side="left")

Label(frame_option, text="Format", width=8).pack(side="left")
cmb_format = ttk.Combobox(frame_option, state="readonly", values=["PNG", "JPG", "BMP"], width=10)
cmb_format.current(0)
cmb_format.pack(side="left")

# ==================================================
# Progress Bar Frame
# ==================================================

frame_progress = LabelFrame(root, text="Progress")
frame_progress.pack(fill="x", padx=5, pady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# ==================================================
# Run / Close Buttons Frame
# ==================================================

frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, text="Close", width=12, command=root.quit)
btn_close.pack(side="right")

btn_start = Button(frame_run, text="Start", width=12, command=start)
btn_start.pack(side="right")

# ==================================================
# Window Settings
# ==================================================

root.resizable(False, False)
root.mainloop()
