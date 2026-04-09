# 18. Scan Surprise - QR Code Forensics

## 📌 Challenge Overview
- **Challenge Name:** Scan Surprise
- **Category:** Forensics (picoCTF 2024)
- **Objective:** Extract the hidden flag from a QR code provided in a zip archive.

## 🛠 Tools & Commands Used
- `wget`: To download the challenge file from the server.
- `unzip`: To extract the contents of the zip file.
- `ls -F`: To list files with symbols indicating their file types.
- `zbarimg`: A command-line tool to scan and decode QR codes from image files.

## 🚀 Step-by-Step Solution

### 1. File Acquisition
First, I downloaded the challenge file using `wget`:
```
wget <challenge_url>
```

### 2. Exploring the Directory with ls -F
After downloading, I used the -F flag to identify the file types clearly:
```
ls -F
```
What is ls -F? It appends a character to each file name to indicate its type:

/ for directories

* for executable files

@ for symbolic links

No symbol for regular files (like our .png or .txt)

### 3. Extracting and Locating the Image
Initially, I tried to scan the .zip file directly, which failed because the QR code was inside the archive. I extracted the files:
```
unzip challenge.zip
```
This provided a file named flag.png (or a similar path like drop-in/flag.png).

### 4. Decoding the QR Code
Using zbar-tools, I decoded the image file to retrieve the text:
```
zbarimg flag.png
```
The tool scanned the image and output the flag hidden within the QR data.

🚩 Key Findings
Flag: picoCTF{p33k_@_b00_b5ce2572}

Takeaway: Even if data is visually encoded (like a QR code), command-line tools like zbarimg can quickly automate the extraction process within a Linux environment.

📖 Vocabulary & Concepts
QR Code: A type of matrix barcode that can store various data, including text and URLs.

Native Scanner: Most modern mobile OS (Android 8+, iOS 11+) have built-in QR recognition in the camera app.

Zbarimg: A powerful CLI utility that supports various barcode formats including QR codes.

