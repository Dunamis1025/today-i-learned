# 29. Data Link Layer - Practice Questions and Review

## Overview

This document covers **Module 6** of the Cisco Networking Academy CCNA course, focusing on the Data Link Layer (OSI Layer 2), its sublayers, topologies, frame structure, and media access control methods.

---

## 1. Purpose of the Data Link Layer (Layer 2)

- Responsible for **NIC-to-NIC communication** within the same network
- Prepares data for transmission over the physical network
- Works with **IP at Layer 3** in a TCP/IP network

### Two Sublayers of Layer 2 (IEEE 802 LAN/MAN)

| Sublayer | Full Name | Role |
|----------|-----------|------|
| **LLC** | Logical Link Control | Acts as a bridge to Layer 3 — identifies which network layer protocol is being used (IPv4 or IPv6) |
| **MAC** | Media Access Control | Handles frame creation, addressing, error detection, and media access control |

### Standards Organizations for Layer 2
- **IEEE** – Institute of Electrical and Electronics Engineers
- **ITU** – International Telecommunication Union
- **ISO** – International Organization for Standardization
- **ANSI** – American National Standards Institute

---

## 2. Data Link Frame Structure

When Layer 2 receives a packet from Layer 3, it wraps it with a **header** and a **trailer** to create a **frame**.

```
| Header | Data (Layer 3 Packet) | Trailer |
```

### Frame Fields

| Field | Location | Purpose |
|-------|----------|---------|
| Start/Stop flags | Header | Marks where the frame begins and ends |
| Source MAC address | Header | Where the frame is coming from |
| Destination MAC address | Header | Where the frame is going |
| Type | Header | Identifies what's inside (IPv4 or IPv6) |
| Data | Middle | The actual Layer 3 packet |
| FCS (Frame Check Sequence) | Trailer | Detects errors — checks if data was damaged during transmission |

### Key Points
- **MAC addresses are only used within the same local network** — they change at every router hop
- **IP addresses remain the same** end-to-end across networks
- There is **no single universal frame structure** — it varies depending on the media (Ethernet, Wi-Fi, PPP, etc.)

### Correct Address Order in a Frame
```
Destination MAC → Source MAC → Destination IP → Source IP
```
> Think of it like a mailing label — recipient always comes first.

---

## 3. Topologies

### Physical vs Logical Topology

| Type | Definition |
|------|-----------|
| **Physical Topology** | How devices are actually connected with cables |
| **Logical Topology** | How data actually flows through the network |

> Changing the physical connections does **not** always change the logical topology.

### WAN Physical Topologies
- **Point-to-point** – Direct connection between two devices
- **Hub-and-spoke** – One central hub connected to multiple branches
- **Mesh** – Every device connected to every other device

### LAN Physical Topologies
- **Star** – All devices connect to a central switch/hub ⭐ *(most common today)*
- **Extended Star** – Multiple stars connected together
- **Bus** – All devices share one cable
- **Ring** – Devices connected in a circle

### Topology Quick Reference

| Topology | Key Feature | Pros | Cons |
|----------|------------|------|------|
| **Star** | Central device (switch/hub) | Easy to manage | Central device = single point of failure |
| **Mesh** | Every node connects to every other node | Highest redundancy | Very expensive (lots of cables) |
| **Bus** | One shared cable | Simple, cheap | One break = whole network down |
| **Ring** | Circle of connections | Predictable traffic | One break = whole network down |

> **Mesh = highest redundancy** because even if one path fails, data can reroute through another path.

---

## 4. Duplex Communication

| Mode | Description | Real-life Example |
|------|-------------|------------------|
| **Half-duplex** | One direction at a time | Walkie-talkie (무전기) |
| **Full-duplex** | Both directions simultaneously | Phone call (전화) |
| **Simplex** | One direction only, forever | TV broadcast |

### Important Rule
- Both connected devices **must use the same duplex mode**
- A **duplex mismatch** causes slowdowns and latency on the link

---

## 5. Media Access Control Methods

When multiple devices share the same network, rules are needed to control who sends when.

### Contention-Based Access (충돌 기반)

| Method | Full Name | Used In | How It Works |
|--------|-----------|---------|--------------|
| **CSMA/CD** | Carrier Sense Multiple Access / **Collision Detection** | Wired Ethernet (legacy hubs) | Detects collision after it happens → retransmits |
| **CSMA/CA** | Carrier Sense Multiple Access / **Collision Avoidance** | Wireless (Wi-Fi / 802.11) | Tries to avoid collision before it happens |

> **CD = Detection** (유선) / **CA = Avoidance** (무선) — just remember this!

### Why CSMA/CD Is No Longer Necessary
- Modern **Layer 2 switches** support **full-duplex** communication
- Full-duplex means sending and receiving happen simultaneously → **no collisions**
- No collisions = no need for collision detection
- Legacy **hubs** used half-duplex → collisions happened → CSMA/CD was needed

### Other Access Control Methods (not contention-based)
- **Token passing** – Devices take turns using a token
- **Priority ordering** – Higher priority devices get access first

---

## 6. Data Link Layer Protocols

### LAN Protocols
- **Ethernet** – Most common wired LAN protocol
- **802.11 (Wi-Fi)** – Wireless LAN protocol

### WAN Protocols (Legacy — being replaced by Ethernet)
- **PPP** – Point-to-Point Protocol
- **HDLC** – High-Level Data Link Control
- **Frame Relay**
- **ATM** – Asynchronous Transfer Mode
- **X.25**

> All of these are **Layer 2 protocols**. IP and UDP are **Layer 3 and Layer 4** respectively.

---

## 7. Practice Questions Review (Q1–Q14)

| Q | Question Summary | Answer | Key Concept |
|---|-----------------|--------|-------------|
| Q1 | Identifier used at Layer 2 to identify an Ethernet device | MAC address | MAC = Layer 2 identifier |
| Q2 | NIC attribute that places it at Layer 2 | MAC address | MAC address lives at Layer 2 |
| Q3 | Two orgs that define Layer 2 standards (choose 2) | IEEE, ITU | Standards bodies for Layer 2 |
| Q4 | Three data link layer protocols (choose 3) | 802.11, PPP, Ethernet | IP=L3, UDP=L4 |
| Q5 | Method for contention-based access on wireless | CSMA/CA | Wireless = CA (Avoidance) |
| Q6 | Topology where every node connects to every other node | Mesh | Mesh = highest redundancy |
| Q7 | Statement describing half-duplex | One direction at a time | Not one direction only (that's simplex) |
| Q8 | Function of LLC sublayer | Identify which Layer 3 protocol is used | LLC = bridge to Layer 3 |
| Q9 | Access control method used with legacy Ethernet hubs | CSMA/CD | Hubs = half-duplex = collisions |
| Q10 | Two sublayers of Layer 2 (choose 2) | MAC, LLC | The two sublayers of Layer 2 |
| Q11 | Layer responsible for specifying encapsulation method | Data Link (Layer 2) | Encapsulation = Layer 2's job |
| Q12 | Topology created by connecting all cables to a central device | Star | Central device = Star topology |
| Q13 | Two services performed by Layer 2 (choose 2) | Media access control + error detection / Encapsulates L3 packets into frames | Core Layer 2 functions |
| Q14 | Why CSMA/CD is no longer necessary | Full-duplex capable Layer 2 switches | No collisions = no need for CD |

---

## 8. What Layer 2 Does vs What It Doesn't Do

### Layer 2 DOES:
- Encapsulate Layer 3 packets into frames (add header + trailer)
- Provide MAC addressing for local delivery
- Perform error detection (FCS in trailer)
- Control media access (CSMA/CD, CSMA/CA)
- Identify Layer 3 protocol via LLC

### Layer 2 DOES NOT:
- Fragment packets into MTU size → **Layer 3**
- Determine the path to forward packets → **Layer 3 (Router)**
- Handle sequence numbers or flags → **Layer 4 (TCP)**
- Build MAC address tables → **Switch function**, not a Layer 2 service itself

---

## Summary

> **Layer 2 = The packaging department.**
> It takes the packet from Layer 3, wraps it in a frame with source/destination MAC addresses, and makes sure it gets delivered correctly to the next device on the local network. If anything gets damaged in transit, the FCS in the trailer catches it.

---

*Study session: Module 6 — Data Link Layer*
*Notes compiled with AI assistance (Claude) for faster review and comprehension*
