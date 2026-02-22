"""
File name example:
15_file_system_metadata_and_path_handling.py

📌 Today's Learning Topic
Working with file system paths and file metadata using:
- os module
- datetime module

This script demonstrates:

✅ Checking the current working directory
✅ Changing directories
✅ Building file paths safely
✅ Extracting directory names
✅ Getting file timestamps (creation, modification, access)
✅ Converting timestamps to readable format
✅ Getting file size in bytes

------------------------------------------------------------
⚠️ Important Notes
------------------------------------------------------------

1) os.path.getctime()
   - On Windows: returns file creation time.
   - On Linux/macOS: may return metadata change time instead.
   - The meaning is OS-dependent.

2) Timestamp values
   - Returned as Unix timestamp (seconds since 1970-01-01).
   - Must be converted using datetime.fromtimestamp() to be readable.

3) Relative paths
   - Always based on the current working directory.
   - Use os.getcwd() to verify your location.

4) Common mistake
   - Do NOT reuse the wrong timestamp variable when formatting output.
   - Each time (ctime, mtime, atime) should be formatted separately.
"""

import os
import datetime


# -----------------------------------------------------------
# 1️⃣ Check Current Working Directory
# -----------------------------------------------------------
# Relative paths depend on this location.
# If a file cannot be found, check this first.
# print(os.getcwd())


# -----------------------------------------------------------
# 2️⃣ Change Working Directory
# -----------------------------------------------------------
# os.chdir("rpa_basic")   # move into subfolder
# os.chdir("..")          # move to parent folder
# os.chdir("../..")       # move to grandparent folder
# os.chdir("c:/")         # move to absolute path (Windows example)
# print(os.getcwd())


# -----------------------------------------------------------
# 3️⃣ Build File Path Safely
# -----------------------------------------------------------
# Avoid manually writing slashes.
# os.path.join() ensures cross-platform compatibility.

# file_path = os.path.join(os.getcwd(), "my_file.txt")
# print(file_path)


# -----------------------------------------------------------
# 4️⃣ Extract Directory Name from File Path
# -----------------------------------------------------------
# Returns only the directory portion of a full path.

# example = r"C:\Users\yunho\OneDrive\Desktop\today-i-learned\my_file.txt"
# print(os.path.dirname(example))


# -----------------------------------------------------------
# 5️⃣ File Timestamp Information
# -----------------------------------------------------------

file_path = "05_rpa_basic/02_desktop/15_file_system_metadata_and_path_handling.py"


# (1) Creation Time
ctime = os.path.getctime(file_path)
print("Creation timestamp:", ctime)

print(
    "Creation time:",
    datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S")
)


# (2) Modification Time
mtime = os.path.getmtime(file_path)
print(
    "Modification time:",
    datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S")
)


# (3) Last Access Time
atime = os.path.getatime(file_path)
print(
    "Last access time:",
    datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S")
)


# -----------------------------------------------------------
# 6️⃣ File Size
# -----------------------------------------------------------
size = os.path.getsize(file_path)
print("File size (bytes):", size)

# Optional: Convert to KB / MB
# print("File size (KB):", size / 1024)
# print("File size (MB):", size / (1024 * 1024))


"""
------------------------------------------------------------
Summary
------------------------------------------------------------

- os.getcwd()      → get current directory
- os.chdir()       → change directory
- os.path.join()   → build path safely
- os.path.dirname()→ extract folder path
- getctime()       → creation time (Windows)
- getmtime()       → modification time
- getatime()       → last access time
- getsize()        → file size in bytes

This practice strengthens understanding of how Python interacts
with the operating system's file system.
"""
