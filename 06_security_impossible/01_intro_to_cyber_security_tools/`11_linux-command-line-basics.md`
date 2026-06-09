# Linux Command Line Basics — Study Notes
> Security Impossible Cyber Range Lab Summary

---

## What is Linux?
- An open-source operating system widely used in servers, cloud environments, and cybersecurity
- Most security tools (e.g. Kali Linux) are built for Linux
- Gives fine-grained control over permissions, networking, and system behaviour

## What is the Command Line?
- A text-based interface to interact with the system by typing commands (instead of clicking)
- Also called the **terminal** or **shell**
- Essential for managing servers, automating tasks, and running security tools

---

## Important Rules to Remember
| Rule | Detail |
|---|---|
| Case-sensitive | `File.txt` and `file.txt` are different files |
| Exact commands | Even one typo causes an error |
| Spaces matter | Use quotes or `\` for filenames with spaces: `ls "file name.txt"` |
| Everything is a file | Directories, devices, and processes are all treated as files |
| Permissions control access | Not all files can be read/modified without correct permissions |
| Use help when unsure | `man <command>` or `<command> --help` |

---

## Core Commands

### Navigation
| Command | Meaning | Example |
|---|---|---|
| `pwd` | Print Working Directory — show current location | `pwd` → `/home/analyst` |
| `ls` | List files in current directory | `ls` |
| `ls -l` | Long listing — shows permissions, size, date | `ls -l` |
| `ls -a` | List ALL files including hidden ones (starting with `.`) | `ls -a` |
| `cd <dir>` | Change Directory — move into a folder | `cd Documents` |
| `cd ~` | Go back to home directory (`~` = home shortcut) | `cd ~` |
| `cd ..` | Go up one level to parent directory | `cd ..` |

### Reading Files
| Command | Meaning | Example |
|---|---|---|
| `cat <file>` | Display file contents | `cat notes.txt` |
| `less <file>` | Read file one page at a time (Space = next, q = quit) | `less /var/log/auth.log` |
| `tail <file>` | Show the last 10 lines of a file (most recent entries) | `tail /var/log/auth.log` |
| `nano <file>` | Open file in nano text editor (like Notepad in terminal) | `nano message.txt` |

> **Nano shortcuts:** `Ctrl+X` to exit → `Y` to save → `Enter` to confirm filename

### Finding Files
| Command | Meaning | Example |
|---|---|---|
| `find ~ -name "file.txt"` | Search for a file by name starting from home directory | `find ~ -name "message.txt"` |

### Copying & Moving Files
| Command | Meaning | Example |
|---|---|---|
| `cp <source> <dest>` | Copy a file to a new location | `cp /home/analyst/.backup/message.txt ~` |

### Searching Inside Files
| Command | Meaning | Example |
|---|---|---|
| `grep "word" <file>` | Find lines containing a specific word | `grep "Failed" /var/log/auth.log` |

### System Information
| Command | Meaning | Example |
|---|---|---|
| `whoami` | Show current username | `whoami` → `analyst` |
| `hostname` | Show the machine's name | `hostname` → `LinuxCLIBasics` |
| `ip a` | Show network interface info including IP address | `ip a` |
| `history` | Show list of previously run commands | `history` |

### Permissions & Privileges
| Command | Meaning | Example |
|---|---|---|
| `ls -l <path>` | Show file permissions | `ls -l /opt/company/` |
| `sudo <command>` | Run a command as administrator (root) | `sudo cat /opt/company/credentials.txt` |

---

## Understanding File Permissions

```
-rw------- 1 root root 18 Apr 20 06:18 credentials.txt
```

| Symbol | Meaning |
|---|---|
| `-` | It's a file (`d` = directory) |
| `rw-------` | Owner can read & write; group and others have no access |
| `root root` | Owner: root, Group: root |
| `r` | read |
| `w` | write |
| `x` | execute |

**Permission groups (in order):** Owner → Group → Others

---

## Understanding Network Interfaces (`ip a`)

When you run `ip a`, you typically see multiple interfaces:

| Interface | What it is |
|---|---|
| `lo` (loopback) | Virtual interface for the computer to talk to itself. IP is always `127.0.0.1` |
| `eth0` | The real network interface connected to the outside network. This holds your actual IP address |
| `docker0` | A virtual network created by Docker for containers to communicate internally |

**Your IP address** = the number after `inet` in the `eth0` section
> Example: `inet 10.100.0.11/24` → IP address is `10.100.0.11`

---

## Reading Log Files

Log files record everything that happens on the system. The main auth log is at:
```
/var/log/auth.log
```

### How to read a log line:
```
Jun 9 00:04:04   LinuxCLIBasics   sshd[1738]:   Accepted password for analyst from 10.1.0.5
    ↑                 ↑               ↑                        ↑
 Date/Time       Hostname        Program name              What happened
```

### What to look for:
| Log entry | What it means |
|---|---|
| `Accepted password for analyst from <IP>` | Successful login — normal |
| `Failed password for root from <IP>` | Failed login attempt — suspicious! |
| `CRON` entries | Scheduled automatic tasks — normal |
| Multiple `Failed password` from same IP | Possible **brute force attack** |

### Key commands for log analysis:
```bash
cat /var/log/auth.log          # View the full log
less /var/log/auth.log         # Read page by page
tail /var/log/auth.log         # See only the most recent entries
grep "Failed" /var/log/auth.log  # Filter only failed login lines
```

---

## Hidden Files

- Hidden files start with a dot (`.`), e.g. `.hidden.txt`, `.backup/`
- `ls` does **not** show them — you must use `ls -a`
- Read them exactly like normal files: `cat .hidden.txt`

---

## Lab Tasks Summary

| Task | What you did | Commands used |
|---|---|---|
| Task 1 | Explored home directory | `pwd`, `ls`, `ls -l`, `cd`, `cd ~` |
| Task 2 | Identified the system on the network | `whoami`, `hostname`, `ip a` |
| Task 3 | Read internal notes | `cat notes.txt` |
| Task 4 | Found and read task file | `cd work`, `cat tasks.txt` |
| Task 5 | Found hidden files | `ls -a`, `cat .hidden.txt` |
| Task 6 | Located and edited a hidden message | `find`, `cp`, `nano` |
| Task 7 | Investigated system logs | `cat`, `less`, `tail`, `grep`, `history` |
| Task 8 | Checked file permissions | `ls -l`, `cat` (Permission denied), `sudo cat` |

---

## Key Takeaways

- The Linux command line is essential for IT and cybersecurity professionals
- You can navigate, read, search, and edit files entirely without a mouse
- Log files are critical for detecting suspicious activity (e.g. brute force login attempts)
- File permissions control who can access sensitive data — always verify them
- `sudo` gives administrator-level access — use with caution
- Hidden files (`.filename`) require `ls -a` to be visible
- Built-in help is always available: `man <command>` or `<command> --help`
