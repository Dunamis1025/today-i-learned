# 07. Adapter Cards and Expansion Slots

## 1.2.7.1 Adapter Cards

Adapter cards increase the functionality of a computer by adding controllers for specific devices or by replacing malfunctioning ports. There are a variety of adapter cards available that are used to expand and customize the capability of a computer.

### Types of Adapter Cards

#### 1. Sound Adapter
- **Function:** Provides audio capability to a computer.
- **Details:** Handles all audio input and output, including music playback, sound effects, and microphone input. Features color-coded audio jacks (e.g., green for speakers, blue for line-in, pink for microphone).

#### 2. Network Interface Card (NIC)
- **Function:** Connects a computer to a network using a network cable.
- **Details:** Provides a physical Ethernet port (RJ-45) to plug in a LAN cable, enabling wired internet or local network connectivity.

#### 3. eSATA Card
- **Function:** Adds additional internal and external SATA ports to a computer through a single PCI Express slot.
- **Details:** Allows connection of additional SATA storage devices (HDDs, SSDs) both inside and outside the computer chassis.

#### 4. Video Adapter (Graphics Card / GPU)
- **Function:** Provides video capability to a computer.
- **Details:** Renders and outputs video signals to a monitor. Critical for gaming, video editing, and any GPU-intensive workloads. Also known as a graphics card or GPU (Graphics Processing Unit).

---

## 1.2.7.2 Other Adapter Cards

The following are additional adapter cards that expand computer functionality:

#### 1. Wireless NIC
- **Function:** Connects a computer to a network using radio frequencies (wireless).
- **Details:** The wireless version of a NIC. Eliminates the need for a physical cable by using Wi-Fi signals. Commonly integrated into modern laptops by default.

#### 2. Capture Card
- **Function:** Sends a video signal to a computer so that the signal can be recorded to a storage drive using video capture software.
- **Details:** Commonly used by streamers and content creators to capture footage from external devices such as gaming consoles or cameras.

#### 3. TV Tuner Card
- **Function:** Provides the ability to watch and record television signals on a PC.
- **Details:** Works by connecting a cable TV, satellite, or antenna to the installed tuner card. Allows a PC to function as a television without a separate TV set.

#### 4. Universal Serial Bus (USB) Controller Card
- **Function:** Provides additional USB ports to connect the computer to peripheral devices.
- **Details:** Useful when the onboard USB ports are insufficient. Acts like a USB hub integrated directly into the motherboard via an expansion slot.

> **Note:**
> - Some of these adapter cards can be **integrated directly on the motherboard** (onboard).
> - Older computers may also have a **modem adapter**, **Accelerated Graphics Port (AGP)**, a **Small Computer System Interface (SCSI)** adapter, and more.

---

## 1.2.7.3 Expansion Slots

Computers have expansion slots on the motherboard to install adapter cards. **The type of adapter card connector must match the expansion slot** — they are not interchangeable.

### Types of Expansion Slots

#### 1. PCI (Peripheral Component Interconnect)
- **Bus width:** 32-bit or 64-bit
- **Status:** ❌ Mostly obsolete
- **Details:** One of the earliest standard expansion slots. Found in very few modern computers. Has been superseded by newer technologies.

#### 2. Mini-PCI
- **Status:** Limited use (legacy laptops)
- **Details:** A smaller version of PCI designed for use in laptops. Comes in three different form factors:
  - Type I
  - Type II
  - Type III

#### 3. PCI-X (PCI eXtended)
- **Bus width:** 32-bit
- **Status:** ❌ Mostly obsolete
- **Details:** An updated version of the standard PCI. Uses a 32-bit bus with higher bandwidth than PCI. Can operate up to **4x faster** than standard PCI. Has been superseded by PCIe.

#### 4. Riser Card
- **Status:** ✅ Still in use (servers, mining rigs, compact builds)
- **Details:** A card that can be added to a computer to provide **additional expansion slots** for more expansion cards. Functions similarly to a power strip — one slot becomes multiple slots.

#### 5. PCIe (PCI Express) ⭐ Current Standard
- **Interface:** 64-bit parallel, backward compatible with 32-bit PCI devices
- **Status:** ✅ Current industry standard
- **Details:** Designed to supersede both PCI and PCI-X. Uses a **serial point-to-point connection**, offering much higher bandwidth. Comes in four sizes (lane counts):

| Slot Type     | Data Lanes | Common Use Case              |
|---------------|------------|------------------------------|
| PCIe x1       | 1 lane     | Small cards (sound, USB)     |
| PCIe x4       | 4 lanes    | Mid-range cards              |
| PCIe x8       | 8 lanes    | High-performance cards       |
| PCIe x16      | 16 lanes   | Graphics cards (GPUs)        |

> The higher the lane count, the greater the data throughput.

#### 6. AGP (Accelerated Graphics Port)
- **Status:** ❌ Obsolete
- **Details:** A high-speed slot specifically designed for attaching AGP video cards. Has been **superseded by PCI**. Very few motherboards still use this technology today.

---

## Summary Table

| Slot Type  | Bit Width | Speed      | Status         | Common Use              |
|------------|-----------|------------|----------------|-------------------------|
| PCI        | 32/64-bit | Slow       | ❌ Obsolete    | Legacy cards            |
| Mini-PCI   | —         | Slow       | ❌ Legacy      | Old laptops             |
| PCI-X      | 32-bit    | 4x PCI     | ❌ Obsolete    | Old servers             |
| AGP        | —         | High       | ❌ Obsolete    | Old GPU cards           |
| Riser Card | —         | Varies     | ✅ In use      | Slot expansion          |
| PCIe       | 64-bit    | Very High  | ✅ Standard    | GPUs, NICs, all modern cards |

## Evolution Timeline

```
Oldest ◄─────────────────────────────────────────► Newest
  AGP → PCI → Mini-PCI → PCI-X → PCIe (current standard)
                                    └── x1 / x4 / x8 / x16
```

> **Key Takeaway:** Modern computers almost exclusively use **PCIe** expansion slots. When building or upgrading a PC, always verify that the adapter card's connector type matches the available expansion slot on the motherboard.
