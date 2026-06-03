# Netcat (nc) Lab — Study Notes

> **Topic:** Network fundamentals using Netcat | **Tool:** Tmux + Netcat + Docker  
> **Goal:** Understand TCP communication, file transfer, port scanning, and banner grabbing hands-on.

---

## 1. Environment Setup — Tmux

**Tmux** is a terminal multiplexer that lets you manage multiple terminal sessions in one window.

### Key Commands

| Action | Shortcut |
|---|---|
| Create a new window | `Ctrl+b` → `c` |
| Move to next window | `Ctrl+b` → `n` |
| Move to previous window | `Ctrl+b` → `p` |
| Jump to window #N | `Ctrl+b` → `0/1/2...` |
| Split screen vertically | `Ctrl+b` → `%` |
| List all windows | `Ctrl+b` → `w` |
| Close current window | `Ctrl+d` or `exit` |

### What is `bash`?
The label `bash` in the status bar means the window is idle — ready to accept shell commands. It is the **command interpreter** that reads your input and executes it.

### Reading the Status Bar
```
0:bash-    1:nc-    2:bash*
```
- `*` = the window you are currently viewing
- `-` = a background window (a process may still be running)
- `nc` = Netcat is actively running in that window

---

## 2. TCP Communication — Netcat Listener & Client

Netcat (`nc`) is a lightweight networking tool for reading and writing data over TCP/UDP connections.

### Setup: Two windows acting as server and client

**Window 1 — Listener (Server)**
```bash
nc -lvp 4444
```
| Flag | Meaning |
|---|---|
| `-l` | Listen mode — wait for incoming connections |
| `-v` | Verbose — show connection details |
| `-p` | Specify port number |

**Window 2 — Client**
```bash
nc <target-ip> 4444
```
- Connects to the listener on port 4444
- Once connected, anything typed in one window appears in the other — like a raw chat session over TCP

### How to find your IP
```bash
ip a
```
Look for the IP address under your active network interface (e.g., `10.100.0.10`).

### Verify connection
Switch back to the listener window (`Ctrl+b` → `p`) and confirm you see:
```
Connection received on ...
```

---

## 3. File Transfer over TCP

Instead of sending text messages, Netcat can pipe file contents through the connection.

**Step 1 — Create a file to send (Window 0)**
```bash
echo "This is a Netcat file transfer test" > sample.txt
```

**Step 2 — Set up the receiver (Window 1)**
```bash
nc -lvp 5555 > received.txt
```
- `>` redirects incoming data into a new file named `received.txt`

**Step 3 — Send the file (Window 0)**
```bash
nc 10.100.0.10 5555 < sample.txt
```
- `<` reads `sample.txt` and pushes its contents through the connection

**Step 4 — Verify transfer (Window 1, after closing connection)**
```bash
cat received.txt
# Output: This is a Netcat file transfer test
```

> **Tip:** If the file content doesn't appear, the sender may still be connected. Press `Ctrl+c` on the sending side to close the connection — this signals the receiver to flush and save the file.

### Why this matters
This is the core mechanism behind:
- Exfiltrating data from a compromised system
- Dropping files onto a target server during a pentest
- Basic sysadmin file transfers without SCP/FTP

---

## 4. Web Server Deployment — Docker + Nginx

Before scanning, you need a target service to probe.

**Deploy an Nginx web server in a Docker container**
```bash
sudo docker run -d -p 8080:80 nginx
```

| Part | Meaning |
|---|---|
| `docker run` | Start a new container |
| `-d` | Detached (runs in background) |
| `-p 8080:80` | Map host port 8080 → container port 80 |
| `nginx` | Use the official Nginx image |

**Verify the server is running**
```bash
curl http://localhost:8080
```
If you receive a block of HTML, the server is up.

---

## 5. Port Scanning

Port scanning checks which ports (network "doors") are open on a system and actively accepting connections.

```bash
nc -zv 127.0.0.1 1-10000
```

| Flag | Meaning |
|---|---|
| `-z` | Zero-I/O mode — only check if port is open, send no data |
| `-v` | Verbose output |
| `1-10000` | Port range to scan |

### Filter results — show only open ports
```bash
nc -zv 127.0.0.1 1-10000 2>&1 | grep succeeded
```
- `2>&1` merges stderr (where nc writes results) into stdout
- `| grep succeeded` filters only successful connections

### Results from this lab

| Port | Service | Description |
|---|---|---|
| 22 | SSH | Secure remote login |
| 631 | IPP | Internet Printing Protocol |
| 3389 | RDP | Remote Desktop Protocol |
| **8080** | **HTTP-alt** | **Our Nginx web server** |

---

## 6. Banner Grabbing

Banner grabbing retrieves the identity information a service broadcasts when you connect to it.

```bash
nc 127.0.0.1 8080
```
After connecting, send an HTTP request manually:
```
HEAD / HTTP/1.0
[press Enter twice]
```

### Sample Response
```
HTTP/1.1 200 OK
Server: nginx/1.31.1
Date: Wed, 03 Jun 2026 ...
Content-Type: text/html
```

### What each field tells you

| Field | Meaning |
|---|---|
| `HTTP/1.1 200 OK` | Request succeeded |
| `Server: nginx/1.31.1` | **Software name and version** — the critical intel |
| `Date` | Server's current time |
| `Content-Type` | Format of the response body |

> **Security implication:** Knowing the exact software version (e.g., `nginx/1.31.1`) allows an attacker to look up known CVEs for that version and craft a targeted exploit.

### What `HEAD / HTTP/1.0` means
- `HEAD` — request only the response **headers**, not the body (faster, stealthier)
- `/` — target the root path of the web server
- `HTTP/1.0` — use HTTP version 1.0 protocol

---

## Summary

| Concept | What you did | Why it matters |
|---|---|---|
| **TCP connection** | Linked two terminals with `nc -lvp` and `nc <ip> <port>` | Foundation of all network communication |
| **File transfer** | Piped a file through a TCP connection using `<` and `>` | Core technique in data exfiltration and remote file delivery |
| **Port scanning** | Swept ports 1–10000 with `nc -zv` | Reconnaissance — find attack surfaces |
| **Banner grabbing** | Sent a raw HTTP request with `nc` and read the `Server:` header | Identify software and version for targeted exploits |
| **Tmux** | Managed multiple terminal sessions in one window | Efficient multi-process workflow |

---

*Tools used: `netcat (nc)`, `tmux`, `docker`, `curl`, `ip`, `cat`, `echo`, `grep`*
