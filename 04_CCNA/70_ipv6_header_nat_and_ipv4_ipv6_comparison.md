# IPv4 vs IPv6: Header Structure & Key Concepts

Study notes on IPv4/IPv6 packet headers, NAT, and Wireshark packet analysis.

---

## 1. Three Major Problems with IPv4

1. **Increased network complexity & routing table growth** — As the internet grew, routing tables became massive and harder to manage efficiently.
2. **IP address depletion** — The pool of available IPv4 addresses (~4.3 billion) has effectively run out.
3. **Lack of end-to-end connectivity** — Because of **NAT (Network Address Translation)**, devices behind a router share one public IP, which makes direct device-to-device (end-to-end) connections difficult. This is especially problematic for P2P apps, video calls, and online gaming, which is why workarounds like STUN/TURN/ICE and port forwarding exist.

---

## 2. What is NAT?

NAT translates **private (internal) IP addresses** (e.g., `192.168.0.x`) into a **single public (external) IP address** so multiple devices on a local network can share one internet connection.

```
[Internal] 192.168.0.2 ──┐
[Internal] 192.168.0.3 ──┼── NAT (Router) ── Public IP ── Internet
[Internal] 192.168.0.4 ──┘
```

**Benefits:** conserves scarce IPv4 addresses; hides internal network structure (adds a layer of security).

**Downside:** outside devices can't easily initiate a direct connection to a specific internal device — this is the "lack of end-to-end connectivity" problem.

---

## 3. IPv4 Header Structure

The header works like a shipping label on a package — it carries the info needed to deliver the data, while the payload is the actual content.

| Field | Meaning |
|---|---|
| **20 Bytes** | Minimum/base header size (without options) |
| **IHL (Internet Header Length)** | States the total length of the header |
| **Flags** | Indicates whether the packet has been fragmented and whether more fragments follow |
| **Fragment Offset** | Tells where a fragment fits within the original (unfragmented) data |
| **Header Checksum** | Verifies the header wasn't corrupted in transit |
| **Padding** | Extra bits added so the header aligns to a 32-bit boundary |

Because of optional fields, the IPv4 header has a **variable length** (20 bytes or more), which takes routers more time to process.

---

## 4. IPv6 Header Structure

IPv6 simplifies the header to speed up processing. It has a **fixed size of 40 bytes**.

| Field | Meaning |
|---|---|
| **Version** | Identifies the packet as IPv6 |
| **Traffic Class** | Manages quality of service / priority (same role as IPv4's Differentiated Services field) |
| **Flow Label** | *(New in IPv6)* Groups packets belonging to the same flow so they get consistent handling — helps real-time applications that need packets in order |
| **Payload Length** | Size of the data following the 40-byte header |
| **Next Header** | Identifies the upper-layer protocol (e.g., TCP) or points to an extension header — plays the same role as IPv4's Protocol field |
| **Hop Limit** | Same function as IPv4's TTL — decremented at each hop; packet is dropped at zero to prevent infinite loops |
| **Source / Destination Address** | 128-bit addresses of sender and receiver |

Additional features:
- Supports optional **extension headers** for extra information, placed after the main header.
- Unlike IPv4, **routers do not fragment IPv6 packets** — the sending host determines the optimal packet size in advance (this is what "end-to-end" packet handling means).

---

## 5. Key Differences: IPv4 vs IPv6

| Aspect | IPv4 | IPv6 |
|---|---|---|
| Header size | Variable (20+ bytes) | Fixed (40 bytes) |
| Fields | Includes checksum, flags, fragment offset, options | Removed/simplified; extra info moved to extension headers |
| Fragmentation | Done by routers along the path | Not done by routers — host determines packet size beforehand |
| Address space | 32-bit | 128-bit |

**Analogy:** IPv4 is a "complex invoice" trying to carry lots of information; IPv6 is a "fast, efficient invoice" carrying only what's necessary.

---

## 6. Wireshark Packet Capture Walkthrough (IPv6 example)

A real IPv6 conversation captured in Wireshark, illustrating the concepts above:

**Packet #46 (TCP SYN — establishing connection to an HTTP server)**
- Source & destination: global unicast IPv6 addresses (start with `2001:6f8...`)
- Protocol: TCP, attempting initial connection to a web server
- IPv6 header fields observed:
  - Version: 6
  - Traffic Class: handles prioritization/congestion (like IPv4's DS field)
  - Flow Label: new field, keeps packet flow consistent through routers/switches
  - Payload Length: 40 bytes in this case (equivalent to IPv4's Total Length)
  - Next Header: indicates TCP
  - Hop Limit: 64 (decrements to 0 → packet dropped)

**Packet #49 (HTTP GET request)**
- Connection to the web server is now established.
- Payload length is much larger.
- Header details now show IPv6 info + TCP info + HTTP info (the actual GET request for a web page).

**ICMPv6 Neighbor Solicitation message (Packet #1)**
- Source address: a **link-local address** (starts with `fe80`), not global unicast.
  - Uses **EUI-64** to generate the interface ID portion (identifiable by `ff:fe` in the address).
- Destination address: an `ff02` address → indicates **multicast**.
- Protocol: ICMPv6 — this is a **Neighbor Solicitation** message.
- Function: similar to an **ARP request in IPv4** — used to discover the link-local address of a nearby device by multicasting a request and waiting for a reply.
- Header fields shown: Version (6), Traffic Class, Flow Label, Payload Length, Next Header (58 = ICMPv6), Hop Limit (255).

---

## 7. Quiz Q&A Summary

**Q1: Three major issues with IPv4?**
- Increased network complexity & routing table expansion
- IP address depletion
- Lack of end-to-end connectivity (due to NAT)

**Q2: Two improvements IPv6 provides over IPv4?**
- Simpler header → improved packet handling
- Increased IP address space

**Q3: True statement about the IPv6 header?**
- It consists of 40 octets (bytes) — fixed size

**Q4: True statement about the IPv6 packet header?**
- The Hop Limit field replaces the IPv4 Time to Live (TTL) field
