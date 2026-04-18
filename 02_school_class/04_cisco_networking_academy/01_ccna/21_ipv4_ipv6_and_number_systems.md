# [TIL] IPv4, IPv6, and Number System Conversions

## 1. IPv4 Addressing and Binary System
Computers and network devices communicate using **Binary (Base 2)**, while humans use **Decimal (Base 10)**. Understanding the relationship between these two is fundamental to networking.

### IPv4 Structure
- **Length**: 32-bit address.
- **Format**: Dotted Decimal Notation (e.g., `192.168.10.10`).
- **Octet**: Each 8-bit section is called an octet.

| Notation | Example |
| :--- | :--- |
| **Dotted Decimal** | 192 . 168 . 10 . 10 |
| **Binary (32-bit)** | 11000000 . 10101000 . 00001010 . 00001010 |

---

## 2. IPv6 and Hexadecimal System
IPv6 uses **Hexadecimal (Base 16)** to represent its 128-bit address space efficiently.

### Characteristics of Hexadecimal
- **Symbols**: 0-9 and A-F (where A=10, B=11, C=12, D=13, E=14, F=15).
- **Case Sensitivity**: Not case-sensitive (e.g., `0xFF` is the same as `0xff`).
- **Relationship with Binary**: One hexadecimal digit represents exactly **4 bits** (a nibble).

### IPv6 Structure
- **Hextet**: The unofficial term for a 16-bit segment (4 hex digits).
- **Format**: `x:x:x:x:x:x:x:x` (8 hextets).
- **Total Length**: 128 bits (32 hex digits).

---

## 3. Number System Conversion Processes

### A. Decimal to Hexadecimal
1. **Decimal to 8-bit Binary**: Convert the decimal number (e.g., 168) into binary.
   - $168 = 10101000_2$
2. **Split into Groups**: Divide the 8-bit binary into two 4-bit groups.
   - `1010` | `1000`
3. **Convert to Hex**: Map each 4-bit group to its hex equivalent.
   - `1010` = 10 = **A**
   - `1000` = 8 = **8**
   - **Result**: $168_{10} = \text{A}8_{16}$

### B. Hexadecimal to Decimal
1. **Hex to 4-bit Binary**: Convert each hex digit into binary.
   - D2 $\rightarrow$ D (13) = `1101`, 2 = `0010`
2. **Combine to 8-bit**: Merge the groups.
   - `11010010`
3. **Binary to Decimal**: Calculate the weighted sum.
   - $128+64+16+2 = 210$
   - **Result**: $\text{D}2_{16} = 210_{10}$

---

## 4. Key Comparison Summary

| Feature | IPv4 | IPv6 |
| :--- | :--- | :--- |
| **Address Length** | 32 bits | 128 bits |
| **Notation** | Dotted Decimal | Hexadecimal |
| **Separator** | Period (.) | Colon (:) |
| **Unit Name** | Octet (8 bits) | Hextet (16 bits) |

---
**Course**: Cisco Networking Academy - CCNA  
**Topic**: 5.1 IPv4 Addresses / 5.2 Hexadecimal and IPv6 Addresses  
**Date**: 2026-04-18
