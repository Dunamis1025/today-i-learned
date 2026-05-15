# 07. DISKO 1 — Disk Image Forensics

## Challenge Info

| Field      | Details             |
|------------|---------------------|
| Category   | Forensics           |
| Difficulty | Easy                |
| Points     | 1 pt                |
| Platform   | CyLab Security Academy (formerly picoCTF) |

**Challenge Description:**
> Can you find the flag in this disk image? Download the disk image here.

---

## What This Challenge Teaches

In real-world forensics, investigators never work directly on a suspect's original storage device — they make a **disk image**: an exact byte-for-byte copy of the entire drive. This challenge simulates that scenario.

Key concepts practiced:
- Understanding disk image file formats (`.dd`, `.img`)
- Compressed file handling (`.gz`)
- Using `file` to identify file types
- Using `strings` to extract human-readable text from binary files
- Understanding why `mount` is the "proper" approach vs. `strings` as a shortcut

---

## Tools Used

| Tool      | Purpose                                      |
|-----------|----------------------------------------------|
| `wget`    | Download the disk image from the server      |
| `gunzip`  | Decompress the `.gz` compressed file         |
| `file`    | Identify what kind of file we're working with |
| `strings` | Extract readable text from a binary file     |
| `grep`    | Filter output to find the flag format        |

---

## Step-by-Step Solution

### Step 1: Download the Disk Image

```bash
wget https://artifacts.picoctf.net/c/536/disko-1.dd.gz
```

The file comes as a `.gz` (gzip compressed) archive.

### Step 2: Decompress the File

```bash
gunzip disko-1.dd.gz
```

This extracts `disko-1.dd` — a raw disk image file.

### Step 3: Identify the File Type

```bash
file disko-1.dd
```

**Output:**
```
disko-1.dd: DOS/MBR boot sector, code offset 0x58+2, OEM-ID "mkfs.fat",
Media descriptor 0xf8, sectors/track 32, heads 8, sectors 102400
(volumes > 32 MB), FAT (32 bit), sectors/FAT 78, serial number 0x241a4420, unlabeled
```

**What this means:**
- **DOS/MBR boot sector** → This disk has a Master Boot Record, the standard structure for bootable drives
- **FAT (32 bit)** → FAT32 file system, commonly used on USB flash drives
- In short: this is a virtual USB drive image

### Step 4: Attempt Proper Mounting (for learning purposes)

The "correct" forensic approach would be:

```bash
mkdir mnt
sudo mount -o loop disko-1.dd mnt/
ls mnt/
find mnt/ -name "flag*"
```

> **Note:** In the CyLab webshell environment, `sudo` and `fdisk` are not available due to security restrictions. So mounting was not possible in this environment.

### Step 5: Extract Flag with `strings` (Workaround)

Since mounting was blocked, we used `strings` as an alternative approach:

```bash
strings disko-1.dd | grep picoCTF
```

**What each part does:**
- `strings disko-1.dd` → Scans the entire binary file and outputs every sequence of readable ASCII text (4+ characters by default)
- `| grep picoCTF` → Pipes that output into `grep`, which filters for lines containing `picoCTF` (the flag format)

**Output:**
```
picoCTF{1t5_ju5t_4_5tr1n9_c63b02ef}
```

---

## Flag

```
picoCTF{1t5_ju5t_4_5tr1n9_c63b02ef}
```

---

## Key Takeaways

### The Proper Way vs. The CTF Shortcut

| Approach | Method | When to Use |
|----------|--------|-------------|
| **Proper forensics** | `mount` → browse files → `find` | Real investigations; learning disk structure |
| **CTF shortcut** | `strings` + `grep` | Quick flag hunting; when mount is unavailable |

### Why `strings` Works Here
The flag was stored as a plain text file inside the FAT32 filesystem. Even without mounting the disk, `strings` can scan the raw binary and pick out any readable text — including the flag.

### What Real Forensic Analysts Do
In actual investigations, analysts use tools like:
- **Autopsy** or **FTK** (GUI-based forensic suites)
- **The Sleuth Kit (TSK)** — command-line forensic toolkit
- `mmls` (list partition layout), `fls` (list files), `icat` (extract file by inode)

These give a structured view of the filesystem without needing `sudo` or kernel-level mounting.

---

## Concepts to Remember

- **Disk image (`.dd`)**: A raw, sector-by-sector copy of a storage device
- **FAT32**: A simple filesystem format common on USB drives and SD cards
- **`gunzip`**: Decompresses `.gz` files
- **`strings`**: Extracts printable character sequences from any binary — a powerful forensic quick-scan tool
- **`grep`**: Filters text output by pattern
- **`mount -o loop`**: Mounts a file as if it were a physical disk (requires root/sudo)
- **MBR (Master Boot Record)**: The first sector of a disk, containing partition info and boot code
