# IPv4 Subnetting — Study Notes

A complete reference covering binary-decimal conversion, subnetting theory, the "magic number" shortcut, and six fully worked practice problems.

---

## 1. Binary ↔ Decimal Basics

Each bit in an 8-bit octet has a fixed place value:

| Bit position | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Place value | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

To convert binary → decimal, sum the place values where the bit is `1`.

```
11111111 = 128+64+32+16+8+4+2+1 = 255   (all bits on — max value of an octet)
11100000 = 128+64+32             = 224
11000000 = 128+64                = 192
10000000 = 128                   = 128
11111000 = 128+64+32+16+8        = 248
11111100 = 128+64+32+16+8+4      = 252
```

Common powers of 2 (subnet/host counts always come from these):

| 2^n | Value |
|---|---|
| 2^1 | 2 |
| 2^2 | 4 |
| 2^3 | 8 |
| 2^5 | 32 |
| 2^6 | 64 |
| 2^7 | 128 |
| 2^8 | 256 |
| 2^9 | 512 |
| 2^13 | 8,192 |
| 2^15 | 32,768 |

**Key insight:** the number of `1`s in the borrowed portion of the mask = number of subnet bits, and reading a mask value like 224 or 248 is just "how many leading 1s does it take to reach this number."

---

## 2. What Subnetting Actually Does

Subnetting means **borrowing bits from the host portion** of an IP address and reassigning them to the network portion. This lets one large network be split into many smaller ones.

**The trade-off, one bit at a time:**
- Each bit borrowed → number of subnets **doubles** (×2)
- Each bit borrowed → number of hosts per subnet **halves** (÷2)

This is why subnetting is a balancing act between "how many networks do I need" and "how many devices per network do I need."

### Formulas

| Quantity | Formula |
|---|---|
| Subnet bits borrowed | new prefix length − original prefix length |
| Number of subnets created | 2^(borrowed bits) |
| Host bits remaining | (original host bits) − (borrowed bits) |
| Usable hosts per subnet | 2^(remaining host bits) − 2 (subtract network address + broadcast address) |

### Sizing a subnet plan to a requirement

To get **at least N subnets**, find the smallest number of bits *b* such that 2^b ≥ N.
- Need 100+ subnets → borrow 7 bits (2^7 = 128 ≥ 100)
- Need 1,000+ subnets → borrow 10 bits (2^10 = 1,024 ≥ 1,000)
- Need 300+ subnets of 20,000+ hosts each (from a /8) → borrow 9 bits (2^9 = 512 subnets), leaving 15 host bits (2^15−2 = 32,766 hosts) — satisfies both requirements simultaneously.

---

## 3. Subnet Masks in Binary and Decimal

A subnet mask is just: `1`s for every network/subnet bit, `0`s for every host bit.

| Prefix | Binary (last relevant octet) | Decimal |
|---|---|---|
| /17 | 10000000 | 128 |
| /18 | 11000000 | 192 |
| /19 | 11100000 | 224 |
| /20 | 11110000 | 240 |
| /24 | 11111111 | 255 |
| /30 | 11111100 | 252 |

General rule: if *n* bits are borrowed in an octet, that octet's mask value = 256 − 2^(8−n).

---

## 4. The "Magic Number" (a.k.a. Block Size)

This is the single most useful shortcut in subnetting.

$$\text{Magic Number} = 256 - (\text{mask value of the "interesting octet"})$$

**The "interesting octet"** is the one octet in the new subnet mask that is neither 255 nor 0 — the octet where the actual bit-borrowing happened. This is *not always the last octet* — it depends on where the new mask value sits (2nd, 3rd, or 4th octet).

Once you have the magic number:
1. **Subnet boundaries** in the interesting octet go `0, magic, 2×magic, 3×magic, …` up to 256.
2. **Network Address** = round the IP's interesting-octet value *down* to the nearest multiple of the magic number.
3. **Broadcast Address** = one less than the *next* boundary.
4. **First Host** = Network Address + 1.
5. **Last Host** = Broadcast Address − 1.

The magic number also directly tells you the remaining host bits, since magic number = 2^(host bits left in that octet). E.g. magic number 8 = 2^3 → 3 host bits remain.

**Why "the interesting octet" matters:** if the borrowed bits land in the 2nd or 3rd octet instead of the last one, you must check *that* octet of the IP address against the block list — not the last octet. Mixing this up (checking the wrong octet) was the single most common mistake in this study session.

---

## 5. Worked Examples (All Six Practice Problems)

### Problem 1
- IP: `192.168.200.139` | Original mask: `255.255.255.0` | New mask: `255.255.255.224`
- 224 = `11100000` → 3 bits borrowed
- Subnets created = 2³ = 8
- Host bits left = 8−3 = 5 → Hosts/subnet = 2⁵−2 = 30
- Magic number = 256−224 = 32 → boundaries: 0,32,64,96,**128**,160,192,224
- 139 falls in 128–159 → Network = `192.168.200.128`
- First host = `.129`, Last host = `.158`, Broadcast = `.159`

### Problem 2
- IP: `10.101.99.228` | Original mask: `255.0.0.0` | New mask: `255.255.128.0`
- Interesting octet = **3rd octet** (128), not the last octet
- 9 bits borrowed (255=8 bits + 128=1 bit) → 512 subnets
- Host bits left = 24−9 = 15 → Hosts/subnet = 2¹⁵−2 = 32,766
- Magic number = 256−128 = 128 (applied to 3rd octet) → boundaries: 0, **128**, 256
- IP's 3rd octet = 99 → falls in 0–127 → Network = `10.101.0.0`
- First host = `10.101.0.1`, Last host = `10.101.127.254`, Broadcast = `10.101.127.255`

### Problem 3
- IP: `172.22.32.12` | Original mask: `255.255.0.0` | New mask: `255.255.224.0`
- 224 = `11100000` → 3 bits borrowed (not 7 — count leading 1s carefully)
- Subnets created = 2³ = 8
- Host bits left = 16−3 = 13 → Hosts/subnet = 2¹³−2 = 8,190
- Interesting octet = 3rd (224) → Magic number = 256−224 = 32 → boundaries: 0,**32**,64,96,128,160,192,224
- IP's 3rd octet = 32 → falls in 32–63 → Network = `172.22.32.0`
- First host = `172.22.32.1`, Last host = `172.22.63.254`, Broadcast = `172.22.63.255`

### Problem 4
- IP: `192.168.1.245` | Original mask: `255.255.255.0` | New mask: `255.255.255.252`
- 252 = `11111100` → 6 bits borrowed → 2⁶ = 64 subnets
- Host bits left = 8−6 = 2 → Hosts/subnet = 2²−2 = 2 (classic point-to-point /30 link size)
- Magic number = 256−252 = 4 → boundaries: 0,4,8,…,240,**244**,248
- IP's last octet = 245 → falls in 244–247 → Network = `192.168.1.244`
- First host = `.245`, Last host = `.246`, Broadcast = `.247`

### Problem 5
- IP: `128.107.0.55` | Original mask: `255.255.0.0` | New mask: `255.255.255.0`
- 255 = `11111111` → 8 bits borrowed → 2⁸ = 256 subnets (classic "chop a /16 into /24s")
- Host bits left = 16−8 = 8 → Hosts/subnet = 2⁸−2 = 254
- Interesting octet = 3rd (255) → Magic number = 256−255 = 1 → every value in the 3rd octet is its own subnet
- IP's 3rd octet = 0 → Network = `128.107.0.0`
- First host = `128.107.0.1`, Last host = `128.107.0.254`, Broadcast = `128.107.0.255`

### Problem 6
- IP: `192.135.250.180` | Original mask: `255.255.255.0` | New mask: `255.255.255.248`
- 248 = `11111000` → 5 bits borrowed → 2⁵ = 32 subnets
- Host bits left = 8−5 = 3 → Hosts/subnet = 2³−2 = 6
- Magic number = 256−248 = 8 → boundaries: 0,8,16,24,…,168,**176**,184,…,248
- IP's last octet = 180 → falls in 176–183 → Network = `192.135.250.176`
- First host = `.177`, Last host = `.182`, Broadcast = `.183`

---

## 6. Subnetting Large (Class A / Class B) Networks

The exact same logic scales up — the magic number can apply to the 2nd or 3rd octet instead of just the last one, and iterates through *every* possible value of the octets to its left before moving to the next block.

**Example — 10.0.0.0/8 subnetted to /11 (3 bits borrowed):**
- Magic number is still 32, but it applies to the **2nd octet** now.
- Subnets: 10.0.0.0, 10.32.0.0, 10.64.0.0, 10.96.0.0 … each with over 2,000,000 usable hosts (21 host bits remain).
- Example: subnet `10.192.0.0/11` → next subnet is `10.224.0.0` → so usable hosts range from `10.192.0.1` to `10.223.255.254`, broadcast `10.223.255.255`.

**Example — need 300+ subnets of 20,000+ hosts each from 10.0.0.0/8:**
- Borrowing 9 bits → 2⁹ = 512 subnets (≥ 300 ✓)
- Remaining host bits = 15 → 2¹⁵−2 = 32,766 hosts/subnet (≥ 20,000 ✓)
- New mask: `255.255.128.0` (magic number 128 in the 3rd octet)
- Subnets iterate through every value of the 2nd octet before the 3rd octet flips: `10.0.0.0`, `10.0.128.0`, `10.1.0.0`, `10.1.128.0`, … all the way to `10.255.0.0`, `10.255.128.0` — 512 total subnets, each a /17.

**Takeaway:** no matter how large the network or how many bits are borrowed, the same magic-number method always works — you just need to correctly identify which octet is "interesting" and remember that boundaries roll over into the next octet to the left once a full octet's range (256) is used up.

---

## 7. Common Mistakes to Watch For

1. **Miscounting bits in binary.** `224 = 11100000` (3 ones), not `11111110`. Always sum place values (128+64+32...) rather than guessing.
2. **Applying the magic number to the wrong octet.** Always find the "interesting octet" (the one in the new mask that isn't 255 or 0) — the block-size logic applies there, not automatically to the last octet.
3. **Forgetting to subtract 2 for hosts per subnet** (network address and broadcast address aren't assignable to devices).
4. **Off-by-one errors on boundaries** — Broadcast Address is one less than the *next* subnet's start, not the current subnet's magic-number value itself.

---

## 8. Quick Formula Reference

```
Subnet bits borrowed        = new prefix − original prefix
Subnets created              = 2^(borrowed bits)
Host bits remaining          = original host bits − borrowed bits
Hosts per subnet              = 2^(remaining host bits) − 2
Magic number (block size)     = 256 − (mask value of interesting octet)
Network Address                = round IP's interesting octet down to nearest multiple of magic number
Broadcast Address              = (next boundary) − 1
First Host                     = Network Address + 1
Last Host                      = Broadcast Address − 1
```
