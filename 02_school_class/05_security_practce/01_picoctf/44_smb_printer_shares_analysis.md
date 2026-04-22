# 44. SMB Protocol & Printer Shares — picoCTF 2026

## Challenge Overview

| Field       | Details                          |
|-------------|----------------------------------|
| Name        | Printer Shares                   |
| Category    | General Skills                   |
| Difficulty  | Easy                             |
| Event       | picoCTF 2026                     |
| Solves      | 4,646                            |
| Liked       | 98%                              |

**Description:**
> "Oops! Someone accidentally sent an important file to a network printer — can you retrieve it from the print server?"

**Hints given:**
1. Knowing how SMB protocol works would be helpful
2. `smbclient` and `smbutil` are good tools

---

## Concepts Learned

### 1. What is SMB?

**SMB (Server Message Block)** is a network protocol that allows computers to share files, folders, and printers over a network.

- Originally developed by IBM in the 1980s
- Widely used in Windows environments (e.g., mapped network drives, shared folders)
- Allows a user sitting at their own computer to open and interact with folders on a **remote computer** — as if those folders were local
- Typically used within the **same local network** (school, office, home), but can technically work over the internet if the server allows it
- External SMB access is usually **blocked for security reasons** — this CTF challenge intentionally left it open

**Real-world analogy:**
> You're at your desk at school. Without leaving your seat, you can open a folder that physically lives on the teacher's computer in another room — because both computers are connected to the same school network. That's SMB.

---

### 2. What is IPC?

**IPC (InterProcess Communication)** is a mechanism that allows programs and processes to communicate with each other.

- Not used for storing or sharing files
- Used for system-level signaling: "Are you there?", "Connection established?", etc.
- In the context of SMB, **IPC$** is a special hidden share automatically created by Windows/Samba

---

### 3. What is IPC$?

- `IPC$` is a **hidden system share** automatically created by the OS
- The `$` suffix means it is hidden and system-reserved
- It is used for inter-process communication between the server and client during SMB sessions
- **Contains no user files** — attempting to browse it returns `NT_STATUS_CONNECTION_REFUSED`
- Should be ignored when looking for actual data

---

### 4. How to identify the right share

When running `smbclient -L`, the output looks like this:

```
Sharename    Type    Comment
---------    ----    -------
shares       Disk    Public Share With Guests
IPC$         IPC     IPC Service
```

**Key rule: Only connect to shares with `Type = Disk`**

| Type | Meaning               | Contains files? |
|------|-----------------------|-----------------|
| Disk | Actual shared folder  | ✅ Yes           |
| IPC  | System communication  | ❌ No            |

---

## Tools Used

### `nc` (netcat) — Connection Test
```bash
nc -vz mysterious-sea.picoctf.net 49573
```
- `-v` : verbose output
- `-z` : just check if port is open, don't send data
- Used to verify the server is reachable before attempting SMB connection

---

### `smbclient` — SMB Client Tool

**List all available shares:**
```bash
smbclient -L //mysterious-sea.picoctf.net -p 49573 -N
```
- `-L` : list shares on the server
- `-p 49573` : specify port number
- `-N` : no password (anonymous/guest access)

**Connect to a specific share:**
```bash
smbclient //mysterious-sea.picoctf.net/shares -p 49573 -N
```

**Commands inside the SMB shell (`smb: \>`):**
```
ls              → list files in current directory
get flag.txt    → download flag.txt to current local directory
exit            → leave SMB shell and return to normal terminal
```

> ⚠️ Important: You cannot run new terminal commands (like `smbclient`) while inside the SMB shell (`smb: \>`). You must type `exit` first to return to the regular shell (`$`).

---

## Step-by-Step Solution

```bash
# Step 1: Verify server is reachable
nc -vz mysterious-sea.picoctf.net 49573

# Step 2: List available shares
smbclient -L //mysterious-sea.picoctf.net -p 49573 -N
# → Found: shares (Disk), IPC$ (IPC)

# Step 3: Connect to the Disk share
smbclient //mysterious-sea.picoctf.net/shares -p 49573 -N

# Step 4: Inside SMB shell — list and download files
smb: \> ls
# → dummy.txt, flag.txt

smb: \> get flag.txt
smb: \> exit

# Step 5: Read the downloaded file
cat flag.txt
```

---

## Flag

```
picoCTF{5mb_pr1nter_5h4re5_51f37693}
```

---

## Key Takeaways

- **SMB = network file sharing protocol** (used in Windows shared folders)
- **IPC$ = system-only share, ignore it** — it has no files
- **Type: Disk = where actual files live** — always connect here
- `smbclient -L` to explore, then connect to the Disk share
- `get` downloads from the **remote server** to your **local current directory**
- Always `exit` the SMB shell before running new terminal commands
- The general CTF pattern: **Enumerate → Connect → Retrieve**
