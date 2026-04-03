# 07. Number Systems & Linux Basics (CTF Foundations)

## 1. Hexadecimal (16진수)

### What is Hex?
Hexadecimal is base-16 number system used in computing.

- Uses digits: 0–9, A–F
- A=10, B=11, C=12, D=13, E=14, F=15

### Prefix
- `0x` → indicates hexadecimal number
- Example: 0x3D

### Conversion Example
0x3D → Decimal

3 × 16¹ = 48  
D (13) × 16⁰ = 13  
Total = 61

✔ Result: 61

---

## 2. Binary (2진수)

### What is Binary?
Binary is base-2 number system used by computers.

- Uses only: 0 and 1

### Example
42 → Binary

42 ÷ 2 → remainder 0  
21 ÷ 2 → remainder 1  
10 ÷ 2 → remainder 0  
5 ÷ 2 → remainder 1  
2 ÷ 2 → remainder 0  
1 ÷ 2 → remainder 1  

→ Read backwards: 101010

✔ Correct Answer: 101010  
❌ Wrong: 00101010 (leading zeros not needed)

---

## 3. Base64 Encoding

### What is Base64?
Base64 converts binary data into readable text.

- Common in cybersecurity (email, tokens, data transfer)

### Example
Input:
bDNhcm5fGgzX3lwcDM1

Decode →  
l3arn_th3_b4535

✔ Flag format:
picoCTF{l3arn_th3_b4535}

---

## 4. Linux Command Basics

### echo
Prints text to terminal

echo "hello"

### -n option
Removes newline

echo -n "text"

---

### base64 -d
Decode Base64

echo -n "text" | base64 -d

---

### Pipe ( | )
Connects output → input

echo "data" | base64 -d

---

### printf (formatted output)

printf "%d\n" 0x3D → 61

---

## 5. Format Specifiers

| Format | Meaning |
|--------|--------|
| %d     | Decimal |
| %x     | Hexadecimal |
| %o     | Octal |
| %s     | String |

✔ Tip: No need to memorize → learn by repetition

---

## 6. Important Concepts

### Leading Zeros
- Do NOT include unnecessary zeros
- Example:
  - ❌ 00101010
  - ✔ 101010

---

### Shell vs Python

- Bash → command environment
- Python → programming environment

✔ Wrong:
int('0x3D', 16)

✔ Correct:
python3 → then run code

---

## 7. Key Takeaways

- 0x = hexadecimal indicator
- Binary/Hex conversion is essential in cybersecurity
- Base64 is VERY common in real-world attacks
- Linux commands can be combined like building blocks
- Practice > memorization



## 🔥 Real Insight

This is NOT just basic knowledge.

These concepts appear in:
- Packet analysis
- Log analysis
- Malware decoding
- Web exploitation

→ This is CORE cybersecurity foundation.
