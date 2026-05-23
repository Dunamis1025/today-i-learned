# Lab 08: Password Cracking with John the Ripper and Hashcat

> **Course:** Ethical Hacking V2 Lab Series  
> **Date:** 2024-02-01  
> **Tools Used:** `cewl`, `crunch`, `john`, `hashcat`, `unshadow`  
> **Environment:** Kali Linux, OWASP Broken Web App (BWA), pfSense

---

## Table of Contents
1. [Overview & Purpose](#overview--purpose)
2. [Lab Environment](#lab-environment)
3. [Core Concepts](#core-concepts)
4. [Task 1 — Generating Password Lists](#task-1--generating-password-lists)
5. [Task 2 — Creating Target User Accounts](#task-2--creating-target-user-accounts)
6. [Task 3 — Password Cracking with John the Ripper](#task-3--password-cracking-with-john-the-ripper)
7. [Task 4 — Password Cracking with Hashcat](#task-4--password-cracking-with-hashcat)
8. [Key Takeaways](#key-takeaways)

---

## Overview & Purpose

This lab simulates a **post-exploitation scenario** — meaning the attacker has already gained root (administrator) access to a Linux system. From that position, the goal is to extract hashed passwords and crack them using dictionary-based attacks.

This type of attack is called **Offline Hash Cracking**: instead of repeatedly attempting to log in (which would trigger lockouts), the attacker copies the password hashes to their own machine and cracks them locally — unlimited, undetected.

**Why learn this?**  
Security professionals must understand how attacks work in order to build effective defenses. This lab demonstrates why weak passwords are dangerous and why strong password policies matter.

---

## Lab Environment

| Virtual Machine      | IP Address(es)                              | Username | Password  |
|----------------------|---------------------------------------------|----------|-----------|
| Kali Linux (Attacker)| 192.168.9.2 / 192.168.0.2                  | root     | toor      |
| pfSense (Firewall)   | 192.168.0.254 / 192.168.68.254 / 192.168.9.1 | admin  | pfsense   |
| OWASP Broken Web App | 192.168.68.12                               | root     | owaspbwa  |

**Network Topology:**
```
[Kali Linux] ── WAN (192.168.9.0/24) ── [pfSense] ── DMZ (192.168.68.0/24) ── [OWASP BWA]
```

---

## Core Concepts

### What is a Hash?
When you set a password (e.g., `123456`), Linux does **not** store it as plain text. Instead, it runs it through a one-way mathematical function called a **hash function** and stores the result:

```
123456  →  SHA-512  →  $6$Px9IYfP85Yxa...(long string)
```

This is a **one-way function** — you cannot reverse the hash back to the original password mathematically.

### How Does Cracking Work?
Since reversing is impossible, attackers go the other direction:

```
(guess) "password"  →  hash it  →  compare with stored hash
                                      ↓
                             Match? → Found the password!
                             No match? → Try next word
```

This is called a **Dictionary Attack** — trying thousands or millions of candidate words until a match is found.

### Where Are Hashes Stored on Linux?

| File           | Contents                                      | Access       |
|----------------|-----------------------------------------------|--------------|
| `/etc/passwd`  | User account info (username, home dir, shell) | All users    |
| `/etc/shadow`  | Hashed passwords                              | Root only    |

---

## Task 1 — Generating Password Lists

Before cracking, you need a **wordlist** (dictionary) — a file full of candidate passwords to try. This task builds one from three sources.

### Step 1: Scrape words from the target website using `cewl`

```bash
cewl --help                                          # explore the tool
cewl -w owaspwords.txt -d 2 -m 5 192.168.68.12      # scrape target site
cat owaspwords.txt                                    # view results
```

**What this does:**
- `cewl` crawls the OWASP web server and extracts words found on its pages
- `-w owaspwords.txt` → save output to this file
- `-d 2` → follow links up to 2 levels deep
- `-m 5` → only include words 5+ characters long

**Why this matters:**  
People tend to use words related to their environment as passwords (company names, project names, etc.). Scraping the target's own website gives us contextually relevant candidates.

**Sample output:**
```
brand
Smithuser
localhost
transaction
statement
Leakage
```

---

### Step 2: Generate brute-force combinations using `crunch`

```bash
crunch                                               # view tool info
crunch 4 8 charset.lst lalpha -o list.txt            # generate combinations
```

**What this does:**
- Generates **every possible combination** of lowercase letters
- Between 4 and 8 characters long
- Output saved to `list.txt`

**Result:** ~48 million combinations, ~409 MB

**Why this matters:**  
`cewl` only finds real words. `crunch` covers passwords like `abcd`, `zzzz`, `abcde` — random-looking strings that wouldn't appear in any dictionary.

---

### Step 3: Combine all wordlists into one master list

```bash
# Merge cewl words + crunch combinations into one file
cat owaspwords.txt list.txt > mylist.txt

# Append John the Ripper's built-in common password list
cat /usr/share/john/password.lst >> mylist.txt
```

**Final wordlist composition:**

| Source              | Content                              | Size       |
|---------------------|--------------------------------------|------------|
| `owaspwords.txt`    | Words scraped from OWASP site        | ~hundreds  |
| `list.txt`          | All lowercase letter combinations    | ~48M       |
| `password.lst`      | Common passwords (John's built-in)   | 3,559      |
| **`mylist.txt`**    | **Combined master wordlist**         | **~48.4M** |

---

## Task 2 — Creating Target User Accounts

This task sets up intentionally vulnerable accounts to crack — simulating real users with weak passwords.

### Create accounts and assign weak passwords

```bash
useradd fake3
useradd fake4

passwd fake3    # set password: 123456
passwd fake4    # set password: password
```

### Verify hashes were created in `/etc/shadow`

```bash
cat /etc/shadow
```

**Expected output (excerpt):**
```
fake3:$6$Px9IYfP85Yxa...(hash)...:18444:0:99999:7:::
fake4:$6$2HwqFaHeq6Za...(hash)...:18444:0:99999:7:::
```

The password `123456` is now stored as a long, unreadable hash. The goal is to recover the original from that hash.

### Prepare hash file for cracking tools

```bash
# Combine /etc/passwd and /etc/shadow into one cracker-friendly file
unshadow /etc/passwd /etc/shadow > hashes.txt

# Filter down to only the two fake accounts
cat hashes.txt | grep fake* > hashes2.txt

# Verify contents
cat hashes2.txt
```

**What `unshadow` does:**  
John the Ripper needs both the account info (`/etc/passwd`) and the hash (`/etc/shadow`) merged together in a specific format. `unshadow` handles that conversion automatically.

**Output of `hashes2.txt`:**
```
fake3:$6$Px9IYfP85Yxa...(hash)...:1000:1000::/home/fake3:/bin/sh
fake4:$6$2HwqFaHeq6Za...(hash)...:1001:1001::/home/fake4:/bin/sh
```

---

## Task 3 — Password Cracking with John the Ripper

**John the Ripper** is one of the oldest and most well-known password cracking tools. It auto-detects hash types and supports multiple attack modes.

### Explore the tool

```bash
john
```

### Run the cracker with the default wordlist

```bash
john --wordlist=/usr/share/john/password.lst hashes2.txt
```

**What happens:**
1. John reads the hashes from `hashes2.txt`
2. For each word in `password.lst`, it hashes the word using SHA-512
3. It compares the result to the stored hashes
4. If there's a match → password found

**Output:**
```
password    (fake4)
123456      (fake3)
```

Both passwords cracked almost immediately — because they're in the default wordlist.

### Compare wordlist sizes

```bash
wc -l /root/mylist.txt                    # → 48,432,715 entries
wc -l /usr/share/john/password.lst        # → 3,559 entries
```

| Wordlist        | Size       | Time to run | Coverage          |
|-----------------|------------|-------------|-------------------|
| `password.lst`  | 3,559      | Seconds     | Common passwords only |
| `mylist.txt`    | ~48.4 M    | Hours/Days  | Very broad coverage |

### Display cracked passwords

```bash
john --show hashes2.txt
```

**Output:**
```
fake3:123456:1000:1000::/home/fake3:/bin/sh
fake4:password:1001:1001::/home/fake4:/bin/sh

2 password hashes cracked, 0 left
```

---

## Task 4 — Password Cracking with Hashcat

**Hashcat** is a more advanced cracking tool that leverages GPU acceleration via OpenCL, making it significantly faster than CPU-based tools like John the Ripper. In this lab, CPU-only mode is used.

### Explore the tool

```bash
hashcat -h | more     # press Space to scroll, Q to quit
```

### Prepare the hash file for Hashcat

Hashcat requires **pure hash values only** — no usernames, no extra fields.

Open `hashes2.txt` in a text editor (Mousepad) and manually edit each line:

**Before:**
```
fake3:$6$Px9IYfP85Yxa...(hash)...:1000:1000::/home/fake3:/bin/sh
```

**After (keep only the hash):**
```
$6$Px9IYfP85Yxa...(hash)...
```

Save as `hashes3.txt`.

### Run Hashcat

```bash
hashcat --force -m 1800 -a 0 hashes3.txt mylist.txt

# If device error occurs, specify device explicitly:
hashcat --force -m 1800 -a 0 hashes3.txt mylist.txt -d 1
```

**Flag breakdown:**

| Flag       | Meaning                                                        |
|------------|----------------------------------------------------------------|
| `--force`  | Ignore warnings and run anyway                                 |
| `-m 1800`  | Hash type: sha512crypt (Linux SHA-512 password hashes)         |
| `-a 0`     | Attack mode: Dictionary attack (straight wordlist comparison)  |
| `-d 1`     | Use device #1 (first available CPU/GPU)                        |

### Monitor cracking progress

Press `s` while running to see status:

```
Session.........: hashcat
Status..........: Running
Hash.Type.......: sha512crypt $6$, SHA512 (Unix)
Hash.Target.....: hashes3.txt
Time.Estimated..: Tue Jul 28 05:54:50 2020 (11 hours, 45 mins)
Speed.#1........: 1135 H/s
Recovered.......: 1/2 (50.00%) Digests
Progress........: 774144/96865346 (0.80%)
```

**Key fields explained:**

| Field            | Meaning                                               |
|------------------|-------------------------------------------------------|
| `Hash.Type`      | The algorithm being targeted (set by `-m 1800`)       |
| `Time.Estimated` | How long until all candidates are tested              |
| `Speed.#1`       | Hashes tested per second (varies by hardware)         |
| `Recovered`      | How many passwords have been cracked so far           |

### Quit and resume later

```bash
# Press Q to quit — progress is automatically saved
# To resume later:
hashcat --restore
```

---

## Key Takeaways

### 1. Weak passwords are cracked instantly
`123456` and `password` are in every default wordlist. They were cracked in seconds. A password that appears in any common list is effectively no password at all.

### 2. The attacker builds a bigger net over time
The larger and more targeted the wordlist, the more passwords can be cracked — but it takes longer. Attackers balance:
- **Speed** (smaller list, fewer candidates)
- **Coverage** (larger list, more candidates)

### 3. Offline cracking is silent and unlimited
Once hashes are stolen, cracking happens on the attacker's own machine. There are no login attempt limits, no lockouts, no alerts sent to the victim. This is why protecting the `/etc/shadow` file is critical.

### 4. John vs Hashcat

| Feature        | John the Ripper         | Hashcat                        |
|----------------|-------------------------|--------------------------------|
| Ease of use    | Simpler                 | More options/flags             |
| Speed          | CPU-based               | GPU-accelerated (much faster)  |
| Hash detection | Auto-detects            | Must specify with `-m` flag    |
| Input format   | Accepts unshadow format | Requires raw hashes only       |
| Resume support | Limited                 | Built-in checkpoint/restore    |

### 5. Defense recommendations
- Use **long, random passwords** (16+ characters, mix of all character types)
- Avoid **dictionary words**, names, or patterns
- Use a **password manager** — humans are bad at generating randomness
- Enable **multi-factor authentication (MFA)** wherever possible
- Protect root access — if an attacker gets root, all hashes are exposed

---

## Commands Reference

```bash
# Wordlist generation
cewl -w output.txt -d 2 -m 5 <target-ip>
crunch <min> <max> charset.lst <charset> -o output.txt
cat file1.txt file2.txt > combined.txt
cat file.txt >> existing.txt

# Hash extraction
cat /etc/shadow
unshadow /etc/passwd /etc/shadow > hashes.txt
cat hashes.txt | grep <username> > filtered.txt

# John the Ripper
john --wordlist=<wordlist> <hashfile>
john --show <hashfile>
wc -l <file>

# Hashcat
hashcat -h
hashcat --force -m 1800 -a 0 <hashfile> <wordlist>
hashcat --force -m 1800 -a 0 <hashfile> <wordlist> -d 1
# During run: s = status, q = quit (saves progress)
```

---

*Study notes from NDG Ethical Hacking V2 Lab Series — Lab 08*
