# 🖥️ CompTIA A+ / IT Hardware Study Notes
## Topic: Motherboards & Components
> Certificate IV in Cybersecurity — Hardware Module

---

## Table of Contents
1. [1.2.2.1 Motherboards Overview](#1221-motherboards-overview)
2. [1.2.2.2 Motherboard Connectors & Interfaces](#1222-motherboard-connectors--interfaces)
   - [SATA](#sata-serial-advanced-technology-attachment)
   - [IDE](#ide-integrated-drive-electronics)
   - [Internal USB](#internal-usb)
3. [1.2.2.3 Motherboard Chipset](#1223-motherboard-chipset)
4. [1.2.2.4 Motherboard Form Factors](#1224-motherboard-form-factors)

---

## 1.2.2.1 Motherboards Overview

### What is a Motherboard?
The **motherboard** (also called *system board* or *main board*) is the **backbone of a computer**. It is a **Printed Circuit Board (PCB)** that physically and electrically connects all components of a computer system.

### Key Characteristics
- Contains **buses** (electrical pathways) that allow components to communicate with each other
- Components can be:
  - **Directly soldered** onto the board (permanent)
  - **Plugged in** via sockets, expansion slots, or ports (removable/upgradeable)

### Core Components on a Motherboard

| Component | Description |
|-----------|-------------|
| **CPU (Central Processing Unit)** | The "brain" of the computer — processes all instructions |
| **RAM (Random Access Memory)** | Temporary storage for data and running applications |
| **Expansion Slots** | Slots to add additional cards (GPU, sound card, network card, etc.) |
| **Chipset** | Integrated circuits that control how hardware interacts with the CPU |
| **BIOS / UEFI Chip** | Firmware that boots the computer and manages hardware communication |

### BIOS vs UEFI

| Feature | BIOS | UEFI |
|--------|------|------|
| Full Name | Basic Input/Output System | Unified Extensible Firmware Interface |
| Era | Older / legacy | Modern replacement for BIOS |
| Function | Boots the computer; manages data flow between hardware | Same as BIOS but with advanced features |
| Interface | Text-based | Graphical UI support |
| Drive support | Up to 2TB (MBR) | 2TB+ support (GPT) |

> **Firmware** = Programming code that allows the OS to control hardware.

---

## 1.2.2.2 Motherboard Connectors & Interfaces

### SATA (Serial Advanced Technology Attachment)

**Purpose:** Connects storage devices to the motherboard.

**Supported Devices:**
- Hard Disk Drives (HDD)
- Solid State Drives (SSD)
- Optical Drives (CD/DVD)

**Key Feature — Hot Swapping:**
> SATA supports **hot swapping** — the ability to connect or disconnect a device **while the computer is still powered on**, without needing to reboot.

**SATA Generations:**

| Version | Max Speed |
|---------|-----------|
| SATA I | 1.5 Gb/s |
| SATA II | 3.0 Gb/s |
| SATA III | 6.0 Gb/s |

---

### IDE (Integrated Drive Electronics)

**Purpose:** An **older** standard interface for connecting disk drives to the motherboard.

**Key Characteristics:**
- Uses a **40-pin connector** (wide, flat ribbon cable)
- Each IDE interface supports a maximum of **2 devices**
- Predecessor to SATA — largely obsolete in modern systems

> **Note for Cybersecurity:** IDE is still relevant in **digital forensics** when dealing with older hard drives and legacy hardware.

**IDE vs SATA Comparison:**

| Feature | IDE | SATA |
|---------|-----|------|
| Connector | 40-pin wide ribbon | Thin 7-pin cable |
| Max devices per port | 2 | 1 |
| Hot swap support | ❌ No | ✅ Yes |
| Speed | Slow (up to 133 MB/s) | Fast (up to 600 MB/s) |
| Status | Legacy / obsolete | Current standard |

---

### Internal USB

**Purpose:** Connects external-facing USB ports (on the computer case) to the motherboard internally.

**How it works:**
```
Case USB Port ←→ Internal cable ←→ Motherboard header
```

**Pin Configurations:**

| USB Version | Pin Count |
|-------------|-----------|
| USB 1.1 / 2.0 | 9 pins |
| USB 3.0 / 3.1 | 19 pins |

> More pins = faster data transfer speeds. USB 3.x headers are not backward-compatible with USB 2.0 headers physically.

---

## 1.2.2.3 Motherboard Chipset

### What is a Chipset?
The chipset acts as a **traffic controller** on the motherboard — it manages communication between the CPU and all other components.

Most chipsets consist of **two main chips**:

---

### Northbridge
Controls **high-speed** components that need fast access:

- **RAM** — direct memory access
- **GPU / Video Card** — via PCI Express slot
- Controls the **speed of CPU communication** with other components
- Video capability is sometimes **integrated into the Northbridge**

---

### Southbridge
Handles **slower-speed** devices and peripherals:

- Hard Drives (storage)
- USB ports
- Keyboard & Mouse
- BIOS / UEFI chip
- PCI expansion slots (32-bit and 64-bit)

---

### Chipset Architecture Diagram

```
                    ┌──────────────────────┐
                    │         CPU          │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
         ┌──────────│     NORTHBRIDGE      │──────────┐
         │          └──────────┬───────────┘          │
         │                     │                       │
   ┌─────▼─────┐    ┌──────────▼───────────┐   ┌──────▼──────┐
   │    RAM    │    │     SOUTHBRIDGE       │   │  PCIe GPU   │
   │  (x4)     │    └──┬────────┬───────┬──┘   │    Slot     │
   └───────────┘       │        │       │       └─────────────┘
                   ┌───▼──┐ ┌──▼──┐ ┌──▼──────────┐
                   │ HDD  │ │ USB │ │ BIOS / PCI  │
                   │      │ │ KB  │ │   Slots     │
                   └──────┘ └─────┘ └─────────────┘
```

---

## 1.2.2.4 Motherboard Form Factors

### What is a Form Factor?
A **form factor** defines the **physical size, shape, and layout** of a motherboard — including where components are placed, what case it fits in, and what power supply it requires.

> ⚠️ **Important:** The form factor determines which **case**, **power supply**, and **components** are compatible. Always match them correctly when building or upgrading a PC.

---

### The Three Main Form Factors

#### 1. ATX (Advanced Technology eXtended)
- **Most common** and widely used
- Size: **30.5 cm × 24.4 cm** (12" × 9.6")
- Power supply connects via a **single 20-pin connector**
- Plenty of expansion slots — ideal for **full-sized desktop PCs and gaming builds**

#### 2. Micro-ATX
- Smaller than ATX but **backward-compatible** with ATX cases
- Size: **24.4 cm × 24.4 cm** (9.6" × 9.6")
- Uses the same Northbridge/Southbridge chipsets as ATX
- **Fewer expansion slots** than full ATX
- Popular in **standard desktops and small form factor PCs**

#### 3. ITX / Mini-ITX
- Designed for **very small devices**
- **Mini-ITX size:** 17 cm × 17 cm (6.7" × 6.7")
- Uses very **little power** — often no cooling fan required
- Only **1 PCI expansion slot**
- Used in: thin clients, set-top boxes, HTPCs, embedded systems
- Great for **quiet or compact environments**

---

### Form Factor Comparison Table

| Form Factor | Size | Expansion Slots | Best For |
|-------------|------|-----------------|----------|
| **ATX** | 30.5 × 24.4 cm | Many | High-performance desktops, gaming |
| **Micro-ATX** | 24.4 × 24.4 cm | Fewer | Standard desktops, budget builds |
| **ITX** | 21.5 × 19.1 cm | Limited | Compact PCs |
| **Mini-ITX** | 17 × 17 cm | 1 only | Ultra-compact, low-power devices |

> **Note:** Some manufacturers use **proprietary form factors** based on ATX design, which can cause incompatibility with standard cases and power supplies.

---

## 📝 Quick Review Summary

| Topic | Key Takeaway |
|-------|-------------|
| Motherboard | Backbone/PCB of a computer; connects all components via buses |
| BIOS | Older firmware; boots PC and manages hardware |
| UEFI | Modern BIOS replacement; supports larger drives and GUI |
| SATA | Current storage connector; supports hot swapping |
| IDE | Legacy 40-pin storage connector; max 2 devices per port |
| Internal USB | Connects case USB ports to the motherboard (9-pin or 19-pin) |
| Northbridge | Manages fast components: RAM and GPU |
| Southbridge | Manages slow components: HDD, USB, keyboard |
| ATX | Standard full-size motherboard form factor |
| Micro-ATX | Smaller, ATX-compatible form factor |
| Mini-ITX | Ultra-compact, low-power form factor |

---

*Study notes compiled for Certificate IV in Cybersecurity — Hardware & IT Fundamentals module.*
