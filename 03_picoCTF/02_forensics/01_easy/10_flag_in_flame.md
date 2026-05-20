# picoCTF – Flag in Flame (Forensics, Easy, 100pts)

## Challenge Description

The SOC team discovered a suspiciously large log file after a recent breach. Instead of normal logs, it contained an enormous block of encoded text. The goal was to inspect the file and reveal its true purpose.

**Hint:** Use base64 to decode the data and generate the image file.

---

## What I Tried

### Step 1 – Download the file
```bash
wget <challenge_url>/logs.txt
```
Downloaded successfully. File size: ~1.5MB.

---

### Step 2 – Decode base64 to image
```bash
base64 -d logs.txt > output.png
file output.png
```
**Result:** `output.png: PNG image data, 896 x 1152, 8-bit/color RGB, non-interlaced`

Successfully decoded. The log file was a base64-encoded PNG image in disguise.

---

### Step 3 – Search for flag as plaintext
```bash
strings output.png | grep "picoCTF"
strings output.png | grep "CTF"
strings output.png | grep "flag"
strings output.png | grep "{"
```
**Result:** No flag found. The flag is likely embedded visually in the image pixels, not as raw text.

---

### Step 4 – Check metadata
```bash
exiftool output.png
exiftool output.png | grep -i "flag\|pico\|CTF"
```
**Result:** No flag in metadata. Just standard PNG info (dimensions, color type, etc.).

---

### Step 5 – Steganography analysis
```bash
zsteg output.png
```
**Result:** No obvious flag. Some random-looking strings appeared but none matched `picoCTF{...}`.

---

### Step 6 – Hex analysis
```bash
xxd output.png | tail -n 50
```
**Result:** No readable flag string near the end of the file. Data ends with a standard PNG `IEND` marker.

---

### Step 7 – Python regex extraction attempts
```bash
python3 -c "import re; data = open('output.png', 'rb').read(); match = re.search(b'picoCTF{[^}]+}', data); print(match.group(0).decode() if match else 'Not found')"
```
**Result:** Not found. Flag is not stored as a raw ASCII/binary string inside the file.

---

### Step 8 – Viewing the image (the real blocker)

The flag appears to be **visually drawn on the image itself**, meaning it must be seen with the naked eye. However, the environment was a browser-based webshell (picoCTF) with no file download button, which made this extremely difficult.

Attempts to view the image:

| Method | Result |
|---|---|
| `python3 -m http.server 8000` | Port blocked / webshell domain not accessible |
| CyberChef `From Base64` → `Render Image` | "Invalid file type" error |
| `base64 output.png` → paste into browser address bar as `data:image/png;base64,...` | Too large, browser rejected it |
| `pip install climage` → render in terminal | Image rendered but too low resolution to read the flag |
| CyberChef download button | Downloaded file was corrupted / unreadable |

---

## Key Takeaways

- **Base64 encoding** can disguise binary files (images, executables) as plain text. Decoding with `base64 -d` restores the original file.
- **`file` command** identifies a file's true type regardless of its extension.
- **`strings` + `grep`** is a quick first pass to find plaintext flags hidden in binary files.
- **`exiftool`** reads file metadata — sometimes flags are hidden there.
- **`zsteg`** detects steganography (data hidden in image pixel bits).
- **`xxd`** dumps raw hex — useful for spotting hidden strings near the end of a file.
- **`python3 -m http.server 8000`** can serve files from a webshell, but only if the port is accessible from outside.
- **CyberChef** is powerful for browser-based encoding/decoding, but `Render Image` requires raw binary input (pipe `From Base64` first, then `Render Image`).
- When a flag is **drawn into image pixels**, all text-based extraction methods will fail — you simply have to view the image.

---

## Conclusion

The flag is visually embedded in the decoded PNG image. All text-based forensics approaches were exhausted without success. The challenge was ultimately blocked by the inability to view the image file in a restricted webshell environment with no download functionality.

**Unsolved** — but the process covered core forensics skills: file type identification, base64 decoding, metadata analysis, steganography detection, and hex inspection.

---

*Tools used: `wget`, `base64`, `file`, `strings`, `grep`, `exiftool`, `zsteg`, `xxd`, `python3`, `CyberChef`*
