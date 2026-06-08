# Password Cracking Basics with John the Ripper

> **Lab Source:** Security Impossible – Cyber Range  
> **Duration:** ~45 minutes  
> **Environment:** Ubuntu 22.04 VM (john-the-ripper jumbo edition, snap package)

---

## Table of Contents
1. [Core Concepts](#core-concepts)
2. [Tool Overview](#tool-overview)
3. [Attack Modes](#attack-modes)
4. [Lab Walkthrough](#lab-walkthrough)
   - [Step 1: Verify Installation](#step-1-verify-installation)
   - [Step 2: Prepare Hash Files](#step-2-prepare-hash-files)
   - [Step 3: Crack MD5 Hashes](#step-3-crack-md5-hashes)
   - [Step 4: Crack the Student Account Password](#step-4-crack-the-student-account-password)
5. [Key Commands Summary](#key-commands-summary)
6. [Results](#results)
7. [Lessons Learned](#lessons-learned)

---

## Core Concepts

### Password Hashing
- Password hashing is a **one-way function**: a plaintext password is transformed into a fixed-length hash string.
- Example: MD5 of `"password"` → `5f4dcc3b5aa765d61d8327deb882cf99`
- **Direct reversal is impossible.** Cracking works by guessing candidates, hashing them, and comparing against the target hash.

### How Linux Stores Passwords
- `/etc/passwd` — stores user account info (username, home dir, shell, etc.)
- `/etc/shadow` — stores the **actual encrypted password hashes** (restricted access, requires sudo)
- Modern Ubuntu uses **yescrypt (`$y$`)** as the default hashing algorithm, which is computationally expensive by design to resist brute-force attacks.

### Offline Password Cracking
- An attacker extracts password hashes from a system and attempts to recover plaintext passwords **without interacting with the login system**.
- This is why strong, unique passwords matter even if the login portal has rate-limiting.

---

## Tool Overview

### John the Ripper (JTR) — Jumbo Edition
- **Version used:** `1.9.0-jumbo-1+bleeding-126b2a4814`
- Open-source password security auditing and recovery tool.
- Supports **500+ hash formats** (MD5, SHA, bcrypt, yescrypt, NTLM, WPA, ZIP/PDF, etc.)
- The **jumbo edition** (from GitHub) is far more capable than the standard apt version — supports modern hashes like `raw-md5`, `sha512crypt`, OpenCL/GPU acceleration, and advanced attack modes.

### unshadow
- A utility bundled with John the Ripper.
- Combines `/etc/passwd` and `/etc/shadow` into a single file that JTR can process.

---

## Attack Modes

| Mode | Flag | Description |
|------|------|-------------|
| **Wordlist (Dictionary)** | `--wordlist=FILE` | Tries every word in a list (e.g., `rockyou.txt`) |
| **Single Crack** | `--single` | Uses username/GECOS info + rules for fast initial guesses |
| **Incremental (Brute Force)** | `--incremental` | Tries all character combinations — very slow |
| **Rules (Mangling)** | `--rules` | Applies transformations to wordlist (e.g., append numbers, change case) |
| **Mask** | `--mask` | Pattern-based generation (e.g., `?u?l?l?l?d?d`) |

### rockyou.txt
- One of the most famous leaked password lists (~14 million entries).
- Located at `/usr/share/wordlists/rockyou.txt` on Kali/Ubuntu security VMs.
- Highly effective against weak, common passwords.

---

## Lab Walkthrough

### Step 1: Verify Installation

```bash
john-the-ripper --help
john-the-ripper --list=formats | grep -i md5
john-the-ripper --list=formats | grep -i crypt
```

**Purpose:** Confirm JTR is the jumbo build and that required formats (`raw-md5`, `sha512crypt`, `yescrypt`) are available.

**Expected output:** Version string shows `jumbo-bleeding` build; `Raw-MD5`, `sha512crypt` appear in format lists.

---

### Step 2: Prepare Hash Files

```bash
mkdir ~/johnlab && cd ~/johnlab
```

**Create `hashes.txt`** (5 raw MD5 hashes):
```bash
cat > hashes.txt << EOF
5f4dcc3b5aa765d61d8327deb882cf99
0192023a7bbd73250516f069df18b500
f30aa7a662c728b7407c54ae6bfd27d1
0d107d09f5bbe40cade3de5c71e9e9b7
d8578edf8458ce06fbc5bb76a58c5ca4
EOF
```

**Create `newhash.txt`** (2 additional MD5 hashes):
```bash
cat > newhash.txt << EOF
5ebe2294ecd0e0f08eab7690d2a6ee69
6e0b7076126a29d5dfcbd54835387b7b
EOF
```

**Verify:**
```bash
cat hashes.txt
cat newhash.txt
```

---

### Step 3: Crack MD5 Hashes

```bash
~/johnlab/john/run/john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
~/johnlab/john/run/john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt newhash.txt
```

**Why `--format=raw-md5`?**  
JTR may not auto-detect unsalted MD5 correctly. Explicitly specifying the format ensures accurate cracking.

**Results:**

| Hash | Cracked Password |
|------|-----------------|
| `5f4dcc3b5aa765d61d8327deb882cf99` | `password` |
| `0192023a7bbd73250516f069df18b500` | `qwerty` |
| `f30aa7a662c728b7407c54ae6bfd27d1` | `letmein` |
| `0d107d09f5bbe40cade3de5c71e9e9b7` | `hello123` |
| `d8578edf8458ce06fbc5bb76a58c5ca4` | `admin123` |
| `5ebe2294ecd0e0f08eab7690d2a6ee69` | `secret` |
| `6e0b7076126a29d5dfcbd54835387b7b` | `john123` |

All 7 hashes cracked in **under 2 seconds** using dictionary attack.

---

### Step 4: Crack the Student Account Password

#### 4-1. Navigate to JTR run directory
```bash
cd ~/johnlab/john/run
```

#### 4-2. Extract and combine password files using unshadow
```bash
sudo ./unshadow /etc/passwd /etc/shadow > ~/johnlab/student_hashes.txt
```

#### 4-3. Verify the file and locate the student entry
```bash
cd ~/johnlab
cat student_hashes.txt
# Look for the line starting with "student:"
```

#### 4-4. Extract only the student hash line
```bash
grep "^student" ~/johnlab/student_hashes.txt > ~/johnlab/student_hash.txt
cat student_hash.txt
```

Example output:
```
student:$y$j9T$80BdC/P3y.x/2pE52FGuQ/$z3eNILG3PDbJeHJJxfS9ahCRGR0hTkrUbnTc/aFJVqC:1001:1001::/home/student:/bin/bash
```

The `$y$` prefix indicates **yescrypt** hashing algorithm.

#### 4-5. Remove the full unshadow file (cleanup)
```bash
sudo rm ~/johnlab/student_hashes.txt
```

#### 4-6. Run the cracker
```bash
cd ~/johnlab/john/run
./john ~/johnlab/student_hash.txt
```

**Result:** `password123` cracked in **~36 seconds**

---

## Key Commands Summary

| Command | Purpose |
|---------|---------|
| `john --help` | Show all available options |
| `john --list=formats \| grep -i md5` | Filter supported formats containing "md5" |
| `john --format=raw-md5 --wordlist=FILE hashfile` | Dictionary attack on unsalted MD5 hashes |
| `./unshadow /etc/passwd /etc/shadow` | Combine passwd + shadow for JTR input |
| `grep "^username" file > output` | Extract specific user's hash line |
| `./john hashfile` | Run JTR with auto-detection |
| `john --show hashfile` | Display all previously cracked passwords |

---

## Results

| Target | Hash Type | Method | Time | Result |
|--------|-----------|--------|------|--------|
| `hashes.txt` (5 hashes) | Raw MD5 | Dictionary (rockyou.txt) | < 2 sec | All cracked ✅ |
| `newhash.txt` (2 hashes) | Raw MD5 | Dictionary (rockyou.txt) | < 2 sec | All cracked ✅ |
| `student` account | yescrypt (`$y$`) | Single + Wordlist | ~36 sec | `password123` ✅ |

---

## Lessons Learned

### Why Dictionary Attacks Are So Powerful
- Most people reuse common or predictable passwords found in leaked lists like `rockyou.txt`.
- Even "slightly modified" common passwords (e.g., `password123`, `admin123`) are cracked instantly.

### Why Hash Algorithm Matters
- **MD5** (unsalted): Extremely fast to compute → cracked in milliseconds at scale.
- **yescrypt**: Intentionally slow and memory-hard → takes longer but still falls to weak passwords.
- A **strong algorithm** can only slow down the attack, not stop it if the password is weak.

### Defense Recommendations
- Use **long, random, unique passwords** (16+ characters).
- Enable **Multi-Factor Authentication (MFA)**.
- Use a **password manager** to avoid reuse.
- Organizations should enforce **password complexity policies** and audit with tools like JTR on their own systems.

### Ethical & Legal Note
> John the Ripper and similar tools must **only be used on systems you own or have explicit written permission to test**. Unauthorized use is illegal and unethical.

---

*Lab completed on Security Impossible Cyber Range — Ubuntu 22.04 VM*
