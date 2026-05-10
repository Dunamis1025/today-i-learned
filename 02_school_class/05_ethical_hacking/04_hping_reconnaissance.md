# Lab 04: Reconnaissance with hping3

## Overview

**hping3** is a TCP/IP packet assembler and analyzer. Unlike a regular `ping`, hping3 allows you to manually craft packets with specific protocols, flags, and options — making it a powerful tool for network reconnaissance in ethical hacking.

---

## Lab Environment

| Virtual Machine     | IP Address                              | Username | Password |
|---------------------|-----------------------------------------|----------|----------|
| Kali Linux          | 192.168.9.2 / 192.168.0.2              | root     | toor     |
| pfSense (Firewall)  | 192.168.0.254 / 192.168.68.254 / 192.168.9.1 | admin | pfsense |
| OWASP BWA           | 192.168.68.12                           | root     | owaspbwa |

### Network Topology
```
Kali (.2)
  |
  | WAN: 192.168.9.0/24
  |
pfSense (.1 / .254)
  |
  | DMZ: 192.168.68.0/24
  |
OWASP BWA (.12)
```

- **Kali Linux**: Attacker machine running hping3
- **pfSense**: Firewall/router separating WAN and DMZ networks
- **OWASP BWA (Broken Web Apps)**: Intentionally vulnerable target server for practice

---

## Key Terminology

| Term | Full Name | Meaning |
|------|-----------|---------|
| ICMP | Internet Control Message Protocol | Protocol used to check network status (e.g., ping). Not for data transfer — used to ask "are you alive?" |
| RTT | Round Trip Time | Time for a packet to travel to the destination and back |
| TTL | Time To Live | Counter that decreases by 1 at each router hop; packet is dropped when it hits 0 |
| TCP | Transmission Control Protocol | Connection-based protocol used for reliable data transfer |
| SYN | Synchronize | First packet sent when initiating a TCP connection ("knock knock") |
| ACK | Acknowledge | Confirmation packet ("I hear you") |
| RST | Reset | Packet that immediately terminates a connection |
| tcpdump | TCP Dump | Tool that "dumps" (outputs) captured network packets to the screen in real time |
| eth0 | Ethernet 0 | Name of the first network interface card in Linux |
| Verbose (-V) | Verbose | Shows detailed output; from the word meaning "wordy/detailed" |

---

## Part 1: Using hping3 as an ICMP Utility

### Command Option Reference

| Option | Full Word | Meaning |
|--------|-----------|---------|
| `-1` | (ICMP mode) | Send packets using ICMP protocol |
| `-2` | (UDP mode) | Send packets using UDP protocol |
| `-c` | count | Number of packets to send |
| `-V` | Verbose | Show detailed output |
| `-C` | ICMP code | Specify ICMP type number |
| `-T` | Traceroute | Enable traceroute mode |
| `-S` | SYN | Set TCP SYN flag |
| `-s` | source port | Set the source port number |
| `-p` | port | Set the destination port number |
| `-8` | scan mode | Scan a range of ports |

---

### Task 1: Basic ICMP Echo (Type 0)

**Command:**
```bash
hping3 -1 192.168.68.12
```

**What it does:**
Sends ICMP Type 0 (echo request) packets to the OWASP server — same concept as a regular `ping`, but using hping3.

**Result:**
```
7 packets transmitted, 7 packets received, 0% packet loss
round-trip min/avg/max = 3.6/5.5/7.9 ms
```

**Interpretation:**
- 0% packet loss → OWASP server is alive and reachable ✅
- RTT of 3.6–7.9 ms is normal for a local virtual network

**RTT Reference:**
| Network Type | Expected RTT |
|--------------|-------------|
| Local/virtual network | 1–10 ms ✅ |
| Same country server | 10–50 ms |
| International server | 100–300 ms |
| Problematic connection | 500ms+ ❌ |

---

### Task 2: ICMP Timestamp (Type 13)

**Command:**
```bash
hping3 -c 3 -1 -V -C 13 192.168.68.12
```

**Options breakdown:**
- `-c 3` → send only 3 packets
- `-1` → ICMP mode
- `-V` → verbose output
- `-C 13` → use ICMP Type 13 (timestamp request)

**What it does:**
Instead of a simple echo, it asks the target "what time is it?" — the target replies with its current timestamp. This is an alternative way to confirm a host is alive, useful when Type 0 (echo) is blocked by a firewall.

**Result:**
```
ICMP timestamp: Originate=77029488 Receive=77029565 Transmit=77029565
3 packets transmitted, 3 packets received, 0% packet loss
```

**Interpretation:**
The server responded with timestamp data → host is confirmed alive ✅

---

### Task 3: Traceroute via ICMP

**Command:**
```bash
hping3 -c 5 -T -1 -V 192.168.68.12
```

**What it does:**
Performs a traceroute using ICMP — maps the path packets take from Kali to the OWASP server by exploiting how TTL works.

**How TTL-based traceroute works:**
1. Send a packet with TTL=1 → first router drops it and sends back an error → we learn the first hop
2. Send with TTL=2 → second router drops it → we learn the second hop
3. Repeat until destination is reached

**Result:**
```
hop=1 TTL 0 during transit from ip=192.168.9.1 name=UNKNOWN
hop=1 hoprtt=7.9 ms
```

**Interpretation:**
- First hop: pfSense firewall at 192.168.9.1
- Then directly reaches OWASP at 192.168.68.12
- Path: **Kali → pfSense → OWASP** (2 hops total) — matches the network topology ✅

---

## Part 2: Using hping3 for Port Scanning

### How TCP Port Scanning Works

When hping3 sends a SYN packet to a port:
- **Port OPEN** → target replies with **SYN-ACK** (connection accepted)
- **Port CLOSED/FILTERED** → target sends **RST** or gives **no response**

hping3 then sends a RST to close the half-open connection without completing the full TCP handshake. This is called a **SYN scan** (or half-open scan).

```
Open port:    Kali --[SYN]--> Target --[SYN-ACK]--> Kali --[RST]--> Target
Closed port:  Kali --[SYN]--> Target  (no response / RST)
```

---

### Task 4: SYN Scan on Single Port — OWASP Port 80

**Setup: Start packet capture in second terminal**
```bash
tcpdump -i eth0
```
- `tcpdump`: captures and displays live network packets
- `-i eth0`: listen on the eth0 (Ethernet 0) network interface
- Leave this running in the background

**Command (in first terminal):**
```bash
hping3 -S -c 1 -s 5151 -p 80 -V 192.168.68.12
```

**Options breakdown:**
- `-S` → set TCP SYN flag
- `-c 1` → send 1 packet
- `-s 5151` → source port (arbitrarily chosen)
- `-p 80` → destination port (HTTP)
- `-V` → verbose

**hping3 result:**
```
sport=80 flags=SA seq=0 win=5840 rtt=7.9 ms
1 packets transmitted, 1 packets received, 0% packet loss
```

**tcpdump result:**
```
Flags [S]   → Kali sent SYN
Flags [S.]  → OWASP replied SYN-ACK
Flags [R]   → Kali sent RST to close
```

**Interpretation:** Port 80 on OWASP is OPEN ✅

---

### Task 5: SYN Scan on pfSense Port 80

**Command:**
```bash
hping3 -S -c 1 -s 5151 -p 80 -V 192.168.9.1
```

**Result:**
```
sport=80 flags=SA rtt=3.9 ms
1 packets transmitted, 1 packets received, 0% packet loss
```

**Interpretation:** Port 80 on pfSense firewall is OPEN ✅

---

### Task 6: SYN Scan on pfSense Port 22 (SSH)

**Command:**
```bash
hping3 -S -c 1 -s 5151 -p 22 -V 192.168.9.1
```

**Result:**
```
1 packets transmitted, 0 packets received, 100% packet loss
round-trip min/avg/max = 0.0/0.0/0.0 ms
```

**Interpretation:** Port 22 (SSH) on pfSense is CLOSED/FILTERED ❌  
No response at all — the firewall is blocking SSH access.

**Comparison:**
| Port | Service | Response | Status |
|------|---------|----------|--------|
| 80 | HTTP | SYN-ACK | OPEN ✅ |
| 22 | SSH | No response | CLOSED ❌ |

---

### Task 7: Port Range Scan on pfSense (ports 20–80)

**Command:**
```bash
hping3 -S -8 20-80 -c 1 -s 5151 -V 192.168.9.1
```

**Options breakdown:**
- `-S` → SYN flag
- `-8 20-80` → scan mode, scan ports 20 through 80
- `-c 1` → 1 packet per port
- `-s 5151` → source port

**Result:**
```
|port| serv name |  flags  |ttl| id | win | len |
   53 domain     : .S..A...  64   0  65228   44
   80 http       : .S..A...  64   0  65228   44

Not responding ports: (20 ftp-data)(21 ftp)(22 ssh)(23 telnet)...
```

**flags=.S..A... means:**
- `S` = SYN was set
- `A` = ACK was received → port replied with SYN-ACK → **OPEN**

**Interpretation:**
- Port 53 (DNS) → OPEN ✅
- Port 80 (HTTP) → OPEN ✅
- All others (20–52, 54–79) → CLOSED ❌

---

## Summary

### What We Learned

| Technique | Tool/Command | Purpose |
|-----------|-------------|---------|
| ICMP Echo | `hping3 -1` | Confirm host is alive (like ping) |
| ICMP Timestamp | `hping3 -1 -C 13` | Alternative host discovery when echo is blocked |
| ICMP Traceroute | `hping3 -T -1` | Map the network path to target |
| TCP SYN scan | `hping3 -S -p [port]` | Check if a specific port is open |
| Port range scan | `hping3 -S -8 [range]` | Scan multiple ports at once |
| Packet capture | `tcpdump -i eth0` | Observe raw packets in real time |

### Key Takeaway
> hping3 gives you precise control over packet crafting — unlike standard tools, you can choose the exact protocol, flags, port, and packet count. This makes it extremely useful for understanding how firewalls respond and which ports are accessible on a target.
