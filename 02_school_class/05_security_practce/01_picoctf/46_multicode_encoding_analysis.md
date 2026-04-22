# 46. MultiCode Challenge & Encoding Analysis

## 1. Challenge Overview — picoCTF MultiCode

- **Category:** General Skills
- **Difficulty:** Easy
- **Platform:** picoCTF 2026 (picoGym)

### Description
> "We intercepted a suspiciously encoded message, but it's clearly hiding a flag. No encryption, just multiple layers of obfuscation. Can you peel back the layers and reveal the truth?"

### Hints
1. The flag has been wrapped in several layers of common encodings such as ROT13, URL encoding, Hex, and Base64. Can you figure out the order to peel them back?
2. A tool like CyberChef can be interesting.

---

## 2. Solution

### Tool Used
**CyberChef** — https://gchq.github.io/CyberChef/

### Decoding Order (Recipe)
The key insight is reading the *shape* of the data at each step to determine the next decoding method.

| Step | Operation | How to Identify |
|------|-----------|-----------------|
| 1 | **From Base64** | Input ends with `=`, uses only `A-Z a-z 0-9 + /` |
| 2 | **From Hex** | Output looks like `4e 6a 4d 33...`, only `0-9 a-f` chars |
| 3 | **URL Decode** | Output contains `%xx` patterns like `%2F`, `%3D` |
| 4 | **ROT13** | Output is unreadable alphabet — shift by 13 to reveal |

### Flag
```
picoCTF{nested_enc0ding_f3a24f73}
```

### Detective Approach
Rather than guessing randomly, each encoding has a **visual fingerprint**:
- `=` padding at the end → Base64
- Only hex digits in pairs → Hex
- `%` followed by two hex digits → URL encoding
- Readable-ish but meaningless alphabet → ROT13

CyberChef's **Magic** operation can also auto-detect encodings when stuck.

---

## 3. Encoding Deep Dive

### 3.1 Base64

**Name origin:** Uses exactly **64 characters** to represent data.

- Raw data is converted to binary, then split into **6-bit chunks**
- 6 bits = 2⁶ = **64 possible values** → mapped to `A-Z`, `a-z`, `0-9`, `+`, `/`
- `=` is used as **padding** to make the length a multiple of 4
- "Base" refers to the numeral base, just like Base10 (decimal) or Base16 (hex)

```
Binary: 010011 010011 ...
         ↓
Characters: T  S  ...  (with = padding at end)
```

### 3.2 URL Encoding / URL Decode

**Name origin:** Encoding scheme designed specifically for safe use in **URLs (web addresses)**.

URLs were designed when only ASCII characters were standard. Characters like spaces, Korean, or special symbols cannot be transmitted directly in a URL.

**How it works:**
- Each unsafe character is converted to its UTF-8 byte values
- Each byte is represented as `%` + two hex digits

```
"안녕" → %EC%95%88%EB%85%95
" " (space) → %20
"=" → %3D
```

**URL Decode** simply reverses this transformation.

### 3.3 ROT13

**Name origin:** **ROT**ate by **13** — shifts every alphabet letter 13 positions forward.

```
A → N
B → O
...
M → Z
N → A  (wraps around)
```

- Since the English alphabet has **26 letters**, applying ROT13 **twice** returns the original text
- This means **encoding = decoding** (same operation both ways)
- Derived from the ancient **Caesar cipher** (which used a shift of 3)
- Offers no real security — purely obfuscation

---

## 4. ASCII — Name & Origin

**ASCII = American Standard Code for Information Interchange**

| Word | Meaning |
|------|---------|
| American Standard | Standardized in the USA |
| Code | A lookup table mapping characters to numbers |
| for Information Interchange | For exchanging data between computers |

- Created in the **early 1960s** so computers could agree on how to represent text
- Covers **128 characters**: English letters, digits, punctuation, control characters
- Example: `A` = 65, `B` = 66, `space` = 32

ASCII was sufficient for English but could not represent characters from other languages — which led to Unicode and UTF-8.

---

## 5. UTF-8 — Name & Origin

**UTF-8 = Unicode Transformation Format — 8-bit**

### Unicode
- **Uni** = Universal (one unified standard)
- **Code** = character code table
- Goal: represent **every character from every language in the world** in one standard
- Maintained by the **Unicode Consortium** — an international organization
- Currently covers **140,000+ characters** including Korean, Chinese, Arabic, ancient scripts, and emoji

### Transformation Format
The method by which Unicode code points are encoded into actual bytes for storage and transmission.

### 8-bit
- Data is processed in **8-bit (1 byte)** units
- **Variable length encoding:**
  - Simple characters (ASCII-compatible): **1 byte**
  - Most European/Middle Eastern scripts: **2 bytes**
  - Korean, Chinese, Japanese: **3 bytes**
  - Rare/ancient scripts, emoji: **4 bytes**

### UTF-8 vs ASCII

| | ASCII | UTF-8 |
|--|-------|-------|
| Origin | USA, 1963 | International, 1992 |
| Characters | 128 (English only) | 140,000+ (all languages) |
| Size | Fixed 1 byte | Variable 1–4 bytes |
| ASCII compatible | — | ✅ Fully compatible |
| Web usage | Legacy | ~98% of the internet |

### Who Created UTF-8?
**Ken Thompson** and **Rob Pike** in **1992**, both from **Bell Labs**.

- **Ken Thompson** — co-creator of **Unix** and the **C language**
- **Rob Pike** — later co-created the **Go language** at Google

Legend has it they sketched the initial design **on a restaurant napkin** and had a working implementation within just **a few days**. 🤯

### Why UTF-8 Won
It is backward-compatible with ASCII — any valid ASCII text is also valid UTF-8. This made adoption easy without breaking existing systems.

---

## 6. How the 140,000+ Unicode Characters Were Defined

- **Not by one person** — the Unicode Consortium organizes contributions from worldwide experts
- Each country submits its own script/characters
- Historians and linguists contribute ancient/extinct scripts
- Emoji are proposed by companies (Apple, Google, etc.) and approved by **community vote**
- The standard is still **actively growing** — new emoji and scripts are added regularly

---

## Key Takeaways

1. Encoding ≠ Encryption — Base64, Hex, URL encoding, and ROT13 are **obfuscation only**, no key needed to reverse
2. Each encoding has a **visual fingerprint** — learn to recognize them by sight
3. **CyberChef** is the go-to tool for chaining multiple decode operations
4. ASCII → Unicode → UTF-8 is the natural evolution of text encoding to support global languages
5. UTF-8's variable-width design and ASCII compatibility made it the dominant encoding standard on the web
