# Network Layer (OSI Layer 3) — Study Notes

## 1. Overview

The network layer is the vital **conduit** that allows devices on different networks to exchange data. While simple local networks can communicate directly, reaching a device in another city or country requires moving beyond the local network using **routers**, which is enabled by network layer protocols (IPv4/IPv6).

**Topics covered:**
- Network layer characteristics and IP protocols
- IPv4 and IPv6 packet structure
- Host routing and routing tables
- Router routing table fields

---

## 2. Core Network Layer Operations

The network layer performs **four fundamental operations** to move data end-to-end:

| Operation | Description |
|---|---|
| **Addressing** | Every device is assigned a unique IP address to identify it on the network. |
| **Encapsulation** | Data received from the transport layer (a *segment*) is wrapped with an **IP header** (source/destination IP) to form a *packet*. |
| **Routing** | The network layer determines the best path to the destination. Each router crossed is called a **hop**. |
| **De-encapsulation** | At the destination, the device checks the IP address; if it matches, the IP header is stripped and the data is passed up to the transport layer. |

> The network layer doesn't care about *what* the data is — it only ensures packets are addressed and routed correctly (like a shipping label, not the package contents).

---

## 3. IP Encapsulation

- **Layer independence**: Because data is encapsulated layer-by-layer, new protocols (e.g., IPv4 → IPv6) can be adopted without redesigning other layers.
- **Consistent addressing**: Source/destination IP addresses stay the same throughout the journey, *except* when NAT (Network Address Translation) is involved.
- **Data integrity**: Routers only inspect the IP header for routing decisions — the encapsulated transport-layer payload remains untouched in transit.

---

## 4. Three Characteristics of IP

### a) Connectionless
No handshake or pre-established connection before sending data — like dropping a letter in a mailbox without confirming the recipient is ready. Transmission starts immediately.

### b) Best Effort (Unreliable)
IP does **not** guarantee delivery, check for errors, or confirm receipt. It avoids overhead to stay fast — reliability (retransmission, ordering) is delegated to higher layers like **TCP**.

### c) Media Independent
IP operates the same way regardless of the physical medium (copper, fiber, wireless). The **data link layer** handles the specifics of preparing data for the actual transmission medium.

- **MTU (Maximum Transmission Unit)**: the largest packet size a given medium can carry.
- **Fragmentation**: when a packet is too large for the next link's MTU, a router splits it into smaller pieces. Fragments are reassembled at the destination.
  - ⚠️ **Note**: Routers do **not** fragment packets in **IPv6** (unlike IPv4).

---

## 5. IPv4 Packet Header — Key Fields

The IPv4 header acts like a **shipping label**, written in binary, read by network devices to route the packet correctly.

| Field | Purpose |
|---|---|
| **Version** | Identifies the protocol as IPv4. |
| **Source / Destination IP Address** | The most critical fields — identify where the packet comes from and where it's going. Stay constant during transit (barring NAT). |
| **Time-to-Live (TTL)** | Limits packet lifespan. Decremented by 1 at each hop/router; packet is discarded when it hits 0 — prevents infinite loops. |
| **Protocol** | Tells the receiving device what upper-layer protocol to use (e.g., `6` = TCP, `1` = ICMP, `17` = UDP). |
| **Identification, Flags, Fragment Offset** | Used together to fragment large packets and reassemble them correctly at the destination. |
| **Header Checksum** | Verifies the header wasn't corrupted in transit; packet is dropped if the check fails. |
| **Total Length** | Indicates the full size of the packet. |
| **Differentiated Services (DS/DiffServ)** | Used for packet prioritization (e.g., for VoIP traffic). |
| **Header Length** | Minimum size of the IPv4 header. |

---

## 6. Wireshark Packet Capture Examples (from video)

Three example packets captured between `192.168.1.109` (source) and `192.168.1.1` (destination):

1. **TCP packet** (general) — small size (52 bytes), `DF` (Don't Fragment) flag set, TTL = 128, Protocol = 6 (TCP).
2. **HTTP GET request** — much larger (411 bytes) since it carries an actual web request; still IPv4, TCP underneath, HTTP on top.
3. **ICMP packet (ping/echo request)** — same source/destination, but Protocol field = 1 (ICMP) instead of 6.

**Takeaway**: The network layer doesn't care whether the payload is HTTP, TCP control data, or an ICMP ping — it only uses the IP header (source/destination address, protocol number, TTL, checksum) to deliver the packet.

---

## 7. Q&A Summary (Quick Reference)

| Question | Answer |
|---|---|
| Which OSI layer sends segments to be encapsulated into IPv4/IPv6 packets? | **Transport layer** |
| Which layer prepares an IP packet for transmission over the medium? | **Data link layer** |
| Splitting a packet for a smaller-MTU medium is called? | **Fragmentation** |
| Delivery method with no guarantee of error-free delivery? | **Best effort** |
| Two key fields showing where a packet is from/going? | **Source IP address & Destination IP address** |
| True statement about IPv4 header fields? | Source/destination IPv4 addresses remain the same start to finish |
| Field that detects corruption in the IPv4 header? | **Header Checksum** |
| Field containing values like ICMP(1), TCP(6), UDP(17)? | **Protocol** |

---

## 8. Quick Concept Map

```
Transport Layer (Segment)
        ↓ encapsulation (+ IP header)
Network Layer (Packet) — Addressing, Routing, TTL, Fragmentation
        ↓ encapsulation (+ frame header/trailer)
Data Link Layer (Frame) — medium-specific framing
        ↓
Physical Medium (copper / fiber / wireless)
```

**Key properties of IP**: Connectionless · Best Effort · Media Independent
