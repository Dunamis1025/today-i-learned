# Day 05: Ethernet LAN Switching (Part 1)

> Detailed English summary of Jeremy's IT Lab CCNA 200-301 video **"Free CCNA | Ethernet LAN Switching (Part 1)"** — based on the user's Gemini-generated Korean notes, expanded and translated with additional explanations to fill in gaps. Video: http://www.youtube.com/watch?v=u2n762WG0Vo

---

## 1. OSI Model Recap (Layers 1 and 2)

Before diving into switching, the video reviews the two OSI layers that Ethernet LAN switching depends on.

### Layer 1 — Physical Layer

- Defines the **physical characteristics of the transmission medium**: voltage levels, maximum cable distance (e.g., the 100 m limit for UTP copper cable, covered in Day 02), physical connectors, and cabling specifications.
- Its job is to **convert digital bits into signals**: electrical signals over copper, or radio signals over wireless.
- It does not understand "frames," "addresses," or "meaning" — it only cares about getting raw bits from one point to another over physical media.

### Layer 2 — Data Link Layer

- Provides **node-to-node connectivity and data delivery** between two directly connected devices — for example, a PC and a switch, or a switch and a router.
- Takes data from the layers above and **formats it into frames** so it can be transmitted over the physical medium, and **detects (and in some cases corrects) errors** introduced by Layer 1 transmission.
- Uses **Layer 2 addresses, i.e. MAC addresses** — completely separate from the **Layer 3 (IP) addresses** used by routers.
- **Switches operate at Layer 2.** This is the key fact that sets up the rest of the video: a switch makes forwarding decisions based on MAC addresses, not IP addresses.

> **Added clarification:** the reason this distinction matters is that a switch never looks inside the IP packet to decide where to send a frame — it only reads the Layer 2 header (source/destination MAC). This is different from a router, which strips off the Layer 2 header and makes its decision based on the Layer 3 (IP) header instead.

### What is a LAN (Local Area Network)?

- A network contained within a relatively small, localized area — e.g., a single office floor or a home network.
- **A switch does not separate/segment a LAN.** Adding more switches simply **extends** the same LAN (all ports on all interconnected switches belong to the same broadcast domain/LAN).
- **A router, by contrast, interconnects different LANs** — it is the device that creates the *boundary* between one LAN and another.

> **Added clarification:** this is a classic CCNA exam distinction. "Switches connect devices within one LAN; routers connect different LANs together." A common way to remember it: switches = Layer 2 = same network, stay local; routers = Layer 3 = different networks, cross boundaries.

### Data Encapsulation Process

As data moves down the OSI stack for transmission, each layer wraps ("encapsulates") the data from the layer above it with its own header (and, at Layer 2, a trailer too):

```
Data (Application/Layer 5-7)
   ↓  + Layer 4 header (TCP/UDP)
Segment
   ↓  + Layer 3 header (IP)
Packet
   ↓  + Layer 2 header AND trailer
Frame
   ↓  converted to bits by Layer 1
Bits (electrical/radio signal)
```

> **Added clarification:** this is why the Ethernet frame (discussed next) has both a **header** *and* a **trailer** — it's the only layer in this chain that adds a trailer, and that trailer (FCS) is what makes error-checking possible.

---

## 2. Ethernet Frame Structure

An Ethernet frame consists of a **header** (5 fields) and a **trailer** (1 field). Below is each field, its size, and its purpose.

### ① Ethernet Header Fields (5 fields)

| # | Field | Size | Content / Purpose |
|---|-------|------|---------------------|
| 1 | **Preamble** | 7 bytes (56 bits) | Alternating pattern of `10101010`, repeated 7 times (i.e., the 1-byte pattern `10101010` repeated across 7 bytes = 56 bits total). Purpose: lets the **receiving device synchronize its receive clock** so it's ready to correctly read the incoming frame. *(See Day 05 follow-up Q&A: `10101010` by itself is 1 byte/8 bits; "7 bytes of `10101010`" means that 1-byte pattern repeated 7 times.)* |
| 2 | **SFD (Start Frame Delimiter)** | 1 byte (8 bits) | Pattern `10101011` — identical to the preamble pattern except the **final bit is `1` instead of `0`**. Purpose: signals "the preamble has ended — the actual frame is starting now." |
| 3 | **Destination MAC Address** | 6 bytes (48 bits) | The physical (Layer 2) address of the device that should **receive** this frame. |
| 4 | **Source MAC Address** | 6 bytes (48 bits) | The physical (Layer 2) address of the device that is **sending** this frame. |
| 5 | **Type / Length** | 2 bytes (16 bits) | Dual-purpose field (see Day 05 follow-up Q&A for the full explanation): a value **≤ 1500** means this field represents the **Length** of the encapsulated packet in bytes; a value **≥ 1536** means this field represents the **Type** of protocol encapsulated inside — e.g., hex `0x0800` = IPv4, hex `0x86DD` = IPv6. |

> **Added clarification on field order:** the actual byte order on the wire is Preamble → SFD → Destination MAC → Source MAC → Type/Length → Data (payload) → FCS. The "Data" field itself (the encapsulated Layer 3 packet) sits between the Type/Length field and the FCS trailer, though the Korean notes didn't list it as a separate numbered field — it's implicitly the payload being described by the Type/Length field.

### ② Ethernet Trailer Field (1 field)

| Field | Size | Content / Purpose |
|-------|------|---------------------|
| **FCS (Frame Check Sequence)** | 4 bytes (32 bits) | Used by the **receiving device** to run a **CRC (Cyclic Redundancy Check)** algorithm and detect whether the frame's data was **corrupted/damaged during transmission**. |

> **Added clarification — how CRC/FCS actually works (not covered in the notes but useful context):** the sending device runs a mathematical calculation over the frame's contents and puts the result into the FCS field. The receiving device performs the *same* calculation on the frame it received and compares its result to the FCS value that arrived with the frame. If the two don't match, the frame is considered corrupted and is **silently discarded** — Ethernet's FCS only *detects* errors, it does **not correct** them or ask for retransmission (that job, if needed, is handled by upper layers like TCP).

### Minimum and Maximum Ethernet Frame Size (gap-fill — commonly tested, not explicitly in the notes)

- **Minimum frame size: 64 bytes** (not counting the Preamble/SFD). A frame smaller than this is called a **"runt"** and is discarded.
- **Maximum frame size: 1518 bytes** (standard Ethernet, not counting Preamble/SFD) — anything larger is called a **"giant"** and is also discarded, unless jumbo frames are explicitly configured on the network.
- This ties directly back to the Type/Length field: since a normal frame's payload tops out around 1500 bytes, any Type/Length value up to 1500 can safely be interpreted as a *length*, and Cisco/IEEE reserved 1536+ to mean *type* instead, leaving a small unused gap (1501–1535) in between.

---

## 3. Understanding MAC Addresses (Media Access Control Address)

### Key Characteristics

- A **6-byte (48-bit)** address that is **permanently assigned to a device's network interface card (NIC) at the time of manufacturing** — this is why it's also called a **BIA (Burned-In Address)**.
- Different from an **IP address**, which is manually (or dynamically via DHCP) configured through the CLI/OS — a MAC address is baked into the hardware.
- **Globally unique** — no two network interfaces in the world are (supposed to be) assigned the same MAC address.

### Structure: OUI + Device ID

A MAC address is written as **12 hexadecimal digits** (48 bits ÷ 4 bits per hex digit = 12 digits), commonly displayed like `00:1A:2B:3C:4D:5E` or `001A.2B3C.4D5E` (Cisco's dotted format).

| Part | Size | Meaning |
|------|------|---------|
| **OUI (Organizationally Unique Identifier)** | First 3 bytes (24 bits) | Identifies the **manufacturer** of the device (e.g., Cisco has its own registered OUI block, assigned by the IEEE). |
| **Device ID** | Last 3 bytes (24 bits) | A number **uniquely assigned by that manufacturer** to each individual device it produces, ensuring no two devices from the same vendor share a MAC address. |

> **Added clarification:** the IEEE is the organization that hands out OUI blocks to manufacturers, which is what guarantees global uniqueness — as long as each vendor doesn't reuse device IDs, no two MAC addresses in the world should ever collide (in practice, extremely rare exceptions exist but are irrelevant for CCNA purposes).

### Quick Refresher: Hexadecimal (Base-16)

- Hex uses 16 symbols: `0–9`, then `A(10) B(11) C(12) D(13) E(14) F(15)`.
- Each hex digit represents exactly **4 bits**, which is why a 48-bit MAC address is neatly represented by **12 hex digits** (48 ÷ 4 = 12).

> **Added clarification (why hex, not decimal or binary, for MAC addresses):** binary would make a MAC address 48 characters long (unreadable); decimal doesn't map cleanly onto binary groupings. Hex is the sweet spot — compact, and each digit maps perfectly onto a 4-bit "nibble," making it easy for humans and easy for computers to convert.

---

## 4. How a Switch Operates: MAC Address Learning and Frame Forwarding

A switch relies on a **MAC Address Table** (also called a **CAM table** — Content Addressable Memory table — a term you'll see in other Cisco material) to decide how to handle frames. Here are the core mechanisms:

### Dynamic Learning

- When a switch receives a frame on any port, it looks at the **Source MAC Address** field and **records/maps that MAC address to the port (interface) it arrived on**, building the MAC address table dynamically — with no manual configuration needed.
- **Aging note:** on Cisco switches, a dynamically learned MAC address entry is **automatically removed after 5 minutes (300 seconds) of no traffic activity** from that address (this is the default MAC address aging timer, and it is configurable).

> **Added clarification — why learning uses the *source* MAC, not the destination:** the switch has no way of "seeing" where a device is unless that device actually transmits something. By watching the *source* address of every incoming frame, the switch learns "this MAC address lives behind this port" purely by observation — it never has to be told directly.

### Unicast Frames

A **unicast frame** is one addressed to a **single specific destination** (as opposed to broadcast or multicast — see the note below).

| Type | Condition | Switch Behavior |
|------|-----------|-------------------|
| **Known unicast** | Destination MAC address **is already in** the switch's MAC address table | The switch forwards the frame **only out the specific port** associated with that MAC address — an efficient, targeted delivery. |
| **Unknown unicast** | Destination MAC address is **NOT in** the switch's MAC address table | The switch **floods** the frame — copies and sends it out **every port except the one it arrived on**. This is called **flooding**. |

> **Added clarification (gap-fill):** the notes cover known/unknown unicast and flooding, but don't mention two related frame types that are important for CCNA and often tested alongside this topic:
> - **Broadcast frame**: destination MAC = `FF:FF:FF:FF:FF:FF`. A switch **always** floods broadcast frames out every port except the one it arrived on (regardless of whether the destination is "known" — because a broadcast, by definition, is meant for everyone).
> - **Multicast frame**: destination MAC is a special multicast address representing a *group* of devices. By default, an unconfigured switch treats unknown multicast somewhat like unknown unicast (floods it), though multicast handling can be optimized with features like IGMP snooping (a more advanced topic, likely covered later in the ENSA portion of CCNA).
>
> **Why flooding matters conceptually:** flooding is *necessary* — the switch would rather over-deliver a frame to ports that don't need it than risk under-delivering and having the frame never reach its real destination. Once the destination device responds (its own frames flow back through the switch), the switch learns that device's MAC-to-port mapping from the *source* address of that reply, and future frames to it become "known unicast" (targeted, not flooded).

---

## 5. Summary of Key Review Quiz Answers (from the video)

| Question | Answer |
|----------|--------|
| Which Ethernet header field synchronizes the receive clock? | **Preamble** |
| Length of a device's physical (MAC) address? | **48 bits (6 bytes)** |
| Name for the first half of a MAC address (identifies the manufacturer)? | **OUI (Organizationally Unique Identifier)** |
| Which field does a switch reference to populate its MAC address table? | **Source MAC Address** |
| What does a switch do when it doesn't know the destination MAC address? | **Flooding** (treats it as an unknown unicast and sends out all ports except the incoming one) |

---

## 6. Quick Summary

- Layer 1 handles raw bit transmission over physical media; Layer 2 handles node-to-node frame delivery using MAC addresses. Switches operate at Layer 2.
- A switch extends a LAN; a router interconnects separate LANs.
- Data encapsulation: Data → Segment (L4 header) → Packet (L3 header) → Frame (L2 header + trailer) → Bits.
- The Ethernet frame has 5 header fields (Preamble, SFD, Destination MAC, Source MAC, Type/Length) and 1 trailer field (FCS).
- A MAC address is a globally unique, burned-in 48-bit address made of a 24-bit OUI (manufacturer) + 24-bit device ID, written in 12 hex digits.
- Switches build their MAC address table dynamically by reading the **source MAC** of incoming frames; entries expire after 5 minutes of inactivity by default.
- Known unicast → forwarded out one specific port. Unknown unicast → flooded out all ports except the incoming one. (Broadcast is always flooded; multicast is flooded by default unless optimized.)

---

## 7. Command / Concept Cheat Sheet

| Term | Meaning |
|------|---------|
| Preamble | 7-byte `10101010` pattern (repeated), synchronizes receive clock |
| SFD | 1-byte `10101011`, marks start of actual frame |
| Destination/Source MAC | 6-byte physical addresses of receiver/sender |
| Type/Length | 2-byte field; ≤1500 = length, ≥1536 = protocol type (e.g., 0x0800 = IPv4) |
| FCS | 4-byte trailer; CRC-based error detection |
| OUI | First 24 bits of a MAC address; identifies manufacturer |
| BIA | Burned-In Address — another name for a MAC address, since it's fixed in hardware |
| MAC Address Table / CAM Table | Switch's dynamic table mapping MAC addresses to ports |
| Known unicast | Destination MAC found in table → forwarded to one port only |
| Unknown unicast | Destination MAC not in table → flooded to all ports (except source) |
| Flooding | Sending a frame out every port except the one it arrived on |
| Aging timer | Default 5 minutes; dynamic MAC entries are removed if idle that long |

---

## 8. Review Questions (for self-testing / Anki)

| Question | Answer |
|----------|--------|
| At which OSI layer does a switch operate? | Layer 2 (Data Link) |
| Does a switch separate a LAN into multiple LANs? | No — it extends/expands the same LAN. Routers separate LANs. |
| What are the 5 fields in the Ethernet header? | Preamble, SFD, Destination MAC, Source MAC, Type/Length |
| What is the 1 field in the Ethernet trailer? | FCS (Frame Check Sequence) |
| How big is the Preamble, and what's its purpose? | 7 bytes; synchronizes the receiver's clock |
| How is the SFD different from the Preamble pattern? | Same alternating pattern, but the last bit is 1 instead of 0 (`10101011`) |
| What does the FCS field use to detect transmission errors? | CRC (Cyclic Redundancy Check) |
| What is another name for a MAC address, referring to how it's assigned? | BIA (Burned-In Address) |
| How many bits/bytes make up a MAC address? | 48 bits / 6 bytes |
| What does OUI stand for and what does it identify? | Organizationally Unique Identifier; identifies the manufacturer |
| Which MAC address field does a switch use to build its MAC address table? | Source MAC Address |
| How long before an inactive dynamic MAC entry is removed by default? | 5 minutes |
| What happens when a switch receives a frame for a known unicast destination? | Forwards it out only the port associated with that MAC address |
| What happens when a switch receives a frame for an unknown unicast destination? | Floods it out all ports except the one it arrived on |
| Is a broadcast frame ever sent to just one port? | No — broadcasts are always flooded to all ports except the source port |

---

## My Study Log

- [x] Watched "Ethernet LAN Switching (Part 1)" video (Jeremy's IT Lab)
- [x] Had Gemini summarize the video content (Korean)
- [x] Had this summary translated, expanded, and gap-filled in English
- [ ] Reviewed Day 05 Anki flashcards
- [ ] Packet Tracer lab for this topic (if available)

### Notes / Confusing Points

- (add your own notes here)
