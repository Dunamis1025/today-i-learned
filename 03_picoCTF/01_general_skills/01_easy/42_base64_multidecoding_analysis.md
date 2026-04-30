# [picoCTF] repetitions - Challenge Write-up

## 1. Challenge Overview
- **Name:** repetitions
- **Category:** General Skills
- **Points:** 100
- **Concepts:** Base64 Encoding, Multi-layered Decoding, Data Representation

## 2. Problem Description
The challenge provides a file named `enc_flag` which contains a string of characters that appear to be encoded. The hint suggests that "Multiple decoding is always good," implying that the data has been passed through the same encoding process several times.

## 3. Analysis & Identification
Upon opening the file, the string ends with `==`, a classic signature of **Base64** encoding. Base64 uses 64 printable characters (A-Z, a-z, 0-9, +, /) to represent binary data. The presence of padding (`=`) confirms the necessity of Base64 decoding.


## 4. Solution Approaches

### Method A: Using CyberChef (GUI Based)
CyberChef is an excellent tool for rapid prototyping of decoding recipes.
1. **Input:** Paste the encoded string from `enc_flag`.
2. **Recipe:** Search for the **"From Base64"** operation.
3. **Execution:** Drag the operation into the recipe area. Since the hint mentions "Multiple," continue adding "From Base64" steps or use the "Magic" tool until the output follows the flag format: `picoCTF{...}`.
4. **Result:** In this specific case, the decoding process had to be repeated **6 times** to reveal the final flag.

### Method B: Using Linux Terminal (CLI Based)
For better automation and efficiency, the Linux command line is preferred. We can use the pipe (`|`) operator to pass the output of one decoding process into the next.

```bash
# Displaying the content of the file
cat enc_flag

# Performing multi-layer decoding using the 'base64' command
# The -d (or --decode) flag is used to transform base64 back to plain text
cat enc_flag | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d

# Alternative: Using a simple loop if the number of repetitions is unknown
# (Manual repetition is often faster for small counts like this)

```

## 5. Conclusion & Key Takeaways
Data Obfuscation: Multiple layers of encoding do not provide security, only obfuscation.

Pattern Recognition: Identifying padding characters like = is crucial for determining the encoding type quickly.

Tool Versatility: Both GUI tools like CyberChef and CLI commands like base64 -d are essential parts of a cybersecurity professional's toolkit.

## 6. Captured Flag
picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_de523f49}
