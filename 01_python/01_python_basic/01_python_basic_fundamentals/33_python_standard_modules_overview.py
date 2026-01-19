"""
📌 What I learned today: Python Standard Modules
(Hands-on practice + understanding module structure)

In this lesson, I explored Python standard modules that are included by default.
I focused on understanding not only how to use them,
but also why they are structured as "module.function".

This includes practical examples of working with:
- files and folders
- the current working directory
- time and date handling

The goal is to understand the structure, not just memorize usage.
"""

# ==================================================
# 1️⃣ glob module – Listing files with patterns
# ==================================================
# The glob module allows you to find files and folders
# using pattern matching.
# It works similarly to the "dir" command on Windows.

import glob

# 🔹 Structure explanation
# glob.glob("*.py")
#
# - The first 'glob'  -> module name (toolbox)
# - The second 'glob' -> function inside that module (actual tool)
#
# Structure:
#
# glob (module)
#  └── glob() (function)
#
# Meaning:
# "Use the glob function inside the glob module"

print(glob.glob("*.py"))

# Example output:
# ['practice.py', 'practice_class.py', 'theater_module.py']


# ==================================================
# 2️⃣ os module – Operating system related features
# ==================================================
# The os module provides functions to interact with the operating system,
# such as working with directories, paths, and environment variables.

import os

# Current Working Directory (cwd)
# This is the folder Python uses as the reference point
# when working with relative paths.
print(os.getcwd())

# Why cwd matters:
# When you open a file like open("data.txt"),
# Python looks for that file inside the cwd.

folder = "sample_dir"

# Check if the folder already exists
if os.path.exists(folder):
    print("The folder already exists.")
    os.rmdir(folder)  # Remove the folder
    print(folder, "folder has been deleted.")
else:
    os.makedirs(folder)  # Create the folder
    print(folder, "folder has been created.")

# Execution flow example:
# 1) Create sample_dir
# 2) Run again → detect it exists
# 3) Delete the folder


# ==================================================
# 3️⃣ time module – Working with time
# ==================================================
# The time module is used for handling system time
# and timestamps.

import time

# Current time as a struct_time object (computer-friendly format)
print(time.localtime())

# strftime = string format time
# Converts time data into a human-readable string format
print(time.strftime("%Y-%m-%d %H:%M:%S"))

# Common format codes:
# %Y : year
# %m : month
# %d : day
# %H : hour (24-hour format)
# %M : minute
# %S : second


# ==================================================
# 4️⃣ strptime – Converting string to time
# ==================================================
# strptime = string parse time
# Parses a formatted string and converts it into a time object.

parsed_time = time.strptime(
    "2026-01-20 14:30:00",
    "%Y-%m-%d %H:%M:%S"
)

print(parsed_time)

# Summary:
# strftime : time   → string (for display)
# strptime : string → time   (for calculation)


# ==================================================
# 5️⃣ datetime module – Working with dates
# ==================================================
# The datetime module provides a more intuitive way
# to work with dates and times.

import datetime

# Print today's date
print("Today's date is:", datetime.date.today())


# ==================================================
# 6️⃣ timedelta – Date calculations
# ==================================================
# timedelta is used to calculate the difference
# between dates or to add/subtract days.

today = datetime.date.today()          # Today's date
td = datetime.timedelta(days=100)      # 100 days

# Calculate the date 100 days from today
print("100 days from today is:", today + td)
