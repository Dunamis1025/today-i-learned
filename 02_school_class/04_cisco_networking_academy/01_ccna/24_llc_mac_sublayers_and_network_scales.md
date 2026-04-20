# 24. IEEE 802 LAN/MAN Data Link Sublayers & Network Scales

## 1. IEEE 802 Data Link Sublayers
The IEEE 802 LAN/MAN standards define the Data Link Layer (Layer 2) as being divided into two distinct sublayers: **Logical Link Control (LLC)** and **Media Access Control (MAC)**. This separation allows for hardware independence and supports multiple upper-layer protocols.

### A. Logical Link Control (LLC) - IEEE 802.2
The LLC sublayer acts as the interface between the network software (Upper Layers) and the device hardware (Lower Layers).
- **Protocol Identification:** It places information in the frame that identifies which Layer 3 protocol (e.g., IPv4, IPv6) is being used.
- **Multiplexing:** Allows multiple Layer 3 protocols to share a single network interface and media.
- **Function:** It essentially acts as a "translator" or "labeler" that tells the hardware what kind of data it is handling.

### B. Media Access Control (MAC)
The MAC sublayer is responsible for data encapsulation and controlling how data is placed on the physical media.
- **Data Encapsulation:**
    - **Frame Delimiting:** Provides delimiters to identify the start and end of a frame, ensuring synchronization between the sender and receiver.
    - **Addressing:** Adds source and destination MAC addresses for Layer 2 transport within the same local network.
    - **Error Detection:** Includes a Frame Check Sequence (FCS) in the trailer to detect transmission errors.
- **Media Access Control:**
    - Controls the Network Interface Card (NIC) and hardware responsible for sending/receiving signals.
    - Manages access to shared media, especially in **Half-duplex** environments where multiple devices share the same communication path.


---

## 2. Network Scales and Classifications
Networks are categorized based on their geographic span and the technology used to connect them.

### A. WPAN (Wireless Personal Area Network)
- **Range:** Very short distance (typically up to 10 meters).
- **Common Technologies:** Bluetooth (IEEE 802.15), Zigbee.
- **Usage:** Connecting personal devices like wireless earbuds, smartwatches, and smartphones.

### B. LAN (Local Area Network)
- **Range:** Small geographic area such as a home, office, or school building.
- **Common Technologies:** Ethernet (IEEE 802.3), Wi-Fi (IEEE 802.11).
- **Usage:** High-speed internal communication between local computers and peripherals.

### C. MAN (Metropolitan Area Network)
- **Range:** A large campus or an entire city.
- **Common Technologies:** Fiber optics, Metro Ethernet.
- **Usage:** Connecting multiple LANs across a city (e.g., a city-wide public Wi-Fi or university campus network).

### D. WAN (Wide Area Network)
- **Range:** Vast geographic distances, including countries or continents.
- **Common Technologies:** MPLS, Cellular (4G/5G), Satellite, Fiber-optic undersea cables.
- **Usage:** The Internet is the most well-known example of a WAN.

---

## 3. Communication Modes
- **Half-duplex:** Data can be sent or received, but not both at the same time. Requires Media Access Control to prevent collisions.
- **Full-duplex:** Data can be sent and received simultaneously. Modern Ethernet switches typically operate in full-duplex, eliminating the need for complex access control.
