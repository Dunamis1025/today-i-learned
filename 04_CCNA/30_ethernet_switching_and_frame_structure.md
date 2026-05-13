# 30. Ethernet Switching and Frame Structure

## Overview

This note covers how Ethernet operates within a switched Local Area Network (LAN), including the role of the MAC sublayer, how Ethernet frames are structured, and how switches use MAC address tables to forward data efficiently.

---

## 1. What Is Ethernet Switching?

Ethernet Switching is the core technology that enables devices within a LAN to communicate efficiently. Unlike older **hubs** (which broadcast data to every port), a **switch** learns which device is on which port and sends data only to the intended recipient.

### Key Topics in This Module

| Topic | Description |
|---|---|
| Ethernet Frame | The basic unit of data at the Ethernet layer |
| Ethernet MAC Address | Unique hardware identifier used to direct frames |
| MAC Address Table | A switch's internal "map" of which device is on which port |
| Switch Forwarding Methods | How switches decide when and how to forward frames (e.g., store-and-forward, cut-through) |

---

## 2. Ethernet Encapsulation

Ethernet is one of the two dominant LAN technologies today (the other being WLAN — Wireless LAN). It operates at:

- **Layer 1 (Physical Layer):** Handles transmission over cables (twisted pair, fiber-optic, coaxial)
- **Layer 2 (Data Link Layer):** Handles logical addressing and frame structure

Defined by IEEE standards **802.2** (LLC) and **802.3** (MAC/Ethernet).

### Supported Data Rates

| Speed | Name |
|---|---|
| 10 Mbps | Ethernet |
| 100 Mbps | Fast Ethernet |
| 1,000 Mbps (1 Gbps) | Gigabit Ethernet |
| 10,000 Mbps (10 Gbps) | 10 Gigabit Ethernet |
| 40,000 Mbps | 40 Gigabit Ethernet |
| 100,000 Mbps | 100 Gigabit Ethernet |

---

## 3. Data Link Sublayers

The Data Link Layer (Layer 2) is divided into two sublayers under IEEE 802 LAN/MAN standards:

### 3.1 LLC Sublayer (Logical Link Control — IEEE 802.2)

- Acts as the **interface between network software (Layer 3) and hardware (Layer 1)**
- Identifies which Layer 3 protocol is being carried (e.g., IPv4, IPv6) by inserting protocol information into the frame
- Allows multiple Layer 3 protocols to share the same physical network interface

> **Analogy:** The LLC is like a label on a package that says "Contents: IPv4 data" so the receiver knows how to process it without opening it.

### 3.2 MAC Sublayer (Media Access Control — IEEE 802.3 / 802.11)

- Primarily implemented in **hardware** (NIC)
- Responsible for two main functions:
  1. **Data Encapsulation** — building the Ethernet frame
  2. **Media Access Control** — managing who can use the shared communication channel

> **Analogy:** The MAC is like the delivery driver who writes the physical address on the box and decides which route (cable type) to use.

---

## 4. MAC Sublayer: Data Encapsulation

When the MAC sublayer encapsulates data into an Ethernet frame, it performs three tasks:

| Task | Description |
|---|---|
| **Ethernet Frame** | Structures the data into a defined format |
| **Ethernet Addressing** | Adds source and destination MAC addresses |
| **Error Detection (FCS)** | Appends a Frame Check Sequence to detect transmission errors |

---

## 5. MAC Sublayer: Media Access Control

Multiple devices may share the same communication medium. The MAC sublayer manages access to prevent data collisions.

### 5.1 Legacy Method — CSMA/CD (Half-Duplex)

- Used in older shared-medium networks (hubs)
- Devices **listen before transmitting** to check if the channel is free
- If two devices transmit simultaneously → **collision** occurs
- After a collision, both devices wait a random amount of time before retrying
- Still referenced in standards but rarely used in modern networks

### 5.2 Modern Method — Full-Duplex (Switched Networks)

- Used with modern **switches**
- Data can travel in **both directions simultaneously** — no collisions
- No need to wait or detect collisions
- Significantly faster and more efficient

---

## 6. Ethernet Frame Structure

Every Ethernet frame must fall within a specific size range and follow a strict field layout.

### 6.1 Frame Size Limits

| Limit | Size | Notes |
|---|---|---|
| **Minimum** | 64 bytes | Smaller frames are called "runt frames" and are discarded |
| **Maximum** | 1518 bytes | Larger frames are called "Jumbo" or "Baby Giant" frames |

Frames outside these limits are automatically **dropped** by the receiving device as they likely result from errors or collisions.

### 6.2 Ethernet Frame Fields

| Field | Size | Purpose |
|---|---|---|
| **Preamble** | 7 bytes | Signals the start of the frame; allows receiver to synchronize |
| **Start Frame Delimiter (SFD)** | 1 byte | Marks the exact start of the frame |
| **Destination MAC Address** | 6 bytes | Physical address of the intended recipient |
| **Source MAC Address** | 6 bytes | Physical address of the sender |
| **Type / Length** | 2 bytes | Identifies the Layer 3 protocol (e.g., 0x0800 = IPv4) or frame length |
| **Data (Payload)** | 46–1500 bytes | The actual data being transmitted |
| **FCS (Frame Check Sequence)** | 4 bytes | CRC value used to detect errors; if mismatched, the frame is discarded |

> **Note:** If the payload is smaller than 46 bytes, **padding** is added to meet the minimum frame size of 64 bytes.

---

## 7. How a Switch Uses the MAC Address Table

1. **Learning:** When a frame arrives, the switch records the **source MAC address** and the **port** it came from into its MAC address table.
2. **Forwarding:** When forwarding a frame, the switch looks up the **destination MAC address** in its table and sends the frame only to the correct port.
3. **Flooding:** If the destination MAC address is not yet in the table, the switch **floods** the frame to all ports (except the one it came from) until it learns the destination.

---

## 8. Cybersecurity Relevance

Understanding Ethernet switching and frame structure is foundational for the following security topics:

- **MAC Spoofing:** Attackers can forge the source MAC address in a frame to impersonate another device
- **MAC Flooding:** Sending large numbers of frames with fake MAC addresses to overwhelm a switch's MAC address table, forcing it to flood traffic like a hub (enabling eavesdropping)
- **ARP Poisoning:** Exploiting Layer 2 addressing to redirect traffic between hosts
- **Packet Analysis (Wireshark):** Inspecting Ethernet frame fields to detect anomalies or malicious traffic
- **Malformed Frames:** Attackers may send frames outside the valid size range to crash or confuse network devices

---

## Summary

| Concept | Key Point |
|---|---|
| Ethernet Switching | Sends data only to the intended recipient using MAC addresses |
| LLC Sublayer | Identifies the Layer 3 protocol; bridges software and hardware |
| MAC Sublayer | Handles frame construction, addressing, and media access |
| Ethernet Frame | Structured data unit with strict size limits (64–1518 bytes) |
| FCS | Detects transmission errors; mismatched frames are dropped |
| Full-Duplex | Modern standard; simultaneous bidirectional transmission, no collisions |
| MAC Address Table | Switch's memory of which device lives on which port |
