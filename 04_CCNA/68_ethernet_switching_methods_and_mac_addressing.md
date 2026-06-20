# Data Link Layer & Ethernet Switching — Study Notes

> Topics: Media Access Control, WAN topologies, frame structure, switching methods, MAC addressing, cabling, and physical layer concepts.

---

## 1. Media Access Control (MAC)

Media Access Control governs **how and when devices place data onto a shared medium** (cable, wireless, etc.).

**Key facts:**
- MAC provides the **placement of data frames onto the media**.
- The **data link layer** defines the rules for accessing different types of media.
- **Ethernet** uses **CSMA/CD** (Carrier Sense Multiple Access with Collision Detection) — devices check if the line is free before sending, and retransmit if a collision occurs.
- **802.11 (Wi-Fi)** uses **CSMA/CA** (Collision **Avoidance**), not CSMA/CD, because wireless collisions are hard to detect directly.
- **Contention-based access** (like CSMA/CD) is **non-deterministic** — devices send whenever they're ready, risking collisions.
- **Controlled access** networks use a fixed order/turn-taking, which **prevents/reduces collisions** (more predictable, but less flexible).

---

## 2. WAN Topologies

Comparing physical WAN topologies for connecting a headquarters to remote sites:

| Topology | Description | Availability |
|---|---|---|
| **Partial Mesh** ✅ | Some sites are directly interconnected; not all sites connect to all others | High availability for critical links, without full-mesh cost |
| Full Mesh | Every site connects to every other site | Highest availability, but expensive/complex |
| Hub and Spoke | All remote sites connect to one central hub | Low resilience — hub failure breaks everything |
| Point-to-Point | Direct link between exactly two nodes | Not suitable for multi-site connectivity |

**Answer for "high availability + connects only some remote sites":** **Partial Mesh**

---

## 3. Frame Structure (Data Link Layer)

Every frame type has **3 basic parts**:

1. **Header** — contains control info (source/destination addresses) needed to deliver the frame.
2. **Data** — the actual payload (e.g., an encapsulated IP packet).
3. **Trailer** — used for **error detection** (e.g., FCS) to confirm the data wasn't corrupted in transit.

> Note: "Type field" and "CRC value" are sub-components *within* the header/trailer, not separate top-level parts. "MTU size" is a size limit setting, not a structural part of the frame.

---

## 4. Ethernet Header & Trailer Fields

The Ethernet frame's header/trailer contain:
- **Destination MAC address** — physical address of the receiving device.
- **Source MAC address** — physical address of the sending device.
- **Error-checking info (FCS)** — in the trailer, used to verify the frame wasn't corrupted.

> IP addresses (source/destination) are **NOT** part of the Ethernet header — they belong to Layer 3 and are carried *inside* the data/payload portion of the frame.

---

## 5. Switching Methods Comparison

| Method | When it forwards | Error checking | Latency | Notes |
|---|---|---|---|---|
| **Store-and-Forward** | After receiving the **entire** frame | ✅ Full CRC check | Highest | Most reliable; drops corrupted frames |
| **Cut-through** | As soon as destination MAC is read | ❌ No check | Low | May forward corrupted frames |
| **Fast-forward** | Immediately after dest. MAC is read (a cut-through variant) | ❌ None | **Lowest** | Prioritizes pure speed |
| **Fragment-free** | After checking first 64 bytes (collision window) | Partial | Medium | Middle ground between speed and reliability |

**Key takeaways:**
- **Cut-through** advantage over store-and-forward: **lower latency**, good for high-performance computing.
- **Store-and-forward** advantage over cut-through: **frame error checking** (via CRC/FCS comparison).
- The switching method that uses the **CRC value** to check for errors = **Store-and-forward**.
- The method with the **absolute lowest latency** = **Fast-forward**.
- Switching decisions are always based on the **destination** MAC address (not source).

---

## 6. Auto-MDIX

**Auto-MDIX (Automatic Medium-Dependent Interface Crossover):**
- Allows a device to **automatically detect and configure** itself for whichever cable type is plugged in (straight-through or crossover) — no manual cable-matching needed.
- **Not** related to duplex or speed settings (those are handled by **Auto-negotiation**, a separate feature).
- **Not** related to forwarding/switching logic (cut-through vs. store-and-forward).

---

## 7. FCS (Frame Check Sequence)

- **Purpose:** Detect whether errors occurred during transmission/reception.
- **How it works:**
  1. Sender calculates a CRC value over the frame contents → places it in the FCS field.
  2. Receiver performs the same calculation on the received frame.
  3. If the two values **match** → frame is good. If they **don't match** → frame is corrupted and **discarded**.
- FCS checks **data integrity only** — it does NOT verify MAC/IP addresses or perform routing.

---

## 8. MAC Address Types

| Address | Type | Example |
|---|---|---|
| `01-00-5E-xx-xx-xx` | **Multicast** | Sends to a specific group of devices |
| `FF-FF-FF-FF-FF-FF` | **Broadcast** | Sends to every device on the local segment |
| Any other fixed address (e.g., `00-26-0F-4B-00-3E`) | **Unicast** | Unique address of a single device's NIC |

---

## 9. Cisco Switch Core Behaviors

A Layer 2 switch performs two main actions:

1. **Learning** — uses the **source MAC address** of incoming frames to build/maintain its MAC address table (records which device is on which port).
2. **Forwarding** — uses the **destination MAC address** to look up the table and send the frame out only the correct port.

> Switches are Layer 2 devices — they do **not** handle IP addresses or routing tables (that's a router's/Layer 3 device's job).

### Practical Lab Tip (Packet Tracer style)
- `show mac address-table` on a switch only shows entries for devices the switch has **already seen traffic from**.
- If the table is empty, you need to **generate traffic first** — e.g., `ping <destination-IP>` from the **PC's Command Prompt** (not from the switch terminal — switches generally can't initiate pings themselves as Layer 2 devices).
- A failed ping (`Success rate is 0 percent`) means **no reply was received** — check IP configuration, port status (`up`/`down`), and that commands are being run from the correct device.

---

## 10. Memory Buffering Methods

| Method | Description | Best for |
|---|---|---|
| **Shared Memory Buffering** ✅ | All ports draw from one common memory pool; allocated dynamically | Connecting ports with **different speeds** (e.g., 1000 Mbps → 100 Mbps) — prevents overflow/drops |
| Port-based Buffering | Fixed memory per port | Can overflow easily when speeds mismatch |

---

## 11. Multi-Hop MAC Address Behavior

When data crosses **multiple networks** (separated by routers), the **destination MAC address changes at every hop**:

- It is **never** the final destination host's MAC address until the **last hop**.
- At each hop, the frame is addressed to the **next-hop device's interface** (e.g., the local gateway/router).
- Example: Web Server → Router (Fa0/0) → ... → PC1
  - Leaving the web server, destination MAC = the **router's interface MAC**, not PC1's.
  - Only after the router forwards the data onto PC1's network does the destination MAC become PC1's actual MAC address.

---

## 12. Cabling — Termination & UTP Standards

### Common termination error
- **Untwisted wire length too long**: when terminating a connector, leaving too much wire untwisted near the connector exposes that section to **crosstalk/EMI**, degrading signal quality and causing data errors.
- **Correct technique:** maintain the twist as close to the connector as physically possible.

### UTP Cable Types (traditional standard)
| Connection | Cable Type |
|---|---|
| PC ↔ Console port (device management) | **Rollover** |
| Switch ↔ Router (legacy standard) | **Crossover** |
| Router ↔ Router / differing device types | **Straight-through** |

> Note: Modern devices with Auto-MDIX auto-detect cable type, but exams typically test the traditional/textbook standard.

---

## 13. Fiber vs. Copper Cabling (Building Interconnects)

**Why fiber is preferred for inter-building links (3 reasons):**
1. **Limited susceptibility to EMI/RFI** — uses light, not electricity, so immune to electromagnetic/radio interference.
2. **Greater bandwidth potential** — can carry much more data at higher speeds.
3. **Greater distances per cable run** — very low signal loss (attenuation), so it can run much farther without repeaters.

**Why these are NOT advantages of fiber:**
- "Easily terminated" — fiber termination is actually **more difficult/precise** than copper.
- "Lower installation cost" — fiber is generally **more expensive** to install.
- "Durable connections" — the glass core is **more fragile** physically than copper.

---

## 14. Physical Layer Term: Latency

- **Latency** = the total time (including delays) for data to travel from source to destination.
- This is distinct from the **transmission media** itself (air, fiber-optic cable, copper cable), which are just the physical paths data travels through — not time measurements.

---

## 15. MAC Sublayer (within Data Link Layer)

The Data Link Layer splits into two sublayers:

| Sublayer | Role |
|---|---|
| **MAC (Media Access Control)** | "Hardware manager" — controls the NIC; provides a mechanism for multiple devices to share a medium without conflict |
| **LLC (Logical Link Control)** | "Translator" — communicates between upper-layer network software (e.g., IP) and lower-layer hardware; identifies which Layer 3 protocol is in use |

**MAC sublayer's two key functions:**
1. Provides a mechanism allowing multiple devices to communicate over a **shared medium**.
2. **Controls the NIC** responsible for sending/receiving data on the physical medium.

---

## 16. Frame Handling at the Receiving Host

If a host receives a frame whose **destination MAC address doesn't match its own**:
- The host **discards** the frame immediately.
- This prevents wasted CPU/memory resources processing data intended for another device.
- (Exception: broadcast/multicast addresses the host is listening for are still processed.)

---

## Quick Reference Summary

- **CSMA/CD** → Ethernet | **CSMA/CA** → Wi-Fi
- **Partial mesh** → high availability, connects *some* sites
- Frame = **Header + Data + Trailer**
- Ethernet header/trailer = **Dest MAC + Source MAC + FCS** (no IP info)
- **Store-and-forward** = reliable, full CRC check, highest latency
- **Cut-through / Fast-forward** = fast, no/partial error check
- **Auto-MDIX** = auto-detects cable type (not speed/duplex)
- **FCS** = error detection only, via CRC comparison
- **01-00-5E...** = multicast | **FF-FF-FF-FF-FF-FF** = broadcast
- Switch: **learns** via source MAC, **forwards** via destination MAC
- **Shared memory buffering** = best for mismatched port speeds
- Destination MAC **changes at every router hop**
- **Untwisted wire too long** = common termination defect (crosstalk risk)
- **Rollover** = PC-to-console | **Crossover** = switch-to-router (legacy) | **Straight-through** = router-to-router
- Fiber advantages: **EMI immunity, bandwidth, distance** (not cost or ease of termination)
- **Latency** = total transit time
- **MAC sublayer** = shared-medium access + NIC control; **LLC sublayer** = software/hardware translation
