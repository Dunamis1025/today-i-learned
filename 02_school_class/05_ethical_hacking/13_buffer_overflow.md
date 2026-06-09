# Lab 13: Understanding Buffer Overflows — Study Notes

## What is a Buffer Overflow?

A **buffer overflow** occurs when a program writes more data into a buffer (temporary memory storage) than it was allocated to hold. Think of it like pouring 9 cups of water into a container that only fits 8 — it spills over into adjacent memory space.

This is one of the most classic and dangerous vulnerabilities in software security. Real-world exploits like the **Morris Worm (1988)** and **Heartbleed** leveraged this exact principle.

---

## How It Works (Memory Perspective)

```
Buffer slots:  [0][1][2][3][4][5][6][7]   ← only 8 slots allocated
Overflow:                              [8] ← belongs to OTHER memory!
```

When data is written beyond index 7:
- It **overwrites adjacent memory** (other variables, return addresses, etc.)
- An attacker can place **malicious code addresses** in that overflowed space
- The program then **executes the attacker's code** instead of its own

---

## The Vulnerable Program — `vuln1.c`

```c
#include<stdio.h>

int main(){

int i;
int buffer[8];   // only 8 slots!
int num;

printf("\nEnter number of integers:");
scanf("%d", &num);   // no validation — accepts ANY number!

printf("\nEnter the values :");
for (i = 0; i < num; i++){
    scanf("%d", &buffer[i]);   // keeps writing even past slot 8
}

for (i = 0; i < num; i++){
    printf("\nbuffer[%d] = %d", i, buffer[i]);
}

return (0);
}
```

### Why is this vulnerable?
- `buffer[8]` allocates exactly **8 integer slots (index 0–7)**
- `scanf("%d", &num)` accepts user input **without any size check**
- If user enters `9`, the loop writes to `buffer[8]` — **outside allocated memory**

### Demonstrated Attack
```
Input:  num = 9
Values: 1 2 3 4 5 6 7 8 9

Output:
buffer[0] = 1
buffer[1] = 2
...
buffer[7] = 8
buffer[8] = 9  ← OVERFLOW! This memory doesn't belong to buffer
```

---

## The Fixed Program — `fixed_vuln1.c`

```c
#include<stdio.h>
#include <stdlib.h>   // needed for exit()

int main(){

int i;
int buffer[8];
int num;

printf("\nEnter number of integers:");
scanf("%d", &num);

// INPUT VALIDATION — the key fix!
if (num > 8){
    printf("You entered a value greater than allowed!\n");
    exit(0);   // terminate immediately
}

printf("\nEnter the values :");
for (i = 0; i < num; i++){
    scanf("%d", &buffer[i]);
}

for (i = 0; i < num; i++){
    printf("\nbuffer[%d] = %d", i, buffer[i]);
}

return (0);
}
```

### What changed?

| | `vuln1.c` | `fixed_vuln1.c` |
|---|---|---|
| Input validation | None | `if (num > 8)` check |
| Overflow possible | Yes | Blocked |
| On input of 9 | Writes to out-of-bounds memory | Prints error & exits |

### Demonstrated Defense
```
Input:  num = 9

Output:
"You entered a value greater than allowed!"
← Program exits immediately. No overflow possible.
```

---

## Key Concepts

### Compiler
A **compiler** translates human-readable source code into machine-executable binary.
```
vuln1.c  →  [gcc compiler]  →  vuln1 (executable)
```
Command used:
```bash
gcc vuln1.c -o vuln1
gcc fixed_vuln1.c -o fixed_vuln1
```

### Buffer
A **buffer** is a fixed-size temporary storage area in memory. In C, arrays like `int buffer[8]` allocate a fixed number of slots. C does **not** automatically check boundaries — the programmer is responsible.

### Why C is Especially Vulnerable
- C gives direct access to memory
- No built-in bounds checking on arrays
- `scanf()` without validation is a classic attack vector

---

## Core Security Lesson

> **Always validate user input before using it.**

The root cause of buffer overflows is **trusting user input without verification**. The single most effective defense is checking that input stays within expected bounds before processing it.

### Defense Strategies (Beyond This Lab)
- **Input validation** — check size before accepting data
- **Safe functions** — use `fgets()` instead of `gets()`, `strncpy()` instead of `strcpy()`
- **Compiler protections** — stack canaries, ASLR (Address Space Layout Randomization)
- **Modern languages** — Java, Python handle bounds checking automatically

---

## Lab Environment
- **OS:** Kali Linux (security-focused Linux distro)
- **Language:** C
- **Tool:** gcc compiler, Mousepad text editor
- **Credentials:** `root` / `toor`

---

## Relevance to Certifications
| Certification | Related Domain |
|---|---|
| CEH v10 | Module 13–15: Web Servers, Web Apps, SQL Injection |
| CompTIA PenTest+ | 4.4: Script Analysis (Bash, Python, Ruby, PowerShell) |
