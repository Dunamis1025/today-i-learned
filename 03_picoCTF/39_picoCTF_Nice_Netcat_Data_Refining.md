# picoCTF: Nice netcat... (General Skills)

## 1. Problem Overview
- **Objective**: Connect to a remote server using a specific network tool and interpret the output to find the hidden flag.
- **Challenge**: The server outputs a sequence of decimal numbers (ASCII codes) rather than human-readable text.
- **Tool used**: `nc` (netcat)

## 2. Technical Analysis
Upon connecting to the server via `nc wily-courier.picoctf.net 52860`, the terminal displayed a vertical list of decimal values:
```text
112
105
99
111
67
84
70
...
```

These values represent the ASCII (American Standard Code for Information Interchange) encoding for characters. To retrieve the flag, these numbers must be converted from Decimal to ASCII characters.

## 3. Solution Strategy
Approach 1: Python Scripting (Most Reliable)
The most efficient way to handle this data is using a Python "one-liner." This method is superior because Python's .split() method automatically handles various whitespace and control characters like \n (Line Feed) or \r (Carriage Return).

Command:
```bash
python3 -c "n='[YOUR_DECIMAL_LIST]'; print(''.join([chr(int(i)) for i in n.split()]))"
```
Code Breakdown:

- python3 -c: Executes the provided string as a Python command without creating a .py file.

- ;: Separates multiple Python statements on a single line.

- n.split(): Splits the raw string into a list of individual numeric strings, ignoring newlines or carriage returns.

- int(i): Converts each string (e.g., '112') into an integer.

- chr(): Converts the integer back into its corresponding ASCII character (e.g., 112 -> 'p').

- ''.join(...): Merges the list of individual characters into one continuous string.


Approach 2: CyberChef (Data Refining)
While using CyberChef's "From Decimal" module, we encountered issues due to hidden CR (Carriage Return) characters.

- Problem: Hidden \r symbols attached to the numbers caused the conversion to fail.

- Solution:

1. Use the Find / Replace module with REGEX enabled to find \r and replace it with nothing.

2. Alternatively, use Remove whitespace to clean the data before conversion.

## 4. Key Takeaways & Lessons Learned
1. The Power of Netcat: Learned how to interact with remote services and receive raw data streams.

2. Data Cleansing: Realized that invisible control characters (CR/LF) can break data processing tools. Learning to "clean" data using REGEX or Python is a vital skill in cybersecurity.

3. ASCII Representation: Reconfirmed that everything in computing is fundamentally numeric; understanding how characters are mapped (Decimal, Hex, Binary) is crucial for CTF challenges.

## 5. Final Flag
picoCTF{g00d_k1tty!_n1c3_k1tty!_d5d88}
