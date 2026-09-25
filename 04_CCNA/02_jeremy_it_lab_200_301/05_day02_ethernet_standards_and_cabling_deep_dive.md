# Day 02 (continued): Ethernet Standards & Cabling — Anki Deep Dive

> This note is a supplementary deep dive built while reviewing Anki flashcards for **Day 02 (Interfaces and Cables)**. It covers the IEEE 802.3 standard family, twisted-pair vs fiber cabling, pinouts, cable types, and related concepts that came up while drilling cards.

---

## 1. IEEE 802.3 Ethernet Standards — Full Timeline

Each IEEE 802.3 standard defines a specific combination of **speed + cable medium**. The suffix letter(s) after "802.3" are assigned roughly in the order the standard was ratified — they don't follow a strict logical pattern, so this table also includes memory hooks.

| Year | Standard | Speed | Nickname | Cable Medium | Cable Name | Pairs Used / Distance |
|------|----------|-------|----------|---------------|------------|------------------------|
| 1983 | 802.3 (original) | 10 Mbps | Ethernet | Coaxial | 10BASE5 | N/A (single conductor) |
| 1990 | 802.3**i** | 10 Mbps | Ethernet | UTP (copper) | 10BASE-**T** | 2 pairs (4 wires) |
| 1995 | 802.3**u** | 100 Mbps | **Fast** Ethernet | UTP (copper) | 100BASE-**TX** | 2 pairs (4 wires) |
| 1998 | 802.3**z** | 1000 Mbps | **Gigabit** Ethernet | Fiber | 1000BASE-**X** | N/A (fiber, no copper pairs) |
| 1999 | 802.3**ab** | 1000 Mbps | **Gigabit** Ethernet | UTP (copper) | 1000BASE-**T** | 4 pairs (8 wires) — first standard to use all 4 pairs |
| 2002 | 802.3**ae** | 10 Gbps | **10 Gigabit** Ethernet | Fiber | 10GBASE-SR/LR/ER | N/A (fiber) |
| 2006 | 802.3**an** | 10 Gbps | **10 Gigabit** Ethernet | UTP (copper) | 10GBASE-**T** | 4 pairs (8 wires) |

### Key rules that unlock most of this table

1. **"BASE-T" in the name = always copper (UTP)**. This applies consistently: 10BASE-T, 1000BASE-T, 10GBASE-T are all copper standards, matched with 802.3i, 802.3ab, 802.3an respectively.
2. **Nicknames are based on speed, not on the letter suffix.** 802.3z (fiber) and 802.3ab (copper) are both "Gigabit Ethernet" because they're both 1000 Mbps — even though the cable medium differs. Same logic applies to 802.3ae and 802.3an, both "10 Gigabit Ethernet."
3. **Pair usage jumps at Gigabit speed.** 10 Mbps and 100 Mbps standards use only 2 pairs (4 wires) — one pair to transmit, one to receive. Starting at 1000BASE-T (1999), all 4 pairs (8 wires) are used simultaneously to support the higher throughput.
4. **Suffix drift from T → TX → X** traces the shift from copper to fiber: 10BASE-**T** (pure copper) → 100BASE-**TX** (still copper, but signal encoding shifts toward the "X" naming) → 1000BASE-**X** (fully fiber).

---

## 2. Fiber Distance Standards (802.3ae family, 10 Gigabit)

| Standard | Distance | Fiber Type |
|----------|----------|------------|
| 10GBASE-**SR** (Short Range) | ~300 m | Multi-mode fiber |
| 10GBASE-**LR** (Long Range) | **10 km** | Single-mode fiber |
| 10GBASE-**ER** (Extended Range) | 40 km | Single-mode fiber |

**Memory trick:** the "10" in "10GBASE-LR" matches the "10 km" answer directly. For ER, add 30 km to LR's 10 km to get 40 km.

**S → L → E = Short → Long → Extended**, distance increasing in that order.

---

## 3. Single-mode vs. Multi-mode Fiber

| Feature | Single-mode (SMF) | Multi-mode (MMF) |
|---------|--------------------|--------------------|
| Core diameter | Thin (~9 μm) | Thick (~50–62.5 μm) |
| Light path | One straight path | Multiple bouncing paths (modal dispersion) |
| Max distance | Long (km range) | Shorter (hundreds of meters) |
| Light source | Laser | LED or low-cost laser |
| Cost | Higher | Lower |
| Jacket color (common) | Yellow | Orange / aqua |

**Why the distance difference:** in multi-mode fiber, light bounces at different angles and arrives at slightly different times (modal dispersion), which blurs the signal over distance. In single-mode fiber, the core is narrow enough that light travels in essentially one path, so the signal stays clear over much longer distances.

**Connecting back to 10GBASE naming:** SR (short) = multi-mode, LR/ER (long) = single-mode.

**μm** is read as "micrometer" (10⁻⁶ meter, i.e., one-millionth of a meter). 1 m = 1,000 mm = 1,000,000 μm.

---

## 4. Baseband vs. Broadband

| Type | Description | Analogy |
|------|--------------|---------|
| **Baseband** | The entire bandwidth of the medium carries **one signal at a time** | A single-lane road — one car at a time |
| **Broadband** | Bandwidth is split into multiple frequencies to carry **multiple signals simultaneously** | A multi-lane road — many cars at once |

Ethernet is Baseband — that's why every Ethernet standard name includes "BASE" (10BASE-T, 100BASE-TX, etc.). Cable TV is a classic example of Broadband.

---

## 5. TX / RX Naming Convention

- **TX = Transmit** (the "X" is a long-standing engineering convention for abbreviating "trans-")
- **RX = Receive** (paired with TX for symmetry)

These labels mark which wire pair sends data and which receives it. Common on cable ports, connectors, and radio equipment.

---

## 6. How Many Pairs Does Each Standard Use?

| Standard | Speed | Pairs Used |
|----------|-------|-------------|
| 10BASE-T | 10 Mbps | 2 pairs (4 wires) — 1 pair TX, 1 pair RX |
| 100BASE-TX | 100 Mbps | 2 pairs (4 wires) |
| 1000BASE-T | 1000 Mbps | **4 pairs (8 wires)** — all pairs used starting here |
| 10GBASE-T | 10 Gbps | 4 pairs (8 wires) |

A standard UTP cable (Cat5e, Cat6, etc.) always physically contains 4 pairs (8 wires) — but slower standards (10/100 Mbps) only use half of them. The unused 2 pairs simply sit idle.

---

## 7. FastEthernet (100BASE-TX) Pinout

| Pin | Function |
|-----|----------|
| 1 | TX+ (Transmit) |
| 2 | TX− (Transmit) |
| 3 | RX+ (Receive) |
| 4 | Unused (until Gigabit) |
| 5 | Unused (until Gigabit) |
| 6 | RX− (Receive) |
| 7 | Unused (until Gigabit) |
| 8 | Unused (until Gigabit) |

- On a standard end device (PC, firewall, etc.): **pins 1, 2 = Transmit**, **pins 3, 6 = Receive**.
- On a switch/hub: the roles are reversed (pins 1, 2 = Receive, pins 3, 6 = Transmit) — this is what makes straight-through cabling work between a PC and a switch (see Section 9).

---

## 8. SFP (Small Form-Factor Pluggable) Transceivers

**Question:** Fiber-optic cables are connected to _____ transceivers in a router or switch.
**Answer:** SFP

- **Small Form-Factor** = physically small module
- **Pluggable** = can be inserted/removed without replacing the whole device

**Why they exist:** rather than building a switch/router with fixed port types, manufacturers leave an empty slot and let the network admin plug in the appropriate SFP module for whatever cable type is needed (fiber, or other media). Similar concept to a laptop's USB-C port accepting different adapters (HDMI, Ethernet, etc.) — the port itself is generic; the module determines what it connects to.

**Connection chain:**
```
[Fiber cable] --- [SFP module] --- (plugged into) --- [Switch/router port]
```

**Common variants:** SFP (~1 Gbps), SFP+ (~10 Gbps), QSFP (40 Gbps+).

---

## 9. Signal Leakage: Why UTP (not Coax) Is the Answer

**Question:** _____ cables emit a faint signal outside of the cable, which can be detected and copied.
**Answer:** UTP

This distinguishes two different problems that twisting solves — and one it doesn't:

| Problem | Does twisting UTP wires prevent it? |
|---------|--------------------------------------|
| **Interference** (external EM noise entering the cable) | ✅ Yes — this is the whole point of twisting |
| **Crosstalk** (pairs inside the cable interfering with each other) | ✅ Yes |
| **Signal leakage / emanation** (signal escaping outward, enabling eavesdropping) | ❌ No |

Twisting cancels out *incoming* interference, but it can't stop the faint electromagnetic field naturally generated by electrical current from radiating slightly outside the cable — that's basic physics, unaffected by the twist.

**Why coax isn't the answer:** coaxial cable has a built-in metal shielding layer that wraps around the signal conductor, blocking both incoming interference *and* outgoing signal leakage.

| Cable Type | Shielding | Vulnerable to Signal Leakage? |
|------------|-----------|-------------------------------|
| UTP (Unshielded Twisted Pair) | None | ✅ Yes (correct answer) |
| STP (Shielded Twisted Pair) | Twisting + metal shield | ❌ No |
| Coax | Shielded by design | ❌ No |

---

## 10. Why Did Networks Move from Coax to UTP?

A common misconception: "Coax has only one conductor, so it's slower — that's why UTP replaced it." This is **not accurate**. Early UTP (10BASE-T) was still only 10 Mbps — identical to coax (10BASE5). Speed was not the driver of the switch.

**The real reasons:**

| Factor | Coax | UTP |
|--------|------|-----|
| Flexibility | Thick, rigid, hard to route | Thin, flexible, easy to install |
| Topology | Bus (daisy-chained) | Star (each device connects to a central switch) |
| Fault tolerance | One break disables the entire segment | One broken cable only affects that device |
| Connectors | Specialized, harder to terminate | RJ45 — simple and cheap |
| Cost | Higher | Lower |

Speed increases came later, driven by **improvements within UTP itself** (better signal encoding, more pairs used, higher cable categories like Cat5e/Cat6) — not by the copper-vs-coax transition itself.

### Daisy Chain (relevant to bus topology)

**Daisy chain** = connecting devices one after another in a single line, like a chain of daisy flowers strung together.

```
[Device A] --- [Device B] --- [Device C] --- [Device D]
```

Early coax-based Ethernet (bus topology) connected all devices this way on one shared cable. The major weakness: if the cable breaks anywhere along the chain, everything downstream of the break loses connectivity.

**Star topology (UTP + switch)** solves this — each device has its own independent link to a central switch, so one bad cable only affects that one device.

---

## 11. Straight-Through vs. Crossover Cable

**Question:** If Auto MDI-X is disabled, what kind of UTP cable should be used to connect a PC and a switch?
**Answer:** Straight-through

### The rule: same device type → crossover; different device type → straight-through

| Connection | Cable Type |
|------------|------------|
| PC ↔ Switch (different types) | **Straight-through** |
| PC ↔ PC (same type) | Crossover |
| Switch ↔ Switch (same type) | Crossover |
| Router ↔ Router (same type) | Crossover |
| PC ↔ Router (different types) | Straight-through |

### Why this works (ties back to Section 7's pinout)

- PC/end device: pins 1,2 = TX, pins 3,6 = RX
- Switch: pins 1,2 = RX, pins 3,6 = TX (opposite of a PC)

Since the pin roles are already reversed between a PC and a switch, a straight-through cable (pin 1 → pin 1, pin 2 → pin 2, etc.) naturally lines up TX-to-RX correctly. If two identical devices (e.g., two PCs) were connected with a straight-through cable, both would be transmitting on pins 1,2 — with nothing on the other end listening on those pins. A crossover cable manually swaps the pairs so TX lines up with RX.

**Auto MDI-X** is a modern feature that automatically detects and adjusts pin roles regardless of which cable type is plugged in — making the straight-through/crossover distinction mostly irrelevant on modern equipment. This question specifically disables that feature, forcing the traditional rule to apply.

---

## 12. Quick Summary

- The IEEE 802.3 standard family names encode speed + medium; the ratification order (letters) doesn't follow the speed logically, but nicknames (Ethernet / Fast Ethernet / Gigabit Ethernet / 10 Gigabit Ethernet) are grouped purely by speed.
- "BASE-T" in a standard's name always means copper/UTP.
- Pair usage jumps from 2 pairs to all 4 pairs starting at Gigabit speed (1000BASE-T, 1999).
- Fiber standards (SR/LR/ER) are distance-graded; single-mode goes further than multi-mode.
- Twisting protects against interference and crosstalk — not against signal leakage, which is why UTP (unlike shielded coax) can be eavesdropped on.
- Coax was replaced by UTP mainly for topology/reliability/cost reasons, not raw speed.
- SFP modules let switches/routers support swappable fiber (and other) connections.
- Straight-through vs. crossover cable choice depends on whether the two connected devices are the same type or different types — this matters only when Auto MDI-X is off.

---

## 13. Review Questions

| Question | Answer |
|----------|--------|
| Which IEEE standard corresponds to 10BASE-T? | 802.3i (1990) |
| Which IEEE standard corresponds to 100 Mbps (Fast Ethernet)? | 802.3u (1995) |
| Which IEEE standard corresponds to 10GBASE-T? | 802.3an (2006) — not 802.3ae, which is the fiber version |
| How many wire pairs does 10BASE-T use? | 2 pairs (4 wires) |
| How many wire pairs does 10GBASE-T use? | 4 pairs (8 wires) |
| What is the maximum cable length for 10GBASE-LR? | 10 km |
| What is the maximum cable length for 10GBASE-SR? | ~300 m |
| What connects fiber-optic cable to a switch/router port? | SFP transceiver |
| Which cable type is vulnerable to signal leakage/eavesdropping? | UTP (unshielded) |
| PC to switch connection with Auto MDI-X disabled — which cable? | Straight-through |
| On a PC, which pins transmit data in FastEthernet? | Pins 1 and 2 |
| On a PC, which pins receive data in FastEthernet? | Pins 3 and 6 |

---

## My Study Log

- [x] Reviewed Anki cards (IEEE 802.3 standards, cabling, pinouts)
- [ ] Watched a new video (none today — pure Anki review day)
- [ ] Packet Tracer lab
- [x] Notes written for today's review session

### Notes / Confusing Points

- (add your own notes here)
