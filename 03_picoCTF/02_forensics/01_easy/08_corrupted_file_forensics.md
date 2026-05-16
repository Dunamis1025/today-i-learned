# 08 - Corrupted File (Digital Forensics / File Header Repair)

**Platform:** picoCTF  
**Category:** Forensics  
**Difficulty:** Easy  
**Flag:** `picoCTF{r3st0r1ng_th3_by73s_2326ca93}`

---

## What This Challenge Teaches You

- Every file format has a unique **magic bytes (file signature)** at the very beginning of its binary data
- A file's extension (`.jpg`, `.png`) can be faked — the OS actually reads the internal header to determine the real type
- How to use a **hex editor / hex dump tools** to inspect and repair raw file bytes
- How to use **CyberChef** to render a recovered binary file in-browser when no file download feature is available
- Basic Linux terminal survival skills: killing a stuck process, resetting a terminal

---

## Core Concept: Magic Bytes (File Signatures)

Every file format starts with a specific sequence of bytes that identifies what kind of file it is. These are called **magic bytes** or a **file signature**.

| File Type | Magic Bytes (Hex)             | ASCII Representation |
|-----------|-------------------------------|----------------------|
| JPEG      | `FF D8 FF E0` or `FF D8 FF E1` | `....`               |
| PNG       | `89 50 4E 47 0D 0A 1A 0A`     | `.PNG....`            |
| ZIP       | `50 4B 03 04`                 | `PK..`                |
| PDF       | `25 50 44 46`                 | `%PDF`                |

If these bytes are corrupted or overwritten, the OS and image viewers refuse to open the file — even if all the actual data is perfectly intact.

---

## Challenge Hint Analysis

The challenge provided these hints:
- *"Try checking the file's header."* → The first few bytes of the file are broken
- *"JPEG"* → The file is actually a JPEG image
- *"Tools like `xxd` or `hexdump` can help you inspect and edit file bytes."* → Use CLI hex tools

---

## Step-by-Step Walkthrough

### Step 1 — Download the File

```bash
wget <challenge_file_url>
```

Watch the terminal output carefully for the saved filename. wget may rename the file if there's a conflict:

```
Saving to: 'file.2'
```

In this case, the file was saved as `file.2`, not the expected name. Always check what wget actually names the downloaded file.

---

### Step 2 — Inspect the File Header with `xxd`

```bash
xxd file.2 | head -n 5
```

**What this does:**
- `xxd` converts the binary file into a human-readable hex dump
- `head -n 5` shows only the first 5 lines (the most important part — the header)

**Example output:**
```
00000000: 5c78 ffe0 0010 4a46 4946 0001 0100 0001  \x....JFIF......
```

**Reading the output:**
- Column 1 (`00000000`): byte offset (position in file)
- Column 2 (`5c78 ffe0 ...`): the actual hex values of the bytes
- Column 3 (`\x....JFIF...`): ASCII representation of those bytes

**What's wrong here:**
- A valid JPEG must start with `FF D8 FF E0`
- This file starts with `5C 78 FF E0` — the first 2 bytes (`5C 78`, which is `\x` in ASCII) are wrong
- The rest of the header (`FF E0 ... JFIF`) is intact, confirming this is a JPEG with a corrupted start

---

### Step 3 — Fix the Header with Python

Rather than using an interactive hex editor, you can fix the file with a single Python one-liner:

```bash
python3 -c "data = open('file.2', 'rb').read(); open('fixed_flag.jpg', 'wb').write(b'\xff\xd8' + data[2:])"
```

**Breaking down what this does:**

| Part | Meaning |
|------|---------|
| `open('file.2', 'rb').read()` | Read the whole corrupted file as raw bytes |
| `b'\xff\xd8'` | The correct first 2 bytes for a JPEG |
| `data[2:]` | Everything after the first 2 (broken) bytes — slicing off the bad part |
| `open('fixed_flag.jpg', 'wb').write(...)` | Write the repaired data to a new file |

This replaces only the broken `5C 78` at the start with the correct `FF D8`, leaving everything else untouched.

---

### Step 4 — Verify the Fix

```bash
xxd fixed_flag.jpg | head -n 1
```

**Expected output after repair:**
```
00000000: ffd8 ffe0 0010 4a46 4946 0001 0100 0001  ....JFIF......
```

If the first bytes are now `ff d8 ff e0`, the file header is correctly restored.

---

### Step 5 — Extract the Flag

#### Method A: Search for text strings inside the file

```bash
strings fixed_flag.jpg | grep -iE "flag|pico|cylab|ctf"
```

- `strings` extracts all human-readable text sequences from a binary file
- `grep -iE` searches case-insensitively using a regex pattern

> If this returns nothing, the flag is embedded visually in the image itself (not as hidden text), so you need to actually view the image.

#### Method B: Check metadata with `exiftool`

```bash
exiftool fixed_flag.jpg
```

`exiftool` reads all EXIF/metadata fields from the image (camera model, GPS, comments, artist fields, etc.). CTF authors sometimes hide flags in these fields. Check every field in the output.

#### Method C: Scan for embedded files with `binwalk`

```bash
binwalk fixed_flag.jpg
```

`binwalk` scans a file for embedded other files or known signatures. Useful when the image might have a ZIP or another file hidden inside.

---

### Step 6 — View the Image via CyberChef (When No Download Is Available)

In a restricted webshell with no file download option, you can render the image inside the browser using CyberChef.

**Step 6a — Encode the fixed file to Base64:**

```bash
base64 -w 0 fixed_flag.jpg
```

- `-w 0` disables line wrapping, outputting the entire file as one long string (crucial for clean copy-paste)
- Without `-w 0`, the output is split into 76-char lines which can still be decoded, but is harder to copy fully

**Step 6b — Save to a file to avoid copy issues:**

```bash
cat fixed_flag.jpg | base64 > b64.txt
cat b64.txt
```

Saving to a file first prevents accidentally copying extra terminal output (command prompts, error messages, etc.) along with the data.

**Step 6c — Render in CyberChef:**

1. Open the **CyberChef** tab in the webshell interface
2. Paste the Base64 string into the **Input** box
3. In the **Recipe** panel, add these operations in order:
   - `From Base64`
   - `Render Image`
4. The image appears in the **Output** panel — the flag is written on it

---

## Terminal Survival Skills

### Kill a stuck/running process

```bash
Ctrl + C    # Send interrupt signal — stops most running programs
Ctrl + Z    # Force-suspend the process and return terminal control to you
```

### Reset a garbled terminal

If text input looks broken after killing a process:

```bash
reset
```

This fully reinitializes the terminal display without losing your files or session.

### Start a temporary HTTP server to download files

```bash
python3 -m http.server 8080
```

This serves files in the current directory over HTTP on port 8080. Access from your browser at `http://<server-ip>:8080/fixed_flag.jpg`. Not always available in CTF environments (ports may be blocked), but worth trying.

---

## Commands Used — Quick Reference

| Command | Purpose |
|---------|---------|
| `wget <url>` | Download a file from a URL |
| `xxd <file> \| head -n 5` | View the first 5 lines of a file's hex dump |
| `python3 -c "..."` | Run a Python one-liner to patch file bytes |
| `strings <file> \| grep -iE "flag\|ctf"` | Search for flag-like text inside a binary |
| `exiftool <file>` | Read all metadata/EXIF fields from an image |
| `binwalk <file>` | Detect embedded files or hidden data |
| `base64 -w 0 <file>` | Encode a file to Base64 (no line wrapping) |
| `cat <file> \| base64 > out.txt` | Save Base64 output cleanly to a file |
| `reset` | Fix a broken/garbled terminal display |
| `Ctrl + C` | Kill the current running process |
| `Ctrl + Z` | Force-suspend a process and regain terminal |

---

## Key Takeaways

1. **File extensions lie.** Always check the actual magic bytes, not just the `.jpg` or `.png` suffix.
2. **Most JPEG corruptions in CTF are header-only.** The data underneath is almost always intact — you just need to fix the first few bytes.
3. **Python is your best friend for byte-level surgery.** `open(file, 'rb')` / `open(file, 'wb')` + slicing is clean and precise.
4. **`strings` is fast but limited.** If the flag is drawn into the image (not stored as text), you need to actually view it.
5. **CyberChef's `Render Image` operation** is a lifesaver in restricted environments where you can't download files directly.
6. **`-w 0` matters with `base64`.** Without it, copy-paste errors are common with large files.
