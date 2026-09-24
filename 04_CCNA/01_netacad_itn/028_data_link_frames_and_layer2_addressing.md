# 28 - Data Link Frames and Layer 2 Addressing

## Overview

This document covers the structure of data link frames, frame fields, Layer 2 addressing, and the different data link layer protocols used across LAN and WAN environments. These concepts are fundamental to understanding how data is packaged and delivered across a local network.

---

## 6.3.1 The Frame

### What is a Frame?

A **data link frame** is the encapsulated unit of data used by the data link layer to transport information across local media. It is created by wrapping an IP packet (Layer 3) with a **header** and a **trailer**.

- The **data link layer** is responsible for **NIC-to-NIC communication** within the same network.
- The information appended to a frame (header/trailer content) is determined by the **protocol being used**.

### Three Basic Parts of Every Frame

| Part | Description |
|------|-------------|
| **Header** | Contains addressing and control information at the beginning of the frame |
| **Data** | The encapsulated Layer 3 packet (IPv4 or IPv6) |
| **Trailer** | Appended at the end — unique to the data link layer; used for error detection |

> **Key point:** Unlike other encapsulation protocols, the data link layer appends control information at **both the beginning (header) and the end (trailer)** of the frame.

### Variable Frame Structures

There is **no universal frame structure** — the format varies depending on the environment:

- The amount of control information in the header/trailer varies based on **media type** and **logical topology**.
- A **WLAN frame** requires more control information than an **Ethernet frame** because wireless media must include collision avoidance procedures.
- **General rule:** The more fragile or unreliable the environment, the larger the header and trailer fields need to be.

---

## 6.3.2 Frame Fields

### How Framing Works

Framing breaks a stream of bits into **decipherable groupings**. Control information is inserted in specific fields within the header and trailer so that receiving nodes can:
- Identify the frame boundaries
- Decode the contents into packets

### Generic Frame Fields

```
┌──────────────┬─────────────┬──────────┬─────────┬──────┬──────────────────┬────────────┐
│ Frame Start  │ Addressing  │   Type   │ Control │ Data │  Error Detection │ Frame Stop │
└──────────────┴─────────────┴──────────┴─────────┴──────┴──────────────────┴────────────┘
└───────────────────────── Header ──────────────────────┘      └────── Trailer ──────────┘
```

### Field Descriptions

| Field | Purpose |
|-------|---------|
| **Frame Start / Stop** | Identifies the beginning and end boundaries of the frame |
| **Addressing** | Specifies source and destination nodes on the local media (MAC addresses) |
| **Type** | Identifies the Layer 3 protocol contained in the data field (e.g., IPv4, IPv6) |
| **Control** | Identifies special flow control services such as **Quality of Service (QoS)**. For example, VoIP frames are given forwarding priority because voice is sensitive to delay |
| **Data** | Contains the frame payload — the Layer 3 packet header, segment header, and data |
| **Error Detection** | Included after the data field to form the trailer; used to verify frame integrity |

> **Note:** Not all protocols use all of these fields. The actual frame format is defined by the specific data link protocol standard being used.

### Error Detection — CRC and FCS

The data link layer adds error detection because signals on physical media can be subject to **interference, distortion, or loss** that changes bit values.

**How it works:**

1. The **transmitting node** performs a mathematical calculation on all bits in the frame.
2. This result is called the **CRC (Cyclic Redundancy Check)** value.
3. The CRC value is placed in the **FCS (Frame Check Sequence)** field in the trailer.
4. The **receiving node** performs the same calculation on the received frame.
5. If the computed value **matches** the FCS field → ✅ No errors.
6. If the values **differ** → ❌ Transmission error detected.

```
Sender:   [Frame Data] → CRC calculation → Place CRC in FCS → Transmit
Receiver: [Frame Data] → CRC calculation → Compare with FCS → Match? ✅ / Mismatch? ❌
```

---

## 6.3.3 Layer 2 Addresses

### Physical vs. Logical Addresses

The network uses **two types of addresses** at different layers:

| Feature | Layer 2 Address (MAC) | Layer 3 Address (IP) |
|---------|----------------------|----------------------|
| **Also called** | Physical address | Logical address |
| **Example** | `AA:BB:CC:DD:EE:FF` | `192.168.1.110` |
| **Scope** | Local network only | Global (end-to-end) |
| **Changes per hop?** | ✅ Yes — changes at every router | ❌ No — stays the same throughout |
| **Assigned to** | The NIC hardware | The network interface logically |

> **Key distinction:** Layer 2 addresses do **not** indicate which network a device belongs to. They are unique to the device itself. Even if a device moves to another network, its Layer 2 address stays the same — but it becomes meaningless on the new network.

### How L2 and L3 Work Together

As a packet travels from source host to destination host through routers, it is **re-encapsulated in a new Layer 2 frame at each hop**. Each frame contains:
- The **source MAC** of the NIC currently sending
- The **destination MAC** of the NIC on the next hop

**Example:** `PC1 (192.168.1.110)` → `Web Server (172.16.1.99)`

```
Hop 1 — PC1 to R1:
  L2 Header: [Src: PC1 MAC | Dst: R1 MAC]
  L3 Packet: [Src IP: 192.168.1.110 | Dst IP: 172.16.1.99]

Hop 2 — R1 to R2:
  L2 Header: [Src: R1 MAC  | Dst: R2 MAC]   ← New frame!
  L3 Packet: [Src IP: 192.168.1.110 | Dst IP: 172.16.1.99]  ← Unchanged

Hop 3 — R2 to Web Server:
  L2 Header: [Src: R2 MAC  | Dst: Server MAC] ← New frame again!
  L3 Packet: [Src IP: 192.168.1.110 | Dst IP: 172.16.1.99]  ← Unchanged
```

### The Role of the Router

When a packet must cross into a **different network**, a router is required:

1. Router **accepts the frame** based on its physical (MAC) address.
2. Router **de-encapsulates** (removes) the Layer 2 frame.
3. Router **examines the Layer 3 IP address** to determine the next destination.
4. Router **creates a new Layer 2 frame** with updated MAC addresses.
5. Router **forwards** the new frame to the next network segment.

> **Summary:** MAC addresses are local delivery labels that change at every router hop. IP addresses are the permanent destination that never change during the trip.

---

## 6.3.4 Data Link Layer Protocols

### Protocol Selection Depends on the Network

The Layer 2 protocol used depends on:
- **Network size** — number of hosts
- **Geographic scope** — building vs. city vs. country
- **Type of service** to be provided

### LAN vs. WAN Protocols

| Network Type | Characteristics | Typical Protocols |
|-------------|----------------|------------------|
| **LAN** | Small geographic area (building/campus), high user density, high bandwidth cost-effective | Ethernet, 802.11 (Wi-Fi) |
| **WAN** | Large geographic area (cities/countries), long-distance links are expensive, lower bandwidth capacity | PPP, HDLC, Frame Relay (legacy) |

> Using high-bandwidth technology over long WAN distances is not cost-effective — the cost of long-distance physical links typically results in lower bandwidth capacity, which is why different protocols were historically used for WANs.

### Common Layer 2 Protocols

| Protocol | Full Name | Used For |
|----------|-----------|----------|
| **Ethernet** | IEEE 802.3 | Wired LAN (most common today) |
| **802.11 Wireless** | IEEE 802.11 | Wireless LAN (Wi-Fi) |
| **PPP** | Point-to-Point Protocol | Direct 1-to-1 WAN connections |
| **HDLC** | High-Level Data Link Control | Legacy WAN; default on Cisco routers |
| **Frame Relay** | — | Legacy WAN packet switching (largely obsolete) |
| **ATM** | Asynchronous Transfer Mode | Legacy high-speed WAN (not the banking ATM!) |
| **X.25** | — | Very old packet-switched WAN protocol |

> **Trend:** Legacy WAN protocols (PPP, HDLC, Frame Relay, ATM, X.25) are increasingly being **replaced by Ethernet** even in WAN environments.

### Design Principle

Each Layer 2 protocol performs **media access control** for a specific logical topology. Devices that operate at this layer include:
- NICs on computers
- Interfaces on routers
- Layer 2 switches

---

## Key Takeaways

1. **Frames** wrap IP packets with a header and trailer for local delivery — the structure varies by protocol and media type.
2. **Frame fields** include start/stop flags, addressing, type, control (QoS), data, and error detection (CRC/FCS).
3. **Error detection** uses CRC to generate a checksum placed in the FCS field of the trailer — the receiver verifies integrity by recalculating and comparing.
4. **Layer 2 (MAC) addresses** are local-only and change at every router hop; **Layer 3 (IP) addresses** are end-to-end and never change.
5. **Routers** strip the old Layer 2 frame, read the IP address, and build a brand-new Layer 2 frame for the next hop.
6. **Protocol choice** depends on network size and geography — Ethernet dominates LANs; legacy WAN protocols are fading in favor of Ethernet.
