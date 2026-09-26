# Day 02 (continued, Part 2): Pinouts, Fiber Distances & Anki Corrections

> Second Anki deep-dive session for **Day 02 (Interfaces and Cables)**. Continues directly from `05_day02_ethernet_standards_and_cabling_deep_dive.md`. This session focused on: SFP transceivers (repeat), a corrected Anki card (10GBASE-ER), physical pin-pair wiring vs. TX/RX role wiring, fiber distance variability by fiber grade (10GBASE-SR), a new Gigabit fiber standard (1000BASE-LX), and UTP's fixed 100 m distance limit.

---

## 1. SFP Transceivers (Recap)

**Question:** Fiber-optic cables are connected to _____ transceivers in a router or switch.
**Answer:** SFP (Small Form-Factor Pluggable)

- **Small Form-Factor** = physically small module.
- **Pluggable** = can be inserted/removed without replacing the whole device.
- Ports on switches/routers are left as generic empty slots; the SFP module plugged into that slot determines what kind of cable (fiber, etc.) the port can connect to — similar to how a laptop's USB-C port accepts different adapters (HDMI, Ethernet) to change what it connects to.

```
[Fiber cable] --- [SFP module] --- (plugged into) --- [Switch/router port]
```

---

## 2. ⚠️ Anki Card Correction: 10GBASE-ER Maximum Cable Length

**The Anki deck's stated answer (30 km) is incorrect.**

| Standard | Correct Max Distance |
|----------|----------------------|
| 10GBASE-SR | 300 m (OM3) / 400 m (OM4) — see Section 4 |
| 10GBASE-LR | 10 km |
| **10GBASE-ER** | **40 km** (not 30 km) |

**Action taken:** the card's Back field should be manually edited in Anki (Browse → search "10GBASE-ER" → edit Back field → change 30 km to 40 km).

**Memory aid:** ER = LR × 4 = 10 km × 4 = 40 km.

---

## 3. Physical Wire Pairs vs. TX/RX Pin Roles — Two Different Questions

This was a major point of confusion this session. There are **two distinct types of pin-related questions**, and they ask about different things entirely:

### Type A: TX/RX role (which pins send vs. receive) — applies when only 2 pairs are used

Relevant for 10BASE-T / 100BASE-TX (2-pair standards):

| Device | Transmit (TX) pins | Receive (RX) pins |
|--------|---------------------|---------------------|
| PC / end device (firewall, router, etc.) | 1, 2 | 3, 6 |
| Switch / hub | 3, 6 (reversed!) | 1, 2 (reversed!) |

**Why the switch is reversed:** a straight-through cable connects pin 1→1, 2→2, etc. with no crossing. For communication to work, one side's transmit pins must line up with the other side's receive pins. Since a PC transmits on 1,2, the switch must receive on 1,2 (and therefore transmit on 3,6) for a straight-through cable to work correctly.

**Question:** In a FastEthernet connection, a switch transmits data on which pins?
**Answer: 3 and 6** (not 1,2 — that would be the PC's transmit pins, not the switch's)

**Key habit:** always check *which device* the question is asking about before answering — the same pin numbers (1,2 / 3,6) mean opposite things depending on whether it's a PC or a switch.

### Type B: Physical wire-pair grouping (which pins are twisted together) — applies when all 4 pairs are used

Relevant for 1000BASE-T / 10GBASE-T (4-pair standards):

**Question:** Which four pin pairs are used in a 1000BASE-T or 10GBASE-T connection?
**Answer:** Pair 1-2, Pair 3-6, Pair 4-5, Pair 7-8

| Physical Pair | Pins |
|----------------|------|
| Pair 1 | 4, 5 |
| Pair 2 | 1, 2 |
| Pair 3 | 3, 6 |
| Pair 4 | 7, 8 |

This is a completely different kind of question — it's not asking "which pins transmit vs. receive," it's asking **which pins are physically twisted together inside the cable** as manufactured (per T568A/B wiring standard). All 4 pairs are used simultaneously in Gigabit+ standards, so there's no simple TX/RX split anymore — each pair carries bidirectional signal.

**Why the seemingly odd pairing (1-2, 3-6 instead of something like 1-4, 2-5, 3-6, 4-7)?**

*Correction from earlier assumption:* this is **not** primarily a crosstalk-avoidance design choice. The real reason is **backward compatibility with the older RJ11 telephone connector**. RJ45 (8-pin) evolved from RJ11 (4/6-pin) telephone jacks, where the center pins (4,5) carried the most important line (so a loosely-inserted plug would still make contact on the most critical circuit first). Ethernet inherited this legacy pin layout rather than designing an optimal one from scratch. Crosstalk is instead managed through **twisting each pair internally** and by giving each pair a **slightly different twist rate (pitch)**, not through the choice of which pin numbers are grouped.

---

## 4. 10GBASE-SR Distance Depends on Fiber Grade

**Question:** 10GBASE-SR maximum cable length?
**The Anki answer given (400 m) is not wrong — it depends on fiber grade, and both common answers are legitimate:**

| Fiber Grade | Max Distance |
|-------------|--------------|
| Legacy FDDI-grade MMF | 26 m |
| **OM3** | **300 m** |
| **OM4** (or OM5) | **400 m** |

- IEEE 802.3ae originally defined 10GBASE-SR's benchmark distance as 300 m over OM3 fiber.
- As fiber manufacturing improved, OM4-grade fiber extended the same standard to 400 m.
- CCNA material commonly cites 300 m (the original IEEE benchmark), but 400 m is a valid real-world figure depending on which fiber grade the deck assumes.

**Updated memory table (revised from earlier session):**

| Standard | Distance |
|----------|----------|
| 10GBASE-SR (OM3) | 300 m |
| 10GBASE-SR (OM4) | 400 m |
| 10GBASE-LR | 10 km |
| 10GBASE-ER | 40 km |

**Correction note:** in the prior session's memory trick ("300m ignored, 30+10=40"), the "40" refers to **40 km**, not 400 (km). Watch the unit — km vs. m matters a lot here.

---

## 5. New Standard: 1000BASE-LX (Gigabit Ethernet over Fiber)

**Question:** 1000BASE-LX maximum cable length?
**Answer:** 550 meters (multimode) / 5 kilometers (single-mode)

This is a **sub-type of 1000BASE-X** (802.3z, 1998) — the same way 10GBASE-SR/LR/ER are sub-types under the 10 Gigabit fiber umbrella.

```
802.3z (1998, Gigabit Ethernet, Fiber) = 1000BASE-X
                    │
        ┌───────────┴───────────┐
   1000BASE-SX               1000BASE-LX
   (multimode only,           (multimode AND single-mode,
    ~550 m)                    550 m / 5 km)
```

- **SX** = Short reach (multimode fiber only)
- **LX** = Long reach (supports **both** multimode and single-mode fiber)

**Why two distances for one standard:** 1000BASE-LX is unusual in that it supports both fiber types. The maximum distance depends on which type is used:
- Multimode fiber → 550 m
- Single-mode fiber → 5 km (note: many vendor datasheets advertise an extended "LX/LH" product rated to 10 km, but the base IEEE 802.3z standard specifies 5 km)

This isn't a contradiction — it's one standard with two valid answers depending on the physical medium connected.

---

## 6. UTP's Fixed 100-Meter Limit

**Question:** What is the maximum length of an Ethernet UTP cable?
**Answer:** 100 meters

**Key insight:** unlike fiber (where distance varies by standard — SR/LR/ER/SX/LX each have different limits), **UTP copper cable has a single fixed limit of 100 m regardless of speed** — this applies identically to 10BASE-T, 100BASE-TX, 1000BASE-T, and 10GBASE-T.

**Why:** copper carries an electrical signal, which weakens (attenuates) with distance due to electrical resistance. Beyond ~100 m, the signal degrades too much to be reliably read. Fiber carries light instead, which attenuates far more slowly — hence fiber standards can reach anywhere from 300 m to 40 km depending on type.

**Memory rule:** "UTP = always 100 m, no matter the standard. Fiber = distance varies by standard, must memorize each one separately."

---

## 7. Quick Summary

- SFP transceivers connect fiber cables to switch/router ports via pluggable modules.
- **Anki correction:** 10GBASE-ER max length is 40 km, not 30 km (deck error, manually fixed).
- Two different pin-related question types exist: (a) TX/RX role questions (PC vs. switch — roles reversed), and (b) physical wire-pair grouping questions (1-2, 3-6, 4-5, 7-8 — fixed cable wiring, inherited from RJ11 telephone jacks, not a crosstalk-avoidance design).
- 10GBASE-SR distance depends on fiber grade: 300 m (OM3) or 400 m (OM4) — both are valid, not a card error.
- 1000BASE-LX is a Gigabit fiber sub-standard supporting both multimode (550 m) and single-mode (5 km) fiber.
- UTP copper cable is always limited to 100 m regardless of speed/standard, due to electrical signal attenuation.

---

## 8. Review Questions

| Question | Answer |
|----------|--------|
| What connects fiber-optic cable to a switch/router port? | SFP transceiver |
| What is the correct max distance for 10GBASE-ER? | 40 km (Anki deck previously showed 30 km — incorrect) |
| In FastEthernet, which pins does a switch transmit on? | 3 and 6 |
| In FastEthernet, which pins does a PC transmit on? | 1 and 2 |
| Which four physical pin pairs are used in 1000BASE-T/10GBASE-T? | Pair 1-2, Pair 3-6, Pair 4-5, Pair 7-8 |
| Why isn't the RJ45 pin-pair layout evenly spaced (e.g., 1-4, 2-5...)? | Inherited from RJ11 telephone connector design, not originally optimized for Ethernet crosstalk |
| What is 10GBASE-SR's max distance on OM3 fiber? | 300 m |
| What is 10GBASE-SR's max distance on OM4 fiber? | 400 m |
| What is 1000BASE-LX's max distance over multimode fiber? | 550 m |
| What is 1000BASE-LX's max distance over single-mode fiber? | 5 km |
| What is the max length of any Ethernet UTP cable? | 100 m (fixed, regardless of speed) |

---

## My Study Log

- [x] Reviewed remaining Anki Day 02 cards (26 → 0 remaining)
- [ ] Watched a new video (none today — pure Anki review day)
- [ ] Packet Tracer lab
- [x] Notes written for today's review session
- [x] Corrected one erroneous Anki card (10GBASE-ER)

### Notes / Confusing Points

- (add your own notes here)
