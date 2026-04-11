# 26. Text Transformation Reversal — picoCTF "Undo" Write-up

## Challenge Info
- **Platform:** picoCTF 2026
- **Category:** General Skills
- **Difficulty:** Easy
- **Challenge Name:** Undo

## Problem Description
Reverse a series of Linux text transformations to recover the original flag.
Each step shows the transformed flag and a hint. Enter the correct Linux command to reverse it.

## Connection
```bash
nc foggy-cliff.picoctf.net 54386
```

## Solution — Step by Step

### Step 1: Base64 Decode
- **Hint:** Base64 encoded the string.
- **Command:**
```bash
base64 -d
```
- **Key concept:** `base64 -d` decodes a Base64-encoded string. The `-d` flag stands for **decode**.

---

### Step 2: Reverse the Text
- **Hint:** Reversed the text.
- **Command:**
```bash
rev
```
- **Key concept:** `rev` reverses the order of characters in each line.

---

### Step 3: Replace Dashes with Underscores
- **Hint:** Replaced underscores with dashes.
- **Command:**
```bash
tr '-' '_'
```
- **Key concept:** `tr 'A' 'B'` replaces every occurrence of character A with character B.

---

### Step 4: Replace Parentheses with Curly Braces
- **Hint:** Replaced curly braces with parentheses.
- **Command:**
```bash
tr '()' '{}'
```
- **Key concept:** `tr` can replace multiple characters simultaneously. `(` → `{` and `)` → `}` in one command.

---

### Step 5: Reverse ROT13
- **Hint:** Applied ROT13 to letters.
- **Command:**
```bash
tr 'a-zA-Z' 'n-za-mN-ZA-M'
```
- **Key concept:** ROT13 shifts each letter by 13 positions. Since the alphabet has 26 letters, applying ROT13 twice returns the original string. The range `a-z` → `n-za-m` handles the wrap-around.

---

## Flag

picoCTF{Revers1ng_t3xt_Tr4nsf0rm@t10ns_dcc1896c}

## Commands Learned Today

| Transformation       | Command                          |
|----------------------|----------------------------------|
| Base64 decode        | `base64 -d`                      |
| Reverse text         | `rev`                            |
| Character substitution | `tr 'old' 'new'`               |
| ROT13 decode         | `tr 'a-zA-Z' 'n-za-mN-ZA-M'`    |

## Key Takeaway
> In CTF challenges, text transformations are often layered (encoded → reversed → substituted).
> Reversing them requires applying each operation in the **opposite order**.
> The `tr` command is extremely versatile for character-level substitution in Linux.
