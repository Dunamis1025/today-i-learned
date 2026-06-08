# 🖥️ Computer Firmware & Boot Process — Study Notes

> Module: IT Essentials / CompTIA A+ Prep  
> Topic: BIOS, UEFI, POST, CMOS — Core Concepts & Lab

---

## 1. POST (Power-On Self-Test)

**What it is:** An automatic hardware diagnostic routine that runs every time the computer is powered on, before the OS loads.

**What it checks:**
- RAM (memory integrity)
- CPU (processor presence)
- USB controllers
- Input devices (keyboard, mouse)
- SATA storage drives
- Other essential motherboard components

**How it reports errors:**

| Situation | What Happens |
|-----------|-------------|
| All hardware OK | Boot continues normally |
| Hardware failure detected | Screen may go blank + system emits **beep codes** |

**Beep Codes:**
- Each beep pattern corresponds to a specific hardware failure (e.g., memory error, CPU issue, GPU missing)
- Patterns **vary by manufacturer** — always consult the specific motherboard manual for interpretation

---

## 2. BIOS (Basic Input/Output System)

**What it is:** A small firmware program stored on a **ROM chip** on the motherboard. It is the first software that runs when the computer powers on.

**Primary roles:**
- Acts as the **bridge** between hardware and the operating system
- Initializes and tests hardware (POST)
- Determines which device to boot from (boot order)
- Manages basic hardware settings:
  - Memory configuration
  - USB/SATA port behavior
  - CPU settings
  - Date & time

**Analogy:** Think of BIOS as the computer's "instruction manual" — it tells the system how to wake up and get to work.

**Limitation:** Traditional BIOS is a legacy system with constraints:
- 16-bit processor mode only
- Supports boot drives up to **2TB** (MBR partition scheme)
- Text-only interface, no mouse support

---

## 3. CMOS (Complementary Metal-Oxide Semiconductor)

**What it is:** A small, low-power **memory chip** on the motherboard that stores the BIOS/UEFI configuration settings.

**What it saves:**
- System date and time
- Boot order sequence
- Hardware enable/disable states
- Custom BIOS settings made by the user

**The CMOS Battery:**
- CMOS requires continuous power to retain its data
- A small coin-cell battery (typically **CR2032**) on the motherboard provides this power
- If the battery dies → settings are lost → system resets to factory defaults

**Diagnostic Tip:** If your computer's clock keeps resetting to the wrong date/time after shutting down, the **CMOS battery is likely dead** and needs replacement.

**Analogy:** If BIOS is the instruction manual, CMOS is the **sticky note** where your custom preferences are written — and the battery is the glue keeping that note in place.

---

## 4. UEFI (Unified Extensible Firmware Interface)

**What it is:** The modern replacement for legacy BIOS. Functionally serves the same purpose but with significantly enhanced capabilities.

**Key improvements over BIOS:**

| Feature | Legacy BIOS | UEFI |
|---------|-------------|------|
| Interface | Text-only, keyboard only | Graphical UI, mouse support |
| Boot drive size | Up to 2TB (MBR) | Up to **9.4 ZB** (GPT) |
| Architecture | 16-bit | 32-bit and 64-bit |
| Security | Minimal | **Secure Boot** feature |
| Boot speed | Slower | Faster (optimized init) |
| Modularity | Limited | Highly modular/extensible |

**Secure Boot:**
- A UEFI security feature that ensures the system only boots into **verified, signed operating systems**
- Protects against **rootkits** and **bootloader malware** that attempt to run before the OS loads

**Terminology Note:** Many manufacturers still label their UEFI firmware as "BIOS" in the interface (e.g., "BIOS Setup Utility") to maintain familiarity. However, any modern computer (post ~2012) is almost certainly running UEFI under the hood.

---

## 5. Quick Comparison Summary

| Term | Type | Role |
|------|------|------|
| **POST** | Process | Hardware self-test on every boot |
| **BIOS** | Firmware program (legacy) | Controls hardware ↔ OS communication |
| **UEFI** | Firmware program (modern) | Replaces BIOS with enhanced features |
| **CMOS** | Memory chip | Stores firmware settings persistently |

---

## 6. Lab — Investigating BIOS/UEFI Settings

### Goal
Access the firmware setup utility, explore system hardware info, and practice configuring the boot order.

### How to Enter the Firmware Setup

1. Power off the computer completely
2. Press the power button, then immediately and repeatedly tap the setup key
3. Common keys: `Delete`, `F2`, `F10`, `F12` (watch for the on-screen prompt during POST)
4. The firmware setup utility will open before Windows loads

### Key Sections to Explore

| Menu Section | What to Look For |
|---|---|
| **Main / System Info** | BIOS/UEFI version, manufacturer, system date/time |
| **CPU Settings** | Processor speed (GHz), core count, cache info |
| **RAM / Memory** | RAM speed (MHz), total capacity, slot configuration |
| **Storage / Hard Drive** | Detected drives, SATA mode (AHCI/IDE) |
| **Boot Order** | Which device the system tries to boot first |
| **Security** | Admin/user passwords, Secure Boot toggle |
| **Power Management (ACPI)** | Sleep states (S1/S3/S4), wake-on-LAN settings |
| **PnP (Plug and Play)** | IRQ resource allocation for hardware |
| **Splash Screen** | Enable/disable the manufacturer logo on boot |

### Boot Order — Why It Matters

- The boot order tells the computer **which device to check first** for an operating system
- Example: Setting **Optical Drive (CD/DVD)** as the first boot device allows you to install a new OS from a disc
- If the optical drive has no bootable media, the system automatically falls through to the **next device** in the list (typically the hard drive)

**Common Boot Order for OS Installation:**
1. Optical Drive (or USB Drive)
2. Hard Disk Drive (HDD/SSD)

### Lab Safety Rules

> ⚠️ **Do not change settings you don't understand.**  
> ⚠️ **Always back up important data before entering firmware settings.**  
> ✅ **To explore safely: exit using "Exit Without Saving" / "Discard Changes and Exit".**  
> ✅ **Only use "Save and Exit" when you intentionally want to apply changes.**

---

## 7. Key Takeaways

- **POST** is the system's health check — beep codes signal hardware failures
- **BIOS** is the legacy firmware bridge between hardware and the OS
- **CMOS** stores your settings; its battery keeps them alive after shutdown
- **UEFI** is the modern, secure, graphical upgrade to BIOS
- **Boot order** determines where the computer looks for an OS — critical for OS installation and troubleshooting
- A **dead CMOS battery** = clock keeps resetting = replace the CR2032 coin cell

---

*Notes compiled from Cisco NetAcad IT Essentials curriculum.*
