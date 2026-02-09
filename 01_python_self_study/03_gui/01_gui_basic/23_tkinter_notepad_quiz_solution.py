import os
from tkinter import *

"""
========================================
📝 Quiz: Simple Notepad Application
========================================

Create a simple Notepad-style text editor using Tkinter.

Requirements:
1. Create a main window with a title similar to Windows Notepad.
2. Set the window size to 640x480.
3. Add a Text widget for writing notes.
4. Add a vertical Scrollbar connected to the Text widget.
5. Create a menu bar with a "File" menu that includes:
   - Open: load text from a file into the editor
   - Save: save the current text to a file
   - Exit: close the application
6. Use a fixed filename (e.g. mynote.txt).
7. When opening a file, replace existing text instead of appending it.

========================================
Answer Code
========================================
"""

# Create main window
root = Tk()
root.title("Untitled - Windows Notepad")

# Set window size (width x height)
root.geometry("640x480")

# File name used for open/save
filename = "mynote.txt"


def open_file():
    """
    Open the text file and display its contents
    inside the Text widget.
    """
    # Check if the file exists
    if os.path.isfile(filename):  # True if file exists, False otherwise
        with open(filename, "r", encoding="utf8") as file:
            # Delete existing text from the Text widget
            # "1.0" means the very first character (line 1, column 0)
            # END means the end of the text
            # If this is not used, new content would be appended instead
            txt.delete("1.0", END)

            # Insert file content into the Text widget
            txt.insert(END, file.read())


def save_file():
    """
    Save the current contents of the Text widget
    into the file.
    """
    with open(filename, "w", encoding="utf8") as file:
        # Get all text from the Text widget
        # from the beginning ("1.0") to the end (END)
        file.write(txt.get("1.0", END))


# Create menu bar
menu = Menu(root)

# File menu
menu_file = Menu(menu, tearoff=0)
# tearoff=0 removes the dashed line that allows detaching the menu
# This matches modern Windows-style menus

menu_file.add_command(label="Open", command=open_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)

# add_cascade:
# Attaches a submenu to the main menu bar
# label="File" is the text shown on the menu bar
menu.add_cascade(label="File", menu=menu_file)

# Other menus (placeholders)
menu.add_cascade(label="Edit")
menu.add_cascade(label="Format")
menu.add_cascade(label="View")
menu.add_cascade(label="Help")

# Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# Text editor area
txt = Text(root, yscrollcommand=scrollbar.set)

# fill="both" → expand horizontally and vertically
# expand=True → allow the widget to grow when the window is resized
txt.pack(side="left", fill="both", expand=True)

# Connect scrollbar to Text widget
scrollbar.config(command=txt.yview)

# Attach menu to the window
root.config(menu=menu)

# Run the application
root.mainloop()
