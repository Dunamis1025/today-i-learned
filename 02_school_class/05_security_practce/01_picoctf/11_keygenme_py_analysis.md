## 1. Challenge Overview
* **Platform**: picoCTF
* **Challenge**: keygenme-py
* **Category**: Reverse Engineering (Medium)
* **Objective**: Reverse engineer a Python-based "Arcane Calculator" to find a valid license key (Flag).

---

## 2. Technical Analysis (Q&A Style)

### Q1: Why are these modules imported?
* `hashlib`: Used to generate SHA256 hashes from the username to create a unique key.
* `cryptography.fernet`: A symmetric encryption system used to decrypt the "Full Version" code once the correct key is provided.
* `base64`: Used for encoding/decoding data into a format that is safe for transmission or storage.

### Q2: What do the Global Variables represent?
* `arcane_loop_trial = True`: A boolean flag that controls the main execution loop of the trial menu.
* `jump_into_full = False`: A status flag that triggers the transition to the full version upon successful key validation.
* `full_version_code = ""`: A placeholder string that will store the decrypted source code of the full application.

### Q3: How is the "Dynamic Part" of the key constructed?
The `check_key()` function compares specific characters of the user input against a SHA256 hash of the username `BENNETT`.



---

## 3. Step-by-Step Solution

### Step 1: Generate the Hash
I executed the following command in the Python terminal to get the hex digest of the username:
```python
import hashlib
print(hashlib.sha256(b"BENNETT").hexdigest())
# Output: ba6c084a4d888e1f7c3b0fc71d61c4625708bd915b5e0e60eb73e1667251b567
```
### Step 2: Extract Characters by Index
Following the logic in the source code, I extracted characters from the hash using Zero-based Indexing:

hash[4] -> 0

hash[5] -> 8

hash[3] -> c

hash[6] -> 4

hash[2] -> 6

hash[7] -> a

hash[1] -> a

hash[8] -> 4

Resulting Dynamic Segment: 08c46aa4

---

## 4. Source Code Reference (Simplified)
# Crucial part of the check_key function
def check_key(key, username_trial):
    # ... logic to check static parts ...
    
    # Validation of the dynamic segment via indexing
    if key[i] != hashlib.sha256(username_trial).hexdigest()[4]: return False
    i += 1
    if key[i] != hashlib.sha256(username_trial).hexdigest()[5]: return False
    # ... repeated for indices [3, 6, 2, 7, 1, 8] ...
    return True

## 5. Personal Reflection & Learning
Logical Flow over Syntax: I learned that understanding the "Input -> Process -> Output" flow is more critical than memorizing every line of code.

Importance of Indexing: Reconfirmed that in Python, indexing starts at 0, which is a fundamental concept in software exploitation and analysis.

Global Perspective: Writing documentation in English ensures that my technical growth and problem-solving process are accessible to a global audience.

---

Final Flag: picoCTF{1n_7h3_kk3y_of_08c46aa4}    
