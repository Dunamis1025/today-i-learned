# Network Cabling — Study Notes

## 1. Twisted-Pair (UTP) Cable Categories

All UTP cables have a maximum transmission distance of **100 meters**. In **plenum spaces** (ventilation areas), **plenum-rated cables** are mandatory due to their fire-retardant materials that produce minimal smoke.

| Category | Speed | Key Features |
|----------|-------|-------------|
| Cat 5 | 100 Mb/s | First widely adopted 4-pair UTP standard |
| Cat 5e | 1 Gb/s | Tighter twists to reduce EMI and RFI |
| Cat 6 / 6a | 1 Gb/s | Internal plastic divider separates wire pairs; Cat 6a offers superior insulation; ideal for gaming and videoconferencing |

---

## 2. Wiring Standards — T568A vs T568B

RJ-45 connectors contain **8 wires** that must be arranged in a specific order. The two standards differ only in the positions of the **orange and green pairs**.

| Standard | Wire Order (left to right) |
|----------|--------------------------|
| T568A | Green/White, Green, Orange/White, Blue, Blue/White, Orange, Brown/White, Brown |
| T568B | Orange/White, Orange, Green/White, Blue, Blue/White, Green, Brown/White, Brown |

**Rules:**
- Both ends of a cable must use the **same standard**
- Follow the existing scheme when working on an established network
- **T568B** is the most commonly used standard in commercial and residential installations

---

## 3. Building a Custom Network Cable — Step by Step

1. **Measure and Cut** — Determine the required length and cut the cable
2. **Strip the Sheath** — Remove the outer jacket using a cable stripper
3. **Organize Wires** — Separate the 4 pairs into 8 individual wires; remove internal plastic separators and pull strings; straighten the wires
4. **Arrange by Color Code** — Order the wires according to T568A or T568B
5. **Connect and Trim** — Trim wires to the correct length so the connector grips the outer sheath, not just the wires; slide firmly into the RJ-45 connector
6. **Crimp** — Use a crimping tool to permanently compress the connector onto the cable
7. **Test** — Use a cable tester to confirm all 8 wires are correctly connected; verify with `ipconfig` and `ping`

---

## 4. Fiber-Optic Cable

Fiber-optic cables transmit data using **pulses of light** instead of electricity, making them immune to **EMI and RFI** and capable of carrying signals over much longer distances with higher bandwidth.

### Cable Structure (innermost → outermost)

| Layer | Function |
|-------|----------|
| **Core** | Central glass element where light travels |
| **Cladding** | Surrounds the core; reflects light inward like a mirror to keep the signal contained |
| **Buffer** | Protects the core and cladding from physical damage |
| **Strengthening Material** | Prevents the cable from stretching during installation (often made from the same material as bulletproof vests) |
| **Jacket** | Outermost layer (usually PVC); protects against abrasion, moisture, and environmental contaminants |

---

## 5. Fiber Types — SMF vs MMF

| Feature | Single-Mode (SMF) | Multimode (MMF) |
|---------|-------------------|-----------------|
| Core Size | Very small (~9 microns) | Larger (50–62.5 microns) |
| Light Source | Laser | LED |
| Light Path | Single path | Multiple paths |
| Distance | Hundreds of kilometers | Up to 550 meters |
| Use Case | Long-haul telephony, cable TV | LAN (office/building environments) |

---

## 6. Fiber-Optic Connectors

- **FX / SX standards** require **two fiber strands** (one TX, one RX) → often use **duplex connectors**
- **BX standard** uses **WDM (Wavelength-Division Multiplexing)** — transmits and receives over a **single fiber strand** using different light wavelengths simultaneously

### Common Connector Types

| Connector | Description |
|-----------|-------------|
| **ST** (Straight Tip) | Bayonet-style; locks with a twist |
| **SC** (Subscriber Connector) | Push-pull design; common in data communications |
| **LC** (Lucent Connector) | Small form-factor; ideal for high-density installations |

---

## 7. Key Terms Glossary

| Term | Definition |
|------|-----------|
| **Plenum-rated** | Fire-retardant cable for use in ventilation spaces |
| **EMI / RFI** | Electromagnetic / Radio Frequency Interference |
| **Crimping** | Permanently compressing a connector onto a cable using a crimping tool |
| **Sheath** | The outer plastic jacket that wraps and protects all inner wires |
| **WDM** | Technology enabling simultaneous bi-directional transmission over a single fiber using different light wavelengths |
| **Duplex connector** | A connector housing two fiber strands in one assembly |
