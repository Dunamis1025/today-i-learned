# IPv4 & IPv6 Addressing — Study Notes

## Part 1: IPv4 Subnetting Fundamentals

### Core Concept: Network vs. Host Portion
An IPv4 address has two components:
- **Network portion** — identifies which network (the "neighborhood")
- **Host portion** — identifies the specific device on that network (the "house")

The **subnet mask** determines where the split between these two portions happens.

### Prefix Length Notation
Prefix length (e.g. `/27`) counts the number of consecutive `1` bits in the subnet mask.

| Mask (decimal) | Binary | Prefix Length |
|---|---|---|
| 255.255.255.224 | 11111111.11111111.11111111.11100000 | /27 |
| 255.255.255.240 | 11111111.11111111.11111111.11110000 | /28 |
| 255.255.240.0 | 11111111.11111111.11110000.00000000 | /20 |

**Relationship between host bits and mask:**
- Host bits = 32 − prefix length
- Prefix length = 32 − host bits

| Host bits available | Subnet mask (last octet) |
|---|---|
| 4 | 240 (11110000) |
| 5 | 224 (11100000) |

### Usable Host Addresses Formula
```
Usable hosts = 2^(host bits) − 2
```
The `−2` accounts for:
1. The **network address** (all host bits = 0)
2. The **broadcast address** (all host bits = 1)

| Mask | Host bits | Total addresses | Usable hosts |
|---|---|---|---|
| /24 | 8 | 256 | 254 |
| /26 | 6 | 64 | 62 |
| /27 | 5 | 32 | 30 |
| /28 | 4 | 16 | 14 |

### Subnetting a Network (Borrowing Bits)
When a `/24` network is subnetted into `/26`, 2 bits are borrowed (26 − 24 = 2), creating:
```
2^(borrowed bits) = 2^2 = 4 equal-sized subnets
```

### Variable-Length Subnet Masking (VLSM)
VLSM allows **different-sized subnets within the same network**, sized according to actual need (rather than one fixed subnet size everywhere). This reduces wasted IP addresses.

### Purpose of the Subnet Mask
The subnet mask's job is **to determine which subnet a host belongs to** — it tells a device (or router) where the network portion ends and the host portion begins.

### Why Layer 3 Devices Perform ANDing
A **Layer 3 device** (router, Layer 3 switch) uses IP addresses — not MAC addresses — to make forwarding decisions.

**ANDing** = a binary logical operation:
```
1 AND 1 = 1
1 AND 0 = 0
0 AND 1 = 0
0 AND 0 = 0
```

When a device ANDs a destination IP with the subnet mask:
- Every bit where the mask = 1 → passes the IP bit through unchanged
- Every bit where the mask = 0 → forced to 0

**Result: the pure network address**, stripped of the host portion.

```
IP:      11000000.10101000.00000001.00001010  (192.168.1.10)
Mask:    11111111.11111111.11111111.00000000  (255.255.255.0)
AND  →   11000000.10101000.00000001.00000000  (192.168.1.0)
```

**Purpose:** to identify the network address of the destination, so the device can decide whether to deliver data directly (same network) or forward it to a router/gateway (different network).

---

## Part 2: Why IPv6? (Module Objective)

**Module goal:** implement an IPv6 addressing **scheme** — i.e., a *design plan* for how IPv6 addresses will be allocated, subnetted, and assigned across a network (which blocks go to which networks, how subnets are divided, which addresses go to which devices).

### The IPv4 Exhaustion Problem
- IPv4's 32-bit space is running out globally.
- All **5 Regional Internet Registries (RIRs)** — the organizations that allocate IP address blocks by continent to ISPs and large organizations — have already exhausted their free IPv4 pools (not just some of them).
- Explosive growth of internet-connected devices (smartphones, appliances, cars — IoT) has intensified the shortage.
- **NAT** (Network Address Translation) extended IPv4's life but has scalability/complexity limits.

### The IPv6 Solution
- **128-bit address space** → practically unlimited unique addresses.
- Every device can get a **globally unique address**, removing the need for NAT workarounds.

### Coexistence Strategies (IPv4 ↔ IPv6 Transition)

| Strategy | What it does | Analogy |
|---|---|---|
| **Dual Stack** | A device runs IPv4 and IPv6 simultaneously; native IPv6 connectivity | A bilingual person responding in whichever language is spoken to them |
| **Translation** (e.g. NAT64) | Converts addresses between IPv4 and IPv6 so the two can communicate | A translator standing between two people who speak different languages |
| **Tunneling** | Encapsulates IPv6 packets inside IPv4 packets to cross an IPv4-only segment, then unwraps them on the other side | Putting a Korean letter inside an English-addressed envelope |

Dual stack is the **native**, most direct connectivity method — no translation or encapsulation involved.

---

## Part 3: IPv6 Address Representation

### Structure: 8 Hextets (16-bit Segments)
An IPv6 address is **128 bits total**, split into **8 groups of 16 bits**, separated by colons:
```
X:X:X:X:X:X:X:X
```
Each group ("hextet") is written as **4 hexadecimal digits** (`0000`–`ffff`).

**Why hex?** Because 1 hex digit = exactly 4 binary digits:
```
0010 0000 0000 0000  (binary, 16 bits)
 2  +  0  +  0  +  0   (convert each 4-bit chunk separately)
 = 2000  (hex)
```

Quick reference table (binary → hex, per 4 bits):

| Binary | Hex | Binary | Hex |
|---|---|---|---|
| 0000 | 0 | 1000 | 8 |
| 0001 | 1 | 1001 | 9 |
| 0010 | 2 | 1010 | a |
| 0011 | 3 | 1011 | b |
| 0100 | 4 | 1100 | c |
| 0101 | 5 | 1101 | d |
| 0110 | 6 | 1110 | e |
| 0111 | 7 | 1111 | f |

**If written in raw binary**, an IPv6 address would be 128 digits long — 4× longer than IPv4's 32 bits. Hex compresses this to 32 characters, which is why IPv6 uses hex instead of binary/decimal.

### Compression Rules
1. **Omit leading zeros** within each hextet: `0db8` → `db8` (trailing zeros CANNOT be omitted — ambiguous otherwise).
2. **`::` compresses one run of consecutive all-zero hextets** — but **only once per address**.

**Why only once?** If `::` appeared twice, there would be no way to know how many zero-groups belong to each `::` — the address becomes ambiguous and invalid.

**Example:**
```
Full:        2001:0000:0db8:1111:0000:0000:0000:0200
Step 1 (omit leading zeros):  2001:0:db8:1111:0:0:0:200
Step 2 (compress longest run of consecutive zeros — here, 3 groups):
Compressed:  2001:0:db8:1111::200
```
✅ Correct — only ONE `::` used, and it replaces the *longest* consecutive run of zero groups.
❌ `2001::db8:1111::200` — invalid, uses `::` twice.

---

## Part 4: IPv6 Address Types

| Type | Purpose | Notes |
|---|---|---|
| **Unicast** | One-to-one communication with a specific device | Includes GUA, LLA, ULA |
| **Multicast** | One packet delivered to a defined group of devices | Replaces IPv4 broadcast (see below) |
| **Anycast** | Delivered to the nearest/most efficient device among a group | — |
| ~~Broadcast~~ | **Does not exist in IPv6** | Replaced by multicast |

### Why No Broadcast in IPv6?
IPv4 broadcast forced **every device** on the network to receive and process the packet, even if irrelevant — wasting CPU and bandwidth (like an apartment-wide announcement everyone must listen to).

IPv6 replaces this with **multicast**: only devices that joined a specific multicast group receive the message (like a group chat only relevant people are in).

Example: `FF02::1` = "all-nodes" multicast address — reaches every IPv6 device on the local link, but through group-based delivery, not a forced broadcast.

### Prefix Length in IPv6
Written as `/0` to `/128` after the address. **`/64`** is the standard/common network portion size for most networks.

---

## Part 5: GUA vs. LLA

### Global Unicast Address (GUA)
- Equivalent to a **public IPv4 address**: globally unique and routable across the internet.
- Currently assigned GUAs begin with binary `001` in the first 3 bits (i.e., **`2000::/3`** range).
  - First hextet range: `2000` to `3fff` (hex)
- **`2001:db8::/32`** is reserved specifically for documentation/examples — not a real routable address.

**GUA structure (3 parts):**

| Part | Size (common) | Assigned by | Role |
|---|---|---|---|
| Global Routing Prefix | 48 bits | ISP | Identifies the organization/site on the internet |
| Subnet ID | 16 bits | The organization, internally | Divides the org's network into subnets |
| Interface ID | 64 bits | Device (auto or manual) | Identifies the specific device |

- 48-bit prefix + 16-bit subnet ID = 64 bits → matches the common **`/64`** network boundary.
- The remaining 64 bits (Interface ID) identify the host.

**Important distinction from IPv4:** IPv6 GUA does **not** need to "borrow bits" from the Interface ID to create subnets — Global Routing Prefix, Subnet ID, and Interface ID are already cleanly separated by design.

### Link-Local Address (LLA)
- Starts with **`fe80::`** (prefix `FE80::/10`).
- **Automatically generated** on every IPv6-enabled interface — no manual configuration required.
- **Only valid within the local link (same network segment)** — routers never forward LLA traffic across network boundaries.

**Visual proof (from network diagrams):**
- Two hosts on the same switch (e.g., `fe80::aaaa` and `fe80::dddd`) **can** communicate via LLA.
- Any attempt for an LLA packet to cross a **router** is blocked (✗) — routers do not route link-local traffic to other links.

**Why is LLA still useful despite this limitation?**

| Use case | Who uses it | Why LLA is sufficient |
|---|---|---|
| Routing protocol updates (e.g. OSPF, EIGRP) between neighboring routers | Router ↔ Router | Neighbors are directly connected on the same link — no need to cross a router |
| Default gateway address for hosts | Host → local router | The gateway is on the same local network — no cross-router communication required |

So LLA isn't "useless" outside its own link — it's specifically designed for **same-link** communication, which covers two very common and important scenarios: router-to-neighbor-router messaging, and host-to-gateway communication.

### Unique Local Address (ULA)
- Similar role to IPv4 **private addresses**.
- Not globally routable — used for internal/site-to-site communication only, without exposure to the public internet.

---

## Quick Reference Summary

| Concept | IPv4 | IPv6 |
|---|---|---|
| Address length | 32 bits | 128 bits |
| Notation | Decimal, dot-separated (4 octets) | Hex, colon-separated (8 hextets) |
| Common prefix | Varies (/24, /27, etc.) | /64 standard |
| Broadcast | Yes | No (replaced by multicast) |
| Address exhaustion | Yes (all RIRs depleted) | Practically unlimited |
| Private/local addressing | Private IP (RFC 1918) | ULA / LLA |
| Subnetting | Borrow bits from host portion | Prefix/Subnet ID/Interface ID are pre-separated — no borrowing needed |
