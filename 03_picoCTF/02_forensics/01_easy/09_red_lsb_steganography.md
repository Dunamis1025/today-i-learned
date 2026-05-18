# 09. RED — LSB Steganography (picoCTF, Forensics / Easy)

## Challenge Overview

| Field      | Detail                          |
|------------|---------------------------------|
| Name       | RED                             |
| Category   | Forensics                       |
| Difficulty | Easy                            |
| Points     | 100                             |
| Solves     | 27,622                          |
| Author     | Shuailin Pan (LeConjuror)       |
| Flag       | `picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}` |

---

## Problem Description

> RED, RED, RED, RED  
> Download the image: `red.png`

**Hints provided:**
1. The picture seems pure, but is it though?
2. Red?Ged?Bed?Aed?
3. Check whatever Facebook is called now. *(→ Meta → Metadata)*

---

## What I Learned

This challenge teaches three core forensics concepts:

1. **Image Metadata Analysis** — hidden information embedded in file headers
2. **LSB (Least Significant Bit) Steganography** — hiding data in pixel color values
3. **Base64 Decoding** — a common encoding scheme used to obscure text data

---

## Concept: How Images Store Color

Every image is made up of **pixels**. Each pixel has three color channels:

| Channel | Meaning | Value Range |
|---------|---------|-------------|
| R       | Red     | 0 – 255     |
| G       | Green   | 0 – 255     |
| B       | Blue    | 0 – 255     |

Each value is stored as an **8-bit binary number**:

```
255 (decimal) = 1111 1111 (binary)
254 (decimal) = 1111 1110 (binary)
```

---

## Concept: LSB Steganography

**LSB = Least Significant Bit** — the last (rightmost) bit of a binary number.

```
1111 111[1]  ← This is the LSB
         ↑
    Changing only this bit: 255 → 254
    Human eyes cannot detect this difference in color!
```

### How data is hidden:

Secret data is converted to binary, then each bit is inserted into the LSB of each pixel's color channel — one bit per channel, spread across thousands of pixels.

```
Original pixels (R values):
  11111111  10101010  11001100  ...

After hiding secret bits (1, 0, 1):
  1111111[1]  1010101[0]  1100110[1]  ...
                                       ↑
                           Hidden bits: 1, 0, 1 → part of the secret message
```

Because only the last bit changes, **the image looks identical to the naked eye**, making this technique nearly undetectable without tools.

---

## Tools Used

### 1. `exiftool` — Metadata Extractor

Reads hidden metadata stored in the file header (EXIF data).

```bash
exiftool red.png
```

**Key output found:**
```
Poem : Crimson heart, vibrant and bold,
       Hearts flutter at your sight.
       Evenings glow softly red, ...
Color Type : RGB with Alpha
Image Size : 128x128
```

→ A poem was hidden inside the metadata field. This was a red herring (distraction), but it confirmed something was deliberately hidden in this file.

---

### 2. `strings` — String Extractor

Extracts all readable ASCII text from a binary file.

```bash
strings red.png
```

**Key output found:**
```
tEXtPoem
Crimson heart, vibrant and bold,
...
IDATx
IEND
```

→ Confirmed the poem was embedded as a PNG text chunk (`tEXt`). No flag here directly, but useful for understanding file structure.

---

### 3. `zsteg` — LSB Steganography Analyzer

Analyzes PNG and BMP files for hidden data across different bit planes and color channels.

```bash
zsteg red.png
```

**Key output found:**
```
b1,rgba,lsb,xy  .. text: "cGljb0NURntyM2RfMXNf..."
```

→ `b1` means **bit 1 (LSB)**, `rgba` means all color channels including Alpha, `lsb` means Least Significant Bit, `xy` means pixel traversal order (left→right, top→bottom).

A long **Base64-encoded string** was discovered hidden in the LSB of the RGBA channels.

---

### 4. `base64` — Decoder

Decodes a Base64-encoded string back into readable text.

```bash
echo "cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==" | base64 -d
```

**Output:**
```
picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}
```

---

## Solution Walkthrough

```bash
# Step 1: Download the file
wget <challenge_url>/red.png

# Step 2: Check metadata
exiftool red.png

# Step 3: Extract readable strings
strings red.png

# Step 4: Analyze LSB steganography
zsteg red.png

# Step 5: Decode the Base64 string found by zsteg
echo "cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==" | base64 -d
```

---

## Why the Hints Made Sense (in Hindsight)

| Hint | What it meant |
|------|---------------|
| "The picture seems pure, but is it though?" | The image looks like a plain red square, but data is hidden inside |
| "Red?Ged?Bed?Aed?" | Focus on the **R**ed channel — the flag was hidden in the Red (and other) LSB channels |
| "Check whatever Facebook is called now" | **Meta** → check the **Meta**data using `exiftool` |

---

## Key Takeaways

- Images can hide data **invisibly** using LSB steganography — changing the last bit of a color value creates no perceptible visual difference.
- Always check **metadata** with `exiftool` when analyzing suspicious files.
- `zsteg` is the go-to tool for automated LSB analysis on PNG files.
- Hidden data is often **encoded** (e.g., Base64) rather than stored in plain text — always try decoding suspicious strings.
- File size can be a clue: `red.png` was only **796 bytes** for a 128×128 image — suspiciously small, suggesting minimal actual image complexity.

---

## References

- [zsteg GitHub](https://github.com/zed-0xff/zsteg)
- [ExifTool Official Site](https://exiftool.org/)
- [Base64 Encoding Explained](https://en.wikipedia.org/wiki/Base64)
- [LSB Steganography — Wikipedia](https://en.wikipedia.org/wiki/Steganography)
- [picoCTF](https://picoctf.org/)
