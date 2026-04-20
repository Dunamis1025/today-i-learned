# TIL: Hexadecimal to ASCII Conversion (picoCTF - Lets Warm Up)

## 📅 Date: 2026-04-21
## 📂 Category: General Skills / Cryptography Concepts
## 📝 Challenge: Lets Warm Up

---

### 1. Challenge Description
The challenge provides a hexadecimal value `0x70` and asks for its corresponding character in the ASCII (American Standard Code for Information Interchange) table. 

- **Input (Hex):** `0x70`
- **Goal:** Convert the hex value to an ASCII character and submit in the format `picoCTF{character}`.

---

### 2. Technical Concepts

#### A. Understanding Hexadecimal (Base-16)
Hexadecimal is a positional numeral system with a radix, or base, of 16. It uses sixteen distinct symbols: `0–9` and `A–F` (representing values 10–15). In programming, the prefix `0x` is used to denote hexadecimal literals.

#### B. The ASCII Table
ASCII is a character encoding standard for electronic communication. Each character (letters, digits, punctuation) is assigned a specific number. 
- For example, the number **112** in decimal is mapped to the lowercase letter **'p'**.

---

### 3. Solution Approach

#### Method 1: Using Python Interpreter (Recommended)
Python provides built-in functions to handle encoding and base conversions efficiently. The `chr()` function converts an integer (representing the Unicode code point) into its character string.

```bash
# Executing Python 3 in the webshell
python3

# Inside the Python interpreter
>>> print(chr(0x70))
'p'
```
### Method 2: Manual Calculation
To convert Hex `0x70` to Decimal:
- $7 \times 16^1 + 0 \times 16^0 = 112$
- Looking up **112** in a standard ASCII table confirms it corresponds to the character **'p'**.

---

### 4. Key Functions Learned
| Function | Description | Example |
| :--- | :--- | :--- |
| `chr(x)` | Converts an integer/hex to its ASCII character | `chr(0x70)` -> `'p'` |
| `ord(c)` | Converts an ASCII character to its decimal integer | `ord('p')` -> `112` |
| `hex(n)` | Converts an integer to a hexadecimal string | `hex(112)` -> `'0x70'` |

---

### 5. Conclusion
The flag for this challenge is found by identifying that 0x70 translates to p.

Flag: picoCTF{p}
