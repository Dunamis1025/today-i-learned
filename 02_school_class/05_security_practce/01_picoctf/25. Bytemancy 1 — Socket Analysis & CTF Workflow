# 25. Bytemancy 1 — Socket Analysis & CTF Workflow

**Date:** 2026-04-11 (3AM study session, day before school CTF)
**Source:** picoCTF 2026 — General Skills / Easy
**Challenge:** bytemancy 1

---

## What the Challenge Asked

The server said:
> "Send me ASCII DECIMAL 101 1751 times, side-by-side, no space."

- ASCII DECIMAL 101 = `e`
- So the answer was `e` repeated 1751 times: `eeeee...e`

The source code confirmed it:
```python
if user_input == "\x65"*1751:
    print(open("./flag.txt", "r").read())
```
- `\x65` = hex for 101 = ASCII `e`
- If input matches → server prints the flag

**Flag:** `picoCTF{h0w_m4ny_e's???_be9356c0}`
- The `???` is part of the flag, not broken text

---

## How to Connect to a picoCTF Instance

1. Click **Launch Instance** on the challenge page
2. The site gives you the connection command, e.g.:
nc foggy-cliff.picoctf.net 59005
3. You don't memorize the address — the site tells you every time
4. Each challenge has a different address and port number

---

## What is `nc` (netcat)?

- A command-line tool to connect to a server and send/receive text
- Works on Linux/Mac by default
- **Not available on Windows PowerShell by default** → need an alternative

---

## What the Pipe `|` Does

```bash
python -c "print('e'*1751)" | nc foggy-cliff.picoctf.net 59005
```

- Left side: generates `eeeee...e` (1751 e's)
- `|` = take the output of the left, feed it as input to the right
- Right side: sends it to the server via netcat
- **Failed on Windows** because `nc` isn't installed

---

## Python Socket Solution (nc alternative for Windows)

Since `nc` wasn't available, we replaced it with Python's `socket` module:

```python
import socket
# Import the socket library — lets Python do what nc does

s = socket.socket()
# Create a socket object (like picking up a phone)

s.connect(('foggy-cliff.picoctf.net', 59005))
# Connect to the server at that address and port (like dialing)

print(s.recv(2048).decode())
# Receive the server's first message (up to 2048 bytes)
# .decode() converts bytes → readable text

s.sendall(('e'*1751+'\n').encode())
# Send 1751 e's to the server
# +'\n' = newline (like pressing Enter) — server needs this to know input is done
# .encode() converts text → bytes (required for sending)

print(s.recv(2048).decode())
# Receive the server's response = the flag
```

---

## File Creation: Windows vs Linux/Mac

| Command | Works on | Purpose |
|---|---|---|
| `echo. > solve.py` | Linux/Mac | Create an empty file |
| `New-Item solve.py` | PowerShell | Create an empty file |

`echo.` failed because PowerShell doesn't recognize that syntax.

**Easier method:** Just use VSCode → File → New File → save as `solve.py`

---

## Key Concepts Summary

| Concept | Plain explanation |
|---|---|
| `nc` / netcat | Tool to talk to a server from terminal |
| socket | Python's way of doing the same thing as nc |
| `\x65` | Hex notation → equals decimal 101 → equals `e` |
| `encode()` | Convert text to bytes (for sending) |
| `decode()` | Convert bytes to text (for reading) |
| `\n` | Newline = pressing Enter |
| pipe `\|` | Send output of one command as input to another |
| port number | Like a door number on a server (59005 here) |

---

## Lessons Learned

- Always read the challenge page carefully — the server address is given to you
- `???` in a flag is not broken text — it's literally part of the flag
- When a tool isn't available (nc on Windows), find an equivalent (Python socket)
- Write the solution as a `.py` file, not one-liners in terminal — easier to debug
- Understanding *why* the code works matters more than just running it
