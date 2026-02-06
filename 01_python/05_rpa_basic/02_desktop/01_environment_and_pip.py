"""
📌 Python Environment & pip Summary (Desktop Automation - RPA Basic)

This file is NOT meant to be executed.
It is a learning-note file written as Python comments,
summarising what I studied about:

- virtual environments (venv)
- pip
- why "pip install" sometimes fails
- how Python decides where libraries are installed

This file exists to document understanding, not to run code.
"""

# ==================================================
# 1️⃣ What is venv?
# ==================================================
# venv = Virtual Environment
#
# A virtual environment is an isolated Python environment
# created specifically for ONE project.
#
# Think of it as:
# - A private Python interpreter
# - With its own pip
# - With its own installed libraries
#
# This prevents conflicts between projects that require
# different versions of the same library.


# ==================================================
# 2️⃣ What does `python -m venv venv` actually do?
# ==================================================
# python            -> run the current Python interpreter
# -m venv           -> run Python's built-in venv module
# venv              -> name of the folder to create
#
# Meaning:
# "Create a virtual environment named 'venv'
#  using THIS Python as the base."
#
# This creates:
# - a copy (or link) of Python
# - a dedicated pip
# - a separate site-packages folder


# ==================================================
# 3️⃣ What's inside the venv folder? (Windows)
# ==================================================
# venv/
# ├─ Scripts/
# │   ├─ python.exe      -> Python used when venv is active
# │   ├─ pip.exe         -> pip tied to THIS Python
# │   └─ activate.bat    -> activation script
# │
# ├─ Lib/
# │   └─ site-packages/  -> where installed libraries live
# │
# └─ pyvenv.cfg          -> venv configuration file
#
# Deleting the venv folder completely removes the environment.


# ==================================================
# 4️⃣ What does "activate" really do?
# ==================================================
# Activating a venv does NOT install anything.
#
# It only:
# - modifies PATH
# - makes `python` and `pip` point to venv versions
# - shows (venv) in the terminal prompt
#
# After activation:
# python -> venv/Scripts/python.exe
# pip    -> venv/Scripts/pip.exe


# ==================================================
# 5️⃣ What is pip?
# ==================================================
# pip = "Pip Installs Packages"
#
# pip is the package manager for Python.
# It installs libraries from PyPI (Python Package Index).
#
# Example:
# pip install pyautogui
#
# Means:
# "Download pyautogui and install it
#  into THIS Python environment."


# ==================================================
# 6️⃣ Why `pip install` sometimes doesn't work
# ==================================================
# The most common mistake:
#
# - Installing a library with one Python
# - Running code with a DIFFERENT Python
#
# Result:
# ModuleNotFoundError
#
# The fix is to bind pip to the current Python:
#
# python -m pip install package_name
#
# This guarantees:
# - pip belongs to THIS python
# - library is installed in the correct environment


# ==================================================
# 7️⃣ How to verify installation correctly
# ==================================================
# To check if a library is installed in the active environment:
#
# python -m pip show pyautogui
#
# If information appears:
# - installation succeeded
# - Python can see the library
#
# If nothing appears:
# - wrong environment
# - wrong Python
# - or library not installed


# ==================================================
# 8️⃣ Key takeaway (VERY IMPORTANT)
# ==================================================
# Most "it doesn't work" errors are NOT code problems.
#
# They are:
# ❌ folder issues
# ❌ environment mismatches
# ❌ pip pointing to the wrong Python
#
# Correct mindset:
# "When imports fail, check the environment first."
#
# This applies to:
# - pyautogui
# - selenium
# - pandas
# - openpyxl
# - almost all Python libraries
