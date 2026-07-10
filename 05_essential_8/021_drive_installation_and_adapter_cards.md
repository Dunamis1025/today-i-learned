# Computer Hardware Study Notes
## PC Assembly — Drives, Adapter Cards & Key Concepts

---

## 1. Chipset

The **chipset** is a set of integrated circuits on the motherboard that acts as a **traffic controller** between the CPU and all other components (RAM, GPU, storage, USB, etc.).

- **Role**: Manages data flow between components
- **Controls**: PCIe lanes, SATA/NVMe ports, USB ports
- **Determines**: Overclocking support, number of ports, compatibility
- **Modern trend**: Functions increasingly consolidated into fewer chips (or integrated into CPU)

| Vendor | Examples |
|--------|----------|
| Intel | Z890, B760, H610 |
| AMD | X870, B650, A620 |
| Mobile | Qualcomm Snapdragon, Apple A-series (SoC) |

> **One-liner**: CPU = brain; Chipset = traffic control system

---

## 2. Buffered vs. Unbuffered Memory

**Buffered (Registered) memory** has a built-in buffer chip between the RAM module and the memory controller, reducing electrical load and improving stability for high-capacity systems.

| Feature | Buffered (RDIMM/LRDIMM) | Unbuffered (UDIMM) |
|---------|------------------------|-------------------|
| Buffer chip | ✅ Yes | ❌ No |
| Stability | Very high | Standard |
| Max capacity | Very large | Limited |
| Latency | Slightly higher | Lower |
| Cost | Higher | Lower |
| Use case | Servers, workstations | Desktop PCs, laptops |

### Types
- **RDIMM** – Registered DIMM; most common buffered type
- **LRDIMM** – Load Reduced DIMM; extreme-capacity servers
- **UDIMM** – Unbuffered; standard consumer PCs

> **Why servers use buffered**: With dozens of RAM slots under load, the buffer absorbs electrical stress that would otherwise overwhelm the memory controller.

---

## 3. Installing Internal Drives

### 3.1 Hard Disk Drive (HDD)
1. Locate the **3.5-inch drive bay** inside the case
2. Slide the HDD in **from the inside** of the case
3. Align screw holes and fasten with appropriate screws

### 3.2 Optical Drive (CD/DVD)
1. Remove the **5.25-inch plastic faceplate** from the front of the case
2. Slide the optical drive in **from the front** of the case (tray must face outward)
3. Push until the front face is **flush** with the case panel
4. Align screw holes and secure

### Key Tips
- **Hand-tighten first**: Finger-tighten all screws before using a screwdriver to avoid cross-threading
- **Connectors face the rear**: Data and power connectors should face the back of the case toward the motherboard and PSU
- **Don't force it**: If screw holes don't align, reposition the drive; never force screws

---

## 4. Drive Interfaces

| Interface | Status | Used For |
|-----------|--------|----------|
| **IDE** | ❌ Obsolete | Old HDDs, optical drives |
| **SATA** | ✅ Current standard | HDD, SSD, optical drives |
| **NVMe (PCIe)** | ✅ High-performance | M.2 SSDs |

> **SATA** connects HDD, SSD, and optical drives — all three.  
> **IDE** is obsolete; modern motherboards no longer include it.

---

## 5. Adapter / Expansion Cards

Adapter cards (also called **expansion cards** or **add-on cards**) add or replace specific functionality on a computer by plugging into motherboard expansion slots.

### Common Types

| Card | Purpose |
|------|---------|
| **Graphics Card (GPU)** | Handles display output; required for 3D gaming, video editing |
| **Sound Card** | Improves audio quality and surround sound support |
| **Storage Controller (RAID)** | Adds drive bays; enables RAID for speed or redundancy |
| **I/O Card** | Adds USB or other ports when motherboard ports are insufficient |
| **NIC (Network Card)** | Adds Wi-Fi or increases network bandwidth |
| **Capture Card** | Records external video (TV tuner, game capture, etc.) |

### Installing an Adapter Card
1. **Identify** a compatible, empty expansion slot on the motherboard
2. **Remove** the metal slot cover on the back of the case (unscrew)
3. **Align** the card's connector with the slot
4. **Press firmly** until you hear/feel a **click** (fully seated)
5. **Secure** the card bracket to the case with a screw

---

## 6. Expansion Slots

| Slot | Status | Notes |
|------|--------|-------|
| **PCI** | Legacy | Older cards only |
| **PCIe x1** | Current | Short slot; sound cards, I/O cards, NICs |
| **PCIe x4** | Current | Mid-length; storage controllers |
| **PCIe x8** | Current | Mid-length; some GPUs, capture cards |
| **PCIe x16** | Current | Longest slot; graphics cards (primary) |
| **Mini PCIe** | Embedded | Wireless cards in desktop towers |

> Longer slot = more bandwidth. A smaller card (e.g., x1) **can** fit in a larger slot (e.g., x16), but not vice versa.

---

## 7. Key Vocabulary

| Term | Definition |
|------|-----------|
| **Cross-threading** | Forcing a screw in at the wrong angle, stripping the threads and making it impossible to remove cleanly |
| **Obsolete** | Technology no longer used as a standard (e.g., IDE, PCI) |
| **Flush** | When a surface is perfectly level/aligned with the surrounding panel |
| **ESD (Electrostatic Discharge)** | Static electricity that can silently damage sensitive components |
| **Drive Bay** | Designated slot inside the case for mounting storage or optical drives |
| **Slot Cover** | Metal bracket covering an unused expansion slot on the rear of the case |
| **RAID** | Redundant Array of Independent Disks — links multiple drives for speed or data protection |
| **Fault Tolerance** | System's ability to continue operating even if one component fails |

---

## 8. Safety Best Practices

- ⚡ **Wear an antistatic wrist strap** or touch a grounded metal object before handling any component
- 🔩 **Hand-tighten screws first**, then finish with a screwdriver
- 🚫 **Never force components** — if resistance is felt, check alignment
- 🌡️ **Prefer SSDs over HDDs** when CPU cooling is a concern (HDDs generate more heat)
- 📋 **Check the motherboard manual** for compatible slots and configurations before purchasing expansion cards

---

## 9. True / False Quick Review

| Statement | Answer |
|-----------|--------|
| Optical drives are installed from the front of the case | ✅ True |
| Hand-tightening screws before using a screwdriver is recommended | ✅ True |
| Modern motherboards use the IDE interface | ❌ False (SATA) |
| SATA works for HDD, SSD, and optical drives | ✅ True |
| HDDs are preferred when CPU cooling is important | ❌ False (SSDs run cooler) |
| Drive connectors should face the front of the case | ❌ False (face the rear) |

---

*Study notes compiled from PC assembly lab exercises and hardware configuration lectures.*
