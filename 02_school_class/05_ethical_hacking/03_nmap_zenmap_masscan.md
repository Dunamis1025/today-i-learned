# Lab 03: Reconnaissance with Nmap, Zenmap, and Masscan

## What is Reconnaissance?
Reconnaissance (recon) is the **first step in ethical hacking**.
Before doing anything else, hackers gather information about the target — like a detective investigating a building before going inside.

---

## What is Port Scanning?
Every computer has **65,535 ports** — think of them as doors.
Each door has a number, and specific services use specific doors:

| Port | Service | What it does |
|------|---------|--------------|
| 22 | SSH | Remote access (like controlling a computer from far away) |
| 80 | HTTP | Normal websites |
| 443 | HTTPS | Secure websites |
| 139/445 | NetBIOS/SMB | Windows file sharing |
| 143 | IMAP | Receiving emails |
| 8080/8081 | HTTP Proxy | Web proxy |

**Port scanning** = knocking on all these doors to see which ones are open.
- Security professionals use it to check: *"Are there any doors we forgot to lock?"*
- Hackers use it to find: *"Which door can I sneak through?"*

---

## Tools We Used

### 1. Nmap (Network Mapper)
A command-line tool for scanning networks and ports.

**Basic commands:**

```bash
# Default scan — just check which ports are open
nmap 192.168.68.12

# TCP Connect scan — fully open and close each door (leaves more traces)
nmap -sT 192.168.68.12

# Fast scan — only checks the 100 most common ports (misses unusual ones like 5001)
nmap -F 192.168.68.12

# Aggressive scan — checks open ports AND looks inside them (OS, versions, etc.)
nmap -A 192.168.68.12

# Script scan — runs built-in security check scripts
nmap -sC 192.168.68.12
```

**Key things I learned about Nmap flags:**

| Flag | Meaning | What it does |
|------|---------|--------------|
| `-sT` | TCP Connect | Full connection scan |
| `-F` | Fast | Top 100 ports only |
| `-A` | Aggressive | OS detection + service versions |
| `-sC` | Script | Runs default scripts to find vulnerabilities |

**Important note:** `-F` missed port 5001 because it's a non-standard port. This means fast scans can leave blind spots!

---

### 2. Zenmap
The **GUI (graphical) version** of Nmap. Same results, but easier to read visually.

**Why use Zenmap?**
- Results shown in a clean table instead of raw text
- Has a **Topology view** — shows a visual map of all discovered devices
- You can save scan results and combine multiple scans into a database
- Great for adding network maps to security reports

**How to open it:**
```bash
zenmap
```

---

### 3. Masscan
The **fastest** Internet port scanner. Claims to scan the entire internet in under 6 minutes.

```bash
# Scan entire 192.168.0.0/24 network for devices with port 80 open
masscan -sS 192.168.0.0/24 -p 80
```

**Speed comparison:**
| Tool | Task | Time |
|------|------|------|
| Nmap `-A` | 1 target, all ports | ~106 seconds |
| Nmap `-sC` | 1 target, all ports | ~90 seconds |
| Masscan | 256 hosts, 1 port | ~15 seconds |

Masscan is way faster, but gives less detail than Nmap.

---

## What We Found on the Target (192.168.68.12 — OWASP BWA)

This was a **deliberately vulnerable** practice server, not a real target.

**Open ports found:**
- 22 (SSH), 80 (HTTP), 139 (NetBIOS), 143 (IMAP), 443 (HTTPS), 445 (SMB), 5001, 8080, 8081

**Interesting findings from `-A` scan:**
- OS: Linux 2.6.32
- Web server: Apache 2.2.14
- `message_signing: disabled (dangerous)` → File sharing has no security signature = vulnerability!
- Network path: Kali → pfSense (192.168.9.1) → OWASP BWA (192.168.68.12)

---

## Key Concepts to Remember

**1. Ethical vs. Unethical hacking**
> Running these scans on a server you don't own or have permission to scan = **illegal**.
> Running them on authorized targets = **ethical hacking / penetration testing**.

**2. The 3-step hacking process**
1. **Reconnaissance** — find open doors (what we did today)
2. **Vulnerability analysis** — check if those doors have weaknesses
3. **Exploitation** — actually break in through the weakness

**3. Why did we stop Docker first?**
```bash
systemctl stop docker
systemctl stop docker.socket
```
Docker messes with network settings and causes Nmap to crash (Segmentation fault). Always stop it before scanning.

**4. Non-standard ports can hide things**
Port 5001 didn't show up in the fast scan (`-F`). In real hacking scenarios, attackers run full scans to avoid missing hidden services.

---

## Vocabulary

| Word | Meaning |
|------|---------|
| Reconnaissance | Gathering information before an attack |
| Port | A numbered "door" on a computer for network communication |
| Port scanning | Checking which ports are open on a target |
| Nmap | Network Mapper — the most popular port scanner |
| Zenmap | GUI version of Nmap |
| Masscan | Ultra-fast port scanner |
| Segmentation fault | A crash error — caused here by Docker interfering with Nmap |
| systemctl | Linux command to start/stop system services |
| pfSense | A firewall/router (pf = packet filter) |
| Security Onion | Network intrusion detection tool (named after layered security) |
| OpenSUSE | A Linux operating system made in Germany |
| OWASP BWA | A deliberately vulnerable web app used for security practice |
