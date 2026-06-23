# Networking Fundamentals – Study Notes

## 1. MAC Addresses (Media Access Control)

### What It Is
A MAC address is a **unique hardware identifier** assigned to every Network Interface Card (NIC). Think of it like a person's name in a room — when multiple devices share the same network, the sender must specify the destination's MAC address so only the right device processes the message.

### Key Properties
- **48 bits long**, represented in hexadecimal
- **Permanent** — burned into the hardware, never changes regardless of location
- Also called a **physical address**

### Structure
| Part | Bits | Description |
|------|------|-------------|
| OUI (Organizationally Unique Identifier) | First 24 bits | Identifies the manufacturer (e.g., Cisco: `00-60-2F`) |
| Vendor-Assigned | Last 24 bits | Unique serial assigned by the manufacturer |

### Common Notation Formats
| Format | Example |
|--------|---------|
| Hyphen | `00-50-56-BE-D7-87` |
| Colon | `00:50:56:BE:D7:87` |
| Dot | `0050.56BE.D787` |

### Role in a LAN
- Used for **NIC-to-NIC communication within the same network**
- When a device sends data, it **must include the destination MAC address**
- Routers have one NIC (and MAC address) per connected network — a router bridging two LANs has two different MAC addresses, one for each side

---

## 2. IP Addresses

### What It Is
An IP address is a **logical address** that identifies a device's location within a network. Unlike MAC addresses, IP addresses **change when a device moves to a different network**.

> **Analogy:** MAC address = fingerprint (permanent identity); IP address = mailing address (location-based, changes when you move)

### Cross-Network Communication
- Devices on the **same network** communicate directly using MAC addresses
- Devices on **different networks** require a **router** to forward the message — the router acts as an intermediary (like a messenger between rooms)

---

## 3. IPv4

### Structure
- **32 bits** total, written in **dotted decimal notation**
- Format: four decimal numbers (0–255) separated by dots
- Example: `192.168.1.100`

### Subnet Mask
Divides an IP address into two parts:

| Part | Description |
|------|-------------|
| **Network portion** | Identifies which network the device belongs to (like a neighborhood) |
| **Host portion** | Identifies the specific device within that network (like a house number) |

- Written in the same dotted decimal format: `255.255.255.0`
- Bits set to **1** = network portion; bits set to **0** = host portion
- Can also be written in **slash/prefix notation**: `255.255.255.0` = `/24`

### Example
```
IP Address:   192.168.1.100
Subnet Mask:  255.255.255.0  (/24)

Network:  192.168.1.0   ← shared by all devices on this LAN
Host:     .100          ← unique to this device
```

If this device moves to `172.16.0.0/16`, its address becomes `172.16.3.10` — the network portion changes to match the new network.

---

## 4. IPv6

### Why It Exists
IPv4 only supports ~4.3 billion addresses, which are now exhausted. IPv6 expands this massively.

### Structure
- **128 bits** total → 8 segments × 16 bits each
- Each segment written in **hexadecimal**, separated by colons
- Example: `2001:0db8:acad:0100:0000:0000:0000:0077`

### Address Compression Rules
IPv6 addresses can be shortened using two rules:

**Rule 1 – Drop leading zeros** within any segment:
```
0db8 → db8
0100 → 100
0000 → 0
```

**Rule 2 – Replace one consecutive run of all-zero segments with `::`**
```
:0000:0000:0000: → ::
```
⚠️ The `::` shorthand can only be used **once** per address.

**Combined example:**
```
Full:       2001:0db8:acad:0100:0000:0000:0000:0077
Compressed: 2001:db8:acad:100::77
```

### Prefix / Network Notation
Same slash notation as IPv4:
```
2001:db8:acad:100::77/64
```
- `/64` means the first 64 bits = **network portion**
- Remaining 64 bits = **host portion**

---

## 5. IPv4 Packet Header vs. IPv6 Packet Header

| Feature | IPv4 Header | IPv6 Header |
|---------|-------------|-------------|
| Complexity | Complex, variable-length | Simplified, fixed-length |
| Fragmentation | Handled in header (supports splitting packets) | Removed from header |
| Processing speed | Slower on modern hardware | Faster — simpler structure |
| Address length | 32 bits | 128 bits |
| Design goal | Original internet standard | Efficiency + scalability |

**Key takeaway:** Although IPv6 addresses are much longer, the packet header itself is *leaner and faster to process* than IPv4's — unnecessary fields were stripped out.

---

## 6. MAC vs. IP — Summary Comparison

| Property | MAC Address | IP Address |
|----------|-------------|------------|
| Length | 48 bits | 32 bits (v4) / 128 bits (v6) |
| Format | Hexadecimal | Decimal (v4) / Hex (v6) |
| Assigned by | Manufacturer (hardware) | Network administrator |
| Changes? | Never | Yes, when network changes |
| Scope | Local network (LAN) | Local and cross-network |
| Analogy | Fingerprint | Mailing address |

---

## 7. Number Systems Quick Reference

| System | Base | Digits Used |
|--------|------|-------------|
| Binary | 2 | 0, 1 |
| Decimal | 10 | 0–9 |
| Hexadecimal | 16 | 0–9, A–F (A=10, F=15) |

> IPv4 uses **decimal**; MAC addresses and IPv6 use **hexadecimal**; underlying networking operates in **binary**
