# [picoCTF] binhexa - Writeup

## Challenge Description
- **Category:** General Skills
- **Level:** Easy
- **Topic:** Binary operations and Hexadecimal conversion.
- **Task:** Perform a series of unique binary operations (Arithmetic and Bitwise) and provide the final result in hexadecimal format to retrieve the flag.

## Key Concepts

### 1. Binary Arithmetic
- **Multiplication (*):** Similar to decimal multiplication but using binary digits. Converting to decimal, multiplying, and converting back to binary is an efficient way to avoid mistakes.
- **Left Shift (<<):** Shifts bits to the left and fills the right side with `0`. Note that it increases the bit length (effectively multiplying the value by 2).

### 2. Bitwise Operations
- **AND (&):** Result is `1` only if both corresponding bits are `1`.
- **OR (|):** Result is `1` if at least one of the corresponding bits is `1`.
- **Right Shift (>>):** Shifts bits to the right and fills the left side with `0`, discarding the rightmost bit.

### 3. Hexadecimal Conversion
- Converting the final binary result to base-16. This is often required as the final answer in CTF challenges to get the flag.

## Step-by-Step Solution

### Challenge Data
- **Binary Number 1:** `10110101` (Decimal: 181)
- **Binary Number 2:** `00100001` (Decimal: 33)

### Operations
1. **Operation (+):** `10110101 + 00100001 = 11010110` (Correct)
2. **Operation (*):** `181 * 33 = 5973` -> `1011101010101`
3. **Operation (>> 1 bit on Binary 2):** `00100001 >> 1 = 00010000`
4. **Operation (|):** `10110101 | 00100001 = 10110101`
5. **Operation (&):** `10110101 & 00100001 = 00100001`
6. **Operation (<< 1 bit on Binary 1):** - Initial thought: `01101010` (8-bit limit) -> **Incorrect**
   - Correct approach: `10110101 << 1 = 101101010` (9-bit, Decimal 362)

### Final Step: Hexadecimal Conversion
- Final Result: `101101010` (362 in decimal)
- Conversion: `362` to Hex -> `16A`

**Flag:** Entered `16A` to receive the flag.
