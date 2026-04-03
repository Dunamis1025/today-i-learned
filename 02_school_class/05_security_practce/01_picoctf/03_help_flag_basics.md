# 03. CTF Help Flag Basics (Wave a flag)

## Overview

This note documents a beginner picoCTF challenge called "Wave a flag".

The key lesson is not about hacking techniques,
but about developing a fundamental habit in Linux and CTF:

Always check help flags when you encounter a new binary.

---

## Challenge Meaning

"Can you invoke help flags for a tool or binary?"

### Key Terms

invoke  
= activate / run / call a function or feature

help flags  
= command-line options such as -h or --help

### Interpretation

The challenge is asking:

"Can you run the program with help-related options to reveal hidden or useful information?"

In CTF context, this often means:
the flag may be hidden inside the help output.

---

## Core Idea of This Challenge

This challenge is designed to test a simple but powerful habit:

When you find a binary file:
1. Run it normally
2. Try common options (-h, --help)
3. Observe its behavior carefully

This is not advanced exploitation.
It is about awareness and curiosity.

---

## Step-by-Step Solution

### 1. Download the file

wget <URL>

Downloads the binary file from the challenge server.

---

### 2. Check the file

ls -l

Confirms that the file exists and shows its permissions.

---

### 3. Make it executable

chmod +x warm

Adds execution permission so the system allows running the file.

---

### 4. Run the program

./warm

Runs the program from the current directory.

Often, the program gives a hint such as:
"Try using the -h flag."

---

### 5. Run with help flag (IMPORTANT)

./warm -h
./warm --help

This is where the program usually reveals:
- usage information
- hidden messages
- sometimes directly the flag

---

## Key Linux Concepts

wget  
Download files from a URL

ls -l  
List files with detailed information

chmod +x  
Grant execute permission

./filename  
Execute a file in the current directory

-h / --help  
Standard options to display help information

---

## When Help Flags Do NOT Work

Not all programs follow standard conventions.

Try alternative inputs:

./warm -?
./warm help

Or move to deeper inspection techniques.

---

## Bonus Technique: Inspect Binary Content

strings warm | grep pico

### Breakdown

strings warm  
Extracts all readable text from the binary

| (pipe)  
Passes output to the next command

grep pico  
Filters lines containing "pico"

### Why This Works

Sometimes the flag is embedded directly inside the binary as plain text.
This method allows you to find it without executing the program.

---

## Key Commands Summary

wget <URL>
ls -l
chmod +x warm
./warm
./warm -h
./warm --help
strings warm | grep pico

---

## What I Learned

- Help flags are often the fastest way to understand a binary
- Many CTF challenges hide flags in help output
- Execution permission is required to run downloaded files
- Observing program output is critical
- Simple habits can solve problems without complex tools

---

## Final Insight

CTF is not always about advanced exploitation.

It is often about:

- reading hints carefully
- testing common options
- understanding basic tools
- thinking step by step

The real skill is not complexity,
but consistency in simple actions.
