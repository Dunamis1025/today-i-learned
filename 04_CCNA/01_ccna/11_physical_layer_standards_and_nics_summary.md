
---

## 1. Network Interface Cards (NICs)

A Network Interface Card (NIC) connects a device to a network.

### Types of NICs
- **Ethernet NIC** → Used for wired connections
- **WLAN NIC** → Used for wireless connections

### Key Points
- Devices may have **one or both** types of NICs
- A **printer** typically uses Ethernet (wired)
- Devices like **smartphones and tablets** use WLAN (wireless)

👉 NIC = the hardware that enables network connectivity

---

## 2. Physical Layer (Layer 1) Overview

The physical layer is responsible for transmitting raw bits over network media.

### Core Functions
- Receives a **frame** from the Data Link layer
- Converts the frame into **bits**
- Encodes bits into signals:
  - Electrical (wired)
  - Optical (fiber)
  - Radio (wireless)
- Transmits signals **one at a time (serial transmission)**

---

## 3. Transmission Behavior

- Bits are **NOT sent all at once**
- Signals are sent:
  
👉 **one at a time (sequentially)**

---

## 4. Receiving Process

At the destination:

1. Signals are received from the media  
2. Signals are converted back into bits  
3. Bits are passed up to the **Data Link layer**  
4. Reconstructed as a **complete frame**

---

## 5. PDU Flow (Important for Exams)

| Layer        | PDU     |
|-------------|--------|
| Data Link   | Frame  |
| Physical    | Bits   |

👉 Physical layer receives a **Frame** and transmits **Bits**

---

## 6. Key Concepts

### Physical Layer Scope
- Works with **hardware**
- Includes:
  - Cables
  - Connectors
  - Signals

### Covers ALL transmission types
- Wired
- Wireless
- Optical

---

## 7. Physical Layer Standards

Physical layer standards ensure all hardware and signals work together properly.

### Major Organizations

- ISO (International Organization for Standardization)
- TIA/EIA (Telecommunications Industry Association)
- ITU (International Telecommunication Union)
- ANSI (American National Standards Institute)
- IEEE (Institute of Electrical and Electronics Engineers)
- Regulatory bodies (FCC, ETSI)

### Regional Standards

- CSA (Canada)
- CENELEC (Europe)
- JSA/JIS (Japan)

---

## 8. Key Takeaways

- Physical layer = **bit transmission using signals**
- Transmission is **sequential, not simultaneous**
- Works with **real-world hardware**
- Receives **Frame → sends Bits**
- Passes data to **Data Link layer**

---

## Final Insight

The physical layer does not "understand" data.

It only converts data into signals and moves them across the network.

---

