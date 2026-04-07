

---

## Overview

In this session, we explored two important cybersecurity techniques:

- **File forensics**: Extracting hidden data from files (even images)
- **Recursive search**: Efficiently locating specific strings within large file systems

These skills are essential for CTF challenges and real-world security analysis.

---

## 1. Enhance! (Forensics)

### Core Concept

- `.svg` files are **NOT bitmap images**
- They are **XML-based vector graphics**
- This means they can contain **readable text data**

👉 Key Insight:  
> "An image file may actually be a text file in disguise."

---

### Investigation Process

1. Open the `.svg` file using a text editor (e.g., VS Code, `strings`)
2. Analyze the XML structure
3. Look for suspicious patterns or fragmented text
4. Identify characters hidden inside tags
5. Reconstruct the flag by combining the characters in order

---

### Example Clue Pattern

```xml
<tspan>p</tspan>
<tspan>i</tspan>
<tspan>c</tspan>
...
```

👉 These fragmented characters form the hidden flag.

---

### Key Learning Points

- File extensions can be misleading
- Always inspect files using multiple tools
- Text-based formats (XML, JSON, HTML) are common hiding places
- Forensics often involves **pattern recognition and reconstruction**

---

## 2. Big Zip (General Skills)

### Core Concept

- Use `grep` for **recursive string searching**
- Essential when dealing with:
  - Large directories
  - Thousands of files
  - Hidden flags across multiple locations

👉 Key Insight:  
> "Manual searching doesn't scale — automation is required."

---

### Solution Workflow

1. Extract the archive:
```bash
unzip big-zip-files.zip
```

2. Search recursively for the flag:
```bash
grep -r "picoCTF" .
```

3. Analyze results and filter out decoys

---

### Useful Commands

```bash
# Recursive search in all files
grep -r "SEARCH_STR" [PATH]

# Include binary files as text
grep -ra "picoCTF" .

# Show file names only
grep -rl "picoCTF" .

# Case-insensitive search
grep -ri "picoctf" .
```

---

### Decoy vs Real Flag

During analysis, multiple fake flags may appear:

- `flag:picoCTF{s4n1ty_...}`  
  → Sanity check (not the answer)

- `picoCTF{l3v3l_up!...}`  
  → Intentional decoy

- ✅ **Real Flag**  
  ```
  picoCTF{gr3p_15_m4g1c_ef8790dc}
  ```

👉 Clue: The real flag is related to the **challenge theme (`grep`)**

---

## Key Takeaways

- Not all files are what they appear to be
- Always inspect file structure, not just file type
- Use command-line tools to handle large-scale data
- Learn to distinguish **signal vs noise (real vs decoy)**

---

## Practical Skills Gained

- SVG/XML file analysis
- Hidden data extraction
- Recursive file searching with `grep`
- Efficient CTF problem-solving strategies

---

## Commit Message

```
Add SVG forensics and recursive grep search notes (picoCTF)
```

---

## Extended Description

```
This commit documents key techniques learned from picoCTF challenges:
- Analyzing SVG files as XML to extract hidden flags
- Using grep for recursive string search across large directories
- Identifying decoy flags and understanding challenge patterns

Includes practical commands, workflow, and key insights for future reference.
```
