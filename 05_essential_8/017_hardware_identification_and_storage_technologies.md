# Computer Hardware Study Notes

A concise reference guide covering core PC hardware concepts.

---

## 1. Power Supply Voltages

A computer's Power Supply Unit (PSU) delivers three standard voltages to components:

| Voltage | Primary Use |
|---------|-------------|
| **3.3V** | CPU, RAM, and sensitive motherboard circuits |
| **5V** | Legacy motherboard logic circuits |
| **12V** | High-power components: GPU, HDD, cooling fans |

---

## 2. Motherboard Chipset — Northbridge vs Southbridge

The chipset acts as a traffic controller between the CPU and all other components.

| Bridge | Role | Connected Components |
|--------|------|----------------------|
| **Northbridge** | High-speed lane — direct CPU access | RAM, Video Card (GPU) |
| **Southbridge** | General I/O management | HDD, Sound Card, USB ports |

> **Key fact:** Northbridge handles RAM access and video card access — the two fastest, most bandwidth-intensive components.

---

## 3. Expansion Cards — Identification Guide

| Card Type | Key Visual Feature | Function |
|-----------|--------------------|----------|
| **Network Interface Card (NIC)** | RJ-45 port (Ethernet jack) | Connects to internet / local network |
| **Video (Graphics) Card** | Large heatsink/fan + HDMI/DisplayPort outputs | Renders display output |
| **Sound Card** | Multiple color-coded 3.5mm audio jacks | Audio input/output |
| **RAID Controller** | Multiple SATA/SAS ports | Manages multiple hard drives |

---

## 4. Port Types

### Modern Ports
| Port | Description |
|------|-------------|
| **USB** | Rectangular slot; connects mice, keyboards, flash drives |
| **Network (RJ-45)** | Large square Ethernet jack; wired internet connection |

### Legacy Ports (rarely seen today)
| Port | Description |
|------|-------------|
| **Parallel Port** | 25-pin large connector; used for older printers |
| **Serial Port** | 9-pin connector; used for older mice and communication devices |
| **Modem Port (RJ-11)** | Narrow phone-line jack; used for dial-up internet |

---

## 5. Storage Devices — By Technology

### Magnetic Storage
Uses magnetism to record data.

| Device | Medium | Notes |
|--------|--------|-------|
| **HDD (Hard Disk Drive)** | Spinning magnetic platters | Fast random access; common in desktops/laptops |
| **Tape Drive** | Long magnetic tape strip | Used for large-scale data backup; high capacity (20TB+) |

### Optical Storage
Uses laser light to read/write data.
- **CD, DVD, Blu-ray** — pits and lands on a plastic disc read by a laser beam

### Solid-State Storage
Uses electrical charges; no moving parts.
- **SSD (Solid State Drive)** — flash memory chips; faster and more durable than HDD

---

## 6. Memory Types

| Type | Full Name | Speed | Cost | Primary Use |
|------|-----------|-------|------|-------------|
| **SRAM** | Static RAM | Very fast | Expensive | **Cache memory** (L1, L2, L3) |
| **DRAM** | Dynamic RAM | Fast | Affordable | Main system RAM |
| **ROM** | Read-Only Memory | — | — | Firmware / BIOS (non-volatile) |

> **Key fact:** SRAM is used for cache memory because it does not need to be constantly refreshed, making it significantly faster than DRAM.

---

## 7. Video Capture Card

| Card | Direction | Purpose |
|------|-----------|---------|
| **Video Capture Card** | **INPUT** | Receives external video signal (from camcorder, game console, etc.) and saves it to the hard drive |
| **Video Adapter (GPU)** | **OUTPUT** | Sends computer-generated images to a monitor |
| **TV Tuner Card** | INPUT | Receives broadcast TV signals |

> A **video capture card** is required to record video from an external recording device to the computer's hard drive.

---

## Quick Reference Summary

| Topic | Key Takeaway |
|-------|--------------|
| PSU Voltages | 3.3V / 5V / 12V |
| Northbridge | Manages RAM + GPU |
| Southbridge | Manages HDD, USB, Audio |
| NIC | Identified by RJ-45 port |
| Magnetic storage | HDD (platters) + Tape Drive (tape strip) |
| Cache memory | Always SRAM |
| Capture video | Use a Video Capture Card |
