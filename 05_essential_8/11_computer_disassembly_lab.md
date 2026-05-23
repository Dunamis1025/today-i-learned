# CCNA Chapter 1: Introduction to Personal Computer Hardware
> Study Notes — Cisco Networking Academy

---

## 📋 Overview

This chapter introduces the internal components of a personal computer, explains safety guidelines for working inside a computer, and walks through the process of physically disassembling one.

---

## ⚡ 1. Safety — ESD (Electrostatic Discharge)

- **ESD** is the "zap" of static electricity that can permanently damage sensitive computer components
- Always wear an **antistatic wrist strap** connected to an unpainted metal part of the case
- Use an **antistatic mat** under the computer during work
- Store removed components in **antistatic bags**

> ⚠️ ESD is invisible but can destroy circuits instantly — never skip grounding steps.

---

## 🔧 2. Recommended Tools

| Tool | Purpose |
|------|---------|
| Safety glasses | Eye protection |
| Antistatic wrist strap | ESD prevention |
| Antistatic mat | ESD prevention on work surface |
| Phillips / Flathead / Torx screwdrivers | Removing various screws |
| Hex driver | Hex-head screws |
| Part retriever | Picking up dropped screws |
| Parts organizer | Keeping screws sorted and labeled |
| Antistatic bags | Storing removed components safely |
| Can of compressed air | Dust removal |
| Thermal compound | CPU cooler reapplication |

---

## 🖥️ 3. Computer Case & Power Supply

### Case Types
- **Screwless** — Held by metal/plastic clips; open by pressing a button or switch
- **Screw** — Side panels secured with screws at the edges
- **Thumbscrew** — Hand-tightened screws; no screwdriver needed

> 💡 Always photograph the inside of the case before disassembly for reassembly reference.

### Power Supply (PSU)
- Acts as the **heart** of the computer — converts AC wall power to DC power for components
- Sends power through connectors: **SATA power**, **Molex**, **PCIe**, **24-pin ATX** (motherboard)
- Provides different voltages: typically **3.3V**, **5V**, and **12V**

---

## 🔌 4. Key Connectors & Interfaces

### Data Interfaces

| Interface | Description |
|-----------|-------------|
| **PATA** (Parallel ATA) | Legacy; wide ribbon cables; slow; rarely used today |
| **SATA** (Serial ATA) | Modern standard; thin cables; fast; used for HDDs and SSDs |

### Power Connectors

| Connector | Description |
|-----------|-------------|
| **Molex** | Older 4-pin connector; used for fans and legacy drives |
| **SATA Power** | Flat connector for modern HDDs and SSDs |
| **PCIe power** | Supplies power to graphics cards |

### Expansion Slots

| Slot | Description |
|------|-------------|
| **PCIe** (PCI Express) | High-speed slot for GPUs, NICs, sound cards — the modern standard |

---

## 🧠 5. Motherboard

The **backbone** of the computer — every component connects to or communicates through it.

### Key Components on the Motherboard

| Component | Role |
|-----------|------|
| **CPU** | The brain — processes all instructions |
| **RAM** | Short-term workspace — holds data currently in use |
| **Chipset** | Traffic controller between CPU and other components |
| **Expansion slots** | PCIe slots for add-in cards |
| **BIOS / UEFI chip** | Firmware that runs on boot before the OS loads |
| **Buses** | Electrical pathways connecting all components |

### BIOS vs. UEFI

| Feature | BIOS | UEFI |
|---------|------|------|
| Age | Legacy (1980s) | Modern replacement |
| Interface | Text-only | Graphical (mouse support) |
| Speed | Slow boot | Fast boot |
| Security | Limited | Secure Boot support |
| Drive size support | Up to 2TB | 2TB+ (GPT) |

> UEFI is the standard in all modern computers.

---

## 💾 6. Storage Devices

| Type | Description |
|------|-------------|
| **HDD** (Hard Disk Drive) | Mechanical; spinning platters; slower but affordable |
| **SSD** (Solid State Drive) | Flash memory; fast; no moving parts |
| **Optical Drive** | Reads/writes CDs, DVDs, Blu-rays |

**Interfaces used:** PATA (legacy) → SATA (current standard)

---

## 🛠️ 7. Disassembly Lab — Step-by-Step

> ⚠️ Motherboard, CPU, and cooling device are **not removed** in this lab due to replacement cost.

### Part 1: Preparation

1. **Power off** — Unplug from wall and PSU
2. **Remove peripherals** — Monitor, keyboard, Ethernet cables, etc.
3. **Open the case** — Using the appropriate method (screwless / screw / thumbscrew)
4. **Wear antistatic wrist strap** — Clip to unpainted metal on the case

### Part 2: Parts Removal (in order)

| Step | Component | Key Notes |
|------|-----------|-----------|
| 1 | **Hard Drive** | Disconnect power + data cables; check jumper (Master/Slave/CS); store in antistatic bag |
| 2 | **Optical Drive** | Disconnect power, data, and audio cables; remove screws |
| 3 | **Power Supply** | Unplug all connectors (motherboard, fans, GPU); remove 4 rear screws |
| 4 | **Adapter Cards** | Remove bracket screw; release locking tab on slot (especially GPUs); store in antistatic bag |
| 5 | **Memory (RAM)** | Press locking tabs on both ends of slot; lift straight out; store in antistatic bag |
| 6 | **Data Cables** | Note connection locations before removing; label if needed |

---

## 📝 Key Takeaways

- ESD is the #1 risk when working inside a computer — always ground yourself
- The **motherboard** connects everything; the **PSU** powers everything
- **SATA** replaced **PATA** as the modern data interface standard
- **UEFI** replaced **BIOS** as the modern boot firmware
- Label and photograph everything before disassembly — reassembly will thank you

---

*Source: Cisco Networking Academy — IT Essentials, Chapter 1*
