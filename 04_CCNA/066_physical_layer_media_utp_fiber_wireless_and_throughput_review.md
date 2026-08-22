# Network Fundamentals – Study Notes

## Q1. UTP Cable Interference Factors
**Two factors that interfere with UTP cable communication (excluding cable length):**

- **Crosstalk** – Electrical signals from one wire "bleed" into adjacent wires, corrupting data. Similar to hearing someone else's conversation on a phone line.
- **Electromagnetic Interference (EMI)** – External electromagnetic noise from motors, power lines, or fluorescent lights distorts the signal inside the cable.

---

## Q2. Characteristics of Fiber-Optic Cable
**Two key characteristics:**

- **More expensive than UTP** – Requires precision glass fiber materials and specialized equipment to convert electricity into light signals.
- **Not affected by EMI or RFI** – Transmits data using light (not electricity), making it completely immune to electromagnetic and radio frequency interference.

---

## Q3. Devices That Commonly Affect Wireless Networks
**Two devices that interfere with Wi-Fi (2.4 GHz band):**

- **Microwaves** – Emit electromagnetic waves at the same 2.4 GHz frequency as Wi-Fi, causing significant temporary interference.
- **Cordless phones** – Older models operate on the 2.4 GHz band and compete with Wi-Fi signals, degrading connection quality.

---

## Q4. Factors That Reduce Network Throughput vs. Bandwidth
> **Bandwidth** = maximum speed limit / **Throughput** = actual speed

**Three factors that lower throughput below expected bandwidth:**

- **Type of traffic** – Complex or high-overhead data types consume more processing resources, slowing effective throughput.
- **Amount of traffic** – Network congestion (too many simultaneous users/apps) causes data to queue, reducing actual speed.
- **Latency from network devices** – Each router or switch a packet passes through adds processing delay; more hops = more cumulative latency.

---

## Q5. Primary Role of the Physical Layer
**The Physical Layer (OSI Layer 1):**

- Converts digital bits (0s and 1s) into **physical signals** — electrical voltages, light pulses, or radio waves — that travel across the medium (cable, fiber, or air).
- Key function: **"Create the signals that represent the bits in each frame onto the media."**

---

## Q6. Identifying Cable Types by Connector
- An **ST (Straight Tip) connector** with a white ceramic **ferrule** at the center → **Fiber-optic cable**
- The ferrule aligns and protects the thin glass fiber core that transmits data via pulses of light.
- Unlike UTP (metal pins) or coax cables, fiber connectors mate glass strands to minimize light loss.

> 💡 **Ferrule** = the small metal/ceramic ring or cap at the tip of a fiber connector that protects and aligns the glass fiber.

---

## Q7. Data Link Layer During Encapsulation
**Encapsulation** = wrapping data in "envelopes" at each OSI layer as it moves down the stack.

- **Data Link Layer (Layer 2)** adds the **physical address (MAC address)** to the data frame.
- MAC address = a unique, permanent identifier burned into the device's Network Interface Card (NIC).
- Note: IP addresses (logical addresses) are handled at the **Network Layer (Layer 3)**, not here.

---

## Key Terms Summary

| Term | Definition |
|------|-----------|
| **Crosstalk** | Signal interference between adjacent wires |
| **EMI** | Electromagnetic interference from external devices |
| **Bandwidth** | Maximum theoretical data transfer rate |
| **Throughput** | Actual data transfer rate in real conditions |
| **Latency** | Delay caused by processing time at each network device |
| **Ferrule** | Protective tip/ring on a fiber-optic connector |
| **MAC Address** | Physical hardware address unique to each NIC |
| **Encapsulation** | Process of wrapping data with headers at each OSI layer |
| **Physical Layer** | OSI Layer 1 — converts bits into physical signals |
| **Data Link Layer** | OSI Layer 2 — handles MAC addressing and local delivery |
