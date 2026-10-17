# Day 10 – Anki Review: Fiber Distances & IPv4 Header Fields (CCNA 200-301)

> Study date: 2026-10-17
> Focus: 10G Ethernet fiber standards, IPv4 header layout, bit sizes, units, fragmentation, MTU, TTL, DSCP

---

## 1. 10G Ethernet Fiber Standards

| Standard | Max Distance | Fiber Type | Notes |
|---|---|---|---|
| 10GBASE-SR | 33 m (OM1), 82 m (OM2), 300 m (OM3), 400 m (OM4) | Multimode (MMF) | Short Reach, 850 nm |
| 10GBASE-LR | 10 km | Single-mode (SMF) | Long Reach, 1310 nm |
| 10GBASE-ER | 40 km | Single-mode (SMF) | Extended Reach, 1550 nm |

### Key points
- **10G** = 10 Gbps, **BASE** = baseband signaling, **LR** = Long Reach, **SR** = Short Reach.
- Single-mode fiber has a very thin core, so light travels a single path with little dispersion, allowing long distances.
- Higher OM number (OM1 → OM4) = better multimode fiber = longer distance at the same speed.
- Many vendors guarantee longer reach on OM4 for SR optics (e.g. 550 m), but the standard value to remember is **400 m for OM4**.
- Specified maximums are limits; connectors and splices add loss and can reduce real-world distance.

**Memory hook:** SR = short = multimode (hundreds of meters). LR = long = single-mode (10 km). ER = extended = 40 km.

---

## 2. IPv4 Header Layout (32 bits per row)

The header is drawn as rows of **32 bits (4 bytes)**. The minimum header is **5 rows = 20 bytes**.

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-------+-------+-----------+---+-------------------------------+
|Version|  IHL  |   DSCP    |ECN|         Total Length          |  Row 1
+-------+-------+-----------+---+-------------------------------+
|        Identification         |Flags|    Fragment Offset      |  Row 2
+---------------+---------------+-----+-------------------------+
|      TTL      |   Protocol    |        Header Checksum        |  Row 3
+---------------+---------------+-------------------------------+
|                       Source Address                          |  Row 4
+---------------------------------------------------------------+
|                    Destination Address                        |  Row 5
+---------------------------------------------------------------+
|                    Options (if IHL > 5)                       |  Row 6+
+---------------------------------------------------------------+
```

### Bit sizes per row (every row sums to 32)

| Row | Fields | Sum |
|---|---|---|
| 1 | Version 4 + IHL 4 + DSCP 6 + ECN 2 + Total Length 16 | 32 |
| 2 | Identification 16 + Flags 3 + Fragment Offset 13 | 32 |
| 3 | TTL 8 + Protocol 8 + Header Checksum 16 | 32 |
| 4 | Source Address 32 | 32 |
| 5 | Destination Address 32 | 32 |

**Trick:** if you forget one field size, subtract the others from 32.
- DSCP = 32 − 4 − 4 − 2 − 16 = **6**
- Fragment Offset = 32 − 16 − 3 = **13**
- TTL = 32 − 8 − 16 = **8**

---

## 3. IHL (Internet Header Length)

- The IHL **field is 4 bits** (can hold 0–15). This is the size of the box.
- The **value stored** is the number of **32-bit words (rows)** in the header, not bytes. One word = 4 bytes.
- Header length in bytes = IHL × 4.

| IHL (binary) | IHL (decimal) | Header length |
|---|---|---|
| 0101 | 5 | 20 bytes (minimum, no options) |
| 0110 | 6 | 24 bytes |
| 1111 | 15 | **60 bytes (maximum)** |

- Options can add up to 40 bytes (60 − 20) and are padded to a multiple of 4 bytes.
- The first byte of most IPv4 packets is `0x45` (Version 4, IHL 5).
- **Why count in 4-byte words?** A 4-bit field would max out at 15 bytes if counted in bytes, which is smaller than the basic 20-byte header. Counting in 4-byte units extends the range to 60 bytes.

**Answer to remember:** Maximum IPv4 header length = **60 bytes**. Minimum = **20 bytes**.

---

## 4. Field Size vs. Stored Value (common confusion)

| Field | Field size (bits) | Typical stored value |
|---|---|---|
| IHL | 4 bits | 5 (5 rows = 20 bytes) |
| TTL | 8 bits | 64 (default) |

- "How many **bits** is the field?" → size of the box.
- "What is the **default / typical** value?" → what is written inside.

---

## 5. DSCP and ECN (Row 1)

- Originally one byte called **ToS (Type of Service)**, later redefined as:
  - **DSCP** (Differentiated Services Code Point) – **6 bits** – traffic priority marking for **QoS**.
  - **ECN** (Explicit Congestion Notification) – **2 bits** – signals network congestion.
- DSCP is the field used to **prioritize delay-sensitive traffic** (VoIP, video calls, gaming) over delay-tolerant traffic (file downloads, email).
- Routers read DSCP to decide which packets to forward first.

---

## 6. Fragmentation Fields (Row 2)

Fragmentation happens when a packet is larger than the **MTU** of a link.

### Identification (16 bits)
- Same value on every fragment of the same original packet, so the receiver knows which fragments belong together.

### Flags (3 bits)

| Bit | Name | Meaning |
|---|---|---|
| 1 | Reserved | Always 0 |
| 2 | **DF** (Don't Fragment) | 1 = do not fragment this packet |
| 3 | **MF** (More Fragments) | 1 = more fragments follow; 0 = last fragment (or unfragmented) |

- If DF = 1 and the packet exceeds the MTU, the router drops it and returns an ICMP error. **Path MTU Discovery** relies on this behavior.

### Fragment Offset (13 bits)
- Indicates the **position of a fragment within the original, unfragmented packet's data**.
- Measured in **8-byte units**: actual byte offset = value × 8.
- Why 8-byte units? Total Length is 16 bits (max 65,535 bytes), but only 13 bits remain after Identification (16) and Flags (3). 13 bits max = 8,191; 8,191 × 8 ≈ 65,528, which covers the full packet range.
- Consequence: every fragment except the last must carry a data length that is a **multiple of 8 bytes**.

### Example (1,480-byte fragments of a 4,000-byte payload)

| Fragment | Data bytes | Start offset (bytes) | Fragment Offset field | MF |
|---|---|---|---|---|
| 1 | 0 – 1,479 | 0 | 0 | 1 |
| 2 | 1,480 – 2,959 | 1,480 | 185 | 1 |
| 3 | 2,960 – 3,999 | 2,960 | 370 | 0 |

### Reassembly in one sentence
The receiver groups fragments by **Identification**, orders them by **Fragment Offset**, and knows it is complete when the fragment with **MF = 0** arrives.

---

## 7. MTU (Maximum Transmission Unit)

- Largest IP packet (header + payload) that can be sent on a link without fragmentation.
- Ethernet default MTU = **1500 bytes**.
- With a 20-byte IPv4 header, the maximum payload = 1500 − 20 = **1480 bytes** (which is divisible by 8: 8 × 185).

---

## 8. TTL (Time To Live)

- **8 bits** wide → range 0–255.
- Decremented by 1 at each router hop; the packet is discarded when it reaches 0 (prevents infinite routing loops).
- **Recommended default: 64** (common on Linux/macOS). Windows commonly uses 128.

---

## 9. Quick Q&A (Anki-style)

| Question | Answer |
|---|---|
| 10GBASE-LR maximum cable length? | 10 km (single-mode fiber) |
| 10GBASE-SR maximum length on OM4? | 400 m |
| Maximum length of the IPv4 header? | 60 bytes |
| Minimum length of the IPv4 header? | 20 bytes |
| IHL field size / typical value? | 4 bits / 5 |
| Fragment Offset field is how many bits? | 13 |
| Fragment Offset unit? | 8 bytes |
| DSCP field is how many bits? | 6 |
| TTL field is how many bits? | 8 |
| Recommended default TTL? | 64 |
| Which field indicates the position of a fragment in the original packet? | Fragment Offset |
| Which field prioritizes delay-sensitive traffic? | DSCP |
| Typical Ethernet MTU? | 1500 bytes |
| Which flag means "no more fragments after this"? | MF = 0 |

---

## 10. Takeaways

1. Every IPv4 header row is 32 bits; check that each row sums to 32 to recover forgotten sizes.
2. Some fields store a **count in units** rather than raw bytes: IHL (4-byte words) and Fragment Offset (8-byte units).
3. Separate "size of the field" from "value stored in the field" (IHL 4 bits vs value 5; TTL 8 bits vs value 64).
4. Fragmentation = Identification (which packet) + Fragment Offset (where) + MF flag (is it the last one).
