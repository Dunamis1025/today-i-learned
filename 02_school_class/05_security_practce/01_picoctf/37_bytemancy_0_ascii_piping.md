# Today I Learned: Bytemancy 0 & Technical Communication via Pipes

## 1. Problem Overview
- **Challenge Name:** bytemancy 0
- **Category:** General Skills (picoCTF 2026)
- **Objective:** Establish a network connection and transmit specific ASCII data to retrieve a hidden flag.

## 2. Key Concepts Learned

### A. ASCII vs. Decimal Representation
- Computers process data in bytes, but humans interact with them via characters.
- **ASCII (American Standard Code for Information Interchange)** maps numbers to characters.
- In this challenge, the server requested **ASCII DECIMAL 101**.
- Referencing the ASCII table: **Decimal 101 = Character 'e'**.
- Sending `eee` (101, 101, 101) fulfills the requirement.

### B. Linux Command Line & Netcat (nc)
- **`nc` (Netcat):** A utility used for reading from and writing to network connections using TCP or UDP.
- **Syntax:** `nc [target_url] [port_number]`
- It acts as a "wormhole" between the local terminal and a remote server.

### C. The Power of the Pipe (`|`)
- The pipe operator takes the standard output (**stdout**) of one command and feeds it as the standard input (**stdin**) to the next.
- **Manual Input:** Connecting first with `nc`, then typing `eee`.
- **Automated Input (One-liner):** `echo "eee" | nc candy-mountain.picoctf.net 59569`
- This is crucial for sending non-printable bytes (like null bytes or memory addresses) that cannot be typed directly via a keyboard.

## 3. Practical Implementation

### Step 1: Connecting and Reading Requirements
```bash
nc candy-mountain.picoctf.net 59569
```

Output: Send me ASCII DECIMAL 101, 101, 101, side-by-side, no space.

### Step 2: Solving with a One-liner (Recommended for Efficiency)

```bash
echo "eee" | nc candy-mountain.picoctf.net 59569
```

## 4. Reflection on "Bytemancy"
The "hardware wall" of a keyboard limits us to human-readable characters. However, tools like echo, printf, and python combined with pipes allow us to bypass these physical limitations. This allows us to inject raw byte data directly into a system's memory or network socket—a fundamental skill in binary exploitation and cybersecurity.

## 5. Flag Captured
picoCTF{pr1n74813_ch4r5_9b465df3}
