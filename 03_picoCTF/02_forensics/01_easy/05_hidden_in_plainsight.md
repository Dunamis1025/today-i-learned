# picoCTF - Hidden in Plainsight Writeup

**Category:** Forensics  
**Difficulty:** Easy  
**Author:** YAHAYA MEDDY  
**Flag:** `picoCTF{h1dd3n_1n_1m4g3_e7f5b969}`

---

## Challenge Description

> You're given a seemingly ordinary JPG image. Something is tucked away out of sight inside the file. Your task is to discover the hidden payload and extract the flag.

**Hint:** Download the jpg image and read its metadata.

**Tags:** `Easy` `Forensics` `picoMini by CMU-Africa` `browser_webshell_solvable`

---

## Concepts Learned

- **Steganography** — the practice of hiding secret data inside an ordinary, non-secret file (in this case, a JPG image)
- **Base64 encoding** — a method of encoding binary data as ASCII text
- **EXIF/Metadata** — data embedded inside image files that can carry hidden information
- **Steghide** — a steganography tool that hides data inside JPEG/WAV/AU files using a passphrase

---

## Solution

### Method 1: Using the picoCTF Webshell (Command Line)

If the browser webshell is available on picoCTF, you can solve this entirely in the terminal.

#### Step 1: Download the image

```bash
wget <image_url> -O img.jpg
```

#### Step 2: Extract strings from the image

Use the `strings` command to pull all readable text from the binary file:

```bash
strings img.jpg
```

Or filter directly for the Base64 string near the top of the output:

```bash
strings img.jpg | head -20
```

You will find the following string near the top:

```
c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9
```

#### Step 3: Decode the Base64 string (first layer)

```bash
echo "c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9" | base64 -d
```

Output:

```
steghide:cEF6endvcmQ=
```

This tells us:
- The tool used is **steghide**
- The passphrase is **Base64 encoded** as `cEF6endvcmQ=`

#### Step 4: Decode the passphrase (second layer)

```bash
echo "cEF6endvcmQ=" | base64 -d
```

Output:

```
pAzzword
```

#### Step 5: Extract the hidden data using steghide

```bash
steghide extract -sf img.jpg -p pAzzword
```

This will extract a hidden file (e.g. `flag.txt`). Read it:

```bash
cat flag.txt
```

Output:

```
picoCTF{h1dd3n_1n_1m4g3_e7f5b969}
```

---

### Method 2: Using Online Tools (No Installation Required)

This method is useful when the webshell is unavailable or you prefer browser-based tools.

#### Step 1: Extract strings using CyberChef

1. Go to [https://cyberchef.org](https://cyberchef.org)
2. Drag and drop the `img.jpg` file into the **Input** window
3. In the Operations search bar, type `Strings` and drag it into the **Recipe**
4. Set:
   - Encoding: `Single byte`
   - Minimum length: `4`
   - Match: `Alphanumeric + punctuation`
5. Click **BAKE!**
6. In the Output, find the following string near the top:

```
c3RlZ2hpZGU6Y0VGNmVuZHZjbVE5
```

#### Step 2: Decode Base64 (first layer) in CyberChef

1. Clear the Input field and paste only:
   ```
   c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9
   ```
2. Replace the `Strings` recipe with **From Base64**
3. Click **BAKE!**

Output:

```
steghide:cEF6endvcmQ=
```

#### Step 3: Decode Base64 (second layer) in CyberChef

1. Replace the Input with:
   ```
   cEF6endvcmQ=
   ```
2. Keep the **From Base64** recipe
3. Click **BAKE!**

Output:

```
pAzzword
```

This is the steghide passphrase.

#### Step 4: Extract hidden data using the online Steganographic Decoder

1. Go to [https://futureboy.us/stegano/decinput.html](https://futureboy.us/stegano/decinput.html)
2. Under **Select a JPEG, WAV, or AU file to decode**, upload `img.jpg`
3. In the **Password** field, enter:
   ```
   pAzzword
   ```
4. Select **View raw output as MIME-type: text/plain**
5. Click **Submit**

Result:

```
picoCTF{h1dd3n_1n_1m4g3_e7f5b969}
```

---

## Summary

| Step | Action | Tool Used | Result |
|------|--------|-----------|--------|
| 1 | Extract readable strings from image | `strings` / CyberChef Strings | Found Base64 string |
| 2 | Decode Base64 (layer 1) | `base64 -d` / CyberChef From Base64 | `steghide:cEF6endvcmQ=` |
| 3 | Decode Base64 (layer 2) | `base64 -d` / CyberChef From Base64 | `pAzzword` (passphrase) |
| 4 | Extract steghide payload | `steghide extract` / futureboy.us | `picoCTF{h1dd3n_1n_1m4g3_e7f5b969}` |

---

## Key Takeaways

- Always check image metadata and embedded strings — flags are often hidden in plain sight
- Base64 strings are recognizable by their alphanumeric characters and `=` padding at the end
- Steganography tools like **steghide** can embed secret files inside images, protected by a passphrase
- CyberChef is an extremely powerful browser-based tool for CTF challenges — bookmark it!
- The `strings` command is one of the first tools to reach for in any forensics challenge
