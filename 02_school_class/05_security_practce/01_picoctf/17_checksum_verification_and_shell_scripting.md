# Checksum Verification and Shell Scripting (picoCTF: Verify)

## 1. Problem Overview
The objective was to identify a specific "authentic" file among thousands of imitation files using a provided **SHA-256 checksum** and then decrypt it using a shell script.

## 2. Key Concepts Learned

### A. SHA-256 Hashing (The Digital Fingerprint)
A hash function transforms any input data into a fixed-size string of characters. 
- **Integrity:** Even a 1-byte change in the source file results in a completely different hash.
- **Verification:** By comparing the hash of a file to a known "good" hash, we can verify if the file is genuine.

### B. Linux Command Pipeline
The power of Linux comes from combining small tools to perform complex tasks:
- `sha256sum files/*`: Generates hashes for every single file in the directory.
- `|` (Pipe): Passes the massive list of hashes to the next command.
- `grep <hash>`: Searches for the specific string and filters out the noise.

### C. Shell Script Execution
- `./decrypt.sh`: Executing a script in the current directory.
- **Arguments:** Passing the identified file path as an input to the script to trigger the decryption logic.

## 3. Technical Workflow
1. **Identify the Target Hash:** Read the provided `checksum.txt`.
2. **Scan and Filter:** ```bash
   sha256sum files/* | grep fba9f49bf22aa7188a155768ab0dfdc1f9b86c47976cd0f7c9003af2e20598f7


## 4. Identify File: The output reveals the specific filename associated with the hash (e.g., files/87590c24).

```
./decrypt.sh files/87590c24
```


## 5. Conceptual Analogy: "The Matrix Potato"
Imagine Neo standing before thousands of identical-looking potatoes (files).

The Oracle's Note: The Oracle gives Neo a specific "flavor profile" (Hash).

The Scan: Neo grinds all potatoes into "Hash Browns" (Computing the hash).

The Match: Only one Hash Brown matches the Oracle's profile exactly.

The Key: Neo takes that specific potato and inserts it into a machine (The Script), which opens the door to the truth (The Flag).

## 6. Reflection
This challenge emphasizes that in cybersecurity, you cannot trust metadata like filenames. You must trust the underlying data verified through cryptographic hashes. Using grep with pipes is not just a shortcut; it is a fundamental skill for analyzing large-scale datasets or forensic images.

Flag: picoCTF{trust_but_verify_87590c24}
