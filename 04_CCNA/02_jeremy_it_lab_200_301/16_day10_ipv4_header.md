# Day 10 – The IPv4 Header (CCNA 200-301)

> Source: Jeremy's IT Lab, Free CCNA, Day 10 – *IPv4 Header*
> Exam topic: 1.0 Network Fundamentals – IPv4 addressing and the fields routers use to forward packets.

---

## 1. Big Picture

- The **IPv4 header** is the Layer 3 (Network layer) header added to the data handed down from Layer 4 (a TCP segment or UDP datagram).
- **Header + payload = IP packet.**
- The IP packet is then placed inside the **payload of an Ethernet frame** (Layer 2). That is why the Ethernet payload is 46–1500 bytes: an IP packet of up to 1500 bytes fits there.
- Routers read the IP header to decide where to forward a packet. Switches only look at the Ethernet header.

```
[ Ethernet header | IPv4 header | TCP/UDP header | Application data | Ethernet FCS ]
                    \_______________ IP packet _______________/
\________________________________ Ethernet frame ________________________________/
```

---

## 2. Header Layout

The header is read in rows of **32 bits (4 bytes)**. The minimum is 5 rows = 20 bytes.

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Version|  IHL  |    DSCP   |ECN|         Total Length          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         Identification        |Flags|     Fragment Offset     |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| Time to Live  |    Protocol   |        Header Checksum        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                        Source Address                         |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                      Destination Address                      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                     Options (if IHL > 5)                      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

---

## 3. Field Summary

| # | Field | Size | Purpose |
|---|---|---|---|
| 1 | **Version** | 4 bits | IP version. Always `4` (`0100`) for IPv4. IPv6 uses `6`. |
| 2 | **IHL** (Internet Header Length) | 4 bits | Header length in **32-bit words**. Min 5 (20 bytes), max 15 (60 bytes). |
| 3 | **DSCP** (Differentiated Services Code Point) | 6 bits | Marks the packet for **QoS** (priority handling). |
| 4 | **ECN** (Explicit Congestion Notification) | 2 bits | Lets routers signal congestion without dropping packets. |
| 5 | **Total Length** | 16 bits | Size of the **whole packet** (header + data) in bytes. Max 65,535. |
| 6 | **Identification** | 16 bits | Identifies which original packet a fragment belongs to. |
| 7 | **Flags** | 3 bits | Fragmentation control: Reserved, **DF**, **MF**. |
| 8 | **Fragment Offset** | 13 bits | Position of this fragment in the original packet (units of 8 bytes). |
| 9 | **TTL** (Time To Live) | 8 bits | Hop limit. Each router subtracts 1. |
| 10 | **Protocol** | 8 bits | Which Layer 4 (or other) protocol is inside the payload. |
| 11 | **Header Checksum** | 16 bits | Error check for the **header only**. |
| 12 | **Source Address** | 32 bits | IPv4 address of the sender. |
| 13 | **Destination Address** | 32 bits | IPv4 address of the receiver. |
| 14 | **Options** | 0–40 bytes | Rarely used extras. Padded to a 32-bit boundary. |

Quick check: 20 bytes of fixed fields = 4+4+6+2+16+16+3+13+8+8+16+32+32 = **160 bits = 20 bytes**.

---

## 4. Field Details

### 4.1 Version
- 4 bits, value **4** for IPv4.
- Receivers read this first to know how to interpret the rest of the header.

### 4.2 IHL (Internet Header Length)
- Counts the header length in **4-byte words**, not bytes.
- Header length in bytes = **IHL × 4**.
- Minimum `5` → 5 × 4 = **20 bytes** (no options).
- Maximum `15` → 15 × 4 = **60 bytes** (40 bytes of options).
- It is needed because the Options field makes the header length variable. The receiver uses IHL to know where the payload starts.

### 4.3 DSCP and ECN (formerly the "ToS" byte)
- The original 8-bit **Type of Service** byte was redefined as:
  - **DSCP (6 bits)** – QoS marking. Examples: `0` = best effort (default), `46` (EF) = voice traffic.
  - **ECN (2 bits)** – congestion signaling.
- Switches and routers with QoS configured use DSCP to decide which packets to prioritize (QoS is covered later in the course).

### 4.4 Total Length
- 16 bits → maximum value 2^16 − 1 = **65,535 bytes**.
- Includes the header and the payload.
- In practice packets are limited by the link **MTU** (1500 bytes on Ethernet), well below the maximum.
- Payload size = Total Length − (IHL × 4).

### 4.5 Identification, Flags, Fragment Offset (fragmentation)

These three fields work together when a packet is **larger than the MTU** of the outgoing link.

**MTU (Maximum Transmission Unit)** = the largest IP packet a link can carry. Ethernet default: **1500 bytes**.

**Flags (3 bits)**

| Bit | Name | Meaning |
|---|---|---|
| 0 | Reserved | Always 0. |
| 1 | **DF** – Don't Fragment | If 1, routers must **not** fragment the packet. If it is too big, the router drops it and sends an ICMP "Fragmentation needed" message back. |
| 2 | **MF** – More Fragments | 1 = more fragments follow. 0 = this is the **last** (or the only) fragment. |

**Identification**
- All fragments of the same original packet carry the **same Identification value**, so the receiver can group them.

**Fragment Offset**
- 13 bits, measured in **8-byte units**.
- First fragment has offset `0`.
- Fragment data sizes (except the last) must be a multiple of 8 bytes.

**Worked example** – a 4000-byte packet (20-byte header + 3980 bytes of data) crosses a link with MTU 1500:

| Fragment | Data size | Total Length | MF | Fragment Offset |
|---|---|---|---|---|
| 1 | 1480 | 1500 | 1 | 0 |
| 2 | 1480 | 1500 | 1 | 185 (1480 ÷ 8) |
| 3 | 1020 | 1040 | 0 | 370 (2960 ÷ 8) |

- Data per fragment = 1500 − 20 = 1480 (and 1480 is divisible by 8).
- **Only the destination host reassembles** the fragments, not the routers in between.
- Fragmentation hurts performance, so modern hosts usually set DF and use Path MTU Discovery instead.

### 4.6 TTL (Time To Live)
- 8 bits → range 0–255.
- Prevents packets from looping forever in a routing loop.
- **Every router decrements TTL by 1.** When TTL reaches **0**, the router **drops** the packet and sends an **ICMP Time Exceeded** message to the source.
- Common starting values: **Windows 128**, **Linux/macOS 64**, **Cisco IOS 255**.
- `traceroute` exploits this: it sends packets with TTL 1, 2, 3, … and records which router replies with Time Exceeded at each hop.
- Example from `ping` output: `Reply from 192.168.1.1: bytes=32 time=2ms TTL=64`.

### 4.7 Protocol
Tells the receiving host which protocol to hand the payload to.

| Value | Protocol |
|---|---|
| **1** | **ICMP** (ping uses ICMP Echo Request / Echo Reply) |
| 2 | IGMP |
| **6** | **TCP** |
| **17** | **UDP** |
| 47 | GRE |
| 50 | ESP (IPsec) |
| 88 | EIGRP |
| **89** | **OSPF** |

- Routing protocols like OSPF (89) and EIGRP (88) ride **directly on IP**, with no TCP or UDP in between.
- Memorize **1, 6, 17, 89** for the exam.

### 4.8 Header Checksum
- 16-bit value used to detect corruption **in the header only** (the payload is protected by Layer 4 and by the Ethernet FCS).
- Calculated as a one's-complement sum of the header's 16-bit words.
- Because **TTL changes at every hop**, each router must **recalculate the checksum** every time it forwards a packet.
- If the checksum does not match on arrival, the packet is discarded.

### 4.9 Source and Destination Address
- 32 bits each, written in dotted decimal (e.g., `192.168.1.10`).
- Normally unchanged end to end, except when **NAT** rewrites them (covered later).
- The destination address is what routers look up in the **routing table**.
- Remember from earlier days: the source address must be a **unicast** address; multicast addresses (224.0.0.0–239.255.255.255) are valid only as destinations.

### 4.10 Options
- Optional, variable length (up to 40 bytes), padded so the header ends on a 32-bit boundary.
- Examples: record route, timestamp, source routing.
- Rarely used today, and many routers handle option packets slowly or drop them.
- This is the reason IHL exists.

---

## 5. What Changes at Each Router?

| Field | Changes in transit? |
|---|---|
| Source / Destination IP | No (unless NAT is used) |
| **TTL** | **Yes**, decremented by 1 |
| **Header Checksum** | **Yes**, recalculated because TTL changed |
| Fragmentation fields | Only if the router fragments the packet |
| Ethernet source/destination MAC | **Yes**, rewritten at every hop (new Layer 2 header per link) |

Key idea: **IP addresses stay the same end to end; MAC addresses change hop by hop.**

---

## 6. IPv4 vs IPv6 Header (quick comparison)

| Item | IPv4 | IPv6 |
|---|---|---|
| Header size | 20–60 bytes (variable) | **40 bytes (fixed)** |
| Header Checksum | Yes | **Removed** |
| Fragmentation by routers | Allowed (if DF = 0) | **Not allowed** (only the source fragments) |
| TTL | TTL | Renamed **Hop Limit** |
| Address size | 32 bits | 128 bits |

---

## 7. Common Exam Pitfalls

- **IHL counts words, not bytes.** `IHL = 5` means 20 bytes, not 5 bytes.
- **Total Length includes the header**, not just the data.
- **Fragment Offset is in 8-byte units.** Multiply by 8 to get bytes.
- **DF = 1 + packet too big → dropped**, with an ICMP error sent back.
- **MF = 0 does not always mean "no fragmentation".** It means "last fragment" (or an unfragmented packet with offset 0).
- **TTL = 0 → drop + ICMP Time Exceeded.**
- **Checksum covers only the header.**
- The **Protocol field** identifies the next layer (TCP 6, UDP 17, ICMP 1, OSPF 89), while **TCP/UDP port numbers** identify the application.

---

## 8. Anki-Style Review Questions

**Q: What is the minimum and maximum size of an IPv4 header?**
A: 20 bytes minimum, 60 bytes maximum.

**Q: What does IHL = 5 mean?**
A: The header is 5 × 4 = 20 bytes long (no options).

**Q: Which field limits a packet's lifetime and prevents routing loops?**
A: TTL (Time To Live), decremented by 1 at each router.

**Q: What happens when a router receives a packet with TTL = 1 and must forward it?**
A: It decrements TTL to 0, drops the packet, and sends an ICMP Time Exceeded message to the source.

**Q: Which field tells the receiver whether the payload is TCP, UDP, ICMP, or OSPF?**
A: The Protocol field (6, 17, 1, 89).

**Q: What is the maximum value of the Total Length field?**
A: 65,535 bytes.

**Q: What is the purpose of the DF flag?**
A: It tells routers not to fragment the packet. If the packet is too large for the link, it is dropped and an ICMP error is returned.

**Q: What does MF = 1 mean?**
A: More fragments follow this one.

**Q: In what unit is Fragment Offset measured?**
A: 8-byte units.

**Q: Which field is shared by all fragments of the same original packet?**
A: Identification.

**Q: Why must routers recalculate the header checksum at every hop?**
A: Because TTL changes at every hop, which changes the header contents.

**Q: Does the IPv4 header checksum protect the payload?**
A: No, only the header.

**Q: Which two fields were formed from the old ToS byte?**
A: DSCP (6 bits) and ECN (2 bits).

**Q: Which IPv4 header field is removed in IPv6?**
A: The Header Checksum (IPv6 also uses a fixed 40-byte header).

**Q: What is the Protocol field value for ICMP, TCP, UDP, and OSPF?**
A: 1, 6, 17, 89.

---

## 9. One-Paragraph Recap

The IPv4 header carries what a router needs to forward a packet: **source and destination addresses**, a **TTL** that stops loops, a **Protocol** number that says what is inside, a **Total Length**, **fragmentation fields** (Identification, Flags, Fragment Offset) for packets larger than the MTU, a **Header Checksum** that is recomputed at every hop, **DSCP/ECN** for QoS, and optional **Options**. The header is 20 bytes by default, up to 60 bytes with options, and its length is given by **IHL** in 4-byte words.
