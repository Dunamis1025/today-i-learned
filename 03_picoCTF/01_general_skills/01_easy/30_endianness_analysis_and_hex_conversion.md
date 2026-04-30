## 2026-04-15 | picoCTF - General Skills: endianness

### Challenge Description
- **Problem**: Understanding the difference between Little Endian and Big Endian byte orders.
- **Task**: Convert a given string into its Hexadecimal representation and then provide both Little Endian and Big Endian formats.

### Key Concepts
- **Big Endian**: The most significant byte is stored at the smallest memory address (human-readable order).
- **Little Endian**: The least significant byte is stored at the smallest memory address (reversed byte order).

### Solving Process
1. **Target Word**: `atvas`
2. **ASCII to Hex Conversion**:
   - `a` -> `61`
   - `t` -> `74`
   - `v` -> `76`
   - `a` -> `61`
   - `s` -> `73`
3. **Big Endian Representation**: `6174766173`
4. **Little Endian Representation**: `7361767461` (Bytes reversed)

### Outcome
- **Flag**: `picoCTF{3ndi4n_sw4p_su33ess_817b7cfe}`
- **Lesson**: Modern x86-64 systems typically use Little Endian. Understanding how data is structured in memory is crucial for exploit development and forensics.
