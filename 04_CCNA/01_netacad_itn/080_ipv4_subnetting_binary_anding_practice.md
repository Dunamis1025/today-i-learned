# IPv4 Addressing & Subnetting — Study Notes

Consolidated notes on IPv4 address structure, subnet masks, network/broadcast
addresses, binary ANDing, and prefix length — including worked practice problems.

---

## 1. Why Subnetting Matters

Even with the ongoing shift to IPv6, most networks still rely on IPv4, so
understanding IPv4 addressing remains essential for network administrators. This
unit covers how to divide a network into subnets and how to build a full IPv4
addressing plan, including **Variable Length Subnet Masking (VLSM)**.

> **Analogy:** Subnetting is like slicing a pie into progressively smaller pieces —
> it can look complicated at first, but becomes manageable with a few tricks.

### Topics covered in this unit
- IPv4 address structure (network portion, host portion, subnet mask)
- Unicast, broadcast, and multicast addressing
- Public, private, and reserved IPv4 address types
- Network segmentation via subnetting
- Subnetting a /24 prefix
- Subnetting /16 and /8 prefixes
- Designing a subnet scheme to meet specific requirements
- Variable Length Subnet Masking (VLSM)
- Structured VLSM addressing design

---

## 2. IPv4 Address Structure

An IPv4 address is a **32-bit** number split into two parts:

- **Network portion** (left side) — identifies which network the device belongs to.
  All devices on the same network share an identical network portion.
- **Host portion** (right side) — identifies the individual device. Each device on
  the network has a unique host portion.

The **subnet mask** is what tells a device where the network portion ends and the
host portion begins — like a signpost indicating which part of an address is the
"neighborhood name" and which part is the "house number."

---

## 3. Prefix Length

Writing out a full subnet mask (e.g. `255.255.255.0`) every time is **cumbersome**
(tedious/inconvenient), so it's commonly shortened using **prefix length notation**:
count how many `1`s appear in the subnet mask's binary form, and write that number
after a slash.

| Subnet Mask | Binary | Prefix Length |
|---|---|---|
| 255.255.255.0 | `11111111.11111111.11111111.00000000` | `/24` |
| 255.255.0.0 | `11111111.11111111.00000000.00000000` | `/16` |
| 255.255.240.0 | `11111111.11111111.11110000.00000000` | `/20` |

---

## 4. Binary ANDing — Finding the Network Address

A device determines which network it belongs to by comparing its **host IP
address** and **subnet mask** bit by bit, using a **logical AND** operation:

- `1 AND 1 = 1`
- `1 AND 0 = 0`, `0 AND 1 = 0`, `0 AND 0 = 0`

In short: **the result is 1 only when both bits are 1** — otherwise it's 0.

### Worked Example 1: 192.168.2.38 /24

| Octet | Host IP (binary) | Subnet Mask (binary) | AND Result | Decimal |
|---|---|---|---|---|
| 1st | 11000000 | 11111111 | 11000000 | 192 |
| 2nd | 10101000 | 11111111 | 10101000 | 168 |
| 3rd | 00000010 | 11111111 | 00000010 | 2 |
| 4th (host) | 00100110 | 00000000 | 00000000 | 0 |

**Network address = 192.168.2.0/24**

Since this uses a /24 mask, the first three octets are the network portion, and the
last octet is the host portion. A network address always has **all binary 0s** in
its entire host portion.

### Determining the Broadcast Address
Keep the network portion the same, but set the **entire host portion to all binary
1s**.
- Network address: `192.168.2.0` (host portion = `00000000`)
- Broadcast address: `192.168.2.255` (host portion = `11111111`)

### Determining the Usable Host Range
- **First usable host** = network address + 1 (all 0s except the last bit) →
  `192.168.2.1`
- **Last usable host** = broadcast address − 1 (all 1s except the last bit) →
  `192.168.2.254`

### Recap of the example
| Value | Result |
|---|---|
| Host IP | 192.168.2.38/24 |
| Network address | 192.168.2.0 |
| Broadcast address | 192.168.2.255 |
| Usable host range | 192.168.2.1 – 192.168.2.254 |

The original host IP (`.38`) falls within this usable range, as expected.

### Key facts about IPv4 addressing
- Every IPv4 host address is 32 bits long.
- The network portion is always on the **left**; the host portion is on the
  **right**.
- Every network has **two reserved addresses that can never be assigned to a
  host**:
  - The **network address** — the lowest address in the range (all 0s in the host
    portion), representing the network itself.
  - The **broadcast address** — the highest address in the range (all 1s in the
    host portion), used to reach every device on the network at once.
- In practice, there are shortcuts for calculating these addresses without manually
  converting to binary each time — but understanding the bit-level process makes it
  clear how devices interpret addresses and how the dotted-decimal format is
  derived.

### Worked Example 2: 10.68.203.212 / 255.255.240.0

Focusing on the third octet (203 AND 240):

```
  11001011  (203, host address)
& 11110000  (240, subnet mask)
-----------
  11000000  (result = 192)
```

- Bits 1–2: both are `1` → result `1`
- Bits 3–4: host bit is `0`, mask bit is `1` → result `0`
- Bits 5–8: mask bits are all `0` → result is always `0`, regardless of the host bits

The last octet (212 AND 0) becomes `0` no matter what, since ANDing with an all-zero
mask always produces `0`.

**Result: Network address = 10.68.192.0**

---

## 5. Three Types of IPv4 Addresses

| Address Type | Description | Host Portion |
|---|---|---|
| **Network Address** | Represents the network itself; cannot be assigned to a device | All 0s |
| **Host Address** | Assigned to actual devices (computers, phones, printers, etc.) | Anything except all 0s or all 1s |
| **Broadcast Address** | Used to reach every device on the network at once; cannot be assigned to a device | All 1s |

---

## 6. Practice Questions

**Q1.** Host-A has IPv4 address `10.5.4.100`, subnet mask `255.255.255.0`. What is
the network address?
> **Answer: 10.5.4.0** — the mask fixes the first three octets (`10.5.4`) as the
> network portion, so the host portion (last octet) becomes 0.

**Q2.** Host-A has IPv4 address `172.16.4.100`, subnet mask `255.255.0.0`. What is
the network address?
> **Answer: 172.16.0.0** — the mask fixes the first two octets (`172.16`), so the
> last two octets become 0.

**Q3.** Host-A has IPv4 address `10.5.4.100`, subnet mask `255.255.255.0`. Which
addresses are on the same network as Host-A?
> **Answer: 10.5.4.1 and 10.5.4.99** — any address starting with `10.5.4` is on the
> same network.

**Q4.** Host-A has IPv4 address `172.16.4.100`, subnet mask `255.255.0.0`. Which
addresses are on the same network as Host-A?
> **Answer: 172.16.4.99 and 172.16.0.1** — any address starting with `172.16` is on
> the same network.

**Q5.** Host-A has IPv4 address `192.168.1.50`, subnet mask `255.255.255.0`. Which
addresses are on the same network as Host-A?
> **Answer: depends on the options given** — any address starting with `192.168.1`
> qualifies (e.g., `192.168.1.100` and `192.168.1.1` would both be correct matches).
> The key check is always: do the first three octets match `192.168.1`?

---

## 7. Related Vocabulary

- **Cumbersome** — tedious, awkward to deal with. Used to describe why prefix
  length notation (`/24`) is preferred over writing out the full subnet mask
  (`255.255.255.0`).
- **Adjacencies** — plural of *adjacency* (a fully synchronized neighbor
  relationship between two OSPF routers). A network can have multiple adjacencies
  at once, one per router pair.
- **Ingress (port)** — the port through which a frame or packet *enters* a device
  (opposite: **egress**, the port through which it exits). Example: a switch floods
  an incoming frame out of every port *except the ingress port* when the
  destination MAC is unknown or the frame is a broadcast.

---

## Summary

IPv4 addressing splits every 32-bit address into a network portion and a host
portion, with the subnet mask defining the boundary between them. Using **binary
ANDing**, a device can derive its network address from its IP and subnet mask; the
network address (all-0 host bits) and broadcast address (all-1 host bits) are
reserved and never assignable, leaving everything in between as the usable host
range. Prefix length (`/24`, `/16`, etc.) is simply a shorthand for the subnet mask,
counting the number of leading 1-bits.
