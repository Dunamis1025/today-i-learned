# Day 07: IPv4 Addressing (Part 1)

> Detailed English summary of Jeremy's IT Lab CCNA 200-301 video **"Free CCNA | IPv4 Addressing (Part 1)"** — based on the user's Gemini-generated Korean notes, expanded, translated, and gap-filled with additional explanations. Continues the topic sequence after `11_day06_ethernet_lan_switching_part2_arp_ping_mac_table.md` (Layer 2 concepts), now moving up to **Layer 3 (Network Layer)**.

---

## 1. OSI Layer 3 (Network Layer) Overview and the Role of the Router

### Layer 3 — Network Layer

- Provides connectivity **between hosts on different networks** — going beyond the local network (LAN) boundary that Layer 2 (switches) operates within.
- Unlike Layer 2's **MAC addresses** (physical, burned-in), Layer 3 uses **logical addresses**: **IP addresses**.
- Performs **path selection** — finding the best route from source to destination across a complex web of interconnected networks.

> **Added clarification — "logical" vs. "physical" addressing:** a MAC address is permanently burned into a device's hardware and never changes no matter where the device is plugged in (Day 05). An IP address, by contrast, is **assigned by software/configuration** based on *where* a device is connected in the network — move a PC to a different network, and it needs a *different* IP address to communicate, even though its MAC address stays the same. This is precisely why IP addresses (not MAC addresses) are used for routing between networks: routing decisions need to reflect network *location*, and only a logical, reassignable address can do that.

### The Router

- **Routers operate at Layer 3.**
- Recap: **switches** connect devices *within* a single LAN (Day 05). **Routers** connect *different* LANs together.
- When a router sits in the middle of a topology, it **splits one large network into multiple separate, independent networks.**
- **Each interface on a router must have its own unique IP address** — because each router interface sits on a *different* network, and every network needs at least one address representing each connected device (including the router itself) on that network.
- **Broadcasts do not cross routers.** A broadcast frame is confined to the local network it originated in; the router acts as the boundary that stops it from propagating further.

> **Added clarification — why broadcast containment matters:** this is a critical practical reason routers exist beyond just "connecting networks." As a network grows larger, broadcast traffic (like ARP requests, covered in Day 06) grows too — every host has to process every broadcast frame sent on its network. Without routers breaking a large network into smaller ones, broadcast traffic would keep increasing and eventually overwhelm every device on the network (known as a "broadcast storm" in extreme cases). This is one of the core reasons real networks are divided into multiple smaller LANs connected by routers (and, later in CCNA, VLANs plus routers/Layer 3 switches) rather than one giant flat network.

---

## 2. IPv4 Address Structure and Notation (Binary vs. Dotted Decimal)

### IPv4 Address Length

- **32 bits total (4 bytes).**

### Octets

- The 32 bits are split into **4 groups of 8 bits each**, and each 8-bit group is called an **octet** (8 × 4 = 32 bits).

### Dotted Decimal Notation

- Computers work in binary (1s and 0s), but binary is very hard for humans to read and write reliably.
- So each 8-bit octet is converted into its **decimal equivalent (0–255)** and the four octets are separated by periods (`.`) — this format is called **dotted decimal notation**.
- Example: `192.168.1.254` — each number represents one octet (8 bits).

> **Added clarification — why exactly 0–255 per octet:** 8 bits can represent 2⁸ = 256 different values, and since counting starts at 0, the range of a single byte is 0 through 255 (256 total values). This directly explains why you never see a number like "256" or "300" in a valid IPv4 address — it's mathematically impossible to represent with only 8 bits.

---

## 3. Binary ↔ Decimal Conversion Basics

To work with IPv4 addresses (subnetting, CIDR, etc.), you need to memorize the **positional weight of each bit** in an 8-bit octet. Each position, moving from right to left, doubles in value:

```
128 | 64 | 32 | 16 | 8 | 4 | 2 | 1
```

### Conversion Method: Decimal → Binary (worked example: 221)

The method is a repeated "can I subtract this weight?" test, working from the largest weight (128) down to the smallest (1):

| Weight | Can I subtract it? | Remaining value | Bit |
|--------|----------------------|--------------------|-----|
| 128 | Yes (221 ≥ 128) | 221 − 128 = 93 | **1** |
| 64 | Yes (93 ≥ 64) | 93 − 64 = 29 | **1** |
| 32 | No (29 < 32) | 29 | **0** |
| 16 | Yes (29 ≥ 16) | 29 − 16 = 13 | **1** |
| 8 | Yes (13 ≥ 8) | 13 − 8 = 5 | **1** |
| 4 | Yes (5 ≥ 4) | 5 − 4 = 1 | **1** |
| 2 | No (1 < 2) | 1 | **0** |
| 1 | Yes (1 ≥ 1) | 1 − 1 = 0 | **1** |

**Result: 221 = `11011101`**

### The Range of an 8-bit Octet

- **0 (`00000000`) to 255 (`11111111`)** — as explained above, this is the full range of values representable in 8 bits.

> **Added clarification — converting Binary → Decimal (the reverse direction, not explicitly detailed in the notes but essential to know both ways):** simply add up the weight values wherever there's a `1` bit. For example, `11011101` → 128 + 64 + 0 + 16 + 8 + 4 + 0 + 1 = **221**. Being fast at *both* directions of this conversion (decimal→binary and binary→decimal) is essential for CCNA subnetting questions, which are timed on the real exam.

---

## 4. Network Portion vs. Host Portion

Every IP address is logically split into two parts:

| Part | Meaning |
|------|---------|
| **Network portion** | Identifies *which network* ("neighborhood") the address belongs to. All devices on the same network share an identical network portion. |
| **Host portion** | Identifies the *individual device* ("house") within that network. |

> **Added clarification — the neighborhood/house analogy extended:** this is very similar to how a street address works — the street name + suburb/city (network portion) tells you which neighborhood a house is in, while the house number (host portion) picks out one specific house within that neighborhood. Just as two houses on the same street share the street name but have different house numbers, two devices on the same IP network share the same network portion but have different host portions.

### Prefix Length (CIDR Notation)

- A `/24` (or similar) written after an IP address is called **CIDR notation** (Classless Inter-Domain Routing notation) or **prefix length**, and it means: **"the first N bits (starting from the left) are the network portion; the rest are the host portion."**

| Prefix | Network bits | Host bits | Network portion (octets) | Host portion (octets) |
|--------|-----------------|--------------|------------------------------|----------------------------|
| **/24** | 24 bits | 8 bits | First 3 octets | Last 1 octet |
| **/16** | 16 bits | 16 bits | First 2 octets | Last 2 octets |
| **/8** | 8 bits | 24 bits | First 1 octet | Last 3 octets |

> **Added clarification — where the term "CIDR" comes from and why it matters:** CIDR was introduced in the 1990s to replace the older, more rigid **classful** addressing system (Section 5, below) because classful addressing wasted enormous numbers of IP addresses. CIDR allows the network/host boundary to fall at *any* bit position (not just at octet boundaries like /8, /16, /24), which is far more flexible — e.g., `/27` or `/29` are valid and commonly used in real networks, splitting a network's host bits far more precisely than the old class-based system ever could. This video's examples use /8, /16, /24 because those line up conveniently with the classful boundaries being taught, but subnetting (likely covered in a later video) breaks addresses at arbitrary bit positions using this same CIDR notation.

---

## 5. IPv4 Address Classes (Class A, B, C, D, E)

Historically, IPv4 addresses were divided into 5 classes based on the value/starting bit pattern of the *first* octet. Classes A, B, and C are used for regular network communication.

| Class | First octet starting bits | First octet decimal range | Default prefix | Characteristics |
|-------|-------------------------------|-------------------------------|--------------------|---------------------|
| **Class A** | `0...` | 0 – 127 | `/8` | Few networks, but each network can have a huge number of hosts (large enterprises/countries) |
| **Class B** | `10...` | 128 – 191 | `/16` | Medium number of networks and hosts (medium-to-large enterprises) |
| **Class C** | `110...` | 192 – 223 | `/24` | Many networks, but only 256 hosts per network (small offices/homes) |
| **Class D** | `1110...` | 224 – 239 | — | Reserved for **Multicast** |
| **Class E** | `1111...` | 240 – 255 | — | Reserved for **research and experimentation** |

> **Added clarification — is classful addressing still used today?** No — in modern networks, **classless (CIDR-based) addressing** has completely replaced the old rule where the class of an address rigidly determined its default prefix length. Today, a `192.168.1.0` address could just as easily be configured with a `/25`, `/26`, or any other prefix, regardless of it "being" a Class C address. However, CCNA still teaches classful addressing because: (1) it's foundational for understanding how subnetting evolved and why prefix lengths line up the way they do, and (2) some legacy terminology and exam questions still reference class ranges. The class ranges themselves (A/B/C/D/E, with their first-octet ranges) remain true as a way to categorize an address's default class, even though routers no longer *enforce* class-based rules in practice.

### ⚠️ Exception: Loopback Address (127.x.x.x)

- The range `127.0.0.0 – 127.255.255.255` falls within the Class A range numerically, but it is **reserved as the loopback address block** (most commonly represented by `127.0.0.1`) — used by a computer to **test its own network stack** by sending traffic to itself.
- Because this entire block is reserved for this special self-test purpose, it **cannot be assigned as a regular host address** to any device.

> **Added clarification — what "testing your own network stack" actually means in practice:** if you ping `127.0.0.1` on your own PC, the packet never actually leaves your computer or touches any physical network card — it's immediately looped back internally by the operating system. This is useful for confirming that a computer's own TCP/IP software is installed and functioning correctly, *independent* of whether its network cable, Wi-Fi, or any external network is working. It's commonly used as a first troubleshooting step: "can I even ping myself?" before checking anything about the actual network.

---

## 6. Subnet Mask

- On Cisco devices (and elsewhere), instead of writing `/24`, you can express the same network/host split using a **subnet mask** written in dotted decimal notation.
- A subnet mask fills the **network portion with all 1s (255 in decimal)** and the **host portion with all 0s**.

| Class | Prefix | Subnet Mask |
|-------|--------|-----------------|
| Class A | `/8` | `255.0.0.0` |
| Class B | `/16` | `255.255.0.0` |
| Class C | `/24` | `255.255.255.0` |

> **Added clarification — how a device actually uses the subnet mask:** the subnet mask isn't just a display format — it's what a device (PC, router) uses in a bitwise **AND** operation against its own IP address to calculate the **network address** (see Section 7) it belongs to, and to decide whether a destination IP address is on its own local network or needs to be sent to a router to reach a different network. This is also *why* CIDR notation (`/24`) and subnet mask notation (`255.255.255.0`) are two different ways of writing the exact same information — one counts the number of `1` bits directly, the other spells out which bits are `1` in dotted decimal form.

---

## 7. Two Special-Purpose IP Addresses (Network Address & Broadcast Address)

Every IP network range has **two addresses that can never be assigned to an actual host device.**

### Network Address

- The address where **all host-portion bits are 0** (e.g., `192.168.1.0` for a `/24` network).
- This represents the network *itself* — it's essentially the "name" of the network — so it **cannot be assigned to a PC or router interface as an individual IP address.**

### Broadcast Address

- The address where **all host-portion bits are 1** (e.g., `192.168.1.255` for a `/24` network).
- This is the destination IP address used to send data to **every device on that network simultaneously** — it also **cannot be assigned to an individual host.**

### Conclusion: Usable Host Addresses in a /24 Network

- A `/24` network has 256 total possible addresses (2⁸, since 8 host bits remain).
- Subtracting the Network Address (1) and the Broadcast Address (1) leaves **254 usable host addresses.**

> **Added clarification — the general formula for usable hosts (not explicit in the notes, but a natural extension of the /24 example given):** for any prefix length with *h* host bits remaining, the total number of addresses in that network is **2ʰ**, and the number of **usable** host addresses is **2ʰ − 2** (always subtracting the network and broadcast addresses). For example:
>
> | Prefix | Host bits (h) | Total addresses (2ʰ) | Usable hosts (2ʰ − 2) |
> |--------|-------------------|---------------------------|-----------------------------|
> | /24 | 8 | 256 | 254 |
> | /16 | 16 | 65,536 | 65,534 |
> | /8 | 24 | 16,777,216 | 16,777,214 |
>
> This formula (2ʰ − 2) is one of the single most frequently tested calculations on the actual CCNA exam, especially once subnetting (breaking networks into smaller pieces with non-default prefixes like /26, /27, /28) is introduced — expect it to reappear constantly in later material.

---

## 8. Quick Summary

- **Layer 3 (Network Layer)** connects hosts across different networks using logical **IP addresses**, and routers are the Layer 3 devices that perform this connection while also containing broadcast traffic to each local network.
- An **IPv4 address is 32 bits**, written as 4 **octets** (8 bits each) in **dotted decimal notation** (0–255 per octet).
- Binary-to-decimal conversion relies on the positional weights **128-64-32-16-8-4-2-1**.
- Every IP address splits into a **network portion** and a **host portion**, with the split point indicated by **CIDR notation** (`/8`, `/16`, `/24`, etc.) or, equivalently, a **subnet mask** in dotted decimal form.
- IPv4 addresses were historically split into 5 **classes** (A, B, C for regular use; D for multicast; E for research) based on the first octet's value — though classful addressing is now superseded by classless (CIDR) addressing in practice.
- `127.0.0.0/8` is reserved as the **loopback** range and can't be used as a regular host address.
- Every network has a **Network Address** (all host bits 0) and a **Broadcast Address** (all host bits 1), neither of which can be assigned to a host — leaving **2ʰ − 2** usable addresses for any network with *h* host bits.

---

## 9. Command / Concept Cheat Sheet

| Term | Meaning |
|------|---------|
| IPv4 address | 32-bit logical (Layer 3) address, written as 4 octets in dotted decimal |
| Octet | An 8-bit group; 4 octets make up a full IPv4 address |
| CIDR notation / Prefix length | `/N` after an IP, meaning the first N bits are the network portion |
| Subnet mask | Dotted-decimal equivalent of the prefix length (all 1s = network, all 0s = host) |
| Class A/B/C | Historical address classes for regular host use, based on first-octet value |
| Class D | Reserved for multicast |
| Class E | Reserved for research/experimentation |
| Loopback address | `127.0.0.1` (and the whole `127.0.0.0/8` range) — used to test a device's own network stack |
| Network Address | All host bits = 0; represents the network itself, unusable as a host address |
| Broadcast Address | All host bits = 1; sends data to every host on the network, unusable as a host address |
| Usable hosts formula | 2ʰ − 2, where h = number of host bits |

---

## 10. Review Questions (for self-testing / Anki)

| Question | Answer |
|----------|--------|
| What type of address does Layer 3 use, as opposed to Layer 2's MAC address? | A logical address — the IP address |
| What Layer 3 device connects different LANs and performs path selection? | The router |
| Do broadcast frames cross a router? | No — a router blocks broadcasts from leaving the local network |
| How many bits make up an IPv4 address? | 32 bits |
| How many bits make up one octet? | 8 bits |
| What is the decimal range of a single octet? | 0 to 255 |
| What are the 8 positional weights in one octet, from left to right? | 128, 64, 32, 16, 8, 4, 2, 1 |
| What does a /24 prefix mean? | The first 24 bits (first 3 octets) are the network portion; the last 8 bits (last octet) are the host portion |
| What is the subnet mask for a /24 network? | 255.255.255.0 |
| What is the subnet mask for a /16 network? | 255.255.0.0 |
| What is the subnet mask for a /8 network? | 255.0.0.0 |
| What is the first-octet decimal range for Class A? | 0–127 |
| What is the first-octet decimal range for Class B? | 128–191 |
| What is the first-octet decimal range for Class C? | 192–223 |
| What is Class D reserved for? | Multicast |
| What is Class E reserved for? | Research and experimentation |
| What special range, though numerically in Class A, cannot be used for regular hosts? | 127.0.0.0/8 (the loopback range, e.g., 127.0.0.1) |
| What is the purpose of the loopback address? | To let a device test its own network stack, without sending traffic onto the physical network |
| What is the Network Address of a network? | The address with all host-portion bits set to 0 |
| What is the Broadcast Address of a network? | The address with all host-portion bits set to 1 |
| Can the Network Address or Broadcast Address be assigned to a host? | No — neither can ever be assigned to an individual device |
| How many usable host addresses are in a /24 network? | 254 (256 total − 2 reserved addresses) |
| What is the general formula for usable host addresses? | 2ʰ − 2, where h is the number of host bits |

---

## My Study Log

- [x] Watched "IPv4 Addressing (Part 1)" video (Jeremy's IT Lab)
- [x] Had Gemini summarize the video content (Korean)
- [x] Had this summary translated, expanded, and gap-filled in English
- [ ] Reviewed Day 07 Anki flashcards
- [ ] Practiced binary ↔ decimal conversion drills
- [ ] Packet Tracer lab for IPv4 addressing (if available)

### Notes / Confusing Points

- (add your own notes here)
