# PicoCTF Challenge Write-up: PW Crack 4

## 1. Challenge Overview
* **Name:** PW Crack 4
* **Goal:** Find the correct password from a list of 100 possibilities to decrypt the flag.
* **Provided Files:**
    * `level4.py`: The password checker and decryption script.
    * `level4.hash.bin`: The MD5 hash of the correct password (binary data).
    * `level4.flag.txt.enc`: The encrypted flag file.

## 2. Key Concepts Learned

### A. Understanding Binary Data (.bin)
I learned that `.bin` files contain raw binary data, not text. Attempting to open `level4.hash.bin` in a text editor like Notepad results in garbled characters. This is normal; the data is meant to be read and processed by the script, not a human.

### B. MD5 Hashing Mechanism
The challenge demonstrated how password verification works. The script computes the MD5 hash of the input password and compares it against the stored correct hash.

### C. Brute Force Automation
Instead of manually typing all 100 password possibilities (which is tedious and error-prone), I wrote a Python script to automate the process. This is the core concept of a Brute Force attack.

### D. Linux Command Line Practice (Webshell)
I practiced essential Linux commands:
* `wget`: For downloading challenge files.
* `nano`: For editing the Python script on the terminal.
* `rm`: For deleting old files to start with a clean slate.
* `python3`: For running the script.

## 3. Solution Approach

My strategy was to modify the execution part of `level4.py` to automatically iterate through the list of potential passwords.

### The Problem in the Original Code:
The original script used `input()` to prompt for a single password entry.

### The Modified Code for Automation:
I replaced the `input()` call with a `for` loop that iterates through `pos_pw_list` (the list of 100 candidates) and compares each candidate's hash with the correct hash.

```python
# --- Automation Part (Inserted into level4.py) ---
for password in pos_pw_list:
    # str_to_hash() converts the password string to an MD5 hash
    # correct_pw_hash is read from level4.hash.bin
    if str_to_hash(password) == correct_pw_hash:
        print(f"Found it! Correct password: {password}")
        # Call the decryption function with the correct password
        decryption_function(password) 
        break
```
Note: In my final implementation, I encountered a minor issue with function names (level_4_pw_check vs. level4_pw_check). For simplicity and clarity in a write-up, it's better to represent the logic.

Alternative, Simpler Solution:
After identifying the correct password using the loop method, a simpler way to get the flag is to restart with the original level4.py script and manually enter the found password: 9f63. This method is useful on a webshell if you find editing with nano cumbersome.

Reset environment: rm * then re-download files.

Run script: python3 level4.py

Enter password: 9f63

##4. Final Flag
The correct password was 9f63. Entering this into the script yielded the flag: picoCTF{...}
