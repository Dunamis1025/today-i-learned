# Glory of the Garden — Write-up

**Category:** Forensics
**Difficulty:** Easy
**CTF:** picoCTF 2019

---

## Challenge Description

> "This file contains more than it seems. Get the flag from garden.jpg."

**Hint:** What is a hex editor?

---

## What I Learned

A file is just a sequence of 0s and 1s. Even an image file like `.jpg` can have extra data hidden at the end — after the actual image data ends. This is because computers don't care what comes after the end-of-file marker; they just display the image part. The hidden text sits silently at the tail end, invisible to the naked eye but readable if you know how to look.

---

## Tools Used

| Tool | What it does |
|------|-------------|
| `wget` | Download a file from a URL |
| `strings` | Extract all readable text from a binary file |
| `grep` | Filter output by keyword |
| `xxd` | View file contents as raw hexadecimal bytes |
| `head -N` | Show the first N lines of output |
| `tail -N` | Show the last N lines of output |

---

## Solution

### Step 1 — Download the file

```bash
wget <challenge-file-url>/garden.jpg
```

### Step 2 — Extract readable text and filter for the flag

```bash
strings garden.jpg | grep pico
```

**Output:**
```
Here is a flag: picoCTF{more_than_m33ts_the_3y3a63b5b27}
```

That's it. One command.

### Step 3 — (Optional) See it with your own eyes in hex

```bash
xxd garden.jpg | tail -20
```

You can literally see the flag text sitting at the very end of the file as raw bytes — the image data ends, and then the hidden message begins.

---

## Why This Works

A `.jpg` file has a defined end marker (`FF D9`). Anything written **after** that marker is ignored by image viewers, but it still physically exists in the file. By reading the file as raw bytes instead of as an image, we can see everything — including data that was intentionally hidden there.

This technique is a basic form of **steganography**: hiding information inside an innocent-looking file.

---

## Key Takeaway

> An image is just bytes. Always look at what's actually in the file, not just what it displays.

**Flag:** `picoCTF{more_than_m33ts_the_3y3a63b5b27}`
