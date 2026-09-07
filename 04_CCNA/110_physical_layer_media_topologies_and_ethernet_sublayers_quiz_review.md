# Physical Layer, Media, Topologies, and Ethernet Sublayers — Quiz Review

Quiz review for questions 11–17. Topics: physical layer terminology (bandwidth / throughput / goodput / latency), bottleneck throughput, fiber-optic cabling, media types, data link sublayers (LLC / MAC), CSMA/CD vs CSMA/CA, and LAN topologies.

---

## 1. Physical Layer Terminology (Q11)

**Question:** Which OSI physical layer term describes the measure of the transfer of bits across a medium over a given period of time?
**Answer:** `throughput`

The physical layer (Layer 1) PDU is the **bit**. Four terms describe the quantity or speed of bits.

| Term | Meaning | Unit | Road analogy |
|---|---|---|---|
| **Bandwidth** | Theoretical **capacity** — the maximum amount of data a link can carry per second | bps | Number of lanes on the road |
| **Throughput** | The amount of data that **actually** got through in a given time. Always ≤ bandwidth because of congestion, errors, overhead | bps | Number of cars that actually passed |
| **Goodput** | Throughput minus protocol overhead (headers, ACKs, retransmissions) — pure application data | bps | Count only the passengers, not the luggage |
| **Latency** | Time for a bit to travel from source to destination | **ms** | Time for one car to drive from A to B |

**How to remember**
- Size order: `bandwidth ≥ throughput ≥ goodput`
- Only latency is measured in **time (ms)**. The other three are **amounts (bps)**.
- Keyword "measure of the transfer" → throughput. Keyword "capacity" → bandwidth. Keyword "delay" or "time" → latency.
- `through`put = what got *through*. `good`put = the *useful* part. `band`width = the *width* of the road.

---

## 2. Maximum Possible Throughput / Bottleneck (Q12)

**Question:** PC —10 Mb/s— switch —100 Mb/s— router —128 kb/s— router —100 Mb/s— switch —1000 Mb/s— server. What is the maximum possible throughput between the PC and the server?
**Answer:** `128 kb/s`

**Key idea: the bottleneck**
Data must pass through every link on the path, so end-to-end throughput is **limited by the slowest link**. The word "maximum" is a trap — it means the *upper limit* that is possible, and that upper limit is set by the bottleneck. No matter how wide the rest of the road is, you cannot go faster than the narrowest tunnel allows.

**Rule:** "end-to-end throughput" or "maximum possible throughput between A and B" → **find the minimum value on the path**.

**Unit check before comparing**
- 1,000 kb = 1 Mb, 1,000 Mb = 1 Gb
- 128 kb/s = 0.128 Mb/s, which is far smaller than 10 Mb/s even though "128" looks bigger
- Lowercase **b = bit**, uppercase **B = byte**. 1 byte = 8 bits. Network speeds are in bits (bps); file sizes are in bytes.

**Tip:** A lightning-bolt-shaped line in an exhibit represents a **WAN** (serial / long-distance) link. In exam questions it is almost always the bottleneck.

---

## 3. Fiber-Optic Cabling (Q13)

**Question:** Which two statements describe the characteristics of fiber-optic cabling? (Choose two.)
**Answer:**
- Fiber-optic cabling is primarily used as **backbone** cabling.
- Fiber-optic cabling does **not conduct electricity**.

**Core concept:** Copper sends signals as **electricity**; fiber sends signals as **light** through a glass (or plastic) strand. Every characteristic follows from that.

**Why the answers are correct**
- Made of glass → does not conduct electricity → immune to **EMI**, lightning, and grounding problems.
- Very low signal loss → can run several **kilometers** without a repeater (copper is limited to 100 m).
- But it is expensive, fragile, and needs special tools to terminate connectors → not run to every desktop. Used for the **backbone** (between buildings, between floors, data center links). Desktop runs ("the ribs") use cheap copper UTP.

**Why the other options are wrong**
- "LEDs for single-mode, laser for multimode" → **backwards**. Single-mode = laser, multimode = LED.
- "High signal loss" → opposite. Fiber has very **low** loss.
- "Multimode carries signals from multiple sending devices" → wordplay trap. "Mode" refers to the number of **light paths**, not the number of devices.

**Single-mode vs multimode**

| | Single-mode | Multimode |
|---|---|---|
| Core diameter | 9 μm (very thin) | 50 / 62.5 μm (thicker) |
| Light source | **Laser** | **LED** |
| Light path | One straight path | Many paths, bouncing off the core wall |
| Distance | Tens of km | A few hundred meters |
| Analogy | A thin hose with one iron ball exactly the size of the hose — it goes straight | A wider hose with a hundred rubber balls thrown in — they bounce around |

Why multimode is short-range: bouncing light travels a longer path than straight light, so parts of the signal arrive at different times and the signal gets smeared (**modal dispersion**). The farther it travels, the worse it gets.

**Memory aid:** A laser pointer hits one precise point → suits a thin core (single). An LED spreads light → suits a thick core (multi). For scale, a human hair is about 70 μm — even a multimode core is thinner than a hair, and about eight single-mode cores equal one hair.

μm = micrometer (micron) = 1/1000 mm.

---

## 4. Media Types Matching (Q14)

**Question:** Match the description with the media.

| Description | Media | Why |
|---|---|---|
| Provides the most mobility options | **Wireless** | No cable, so you can carry the device around freely |
| Traditionally used for television; now connects the customer location to the wiring of the customer premises | **Coaxial** | The TV antenna cable — a copper core in the center surrounded by insulation and a shield (same axis = co-axial). Cable TV companies deliver internet over it (cable modem). Keyword: **television** |
| Used for high transmission speed and long distances | **Optical fiber** | Sends light → fast, very low loss → kilometers. Keywords: **speed + distance** |
| Copper media used in industrial environments with a lot of interference | **STP** | **S**hielded **T**wisted **P**air. Keywords: **copper** (rules out fiber) + **interference** (needs shielding) |

**UTP vs STP**
- Twisting the wire pairs already cancels most external noise — that is the baseline defense in both UTP and STP.
- STP adds a foil/braided **shield** on top — extra armor for factories with motors and heavy electrical equipment.
- **UTP** (Unshielded) is the common office LAN cable: cheap and easy to install.

**Keyword summary**
- mobility → wireless (radio waves)
- TV / cable → coaxial (electricity)
- office, cheap, most common → UTP (electricity)
- interference, industrial, shield → STP (electricity)
- speed, distance, backbone → optical fiber (light)

---

## 5. Data Link Sublayers (Q15)

**Question:** Which two acronyms represent the data link sublayers that Ethernet relies upon to operate? (Choose two.)
**Answer:** `LLC` and `MAC`

**What is a sublayer?**
A layer inside a layer. In the OSI model, only Layer 2 (data link) is split into two parts — like a seven-story building where only the second floor is a split-level.

```
Layer 3  Network (IP)
------------------------
   LLC   ← upper half: talks to Layer 3
------------------------
   MAC   ← lower half: talks to Layer 1
------------------------
Layer 1  Physical (cable / wireless)
```

**LLC — Logical Link Control (upper)**
- Identifies which Layer 3 protocol (IP, etc.) the data belongs to and passes it down to MAC.
- Does the same job regardless of the medium (cable or wireless) → independent of physical stuff → "logical".

**MAC — Media Access Control (lower)**
- Controls how and when to access the actual medium, attaches MAC addresses, builds the frame, checks for errors (FCS).
- Behaves differently per medium: wired Ethernet uses **CSMA/CD**, Wi-Fi uses **CSMA/CA**.

**Memory aid:** The MAC address is burned into the NIC hardware → MAC is closer to the physical layer → MAC is on the bottom, LLC on top. Alphabetical order L → M also goes top → bottom.

**Why the other options are wrong**
SFD (Start Frame Delimiter), FCS (Frame Check Sequence), and CSMA (Carrier Sense Multiple Access) all belong to the data link layer, but they are **fields in the frame or access methods**, not sublayers.

---

## 6. Why CSMA/CD Is No Longer Necessary (Q16)

**Question:** Although CSMA/CD is still a feature of Ethernet, why is it no longer necessary?
**Answer:** The use of **full-duplex capable Layer 2 switches**

**CSMA/CD explained**
- **CS** — Carrier Sense: listen before you talk; make sure the line is quiet.
- **MA** — Multiple Access: many devices share one medium.
- **CD** — Collision Detection: if two devices talk at once, detect the collision, wait a random time, and resend.

**Why it was needed (the old days)**
Old LANs used a single coaxial bus cable, or a **hub**. A hub simply broadcasts every incoming signal out of every port, so all PCs effectively share one lane. This is **half-duplex**, like a **walkie-talkie**: only one device can talk at a time, and collisions happen. A collision-handling rule was mandatory.

**Why it is not needed now**
Modern LANs use **switches**. A switch gives each port its own dedicated path, and each link runs **full-duplex** — one pair of wires for sending, another for receiving. Devices can talk and listen at the same time, like a **phone call**. Collisions cannot happen, so the collision-detection rule never triggers. The feature still exists in the standard but is never used.

**Summary**
- hub + half-duplex = walkie-talkie = collisions → CSMA/CD needed
- switch + full-duplex = phone call = no collisions → CSMA/CD unnecessary

**Why the other options are wrong**
- IPv6 addresses → Layer 3, unrelated to Layer 2 collisions.
- CSMA/CA → that is **Wi-Fi**. Wireless cannot detect collisions in the air, so it **avoids** them in advance. Wired Ethernet did not switch to CA; it eliminated collisions entirely. Similar-looking name = bait.
- Half-duplex switch operation → backwards; half-duplex is exactly the situation that *needs* CSMA/CD.
- Gigabit speeds → faster does not mean collision-free.

---

## 7. Hybrid Topology for a LAN (Q17)

**Question:** A network team is comparing topologies for connecting on a shared media. Which physical topology is an example of a hybrid topology for a LAN?
**Answer:** `extended star`

**Hybrid** = a combination of two or more basic topologies.

| Topology | Shape | Notes |
|---|---|---|
| **Bus** | All devices hang off one shared cable | Old coaxial LANs. One break kills the whole segment. Basic type. |
| **Ring** | Each device connects to the next, forming a loop | Token Ring era. Basic type. |
| **Star** | One switch in the middle, every device connected to it | The default for almost every modern LAN. Basic type. |
| **Extended star** | Several stars connected together — a central switch, a switch on each floor, then desktops | **Hybrid** — the everyday corporate network. Fiber backbone + copper "ribs". |
| **Partial mesh** | Some devices have multiple redundant connections | Mainly a **WAN** topology, and a basic type — not a LAN hybrid. |

**Two filters for this question**
1. Is it a **LAN** topology? → rules out partial mesh (WAN).
2. Is it a **combination** of basic types? → rules out bus, ring, star.

Only extended star passes both. Keyword "hybrid topology for a LAN" → **extended star**.

---

## Quick Recall Sheet

- measure of transfer of bits over time → **throughput**; capacity → **bandwidth**; time → **latency**
- max throughput between A and B → **smallest link on the path** (check units first; b ≠ B)
- fiber → light, no electricity, low loss, long distance, expensive → **backbone**
- single-mode = laser, thin core, tens of km; multimode = LED, thick core, hundreds of m
- mobility → wireless; TV → coaxial; interference → STP; speed + distance → fiber
- data link sublayers → **LLC (top) + MAC (bottom)**
- CSMA/CD unnecessary because → **full-duplex switches**; CSMA/CA = Wi-Fi
- hybrid LAN topology → **extended star**

## English Phrases Practiced While Explaining

- similar **to** / related **to** / connected **to** (not "with")
- less than or equal **to**
- measured **in** milliseconds / bps
- limited **by** the bottleneck, determined **by** the slowest link
- **a few** kilometers (not "few" — that means almost none)
- bounce **off** the wall, made **of** glass, **at** a time, **at** the same time
- matching question, dedicated path, receive (not accept), access (not approach), uses (not checks)
