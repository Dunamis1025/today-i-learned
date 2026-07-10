# 04 - Motherboards, CPUs, and Memory
> Study Notes | CompTIA IT Fundamentals / Cisco Networking Academy  
> Topics: 1.2.2 Motherboards · 1.2.3 CPUs & Cooling · 1.2.5 Memory

---

## Table of Contents
1. [Motherboard Components](#1-motherboard-components)
2. [CPU Architecture](#2-cpu-architecture)
3. [Cooling Systems](#3-cooling-systems)
4. [Memory Types](#4-memory-types)
5. [Quick Reference Cheat Sheet](#5-quick-reference-cheat-sheet)

---

## 1. Motherboard Components

The motherboard is the **main circuit board** of a computer. Every component either plugs into it or communicates through it.

### Key Components & Descriptions

| Component | Description |
|-----------|-------------|
| **BIOS Chip** | Used to boot the computer and perform a Power-On Self-Test (POST) |
| **Northbridge** | Controls high-speed access to RAM and the video card |
| **Southbridge** | Allows the CPU to communicate with slower-speed devices (USB, keyboard, etc.) |
| **CPU** | Considered the brain of the computer |
| **RAM** | A temporary location to store data and applications |
| **Expansion Slot** | Provides locations for connecting additional components to the motherboard |
| **Micro ITX** | Smaller form factor that is backward compatible with ATX |
| **Mini ITX** | Has only one PCI slot for expansion cards |

### Motherboard Form Factors

- **ATX** — Standard full-size motherboard; most common desktop form factor
- **Micro ITX** — Smaller than ATX but still backward compatible with ATX components
- **Mini ITX** — Very small; only has **one** PCI expansion slot

### Chipset: Northbridge vs Southbridge

```
         CPU
          |
    [Northbridge]  ←→  RAM, Video Card (high-speed)
          |
    [Southbridge]  ←→  USB, Keyboard, Hard Drive (slow-speed)
```

- **Northbridge** handles fast communication between the CPU, RAM, and GPU
- **Southbridge** handles slower peripherals like USB ports, audio, and storage

> 💡 Think of Northbridge as the **highway** (fast) and Southbridge as **local roads** (slower)

---

## 2. CPU Architecture

### What is a CPU?

The **Central Processing Unit (CPU)** is the brain of the computer.

- Interprets and executes commands from hardware and software
- Handles input from devices (keyboard, mouse) and outputs results to the monitor
- A tiny **microchip** inside a CPU package
- Major manufacturers: **Intel** and **AMD**

### CPU Socket Types

The CPU socket is the connection point between the CPU and the motherboard. There are two main architectures:

#### PGA — Pin Grid Array

- **Pins are on the CPU** (on the underside of the processor package)
- Inserted into the motherboard socket using **ZIF (Zero Insertion Force)**
- ZIF = very little force needed to install — prevents pin damage
- Primarily used by **AMD**

```
 [CPU]
 | | | | |  ← pins on the bottom of the CPU
  \_____/
     ↓
[Motherboard Socket] — has holes to receive the pins
```

#### LGA — Land Grid Array

- **Pins are on the motherboard socket** (not on the CPU)
- The CPU itself is flat with no pins
- Primarily used by **Intel**

```
 [CPU] — flat, no pins
     ↓
[Motherboard Socket]
 | | | | |  ← pins inside the socket
```

### PGA vs LGA Comparison

| Feature | PGA | LGA |
|---------|-----|-----|
| Pin location | On the CPU | On the socket |
| Pin damage risk | CPU pins can bend | Socket pins can bend |
| Main brand | AMD | Intel |
| CPU appearance | Spiky bottom | Flat, smooth bottom |
| Insertion method | ZIF socket | Pressure clamp |

> 💡 Memory trick:
> - **PGA** → **P**ins on the **P**rocessor
> - **LGA** → Pins **L**aid in the socket like **L**and

---

## 3. Cooling Systems

### Why Cooling Matters

- Electrical current flowing through components **generates heat**
- Overheating causes:
  - Reduced performance (throttling)
  - System crashes
  - Permanent component damage
- Keeping components cool is **critical** for stable operation

### Two Types of Cooling Solutions

#### Passive Cooling — No power required

- Works without electricity
- Methods:
  - **Reduce component speed** (thermal throttling) → less heat generated
  - **Heat sink** → a metal block that absorbs heat and dissipates it into the air
- Silent, no moving parts
- Lower cooling capacity

> 💡 Like a **radiator** — sits there and naturally draws heat away

#### Active Cooling — Requires power

- Uses electricity to actively remove heat
- Examples:
  - **Case fans** — blow hot air out of the chassis
  - **CPU fans** — mounted on the heat sink to increase airflow
- Louder, has moving parts
- Higher cooling capacity

> 💡 Like an **electric fan** — needs to be powered to work, but cools much more effectively

### Passive vs Active Cooling Comparison

| Feature | Passive | Active |
|---------|---------|--------|
| Needs electricity? | ❌ No | ✅ Yes |
| Examples | Heat sink, throttling | Case fan, CPU fan |
| Noise level | Silent 🤫 | Produces noise 🔊 |
| Cooling power | Lower | Higher |
| Moving parts | None | Yes (fans) |

---

## 4. Memory Types

### What is a Byte?

All memory stores data in **bytes**:

- **Bit** = the smallest unit of data; a single `0` or `1`
- **Byte** = 8 bits grouped together
- Bytes represent letters, numbers, and symbols

```
Bit:   0  1  0  1  1  0  0  1
       └──────────────────────┘
              = 1 Byte
```

### ROM — Read-Only Memory

- Located on the **motherboard** and other circuit boards
- Contains basic instructions the CPU needs to start up
- Stores: booting sequence, POST (Power-On Self-Test), loading the OS
- **Nonvolatile** → data is **retained** even when the power is off
- Cannot be easily modified (read-only)

> 💡 ROM is like a **textbook** — fixed content, always there even without power

### RAM — Random Access Memory

- **Temporarily stores** data and programs currently in use by the CPU
- **Volatile** → all data is **lost** when the computer is powered off
- More RAM = better multitasking and faster performance
- Without enough RAM, the computer swaps data to the **hard drive** (much slower)
- Maximum installable RAM is determined by the **motherboard**

> 💡 RAM is like a **desk** — your active workspace. When you leave (power off), the desk is cleared

### ROM vs RAM Comparison

| Feature | ROM | RAM |
|---------|-----|-----|
| Volatility | **Nonvolatile** (data stays) | **Volatile** (data erased) |
| Power off behavior | Data retained ✅ | Data lost ❌ |
| Primary purpose | Boot instructions & firmware | Active program/data storage |
| Modifiable? | Read-only ❌ | Read & Write ✅ |
| Location | Fixed chip on motherboard | Removable sticks (DIMM slots) |
| Performance impact | Fixed | More RAM = faster system |

> 💡 Memory tricks:
> - **ROM** = **R**emains **O**n **M**achine → survives power off
> - **RAM** = **R**eset **A**fter **M**achine off → cleared on shutdown

---

## 5. Quick Reference Cheat Sheet

### Motherboard At-a-Glance

```
┌─────────────────────────────────────────┐
│             MOTHERBOARD                 │
│                                         │
│  [BIOS Chip] → boots the computer       │
│  [CPU Socket] → holds the processor     │
│  [RAM Slots] → temporary memory         │
│  [Northbridge] → fast: RAM + GPU        │
│  [Southbridge] → slow: USB + HDD        │
│  [Expansion Slots] → add-on cards       │
└─────────────────────────────────────────┘
```

### All Key Terms

| Term | Full Name | One-Line Summary |
|------|-----------|-----------------|
| BIOS | Basic Input/Output System | Boots the computer; performs POST |
| POST | Power-On Self-Test | Hardware check at startup |
| PGA | Pin Grid Array | Pins on the CPU |
| LGA | Land Grid Array | Pins on the socket |
| ZIF | Zero Insertion Force | Install CPU with minimal force |
| ROM | Read-Only Memory | Nonvolatile; stores firmware |
| RAM | Random Access Memory | Volatile; temporary working memory |
| ATX | Advanced Technology eXtended | Standard motherboard size |
| ITX | Information Technology eXtended | Compact motherboard form factor |
| CPU | Central Processing Unit | The brain of the computer |

### Memory Hierarchy (Speed: Fast → Slow)

```
CPU Registers  →  Cache  →  RAM  →  Hard Drive / SSD
   (fastest)                           (slowest)
```

---

*End of Notes — Section 1.2.2 through 1.2.5*
