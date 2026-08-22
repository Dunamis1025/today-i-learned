# Networking Fundamentals — Study Notes

## 1. OSI Model — Transport Layer

**Key Function:** Segmentation & Reassembly

- The **Transport Layer (Layer 4)** is responsible for breaking large data into smaller pieces (**segmentation**) and reassembling them in the correct order at the destination (**reassembly**).
- Think of it like tearing pages out of a book, mailing them in separate envelopes, and the receiver putting them back in order.

---

## 2. Standardization Organizations

**Three key bodies that create networking standards:**

| Abbreviation | Full Name | Role |
|---|---|---|
| **IANA** | Internet Assigned Numbers Authority | Manages IP addresses and internet resources |
| **IETF** | Internet Engineering Task Force | Develops internet technical standards |
| **IEEE** | Institute of Electrical and Electronics Engineers | Standardizes electrical/electronics tech (e.g., Wi-Fi) |

> ❌ Not organizations: MAC (hardware address), OSI (communication model), TCP/IP (protocol suite)

---

## 3. Types of Communication

| Type | Description | Example |
|---|---|---|
| **Unicast** | 1-to-1 — one sender to one specific receiver | Phone call |
| **Multicast** | 1-to-Group — one sender to a subscribed group | Group chat, live stream |
| **Broadcast** | 1-to-All — one sender to every device on the network | Network-wide announcement |

---

## 4. Message Encoding & Decoding

- **Encoding:** Converting a message into a transmittable signal (e.g., electrical pulses, light) — done by the **sender**.
- **Decoding:** Receiving a signal and converting it back into a readable message — done by the **receiver**.

> Analogy: Encoding = writing in Morse code. Decoding = translating it back to English.

---

## 5. Encapsulation

**Definition:** The process of wrapping data with protocol information at each layer as it travels down the network stack — like putting a letter inside an envelope, then inside a shipping box.

- Each layer **adds its own header** before passing data to the layer below.
- The reverse process (removing headers upon receipt) is called **decapsulation**.

**Other terms clarified:**
- **Flow control** — regulates the speed of data transfer so the receiver isn't overwhelmed.
- **Access control** — manages who is permitted to access a network or resource.

---

## 6. IP Packet Before Physical Transmission

**Before an IP packet travels over a physical medium (cable/wireless), it is:**

> ✅ **Encapsulated in a Layer 2 (Data Link) frame**

- Layer 3 (IP packet) handles logical addressing.
- Layer 2 (frame) handles physical delivery between adjacent network devices.
- The frame acts as the "final envelope" needed to move data across the physical wire.

**Why the others are wrong:**
- Segmentation → happens at Layer 4 (Transport), not here
- Reliable delivery guarantee → handled by TCP, not IP
- Encapsulated in TCP segment → backwards; TCP segment goes *inside* the IP packet, not the other way

---

## 7. Protocol

**Definition:** A set of rules that defines how communication between devices should occur.

> Protocol = the agreed-upon "language" and "manners" that all devices follow so they can understand each other.

- Protocols do **not** define message content, bandwidth, or operating systems — only the **rules for communication**.

---

## 8. Protocol Stack — Data Encapsulation Order (Client Side)

**When a web client requests a webpage, data is encapsulated in this order (top → bottom):**

```
HTTP  →  TCP  →  IP  →  Ethernet
```

| Layer | Protocol | Role |
|---|---|---|
| Application | **HTTP** | Creates the actual web request (the content) |
| Transport | **TCP** | Breaks data into segments; ensures reliable delivery |
| Network | **IP** | Adds source & destination IP addresses |
| Data Link | **Ethernet** | Packages data for physical network transmission |

> Each layer **wraps** the layer above it — like nesting envelopes before sending.

---

## Quick Reference Summary

| Concept | One-Line Answer |
|---|---|
| Transport Layer | Segments and reassembles data |
| IANA / IETF / IEEE | The three major standardization bodies |
| Broadcast | Sends to all devices on the network |
| Encoding | Converts message → transmittable signal |
| Decoding | Converts received signal → readable message |
| Encapsulation | Wrapping data in protocol headers layer by layer |
| Layer 2 Frame | Required wrapper before physical transmission |
| Protocol | Rules governing how communication works |
| HTTP→TCP→IP→Ethernet | Correct encapsulation order from client side |
