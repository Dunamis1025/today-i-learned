# Chapter 3 – Advanced Computer Hardware: Study Notes

---

## Lab: Research a Hardware Upgrade

### Background
The goal of this lab is to upgrade a computer with the following current specs to support **advanced video gaming**:

| Component | Current Spec |
|---|---|
| RAM | 2 GB (1 module) |
| Storage | 500 GB HDD |
| Video Adapter | PCIe, 256 MB VRAM |

---

### Step 1: RAM Upgrade

**What is RAM?**
RAM (Random Access Memory) is the computer's short-term workspace. The more RAM you have, the more programs and game data can run simultaneously without slowdowns.

**Target:** Two 8 GB DDR3 modules

**Research Table (Example):**

| Brand & Model | Features | Cost |
|---|---|---|
| *(e.g., Corsair Vengeance 8GB DDR3-1600)* | 1600 MHz, CL9, 1.5V | ~$XX |
| *(e.g., Kingston HyperX Fury 8GB DDR3-1866)* | 1866 MHz, auto-overclocking, low profile | ~$XX |

**Selection Criteria:**
- Match the **DDR generation** (DDR3) supported by the motherboard
- Check maximum supported **frequency (MHz)**
- Consider **dual-channel compatibility** for better performance
- Balance **price vs. speed**

---

### Step 2: Hard Disk Drive (Storage) Upgrade

**What is a Hard Drive?**
Storage holds all your files, games, and the operating system permanently — even when the power is off.

**Two types to consider:**

| Type | Capacity | Speed | Best For |
|---|---|---|---|
| HDD (Hard Disk Drive) | 3 TB | ~7200 RPM | Large game libraries, bulk storage |
| SSD (Solid State Drive) | 500 GB – 1 TB | Much faster (no moving parts) | OS, frequently played games, faster load times |

**Research Table (Example):**

| Brand & Model | Features | Cost |
|---|---|---|
| *(e.g., Seagate Barracuda 3TB HDD)* | 7200 RPM, SATA 3, 256MB cache | ~$XX |
| *(e.g., Samsung 870 EVO 1TB SSD)* | SATA 3, up to 560MB/s read, V-NAND | ~$XX |

**Selection Criteria:**
- HDD for **high-capacity storage** at lower cost
- SSD for **speed** — dramatically reduces game load times
- Ideal setup: **SSD for OS + key games**, HDD for bulk storage
- Verify **SATA 3 compatibility** with the motherboard

---

### Step 3: Video Adapter Card (GPU) Upgrade

**What is a Video Adapter Card (GPU)?**
The GPU (Graphics Processing Unit) is the most critical component for gaming. It renders all the visuals on screen — textures, lighting, shadows, and frame rates.

**Target:** PCIe card with at least 1 GB VRAM

**Research Table (Example):**

| Brand & Model | Features | Cost |
|---|---|---|
| *(e.g., NVIDIA GeForce GTX 1650 4GB)* | PCIe 3.0, 4GB GDDR5, DirectX 12 | ~$XX |
| *(e.g., AMD Radeon RX 570 4GB)* | PCIe 3.0, 4GB GDDR5, Vulkan support | ~$XX |

**Selection Criteria:**
- Minimum **1 GB VRAM** (more is better for modern games)
- Ensure the **PCIe slot** on the motherboard matches
- Check if the **Power Supply Unit (PSU)** can handle the card's wattage
- Consider **driver support**, **DirectX version**, and **resolution support**

---

### Key Decision Factors (Applies to All Components)

| Factor | Why It Matters |
|---|---|
| **Compatibility** | Parts must physically and electronically fit your existing motherboard |
| **Power Requirements** | Upgraded parts may draw more power; the PSU must be able to handle it |
| **Performance vs. Budget** | Focus upgrades on parts that give the biggest gaming performance gain |

---

## 3.5.1.1 – Safe Disposal of Computer Components

When replacing hardware, old components **cannot be thrown into regular trash**. Improper disposal is both **environmentally harmful and potentially illegal**.

### Disposal Guidelines by Component

| Component | Reason for Special Disposal | Correct Method |
|---|---|---|
| **Batteries** | Contain mercury and other toxic chemicals | Use designated battery recycling bins |
| **CRT Monitors** | Retain high voltage even when unplugged; contain lead | Follow local e-waste regulations; professional handling only |
| **Toner / Ink Cartridges** | Contain chemical residues | Return to manufacturer or supplier recycling programs |
| **Chemical Solvents** | Hazardous to water supply | Contact local sanitation/hazardous waste services |
| **Mobile Devices / Electronics** | Contain heavy metals that contaminate soil | Use certified e-waste recycling programs |

> ⚠️ **Always verify local environmental and sanitation regulations** before disposing of any electronic component.

---

## 3.5.1.2 – Safety Data Sheet (SDS)

### What is an SDS?
An **SDS (Safety Data Sheet)** is a standardized document required for any hazardous material. It acts as an official safety manual that anyone handling the material must reference.

### Why It Matters
- Provides **immediate access** to critical safety information at the time of transfer or handling
- Required by law in many jurisdictions (e.g., OSHA in the United States)

### Key Sections of an SDS

| Section | Contents |
|---|---|
| **Hazard Identification** | Health risks, flammability, reactivity |
| **Handling & Storage** | Safe storage conditions and transport guidelines |
| **Emergency Procedures** | Steps for spills, leaks, or accidental exposure |
| **Disposal Instructions** | Environmentally compliant disposal procedures |

> 📌 Always consult the manufacturer's SDS when working with chemical-containing computer components.

---

## 3.5.1.3 – True/False Review Questions

| Statement | Answer | Explanation |
|---|---|---|
| Disposal regulations vary from state to state and country to country. | ✅ **True** | Environmental protection standards differ by region and jurisdiction. |
| CRT monitors may contain dangerously high voltage after being unplugged. | ✅ **True** | Internal capacitors can retain lethal charge even after power is removed. |
| It is acceptable to dispose of small mobile devices (e.g., cell phones) in landfills. | ❌ **False** | Mobile devices contain heavy metals that contaminate soil; they must go through e-waste programs. |
| OSHA requires that all hazardous materials be accompanied by an SDS. | ✅ **True** | OSHA mandates that an SDS be provided whenever a hazardous material is transferred to a new owner. |

---

## 3.6.1.1 – Chapter Summary

### 1. System Boot Process
- On power-on, the **BIOS** runs a **POST (Power-On Self-Test)** to verify hardware health.
- Hardware configuration settings are stored in **CMOS memory**.

### 2. Power Management
- Core equations: **V = IR** (Ohm's Law) and **P = VI** (Power formula)
- Protect systems using:
  - **Surge Protectors** – guard against voltage spikes
  - **UPS (Uninterruptible Power Supply)** – provides battery backup during outages

### 3. CPU & Cooling
- Modern CPUs use **multicore architecture** for parallel processing.
- Cooling solutions include:
  - Air cooling (fans + heat sinks)
  - **Liquid/water cooling** for high-performance systems

### 4. Storage: RAID Technology
- **RAID (Redundant Array of Independent Disks)** combines multiple drives to improve:
  - **Speed** (striping)
  - **Redundancy/data safety** (mirroring)

### 5. Connectivity & Display Standards

| Standard | Notes |
|---|---|
| Legacy ports → Modern USB | Evolution from PS/2, serial, parallel to USB 3.x and USB-C |
| CGA → UHD | Display resolution has advanced from 320×200 (CGA) to 3840×2160 (UHD/4K) |

### 6. Environmental Responsibility
- Dispose of batteries, toner cartridges, and electronics **according to local regulations**.
- Always reference the **SDS** for safe handling and disposal of hazardous materials.

---

*Study notes compiled from Cisco IT Essentials curriculum – Chapter 3: Advanced Computer Hardware*
