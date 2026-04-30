# 09. Detailed Logic Analysis: Password Cracking with MD5 and Dictionary Attack

## 1. Objective
The goal is to decrypt an encrypted flag file (`level5.flag.txt.enc`) by finding the correct password using a Dictionary Attack. Since the original password's MD5 hash is provided, we compare the hashes of all candidate passwords in a dictionary file to identify the correct one.

## 2. Technical Breakdown of the Code

### A. XOR Decryption Function (`str_xor`)
This function handles the actual decryption of the flag once the password is found.
* **Key Extension:** Since the `key` (password) is shorter than the `secret` (encrypted flag), a `while` loop is used to repeat the key until its length matches the secret.
* **Modulo Operation (`%`):** Used within the loop to cycle through the key's indices (`0, 1, 2...`) repeatedly.
* **XOR Logic:** The core operation uses a list comprehension: `chr(ord(secret_c) ^ ord(new_key_c))`. It converts characters to their integer ASCII values, performs the XOR, and converts them back to characters.

### B. MD5 Hashing Function (`hash_pw`)
This function converts a plain-text password into an MD5 hash for comparison.
* **Byte Conversion:** Uses `bytearray()` and `.encode()` to transform the string password into a byte stream, which is required by the `hashlib` library.
* **Hashing Process:** Initializes an MD5 object using `hashlib.md5()`, updates it with the bytes, and returns the raw binary digest using `.digest()`.

### C. File Handling and Environment
* **Binary Read Mode (`'rb'`):** Used to read `level5.flag.txt.enc` and `level5.hash.bin`. This is critical because these files contain raw binary data, not plain text.
* **Dictionary File (`'r'`):** The `dictionary.txt` is opened in standard read mode to iterate through potential password strings line by line.

## 3. Implementation of the Dictionary Attack (`level_5_pw_check`)
This is the main control logic of the script:

1.  **Iterative Search:** The script uses a `for line in f:` loop to process every single password candidate in the dictionary.
2.  **String Cleaning:** `line.strip()` is used to remove newline characters (`\n`) or trailing spaces. Failing to do this would result in an incorrect hash.
3.  **Hash Verification:** For each candidate, it calculates the MD5 hash and compares it against the `correct_pw_hash` found in the `.bin` file.
4.  **Automatic Decryption:** Once the condition `if hash_pw(password) == correct_pw_hash:` is met:
    * The script prints the discovered password.
    * It immediately calls `str_xor` with the encrypted flag and the found password.
    * The decrypted flag (the "picoCTF{...}" string) is displayed on the terminal.

## 4. Execution Workflow in Terminal
To execute the attack successfully:
1.  Navigate to the directory: `cd downloads`
2.  Run the script: `python level5.py`
3.  **Result:** The script identifies the password (e.g., `eee0`) and outputs the flag: `picoCTF{h45h_sl1ng1ng_fffcda23}`.
