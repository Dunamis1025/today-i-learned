# 08. Storage Devices

## Table of Contents
1. [Semiconductor Storage (SSD)](#1-semiconductor-storage-ssd)
2. [SSD Form Factors](#2-ssd-form-factors)
3. [NVMe](#3-nvme-non-volatile-memory-express)
4. [SSHD (Solid State Hybrid Drive)](#4-sshd-solid-state-hybrid-drive)
5. [Storage Technology Types](#5-storage-technology-types)
6. [Optical Storage Devices](#6-optical-storage-devices)
7. [Types of Optical Media](#7-types-of-optical-media)

---

## 1. Semiconductor Storage (SSD)

Solid-state drives (SSDs) store data as **electrical charges in semiconductor flash memory**.

### Advantages over HDD

| Feature | SSD | HDD |
|---|---|---|
| Speed | Much faster | Slower |
| Noise | Silent (no moving parts) | Mechanical noise |
| Heat | Low | Higher |
| Power consumption | Low | Higher |
| Reliability | Higher (no moving parts to fail) | Lower |
| Weight | Lighter | Heavier |

### Storage Capacity
- Ranges from approximately **120 GB to several TBs**

---

## 2. SSD Form Factors

SSDs come in **three main form factors**:

### 2.1 Disc Drive Form Factor
- Packaged similarly to an HDD in a closed casing
- Can be mounted in a computer case just like an HDD
- Available in sizes: **2.5 inch**, **3.5 inch**, and **1.8 inch** (1.8" is rare)
- Most common: **2.5" SSD** used in laptops

### 2.2 Expansion Card
- Plugs directly into the **motherboard**
- Mounts in the computer case like other expansion cards (e.g., GPU)
- High performance due to direct board connection

### 2.3 mSATA or M.2 Modules
- Uses a **special socket** on the motherboard
- **M.2** is a standard for computer expansion cards
- M.2 is a **family of standards** that specifies physical aspects such as:
  - Connectors
  - Dimensions/size
- Much smaller and more compact than disc-drive form SSDs

---

## 3. NVMe (Non-Volatile Memory Express)

**NVMe** is a specification developed specifically to allow computers to take greater advantage of the features of SSDs.

### Key Points
- Provides a **standard interface** between SSDs, the **PCIe bus**, and operating systems
- Allows compliant SSD drives to attach to the PCIe bus **without requiring special drivers**
- Similar concept to USB flash drives — plug in and use across multiple computers without installation

### Why NVMe Matters
> Traditional SSDs using SATA interface couldn't fully utilize the speed of flash memory. NVMe removes this bottleneck by communicating directly over PCIe.

| Interface | Max Theoretical Speed |
|---|---|
| SATA SSD | ~600 MB/s |
| NVMe SSD (PCIe) | ~3,500–7,000+ MB/s |

---

## 4. SSHD (Solid State Hybrid Drive)

SSHDs are a **compromise between a magnetic HDD and an SSD**.

### How It Works
```
SSHD = Magnetic HDD  +  Small amount of onboard Flash Memory (Non-volatile cache)
```

- The SSHD **automatically caches frequently accessed data** onto the flash memory
- This speeds up operations such as **operating system start-up**

### Comparison

| | HDD | SSHD | SSD |
|---|---|---|---|
| Speed | Slow | Medium | Fast |
| Price | Cheap | Mid-range | Expensive |
| Technology | Magnetic only | Magnetic + Flash cache | Flash only |

---

## 5. Storage Technology Types

Every storage device can be categorized into one of three technologies:

| Technology | How It Works | Examples |
|---|---|---|
| **Optical** | Uses laser light to record or erase data | CD, DVD, Blu-ray |
| **Magnetic** | Records bits as magnetized areas on magnetic media | HDD, Tape Drive |
| **Solid State** | Uses non-volatile memory chips to store data | SSD, Flash Drive (USB) |

### Quick Reference — Device Classification

| Device | Technology |
|---|---|
| CD | Optical |
| DVD | Optical |
| Blu-ray | Optical |
| HDD | Magnetic |
| Tape Drive | Magnetic |
| 2.5" SSD | Solid State |
| Flash Drive (USB) | Solid State |
| M.2 SSD | Solid State |

---

## 6. Optical Storage Devices

**Optical drives** are a type of **removable media storage device** that use lasers to read and write data on optical media.

### Background
- Developed to overcome the storage capacity limitations of removable magnetic media (e.g., floppy discs, magnetic storage cartridges)

### Three Types of Optical Drives

| Type | Full Name | Primary Use |
|---|---|---|
| **CD** | Compact Disc | Audio and general data |
| **DVD** | Digital Versatile Disc | Digital video and data |
| **BD** | Blu-ray Disc | HD digital video and data |

### Read/Write Modes

All three types (CD, DVD, BD) come in three modes:

| Mode | Description |
|---|---|
| **Pre-recorded (ROM)** | Read-only; data is factory-recorded |
| **Recordable (R)** | Write once; cannot be erased or re-recorded |
| **Re-recordable (RW / RAM / RE)** | Can be recorded, erased, and re-recorded multiple times |

### Single-Layer vs. Dual-Layer

- **DVD** and **BD** media can be **single layer (SL)** or **dual layer (DL)**
- Dual layer roughly **doubles the capacity** of a single disc

---

## 7. Types of Optical Media

### 7.1 CD Media (~700 MB)

| Optical Media | Description | Storage Capacity |
|---|---|---|
| **CD-ROM** | CD read-only memory; pre-recorded at factory | ~700 MB |
| **CD-R** | CD recordable; can be written once | ~700 MB |
| **CD-RW** | CD rewritable; can be recorded, erased, and re-recorded | ~700 MB |

### 7.2 DVD Media

| Optical Media | Description | Storage Capacity |
|---|---|---|
| **DVD-ROM** | DVD read-only memory; pre-recorded | 4.7 GB (SL) / 8.5 GB (DL) |
| **DVD-RAM** | DVD rewritable; record, erase, and re-record | 4.7 GB (SL) / 8.5 GB (DL) |
| **DVD+/-R** | DVD recordable; written once | 4.7 GB (SL) / 8.5 GB (DL) |
| **DVD+/-RW** | DVD rewritable; record, erase, and re-record | 4.7 GB (SL) / 8.5 GB (DL) |

> **Note:** DVD+R and DVD-R are two competing standards with slightly different write methods, but both hold the same capacity.

### 7.3 Blu-ray Media

| Optical Media | Description | Storage Capacity |
|---|---|---|
| **BD-ROM** | Blu-ray read-only; pre-recorded with movies, games, or software | 25 GB (SL) / 50 GB (DL) |
| **BD-R** | Blu-ray recordable; written once | 25 GB (SL) / 50 GB (DL) |
| **BD-RE** | Blu-ray rewritable; record, erase, and re-record | 25 GB (SL) / 50 GB (DL) |

### Capacity Summary

```
CD      ~700 MB
DVD-SL  ~4.7 GB    (≈ 6.7× CD)
DVD-DL  ~8.5 GB    (≈ 1.8× DVD-SL)
BD-SL   ~25 GB     (≈ 5.3× DVD-SL)
BD-DL   ~50 GB     (≈ 2× BD-SL)
```

---

## Key Takeaways

- **SSD** stores data electrically in flash memory — faster, quieter, and more reliable than HDD
- **SSD form factors**: Disc drive (2.5"/3.5"), Expansion card, M.2/mSATA
- **NVMe** is the modern high-speed interface for SSDs over PCIe
- **SSHD** = HDD + small SSD cache — a cost-effective middle ground
- **Three storage technologies**: Optical (laser), Magnetic (magnetism), Solid State (flash)
- **Optical media suffix rules**: `-ROM` = read only, `-R` = write once, `-RW/-RAM/-RE` = rewritable
- **Dual-layer** optical discs roughly double capacity vs single-layer
