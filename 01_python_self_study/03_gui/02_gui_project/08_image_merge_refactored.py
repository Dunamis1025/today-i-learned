import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog
from PIL import Image

# ==================================================
# Main Window
# ==================================================

root = Tk()
root.title("Nado GUI")
root.resizable(False, False)

# ==================================================
# File Handling
# ==================================================

def add_file():
    files = filedialog.askopenfilenames(
        title="Select image files",
        filetypes=(("PNG files", "*.png"), ("All files", "*.*"))
    )
    for file in files:
        list_file.insert(END, file)

def del_file():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

def browse_dest_path():
    folder = filedialog.askdirectory()
    if folder:
        txt_dest_path.delete(0, END)
        txt_dest_path.insert(0, folder)

# ==================================================
# Image Merge Logic
# ==================================================

def merge_image():

    # ---------------------------
    # Options
    # ---------------------------
    width_option = cmb_width.get()
    space_option = cmb_space.get()
    format_option = cmb_format.get().lower()

    if width_option == "Original":
        target_width = None
    else:
        target_width = int(width_option)

    if space_option == "Small":
        spacing = 30
    elif space_option == "Medium":
        spacing = 60
    elif space_option == "Large":
        spacing = 90
    else:
        spacing = 0

    # ---------------------------
    # Load & Resize Images
    # ---------------------------
    image_paths = list_file.get(0, END)
    images = []

    for path in image_paths:
        img = Image.open(path)

        if target_width:
            new_height = int(target_width * img.size[1] / img.size[0])
            img = img.resize((target_width, new_height))

        images.append(img)

    # ---------------------------
    # Canvas Size
    # ---------------------------
    widths, heights = zip(*(img.size for img in images))
    max_width = max(widths)
    total_height = sum(heights) + spacing * (len(images) - 1)

    result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255))

    # ---------------------------
    # Paste + Progress
    # ---------------------------
    y_offset = 0
    for idx, img in enumerate(images):
        result_img.paste(img, (0, y_offset))
        y_offset += img.size[1] + spacing

        progress = (idx + 1) / len(images) * 100
        p_var.set(progress)
        progress_bar.update()

    # ---------------------------
    # Save
    # ---------------------------
    save_path = os.path.join(txt_dest_path.get(), f"nado_photo.{format_option}")
    result_img.save(save_path)

    msgbox.showinfo("Notice", "Image merging completed successfully.")

def start():
    if list_file.size() == 0:
        msgbox.showwarning("Warning", "Please add at least one image file.")
        return
    if not txt_dest_path.get():
        msgbox.showwarning("Warning", "Please select a destination folder.")
        return
    merge_image()

# ==================================================
# UI Layout
# ==================================================

# File buttons
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

Button(file_frame, text="Add File", width=12, command=add_file).pack(side="left")
Button(file_frame, text="Delete Selected", width=12, command=del_file).pack(side="right")

# File list
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# Destination path
path_frame = LabelFrame(root, text="Destination Path")
path_frame.pack(fill="x", padx=5, pady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5)
Button(path_frame, text="Browse", width=10, command=browse_dest_path).pack(side="right")

# Options
option_frame = LabelFrame(root, text="Options")
option_frame.pack(padx=5, pady=5)

Label(option_frame, text="Width", width=8).pack(side="left")
cmb_width = ttk.Combobox(option_frame, values=["Original", "1024", "800", "640"], state="readonly", width=10)
cmb_width.current(0)
cmb_width.pack(side="left")

Label(option_frame, text="Spacing", width=8).pack(side="left")
cmb_space = ttk.Combobox(option_frame, values=["None", "Small", "Medium", "Large"], state="readonly", width=10)
cmb_space.current(0)
cmb_space.pack(side="left")

Label(option_frame, text="Format", width=8).pack(side="left")
cmb_format = ttk.Combobox(option_frame, values=["PNG", "JPG", "BMP"], state="readonly", width=10)
cmb_format.current(0)
cmb_format.pack(side="left")

# Progress bar
progress_frame = LabelFrame(root, text="Progress")
progress_frame.pack(fill="x", padx=5, pady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(progress_frame, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# Run buttons
run_frame = Frame(root)
run_frame.pack(fill="x", padx=5, pady=5)

Button(run_frame, text="Close", width=12, command=root.quit).pack(side="right")
Button(run_frame, text="Start", width=12, command=start).pack(side="right")

# ==================================================
# Start App
# ==================================================

root.mainloop()
