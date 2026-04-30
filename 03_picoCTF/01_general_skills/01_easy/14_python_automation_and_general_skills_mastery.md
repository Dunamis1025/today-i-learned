

# [picoCTF] General Skills - Practical Mastery and Python Automation

## 1. Overview
Today's session focused on finalizing the "Easy" difficulty challenges in the General Skills category. The primary goal was to bridge the gap between basic Linux CLI usage and Python-based automation to solve common CTF hurdles.

## 2. Challenge Breakdown

### A. Glitch Cat
*   **Concept**: Retrieving flags from services that output raw Python function calls instead of plaintext.
*   **Technique**: Used `nc` (Netcat) to connect to the server, then piped the output (ASCII character codes via `chr()`) into a Python interpreter to reconstruct the flag string.
*   **Key Learning**: Python's interactive shell is a powerful tool for immediate decoding of obfuscated data.

### B. Codebook
*   **Concept**: Understanding file system dependencies in script execution.
*   **Technique**: Downloaded both `code.py` and `codebook.txt` into the same directory. Executed the script using `python3 code.py` which programmatically parsed the local text file to unlock the flag.
*   **Key Learning**: Script behavior often depends on relative file paths and local metadata files.

### C. convertme.py
*   **Concept**: Manual data representation and base conversion.
*   **Technique**: Executed a Python script that challenged the user with a Decimal-to-Binary conversion. Converted the decimal value (e.g., 41) to binary (101001) to satisfy the script's condition.
*   **Key Learning**: Proficiency in number systems (Binary, Hex, Decimal) is essential for bypassing conditional check gates in CTF tasks.

### D. HashingJobApp
*   **Concept**: Real-time data integrity and hashing.
*   **Technique**: Faced a time-limited challenge requiring the MD5 hash of a specific string. Utilized Python's `hashlib` library for rapid conversion.
*   **Automation Snippet**:
    ```python
    import hashlib
    print(hashlib.md5(b'target_word').hexdigest())
    ```
*   **Key Learning**: Speed is a factor in security tasks; knowing how to leverage Python libraries for hashing is more efficient than manual lookup.

## 3. Summary of Tools & Commands Used
| Tool/Library | Usage |
| :--- | :--- |
| `nc` | Connecting to remote challenge instances. |
| `python3` | Executing scripts and debugging in REPL mode. |
| `hashlib` | Generating MD5 hashes for data verification. |
| `wget` | Fetching challenge artifacts from remote repositories. |

## 4. Conclusion
Successfully cleared the General Skills (Easy) path. The experience emphasized the importance of a streamlined workflow between the terminal and the Python environment—a critical skill for the upcoming CTF competition on April 11th.
