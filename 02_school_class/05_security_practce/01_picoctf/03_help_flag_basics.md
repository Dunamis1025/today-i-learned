# 

## Overview

This note summarizes a beginner picoCTF challenge called "Wave a flag".

The main lesson is simple:
Always check help flags when you encounter a new binary.

---

## Challenge Meaning

"Can you invoke help flags for a tool or binary?"

- invoke = activate / run / call
- help flags = -h, --help

Meaning:
Run the program with help options to reveal useful information.

---

## Step-by-Step Solution

1. Download the file

wget <URL>

2. Check the file

ls -l

3. Make it executable

chmod +x warm

4. Run the program

./warm

5. Run with help flag (IMPORTANT)

./warm -h
./warm --help

This is where the flag is usually revealed.

---

## Key Linux Concepts

wget  
Downloads a file from the internet

ls -l  
Lists files with details

chmod +x  
Gives execution permission

./filename  
Runs a file in the current directory

-h / --help  
Shows help information for a program

---

## If -h does NOT work

Try alternative options:

./warm -?
./warm help

---

## Bonus Technique (Very Important)

strings warm | grep pico

Explanation:

strings warm  
Extracts readable text from the binary

|  
Pipe (sends output to another command)

grep pico  
Searches for lines containing "pico"

This can reveal the flag without running the program.

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

- Always try help flags first (-h, --help)
- Binaries may hide useful information in help output
- chmod +x is required to execute files
- ./ runs a file in the current directory
- strings can reveal hidden text inside binaries
- Simple habits solve simple CTF challenges

---

## Final Insight

CTF is not always about complex hacking.

It is often about:

- reading carefully
- following hints
- trying basic commands
- testing common flags

Small habits = big results
