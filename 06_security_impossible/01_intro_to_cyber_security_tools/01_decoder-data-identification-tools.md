# 🔍 Decoder & Data Identification Tools — Study Notes

> **Course**: Security Impossible  
> **Topic**: Introduction to Decoder & Data Identification Tools  
> **Duration**: ~50 min  
> **Goal**: Learn how to recognize, identify, and decode disguised or encoded data using standard cybersecurity tools.

---

## 📌 Table of Contents

1. [Why This Matters](#1-why-this-matters)
2. [Key Concepts: Encoding vs Encryption vs Hashing](#2-key-concepts-encoding-vs-encryption-vs-hashing)
3. [Common Encoding Formats](#3-common-encoding-formats)
4. [Other Data Formats](#4-other-data-formats)
5. [Tool: CyberChef](#5-tool-cyberchef)
6. [Tool: Linux CLI Commands](#6-tool-linux-cli-commands)
7. [Decoding Workflow](#7-decoding-workflow)
8. [Layered Encoding](#8-layered-encoding)
9. [Safety Reminders](#9-safety-reminders)

---

## 1. Why This Matters

In cybersecurity, data is often **disguised or transformed** to avoid detection by security systems. Attackers encode malicious payloads so they appear as harmless noise. Security analysts must be able to:

- Recognize patterns in data that suggest it has been encoded
- Reverse the encoding to reveal the original content
- Determine whether the decoded content is benign or malicious

> **Analogy**: Think of encoded data like a package in a shipping box. The box hides what's inside — but if you know how to open it, you can see the real contents.

---

## 2. Key Concepts: Encoding vs Encryption vs Hashing

| Concept | Reversible? | Key Required? | Purpose | Example |
|---|---|---|---|---|
| **Encoding** | ✅ Yes | ❌ No | Data transport / formatting | Base64, Hex, URL |
| **Encryption** | ✅ Yes | ✅ Yes | Keeping data secret | AES, RSA |
| **Hashing** | ❌ No | ❌ No | Integrity verification / fingerprinting | MD5, SHA-256 |

### Encoding
- Transforms data into another format for **easier storage or transmission**
- No secret key needed — anyone who knows the format can reverse it
- Not designed for secrecy; designed for compatibility

### Encryption
- Scrambles data so it **cannot be read without a key**
- Even if intercepted, the content remains protected
- Requires a secret key to decrypt

### Hashing
- Produces a **fixed-length fingerprint** of the input data
- **One-way only** — the original data cannot be recovered
- Even a tiny change in input produces a completely different hash
- Used to verify data integrity (e.g., checking if a file has been tampered with)

---

## 3. Common Encoding Formats

### 3.1 Base64

- Converts binary data into **ASCII text** using 64 characters
- Character set: `A–Z`, `a–z`, `0–9`, `+`, `/`
- Often ends with `=` or `==` (padding characters)
- Widely used for email attachments, JWTs, and embedding data in URLs

**Example:**
```
Encoded:  SGVsbG8=
Decoded:  Hello
```

**How to spot it:**
- Looks like a long random string of letters and numbers
- Ends with `=` or `==`
- Only contains characters from `A–Z a–z 0–9 + /`

---

### 3.2 Hex (Hexadecimal)

- Represents binary data using **base-16 values** (`0–9` and `A–F`)
- Each byte (8 bits) is represented by **2 hex characters**
- Often used in low-level data inspection, memory dumps, and file headers

**Example:**
```
Encoded:  48656c6c6f
Decoded:  Hello
```

**How to spot it:**
- Long string of only `0–9` and `A–F` characters
- Usually grouped in pairs
- No special punctuation or padding

---

### 3.3 URL Encoding (Percent Encoding)

- Encodes **special characters** in URLs so they don't break web requests
- Replaces special characters with `%` followed by two hex digits

**Common examples:**
```
%20  →  (space)
%3A  →  :  (colon)
%2F  →  /  (forward slash)
%40  →  @  (at sign)
```

**How to spot it:**
- Contains `%` followed by two characters (`0–9`, `A–F`)
- Looks like parts of a URL or web request
- Commonly seen in HTTP logs and web traffic analysis

---

### 3.4 Binary

- The most fundamental computer language — data represented as `0`s and `1`s
- Typically grouped in sets of 8 bits (1 byte)
- Rarely seen directly, but underlies all other formats

**Example:**
```
01001000 01100101 01101100 01101100 01101111
→ Hello
```

---

## 4. Other Data Formats

### 4.1 JWT (JSON Web Token)

- A token format used for **user authentication and data exchange** in web services
- Consists of three parts separated by `.`:
  - **Header** — algorithm and token type (Base64 encoded)
  - **Payload** — claims / user data (Base64 encoded)
  - **Signature** — verifies the token hasn't been tampered with

**Structure:**
```
xxxxx.yyyyy.zzzzz
(header).(payload).(signature)
```

> The header and payload are Base64 encoded, so they can be decoded — but the signature cannot be forged without the secret key.

---

### 4.2 Hash Values

- Fixed-length output produced from input data
- **Cannot be reversed** — used only for verification
- Common algorithms: MD5, SHA-1, SHA-256

**Example (MD5):**
```
Input:   Hello
Output:  8b1a9953c4611296a827abf8c47804d7
```

> If a file's hash matches the expected value, the file has not been modified.

---

## 5. Tool: CyberChef

**URL**: [https://gchq.github.io/CyberChef/](https://gchq.github.io/CyberChef/)

CyberChef is a browser-based, drag-and-drop data analysis tool — no installation required.

### Interface Overview

| Panel | Description |
|---|---|
| **Operations** (left) | Library of all available transformations |
| **Recipe** (center) | The sequence of operations you want to apply |
| **Input** (top right) | Paste your encoded data here |
| **Output** (bottom right) | The decoded result appears here |

### Step-by-Step Usage

1. Open CyberChef in your browser
2. Paste the encoded/suspicious string into the **Input** panel
3. Search for **"Magic"** in the Operations panel
4. Drag "Magic" into the **Recipe** panel (or double-click it)
5. Check the **Output** panel for the decoded result
6. If the output still looks encoded, repeat the process

### Manual Decoding Operations

If "Magic" doesn't work, try these manually:

| Operation | When to use |
|---|---|
| `From Base64` | String ends in `=`, uses A–Z a–z 0–9 |
| `From Hex` | String uses only `0–9` and `A–F` |
| `URL Decode` | String contains `%` followed by hex digits |

> **Rule of thumb**: Always try "Magic" first. Only switch to manual if needed.

---

## 6. Tool: Linux CLI Commands

When CyberChef is unavailable, or when working with full files and large datasets, use these terminal commands.

### `base64 -d` — Decode Base64 Data

```bash
echo "SGVsbG8=" | base64 -d
# Output: Hello

base64 -d encoded_file.txt
```

Use when: You have a Base64 encoded string or file to decode.

---

### `file` — Identify File Type

```bash
file mystery_file
# Output: mystery_file: PNG image data, 800 x 600, 8-bit/color RGB
```

Use when: You don't know what type of file you're dealing with. Reads internal "magic bytes" — not just the file extension.

---

### `strings` — Extract Readable Text from Binary Files

```bash
strings binary_file.exe
strings binary_file.exe | grep "flag"
```

Use when: A file is binary/unreadable and you want to pull out any human-readable text hidden inside (e.g., URLs, flags, credentials, error messages).

---

### `xxd` — Hex Dump a File

```bash
xxd file.bin
xxd file.bin | head -20    # show first 20 lines only
```

Use when: You need to inspect the raw byte-level structure of a file. Useful for identifying file headers and spotting patterns.

---

### Why Use CLI Over CyberChef?

| Situation | Preferred Tool |
|---|---|
| Quick single string | CyberChef |
| Processing full files | CLI |
| No browser available | CLI |
| Large datasets (speed matters) | CLI |
| Automated / scripted analysis | CLI |

---

## 7. Decoding Workflow

Use this process whenever you encounter suspicious or unreadable data:

```
1. OBSERVE
   └─ Look for patterns: ends in =? contains %? only hex chars?

2. IDENTIFY
   └─ Guess the encoding format based on visual patterns

3. AUTO-DECODE (CyberChef)
   └─ Try "Magic" first

4. MANUAL DECODE
   └─ If Magic fails → try From Base64, From Hex, URL Decode

5. CHECK OUTPUT
   └─ Is it human-readable? Does it make sense?

6. REPEAT IF NEEDED
   └─ If output is still encoded → go back to step 1 with the new output
```

---

## 8. Layered Encoding

Data can be encoded **multiple times** — like an onion with many layers, or boxes nested inside boxes.

**Example:**
```
Original:  Hello
→ Base64:  SGVsbG8=
→ Hex:     5347567362473873
→ URL:     5347567362473873  (or further encoded)
```

**How to handle it:**
- Decode once, then inspect the output
- If the output is still unreadable, treat it as a new encoded string and decode again
- Keep repeating until you reach plaintext

> Don't stop just because you decoded it once. Always verify the output is actually readable.

---

## 9. Safety Reminders

| ⚠️ Rule | Why It Matters |
|---|---|
| Never paste real credentials or personal data into online tools | CyberChef is public — sensitive data could be exposed |
| Always verify decoded output manually | Automated tools can misidentify encoding formats |
| Be careful with decoded payloads | The decoded content might be malware — handle in a safe environment |
| Remember: hashes cannot be decoded | Don't waste time trying to "reverse" a hash — it's a one-way function |
| Use isolated environments for suspicious files | Executing decoded malware on your main machine is dangerous |

---

## 📚 Quick Reference Card

### Identify by Pattern

| Pattern | Likely Encoding |
|---|---|
| Ends with `=` or `==` | Base64 |
| Only `0–9` and `A–F` chars | Hex |
| Contains `%XX` sequences | URL Encoding |
| Three parts separated by `.` | JWT |
| Fixed-length alphanumeric string | Hash (MD5 / SHA) |
| Only `0`s and `1`s | Binary |

### Decode with CyberChef

```
Input → Magic → Output
         ↓ (if fails)
    From Base64 / From Hex / URL Decode
         ↓ (if still encoded)
         Repeat
```

### Decode with CLI

```bash
# Base64
echo "SGVsbG8=" | base64 -d

# Identify file type
file unknown_file

# Extract readable strings
strings binary_file

# Hex dump
xxd file.bin
```

---

*Study notes based on Security Impossible lab: Introduction to Decoder & Data Identification Tools*
