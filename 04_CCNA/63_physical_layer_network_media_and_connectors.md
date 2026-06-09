# Network Fundamentals — Study Notes
> Topic: Physical Layer & Network Media (Cables & Connectors)

---

## 1. Network Media Overview

| Media Type | Common Name | Connector | Shielding | Primary Use |
|---|---|---|---|---|
| **UTP** | Ethernet / LAN cable | RJ-45 | ❌ None | Homes, offices, schools |
| **STP** | Shielded LAN cable | RJ-45 (grounded) | ✅ Metal foil/braid | Factories, high-interference areas |
| **Coaxial** | Coax cable | BNC / N-type / F-type | ✅ Built-in | Antennas, TV, cable internet |
| **Fiber-Optic** | Fiber cable | SC / LC / ST | N/A (light-based) | Long-distance, high-speed backbone |

---

## 2. UTP — Unshielded Twisted Pair

- **Most common** network media in use worldwide
- Found in virtually every home, school, and office
- **Connector:** RJ-45 (the transparent plastic plug on a standard Ethernet cable)
- **Advantages:** Inexpensive, flexible, easy to install
- **Disadvantage:** Susceptible to EMI/RFI interference (no shielding)
- **Examples:** Cat5e, Cat6, Cat6a — differ in supported speeds and frequencies

> ✅ Default choice for everyday local networking due to best cost-to-performance ratio.

---

## 3. STP — Shielded Twisted Pair

- Same twisted-pair structure as UTP, but wrapped in **metallic foil or braided shielding**
- Uses **special grounded connectors** to maintain the shielding's effectiveness end-to-end
- **Counters:** EMI (Electromagnetic Interference) and RFI (Radio Frequency Interference)
- **Use cases:** Industrial environments, near high-voltage equipment, server rooms with heavy electrical noise
- **Disadvantage:** More expensive and harder to install than UTP

> 🛡️ Think of STP as a cable wearing "armor" — it protects the signal from external electrical noise.

---

## 4. Coaxial Cable

- A thick, round cable with a central conductor surrounded by insulation and a metallic shield
- **Terminates with specialized connectors:**
  - **F-type** — Home TV / cable modem connections
  - **BNC** — CCTV, professional video equipment, older network topologies
  - **N-type** — Wireless/radio equipment, outdoor antennas (weatherproof, heavy-duty)
- **Key role:** Connects **antennas to wireless devices** — carries high-frequency RF signals with minimal loss
- **Bundled with fiber:** In telecom infrastructure (e.g., cell towers), coaxial cables are often bundled together with fiber-optic cables — fiber carries bulk data as light; coax delivers power or RF signals to the antenna

> 📡 If you see "antenna" + "two-way transmission" in a question, the answer is almost always **Coaxial**.

---

## 5. Physical Layer (OSI Layer 1) — Key Facts

- The Physical Layer manages **all physical transmission media** — both wired and wireless
- It does **not** deal only with wired connections; Wi-Fi and Bluetooth also operate at this layer
- When a frame is encoded and transmitted at the Physical Layer:
  - Bits are sent **serially** (one bit at a time, in sequence) — **not** all at once in parallel
  - This sequential transmission allows the receiver to accurately reconstruct the signal and detect errors

> ❌ **False:** "The Physical Layer only involves wired connections." — It includes wireless too.  
> ❌ **False:** "All bits are transmitted simultaneously." — They are sent one at a time (serially).

---

## 6. Interference — EMI vs. RFI

| Term | Full Name | Source Examples |
|---|---|---|
| **EMI** | Electromagnetic Interference | Power lines, motors, fluorescent lights |
| **RFI** | Radio Frequency Interference | Wireless devices, radio transmitters |

- **UTP** — vulnerable to both EMI and RFI
- **STP** — specifically designed to counter both using shielding + grounded connectors
- **Coaxial** — also has built-in shielding, but is in a different cable category (not twisted pair)

---

## 7. Quick-Reference: "Which cable is it?" Decision Guide

```
Need to connect an antenna?              → Coaxial
Bundled with fiber at a cell tower?      → Coaxial
BNC / N-type / F-type connector?         → Coaxial
Blocks EMI/RFI with shielding?           → STP
Most common / cheapest / everyday LAN?  → UTP
RJ-45 connector?                         → UTP or STP
```

---

## 8. Key Vocabulary

| Term | Definition |
|---|---|
| **EMI** | Electromagnetic Interference — noise from electrical sources |
| **RFI** | Radio Frequency Interference — noise from radio/wireless sources |
| **Shielding** | Metallic foil or braiding wrapped around cable wires to block interference |
| **Serial transmission** | Sending data one bit at a time in sequence |
| **RJ-45** | Standard 8-pin connector used with UTP/STP Ethernet cables |
| **BNC / N-type / F-type** | Specialized connectors used exclusively with coaxial cables |
| **Physical Layer** | OSI Layer 1 — responsible for transmitting raw bits over a physical medium |
