# Cyber Forensics (Digital Investigation) — Intro Lab Notes

> **Course:** Introduction to Cyber Forensics  
> **Lab File:** `suspicious_usb.img`  
> **Environment:** Ubuntu Linux (browser-based virtual machine)  
> **Date:** 2025

---

## Table of Contents

1. [What is Cyber Forensics?](#1-what-is-cyber-forensics)
2. [Incident Response vs. Forensics](#2-incident-response-vs-forensics)
3. [The 4-Step Forensic Process](#3-the-4-step-forensic-process)
4. [Lab Setup](#4-lab-setup)
5. [Step-by-Step Investigation](#5-step-by-step-investigation)
   - [Step 1: Identify the Evidence File](#step-1-identify-the-evidence-file)
   - [Step 2: Examine Disk Structure](#step-2-examine-disk-structure)
   - [Step 3: Mount the Disk Image](#step-3-mount-the-disk-image)
   - [Step 4: List Files (Including Hidden)](#step-4-list-files-including-hidden)
   - [Step 5: Search for Suspicious Content](#step-5-search-for-suspicious-content)
   - [Step 6: Extract Readable Text](#step-6-extract-readable-text)
   - [Step 7: Cleanup — Unmount](#step-7-cleanup--unmount)
6. [Evidence Found](#6-evidence-found)
7. [Key Rules & Best Practices](#7-key-rules--best-practices)
8. [Essential Linux Commands Reference](#8-essential-linux-commands-reference)
9. [Next Steps / Further Learning](#9-next-steps--further-learning)

---

## 1. What is Cyber Forensics?

Cyber forensics (also called **digital forensics**) is the process of investigating digital devices and data to uncover evidence of criminal or malicious activity.

**Core questions it answers:**
- **What** happened?
- **When** did it happen?
- **How** did it happen?
- **Who** was responsible?

**Real-world use cases:**
- Data breach investigations
- Malware infection analysis
- Insider threat investigations
- Law enforcement / legal proceedings
- Corporate HR investigations
- Regulatory compliance

---

## 2. Incident Response vs. Forensics

| Aspect | Incident Response (IR) | Forensics |
|---|---|---|
| **Goal** | Stop the attack immediately | Explain *why/how* it happened |
| **Timing** | Real-time, during the incident | Post-incident analysis |
| **Focus** | Containment & recovery | Evidence collection & root cause |
| **Output** | System restored | Detailed investigation report |

> **Key insight:** IR stops the bleeding; Forensics performs the autopsy.

---

## 3. The 4-Step Forensic Process

```
1. IDENTIFY   →   2. PRESERVE   →   3. ANALYZE   →   4. PRESENT
```

| Step | Description |
|---|---|
| **Identify** | Recognize what digital evidence exists and where it is |
| **Preserve** | Protect the original data — always work on a **copy** |
| **Analyze** | Examine the copy using forensic tools and techniques |
| **Present** | Document and report findings clearly |

---

## 4. Lab Setup

- **Virtual machine** launched via browser — no local installation needed
- **Session duration:** 30 minutes (extendable; warning at 5 min remaining)
- **Login credentials:**
  - Username: `user010`
  - Password: `UseE5#CMKA#O!`
- **Lab files location:** `/home/user010/Lab-Files/`
- **Target file:** `suspicious_usb.img` — a forensic copy of a suspicious USB drive

> ⚠️ **Warning:** Unsaved work is lost if the session expires without extension.

---

## 5. Step-by-Step Investigation

### Step 1: Identify the Evidence File

Navigate to the lab directory and confirm the target file exists.

```bash
cd /home/user010/Lab-Files
ls
```

Identify what type of file it is:

```bash
file suspicious_usb.img
```

**What this tells you:**
- The file is a **disk image** (not a regular document)
- It contains a complete disk structure with an **MBR (Master Boot Record)**
- Formatted using the **FAT16** file system
- Behaves like a bootable USB drive

---

### Step 2: Examine Disk Structure

```bash
fdisk -l suspicious_usb.img
```

**Output details:**
| Property | Value |
|---|---|
| Total size | 100 MB |
| Number of sectors | 204,800 |
| Sector size | 512 bytes |
| Partition type | DOS/MBR |

---

### Step 3: Mount the Disk Image

**Mounting** = attaching a virtual disk image so the OS treats it like a real USB drive.

```bash
sudo mount -o loop suspicious_usb.img /mnt
```

- `sudo` — run with administrator privileges
- `mount` — attach the image
- `-o loop` — treat the file as a block device (loop device)
- `/mnt` — the mount point (folder where the drive appears)

Navigate into the mounted drive:

```bash
cd /mnt
```

---

### Step 4: List Files (Including Hidden)

```bash
ls -la
```

- `ls` — list files
- `-l` — long format (shows permissions, size, etc.)
- `-a` — show **all** files, including hidden ones (files starting with `.`)

**Files discovered:**

| Filename | Type | Notes |
|---|---|---|
| `employee_data.txt` | Text file | Contains user credentials |
| `notes.txt` | Text file | Contains admin password |
| `runme.sh` | Shell script | Suspicious — potentially malicious |
| `.hidden_credentials.txt` | **Hidden file** | Contains backup password |

---

### Step 5: Search for Suspicious Content

Use `grep` to search for keywords across all files recursively:

```bash
grep -R "password" .
```

- `grep` — search tool (like Ctrl+F, but for the terminal)
- `-R` — recursive: searches all files in all subdirectories
- `"password"` — the keyword to find
- `.` — search in the current directory

**What was found:**
- `notes.txt` — exposed admin password: `P@ssw0rd123`
- `runme.sh` — contained the string `"Stealing passwords..."` confirming malicious intent

---

### Step 6: Extract Readable Text

For files that may contain binary/non-readable data, use `strings` to extract human-readable text:

```bash
strings employee_data.txt
```

Also read file contents directly:

```bash
cat employee_data.txt
cat notes.txt
cat .hidden_credentials.txt
```

---

### Step 7: Cleanup — Unmount

Always unmount the image when done. Good forensic hygiene.

```bash
cd ~                  # Exit the mounted directory first
sudo umount /mnt      # Safely detach the disk image
```

---

## 6. Evidence Found

| Evidence File | Content | Significance |
|---|---|---|
| `notes.txt` | Admin password: `P@ssw0rd123` | Credential exposure |
| `employee_data.txt` | Employee usernames & passwords | Sensitive data leak |
| `.hidden_credentials.txt` | Backup password: `Company@2025` | Hidden credential store |
| `runme.sh` | Script with `"Stealing passwords..."` | **Confirmed malicious intent** |

> **Conclusion:** The USB drive contained stolen credentials, hidden files, and a malicious script designed to exfiltrate passwords.

---

## 7. Key Rules & Best Practices

### ✅ The Golden Rule of Forensics
> **Always work on a copy. NEVER analyze the original evidence directly.**

Analyzing the original modifies timestamps and data, making it inadmissible in court.

### ✅ Documentation
- Record every command you run
- Note the output at each step
- Maintain a chain of custody

### ✅ Know How to Use Help
You don't need to memorize every command — know how to find the answer:

```bash
grep --help        # Quick usage summary
man grep           # Full manual (press q to quit)
```

---

## 8. Essential Linux Commands Reference

| Command | Purpose | Example |
|---|---|---|
| `cd` | Change directory | `cd /home/user010/Lab-Files` |
| `ls` | List files | `ls -la` |
| `file` | Identify file type | `file suspicious_usb.img` |
| `fdisk -l` | Show disk structure | `fdisk -l suspicious_usb.img` |
| `mount` | Attach disk image | `sudo mount -o loop suspicious_usb.img /mnt` |
| `umount` | Detach disk image | `sudo umount /mnt` |
| `cat` | Print file contents | `cat notes.txt` |
| `grep` | Search for text in files | `grep -R "password" .` |
| `strings` | Extract readable text from binary files | `strings employee_data.txt` |

---

## 9. Next Steps / Further Learning

### Foundations
- [ ] Deepen Linux command-line skills
- [ ] Study file systems in detail: **FAT**, **NTFS**, **EXT4**

### Intermediate Topics
- [ ] **Memory Forensics** — analyzing RAM for running processes and volatile data
- [ ] **Timeline Analysis** — reconstructing events chronologically from file timestamps
- [ ] **Network Forensics** — investigating packet captures and network logs

### Practice
- [ ] **CTF (Capture The Flag)** challenges — practical forensics puzzles
  - Recommended platforms: [PicoCTF](https://picoctf.org), [CyberDefenders](https://cyberdefenders.org), [Hack The Box](https://www.hackthebox.com)

### Tools to Explore
- **Autopsy / Sleuth Kit** — GUI-based forensic analysis suite
- **Volatility** — memory forensics framework
- **Wireshark** — network packet analyzer
- **FTK Imager** — forensic imaging tool

---

*Notes compiled from hands-on lab walkthrough — Introduction to Cyber Forensics*
