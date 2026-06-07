# Wireshark Introduction Lab — Study Notes

**Lab Source:** Security Impossible – Cyber Range Documentation  
**Tool:** Wireshark v4.6.4  
**Estimated Duration:** 40–60 minutes

---

## What is Wireshark?

Wireshark is a free, open-source **network protocol analyzer** (packet sniffer). It captures live network traffic or reads saved `.pcap`/`.pcapng` files and dissects every packet into its protocol layers.

- Used by network administrators, cybersecurity analysts, and penetration testers
- Supports over 3,000 protocols
- Essential for troubleshooting, security monitoring, and forensic analysis

---

## Core Concept: What is a Packet?

A **network packet** is the smallest unit of data sent over a network. Every packet is wrapped in multiple layers — like a series of nested envelopes:

| Layer | Protocol | Analogy |
|-------|----------|---------|
| Layer 1 | Frame | The physical signal on the wire |
| Layer 2 | Ethernet II | The delivery truck (MAC addresses) |
| Layer 3 | IP (IPv4/IPv6) | The home address (IP addresses) |
| Layer 4 | TCP/UDP | The delivery method and door number (ports) |
| Layer 5+ | HTTP/TLS/DNS... | The actual content inside |

---

## The 3-Pane Interface

| Pane | Location | Purpose |
|------|----------|---------|
| **Packet List** | Top | One row per packet — No., Time, Source, Destination, Protocol, Length, Info |
| **Packet Details** | Bottom-left | Expandable protocol tree for the selected packet |
| **Packet Bytes** | Bottom-right | Raw hex and ASCII representation of the packet |

Clicking a packet in the top pane instantly updates both bottom panes.

---

## Step 1 — Live Capture

1. Launch Wireshark → the welcome screen lists all available **network interfaces**
2. Select an interface with live traffic (e.g., `Ethernet 12`) — look for the moving traffic graph
3. Click the interface to start capturing — packets scroll in real time
4. Stop capture: **Capture → Stop** (`Ctrl + E`) or click the red square icon

> **Key insight:** Live capture shows every packet your machine sends and receives in real time. This is the "recording" mode.

---

## Step 2 — Opening a .pcap File

A `.pcapng` file is a **saved recording** of past network traffic — like a video file you can replay and analyze.

1. **File → Open** (`Ctrl + O`)
2. Navigate to `Network Traffic.pcapng` on the Desktop
3. Click **Open** — the same 3-pane interface loads with pre-captured packets

> **Key insight:** Offline analysis lets you examine traffic captured earlier, on another machine, or provided as evidence in an investigation.

---

## Step 3 — Reading the Packet Details Pane

When you expand the protocol tree for a packet, focus on these **4 key fields**:

| Field | Where to find it | What it tells you |
|-------|-----------------|-------------------|
| **Source IP** | Internet Protocol layer | Who sent the packet |
| **Destination IP** | Internet Protocol layer | Who received it |
| **Protocol** | Packet List / TCP layer | How it was sent (TCP, UDP, TLS...) |
| **Port number** | TCP/UDP layer | Which service was used |

### Common Port Numbers to Know

| Port | Service |
|------|---------|
| 80 | HTTP (unencrypted web) |
| 443 | HTTPS (encrypted web) |
| 3389 | RDP (Remote Desktop) |
| 22 | SSH (secure shell) |
| 53 | DNS (domain name lookup) |

---

## Step 4 — Statistics Menu

### Protocol Hierarchy (`Statistics → Protocol Hierarchy`)

Shows a **breakdown of all protocols** in the capture by percentage.

- Useful for quickly understanding what kind of traffic dominates
- High HTTP (port 80) → unencrypted traffic → potential security risk
- Unknown protocols → possible malware

**Example from lab capture:**

| Protocol | Share |
|----------|-------|
| TCP | 72.2% |
| TLS (encrypted) | 46.3% |
| UDP / QUIC | 26.5% |
| DNS | 1.3% |

### Conversations (`Statistics → Conversations`)

Shows **who talked to whom**, how many packets were exchanged, and how much data was transferred. Tabs available: Ethernet, IPv4, TCP, UDP.

- Sort by **Bytes** column to find the heaviest talkers
- A single IP dominating all conversations can indicate malware C2 communication or a busy server

**Example from lab:**

```
172.16.0.10 ↔ 146.75.77.91 → 2,057 packets / 14 MB
103.160.27.4 ↔ 172.16.0.10 → 16,430 packets / 13 MB
```

---

## Step 5 — Display Filters

Display filters are the **most powerful feature** of Wireshark. They let you show only the packets you care about without deleting anything.

- Type in the filter bar at the top
- Bar turns **green** = valid filter syntax
- Bar turns **red** = invalid syntax
- Clear with the **X button** on the right

### Essential Filter Syntax

| Filter | What it shows |
|--------|--------------|
| `tcp` | TCP packets only |
| `udp` | UDP packets only |
| `dns` | DNS queries only |
| `http` | Unencrypted HTTP only |
| `ip.addr == 192.168.1.1` | All packets to/from this IP |
| `ip.src == 10.0.0.1` | Packets FROM this IP only |
| `ip.dst == 10.0.0.1` | Packets TO this IP only |
| `tcp.port == 443` | Traffic on port 443 |
| `tcp.port == 80` | HTTP traffic |

### Capture Filters vs Display Filters

| | Capture Filter | Display Filter |
|-|---------------|----------------|
| **When applied** | Before recording | After recording |
| **Effect** | Drops non-matching packets permanently | Hides them temporarily |
| **Syntax** | BPF syntax (e.g., `tcp port 80`) | Wireshark syntax (e.g., `tcp.port == 80`) |

---

## Step 6 — Follow Stream

Right-click any packet → **Follow → TCP Stream** (or UDP / TLS)

Reassembles the **entire conversation** between two hosts into a single readable window.

- **Red text** = client → server
- **Blue text** = server → client
- If traffic is **TLS-encrypted**, content appears as garbled characters (cannot be read without the decryption key)
- Shows total size, number of packets, and number of turns

> **Key insight:** Follow Stream is the fastest way to see "what actually happened" in a connection — login attempts, file transfers, web requests, etc.

---

## Key Concepts Summary

| Concept | Meaning |
|---------|---------|
| **Live Capture** | Recording traffic in real time from a network interface |
| **Offline Analysis** | Analyzing a pre-saved `.pcap` / `.pcapng` file |
| **Promiscuous Mode** | Captures ALL packets on the network, not just your own |
| **Protocol Dissection** | Wireshark automatically decodes each protocol layer |
| **Coloring Rules** | Packets are color-coded by protocol for quick identification |
| **Expert Information** | Wireshark flags retransmissions, checksum errors, etc. automatically |
| **Follow Stream** | Reassembles a full TCP/UDP/HTTP/TLS conversation into readable text |

---

## What to Look For as a Security Analyst

1. **Unusual ports** — traffic on unexpected ports may indicate malware or tunneling
2. **One IP talking to many IPs** — could be a port scan or C2 beacon
3. **Large data transfers to external IPs** — potential data exfiltration
4. **Unencrypted HTTP traffic** — credentials or sensitive data may be exposed
5. **DNS anomalies** — excessive DNS queries can indicate DNS tunneling or malware
6. **TCP retransmissions** — may indicate network issues or evasion attempts

---

*Notes based on hands-on lab completed on Security Impossible Cyber Range — June 2026*
