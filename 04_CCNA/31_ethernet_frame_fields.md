# 7.1.4 Ethernet Frame Fields

## Overview

Ethernet is the most widely used LAN technology today. When data is transmitted over an Ethernet network, it is encapsulated into a structured unit called an **Ethernet Frame**. Understanding the structure of an Ethernet frame is fundamental to networking.

---

## Frame Size Requirements

Every Ethernet frame must conform to strict size constraints:

| Constraint | Size | Notes |
|-----------|------|-------|
| **Minimum frame size** | 64 bytes | Measured from Destination MAC Address through FCS |
| **Maximum frame size** | 1518 bytes | Standard maximum; excludes preamble |
| **Maximum data payload** | 1500 bytes | The Data field alone |

> **Important:** The **Preamble** field is **not** counted when measuring frame size. Size is calculated from the Destination MAC Address field through the Frame Check Sequence (FCS) field.

> **Note:** Frame size may exceed 1518 bytes if additional features like **VLAN tagging** are applied, but this is considered beyond standard scope.

---

## Frame Size Edge Cases

### Undersized Frames (< 64 bytes)
- Called **"collision fragments"** or **"runt frames"**
- Automatically **discarded** by receiving network devices
- Most commonly caused by **signal collisions** on the network
- Considered **invalid frames**

### Oversized Frames (> 1500 bytes of data)
- Called **"jumbo frames"** or **"baby giant frames"**
- Generally supported by most modern **Fast Ethernet** and **Gigabit Ethernet** switches and NICs
- If a frame exceeds the maximum allowed size and jumbo frames are not supported, the receiving device **drops the frame**

### Why the minimum size matters
If a transmitted frame is smaller than the minimum or larger than the maximum, the receiving device drops the frame. Dropped frames are usually the result of collisions or other unwanted signals and are considered invalid.

---

## Ethernet Frame Structure

```
|<-------------------------------- 64 - 1518 bytes -------------------------------->|
|            |                                                                      |
|  8 bytes   |                   (counted in frame size)                           |
+------------+------------+------------+------------+------------------+-----------+
| Preamble & |    Dest.   |   Source   |   Type /   |       Data       |    FCS    |
|    SFD     | MAC Address| MAC Address|   Length   |  (46-1500 bytes) | (4 bytes) |
|  (8 bytes) |  (6 bytes) |  (6 bytes) |  (2 bytes) |                  |           |
+------------+------------+------------+------------+------------------+-----------+
```

---

## Field-by-Field Breakdown

### 1. Preamble and SFD (Start of Frame Delimiter)
- **Size:** 8 bytes (Preamble: 7 bytes + SFD: 1 byte)
- **Purpose:** Synchronizes communication between sender and receiver
- The **Preamble** (7 bytes) consists of alternating 1s and 0s that alert receiving devices that a frame is incoming and allows them to synchronize their clocks
- The **SFD** (1 byte) signals that the next byte begins the Destination MAC Address field — essentially saying *"the actual frame data starts NOW"*
- **Not counted** in the frame size calculation
- **Quiz relevance:** Does NOT detect errors, does NOT identify protocols

---

### 2. Destination MAC Address
- **Size:** 6 bytes (48 bits)
- **Purpose:** Identifies the **intended recipient** of the frame
- A MAC (Media Access Control) address is a hardware address permanently burned into a network interface card (NIC)
- Format: `XX:XX:XX:XX:XX:XX` (hexadecimal)
- Can be a **unicast** (single device), **multicast** (group), or **broadcast** (`FF:FF:FF:FF:FF:FF`) address
- Receiving devices compare this field to their own MAC address to decide whether to process the frame

---

### 3. Source MAC Address
- **Size:** 6 bytes (48 bits)
- **Purpose:** Identifies the **sender** of the frame
- Always a unicast address (a frame can only come from one device)
- Used by network switches to **learn** which devices are on which ports (building the MAC address table)

---

### 4. EtherType / Length
- **Size:** 2 bytes
- **Dual purpose field:**
  - If value is **≥ 1536 (0x0600)** → interpreted as **EtherType** (identifies the upper-layer protocol)
  - If value is **≤ 1500** → interpreted as **Length** (indicates the size of the data payload)

#### Common EtherType Values
| Value (Hex) | Protocol |
|-------------|----------|
| `0x0800` | IPv4 |
| `0x86DD` | IPv6 |
| `0x0806` | ARP (Address Resolution Protocol) |
| `0x8100` | VLAN-tagged frame (802.1Q) |

- **Quiz relevance:** This field describes the **higher-layer protocol that is encapsulated** in the frame ✅

---

### 5. Data Field (Payload)
- **Size:** 46 – 1500 bytes
- **Purpose:** Carries the **actual data** being transmitted (e.g., part of a web page, email, video stream)
- The data here is typically an **IP packet** passed down from the Network Layer (Layer 3)

#### Padding
- If the data being sent is **less than 46 bytes**, the Data field is **padded** with extra bytes (zeros) to reach the minimum of 46 bytes
- This ensures the total frame meets the **minimum 64-byte requirement**
- **Quiz relevance:** The Data field uses **padding** to increase the frame to at least 64 bytes ✅

---

### 6. Frame Check Sequence (FCS)
- **Size:** 4 bytes
- **Purpose:** **Error detection** — verifies that the frame arrived without corruption

#### How FCS Works (CRC Process)
1. The sender performs a mathematical calculation called **CRC (Cyclic Redundancy Check)** on the frame contents
2. The resulting value is stored in the FCS field
3. The receiver performs the **same CRC calculation** on the received frame
4. If the receiver's result **matches** the FCS value → ✅ Frame is valid
5. If they **don't match** → ❌ Frame was corrupted in transit → Frame is **discarded**

> **Note:** FCS only **detects** errors — it does **not correct** them. If a frame is dropped, higher-layer protocols (like TCP) handle retransmission.

- **Quiz relevance:** FCS is the part of an Ethernet frame that **detects errors** ✅

---

## Summary Table

| Field | Size | Role | Key Point |
|-------|------|------|-----------|
| **Preamble & SFD** | 8 bytes | Sync signal + frame start indicator | Not counted in frame size |
| **Destination MAC** | 6 bytes | Who receives the frame | Unicast / Multicast / Broadcast |
| **Source MAC** | 6 bytes | Who sent the frame | Always unicast |
| **EtherType / Length** | 2 bytes | Upper-layer protocol identifier | IPv4=0x0800, IPv6=0x86DD |
| **Data** | 46–1500 bytes | Actual payload | Padded if < 46 bytes |
| **FCS** | 4 bytes | Error detection (CRC) | Drops frame if mismatch |

---

## Quiz Review

| Question | Answer | Reason |
|----------|--------|--------|
| Which field uses padding to reach 64 bytes? | **Data field** | Pads with zeros if payload < 46 bytes |
| Which field detects errors in the frame? | **Frame Check Sequence (FCS)** | Uses CRC to verify data integrity |
| Which field describes the higher-layer protocol encapsulated? | **EtherType** | Identifies IPv4, IPv6, ARP, etc. |

---

## Key Takeaways

- Ethernet frames must be between **64 and 1518 bytes** (excluding preamble)
- Frames outside this range are **automatically dropped**
- Each field has a **specific, non-overlapping role** in frame delivery and integrity
- **FCS** ensures data integrity; **EtherType** ensures proper protocol handling; **Padding** ensures minimum frame size compliance
- MAC addresses operate at **Layer 2 (Data Link Layer)** of the OSI model

---

*Study notes based on CCNA / Networking Fundamentals — Section 7.1.4*
