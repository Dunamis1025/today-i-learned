# Network Fundamentals — Study Notes

> Topics: Wireless LAN Interference · OSI Physical Layer · Crosstalk · Throughput · WLAN Standards

---

## Q11 — Wireless LAN Signal Interference

**Problem:** A wireless LAN in a park ranger's office (located at the highest point of a national park) occasionally suffers signal distortion. What is the most likely cause?

**Answer:** Microwave oven

### Key Points
- Standard Wi-Fi operates on the **2.4 GHz** frequency band.
- Microwave ovens also emit electromagnetic waves at **2.4 GHz** when heating food.
- When both operate simultaneously, their signals **collide and interfere**, causing slowdowns or dropped connections.
- This is a classic real-world example of **RF (Radio Frequency) interference**.

---

## Q12 — Purpose of the OSI Physical Layer

**Problem:** What is the purpose of the OSI Physical Layer?

**Answer:** Transmitting bits across the local media

### Key Points
- Computers process all data as **bits (0s and 1s)**.
- The Physical Layer is **Layer 1** of the OSI model — the very foundation.
- Its job is to convert bits into **physical signals** for transmission:
  - Electrical voltage → copper wire
  - Light pulses → fiber optic cable
  - Radio waves → wireless (air)
- It does **not** interpret the data — it only moves it from point A to point B.

---

## Q13 — Crosstalk

**Problem:** Which characteristic describes crosstalk?

**Answer:** The distortion of transmitted messages caused by signals carried in adjacent wires

### Key Points
- **Crosstalk** = signal bleeding between neighboring wires in the same cable bundle.
- When a strong electrical signal flows through one wire, it generates a small **electromagnetic field**.
- That field can leak into an **adjacent wire**, creating interference and distorting the data signal.
- Result: data errors and "noise" on the line.
- **Twisted-pair cables** (e.g., Cat5e, Cat6) mitigate crosstalk by twisting wire pairs together, which cancels out the interfering electromagnetic fields.

---

## Q14 — Throughput

**Problem:** What is indicated by the term throughput?

**Answer:** The measure of the usable data transferred across the media

### Key Points

| Term | Definition | Analogy |
|---|---|---|
| **Bandwidth** | Theoretical maximum capacity of a connection | Number of lanes on a highway |
| **Throughput** | Actual usable data successfully delivered | Cars that actually reach the destination |

- Throughput is **always ≤ bandwidth** in practice.
- Real-world throughput is reduced by:
  - Network errors and retransmissions
  - Packet collisions
  - Protocol **overhead** (headers, control data)
- Throughput = what you actually get; Bandwidth = what the connection promises.

---

## Q15 — WLAN Standards Organization

**Problem:** Which standards organization oversees the development of wireless LAN standards?

**Answer:** IEEE (Institute of Electrical and Electronics Engineers)

### Key Points
- IEEE manages the **802.11 standard** — the technical rulebook for all Wi-Fi devices.
- Because all manufacturers (Apple, Samsung, TP-Link, etc.) follow IEEE 802.11, devices from different brands can communicate seamlessly.
- Common 802.11 variants:

| Standard | Frequency | Max Speed |
|---|---|---|
| 802.11b/g/n | 2.4 GHz | Up to 600 Mbps (n) |
| 802.11a/ac/ax | 5 GHz / 6 GHz | Up to several Gbps (ax) |

- IEEE sets the standard; **Wi-Fi Alliance** certifies that products correctly implement it.

---

## Quick Reference Summary

| # | Topic | Key Answer |
|---|---|---|
| Q11 | WLAN interference source | Microwave oven (2.4 GHz conflict) |
| Q12 | OSI Physical Layer purpose | Transmit bits across physical media |
| Q13 | Crosstalk definition | Signal bleeding between adjacent wires |
| Q14 | Throughput vs. Bandwidth | Throughput = actual usable data delivered |
| Q15 | WLAN standards body | IEEE (802.11 standard) |
