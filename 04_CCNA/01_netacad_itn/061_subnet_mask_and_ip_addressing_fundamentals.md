# Networking Fundamentals — Study Notes

> **Course:** Cisco NetAcad (Protocols, Models, and IP Addressing)
> **Last updated:** 2026-06-08

---

## Table of Contents

1. [How Communication Works](#1-how-communication-works)
2. [Message Timing](#2-message-timing)
3. [Message Delivery Methods](#3-message-delivery-methods)
4. [Data Encapsulation & Decapsulation](#4-data-encapsulation--decapsulation)
5. [Protocol Stack — TCP/IP vs OSI](#5-protocol-stack--tcpip-vs-osi)
6. [Network Layer vs Data Link Layer Addresses](#6-network-layer-vs-data-link-layer-addresses)
7. [IP Addressing Basics](#7-ip-addressing-basics)
8. [Subnet Mask — Deep Dive](#8-subnet-mask--deep-dive)
9. [Default Gateway, DHCP, DNS](#9-default-gateway-dhcp-dns)
10. [Testing Connectivity with Ping](#10-testing-connectivity-with-ping)
11. [Key Terms Cheat Sheet](#11-key-terms-cheat-sheet)

---

## 1. How Communication Works

Data sent across a network is broken into structured units. Each layer of the network model adds its own wrapper before transmission.

### Encoding
Converting information into a format suitable for transmission (e.g., turning data into electrical signals or binary).

### Formatting
Structuring data so both sender and receiver understand how to interpret it (e.g., HTTP headers, JSON structure).

> ⚠️ **Encoding ≠ Formatting** — these are distinct steps. Encoding is about the signal/medium; formatting is about the data structure.

### Access Method
The rule that determines **when** a device is allowed to send data onto the shared network medium (e.g., CSMA/CD in Ethernet). Without this, multiple devices transmitting at once would cause collisions.

---

## 2. Message Timing

### Response Timeout
**Definition:** A pre-set time limit that tells a device how long to wait for a reply before giving up.

**Analogy:** You order food at a restaurant and decide, *"If it doesn't arrive in 15 minutes, I'll cancel the order."* The computer does the same — if the server doesn't reply within the timeout window, the connection is dropped or an error is returned.

**Why it matters:** Prevents a device from hanging indefinitely when a server is slow or unresponsive.

### Flow Control
Managing the rate of data transmission so the **receiver is not overwhelmed** by the sender. Think of it like a water tap — you control the flow so the cup doesn't overflow.

---

## 3. Message Delivery Methods

| Method | Recipients | Example |
|---|---|---|
| **Unicast** | One specific device | Visiting a website |
| **Broadcast** | All devices on the network | ARP request |
| **Multicast** | A specific group of devices | Live video streaming |

---

## 4. Data Encapsulation & Decapsulation

### Encapsulation (Sending)
Each network layer **wraps** the data from the layer above it with its own header (and sometimes a trailer). This is like putting a letter into an envelope, then putting the envelope into a shipping box.

```
Application Data  →  [HTTP]
                  →  [TCP | HTTP]
                  →  [IP | TCP | HTTP]
                  →  [Ethernet | IP | TCP | HTTP | Trailer]
```

### Decapsulation (Receiving)
The receiver **unwraps** the layers in reverse order, from the outermost to the innermost.

```
Ethernet → IP → TCP → HTTP → (actual web page content)
```

**Analogy:** Opening a nested package — you remove the shipping box first, then the envelope, and finally read the letter inside.

### PDU (Protocol Data Unit)
The name for data at each layer:

| Layer | PDU Name |
|---|---|
| Application | Data / Message |
| Transport | Segment |
| Network | Packet |
| Data Link | Frame |
| Physical | Bit |

---

## 5. Protocol Stack — TCP/IP vs OSI

### TCP/IP Model (4 layers — real-world implementation)

| Layer | Protocols | Role |
|---|---|---|
| **Application** | HTTP, DNS, DHCP | What the user sees; data formatting |
| **Transport** | TCP, UDP | Reliable delivery; error checking |
| **Internet** | IP | **Routing** — finding the path across networks |
| **Network Access** | Ethernet, Wi-Fi | Physical transmission over the medium |

### OSI Model (7 layers — theoretical/educational)

| # | Layer | Maps to TCP/IP |
|---|---|---|
| 7 | Application | Application |
| 6 | Presentation | Application |
| 5 | Session | Application |
| 4 | Transport | Transport |
| 3 | Network | Internet |
| 2 | Data Link | Network Access |
| 1 | Physical | Network Access |

### Which model do Ethernet / IP / TCP / HTTP belong to?

They are primarily **TCP/IP** protocols, but each maps to a corresponding OSI layer:

| Protocol | TCP/IP Layer | OSI Layer(s) |
|---|---|---|
| HTTP | Application | 7 / 6 / 5 |
| TCP | Transport | 4 |
| IP | Internet | 3 |
| Ethernet | Network Access | 2 / 1 |

> **TCP/IP = practical model** (how the internet actually works)
> **OSI = academic model** (used for education and troubleshooting frameworks)

### Which layer handles routing?
The **Internet layer** (TCP/IP) = **Network layer** (OSI Layer 3).

**Analogy:** Like a GPS — it figures out the best route for your data to travel from source to destination using IP addresses.

---

## 6. Network Layer vs Data Link Layer Addresses

| | Network Layer (IP Address) | Data Link Layer (MAC Address) |
|---|---|---|
| **Type** | Logical (can change) | Physical (burned into hardware) |
| **Length** | 32-bit (IPv4) or 128-bit (IPv6) | 48-bit |
| **Format** | Decimal (e.g., `192.168.1.1`) | 12-digit hexadecimal (e.g., `AA:BB:CC:DD:EE:FF`) |
| **Scope** | End-to-end across networks | Local network (hop-to-hop) |

---

## 7. IP Addressing Basics

### Structure of an IPv4 Address

An IPv4 address has **two parts**:

```
192  .  168  .  1  .  100
|_______________|  |_____|
  Network portion  Host portion
  (neighborhood)   (house number)
```

> The **left** side identifies the network; the **right** side identifies the device.
> The boundary between them is defined by the **subnet mask**.

### Private vs Public IP Addresses

- **Private IPs** (e.g., `192.168.x.x`, `10.x.x.x`) — used inside local networks; not routable on the internet.
- **Public IPs** — globally unique; assigned by ISPs; routable on the internet.
- Private addresses conserve the limited pool of available public IPv4 addresses.

### Checking Your IP (Command Line)

```bash
# Windows
ipconfig

# macOS / Linux
ifconfig
```

---

## 8. Subnet Mask — Deep Dive

### What is a Subnet?
**Sub + Network = Subnet** — a smaller network carved out of a larger one.

```
[Large Network: 192.168.0.0]
        ↓  (divided into)
┌──────────────┬──────────────┬──────────────┐
[192.168.1.x]  [192.168.2.x]  [192.168.3.x]
```

### What is a Subnet Mask?
A subnet mask tells a device **which bits of an IP address represent the network** and which represent the host.

**Why "mask"?** — Just like a face mask covers part of your face while exposing the rest, a subnet mask "covers" (zeros out) the host portion and "exposes" the network portion.

### How it works (binary)

```
IP Address:    192.168.1.100
               11000000.10101000.00000001.01100100

Subnet Mask:   255.255.255.0
               11111111.11111111.11111111.00000000
                  ↑ 1s = Network portion (keep)
                                          ↑ 0s = Host portion (mask out)

AND operation result:
Network Addr:  192.168.1.0
```

### Reading the Subnet Mask

| Subnet Mask | Meaning |
|---|---|
| `255.0.0.0` | First 8 bits = network |
| `255.255.0.0` | First 16 bits = network |
| `255.255.255.0` | First 24 bits = network |

### Example

```
IP:   192.168.1.100    Subnet Mask: 255.255.255.0
       ↓                             ↓
255 → keep "192"        0 → zero out "100"
255 → keep "168"
255 → keep "1"

→ Network Address: 192.168.1.0
→ Host:            .100
```

---

## 9. Default Gateway, DHCP, DNS

### Default Gateway
The **router's IP address** on your local network — the "front door" your device uses to reach the internet (devices outside your local network).

```
Your device → Default Gateway (Router) → Internet
```

### DHCP (Dynamic Host Configuration Protocol)
Automatically assigns IP addresses to devices on a network. Without DHCP, every device would need a manually configured IP.

**Analogy:** A ticket dispenser at a deli counter — you walk in, grab a number (IP address), and you're ready to go.

### DNS (Domain Name System)
Translates human-readable domain names into IP addresses.

```
"google.com" → DNS lookup → 142.250.x.x
```

**Analogy:** The internet's phonebook — you look up a name and get the number.

---

## 10. Testing Connectivity with Ping

The `ping` command tests whether two devices can communicate over the network.

### How it works
1. Device A sends an **ICMP echo request** to Device B.
2. Device B replies with an **ICMP echo reply**.
3. Replies received → connection is working ✅

### Important notes

- **First ping often times out** — this is normal. The network needs a moment for ARP resolution.
- **Always test in both directions** (A→B and B→A).
  - A→B works but B→A fails → likely a **firewall issue**, not a cable/network issue.
  - Windows Firewall blocks ICMP echo requests by default.

### Example

```bash
PC-A> ping 192.168.1.2    # Ping Switch S1
PC-A> ping 192.168.1.3    # Ping Switch S2
PC-A> ping 192.168.1.11   # Ping PC-B
PC-B> ping 192.168.1.10   # Reverse test back to PC-A
```

---

## 11. Key Terms Cheat Sheet

| Term | One-line Definition |
|---|---|
| **Encoding** | Converting data into a transmittable signal format |
| **Formatting** | Structuring data so sender and receiver agree on its layout |
| **Access Method** | Rule for when a device may transmit on shared media |
| **Response Timeout** | Max wait time before giving up on a server reply |
| **Flow Control** | Regulating transmission speed to prevent receiver overload |
| **Encapsulation** | Wrapping data with headers as it moves down the protocol stack |
| **Decapsulation** | Stripping headers as data moves up the protocol stack |
| **PDU** | Protocol Data Unit — the name for data at each layer |
| **Unicast** | One-to-one delivery |
| **Broadcast** | One-to-all delivery |
| **Multicast** | One-to-group delivery |
| **IP Address** | Logical address identifying a device on a network |
| **MAC Address** | Physical address burned into a network interface card |
| **Subnet** | A smaller network divided from a larger one |
| **Subnet Mask** | Identifies which part of an IP is network vs host |
| **Default Gateway** | Router address used to reach outside networks |
| **DHCP** | Protocol that automatically assigns IP addresses |
| **DNS** | Translates domain names to IP addresses |
| **Ping** | Tool to test network connectivity using ICMP |
| **Routing** | Finding the best path for data across networks (Internet/Network layer) |

---

*Based on Cisco NetAcad — Introduction to Networks, study sessions Apr–Jun 2026*
