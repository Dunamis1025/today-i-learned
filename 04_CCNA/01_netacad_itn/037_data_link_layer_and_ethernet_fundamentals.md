# Networking Study Notes — Data Link Layer & Ethernet Fundamentals

---

## 1. Ethernet vs. Token Ring

| Feature | Ethernet (IEEE 802.3) | Token Ring (IEEE 802.5) |
|---|---|---|
| Standard | 802.3 | 802.5 |
| Topology | Star, Bus | Ring |
| Typical Speeds | 10 / 100 / 1000 Mbps+ | 4 / 16 Mbps |
| Access Method | CSMA/CD | Token Passing |

### Key Points
- **IEEE 802.3** is the standard for Ethernet — the dominant wired LAN technology today.
- **IEEE 802.5** is the standard for Token Ring, developed primarily by IBM.
- Token Ring uses a **ring topology**: devices are connected in a closed loop, and only the device holding the "token" (a special control frame) is allowed to transmit data — eliminating collisions by design.
- Ethernet uses a **star topology** (modern, via switches) or bus topology (legacy), and manages collisions using **CSMA/CD (Carrier Sense Multiple Access with Collision Detection)**.
- The **16 Mbps** speed and **ring topology** are hallmarks of Token Ring, not Ethernet.

---

## 2. MAC Addresses

### Structure
A MAC address is a **48-bit (6-byte)** physical address burned into a Network Interface Card (NIC) by the manufacturer.

```
[  OUI (3 bytes)  ] [  Device ID (3 bytes)  ]
  01 - 00 - 5E         0A - 00 - 02
```

- **First 3 bytes** → OUI (Organizationally Unique Identifier): assigned by the **IEEE** to the manufacturer. Identifies the vendor.
- **Last 3 bytes** → Unique serial number assigned by the manufacturer per device.

### Key Properties
- MAC addresses must be **globally unique**.
- They are **Layer 2 (Data Link Layer)** addresses — not routed across networks.
- They are **physical/hardware** addresses, not logical ones (unlike IP addresses).
- The managing body is **IEEE**, not ISO.

### MAC Address Types

| Type | Purpose | Identifier |
|---|---|---|
| Unicast | Reaches one specific host | First byte is even (LSB = 0) |
| Multicast | Reaches a specific group of hosts | Starts with `01-00-5E` (for IPv4 multicast) |
| Broadcast | Reaches all hosts on the segment | `FF-FF-FF-FF-FF-FF` |

#### How to identify Multicast
- Check the **Least Significant Bit (LSB)** of the first byte.
- If it is `1`, the address is multicast.
- Example: `01-00-5E-0A-00-02` → first byte = `01` = `0000 0001` → LSB is `1` → **Multicast**

#### IPv4 Multicast → MAC Address Mapping
- The IEEE reserved the `01-00-5E` prefix for IPv4 multicast.
- The last 23 bits of the IPv4 multicast address are mapped into the last 23 bits of the MAC address.
- The most significant bit of the 4th byte is always set to `0`.

---

## 3. OSI Model & PDUs (Protocol Data Units)

A **PDU** is the unit of data at each layer of the OSI model. As data moves down the stack, each layer adds its own header (encapsulation), changing the PDU name.

| OSI Layer | PDU Name | Key Info |
|---|---|---|
| Layer 4 (Transport) | **Segment** | Used by TCP/UDP |
| Layer 3 (Network) | **Packet** | Contains IP addresses |
| Layer 2 (Data Link) | **Frame** | Contains MAC addresses |
| Layer 1 (Physical) | **Bit** | Electrical/optical signals |

### Analogy: Shipping System
| Step | Networking | Shipping |
|---|---|---|
| Transport (L4) | Add TCP/UDP info | Pack item in a box with a packing slip |
| Network (L3) | Add IP address | Write the final destination address |
| Data Link (L2) | Add MAC address | Label with the next stop address |
| Physical (L1) | Send as bits | Put on a truck and drive |

---

## 4. Data Link Layer — Sublayers: LLC vs. MAC

The Data Link Layer (Layer 2) is divided into two sublayers:

| Sublayer | Full Name | Responsibilities |
|---|---|---|
| **LLC** | Logical Link Control | Interfaces with Layer 3; identifies which network protocol (IPv4, IPv6, etc.) to pass data up to; manages flow control |
| **MAC** | Media Access Control | Controls access to the physical medium; performs framing (adds header + trailer); handles physical addressing |

### LLC Responsibilities
- **Communicates with upper protocol layers** (Layer 3 and above).
- Identifies the network layer protocol being used in the frame.

### MAC Responsibilities
- **Adds a header and trailer** to the packet to form a Layer 2 PDU (frame).
  - Header: contains source and destination MAC addresses.
  - Trailer: contains the **FCS (Frame Check Sequence)** for error detection.
- **Responsible for Media Access Control** — determines when and how a device accesses the physical medium.

---

## 5. Ethernet Frame

### Frame Size Constraints
| Size | Name | Description |
|---|---|---|
| < 64 bytes | **Runt frame** | Dropped immediately — likely caused by a collision or NIC error |
| 64 – 1518 bytes | **Valid frame** | Standard Ethernet frame size range |
| > 1518 bytes | **Giant frame** | Dropped — considered malformed (unless Jumbo Frames are enabled) |

> Note: With VLAN tagging (802.1Q), the maximum size can extend to **1522 bytes**.

---

## 6. How a Host Processes an Incoming Frame

When a host receives an Ethernet frame, the NIC checks the **destination MAC address**:

- **Match** → Accept the frame → Decapsulate → Pass data to Layer 3.
- **No match** → **Discard the frame** immediately. The host does not look at the IP address inside.

> This saves CPU resources and prevents unnecessary processing of traffic not intended for the host.

---

## 7. Network Devices & Their OSI Layers

| Device | OSI Layer | Forwarding Logic |
|---|---|---|
| **Hub / Repeater** | Layer 1 (Physical) | No address awareness — broadcasts all data to every port |
| **Switch** | Layer 2 (Data Link) | Forwards frames based on **destination MAC address** |
| **Router** | Layer 3 (Network) | Routes packets based on **IP address** |
| **Modem** | Physical/Data Link | Converts digital ↔ analog signals; not a forwarding device |

### How a Switch Builds Its MAC Address Table
1. A frame arrives on a switch port.
2. The switch reads the **source MAC address** of the incoming frame.
3. It records: `source MAC address → port number` in its **MAC Address Table** (also called the **CAM table**).
4. When the switch later needs to forward data to that device, it looks up the **destination MAC address** in the table and sends the frame to the correct port only.

> The switch builds its table using the **source** address of **incoming** frames — not the destination address.

---

## 8. Auto-MDIX

| Feature | Function |
|---|---|
| **Auto-MDIX** | Automatically detects the Ethernet cable type (straight-through vs. crossover) and adjusts the TX/RX pin configuration internally |
| **Auto-Negotiation** | Automatically determines the connection speed (e.g., 100/1000 Mbps) and duplex mode (Full/Half) |

### Background
- Traditionally, connecting **different device types** required a **straight-through cable**, while connecting **same device types** required a **crossover cable**.
- With **Auto-MDIX enabled**, the interface detects and adjusts automatically — either cable type works regardless of the devices connected.

---

## 9. Key Vocabulary

| Term | Definition |
|---|---|
| **PDU** | Protocol Data Unit — the form of data at a specific OSI layer |
| **Encapsulation** | The process of wrapping data with headers (and trailers) as it moves down the OSI stack |
| **CSMA/CD** | Carrier Sense Multiple Access with Collision Detection — Ethernet's access control method |
| **OUI** | Organizationally Unique Identifier — the first 3 bytes of a MAC address identifying the manufacturer |
| **CAM Table** | Content Addressable Memory table — a switch's MAC address table |
| **FCS** | Frame Check Sequence — error detection field in an Ethernet frame trailer |
| **Runt Frame** | An Ethernet frame smaller than 64 bytes — always dropped |
| **Hallmark** | A defining or characteristic feature of something (e.g., "16 Mbps is a hallmark of Token Ring") |
| **Constraint** | A rule or limitation that must be respected (e.g., Ethernet frame size constraints: 64–1518 bytes) |
| **Exclusively** | Solely; only; without exception (e.g., "The switch builds its table exclusively from source addresses of incoming frames") |
