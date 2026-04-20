# Today I Learned: Data Link Layer Sublayers and Router Functions

## 1. Data Link Sublayers (LLC & MAC)
The Data Link Layer (Layer 2) is divided into two distinct sublayers to handle software-level logic and hardware-level media access separately.

### LLC (Logical Link Control) Sublayer
- **Role:** Acts as an interface between the network software (Layer 3) and the device hardware.
- **Functions:**
    - Identifies the Network Layer protocol (IPv4 or IPv6) being used.
    - Adds Layer 2 control information to help deliver the packet to the destination.

### MAC (Media Access Control) Sublayer
- **Role:** Responsible for data encapsulation and controlling the hardware (NIC) that sends/receives data.
- **Key Functions:**
    - **Frame Delimiting:** Identifies bits that mark the start and end of a frame for synchronization.
    - **Addressing:** Adds source and destination MAC addresses to ensure delivery within the local network.
    - **Error Detection:** Includes a trailer (FCS) to check if the data was corrupted during transmission.
    - **Media Access Control:** Manages how frames are placed on the media, especially in shared (half-duplex) environments.

## 2. Router Functions at Layer 2
When a router receives a packet, it must transition it across different media types. This involves a constant cycle of re-encapsulation:

1. **Accepts a frame** from the physical medium (e.g., Ethernet cable).
2. **De-encapsulates the frame** to expose the Layer 3 packet.
3. **Determines the next path** (Layer 3 function).
4. **Re-encapsulates the packet into a new frame** that matches the technology of the exit interface (e.g., from Ethernet to a Serial link).
5. **Forwards the new frame** onto the next segment of the network.

## 3. Standards Organizations
Unlike upper layers which are defined by IETF (RFCs), the lower layers (Physical and Data Link) are defined by engineering organizations that specialize in hardware and electronics:
- **IEEE (Institute of Electrical and Electronics Engineers):** Defines Ethernet (802.3) and Wi-Fi (802.11) standards.
- **ITU / ISO / ANSI:** Develop international standards for telecommunications and data transmission.

## 4. Key Concept Review
- **Media Access Control Method:** The method used depends on the **Topology** (how nodes are connected) and **Media Sharing** (whether the path is shared or point-to-point).
- **Full-Duplex vs. Half-Duplex:** Full-duplex does not require access control as devices can send and receive simultaneously without collisions.
- **Standardization:** IEEE is the primary organization responsible for defining Layer 1 and Layer 2 standards used in LAN/WAN access.
