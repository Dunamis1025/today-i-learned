# 33. MAC Address and Ethernet Fundamentals

> **Source**: Cisco CCNA Curriculum — Chapter 7.2 (MAC Address, Hexadecimal, Frame Processing, Unicast)  
> **Topics**: Hexadecimal, MAC Address Structure, BIA, Frame Processing, Unicast Communication

---

## Table of Contents

1. [Hexadecimal Number System](#1-hexadecimal-number-system)
2. [Decimal, Binary, and Hexadecimal Equivalents](#2-decimal-binary-and-hexadecimal-equivalents)
3. [Ethernet MAC Address Structure](#3-ethernet-mac-address-structure)
4. [Frame Processing](#4-frame-processing)
5. [Unicast MAC Address](#5-unicast-mac-address)
6. [Summary Table](#6-summary-table)

---

## 1. Hexadecimal Number System

### Why Hexadecimal?

| Address Type | Number System Used |
|---|---|
| IPv4 (e.g., 192.168.1.1) | Decimal (base 10) |
| IPv6 | Hexadecimal (base 16) |
| Ethernet MAC Address | Hexadecimal (base 16) |

Hexadecimal is used for MAC and IPv6 addresses because **1 hex digit = 4 binary bits**, making it far more compact than binary.

### How It Works

- Uses digits `0–9` and letters `A–F` (16 total symbols)
- A 48-bit MAC address → only **12 hexadecimal digits** needed

```
Binary (48 bits):  1100 1010 0001 1111 ... (long and hard to read)
Hexadecimal:       CA-1F-... (compact and readable)
```

### Conversion Reference (0–F)

| Decimal | Binary | Hexadecimal |
|:---:|:---:|:---:|
| 0  | 0000 | 0 |
| 1  | 0001 | 1 |
| 2  | 0010 | 2 |
| 3  | 0011 | 3 |
| 4  | 0100 | 4 |
| 5  | 0101 | 5 |
| 6  | 0110 | 6 |
| 7  | 0111 | 7 |
| 8  | 1000 | 8 |
| 9  | 1001 | 9 |
| 10 | 1010 | A |
| 11 | 1011 | B |
| 12 | 1100 | C |
| 13 | 1101 | D |
| 14 | 1110 | E |
| 15 | 1111 | F |

---

## 2. Decimal, Binary, and Hexadecimal Equivalents

### 1-Byte (8-bit) Range

One byte = 8 bits = **2 hex digits**.  
Range: `00` to `FF` (decimal 0 to 255).

| Decimal | Binary    | Hexadecimal | Notes |
|:---:|:---:|:---:|:---|
| 0   | 0000 0000 | 00 | Minimum value |
| 10  | 0000 1010 | 0A | Leading zero required |
| 15  | 0000 1111 | 0F | |
| 16  | 0001 0000 | 10 | |
| 128 | 1000 0000 | 80 | |
| 192 | 1100 0000 | C0 | Common subnet boundary |
| 255 | 1111 1111 | FF | Maximum value |

### Key Rules

#### Rule 1: Always Use Leading Zeros
Hexadecimal always displays leading zeros to complete the 8-bit representation.

```
Decimal 10 → Binary: 0000 1010 → Hexadecimal: 0A  ✅ (NOT just "A")
```

#### Rule 2: Three Ways to Write Hex

| Notation | Example | Common Usage |
|:---:|:---:|:---|
| `0x` prefix | `0x73` | Programming / code |
| Subscript 16 | `73₁₆` | Academic / mathematics |
| `H` suffix | `73H` | Legacy hardware docs |

#### Rule 3: Convert via Binary
When converting between decimal and hexadecimal, **use binary as an intermediate step**:

```
Decimal → Binary → Hexadecimal
Hexadecimal → Binary → Decimal
```

---

## 3. Ethernet MAC Address Structure

### Overview

- A MAC address is a **48-bit** hardware identifier assigned to every NIC (Network Interface Card)
- Expressed as **12 hexadecimal digits** (= 6 bytes)
- Operates at **Layer 2 (Data Link Layer)** of the OSI model
- Used to identify the **physical source and destination** within a local network segment

```
Bit layout:
[ 4-bit ][ 4-bit ] [ 4-bit ][ 4-bit ] ... × 12 = 48 bits
[  Hex  ][  Hex  ] [  Hex  ][  Hex  ] ... × 12 = 12 hex digits
[      Byte      ] [      Byte      ] ... × 6  = 6 bytes
```

### MAC Address = OUI + Vendor Assigned

```
00 - 60 - 2F  -  3A - 07 - BC
└────────────┘    └────────────┘
 OUI (3 bytes)    Vendor Code (3 bytes)
 = 6 hex digits   = 6 hex digits
```

| Section | Size | Assigned By | Purpose |
|---|---|---|---|
| **OUI** (Organizationally Unique Identifier) | 24 bits / 3 bytes / 6 hex | IEEE | Identifies the manufacturer |
| **Vendor Assigned** | 24 bits / 3 bytes / 6 hex | Manufacturer | Uniquely identifies each device |

### Example: Cisco MAC Address

```
IEEE assigns OUI to Cisco:    00-60-2F
Cisco assigns device code:    3A-07-BC
                                  ↓
Final MAC address:            00-60-2F-3A-07-BC
```

### MAC Address Uniqueness

- All MAC addresses **must be globally unique**
- Vendors register with IEEE to receive a unique OUI
- Duplicates can occur due to:
  - Manufacturing errors
  - Virtual machine (VM) implementations
  - Software-based MAC spoofing
- Resolution: replace the NIC or modify via software

---

## 4. Frame Processing

### BIA (Burned-In Address)

The MAC address is also called a **BIA (Burned-In Address)** because it is permanently hard-coded into the **ROM chip** of the NIC at manufacturing time.

```
Power ON sequence:
ROM (permanent) → copied to → RAM (active use)
[MAC Address]                 [MAC Address]
```

> **Note**: Modern operating systems allow MAC address modification via software. This makes MAC-based filtering less reliable as a sole security mechanism.

### Ethernet Frame Header Contents

When sending data over an Ethernet network, each frame includes:

| Field | Description |
|---|---|
| **Source MAC Address** | MAC address of the sending device's NIC |
| **Destination MAC Address** | MAC address of the target device's NIC |

### Frame Reception Logic

When a NIC receives an Ethernet frame:

```
Frame arrives at NIC
        ↓
Check: Destination MAC == My MAC?
        ↓                    ↓
      YES                   NO
        ↓                    ↓
Pass up OSI layers       Discard frame
(de-encapsulation)       (not for me)
```

#### Exceptions — NIC also accepts:

| Type | Description |
|---|---|
| **Broadcast** | Sent to all devices on the network (e.g., `FF-FF-FF-FF-FF-FF`) |
| **Multicast** | Sent to a specific group the host belongs to |

### Devices with MAC Addresses

Any device that sends or receives Ethernet frames has a NIC and therefore a MAC address:
- Workstations
- Servers
- Printers
- Mobile devices
- Routers (each interface has its own MAC)

---

## 5. Unicast MAC Address

### Three Layer 2 Communication Types

| Type | Sender | Receiver | Example |
|---|---|---|---|
| **Unicast** | 1 device | 1 specific device | Direct message |
| **Broadcast** | 1 device | All devices | Network-wide announcement |
| **Multicast** | 1 device | A group of devices | Streaming to subscribers |

### Unicast Communication

A **unicast MAC address** is the unique address used when a frame is sent from **one device to one specific destination device**.

#### Ethernet Frame Structure (Unicast Example)

```
Source Host H1:
  IP:  192.168.1.5
  MAC: 00-07-E9-63-CE-53

Destination Server:
  IP:  192.168.1.200
  MAC: 00-07-E9-42-AC-28
```

```
┌─────────────────┬─────────────────┬─────────────┬──────────────┬───────────┬─────────┐
│  Dest MAC       │  Source MAC     │  Source IP  │  Dest IP     │ User Data │ Trailer │
│ 00-07-E9-42-    │ 00-07-E9-63-    │ 192.168.1.5 │192.168.1.200 │           │         │
│    AC-28        │    CE-53        │             │              │           │         │
└─────────────────┴─────────────────┴─────────────┴──────────────┴───────────┴─────────┘
 ←── Layer 2 ───→                   ←────────── Layer 3 (IP Packet) ──────────→
 ←─────────────────────── Ethernet Frame ───────────────────────────────────────────────→
```

### IP-to-MAC Resolution

Before sending, the source must know the **destination MAC address**. If only the IP address is known:

| Protocol | IP Version | Function |
|---|---|---|
| **ARP** (Address Resolution Protocol) | IPv4 | Resolves IPv4 address → MAC address |
| **ND** (Neighbor Discovery) | IPv6 | Resolves IPv6 address → MAC address |

```
Source knows: Destination IP = 192.168.1.200
ARP process:  "Who has 192.168.1.200? Tell me your MAC."
ARP reply:    "I am 00-07-E9-42-AC-28"
Now send:     Frame with Dest MAC = 00-07-E9-42-AC-28
```

> **Important**: The **source MAC address must always be a unicast address**.

---

## 6. Summary Table

| Concept | Key Detail |
|---|---|
| Hexadecimal base | Base-16 (0–9, A–F) |
| 1 hex digit represents | 4 binary bits |
| 1 byte in hex | 2 hex digits (00–FF) |
| MAC address size | 48 bits = 12 hex digits = 6 bytes |
| OUI | First 6 hex digits — assigned by IEEE to vendor |
| Vendor code | Last 6 hex digits — assigned by vendor to device |
| BIA | MAC permanently stored in ROM, copied to RAM on boot |
| Frame check (unicast) | NIC discards frame if dest MAC ≠ own MAC |
| Broadcast exception | NIC accepts `FF-FF-FF-FF-FF-FF` frames |
| IPv4 MAC discovery | ARP (Address Resolution Protocol) |
| IPv6 MAC discovery | ND (Neighbor Discovery) |
| Hex notation styles | `0x73` / `73₁₆` / `73H` |

---

*Documented as part of CCNA self-study — today-i-learned series*
