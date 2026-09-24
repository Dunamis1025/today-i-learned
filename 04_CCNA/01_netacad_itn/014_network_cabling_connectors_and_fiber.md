# 11. Network Cabling Fundamentals (UTP, RJ-45, Fiber Optics)

---

## 1. UTP Cabling Overview

UTP (Unshielded Twisted Pair) is the most commonly used cable in LAN networks.

### Key Characteristics
- Low cost
- Easy to install
- Uses electrical signals
- Sensitive to interference (EMI, RFI)

---

## 2. Cabling Standards (TIA/EIA & IEEE)

### TIA/EIA-568
Defines:
- Cable types
- Cable length
- Connectors
- Termination
- Testing methods

### IEEE
- Defines electrical characteristics
- Categorizes cables based on performance

---

## 3. UTP Cable Categories

| Category | Speed |
|--------|------|
| Cat3 | Voice |
| Cat5 | 100 Mbps |
| Cat5e | 1 Gbps |
| Cat6 | Up to 10 Gbps |
| Cat7 | 10 Gbps |
| Cat8 | 40 Gbps |

👉 Higher category = higher speed & bandwidth

---

## 4. RJ-45 Connector

- Standard connector for Ethernet cables
- Male connector (plug)
- Female = socket (wall, switch, patch panel)

### Important
👉 Poor termination = performance degradation

---

## 5. Good vs Bad Termination

### Bad Termination
- Wires exposed
- Untwisted too much
- Not fully covered

👉 Causes signal loss

### Good Termination
- Minimal untwisting
- Clean arrangement
- Fully inserted

---

## 6. Wiring Standards (T568A vs T568B)

### T568A
Green first

### T568B (Most common)
Orange first

### Key Pattern
- Blue (pins 4-5) → always same
- Brown (pins 7-8) → always same
- Only Green & Orange swap

👉 "Blue & Brown fixed, Green vs Orange changes"

---

## 7. Cable Types

### 1. Straight-through
- Same standard both ends (A-A or B-B)
- Used for:
  - PC → Switch
  - Switch → Router

---

### 2. Crossover
- A on one side, B on the other
- Used for:
  - Switch ↔ Switch
  - PC ↔ PC
  - Router ↔ Router

👉 Now mostly replaced by Auto-MDIX

---

### 3. Rollover Cable
- Cisco proprietary
- Used for:
  - PC → Console port

---

## 8. Common Troubleshooting Tip

Wrong cable type:
- ❌ No damage
- ❌ No connection

👉 First check: cable connection

---

## 9. Fiber Optic Cabling

### Key Advantages
- Longer distance
- Higher bandwidth
- Low attenuation
- Immune to EMI/RFI

---

### How it Works
- Uses light instead of electricity
- Data = light signals
- Glass fiber = light path (waveguide)

---

### Structure
- Very thin (like human hair)
- Made of pure glass

---

### Analogy
Fiber optic = light pipe

👉 Like a mirror tube sending laser signals

---

## 10. Key Concepts Summary

- UTP = electrical signal, cheap but sensitive
- Fiber = light signal, fast and reliable
- RJ-45 = standard connector
- T568A/B = wiring standards
- Cable type must match situation

---

## 🔥 One-Line Summary

👉 "Correct cable + correct wiring = stable network"
