# Network Physical Layer: Standards, Components, and Theory

This document summarizes the fundamental concepts of the Physical Layer (OSI Layer 1), focusing on standards, functional areas, and data transmission theory.

---

## 1. Physical Layer Standards (4.2.1)
Unlike upper layers (defined by IETF/software), the Physical Layer is governed by electrical and communications engineering organizations due to its reliance on hardware, media, and electronics.

### Key Standards Organizations:
* **ISO:** International Organization for Standardization
* **IEEE:** Institute of Electrical and Electronics Engineers (e.g., 802.3 for Ethernet)
* **TIA/EIA:** Telecommunications Industry Association / Electronic Industries Association
* **ITU:** International Telecommunication Union
* **ANSI:** American National Standards Institute

---

## 2. Three Functional Areas (4.2.2 - 4.2.4)
Physical Layer standards address three specific areas to ensure data can be transmitted across the media.

### A. Physical Components
The actual hardware that carries the signals.
* **Examples:** NICs (Network Interface Cards), connectors (RJ-45), cable materials (Copper, Fiber), and **Pinouts** (the specific wiring diagrams for connectors).

### B. Encoding
The process of converting a stream of data bits into a predefined "code" or pattern.
* **Manchester Encoding:** Used in 10 Mbps Ethernet.
    * **0 bit:** High-to-low voltage transition.
    * **1 bit:** Low-to-high voltage transition.
    * *Note:* The transition occurs at the middle of each bit period for synchronization.
* **High-speed Encoding:** Faster rates use more complex methods like **4B/5B** (100 Mbps) or **8B/10B** (1000 Mbps).

### C. Signaling
The method of representing "1"s and "0"s on the physical media using electrical, optical, or wireless pulses.
* **Example:** A long pulse = 1, a short pulse = 0 (similar to Morse Code).

---

## 3. Bandwidth Concepts (4.2.5)
**Bandwidth** is the capacity of a medium to carry data in a given amount of time.

### Key Distinctions:
* **Speed vs. Capacity:** Bits always travel at the speed of electricity/light regardless of bandwidth (10 Mbps vs. 100 Mbps). The difference is the **number of bits** sent per second.
* **Units of Measure:**
    * **kbps:** $10^3$ bits per second (Thousands)
    * **Mbps:** $10^6$ bits per second (Millions)
    * **Gbps:** $10^9$ bits per second (Billions)
    * **Tbps:** $10^{12}$ bits per second (Trillions)

### Factors Affecting Bandwidth:
1. Properties of the physical media (Copper vs. Fiber).
2. Signaling and detection technologies.
3. Laws of physics.
