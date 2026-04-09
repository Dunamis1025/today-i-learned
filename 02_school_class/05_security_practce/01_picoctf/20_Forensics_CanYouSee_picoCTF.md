# [picoCTF] CanYouSee - Write-up

## 1. Challenge Description
- **Category**: Forensics
- **Objective**: Find a hidden flag within a provided image file.
- **Key Hint**: Information about the picture (Metadata) and non-standard data formats.

## 2. Tools Used
- `wget`: To download the challenge file.
- `unzip`: To extract the compressed image.
- `exiftool`: To analyze the metadata of the image.
- `base64`: To decode the discovered string.

## 3. Step-by-Step Solution

### Step 1: Download and Extract
Initially, a ZIP file named `unknown.zip` was provided.
```bash
wget [Challenge_URL]
$ unzip unknown.zip
```
Inside the archive, an image file named ukn_reality.jpg was found.

### Step 2: Metadata Analysis
Using exiftool, I inspected the metadata of the image to find hidden strings.

```bash
$ exiftool ukn_reality.jpg
```
In the Attribution URL field, a suspicious Base64 encoded string was identified:
cGlqbm0NURntNRTc0RDQ3QV9ISUREM05FNGRhYmRkY2J9Cg==

### Step 3: Decoding the Flag
The string was decoded using the base64 utility.
```bash
$ echo "cGlqbm0NURntNRTc0RDQ3QV9ISUREM05FNGRhYmRkY2J9Cg==" | base64 -d
```
## 4. Final Flag
picoCTF{ME74D47A_HIDD3N_4dabddcb}

## 5. Lessons Learned
Always check the metadata (EXIF data) of media files in forensics challenges.

Look for fields that contain non-standard or unusually long strings.

Practice identifying Base64 encoding by its character set and padding (=).
