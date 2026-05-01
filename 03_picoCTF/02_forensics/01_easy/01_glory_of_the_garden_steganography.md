# Glory of the Garden - picoCTF 2019

**Category:** Forensics  
**Difficulty:** Easy  
**Tags:** Steganography, strings, file analysis

---

## Challenge Description

> "This file contains more than it seems. Get the flag from [garden.jpg](garden.jpg)."

**Hint:** What is a hex editor?

---

## Concept: What is Steganography?

Steganography is the practice of **hiding data inside other files**.  
Unlike encryption (which scrambles data), steganography **conceals the existence** of the data itself.

In this challenge, a text string (the flag) was appended to the **end of a JPG image file**.

---

## How JPG Files Work

A JPG file follows a specific structure:

```
[JPG Header: FF D8] ... [Image Data] ... [JPG End Marker: FF D9] [Hidden Data]
```

- `FF D8` = Start of JPG file
- `FF D9` = End of JPG file (EOI - End of Image marker)
- Any data **after** `FF D9` is **ignored by image viewers**
- But the data still exists inside the file!

This means you can append any text after `FF D9` and the image will display normally,  
while the hidden data remains invisible to anyone just opening the file.

---

## Tools Used

| Tool | Purpose |
|------|---------|
| `wget` | Download file from URL |
| `strings` | Extract all readable text from a binary file |
| `grep` | Filter output to find specific patterns |

---

## Solution

### Step 1: Download the file

```bash
wget https://challenge-files.picoctf.net/.../garden.jpg
```

### Step 2: Extract hidden text

```bash
strings garden.jpg | grep picoCTF
```

**Output:**
```
Here is a flag: picoCTF{more_than_m33ts_the_3y3a63b5b27}
```

### Why this works

- `strings` scans the **entire file** from start to finish and extracts any sequence of readable ASCII characters (default: 4+ characters long)
- It does not care about file format — it reads raw bytes
- `grep picoCTF` filters the output to only show lines containing "picoCTF"
- The flag was sitting right after the `FF D9` end marker, invisible to image viewers but fully readable to `strings`

---

## Real-World Applications

### 🔍 Digital Forensics
- Investigators use `strings` on suspicious files to find hidden messages, malware commands, or leaked credentials
- This exact technique is used in **incident response** when analyzing files found on compromised systems

### 🦠 Malware Analysis
- Attackers often hide malicious code or C2 (Command & Control) server addresses inside image files
- Security analysts run `strings` as a **first-pass analysis** on unknown files

### 📋 GRC / Compliance
- Data exfiltration investigations check whether sensitive data has been embedded into files being transferred out of a network
- Understanding steganography helps when defining **data loss prevention (DLP)** policies

---

## Key Takeaways

1. Files are just sequences of bytes — file extensions don't define what data can be inside
2. Image viewers only read up to the end-of-file marker and ignore everything after
3. `strings` is one of the most fundamental and useful tools in forensic analysis
4. Always examine files beyond what they "look like" — appearances can be deceiving

---

## Flag

```
picoCTF{more_than_m33ts_the_3y3a63b5b27}
```
