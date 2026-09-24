# 📡 Networking Study Summary

## Part 1: Standards Organizations

### Key Concept
Standards organizations are **vendor-neutral** — they develop standards without bias toward any specific company or product (e.g., ISO, IEEE, W3C).

### Major Internet Standards Organizations

| Organization | Full Name | Responsibility |
|---|---|---|
| **ISOC** | Internet Society | Promotes open development of the Internet |
| **IETF** | Internet Engineering Task Force | Develops and updates **RFC (Request for Comments)** documents that define new and existing protocols |
| **IRTF** | Internet Research Task Force | Long-term research on Internet protocols |
| **IAB** | Internet Architecture Board | Oversees Internet architecture and standards |
| **IANA** | Internet Assigned Numbers Authority | Manages **IP address allocation** and **domain name (DNS) management** |
| **EIA** | Electronics Industries Alliance | Develops standards for **electrical wiring and connectors** (e.g., RS-232) |

> 💡 **Quick Rule:**
> - RFC documents → **IETF**
> - IP addresses & DNS → **IANA**
> - Wiring & connectors → **EIA**

---

## Part 2: Data Transmission Fundamentals

### Segmentation
- The process of **dividing a large data stream into smaller pieces** before transmission.
- Analogy: Packing one large shipment into multiple smaller boxes.

### Encapsulation vs. De-encapsulation

| Direction | Process | Description |
|---|---|---|
| Sending (down the stack) | **Encapsulation** | Protocol information (headers) is added at each layer |
| Receiving (up the stack) | **De-encapsulation** | Headers are removed layer by layer |

- Analogy: Encapsulation = wrapping a gift layer by layer; De-encapsulation = unwrapping it.

### PDU (Protocol Data Unit) by Layer
Each layer of the protocol stack has its own name for a unit of data:

| Layer | PDU Name |
|---|---|
| Application | Data |
| Transport | **Segment** |
| Network | **Packet** |
| Data Link | **Frame** |
| Physical | **Bits** |

> 💡 The **Transport layer** encapsulates data into **Segments**.
> The **Data Link layer** encapsulates data into **Frames**.

---

## Part 3: IP Addressing

### IP Address Structure
An IP address has two parts:
- **Left portion** → identifies the **Network**
- **Right portion** → identifies the **Host (device)**

**Example:** `192.168.1.100`
- `192.168.1` = Network
- `100` = Host

### Subnet Mask
- Used to **determine which part of an IP address is the network portion**.
- Acts like a highlighter: `255` = network part, `0` = host part.

**Example:**
```
IP Address:   192.168.1.100
Subnet Mask:  255.255.255.0
              └──────────┘└─┘
                Network   Host
```

### Default Gateway
- When devices on **different networks** communicate, data must be forwarded to the **default gateway** (typically a router).
- Devices on the **same network** communicate directly without a gateway.

---

## Part 4: Network Layer vs. Data Link Layer Addresses

| Feature | Network Layer (IP Address) | Data Link Layer (MAC Address) |
|---|---|---|
| Type | **Logical** (can change) | **Physical** (burned into hardware) |
| Length | **32 bits** (IPv4) or **128 bits** (IPv6) | **48 bits** |
| Format | Decimal — e.g., `192.168.1.1` | 12 hexadecimal digits — e.g., `AA:BB:CC:DD:EE:FF` |
| Changes during transit? | **No** — stays the same end-to-end | **Yes** — changes at each router hop |

### Data Link Frame Address Order
Frames always list addresses in this order:
1. **Destination MAC** (where is it going?)
2. **Source MAC** (where did it come from?)

> 📬 Like an envelope: recipient's address comes first, sender's address comes second.

### Why MAC Addresses Change at Each Hop
Even though MAC addresses are physically fixed to devices, the **source and destination MAC in the frame are updated at every router**.

- **IP address** = the final destination (stays the same throughout the journey)
- **MAC address** = the next stop (updated at each hop)

> 📦 Analogy: Like a package traveling through multiple distribution centers — the shipping label (MAC) changes at each center, but the final delivery address (IP) never changes.

---

## Quick Reference Cheat Sheet

```
Segmentation    → Breaking large data into smaller pieces before sending
Encapsulation   → Adding headers as data moves DOWN the protocol stack
De-encapsulation→ Removing headers as data moves UP the protocol stack

Transport Layer PDU  → Segment
Network Layer PDU    → Packet
Data Link Layer PDU  → Frame
Physical Layer PDU   → Bits

IP Address  → Logical, left = network, right = host
Subnet Mask → Determines network vs. host portion
MAC Address → Physical, 48-bit, 12 hex digits, changes per hop
Gateway     → Required when communicating across different networks

Frame order → Destination MAC first, then Source MAC
```
