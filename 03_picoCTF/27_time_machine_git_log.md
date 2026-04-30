# 27. Time Machine — Git Log & Commit History Analysis (picoCTF 2024)

## Overview

| Field      | Details                          |
|------------|----------------------------------|
| Challenge  | Time Machine                     |
| CTF        | picoCTF 2024                     |
| Category   | General Skills                   |
| Difficulty | Easy                             |
| Solves     | 52,209                           |
| Tags       | `git`, `browser_webshell_solvable` |

---

## Problem Description

> "What was I last working on? I remember writing a note to help me remember..."

A `challenge.zip` file is provided. The hints suggest:
- `cat` won't help you read the flag
- The challenge involves Git
- Git commits can (and should) include messages

---

## Key Concept

Git stores a full history of commits, each with an author, timestamp, and a **commit message**.  
Using `git log`, you can travel back in time through that history — hence the name *Time Machine*.

```
git log         # Full commit history with messages
git log --oneline   # Condensed one-line view per commit
```

The flag was hidden inside a **commit message**, not inside any file — which is why `cat` doesn't work.

---

## Solution

### Step 1 — Download and extract the challenge file

```bash
wget <challenge.zip URL>
unzip challenge.zip
cd drop-in
```

> ⚠️ If wget saves the file as `challenge.zip.2` (duplicate filename), unzip that instead:
> ```bash
> unzip challenge.zip.2
> cd drop-in
> ```

> ⚠️ Check where the files are extracted to. The zip may unpack into a nested path like  
> `home/ctf-player/drop-in/` instead of directly into `drop-in/`.  
> Always verify with `ls` before `cd`.

### Step 2 — Verify it's a git repository

```bash
ls -a
# Should show a .git/ folder
```

If `.git/` is missing, you're in the wrong directory or extracted the wrong zip.

### Step 3 — Read the git commit history

```bash
git log
```

### Step 4 — Find the flag in the commit message

```
commit b92bdd8ec87a21ba45e77bd9bed3e4893faafd0f (HEAD -> master)
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:10:29 2024 +0000

    picoCTF{t1m3m@ch1n3_5cde9075}
```

---

## Flag

```
picoCTF{t1m3m@ch1n3_5cde9075}
```

---

## Lessons Learned

- **Always run `git log` first** on any challenge that involves a git repository.
- Commit messages are meant for human-readable notes — in CTFs, they're a common hiding spot for flags.
- `cat` only reads file contents. It cannot read git metadata like commit messages.
- When unzipping, always check the actual extraction path with the output lines or `ls` — it may differ from what you expect.
- A missing `.git/` folder means `git log` will throw `fatal: not a git repository` — double-check your directory.
