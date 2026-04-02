# 01_ROT13_CLI.md

## 🚩 picoCTF - ROT13 (Mod 26)

---

## 📝 Problem Overview
- Category: Cryptography
- Goal: Decode a ROT13 encrypted flag from `values.txt`

---

## 🛠️ Solution Approaches

### 1. Basic Method (CyberChef)
1. Download `values.txt`
2. Open in CyberChef
3. Apply ROT13
4. Get readable flag

---

### 2. CLI Method (Webshell / Linux) 🚀

```bash
cat values.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

---

## 🔍 Command Breakdown

### 1. cat (Concatenate)
- Displays file content
- Originally used to combine multiple files
- Not a cat 🐱 → means "concatenate"

---

### 2. | (Pipe)
- Sends output from one command to another

Example:
```bash
cat file.txt | another_command
```

---

### 3. tr (Translate)
- Replaces characters based on mapping

```bash
tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

#### Mapping Concept:
| Original | Converted |
|----------|----------|
| A        | N        |
| B        | O        |
| C        | P        |
| ...      | ...      |
| N        | A        |

👉 1:1 positional mapping

---

## 🔐 What is ROT13?

ROT13 = Rotate by 13 positions

- Alphabet has 26 letters
- 13 = half of 26

### 특징:
- Apply once → encode
- Apply again → decode

Example:
```
A → N → A
B → O → B
```

---

## 🧠 Key Takeaways

- CLI is faster and scalable than GUI tools
- Pipe (`|`) is essential for chaining commands
- `tr` is powerful for quick transformations
- Understanding mapping is critical for encoding/decoding

---

## ⚔️ CyberChef vs CLI

| Tool        | Pros                     | Cons                  |
|------------|--------------------------|-----------------------|
| CyberChef  | Easy, visual             | Manual, not scalable  |
| CLI        | Fast, automatable        | Requires practice     |

---

## 💭 Reflection

Using CyberChef is convenient,  
but solving it with CLI feels more like real hacking.

---

