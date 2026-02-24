"""
17_file_system_manage_folders.py

📌 Topic: Creating and Deleting Folders using os and shutil

In this file, we learn:
- How to create nested folders
- The difference between os.rmdir() and shutil.rmtree()
- Why deleting folders can be dangerous
- How to safely check before deleting

This is written clearly so I can understand it again later.
"""

import os
import shutil


# ------------------------------------------------------------
# 1) Create nested folders using os.makedirs()
# ------------------------------------------------------------
"""
Why use os.makedirs()?

- os.mkdir("a/b/c") fails if parent folders do not exist.
- os.makedirs("a/b/c") creates ALL missing parent folders automatically.

Example:
new_folders/a/b/c

If new_folders does not exist → create it.
If a does not exist → create it.
If b does not exist → create it.
Then create c.
"""

# exist_ok=True prevents error if the folder already exists
os.makedirs("new_folders/a/b/c", exist_ok=True)


# ------------------------------------------------------------
# 2) Delete empty folder using os.rmdir()
# ------------------------------------------------------------
"""
os.rmdir("folder")

- Can ONLY remove an empty folder.
- If the folder contains files or subfolders, it will fail.

Since new_folders contains subfolders,
os.rmdir("new_folders") would normally fail.
"""

# os.rmdir("new_folders")  # This would fail if not empty


# ------------------------------------------------------------
# 3) Delete entire folder tree using shutil.rmtree()
# ------------------------------------------------------------
"""
shutil.rmtree("folder")

- Deletes the folder AND everything inside it.
- Works even if the folder contains files and subfolders.

⚠ WARNING:
This permanently deletes everything.
Be very careful with the path.
"""

target_folder = "new_folders"

# Safety check before deleting
if os.path.exists(target_folder):
    print(f"[INFO] '{target_folder}' exists. Deleting now...")
    shutil.rmtree(target_folder)
    print(f"[DONE] '{target_folder}' has been completely removed.")
else:
    print(f"[SKIP] '{target_folder}' does not exist.")


# ------------------------------------------------------------
# ✅ Summary
# ------------------------------------------------------------
"""
Folder Creation:
- os.mkdir("folder") → creates one folder only
- os.makedirs("a/b/c") → creates nested folders
- exist_ok=True → prevents error if folder already exists

Folder Deletion:
- os.rmdir("folder") → removes empty folder only
- shutil.rmtree("folder") → removes entire folder tree (dangerous)

Best Practice:
Always check with os.path.exists() before deleting.
"""
