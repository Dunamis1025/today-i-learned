"""
File Name: 16_os_file_system_basics.py

📌 Today's Topic
Working with the file system in Python using the os module.

In this script, I learned how to:

1️⃣ Check and change the current working directory
2️⃣ Create absolute file paths safely
3️⃣ Extract directory information from a file path
4️⃣ Retrieve file metadata (created, modified, accessed time)
5️⃣ Check file size
6️⃣ List files and folders
7️⃣ Walk through subdirectories recursively
8️⃣ Search for a specific file by name
9️⃣ Search for files using patterns (e.g., *.py)

📌 Purpose
When building automation (RPA) or file management tools,
handling files and directories is a fundamental skill.

This script will serve as a reusable reference
for future automation and cybersecurity projects.
"""

import os
import datetime
import fnmatch


# -----------------------------------------------------------
# 1️⃣ Check the current working directory
# -----------------------------------------------------------
# This shows the folder where the script is currently running.
print("📁 Current Working Directory:")
print(os.getcwd())


# -----------------------------------------------------------
# 2️⃣ Create an absolute file path
# -----------------------------------------------------------
# Combine the current directory with a file name safely.
file_path = os.path.join(os.getcwd(), "my_file.txt")

print("\n📌 Absolute Path Example:")
print(file_path)


# -----------------------------------------------------------
# 3️⃣ Extract directory name from a file path
# -----------------------------------------------------------
# This removes the file name and returns only the folder path.
example_path = r"C:\Users\yunho\OneDrive\Desktop\today-i-learned\my_file.txt"

print("\n📂 Directory Name:")
print(os.path.dirname(example_path))


# -----------------------------------------------------------
# 4️⃣ Retrieve file metadata (time and size)
# -----------------------------------------------------------
# Change the file name below if necessary.
target_file = "16_os_file_system_basics.py"

if os.path.exists(target_file):

    # File creation time
    ctime = os.path.getctime(target_file)
    print("\n🕒 Created Time:")
    print(datetime.datetime.fromtimestamp(ctime).strftime("%Y-%m-%d %H:%M:%S"))

    # File last modified time
    mtime = os.path.getmtime(target_file)
    print("\n📝 Modified Time:")
    print(datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S"))

    # File last accessed time
    atime = os.path.getatime(target_file)
    print("\n👀 Last Access Time:")
    print(datetime.datetime.fromtimestamp(atime).strftime("%Y-%m-%d %H:%M:%S"))

    # File size in bytes
    size = os.path.getsize(target_file)
    print("\n📦 File Size (bytes):")
    print(size)

else:
    print("\n⚠ File does not exist. Please check the path.")


# -----------------------------------------------------------
# 5️⃣ List files and folders in the current directory
# -----------------------------------------------------------
print("\n📜 Files and Folders in Current Directory:")
print(os.listdir())


# -----------------------------------------------------------
# 6️⃣ Walk through all subdirectories recursively
# -----------------------------------------------------------
print("\n🔍 Walking Through All Subdirectories:")

for root, dirs, files in os.walk("."):
    print("Current Folder:", root)
    print("Subfolders:", dirs)
    print("Files:", files)
    print("-" * 40)


# -----------------------------------------------------------
# 7️⃣ Search for a specific file by name
# -----------------------------------------------------------
print("\n🎯 Searching for a specific file:")

search_name = "16_os_file_system_basics.py"
found_files = []

for root, dirs, files in os.walk("."):
    if search_name in files:
        found_files.append(os.path.join(root, search_name))

print(found_files)


# -----------------------------------------------------------
# 8️⃣ Search for files using a pattern (e.g., *.py)
# -----------------------------------------------------------
print("\n🧠 Searching files by pattern:")

pattern = "*.py"  # All Python files
matched_files = []

for root, dirs, files in os.walk("."):
    for name in files:
        if fnmatch.fnmatch(name, pattern):
            matched_files.append(os.path.join(root, name))

print(matched_files)


print("\n✅ File system basic practice complete.")
