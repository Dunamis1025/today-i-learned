# Network Layer (OSI Layer 3) — Study Notes

> **Module:** 8.0 — Network Layer  
> **Source:** Cisco Networking Academy (reviewed via Gemini)  
> **Topics:** Network Layer Characteristics · IPv4/IPv6 Packets · Host Routing · Router Routing Tables

---

## Table of Contents

1. [Why Study the Network Layer?](#1-why-study-the-network-layer)
2. [Module Learning Objectives](#2-module-learning-objectives)
3. [What is the Network Layer?](#3-what-is-the-network-layer)
4. [Four Basic Operations of the Network Layer](#4-four-basic-operations-of-the-network-layer)
5. [IP Encapsulation](#5-ip-encapsulation)
6. [Core Characteristics of IP](#6-core-characteristics-of-ip)
7. [Key Concepts & Terminology](#7-key-concepts--terminology)
8. [Summary](#8-summary)

---

## 1. Why Study the Network Layer?

So far, lower OSI layers (Physical, Data Link) have been covered. Those layers handle communication **within** a local network. But what happens when you need to send data to a device on a **completely different network** — a different city or country?

- Switched networks alone **cannot** deliver data across network boundaries.
- **Routers** are required to guide data along the correct path to the final destination.
- The Network Layer provides the protocols that make routers work.

> 💡 **Analogy:** If the Data Link layer is a local courier delivering mail within a building, the Network Layer is the international postal system delivering mail across the entire world.

This module also includes **two Wireshark hands-on labs** to observe real network traffic in action.

---

## 2. Module Learning Objectives

| Topic | What You Will Learn |
|---|---|
| **Network Layer Characteristics** | How IP protocols provide the foundation for end-to-end communication |
| **IPv4 Packet** | Structure and function of IPv4 header fields |
| **IPv6 Packet** | Structure and function of IPv6 header fields (the modern standard) |
| **How a Host Routes** | How devices use routing tables to determine the path to a destination |
| **Router Routing Tables** | Fields in a router's routing table and how forwarding decisions are made |

**Ultimate Goal:** Understand how data travels across different networks — from source to destination — using network layer protocols and routers.

---

## 3. What is the Network Layer?

The **Network Layer (OSI Layer 3)** is responsible for enabling end devices to **exchange data across different networks**.

### Key Protocols at This Layer

| Protocol | Purpose |
|---|---|
| **IPv4** | Primary addressing and routing protocol (widely used) |
| **IPv6** | Modern replacement for IPv4 (larger address space) |
| **OSPF** | Routing protocol — finds the best path between routers |
| **ICMP** | Messaging protocol — reports errors and diagnostics (used by `ping`) |

### Network Layer vs. Transport Layer

| | Transport Layer (Layer 4) | Network Layer (Layer 3) |
|---|---|---|
| **Focus** | Data between processes/applications on a host | Data between hosts across networks |
| **Example** | Managing a TCP connection for a web browser | Routing an IP packet across the internet |

The Network Layer is **media-agnostic** — it does not care whether the data travels over copper cable, fiber optic, or Wi-Fi. This flexibility is what enables the global internet to function across vastly different hardware infrastructures.

---

## 4. Four Basic Operations of the Network Layer

When data travels from a source to a destination, the Network Layer performs **four essential steps**:

### Step 1 — Addressing
- Every end device must have a **unique IP address** so it can be identified and located on the network.
- Without addressing, routers have no way to know where to deliver a packet.

### Step 2 — Encapsulation
- The source host takes the **Transport Layer segment** (data + TCP/UDP header) and wraps it in an **IP header**.
- The IP header contains, at minimum:
  - **Source IP Address**
  - **Destination IP Address**
- The resulting bundle is called an **IP Packet** (Network Layer PDU).

```
[ IP Header | TCP/UDP Header | Application Data ]
       ↑
   Added by Network Layer
```

### Step 3 — Routing
- Routers examine the packet's IP header and **select the best path** toward the destination.
- Each router a packet passes through is called a **hop**.
- Routers use their **routing tables** to make forwarding decisions at every hop.

```
Source Host → Router 1 → Router 2 → ... → Destination Host
              (hop 1)    (hop 2)
```

### Step 4 — De-encapsulation
- When the packet arrives at the destination host, the host reads the IP header.
- If the destination IP matches its own address, the host **strips the IP header** (de-encapsulates).
- The inner data (the Transport Layer segment) is then passed **up to Layer 4**.

> 💡 **Key point:** The data payload remains completely unchanged as it travels through routers. Only the IP header is inspected and used for routing decisions.

---

## 5. IP Encapsulation

### What is Encapsulation?

Encapsulation is the process of **wrapping data from a higher layer with the header information needed by the current layer**.

At the Network Layer, this means taking the Transport Layer segment and adding an **IP header** to form an **IP Packet**.

### The Process Step-by-Step

```
Application Data
       ↓  [Transport Layer adds TCP/UDP header]
   [ TCP Header | Data ]   ← Transport Layer PDU (Segment)
       ↓  [Network Layer adds IP header]
[ IP Header | TCP Header | Data ]   ← Network Layer PDU (Packet)
       ↓  [Data Link Layer adds Frame header/trailer]
[ Frame Header | IP Header | TCP Header | Data | Frame Trailer ]   ← Data Link PDU (Frame)
```

### Why Encapsulation Matters

| Benefit | Explanation |
|---|---|
| **Modular design** | Each layer is independent. Upgrading from IPv4 → IPv6 does not require changing how the Transport Layer works. |
| **Data integrity** | The payload (actual data) is never modified as it passes through routers. |
| **Scalability** | Routers only need to read the IP header — they don't need to understand the data inside. |

### Important Note on IP Addresses

In most cases, the **source and destination IP addresses remain the same** from source to destination. However, devices using **NAT (Network Address Translation)** — such as home routers — may translate addresses. *(NAT will be covered in a later module.)*

---

## 6. Core Characteristics of IP

IP was intentionally designed to be **lightweight and efficient**. It focuses only on delivering packets — nothing more.

### Characteristic 1 — Connectionless

- IP does **not** establish a connection with the destination before sending data.
- There is no "handshake" — no waiting for the receiver to say "I'm ready."
- Data is simply sent out with a destination address and the network does its best.

> 💡 **Analogy:** Like mailing a postcard. You write the address and drop it in the mailbox. You don't wait for the recipient to confirm they're ready to receive it.

### Characteristic 2 — Best Effort (Unreliable)

- IP does **not guarantee delivery**.
- Packets can be:
  - **Lost** in transit
  - **Corrupted/damaged**
  - **Delivered out of order**
- IP does not check for these issues or retransmit lost packets.

**Who handles reliability then?**
→ **TCP (Transport Control Protocol)** at Layer 4 handles:
- Acknowledgements (confirming delivery)
- Retransmission of lost packets
- Ordering of packets

> 💡 IP says "I'll try my best." TCP says "I'll make sure it gets there."

### Characteristic 3 — Media Independent

- IP does **not care** what physical medium carries the data.
- It works the same whether data travels over:
  - Copper cables (Ethernet)
  - Fiber-optic cables
  - Wireless signals (Wi-Fi)
  - Satellite links
- This is what allows the internet to span the entire globe using countless different types of hardware.

### Summary Table

| Characteristic | Description | Who Compensates? |
|---|---|---|
| **Connectionless** | No prior session established before sending | — |
| **Best Effort** | No delivery guarantee; packets may be lost | TCP (Layer 4) |
| **Media Independent** | Works over any physical medium | — |

> 💡 **Why design IP this way?** By keeping IP simple and offloading complex management to upper layers, IP can operate with **very low overhead**, processing enormous amounts of traffic at high speeds.

---

## 7. Key Concepts & Terminology

| Term | Definition |
|---|---|
| **PDU (Protocol Data Unit)** | The name for data at each layer. Layer 3 PDU = Packet, Layer 4 PDU = Segment |
| **IP Header** | The metadata added to a packet containing source/destination IP addresses and other control info |
| **Hop** | Each router a packet passes through on its way to the destination |
| **Routing Table** | A "map" inside a router that tells it where to forward a packet based on the destination IP |
| **Encapsulation** | Wrapping data with a header at the current layer |
| **De-encapsulation** | Stripping a header at the destination layer |
| **NAT** | Network Address Translation — a technique that modifies IP addresses (usually at a home router) |
| **ICMP** | Internet Control Message Protocol — used for error reporting and network diagnostics (e.g., `ping`) |
| **OSPF** | Open Shortest Path First — a routing protocol used to find the best paths between routers |
| **IPv4** | 32-bit IP addressing scheme (e.g., 192.168.1.1) |
| **IPv6** | 128-bit IP addressing scheme, the modern standard replacing IPv4 |

---

## 8. Summary

```
┌─────────────────────────────────────────────────────────────┐
│                  NETWORK LAYER (OSI Layer 3)                │
├─────────────────────────────────────────────────────────────┤
│  PURPOSE: Enable communication between devices on different │
│           networks (end-to-end connectivity)                │
├─────────────────────────────────────────────────────────────┤
│  KEY PROTOCOLS: IPv4, IPv6, ICMP, OSPF                      │
├─────────────────────────────────────────────────────────────┤
│  4 OPERATIONS:                                              │
│    1. Addressing    → Unique IP address for every device    │
│    2. Encapsulation → Wrap data in IP header → IP Packet    │
│    3. Routing       → Best path selection via routers       │
│    4. De-encap      → Strip IP header at destination        │
├─────────────────────────────────────────────────────────────┤
│  IP CHARACTERISTICS:                                        │
│    • Connectionless  (no pre-established session)           │
│    • Best Effort     (no delivery guarantee → TCP handles)  │
│    • Media Indep.    (works over any physical medium)       │
└─────────────────────────────────────────────────────────────┘
```

The Network Layer is the backbone of internet communication. By keeping IP simple — connectionless, best-effort, and media-independent — the protocol can operate at enormous scale. The complexity of ensuring reliable communication is deliberately delegated to higher layers (TCP at Layer 4), keeping the overall system efficient and modular.

---

*Next topics to study: IPv4 Packet Structure · IPv6 Packet Structure · Host Routing · Router Routing Tables*
