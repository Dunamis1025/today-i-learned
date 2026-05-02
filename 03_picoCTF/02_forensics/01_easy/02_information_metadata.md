# picoCTF - information (Forensics / Easy)

## Challenge Summary
- **Category:** Forensics
- **Difficulty:** Easy
- **Source:** picoCTF 2021

## What I Did
1. Downloaded `cat.jpg` from the challenge link using `wget`
2. Ran `exiftool cat.jpg` to inspect the file's metadata
3. Found a suspicious Base64-encoded string in the `License` field
4. Decoded it with `echo "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" | base64 -d`
5. Got the flag

## Key Concepts Learned

### Metadata
- Metadata is "data about data"
- JPEG files store EXIF metadata alongside the image itself
- Examples: timestamp, GPS location, camera model, copyright, custom fields
- In forensics, metadata is crucial evidence (who, when, where)

### Base64 Recognition
- Uses only A-Z, a-z, 0-9, `+`, `/`
- Length is always a multiple of 4
- May end with `=` or `==` padding
- Looks like random gibberish but has a recognizable character set

### Decoding Priority (CTF heuristic)
When you find a suspicious string, try in this order:
1. Base64
2. Hex
3. ROT13 / Caesar cipher
4. Other encodings

## Commands Used
```bash
wget <challenge-url>/cat.jpg
exiftool cat.jpg
echo "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" | base64 -d
```

## Flag
`picoCTF{the_m3tadata_1s_modified}`
