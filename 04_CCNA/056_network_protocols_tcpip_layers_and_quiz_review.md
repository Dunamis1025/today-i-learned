# Network Protocols — Study Notes

> Topics covered: Routing, Service Discovery, TCP/IP Model Layers, Sequencing, Error Reporting, Encapsulation

---

## 1. Routing Protocols — BGP & OSPF

**BGP and OSPF are Routing Protocols.**

Routing protocols determine the **best path for data to travel** across a network.

| Protocol | Full Name | Role |
|----------|-----------|------|
| OSPF | Open Shortest Path First | Finds shortest path **within** a private/internal network (Interior Gateway Protocol) |
| BGP | Border Gateway Protocol | Manages routing **between** different networks/ISPs across the internet (Exterior Gateway Protocol) |

> **Analogy:** Routers are like GPS navigation systems at every intersection. OSPF navigates internal roads; BGP connects highways between countries.

---

## 2. Service Discovery Protocols — DNS & DHCP

**Service discovery** = identifying what services/devices are available on a network and where they are.

| Protocol | Full Name | Function |
|----------|-----------|----------|
| DNS | Domain Name System | Translates human-readable domain names (e.g., `google.com`) into IP addresses — acts as a **digital phonebook** |
| DHCP | Dynamic Host Configuration Protocol | Automatically assigns IP addresses to devices when they join a network — acts as a **registration desk** |

**Not service discovery:**
- **TCP** — a transport/delivery method
- **SSH** — a secure remote access tool

---

## 3. Sequencing in Network Communication

**Purpose:** To uniquely label transmitted segments of data so the receiver can correctly reassemble them.

- Large data is broken into smaller **packets** before transmission
- Each packet is assigned a **sequence number**
- Even if packets arrive **out of order**, the receiver uses sequence numbers to reconstruct the original data correctly

> **Analogy:** Shipping furniture in multiple boxes labeled "Box 1, Box 2, Box 3..." so the recipient can assemble them in the right order.

---

## 4. Reliable Delivery Protocol — TCP

**TCP (Transmission Control Protocol)** is responsible for guaranteeing reliable delivery of data.

| Protocol | Role | Reliable? |
|----------|------|-----------|
| **TCP** | Confirms receipt; retransmits lost data | ✅ Yes |
| IP | Addresses and routes packets | ❌ No |
| Ethernet | Physical transmission medium | ❌ No |
| HTTP | Web content format/structure | ❌ No |

> **Analogy:** TCP is like **certified/registered mail** — delivery is confirmed, and if it fails, it's resent automatically.

**Key TCP mechanism:** The **3-Way Handshake** establishes a reliable connection before data transfer begins.

---

## 5. The TCP/IP Model — 4 Layers

| Layer | Analogy | Key Protocols |
|-------|---------|---------------|
| **Application** | The letter's content | HTTP, DNS, DHCP, FTP |
| **Transport** | The delivery method | TCP, UDP |
| **Internet** | Address lookup & routing | IP, ICMP, OSPF, EIGRP, ARP |
| **Network Access** | The physical road | Ethernet, Wi-Fi |

### Layer Details

#### Application Layer
- Closest to end-users and their applications
- **DNS** — name-to-IP resolution
- **DHCP** — automatic IP assignment

#### Transport Layer
- Determines *how* data is delivered
- **TCP** — reliable, ordered, error-checked delivery
- **UDP** — fast, lightweight, no delivery guarantee (used in video streaming, gaming, VoIP)

#### Internet Layer
Provides three core services:
1. **Internet Protocol (IP)** — assigns source/destination addresses to packets
2. **Routing Protocols (OSPF, EIGRP, BGP)** — calculate the optimal path across networks
3. **Address Resolution (ARP/NDP)** — maps logical IP addresses to physical MAC addresses

#### Network Access Layer
- Handles physical transmission of data between directly connected nodes
- **Ethernet** — defines how data is transmitted via cables or Wi-Fi signals
- Closest layer to hardware

---

## 6. Error Reporting — ICMPv4 & ICMPv6

**ICMP (Internet Control Message Protocol)** provides feedback from the destination host back to the source host when packet delivery fails.

| Protocol | Used With |
|----------|-----------|
| ICMPv4 | IPv4 networks |
| ICMPv6 | IPv6 networks (also supports Neighbor Discovery) |

> **Analogy:** ICMP is like a **delivery failure notification** — "Package not delivered: address not found."

**Common ICMP-based tools:**
- `ping` — tests connectivity to a host
- `traceroute` — traces the path packets take across a network

**Not error-reporting protocols:**
- **UDP / TCP** — transport methods (TCP handles retransmission, but not network-wide error reporting)
- **IPv4 / IPv6** — addressing systems only

---

## 7. De-encapsulation (Peeling the Onion)

When a device receives data, it **strips headers layer by layer** from the bottom up:

```
Network Access Layer  →  Strip Ethernet header  (outermost shell)
         ↓
Internet Layer        →  Strip IP header
         ↓
Transport Layer       →  Strip TCP/UDP header
         ↓
Application Layer     →  Access actual data (e.g., HTTP content)
```

> **Example:** If a device receives a frame and removes the Ethernet info, the **next** information to process is the **IP packet** at the Internet Layer.

---

## Quick Reference — Protocol Layer Map

| Protocol | Layer |
|----------|-------|
| HTTP, FTP, SMTP | Application |
| DNS | Application |
| DHCP | Application |
| TCP | Transport |
| UDP | Transport |
| IP | Internet |
| ICMP (v4/v6) | Internet |
| OSPF, EIGRP, BGP | Internet |
| ARP | Internet |
| Ethernet | Network Access |
| Wi-Fi (802.11) | Network Access |

---

*Study notes compiled from Cisco Networking Academy quiz content.*
