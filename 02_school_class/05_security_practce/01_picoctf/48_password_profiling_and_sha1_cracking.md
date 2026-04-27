# 48. Password Profiling & SHA-1 Hash Cracking (picoCTF 2026)

## Challenge Overview

- **Challenge Name:** Password Profiler
- **Category:** General Skills
- **Difficulty:** Easy
- **Platform:** picoCTF 2026

### Description
A suspicious file was intercepted from a system. Instead of containing the password itself, it only contains its **SHA-1 hash**. Using OSINT techniques, personal details about the target were gathered. The goal is to generate a custom password list from this personal data and recover the original password by matching its hash.

### Provided Files
| File | Description |
|------|-------------|
| `userinfo.txt` | Personal details about the target |
| `hash.txt` | SHA-1 hash of the target's password |
| `check_password.py` | Script that checks a wordlist against the hash |

---

## Key Concepts

### 1. SHA-1 Hash
SHA-1 (Secure Hash Algorithm 1) is a **one-way cryptographic function** that converts any input into a fixed 40-character hex string.

- `Alice1990` → `968c2349040273dd57dc4be7e238c5ac200ceac5`
- It is **irreversible** — you cannot go from hash back to password
- The only way to crack it is **brute-force**: try many passwords, hash each one, and compare

```python
import hashlib
hashlib.sha1("Alice1990".encode()).hexdigest()
# → '968c2349040273dd57dc4be7e238c5ac200ceac5'
```

### 2. OSINT (Open Source Intelligence)
OSINT is the practice of collecting information about a target from **publicly available sources** (social media, public records, etc.).

People commonly use personal details in their passwords:
- First/last name
- Birthday
- Partner's or child's name
- Nicknames

### 3. CUPP (Common User Passwords Profiler)
CUPP is a Python tool that takes personal information as input and **automatically generates a wordlist** of likely passwords by combining and mutating that data.

- Combines name + birthday + nickname etc.
- Applies **leet mode**: `a→4`, `e→3`, `i→1`, `o→0`
- Adds special characters: `!`, `@`, `#`
- Adds random numbers at the end
- Result: thousands of password candidates

---

## Target Information (from `userinfo.txt`)

```
First Name:      Alice
Surname:         Johnson
Nickname:        AJ
Birthdate:       15-07-1990
Partner's Name:  Bob
Child's Name:    Charlie
```

**SHA-1 Hash (from `hash.txt`):**
```
968c2349040273dd57dc4be7e238c5ac200ceac5
```

---

## Solution Walkthrough

### Step 1: Download the challenge files

```bash
wget <url>/userinfo.txt
wget <url>/hash.txt
wget <url>/check_password.py
```

### Step 2: Install CUPP

```bash
git clone https://github.com/Mebus/cupp.git
cd cupp
```

- `git clone` downloads the CUPP tool from GitHub into a folder called `cupp/`
- `cd cupp` moves into that folder to run it

### Step 3: Remove the artificial slow-print delay

CUPP has a `time.sleep(0.0001)` call that makes wordlist generation very slow. Remove it before running:

```bash
sed -i 's/time.sleep(0.0001)/pass/' cupp.py
```

- `sed -i` edits the file in-place
- Replaces `time.sleep(0.0001)` with `pass` (a Python no-op)
- This makes wordlist generation near-instant

### Step 4: Run CUPP in interactive mode

```bash
python3 cupp.py -i
```

Enter the target's personal information when prompted:

```
First Name:                  Alice
Surname:                     Johnson
Nickname:                    AJ
Birthdate (DDMMYYYY):        15071990
Partner's name:              Bob
Partner's nickname:          (Enter)
Partner's birthdate:         (Enter)
Child's name:                Charlie
Child's nickname:            (Enter)
Child's birthdate:           (Enter)
Pet's name:                  (Enter)
Company name:                (Enter)
Keywords:                    N
Special chars at end:        y
Random numbers at end:       y
Leet mode:                   y
Hyperspeed Print:            y
```

This generates `alice.txt` with **29,372 password candidates**.

### Step 5: Set up the check_password script

`check_password.py` expects specific file names in the working directory:
- `hash.txt` — the target hash
- `passwords.txt` — the wordlist to check

```bash
cd ~
cp ~/cupp/alice.txt ~/passwords.txt
```

### Step 6: Run the password checker

```bash
python3 ~/check_password.py
```

The script reads each password from `passwords.txt`, computes its SHA-1 hash, and compares it to the target hash in `hash.txt`.

### Result

```
Password found: picoCTF{Aj_15901990}
```

The password was `Aj_15901990` — a combination of:
- `Aj` (nickname)
- `1590` + `1990` (birthday digits rearranged)

---

## What I Learned

| Concept | Summary |
|---------|---------|
| SHA-1 | One-way hash; can only be cracked by brute-force comparison |
| OSINT | Personal info from public sources is often used in passwords |
| CUPP | Automates wordlist generation from personal data |
| `sed -i` | In-place file editing from the command line |
| `git clone` | Downloads a remote repository locally |
| Wordlist attack | Try all candidates → hash each → compare to target |

### Security Lesson
Passwords based on personal information (name, birthday, family members) are **extremely weak** because tools like CUPP can generate and test thousands of variants in seconds. Always use a **random, unrelated password** or a password manager.

---

## Flag

```
picoCTF{Aj_15901990}
```
