# ===============================
# File Handling with "with"
# ===============================
# The "with" statement automatically manages resources
# → The file is closed automatically after the block ends
# → Prevents file leaks and makes the code cleaner

# ===============================
# 1️⃣ Write text to a file
# ===============================

# "w" = write mode (creates a new file or overwrites an existing one)
# encoding="utf8" ensures the file supports Unicode characters
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("I am studying Python very hard.")

# ===============================
# 2️⃣ Read text from a file
# ===============================

# "r" = read mode
# study_file.read() reads the entire contents of the file at once
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
