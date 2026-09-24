# Networking Fundamentals — Study Notes

> **Topics Covered:** Subnetting · RAM · Port Numbers · TCP vs UDP · OSI Layers & MAC Address

---

## 1. Subnetting & IP Prefixes

### What is Subnetting?
Subnetting is the process of dividing a network into smaller, more efficient sub-networks based on the number of hosts (devices) required in each segment.

### The Formula

> **Usable Hosts = 2^(32 − Prefix) − 2**

- `32` = total bits in an IPv4 address
- `Prefix` = the number after the `/` (bits reserved for network identity)
- `− 2` = subtract the **Network Address** (first) and **Broadcast Address** (last), which cannot be assigned to devices

### Common Prefix Reference Table

| Prefix | Remaining Bits | Total Addresses | Usable Hosts |
|--------|---------------|-----------------|--------------|
| /25    | 32 − 25 = 7   | 2⁷ = 128        | **126**      |
| /26    | 32 − 26 = 6   | 2⁶ = 64         | **62**       |
| /27    | 32 − 27 = 5   | 2⁵ = 32         | **30**       |
| /30    | 32 − 30 = 2   | 2² = 4          | **2**        |

### Key Rules
- **Inverse relationship:** As prefix number ↑, available hosts ↓
- **The Half Rule:** Every time the prefix increases by 1, the number of usable hosts is cut in half (÷ 2)
- **The −2 Rule:** Always subtract 2 for the reserved network and broadcast addresses

### Subnet Matching Example (VLSM — Variable Length Subnet Masking)
Assign the **largest block to the largest requirement**, working downward:

| Network   | Required Hosts | Assigned Block        | Capacity |
|-----------|---------------|-----------------------|----------|
| Network A | 100           | 192.168.0.128 **/25** | 126      |
| Network B | 50            | 192.168.0.0 **/26**   | 62       |
| Network C | 25            | 192.168.0.96 **/27**  | 30       |
| Network D | 2             | 192.168.0.80 **/30**  | 2        |

> **Goal:** Allocate address blocks efficiently — no wasted space.

---

## 2. RAM on Network Devices (Cisco)

### What is RAM?
RAM (Random Access Memory) is the **active workspace** of a network device. Think of it as a **desk** — it holds whatever you are currently working on.

### Key Characteristics of RAM

| Characteristic | Detail |
|----------------|--------|
| **Volatile** | Contents are **lost** when the device powers off (power cycle) |
| **Stores Running Config** | The active, currently-running configuration lives in RAM |
| **Active processing** | Used for real-time operations while the device is on |

### What RAM is NOT
| False Statement | Why It's Wrong |
|-----------------|----------------|
| "RAM provides nonvolatile storage" | RAM **is** volatile — data disappears when power is cut |
| "RAM is only in switches, not routers" | RAM is a **core component** of all network devices |
| "RAM stores multiple IOS versions" | Long-term file storage belongs in **Flash** or **NVRAM**, not RAM |

### Memory Types — Quick Comparison

| Memory Type | Volatile? | Stores What? |
|-------------|-----------|--------------|
| **RAM** | ✅ Yes (data lost on reboot) | Running configuration, active processes |
| **NVRAM** | ❌ No | Startup configuration |
| **Flash** | ❌ No | IOS operating system image |
| **ROM** | ❌ No | Bootstrap program |

---

## 3. Port Numbers

### What Are Port Numbers?
Port numbers identify **which application or service** should handle incoming data on a device. They work alongside IP addresses to direct data precisely.

- **Destination Port** — identifies the *service* being contacted (e.g., port 80 = HTTP/web)
- **Source Port** — a dynamically assigned number that tracks *which specific session* the data belongs to

### The Core Function of Source Ports

> If multiple conversations occur using the **same service**, the **source port number** is used to track and separate those conversations.

**Example:** Three browser tabs open to the same website all use destination port 80, but each tab gets a unique source port (e.g., 50001, 50002, 50003) so the computer can sort the returning data to the correct tab.

### Common Well-Known Destination Ports

| Port | Protocol | Service |
|------|----------|---------|
| 20/21 | TCP | FTP (File Transfer) |
| 22 | TCP | SSH (Secure Shell) |
| 25 | TCP | SMTP (Email sending) |
| 53 | UDP/TCP | DNS (Domain Name System) |
| 67/68 | UDP | DHCP |
| 80 | TCP | HTTP (Web) |
| 443 | TCP | HTTPS (Secure Web) |

### Key Points
- Both **TCP and UDP** use port numbers (not just TCP)
- Source ports are typically generated **dynamically/randomly** by the OS
- Destination ports for standard services are standardized but **can be changed** in server configuration

---

## 4. TCP vs UDP

### Full Names
- **TCP** — Transmission Control Protocol
- **UDP** — User Datagram Protocol
- **IP** — Internet Protocol

### Core Difference

| Feature | TCP | UDP |
|---------|-----|-----|
| **Priority** | Reliability (accuracy) | Speed |
| **Connection** | Establishes connection first (3-way handshake) | No connection established |
| **Delivery check** | ✅ Confirms receipt, retransmits lost data | ❌ No confirmation, just sends |
| **Order guarantee** | ✅ Data arrives in correct order | ❌ No order guarantee |
| **Speed** | Slower (overhead from confirmation) | Faster (no overhead) |
| **Analogy** | Registered mail (signed receipt required) | Dropping flyers (just sent out) |

### When to Use Each

| Use Case | Protocol | Reason |
|----------|----------|--------|
| Web browsing (HTTP/HTTPS) | **TCP** | Every byte of data must arrive correctly |
| Email | **TCP** | Complete message integrity required |
| File transfer (FTP) | **TCP** | Cannot afford missing data |
| Live video streaming | **UDP** | Speed > perfection; a dropped frame is fine |
| Online gaming | **UDP** | Low latency is critical |
| Voice/video calls (VoIP) | **UDP** | Real-time; brief glitches are acceptable |
| DNS lookups | **UDP** | Small, fast queries |

> **Rule of thumb:** If missing data = critical failure → **TCP**. If speed > perfection → **UDP**.

---

## 5. OSI Model — Where the MAC Address is Added

### The OSI Model (7 Layers) — Quick Overview

| Layer | Name | Function | Address Used |
|-------|------|----------|--------------|
| 7 | Application | User-facing apps (HTTP, FTP, DNS) | — |
| 6 | Presentation | Data formatting, encryption | — |
| 5 | Session | Session management | — |
| 4 | Transport | Reliable delivery (TCP/UDP) | **Port Numbers** |
| 3 | Network | Routing between networks | **IP Address** |
| **2** | **Data Link** | Local physical delivery | **MAC Address** ← |
| 1 | Physical | Raw bits over cable/wireless | — |

### Where is the MAC Address Added?

> **Answer: Data Link Layer (Layer 2)**

### Why?

The **MAC (Media Access Control) address** is a hardware address burned into every network interface card (NIC). It is used for **local, physical delivery** — getting data from one directly connected device to the next.

**Postal analogy:**
- **IP Address** (Layer 3) = the full destination address on the envelope → gets it to the right city/building
- **MAC Address** (Layer 2) = the local delivery label → gets it from the local post office to the exact doorstep

Because Layer 2 (Data Link) handles the **physical hop-by-hop** delivery between directly connected hardware, this is where the MAC address is encapsulated.

### Encapsulation — The "Envelope Inside Envelope" Process

As data travels **down** the OSI layers before transmission, headers are added at each stage:

```
[Application Data]
  → + Transport Header (port numbers)     = Segment
  → + Network Header (IP addresses)       = Packet
  → + Data Link Header (MAC addresses)    = Frame
  → + Physical transmission (bits)        = Bits on wire
```

When received, the process is reversed (**decapsulation**) — each layer removes its own header.

---

## Quick Reference Cheat Sheet

```
SUBNETTING FORMULA:   Usable Hosts = 2^(32 - Prefix) - 2

RAM:                  Volatile | Stores Running Config | Lost on power off

PORT NUMBERS:         Destination = Service ID | Source = Session tracker

TCP vs UDP:           TCP = reliable/slow | UDP = fast/lossy

MAC ADDRESS:          Added at Layer 2 (Data Link) | Local hop delivery
                      IP Address = Layer 3 (Network) | End-to-end routing
```

---

*Notes compiled from Cisco Networking Academy study materials.*
