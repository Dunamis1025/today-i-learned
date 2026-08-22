# Physical Layer Summary and Network Media Comparison

## 1. Overview of the Physical Layer (OSI Layer 1)
The Physical Layer is responsible for the actual physical connection between devices. It serves as the foundation for all network communications by converting data into signals that can be transmitted over physical media.

### Key Functions
* **Signal Encoding:** Converting bits (0s and 1s) into electrical, optical, or radio signals.
* **Transmission:** Moving bits across the physical link.
* **Reception:** Receiving signals from the media and converting them back into bits.

---

## 2. Performance Metrics and Terminology
Understanding the quality of data transmission is crucial at the physical layer.

* **Bandwidth:** The maximum capacity of a medium to carry data (Theoretical maximum).
* **Throughput:** The actual amount of data transferred over a period of time (Practical speed).
* **Latency:** The time required for a signal to travel from one point to another, including delays.
* **Goodput:** The measure of usable, application-level data transferred, excluding protocol overhead and retransmissions.

---

## 3. Network Media Comparison

### A. Copper Cabling (UTP/STP/Coaxial)
Copper media is widely used due to its low cost and ease of installation.
* **Signal Type:** Electrical Pulses.
* **Vulnerabilities:** Susceptible to **EMI (Electromagnetic Interference)**, **RFI (Radio Frequency Interference)**, and **Crosstalk**.
* **UTP (Unshielded Twisted Pair):** Uses cancellation (twisting pairs) to minimize interference.
* **Connectors:** Commonly terminated with **RJ-45** connectors.

### B. Fiber-Optic Cabling
Fiber-optic technology uses glass or plastic strands to transmit data as pulses of light.
* **Signal Type:** Light Pulses.
* **Advantages:** Immune to EMI/RFI, extremely high bandwidth, and supports very long distances.
* **Common Connectors:** ST (Snap-in), SC (Square), and LC (Little/Lucent).
* **Usage:** Primarily used for backbone cabling and interconnecting buildings.

### C. Wireless Media
Wireless media use radio or microwave frequencies to transmit electromagnetic signals.
* **Signal Type:** Electromagnetic Waves.
* **Limitation Factors:** Coverage area, interference from other devices, and security risks.
* **Major Standards:** * **Wi-Fi:** IEEE 802.11
    * **Bluetooth:** IEEE 802.15
    * **Zigbee:** IEEE 802.15.4

---

## 4. Ethernet Cable Wiring Standards (UTP)
The wiring convention determines the type of connection:

| Cable Type | Use Case |
| :--- | :--- |
| **Straight-through** | Connecting different types of devices (e.g., PC to Switch). |
| **Crossover** | Connecting similar types of devices (e.g., Switch to Switch, PC to PC). |
| **Rollover** | Cisco proprietary cable for connecting a workstation to a router console port. |

---

## 5. Conclusion
The Physical Layer is the critical first step in network communication. Selecting the appropriate medium (Copper, Fiber, or Wireless) depends on the required distance, bandwidth, and environmental factors such as potential interference.
