"""
18_shutil_file_and_folder_operations.py

Topic:
File and Folder Operations using shutil

This file demonstrates how to copy files, copy directories,
and move or rename folders using Python's shutil module.
"""

import shutil


# ============================================================
# 1️⃣ File Copy Operations
# ============================================================

"""
shutil.copy(src, dst)

If dst is a folder:
    → The file keeps its original name inside the folder.

If dst includes a new filename:
    → The file is copied using the new name.

Important:
The destination folder must already exist.
Otherwise, FileNotFoundError will occur.
"""

# Example:
# shutil.copy("run_btn.png", "test_folder")
# shutil.copy("run_btn.png", "test_folder/copied_run_btn.png")


"""
shutil.copyfile(src, dst)

- Copies file contents only.
- dst must be a full file path (including filename).
- Does NOT copy metadata.
"""

# shutil.copyfile("run_btn.png", "test_folder/copied_run_btn_2.png")


"""
shutil.copy2(src, dst)

- Similar to copy()
- Also copies metadata (timestamps, etc.)
- Often preferred in real-world applications
"""

# shutil.copy2("run_btn.png", "test_folder/copy2.png")


# ============================================================
# 2️⃣ Copying Entire Folders
# ============================================================

"""
shutil.copytree(src_dir, dst_dir)

- Copies entire directory including all subfolders and files.
- The destination directory must NOT already exist.
"""

# shutil.copytree("test_folder", "test_folder2")
# shutil.copytree("test_folder", "test_folder3")


# ============================================================
# 3️⃣ Moving and Renaming (move)
# ============================================================

"""
shutil.move(src, dst)

- Can move files or folders.
- Can also act like renaming.

Example 1: Move folder into another folder
move("test_folder", "test_folder3")
→ Result: test_folder3/test_folder

Example 2: Rename folder
move("test_folder3", "test_folder")
→ test_folder3 is renamed to test_folder

Important:
Behavior depends on whether the destination exists.
Always check directory structure before using move().
"""

# Example practice:
# shutil.move("test_folder", "test_folder3")
# shutil.move("test_folder2", "test_folder3")

# Rename effect example
shutil.move("test_folder3", "test_folder")
