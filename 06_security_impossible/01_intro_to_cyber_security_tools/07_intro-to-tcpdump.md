# Introduction to Tcpdump — Lab Notes
> Security Impossible | Cyber Range Documentation

---

## Overview

**Tcpdump** is a command-line packet analyzer that captures and displays packets traversing network interfaces in real time. It is essential for network troubleshooting, security monitoring, incident response, and traffic inspection.

---

## Key Concepts

### What is a Network Packet?
A network packet is the fundamental unit of data transmitted across networks. Each packet consists of multiple layers of headers (encapsulation) followed by the actual data payload.

| Layer | Name | Contains | Examples |
|-------|------|----------|----------|
| Layer 2 | Data Link | MAC addresses, frame type | Ethernet header |
| Layer 3 | Network | IP addresses, protocol type | IPv4/IPv6 header |
| Layer 4 | Transport | Port numbers, sequence numbers | TCP/UDP header |
| Layer 5+ | Application | Actual data | HTTP, DNS, SSH |

### TCP Connection Flow
| Flag | Meaning |
|------|---------|
| `SYN` | Client initiates connection |
| `SYN-ACK` | Server acknowledges + responds |
| `ACK` | Client confirms |
| `[P.]` | Push — data is being sent |
| `[F.]` | FIN — connection closing |
| `[.]` | ACK only — no data |

### Berkeley Packet Filter (BPF) Syntax
Tcpdump uses BPF syntax to filter specific traffic:

| Primitive | Description |
|-----------|-------------|
| `host <IP>` | Traffic to/from a specific IP |
| `src host <IP>` | Traffic from a specific source |
| `dst host <IP>` | Traffic to a specific destination |
| `port <PORT>` | Traffic on a specific port |
| `tcp`, `udp`, `icmp` | Filter by protocol |
| `net <NETWORK>` | Traffic on a specific network |
| `and`, `or`, `not` | Combine multiple filters |

---

## Tools & Environment

- **Tool:** `tcpdump` (pre-installed, version 4.99.1)
- **OS:** Ubuntu 22.04 (`GoldenImage-Ubuntu22`)
- **Multiplexer:** `tmux` (for running multiple terminal sessions simultaneously)

### Network Interfaces Found
```bash
ip link show
```
| Interface | Type | Status |
|-----------|------|--------|
| `lo` | Loopback (127.0.0.1) — internal only | UP |
| `eth0` | Ethernet — main network interface | UP ✅ |
| `docker0` | Docker virtual network | DOWN |

> **Note:** `lo` (loopback) is a virtual interface used for internal communication within the same machine (e.g., `localhost`). `docker0` is created by Docker for container networking.

---

## Walkthrough Steps

### Step 1: Tcpdump Basics & Interface Discovery

#### Verify installation
```bash
tcpdump --version
```
Confirms tcpdump is installed and shows version info. Always verify tools before use.

#### List network interfaces
```bash
ip link show
```

#### Capture all live traffic on eth0
```bash
sudo tcpdump -i eth0
```
- Captures **all** packets on the interface in real time
- Output floods fast because SSH session traffic itself generates packets (recursive capture effect)
- Press `Ctrl + C` to stop

#### Reading Tcpdump Output
```
07:11:30.147551 IP 10.100.0.10.57650 > 168.63.129.16.80: Flags [S], seq 2023866226, length 0
```
| Field | Meaning |
|-------|---------|
| `07:11:30.147551` | Timestamp |
| `IP` | Protocol (IPv4) |
| `10.100.0.10.57650` | Source IP : Port |
| `168.63.129.16.80` | Destination IP : Port |
| `Flags [S]` | TCP flag (S = SYN) |
| `seq 2023866226` | Sequence number |
| `length 0` | Payload size |

---

### Step 2: Filtering by Host and Port

#### Why filter?
Unfiltered captures are overwhelming. BPF filters isolate only relevant traffic.

#### Using tmux for two simultaneous terminals
```bash
tmux                    # Start tmux session
# Ctrl + B then C      → Open new terminal window
# Ctrl + B then P      → Go to Previous window
# Ctrl + B then N      → Go to Next window
exit                    # Exit a tmux window
```

#### Terminal 1 — Filter by host (capture only 8.8.8.8 traffic)
```bash
sudo tcpdump -i eth0 -nn host 8.8.8.8
```
| Flag | Meaning |
|------|---------|
| `-i eth0` | Capture on eth0 interface |
| `-nn` | Don't resolve IPs/ports to names (faster, avoids DNS lookup noise) |
| `host 8.8.8.8` | Only show packets to/from 8.8.8.8 (Google DNS) |

#### Terminal 2 — Generate traffic with ping
```bash
ping 8.8.8.8
ping -c 4 8.8.8.8      # Send only 4 packets
```

#### Observation: Firewall Behavior
- `ICMP echo request` packets were **captured** (outgoing traffic visible)
- `ICMP echo reply` packets were **absent** (no response from 8.8.8.8)
- Result: `100% packet loss`
- **Conclusion:** The lab environment's firewall blocks outbound ICMP, but tcpdump still captures the outgoing attempts — useful for diagnosing firewall rules in real-world scenarios

#### Filter by port (HTTP traffic only)
```bash
sudo tcpdump -i eth0 -nn port 80
```
- Captures only packets on port 80 (HTTP)
- VM's background processes were making HTTP requests to `168.63.129.16:80`
- Both `HTTP GET` requests and `HTTP/1.1 200 OK` responses were visible → confirmed HTTP works even when ICMP is blocked

#### Combine host + port filters
```bash
sudo tcpdump -i eth0 -nn 'host 168.63.129.16 and port 80'
```
- Narrows capture to a specific host AND specific port simultaneously
- Significantly reduces noise for targeted analysis

---

## Filter Cheat Sheet

| Command | Purpose |
|---------|---------|
| `sudo tcpdump -i eth0` | Capture all traffic |
| `sudo tcpdump -i eth0 -nn host 8.8.8.8` | Filter by host |
| `sudo tcpdump -i eth0 -nn port 80` | Filter by port |
| `sudo tcpdump -i eth0 -nn 'host X and port 80'` | Filter by host AND port |
| `Ctrl + C` | Stop capture |

---

## Key Takeaways

1. **Tcpdump captures everything** — SSH session traffic, background processes, everything on the wire
2. **Filters are essential** — `host`, `port`, and `and/or` operators narrow down relevant traffic
3. **Outgoing ≠ Incoming** — You can see packets leave even if they never come back (firewall diagnosis)
4. **HTTP vs ICMP** — Different protocols can have different firewall rules; HTTP (port 80) worked while ICMP (ping) was blocked
5. **tmux** — Essential for running tcpdump in one terminal while generating traffic in another
6. **`-nn` flag** — Always use it to prevent DNS lookups from polluting captures and slowing analysis

---

## Real-World Applications

| Use Case | How Tcpdump Helps |
|----------|-------------------|
| Incident Response | Capture traffic during live attacks |
| Threat Hunting | Find indicators of compromise in traffic |
| Network Troubleshooting | Diagnose connectivity and firewall issues |
| Forensics | Preserve packet evidence (save to `.pcap`) |
| Penetration Testing | Verify attack traffic reaches target |

---

## Cleartext Protocol Warning

These older protocols transmit data **unencrypted** — visible in tcpdump captures:

| Protocol | Port | Risk |
|----------|------|------|
| FTP | 21 | Credentials in cleartext |
| Telnet | 23 | All data in cleartext |
| HTTP | 80 | Web traffic in cleartext |
| SMTP | 25 | Email + credentials in cleartext |

**Secure alternatives:** SFTP, SSH, HTTPS, SMTPS

---

## Next Steps
- Practice with different network scenarios
- Explore **Wireshark** for graphical PCAP analysis
- Study network protocols: TCP/IP, DNS, HTTP, TLS
- Participate in CTF competitions
- Integrate Tcpdump with SIEM systems for automated monitoring
