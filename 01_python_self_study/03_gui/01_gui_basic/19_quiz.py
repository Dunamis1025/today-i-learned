"""
====================================
📝 Quiz: Simple Notepad Application
====================================

[Problem]
Create a simple Notepad-like text editor using Tkinter with the following features:

1. A main window titled "Untitled - Windows Notepad"
2. A fixed window size of 640x480
3. A text area where users can type notes
4. A vertical scrollbar connected to the text area
5. A menu bar with:
   - File > Open (load text from a file)
   - File > Save (save text to a file)
   - File > Exit (close the application)
6. The text file name should be "mynote.txt"
7. When opening a file, existing text in the editor should be cleared first
8. Use proper file encoding (UTF-8)

[Goal]
Demonstrate basic GUI layout, menu handling, file I/O,
and widget interaction using Tkinter.
"""

import os
from tkinter import *

# ===============================
# 1️⃣ Create main window
# ===============================
root = Tk()
root.title("Untitled - Windows Notepad")

# Set window size (width x height)
root.geometry("640x480")

# File name used for open/save
filename = "mynote.txt"

# ===============================
# 2️⃣ File handling functions
# ===============================

def open_file():
    # Check if the file exists before opening
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf8") as file:
            # Delete existing content in the Text widget
            # "1.0" = first line, first character
            # END = end of all text
            # Without this, file content would be appended
            txt.delete("1.0", END)

            # Insert file content into the Text widget
            txt.insert(END, file.read())

def save_file():
    with open(filename, "w", encoding="utf8") as file:
        # Get all text from the Text widget and save it
        file.write(txt.get("1.0", END))

# ===============================
# 3️⃣ Menu bar setup
# ===============================

menu = Menu(root)

# File menu
# tearoff=0 disables the dashed line that allows detaching the menu
menu_file = Menu(menu, tearoff=0)

menu_file.add_command(label="Open", command=open_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)

# add_cascade:
# Attaches a submenu to the main menu bar
# label="File" is the text shown on the menu bar
menu.add_cascade(label="File", menu=menu_file)

# Other menu placeholders (no functionality yet)
menu.add_cascade(label="Edit")
menu.add_cascade(label="Format")
menu.add_cascade(label="View")
menu.add_cascade(label="Help")

# ===============================
# 4️⃣ Scrollbar and Text widget
# ===============================

# Create vertical scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# Create text area
txt = Text(root, yscrollcommand=scrollbar.set)

# expand=True:
# Allows the widget to expand and fill extra space when the window resizes
txt.pack(side="left", fill="both", expand=True)

# Connect scrollbar to the Text widget
scrollbar.config(command=txt.yview)

# ===============================
# 5️⃣ Apply menu and run app
# ===============================
root.config(menu=menu)
root.mainloop()
