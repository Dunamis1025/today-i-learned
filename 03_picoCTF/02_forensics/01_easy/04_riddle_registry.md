# 03. Riddle Registry — PDF Metadata Forensics

## Challenge Info

| Field      | Details                        |
|------------|-------------------------------|
| Platform   | picoCTF / picoGym             |
| Category   | Forensics                     |
| Difficulty | Easy                          |
| Tags       | `picoMini by CMU-Africa`, `browser_webshell_solvable` |
| Solves     | 40,182                        |
| Liked      | 95%                           |

---

## Description

> "Hi, intrepid investigator! You've stumbled upon a peculiar PDF filled with what seems like nothing more than garbled nonsense. But beware! Not everything is as it appears. Amidst the chaos lies a hidden treasure — an elusive flag waiting to be uncovered. Find the PDF file here and uncover the flag within the metadata."

---

## Hints

- **Hint 1:** Don't be fooled by the visible text; it's just a decoy!
- **Hint 2:** Look beyond the surface for hidden clues.

---

## Key Concepts

### What is Metadata?
Metadata is hidden information stored inside a file that is **not visible** when you simply open and read the file. For PDF files, metadata can include fields such as:
- `Author`
- `Title`
- `Producer`
- `Creation Date`
- `Keywords`

### What is Base64?
Base64 is a common encoding scheme that converts binary or text data into a string of ASCII characters. It is widely used to embed data in formats that only support plain text.

**How to recognize Base64:**
- Contains letters (A–Z, a–z), numbers (0–9), `+`, `/`
- Often ends with one or two `=` signs (padding)
- Example: `cGljb0NURns...MH0=`

---

## Tools Used

| Tool       | Purpose                            |
|------------|------------------------------------|
| `wget`     | Download the PDF file              |
| `exiftool` | Extract metadata from the PDF      |
| `base64`   | Decode the Base64-encoded flag     |

---

## Solution — Step by Step

### Step 1: Download the PDF

```bash
wget https://challenge-files.picoctf.net/.../confidential.pdf
```

### Step 2: Extract Metadata with exiftool

```bash
exiftool confidential.pdf
```

**Output (key fields):**

```
File Name        : confidential.pdf
File Size        : 178 KiB
PDF Version      : 1.7
Producer         : PyPDF2
Author           : cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9lZTQ1NDk1MH0=
```

> 💡 The `Author` field looks suspicious — it ends with `=`, which is a classic Base64 padding indicator.

### Step 3: Decode the Base64 String

```bash
echo "cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9lZTQ1NDk1MH0=" | base64 -d
```

**Output:**

```
picoCTF{puzzl3d_m3tadata_f0und!_ee454950}
```

---

## Flag

```
picoCTF{puzzl3d_m3tadata_f0und!_ee454950}
```

---

## Lessons Learned

1. **Visible content can be a decoy.** Always look beyond what is displayed on screen.
2. **Metadata holds hidden information.** Tools like `exiftool` can reveal data that is invisible to the naked eye.
3. **Recognize Base64 encoding.** The trailing `=` sign and alphanumeric character set are key indicators.
4. **Simple Linux commands are powerful.** `wget`, `exiftool`, and `base64` together solved this challenge in just three steps.

---

## Commands Summary

```bash
# 1. Download the file
wget <pdf_url>

# 2. Read metadata
exiftool confidential.pdf

# 3. Decode Base64 from Author field
echo "<base64_string>" | base64 -d
```
