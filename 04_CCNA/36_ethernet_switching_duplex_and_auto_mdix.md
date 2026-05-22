# 📡 Networking Module 7 — Study Notes

> **Topic:** Ethernet, Switching, MAC Addresses, Duplex & Speed, Auto-MDIX  
> **Source:** Cisco Networking Academy (CCNAv7)

---

## Table of Contents

1. [Ethernet Frame](#1-ethernet-frame)
2. [Ethernet MAC Address](#2-ethernet-mac-address)
3. [MAC Address Table](#3-mac-address-table)
4. [Switch Speeds & Forwarding Methods](#4-switch-speeds--forwarding-methods)
5. [Duplex & Speed Settings (7.4.4)](#5-duplex--speed-settings-744)
6. [Auto-MDIX (7.4.5)](#6-auto-mdix-745)
7. [Quiz Review](#7-quiz-review)

---

## 1. Ethernet Frame

Ethernet operates at both the **Data Link Layer (Layer 2)** and the **Physical Layer (Layer 1)**.

- Uses **LLC** and **MAC sublayers** of the Data Link Layer
- Data encapsulation includes:
  - Ethernet frame structure
  - Ethernet addressing
  - Ethernet error detection
- Ethernet LANs use switches operating in **full-duplex** mode

### Ethernet Frame Fields

| Field | Description |
|---|---|
| Preamble | Synchronization signal |
| Start Frame Delimiter (SFD) | Marks the start of the frame |
| Destination MAC Address | Where the frame is going |
| Source MAC Address | Where the frame came from |
| EtherType | Identifies the Layer 3 protocol |
| Data | The actual payload |
| FCS (Frame Check Sequence) | Error detection |

> 💡 **Analogy:** Think of a frame like a shipping box — it has a label (addresses), contents (data), and a damage check sticker (FCS).

---

## 2. Ethernet MAC Address

A **MAC (Media Access Control) address** is a unique hardware identifier assigned to every NIC (Network Interface Card).

### Key Facts

- **48-bit address** expressed as **12 hexadecimal digits** (6 bytes)
- Format: `XX:XX:XX:XX:XX:XX`
- First 6 hex digits → **OUI (Organizationally Unique Identifier)** — identifies the manufacturer
- Last 6 hex digits → **Vendor-assigned unique value**

### Number Systems

| System | Digits Used |
|---|---|
| Binary | 0, 1 |
| Decimal | 0–9 |
| Hexadecimal | 0–9, A–F |

### MAC Address Types (Layer 2)

| Type | Description |
|---|---|
| **Unicast** | One-to-one communication |
| **Broadcast** | One-to-all (`FF:FF:FF:FF:FF:FF`) |
| **Multicast** | One-to-many (specific group) |

> 💡 **Analogy:** A MAC address is like a **social security number** — globally unique, permanently assigned to your device.

---

## 3. MAC Address Table

A **Layer 2 Ethernet switch** makes forwarding decisions based **solely on MAC addresses**.

### How It Works

1. A frame arrives at a switch port
2. The switch reads the **source MAC address** and records it in the MAC address table (maps MAC → port)
3. The switch looks up the **destination MAC address** in the table
4. If found → forwards to that specific port (**filtering**)
5. If not found → floods to all ports except the source port

### MAC Address Table Summary

```
Port 1  →  AA:BB:CC:DD:EE:01  (PC-A)
Port 2  →  AA:BB:CC:DD:EE:02  (PC-B)
Port 3  →  AA:BB:CC:DD:EE:03  (PC-C)
```

> 💡 **Analogy:** The switch is a smart mailroom that keeps an **address book**. The first time it sees a device, it writes it down. After that, it delivers directly — no guessing.

---

## 4. Switch Speeds & Forwarding Methods

### Forwarding Methods

| Method | How It Works | Pros | Cons |
|---|---|---|---|
| **Store-and-forward** | Receives entire frame, checks for errors (FCS), then forwards | Accurate, catches errors | Slightly slower (higher latency) |
| **Cut-through** | Reads only destination MAC, forwards immediately | Very fast (low latency) | May forward corrupt frames |

### Cut-through Variants

| Variant | Detail |
|---|---|
| **Fast-forward** | Forwards immediately after reading destination MAC — fastest possible |
| **Fragment-free** | Reads first **64 bytes** before forwarding — filters collision fragments |

### Memory Buffering Methods

| Method | Description |
|---|---|
| **Port-based** | Each port has its own dedicated memory queue. A full queue blocks that port only. |
| **Shared** | All ports share a common memory pool. Dynamically allocated — more efficient. |

> 💡 **Analogy:**  
> - Port-based = individual lockers  
> - Shared = one big communal storage room

---

## 5. Duplex & Speed Settings (7.4.4)

### Duplex Types

| Type | Description |
|---|---|
| **Full-duplex** | Both ends can send AND receive **simultaneously** — like a two-way street |
| **Half-duplex** | Only one end can send at a time — like a walkie-talkie |

### Autonegotiation

- An **optional feature** on most Ethernet switches and NICs
- Devices automatically negotiate the **best speed and duplex** both support
- If both support full-duplex → full-duplex is selected at the **highest common bandwidth**
- Most Cisco switches and NICs default to **autonegotiation**
- **Gigabit Ethernet ports operate in full-duplex only**

### Duplex Mismatch ⚠️

A **duplex mismatch** is one of the most common causes of performance issues on 10/100 Mbps links.

**Cause:** One port operates at full-duplex, the other at half-duplex.

**Effect:** The half-duplex side experiences constant **collisions** because the full-duplex side sends data freely without checking if the line is clear.

**How it happens:**
- One or both ports are reset and autonegotiation fails to align
- A user reconfigures one side and forgets the other

**Best Practice:**
```
✅ Both sides: Autonegotiation ON
✅ Both sides: Manually set to Full-duplex
❌ Never: One side Auto, other side Manual
❌ Never: Mismatched duplex modes
```

---

## 6. Auto-MDIX (7.4.5)

### Background — Cable Types

| Connection | Required Cable |
|---|---|
| Switch ↔ Switch | ❌ Crossover cable |
| Switch ↔ Router | ✅ Straight-through cable |
| Switch ↔ Host (PC) | ✅ Straight-through cable |
| Router ↔ Host (PC) | ❌ Crossover cable |

> **Note:** A direct router-to-host connection requires a **crossover cable**.

### What is Auto-MDIX?

**Auto-MDIX (Automatic Medium-Dependent Interface Crossover)** automatically detects the cable type and adjusts internally — so either cable type works regardless of the connected device.

- Enabled by default on switches running **Cisco IOS Release 12.2(18)SE or later**
- Can be re-enabled with the command:

```bash
Switch(config-if)# mdix auto
```

### Best Practice

> Even though Auto-MDIX fixes cable mismatches automatically, **always use the correct cable type**. The feature can be disabled, and relying on it alone is not professional practice.

> 💡 **Analogy:** Auto-MDIX is like a power adapter that automatically adjusts voltage — convenient, but you should still know what voltage you need.

---

## 7. Quiz Review

### Q1 — Two switching methods for data between ports?
✅ **Store-and-forward switching**  
✅ **Cut-through switching**

> ❌ Store-and-restore, Cut-off, Store-and-supply — these do not exist.

---

### Q2 — Which method uses fast-forward or fragment-free?
✅ **Cut-through switching**

> Fast-forward and fragment-free are both **variants of cut-through switching**.

---

### Q3 — Two memory buffering techniques used by switches?
✅ **Port-based memory buffering**  
✅ **Shared memory buffering**

> ❌ Short-term and Long-term memory buffering — these do not exist.

---

### Q4 — Feature that automatically negotiates best speed and duplex?
✅ **Autonegotiation**

> Auto-MDIX handles cable type detection, not speed/duplex negotiation.

---

## Summary Cheat Sheet

```
Ethernet Frame     → Digital "shipping box" with address labels + error check
MAC Address        → 48-bit unique hardware ID (OUI + vendor value)
MAC Address Table  → Switch's "address book" — built dynamically
Store-and-forward  → Full frame received → error checked → forwarded (accurate)
Cut-through        → Destination MAC read → immediately forwarded (fast)
Fast-forward       → Cut-through: send after address only (fastest)
Fragment-free      → Cut-through: send after first 64 bytes (safer)
Port-based buffer  → Dedicated memory queue per port
Shared buffer      → One common memory pool for all ports
Full-duplex        → Two-way simultaneous (like a phone call)
Half-duplex        → One-way at a time (like a walkie-talkie)
Autonegotiation    → Devices agree on best speed + duplex automatically
Auto-MDIX          → Switch detects cable type and adjusts internally
```

---

*Last updated: May 2026 | Cisco CCNAv7 Module 7*
