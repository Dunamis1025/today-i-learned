# Lab 07: Evading IDS — Study Notes

## Overview

This lab explores how an attacker can attempt to **evade Intrusion Detection Systems (IDS)** using various Nmap scan techniques, and how monitoring tools detect (or fail to detect) those attacks.

---

## Lab Environment

| Virtual Machine     | Role               | IP Address(es)                              |
|---------------------|--------------------|---------------------------------------------|
| Kali Linux          | Attacker           | 192.168.9.2 / 192.168.0.2                   |
| pfSense             | Firewall / Router  | 192.168.0.254 / 192.168.68.254 / 192.168.9.1 |
| OpenSUSE            | Target (victim PC) | 192.168.0.30                                |
| OWASP BWA           | Target (web server)| 192.168.68.12                               |
| Security Onion      | IDS / Monitor      | 192.168.0.100                               |

### Why are all these machines needed?
- **Kali** → the attacker's machine; all scans are run from here
- **pfSense** → acts as the real-world router/firewall; all traffic passes through it
- **OpenSUSE / OWASP BWA** → intentionally vulnerable targets that receive the attacks
- **Security Onion** → passively monitors all traffic passing through pfSense and raises alerts

---

## Key Concepts

### What is an IDS?
An **Intrusion Detection System** monitors network traffic and raises alerts when suspicious activity is detected. It works like a security camera — it watches everything but does not block traffic on its own (that would be an IPS).

### What is Nmap?
A network scanning tool used to discover hosts and open ports on a network. In this lab, it is used as the "attack" tool.

---

## Monitoring Tools on Security Onion

All three tools below read the **same data** — they just display it differently.

| Tool       | Pronunciation | Best For                                      |
|------------|---------------|-----------------------------------------------|
| **Sguil**  | "sgweel"      | Real-time raw event log; see exact packets    |
| **Snorby** | "snore-bee"   | Dashboard with severity counts and charts     |
| **Squert** | "skwert"      | Visual patterns; source/destination flow view |

### What to look for in each tool:
- **Sguil** → Check `Source IP` column. Is the attacker's real IP visible?
- **Snorby** → Check `Medium Severity` count on the Dashboard. Did it go up after a scan?
- **Squert** → Check the `QUEUE` events. Are multiple source IPs showing up (real + decoys)?

> **Tip for Snorby:** Always make sure the time filter at the top is set to **TODAY** or **LAST 24**. If it's set to a different range, the count may show 0 even when attacks were detected.

---

## Tasks Performed

### Task 1: Initialize Monitoring Applications
- Logged into **Security Onion** and launched Squert, Snorby, and Sguil
- These tools must be running before any scans are performed, so alerts can be captured

---

### Task 2: Regular Nmap Scan (Fragmented Packets)
```bash
nmap -f 192.168.0.30
```
- `-f` = fragment packets (split into smaller pieces to try to confuse IDS)
- **Result:** Security Onion still detected the scan
- Snorby showed **6 Medium Severity** events
- Sguil showed **no new real-time alerts** at this stage (pre-existing events only)

**What this shows:** Even a basic evasion technique (fragmentation) is caught by a properly configured IDS.

---

### Task 3: Decoy Scan
```bash
nmap -D 192.168.9.20 192.168.9.30 192.168.9.40 192.168.0.30
```
- `-D` = Decoy mode; sends packets that appear to come from multiple IPs simultaneously
- The IPs listed (`.20`, `.30`, `.40`) are **fake/decoy** source addresses mixed in with the real attacker IP (`192.168.9.2`)
- **Result:** IDS detected the scan but saw multiple source IPs — harder to pinpoint the real attacker
- Squert showed both `192.168.9.2` (real) and `192.168.9.20` (decoy) as sources
- Sguil displayed only the decoy IP `192.168.9.20`, not the real one

**What this shows:** Decoy scans can obscure the attacker's real IP, causing confusion in IDS logs — but the scan itself is still detected.

---

### Task 4: Spoofed MAC Address Scan
```bash
nmap -sT -PN --spoof-mac 0 192.168.0.30
```
- `--spoof-mac 0` = assign a random fake MAC address for this scan
- `-sT` = TCP Connect scan
- `-PN` = skip host discovery (assume host is up)
- **Result:** Nmap reported a randomly generated MAC (e.g., `11:4E:26:C6:6D:9D`) with no registered vendor
- Compared results across Snorby, Squert, and Sguil

**What this shows:** MAC spoofing changes the hardware-level identifier of the attacker's machine, making it harder to trace back to a specific physical device.

---

## Key Takeaways

| Scan Type        | IDS Detects Scan? | Real IP Visible? | Notes                                      |
|------------------|:-----------------:|:----------------:|--------------------------------------------|
| Regular (`-f`)   | ✅ Yes            | ✅ Yes           | Fragmentation doesn't fool modern IDS       |
| Decoy (`-D`)     | ✅ Yes            | ⚠️ Partially     | Real IP mixed with fakes; harder to isolate |
| MAC Spoof        | ✅ Yes            | ✅ Yes (IP)      | MAC is hidden, but IP-level identity remains|

> **Bottom line:** These evasion techniques make attribution harder, but a well-configured IDS (like Security Onion with Snort rules) will still detect that *a* scan occurred — it just may struggle to identify exactly *who* did it.

---

## Tool Name Origins

| Name            | Origin / Meaning                                                                 |
|-----------------|----------------------------------------------------------------------------------|
| Security Onion  | Layered security — like the layers of an onion                                   |
| pfSense         | **pf** = Packet Filter; a smart packet-filtering firewall/router                 |
| Sguil           | Named after a type of squirrel fish; a Tcl/Tk network security monitoring tool   |
| Snorby          | Built on top of **Snort** (the IDS engine); "-by" is a common naming suffix      |
| Squert          | A web interface for querying Sguil/Snort data                                    |
| Nmap            | **N**etwork **Map**per                                                           |
