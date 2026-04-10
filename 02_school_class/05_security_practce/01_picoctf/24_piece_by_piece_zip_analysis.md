# 24. Piece by Piece – ZIP Splitting & Extraction (picoCTF 2026)

## Challenge Info
- **Category:** General Skills
- **Difficulty:** Easy
- **Platform:** picoCTF 2026
- **Solves:** 5,297 | **Liked:** 99%

## Description
Multiple file parts are stored in the home directory.
Combine and extract them to reveal the flag.

## Connection
- **Host:** `dolphin-cove.picoctf.net`
- **Port:** `51722`
- **User:** `ctf-player`
- **Auth:** password provided on instance launch

## Solution Steps

### 1. SSH into the instance
```bash
ssh ctf-player@dolphin-cove.picoctf.net -p 51722
# Enter password when prompted (characters won't be visible — this is normal)
```

### 2. List files in home directory
```bash
ls -la
# Found: instructions.txt, part_aa, part_ab, part_ac, part_ad, part_ae
```

### 3. Read the instructions
```bash
cat instructions.txt
```
**Key hints from instructions.txt:**
- The flag is split into multiple parts as a zip file
- Use Linux commands to combine the parts into one file
- The zip file is password protected — password: `supersecret`
- After unzipping, check the extracted text file for the flag

### 4. Combine all parts into one zip file
```bash
cat part_* > combined.zip
```

### 5. Extract with password
```bash
unzip -P supersecret combined.zip
# Extracts: flag.txt
```
> ⚠️ Note: `-P` must be uppercase. `-p` (lowercase) is a different option.

### 6. Read the flag
```bash
cat flag.txt
```

## Flag
picoCTF{z1p_and_spl1t_f1l3s_4r3_fun_27804340}
## Key Takeaways
- `cat part_* > file.zip` — combines split files in alphabetical order using wildcard
- `unzip -P <password> file.zip` — extracts a password-protected zip (`-P` uppercase)
- `file <filename>` — useful command to identify unknown file types
- Always read `instructions.txt` or any readme file first — it often contains all the hints needed
- When SSH password input appears blank, that is expected Unix behavior
