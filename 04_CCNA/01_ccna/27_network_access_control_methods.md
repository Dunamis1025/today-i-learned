# Network Access Control: CSMA/CD and CSMA/CA

This document outlines how different network types manage data transmissions and handle potential collisions on a shared medium.

## 1. Data Link Layer Access Control
In shared medium networks, multiple devices compete for the same communication channel. To prevent data corruption, specific protocols are used to manage how and when a device can transmit data.

### Characteristics of Contention-Based Access
- All nodes compete for the use of the medium.
- If two or more devices transmit at the same time, a **collision** occurs.
- These systems do not scale well under heavy traffic due to increased collision rates.

---

## 2. CSMA/CD (Carrier Sense Multiple Access with Collision Detection)
Primarily used in **legacy wired Ethernet** (Half-duplex) using Hubs.

### How it Works:
1. **Carrier Sense**: The device listens to the medium to see if a signal is present.
2. **Transmission**: If the medium is free, the device starts transmitting its **Ethernet Frame**.
3. **Collision Detection**: While transmitting, the NIC monitors the signal amplitude. If the amplitude increases abnormally, a collision is detected.
4. **Jam Signal & Backoff**: Upon collision, devices send a jam signal, stop transmitting, and wait for a random period before retrying.



---

## 3. CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance)
Primarily used in **Wireless LANs (Wi-Fi/IEEE 802.11)**. Wireless media cannot detect collisions while transmitting, so they focus on *avoidance*.

### How it Works:
1. **Carrier Sense**: The device checks if the medium (air) is busy.
2. **Duration Notification**: When transmitting, the device includes a **Time Duration** in the frame, telling other devices how long the medium will be occupied.
3. **Acknowledgment (ACK)**: Because wireless is prone to interference, the receiver must send an **ACK frame** back to the sender to confirm successful delivery.
4. **Retransmission**: If no ACK is received, the sender assumes a collision occurred and resends the data.



---

## 4. Key Components & Comparison

| Concept | Description |
| :--- | :--- |
| **Medium** | The physical path (Copper, Fiber, or Air) where signals travel. |
| **Ethernet Frame** | The Data Link Layer PDU that encapsulates data with Source/Destination MAC addresses. |
| **Hub** | A legacy device (Multiport Repeater) that broadcasts incoming data to all ports, leading to collisions. |
| **Switch** | A modern device that operates in **Full-duplex**, creating dedicated paths and eliminating the need for CSMA/CD. |

### Summary of Differences
- **CSMA/CD**: "Listen, send, and if a crash happens, fix it later." (Wired/Half-duplex)
- **CSMA/CA**: "Listen, announce how long you'll use the road, and wait for a receipt." (Wireless/Wi-Fi)

---

## 5. Security Perspective (Note for Cybersecurity Students)
Understanding these legacy and shared-medium protocols is vital for:
- **Sniffing Attacks**: In Hub-based or Wireless networks, data is broadcasted, making it easier for attackers to intercept traffic.
- **DoS (Denial of Service)**: Attackers can exploit CSMA/CA "Duration" fields to keep the medium busy, preventing legitimate users from connecting.
- **Troubleshooting**: Identifying **Duplex Mismatches** that lead to poor network performance.
