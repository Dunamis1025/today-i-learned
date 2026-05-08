# 01 Computer Hardware Basics & Safety

> 📚 Study Notes — Essential 8 | Day 1  
> Topic: Introduction to Computer Hardware, Safety, and Internal Components

---

## 1. How a Computer Works — The Core Cycle

Every computer, no matter its size, follows this fundamental cycle:

```
INPUT → STORAGE → PROCESSING → OUTPUT
```

| Stage | Description | Examples |
|---|---|---|
| **Input** | Data enters the computer | Keyboard, mouse, microphone, webcam |
| **Storage** | Data is held in memory | RAM (temporary), SSD/HDD (permanent) |
| **Processing** | CPU executes instructions | Running programs, calculations |
| **Output** | Results are delivered to the user | Monitor, speakers |

---

## 2. The Evolution of Computers

- Computers used to fill **entire rooms** with mainframes just to do what a small single-board computer (e.g., Raspberry Pi) can do today.
- Computers are now **integrated into everyday life**: smartwatches, health/fitness trackers, etc.
- The field has changed **drastically** and continues to evolve rapidly.

---

## 3. External Components (Outside "The Box")

### Input Devices
- Keyboard
- Mouse
- Microphone
- Webcam

### Output Devices
- Monitor
- Speakers

### The Computer Case (a.k.a. "The Box" / Tower)

**Front of the case:**
- USB ports (for keyboard, mouse, external devices)
- Headphone/speaker-out port
- Microphone-in port
- Optical drive (CD/DVD — legacy but still used)

**Back of the case:**
- Power supply connector (plugs into wall outlet)
- Adapter cards (networking, display/multiple monitors)
- Display ports: VGA, DVI, DisplayPort
- Audio connectors (mic in, speaker out, line in)
- Multiple USB ports
- Networking jack (sometimes two — one onboard, one high-performance)

---

## 4. Internal Components (Inside "The Box")

### 🖥️ Motherboard (System Board / Main Board)
- The **central hub** that all other components connect to.
- Full of circuitry, capacitors, and connectors.
- Enables all components to **send and receive data** with each other.
- Physically mounted inside the computer case.

### 🧠 CPU — Central Processing Unit
- The **"brain"** of the computer.
- Executes instructions and runs programs.
- Gets **very hot, very fast** → requires cooling.
- Cooling solution:
  - **Heatsink (fins):** absorbs and spreads heat away from the CPU.
  - **Fan:** blows air over the heatsink to cool it down.

### 🗂️ RAM — Random Access Memory
- **Temporarily** stores data so the CPU can access it quickly.
- More RAM = faster multitasking and program execution.
- Data is lost when the computer is powered off.

### 💾 Storage — SSD / HDD
- **Permanently** stores data (files, OS, programs, photos, etc.).
- **SSD (Solid-State Drive):** fast read/write speeds, no moving parts — preferred today.
- **HDD (Hard Disk Drive):** older technology, slower, uses spinning platters.
- Example shown in video: a solid-state drive (SSD).

### ⚡ Power Supply Unit (PSU)
- Plugs into the **wall outlet** and converts AC power to DC power.
- Distributes power to **all internal components** (motherboard, CPU, GPU, drives, etc.).
- Must be powerful enough to support high-end components like large graphics cards.

### 🎮 Expansion / Adapter Cards
- Installed in **expansion slots** on the motherboard.
- Add extra functionality to the system.

| Card Type | Purpose |
|---|---|
| **Graphics Card (GPU)** | High-performance display output; gaming, 3D, VR |
| **Network Card (NIC)** | Networking / internet connectivity |

> ⚠️ Note: Motherboards often have **built-in (onboard)** graphics and network ports, but dedicated expansion cards offer significantly higher performance.

### 💿 Optical Drive (Legacy)
- Reads/writes CD and DVD discs.
- Can temporarily store data on physical media.
- Less common today but still found in some systems.

---

## 5. Safety & ESD (Electrostatic Discharge)

### ⚠️ Why Safety Matters
- Computer components operate with **high-voltage electricity**.
- Improper handling can cause:
  - **Electrical fires**
  - **Serious personal injury**
  - **Permanent damage to components**

### ⚡ What is ESD (Electrostatic Discharge)?
- **Static electricity** built up on your body can discharge into sensitive components.
- Even a small, undetectable static shock can **permanently damage** a CPU, RAM, or motherboard.

### 🛡️ How to Prevent ESD Damage
- Use an **anti-static wrist strap** connected to a grounded surface.
- Touch a **metal part of the case** before handling components to discharge static.
- Work on a **non-carpeted, grounded surface**.
- Keep components in **anti-static bags** when not in use.

---

## 6. Hands-On Practice

> 💡 Theory alone is not enough. The best way to learn hardware is to **physically disassemble and reassemble** a computer.

Skills to practice:
- Identify each internal component by sight.
- Understand which slot/connector each part uses.
- Safely handle components with ESD precautions.
- Trace cables from the power supply to each component.

---

## 7. Career Path in IT

People enter the IT field through:
- **Certifications** (e.g., CompTIA A+, Network+)
- **Formal education** (degrees, diplomas)
- **Hands-on experience** (internships, self-study, home labs)

---

## Key Vocabulary

| Term | Meaning |
|---|---|
| **Motherboard** | Main circuit board; connects all components |
| **CPU** | Brain of the computer; processes instructions |
| **RAM** | Temporary memory; fast, volatile storage |
| **SSD** | Fast permanent storage with no moving parts |
| **PSU** | Power Supply Unit; provides power to all parts |
| **GPU** | Graphics Processing Unit; handles display/rendering |
| **NIC** | Network Interface Card; handles network connectivity |
| **ESD** | Electrostatic Discharge; static electricity that damages components |
| **Heatsink** | Metal fins that draw heat away from the CPU |
| **Expansion Slot** | Slot on the motherboard for adding extra cards |
| **Optical Drive** | CD/DVD reader/writer |
| **Onboard** | Built directly into the motherboard (vs. dedicated card) |

---

*Notes based on: CompTIA IT Fundamentals / Essential 8 — Module 1.0.1*  
*Source: Cisco/CompTIA course video transcript + course introduction material*
