"""
34_custom_module_and_import_practice.py

What I learned:
- How to create my own Python module
- How Python treats a .py file as a module
- How to import a custom module
- How to call a function from another file

This practice marks the end of my Python basic fundamentals.
"""

# ==================================================
# Practice Goal
# ==================================================
# 1. Create a custom module (byme.py)
# 2. Define a function inside that module
# 3. Import the module from another file
# 4. Execute the function using module.function() syntax
#
# This exercise helps solidify the concept of:
# "Python code can be reused by importing it as a module."
# ==================================================


# --------------------------------------------------
# Import my custom module
# --------------------------------------------------
import byme


# --------------------------------------------------
# Call a function from the imported module
# --------------------------------------------------
byme.sign()


"""
Expected Output:

This program was created by Shinyhat.
YouTube : http://youtube.com
Email   : yunho1025@gmail.com
"""
"""
byme.py

This file is a custom Python module created by me.
In Python:
- One .py file = one module
"""

def sign():
    """
    Prints information about the creator of this program.
    """

    print("This program was created by Shinyhat.")
    print("YouTube : http://youtube.com")
    print("Email   : yunho1025@gmail.com")
  
- A Python module is simply a .py file.
- import brings another file's code into the current file.
- module.function() makes it clear where the function comes from.
- Custom modules work the same way as built-in or external libraries.
