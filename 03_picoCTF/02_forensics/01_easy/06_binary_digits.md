# picoCTF 2026 - Binary Digits

**Category:** Forensics  
**Difficulty:** Easy  
**Competition:** picoCTF 2026  

---

## Description

> "This file doesn't look like much... just a bunch of 1s and 0s. But maybe it's not just random noise. Can you recover anything meaningful from this?"

---

## Intent

The goal is to recognize that the 0s and 1s in the file are not plain ASCII text, but rather **binary-encoded image data**. All data in a computer is represented in bits (0s and 1s), and grouping them into 8-bit chunks (1 byte) allows us to reconstruct meaningful data — in this case, an image containing the flag.

---

## Solution

### 1. Download and Open the File

Download the file provided in the challenge. Opening it reveals a very long string of 0s and 1s:

```
00010100000000001010001010010100...
```

At first glance it looks like random binary text, but the sheer length and repeating patterns suggest it might encode something more structured.

### 2. CyberChef (Recommended)

Open [CyberChef](https://gchq.github.io/CyberChef/) and apply the following recipe:

| Step | Operation | Settings |
|------|-----------|----------|
| 1 | **From Binary** | Delimiter: `Space`, Byte Length: `8` |
| 2 | **Render Image** | Input Format: `Raw` |

**Result:**  
The output panel renders an image, and the flag is visible as small text within it.

> **Key Insight:** When `From Binary` alone does not produce readable ASCII text, the decoded bytes may represent a **binary file format** such as an image. Adding `Render Image` to the recipe visualizes the result directly.

### 3. Python (Alternative)

The same result can be achieved with a short Python script:

```python
# Read binary string from file
with open('binary_file.txt', 'r') as f:
    binary_data = f.read().replace('\n', '').replace(' ', '')

# Convert every 8 bits into a byte
byte_data = bytes([int(binary_data[i:i+8], 2) for i in range(0, len(binary_data), 8)])

# Save as image file
with open('output.png', 'wb') as f:
    f.write(byte_data)

print("Saved as output.png")
```

Open `output.png` and the flag will be visible in the image.

---

## Flag

```
picoCTF{h1dd3n_1n_th3_b1n4ry_8d00e35f}
```

---

## What I Learned

- Binary data does not always decode to text — it can represent **images, audio, or any other file format**.
- CyberChef's `Render Image` operation is a quick way to visualize raw binary output without saving a file manually.
- When faced with a long stream of 0s and 1s that doesn't decode to readable text, it's worth checking whether the bytes match a known **file signature (magic bytes)** or trying to render them as an image.

---

## Tools Used

- [CyberChef](https://gchq.github.io/CyberChef/) — From Binary + Render Image
- Python 3 (alternative approach)
