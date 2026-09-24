# 32. Ethernet Frames & Wireshark Lab

## Overview
Today's study covered Ethernet frame structure, Data Link sublayers (LLC & MAC), and hands-on packet capture analysis using Wireshark.

---

## 1. Ethernet II Frame Structure

An Ethernet frame is a data packet wrapped at Layer 2 (Data Link Layer). Each field has a specific role:

| Field | Size | Description |
|-------|------|-------------|
| **Preamble** | 8 Bytes | Alerts the receiver that a new frame is coming. Acts like a "heads up!" signal. Processed by NIC hardware — not visible in Wireshark. |
| **Destination Address** | 6 Bytes | MAC address of the receiving device. Can be unicast or broadcast (`ff:ff:ff:ff:ff:ff`). |
| **Source Address** | 6 Bytes | MAC address of the sending device. Always unicast. |
| **Frame Type** | 2 Bytes | Identifies the upper-layer protocol (e.g., `0x0800` = IPv4, `0x0806` = ARP). |
| **Data** | 46–1500 Bytes | The actual payload being transmitted. |
| **FCS** | 4 Bytes | Frame Check Sequence — used for error detection. |

### Key Points
- The **Preamble** is like a drumroll 🥁 — it synchronizes the receiver before data arrives.
- The **first 6 hex digits** of a MAC address = **OUI (Organizationally Unique Identifier)** → identifies the manufacturer.
- The **last 6 hex digits** = NIC serial number (unique to each device).

---

## 2. Data Link Sublayers: LLC vs MAC

The Data Link Layer (Layer 2) is divided into two sublayers:

```
[ Upper Layers: OS, Applications ]
            ↕
         [ LLC ]   ← Software side
         [ MAC ]   ← Hardware side
            ↕
[ Physical Layer: Cables, Wi-Fi ]
```

### LLC (Logical Link Control)
- **Upper sublayer** of the Data Link Layer
- Communicates with upper layers (OS, applications) via **software drivers**
- Allows multiple Layer 3 protocols to share the same network interface
- Acts as the bridge between software and hardware

### MAC (Media Access Control)
- **Lower sublayer** of the Data Link Layer
- Controls **physical access to the media**
- Checks for **errors in received bits** (via FCS)
- Uses **CSMA/CD** (wired Ethernet) or **CSMA/CA** (Wi-Fi) to manage collisions

| Feature | LLC | MAC |
|---------|-----|-----|
| Layer position | Upper sublayer | Lower sublayer |
| Handles | Software / Drivers | Hardware / Physical |
| Talks to | OS and upper-layer protocols | Network card and physical media |
| Key functions | Protocol multiplexing, software control | Media access, error checking, CSMA |

> 💡 **Memory trick:** **L**LC = **L**ogical = **S**oftware | **M**AC = **M**achine = **H**ardware

---

## 3. ARP (Address Resolution Protocol)

ARP is used to discover the MAC address associated with a known IP address.

### ARP Process
```
PC wants to ping 192.168.4.1 but doesn't know its MAC address

1. PC sends ARP Request (Broadcast: ff:ff:ff:ff:ff:ff)
   → "Who has 192.168.4.1? Tell 192.168.4.34"

2. Gateway replies with ARP Reply (Unicast)
   → "192.168.4.1 is at 64:da:ed:e5:a0:ed"

3. PC now knows the MAC → sends the ping
```

### Why Broadcast?
- PC knows the destination IP but **not the MAC address**
- Sends to `ff:ff:ff:ff:ff:ff` so **all devices on the network** receive it
- Only the device with the matching IP responds

---

## 4. Wireshark Lab — Capturing Ethernet Frames

### Lab Setup
- **PC IP:** `192.168.4.34`
- **Default Gateway IP:** `192.168.4.1`
- **PC MAC:** `40:ec:99:13:70:f9` (Intel NIC)
- **Gateway MAC:** `64:da:ed:e5:a0:ed` (eero router)

### Part 1 — Ping the Default Gateway

**Command used:**
```
ping 192.168.4.1
```

**Wireshark filter applied:**
```
icmp
```

**Captured Ethernet II frame (ping request):**

| Field | Value |
|-------|-------|
| Destination MAC | `64:da:ed:e5:a0:ed` (eero — gateway) |
| Source MAC | `40:ec:99:13:70:f9` (Intel — my PC) |
| Frame Type | `0x0800` (IPv4) |
| Source IP | `192.168.4.34` |
| Destination IP | `192.168.4.1` |

**Result:** 4 packets sent, 4 received — 0% loss ✅

---

### Part 2 — Ping a Remote Host (www.cisco.com)

**Command used:**
```
ping www.cisco.com
```

**Resolved to:** `23.214.109.210` (Akamai CDN)

**Captured Ethernet II frame (ping request):**

| Field | Value |
|-------|-------|
| Destination MAC | `64:da:ed:e5:a0:ed` (eero — gateway) ← **Same!** |
| Source MAC | `40:ec:99:13:70:f9` (Intel — my PC) |
| Frame Type | `0x0800` (IPv4) |
| Source IP | `192.168.4.34` |
| Destination IP | `23.214.109.210` ← **Changed!** |

**Result:** 4 packets sent, 4 received — 0% loss ✅

---

## 5. Key Observation — Local vs Remote Traffic

### Why does the destination IP change but the destination MAC stays the same?

```
My PC ──→ [eero Router] ──→ Internet ──→ cisco.com
           (Gateway)
```

- **MAC addresses** are only valid **within the local network**
- When sending data outside the local network, the frame must first go to the **default gateway (router)**
- Therefore, the **destination MAC is always the gateway's MAC**, regardless of the final destination
- The **destination IP changes** to reflect the actual remote host

### Analogy 📬
> Sending a letter overseas:
> - **MAC address** = address of your local post office (gateway)
> - **IP address** = the final recipient's address (written inside the envelope)

---

## 6. Frame Type Values Reference

| Hex Value | Protocol |
|-----------|----------|
| `0x0800` | IPv4 |
| `0x0806` | ARP |
| `0x86DD` | IPv6 |

---

## 7. Reflection — Why Wireshark Doesn't Show the Preamble

The **Preamble** field is handled entirely by the **NIC hardware** before the data is passed up to the OS. Since Wireshark captures traffic at the software level, the preamble has already been stripped and discarded by the time Wireshark sees the frame.

---

## Summary

| Concept | Key Takeaway |
|---------|-------------|
| Preamble | "Get ready!" signal — handled by hardware, invisible in Wireshark |
| LLC | Software sublayer — bridges OS and hardware via drivers |
| MAC | Hardware sublayer — controls media access, error checking, CSMA |
| ARP | Resolves IP → MAC using broadcast on local network |
| Destination MAC (remote) | Always the gateway's MAC — not the final destination |
| Frame Type `0x0800` | IPv4 protocol |
| Frame Type `0x0806` | ARP protocol |
