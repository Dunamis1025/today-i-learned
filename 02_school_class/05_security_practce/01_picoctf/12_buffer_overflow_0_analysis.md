# [picoCTF] buffer overflow 0 - Binary Exploitation

## 1. Overview
* **Challenge Name:** buffer overflow 0
* **Category:** Binary Exploitation
* **Objective:** Understand the fundamental concept of memory corruption by overflowing a buffer to trigger a specific program behavior (printing the flag).

---

## 2. Key Concepts

### Binary Exploitation
A technique to find and exploit vulnerabilities in a compiled program (binary) to force it to perform unintended actions, such as bypassing authentication or leaking sensitive information.

### Compilation
The process of translating human-readable source code (like C) into machine-readable binary (0s and 1s) that a computer can execute.

### Buffer & Overflow
* **Buffer:** A temporary storage area in memory (like a fixed-size container) meant to hold data.
* **Overflow:** Occurs when more data is written to a buffer than it can hold. This extra data spills over into adjacent memory, potentially overwriting critical program control variables.

---

## 3. Code Analysis (`vuln.c`)

The program is intentionally vulnerable to demonstrate the danger of certain C functions.

### Vulnerability Points
1.  **`gets(buf1)`**: The `gets()` function does not check the length of the input, making it inherently insecure. It will keep reading data until it hits a newline character, regardless of the buffer size.
2.  **`strcpy(buf2, input)`**: In the `vuln` function, a 16-byte buffer (`buf2`) is used. If the `input` string is longer than 16 bytes, it overflows the memory.

### Flag Trigger Mechanism
* The program uses `signal(SIGSEGV, sigsegv_handler);`. This tells the OS: "If a **Segmentation Fault** (memory error) occurs, run the `sigsegv_handler` function."
* Inside `sigsegv_handler`, the code prints the flag: `printf("%s\n", flag);`.
* Therefore, the goal is to intentionally crash the program by overflowing the buffer.

---

## 4. Solution (Exploit)

1.  **Connect to Server**: Use the `nc` (Netcat) command to connect to the provided instance.
    ```bash
    nc saturn.picoctf.net [PORT]
    ```
2.  **Inject Payload**: When prompted for input, provide a string significantly longer than the buffer size (e.g., 100+ characters).
    * Example: `AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA`
3.  **Result**: The overflow causes a Segmentation Fault, the signal handler catches it, and the flag is printed to the terminal.

---

## 5. Lessons Learned
* **Security Best Practices**: Never use insecure functions like `gets()`. Modern alternatives like `fgets()` should be used to specify maximum input length.
* **Memory Management**: Understanding how the stack works and how adjacent memory can be affected by unvalidated input.
* **CTF Workflow**: Analyzing source code to find the "logical path" to the flag, even if it requires intentionally breaking the program.
