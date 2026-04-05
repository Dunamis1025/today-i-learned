# 06. Webshell Commands & picoCTF Workflow

---

## 1. Overview

This note summarizes essential webshell (Linux terminal) commands and practical workflow used in picoCTF challenges.

Focus:
- Navigating files
- Viewing and analyzing code
- Running scripts
- Extracting hidden data (passwords, flags)

---

## 2. Core Webshell Commands

### File Download
`wget <URL>`

- Downloads files from the internet  
- Used to retrieve challenge files  

Example:  
`wget https://example.com/level1.py`

---

### List Files
`ls`  
`ls -l`

- `ls` → shows files  
- `ls -l` → detailed info  

---

### Change Directory
`cd <directory>`

- Moves between folders  
- Works only for directories (NOT files)

---

### View File Content

`nano filename.py`  
- Open file for reading/editing  
- Exit: `Ctrl + X`

`cat filename.py`  
- Quick full output  

`less filename.py`  
- Scrollable view  

---

### Run Python Script
`python3 filename.py`

- Executes scripts  
- Usually asks for password input  

---

### View Binary File
`bvi filename.bin`

- Inspect binary / encoded files  
- Exit: `:q`

---

## 3. picoCTF Workflow

### Step 1: Download Files
`wget <file1>`  
`wget <file2>`

---

### Step 2: Inspect Code
`nano levelX.py`

Look for:
- Hardcoded passwords  
- Encoded values  
- Input checks  

Example:
`if user_pw == "password":`

---

### Step 3: Identify Patterns

#### Plain Text Password
`if user_pw == "secret"`

→ Direct answer  

---

#### Hex / ASCII Encoding
`chr(0x34) + chr(0x65)`

→ Convert hex to characters  

Example:  
`0x34 = '4'`  
`0x65 = 'e'`

---

#### Password List
`pos_pw_list = ["pw1", "pw2", "pw3"]`

→ Try each one  

---

### Step 4: Use Python Interpreter

Start:
`python3`

Then:
`print(chr(0x34) + chr(0x65))`

---

### Step 5: Run Program
`python3 levelX.py`

- Enter password  
- Get flag  

---

## 4. Key Concepts

### Do NOT Overcomplicate

"The str_xor function does not need to be reverse engineered."

Meaning:
- No need to understand encryption  
- Just find correct input  

---

### Focus on Input Check

`if input == correct_value`

→ Find `correct_value`

---

### Code Reading is Key

- Most beginner CTF = reading logic  
- Not hacking systems  

---

## 5. Common Mistakes

### Wrong: Using cd on files
`cd level2.py`

---

### Wrong: Running Python in shell
`print(chr(0x34))`

---

### Correct:
`python3`  
`>>> print(chr(0x34))`

---

### File Structure Issue
- `.py` and `.enc` must be in same folder  

---

## 6. Key Takeaway

CTF solving loop:

1. Download  
2. Read code  
3. Find logic  
4. Reconstruct input  
5. Execute  

"Understand the logic, not the tool."

---

## 7. Skills Gained

- Linux terminal usage  
- Python code reading  
- Encoding / decoding basics  
- Problem-solving mindset  

---

## Final Insight

The terminal is not magic.  
It simply reveals what the code already contains.
