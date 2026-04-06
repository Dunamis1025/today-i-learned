# 07. Password Cracking and Python Brute-force

## 1. Challenge Overview
- **Name:** PW Crack 3 (picoCTF)
- **Objective:** Decrypt the encrypted flag file by identifying the correct password from a list of potential candidates provided in the source code.
- **Resources:** 
    - `level3.py`: The password checker script.
    - `level3.flag.txt.enc`: The encrypted flag.
    - `level3.hash.bin`: The MD5 hash of the correct password.

## 2. Technical Implementation
### Analysis
The script contains a list named `pos_pw_list` with 7 possible passwords. Instead of manually entering each password, I modified the script to automate the cracking process using a brute-force approach.

### Automated Script (Python)
I refactored the `level_3_pw_check()` function to iterate through the password list and automatically compare the hashes.

```python
def level_3_pw_check():
    # Iterate through all passwords in the list
    for password in pos_pw_list:
        user_pw_hash = hash_pw(password)
        
        # Check if the hash matches the correct one
        if( user_pw_hash == correct_pw_hash ):
            print(f"Found! Correct Password: {password}")
            # Decrypt the flag using the correct password
            decryption = str_xor(flag_enc.decode(), password)
            print(f"Flag: {decryption}")
            return 

    print("Password not found.")
```

## 3. Key Learnings & Troubleshooting
### Python Execution Flow (NameError)
- **Problem:** Encountered `NameError: name 'pos_pw_list' is not defined`.
- **Cause:** Python reads code from top to bottom. The list was defined after the function call.
- **Solution:** Moved the `pos_pw_list` definition above the function call to ensure it is defined before use.

### Working Directory (FileNotFoundError)
- **Problem:** Encountered `FileNotFoundError` for the `.enc` file.
- **Cause:** The terminal was running in a different directory than where the files were located.
- **Solution:** Used `cd Downloads` to navigate to the correct directory before executing the script.

## 4. Conclusion
- **Correct Password:** `87ab`
- **Result:** Successfully decrypted the flag by automating the hash comparison.
