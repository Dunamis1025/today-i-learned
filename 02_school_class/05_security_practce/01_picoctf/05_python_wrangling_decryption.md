# 05. Python Wrangling (CTF – Decryption & CLI Arguments)

---

## 1. Overview

This challenge focuses on:

- Running Python scripts from the terminal
- Passing arguments using `sys.argv`
- Understanding basic symmetric encryption using Fernet

---

## 2. Challenge Setup

The challenge provides three files:

- `ende.py` → Python script used for encryption/decryption  
- `flag.txt.en` → Encrypted flag file  
- `password.txt` → Password required for decryption  

---

## 3. Core Concept

To decrypt the flag, three components are required:

- **Tool** → `ende.py`  
- **Key** → password from `password.txt`  
- **Target** → encrypted file `flag.txt.en`  

👉 Without the correct key, the encrypted data is useless.

---

## 4. Solution Steps

### Step 1: Retrieve the password

```bash
cat password.txt
```

Copy the password.

---

### Step 2: Run the Python script in decrypt mode

```bash
python3 ende.py -d flag.txt.en
```

---

### Step 3: Enter the password

When prompted:

```
Please enter the password:
```

Paste the password and press Enter.

---

### Step 4: Get the flag

```text
picoCTF{...}
```

---

## 5. Alternative Execution (Direct Argument)

You can also pass the password directly:

```bash
python3 ende.py -d flag.txt.en <password>
```

---

## 6. Code Analysis (ende.py)

### 6.1 Import Section

```python
import sys
import base64
from cryptography.fernet import Fernet
```

- `sys` → handles command-line arguments  
- `base64` → encodes password into a valid key format  
- `Fernet` → performs encryption/decryption  

---

### 6.2 Argument Handling

```python
sys.argv
```

- `sys.argv[1]` → option (`-e` or `-d`)  
- `sys.argv[2]` → target file  
- `sys.argv[3]` → optional password  

---

### 6.3 Key Generation

```python
ssb_b64 = base64.b64encode(password.encode())
c = Fernet(ssb_b64)
```

- Converts user input into a valid Fernet key  
- Required before encryption/decryption  

---

### 6.4 Decryption Logic

```python
with open(sys.argv[2], "r") as f:
    data = f.read()
    data_c = c.decrypt(data.encode())
    sys.stdout.buffer.write(data_c)
```

- Reads encrypted file  
- Decrypts using the generated key  
- Outputs the original content (flag)  

---

## 7. Key Concepts Learned

### 7.1 CLI Argument Handling
- Python scripts can receive input directly from terminal commands

### 7.2 Symmetric Encryption
- The same key is used for both encryption and decryption

### 7.3 Base64 Encoding
- Required to transform user input into a valid encryption key

---

## 8. Commands Summary

| Command | Description |
|--------|------------|
| `cat file` | Display file content |
| `python3 script.py` | Run Python script |
| `-d` | Decrypt mode |
| `-e` | Encrypt mode |

---

## 9. Key Insight

👉 **"Encryption is meaningless without proper key management."**

- Encrypted data alone cannot be used  
- The password (key) is essential  

---

## 10. Personal Reflection

- Learned how Python scripts interact with the terminal  
- Understood how encryption and keys work together  
- Realized the importance of automation tools in cybersecurity  

---

## 11. One-Line Summary

👉 **"Use a Python script with the correct key to decrypt protected data."**
