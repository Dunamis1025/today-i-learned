# Day 02 - Interfaces and Cables

> **Course:** Jeremy's IT Lab - Free CCNA 200-301 Complete Course
> **Topic:** Network interfaces, Ethernet standards, UTP cabling and pinouts, and fiber-optic cabling
> **Source:** https://youtu.be/ieTH5lVhNaY

---

## 1. Interfaces and Measuring Speed

### Interfaces (ports)

- A network **switch** has many **ports (interfaces)** used to connect hosts such as PCs and servers.

### Bits per second

- Computer **data size** is measured in **bytes** (1 byte = **8 bits**).
- **Network transmission speed** is measured in **bits per second (bps)**.

| Unit | Name |
|------|------|
| Kbps | Kilobits per second |
| Mbps | Megabits per second |
| Gbps | Gigabits per second |
| Tbps | Terabits per second |

---

## 2. Copper Ethernet Cables and IEEE Standards

- **IEEE 802.3** is the family of standards that defines **Ethernet** (defined by the IEEE, the Institute of Electrical and Electronics Engineers).

### Copper (UTP) Ethernet standards

| Speed | Common name | IEEE standard | Informal name | Max cable length |
|-------|-------------|---------------|---------------|------------------|
| 10 Mbps | Ethernet | 802.3 | **10Base-T** | 100 m |
| 100 Mbps | Fast Ethernet | 802.3u | **100Base-T** | 100 m |
| 1 Gbps | Gigabit Ethernet | 802.3ab | **1000Base-T** | 100 m |
| 10 Gbps | 10 Gigabit Ethernet | 802.3an | **10GBase-T** | 100 m |

### Reading the names (e.g. `1000Base-T`)

| Part | Meaning |
|------|---------|
| `1000` | Speed in Mbps (1000 Mbps = 1 Gbps). `10G` means 10 Gbps |
| `Base` | **Baseband** signaling |
| `T` | **Twisted-pair** cable |

### Distance limit

- The maximum length for twisted-pair Ethernet cable is **100 meters**, to keep the signal reliable.

---

## 3. UTP Cable Structure and the RJ45 Connector

### UTP (Unshielded Twisted-Pair)

- **Unshielded**: no metal shielding around the wires.
- **Twisted**: the wires in each pair are **twisted together**, which protects against **electromagnetic interference (EMI)**.
- Consists of **4 pairs = 8 copper wires** in total.

### RJ45 connector

- The connector at each end of an Ethernet cable, with **8 pins** inside.

### Pins used by each speed

| Standard | Wires used | Pins |
|----------|-----------|------|
| **10Base-T / 100Base-T** | 4 wires (2 pairs) | Pins **1, 2** and **3, 6** |
| **1000Base-T and above** (1 Gbps, 10 Gbps) | **All 8 wires** (4 pairs) | All pins |

### Communication in Gigabit and above

- At 1 Gbps and higher, **each pair communicates in both directions (bi-directional)**, which is how these standards reach much higher speeds.

---

## 4. Transmit/Receive Pins and Cable Types (Very Important)

### Pin roles for 10/100 Mbps

| Device | Pins 1 & 2 | Pins 3 & 6 |
|--------|-----------|-----------|
| **PC / Server / Router / Firewall** | **Transmit (TX)** | **Receive (RX)** |
| **Switch** | **Receive (RX)** | **Transmit (TX)** |

> The **switch is the opposite** of the other devices: what a PC transmits on pins 1 and 2, the switch receives on pins 1 and 2.

### Straight-through cable

- Pin 1 -> pin 1, pin 2 -> pin 2, and so on, straight across.
- Use it to connect devices whose TX/RX pins are **opposite**:
  - **PC -> Switch**
  - **Router -> Switch**
  - Firewall -> Switch (a firewall uses the same pins as a router)

### Crossover cable

- The pins at the two ends are **crossed**:

| One end | Other end |
|---------|-----------|
| Pin 1 | Pin 3 |
| Pin 2 | Pin 6 |
| Pin 3 | Pin 1 |
| Pin 6 | Pin 2 |

- Use it to connect devices whose TX/RX pins are the **same**:
  - **Router -> Router**
  - **Switch -> Switch**
  - **PC -> PC**
  - **PC -> Router**

### Quick rule

```
Different roles  (PC, Router, Firewall  <->  Switch)  ->  Straight-through
Same roles       (Switch <-> Switch, PC <-> Router)   ->  Crossover
```

### Auto MDI-X

- Modern devices support **Auto MDI-X**: the port **detects which pins the other device transmits on** and adjusts its own pins internally.
- Because of this, unless you are working with **older equipment**, the connection will usually work whether you use a straight-through or a crossover cable.
- Still know the difference: it is exam material.

---

## 5. Fiber-Optic Cabling

### Why use fiber?

- When you need to go **farther than 100 meters** or connect a large network, use fiber instead of copper.

### How it works

- Sends **light** through glass fiber instead of electrical signals.

### Connecting to a device

- Routers and switches use an **SFP transceiver (Small Form-factor Pluggable)** module inserted into an expansion slot, and the fiber cable plugs into that module.

### Cable structure (from the inside out)

1. **Fiberglass core**: the light travels through here
2. **Cladding**: reflects the light back into the core
3. **Buffer**: protective layer
4. **Outer jacket**: outer protective covering

### Two types of fiber

| Feature | **Multimode fiber (MMF)** | **Single-mode fiber (SMF)** |
|---------|---------------------------|-----------------------------|
| Core diameter | **Thicker** | **Much thinner** |
| Light path | Multiple light waves travel at **various angles (modes)** | Light travels in **a single, straight path** |
| Distance | Longer than UTP, shorter than single-mode (e.g. **hundreds of meters**) | **Very long** (several km or more) |
| Transmitter | Cheaper **LED-based** | More expensive **laser-based** |
| Cost | Lower | Higher |

---

## 6. UTP vs. Fiber-Optic Summary

| Feature | UTP (copper) | Fiber-optic |
|---------|-------------|-------------|
| **Cost** | Cheap | Expensive (including equipment/modules) |
| **Max distance** | Short (100 m) | Very long (several km or more) |
| **Interference** | Susceptible to **EMI** (reduced by twisting) | **Not affected** by electrical interference |
| **Security** | Small amounts of signal can **leak out** of the cable (possible eavesdropping) | **No signal leakage**, so more secure |

---

## 7. Review Questions

| Question | Answer |
|----------|--------|
| How many bits are in a byte? | **8** |
| What is the max length of UTP Ethernet cable? | **100 meters** |
| Which IEEE standard is Gigabit Ethernet over copper? | **802.3ab (1000Base-T)** |
| Which standard is Fast Ethernet? | **802.3u (100Base-T)** |
| What does `T` in `1000Base-T` stand for? | **Twisted-pair** |
| How many wires do 10/100 Mbps Ethernet use? | **4 (pins 1, 2, 3, 6)** |
| How many wires do 1 Gbps and above use? | **8 (all four pairs)** |
| Which pins does a PC use to transmit? | **1 and 2** |
| Which pins does a switch use to transmit? | **3 and 6** |
| What cable connects a PC to a switch? | **Straight-through** |
| What cable connects a switch to a switch? | **Crossover** |
| What feature makes cable type mostly irrelevant on modern gear? | **Auto MDI-X** |
| What module lets a switch use fiber cable? | **SFP transceiver** |
| Which fiber type goes farther and uses lasers? | **Single-mode** |
| Which fiber type is cheaper and uses LEDs? | **Multimode** |
| Which medium is immune to EMI and does not leak signal? | **Fiber-optic** |

---

## 8. Quick Summary

- Network speed is in **bits per second**; 1 byte = 8 bits.
- Copper Ethernet: **10Base-T, 100Base-T, 1000Base-T, 10GBase-T**, all with a **100 m** limit.
- UTP has **4 pairs (8 wires)**; **10/100** use pins **1, 2, 3, 6**, and **1G+** use all 8 wires bi-directionally.
- PC, router, firewall: **TX on 1, 2 / RX on 3, 6**. Switch: **the opposite**.
- **Straight-through** for different device types; **crossover** for the same. **Auto MDI-X** handles it automatically on modern gear.
- **Fiber** uses light, needs **SFP** modules, and comes as **multimode** (cheaper, shorter, LED) or **single-mode** (pricier, longer, laser).
- UTP = cheap but limited in distance and less secure; fiber = expensive but long-range, immune to EMI, and secure.

---

## 9. My Study Log

- [x] Watched the video
- [ ] Reviewed Anki cards (Day 02 Flashcards - Interfaces and Cables)
- [ ] Practiced pinouts from memory (TX/RX on PC vs. switch)

### Notes / Confusing Points

- (add your own notes here)
