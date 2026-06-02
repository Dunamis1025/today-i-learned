# 🖥️ PC Assembly & Maintenance — Study Notes

> **Course:** CompTIA A+ / IT Technician Fundamentals  
> **Topic:** Chapter 1 — Safety, PC Components, and Power Supply Installation  
> **Source:** Video lecture + Gemini AI-assisted review sessions

---

## Table of Contents
1. [Chapter Overview](#1-chapter-overview)
2. [Personal & Workspace Safety](#2-personal--workspace-safety)
3. [Fire Safety — The PASS Method](#3-fire-safety--the-pass-method)
4. [Computer Case Selection](#4-computer-case-selection)
5. [Case Fan Selection & Airflow](#5-case-fan-selection--airflow)
6. [Power Supply Unit (PSU) Installation](#6-power-supply-unit-psu-installation)
7. [Key Vocabulary](#7-key-vocabulary)
8. [Quiz — PSU Installation Order](#8-quiz--psu-installation-order)

---

## 1. Chapter Overview

This chapter introduces the foundational skills required for an IT technician to **build, upgrade, and troubleshoot computers**.

| Area | What You Learn |
|---|---|
| **Safety** | Prevent injury from electricity, sharp edges, and fire |
| **Components** | Understand PSU, motherboard, CPU, RAM, storage, and cases |
| **Compatibility** | Ensure components work together (form factors, wattage, etc.) |
| **Hands-on Lab** | Step-by-step PC assembly from scratch |

---

## 2. Personal & Workspace Safety

> ⚠️ **Safety always comes before technical skill.**

### Body Preparation
- **Remove all jewelry** (rings, watches) — metal conducts electricity and can short-circuit components
- **Secure loose clothing** — fabric can catch on sharp internal edges or get tangled in fans

### Power Management
- **Always power off AND unplug** the equipment before opening the case or touching any internal parts
- **Never open** a power supply or a monitor with a built-in power supply — they store dangerous electrical charge even when unplugged

### Workspace Setup
- Keep the workspace **clean, organized, and clutter-free**
- **No food or drinks** near the workspace — spills can destroy components
- Cover any **sharp internal edges** with tape to prevent cuts
- Wear **safety goggles** to protect your eyes from debris

### Lifting & Ergonomics
- When moving heavy equipment (towers, servers, printers):
  - **Bend your knees**, not your back
  - Lift with your **leg muscles**, not your spine

---

## 3. Fire Safety — The PASS Method

> 🔥 Know where the nearest fire extinguisher is **before** you need it.

### PASS — How to Use a Fire Extinguisher

| Letter | Action | Detail |
|---|---|---|
| **P** | **P**ull the pin | Breaks the tamper seal to enable discharge |
| **A** | **A**im at the base | Point at the *base* of the fire, NOT the flames |
| **S** | **S**queeze the lever | Firmly squeeze to release the extinguishing agent |
| **S** | **S**weep side to side | Move the nozzle back and forth to cover the fire fully |

### Fire Extinguisher Types
Different extinguishers are rated for different materials:

| Rating | Covers |
|---|---|
| **Class A** | Paper, wood, cardboard, plastics |
| **Class B** | Liquids, grease, gasoline |
| **Class C** | Electrical equipment |
| **Multi-rated** | Combination of A, B, and/or C |

> ✅ Always use a **Class C or multi-rated** extinguisher for computer equipment.

### Critical Rules
- **Check the gauge regularly** — if it reads empty or low, it needs recharging before use
- **If the fire is out of control**: do NOT fight it — evacuate immediately and call emergency services (119 / 911)

---

## 4. Computer Case Selection

The case is the "home" for all your components. Choosing the wrong one causes compatibility and cooling problems.

### Key Selection Criteria

| Factor | Why It Matters |
|---|---|
| **Form Factor** | Must match your motherboard size (e.g., ATX case ↔ ATX motherboard) |
| **Size** | Larger = easier assembly + more upgrade space; Smaller = compact but cramped |
| **Included PSU** | If bundled, verify it provides enough wattage for your specific components |
| **Ventilation (Vents)** | More and better-placed vents = better airflow = cooler components |

> 💡 **Rule:** Always confirm the case **form factor** matches your motherboard before purchasing.

### Common Form Factors (Motherboard ↔ Case)

| Motherboard | Case Required |
|---|---|
| ATX | Full Tower / Mid Tower (ATX) |
| Micro-ATX | Mid Tower or Micro-ATX case |
| Mini-ITX | Mini-ITX case |

---

## 5. Case Fan Selection & Airflow

### Why Airflow Matters
Computer components generate heat during operation. Without proper airflow, heat builds up and causes:
- **Thermal throttling** (CPU/GPU slow down to protect themselves)
- **Component damage or failure** over time

### Airflow Direction — The Golden Rule

```
[ FRONT / SIDE ]  →→→  [ BACK / TOP ]
   Cool Air IN              Hot Air OUT
```

- **Intake fans** (front/side): pull **cool air in**
- **Exhaust fans** (back/top): push **hot air out**

> ⚠️ Fans installed backwards or in wrong positions create **air turbulence**, trapping heat inside.

### Fan Selection Criteria

| Factor | Guidance |
|---|---|
| **Size** | Larger fan = more airflow at lower RPM = quieter operation |
| **Speed (RPM)** | Higher RPM = more cooling but more noise |
| **Quantity** | High-performance builds need more fans |
| **Power Connector** | 3-pin/4-pin to motherboard (speed-controllable) or directly to PSU |
| **Available Slots** | Check case mounting positions before buying |

> 💡 **Key Insight:** A larger, slower fan is often **better and quieter** than a smaller, faster one moving the same amount of air.

---

## 6. Power Supply Unit (PSU) Installation

### What Is a PSU?
The **Power Supply Unit (PSU)** converts wall electricity into the voltages your computer components need. Every other component depends on it.

### Before You Start — Anti-Static Protection
| Item | Purpose |
|---|---|
| **Anti-static mat** | Grounds the work surface to prevent static discharge |
| **Anti-static wrist strap** | Grounds your body; connects to the mat |

> ⚡ Static electricity is invisible but can permanently destroy sensitive components (CPU, RAM, GPU).

### PSU Specifications to Check

| Spec | Notes |
|---|---|
| **Wattage** | Must be sufficient for ALL components combined (CPU + GPU are the biggest consumers) |
| **Voltage Setting** | Match to regional standard (e.g., 110–115V in US; 220–240V in Korea/Europe) |
| **Form Factor** | Must physically fit the case (ATX is most common) |

### Step-by-Step Installation

```
Step 1: Open the right side panel of the case
        └─ Unscrew using a Torx or Phillips screwdriver; slide the cover off

Step 2: Identify the PSU slot
        └─ Located at the back of the case (top or bottom depending on case design)

Step 3: Check voltage setting on PSU
        └─ Confirm the voltage switch matches your region before powering on

Step 4: Insert PSU into the slot
        └─ Align the screw holes on the PSU with the mounting holes on the case

Step 5: Secure with 4 screws
        └─ Use the included PSU screws; tighten firmly so it does not move
```

> 🔑 **If your PSU wattage is too low**, your computer will crash, fail to boot, or damage components. Plan your wattage **before** buying.

---

## 7. Key Vocabulary

| Term | Definition |
|---|---|
| **PSU** | Power Supply Unit — converts AC wall power to DC for components |
| **ATX** | Standard form factor for motherboards and cases |
| **Form Factor** | Physical size and shape standard that determines compatibility |
| **Wattage (W)** | Unit of power; higher wattage PSU supports more powerful components |
| **Airflow** | The directional movement of air through the PC case for cooling |
| **Anti-static** | Protection method to prevent static electricity from damaging components |
| **PASS** | Pull, Aim, Squeeze, Sweep — fire extinguisher technique |
| **Torx Screwdriver** | Star-shaped screwdriver commonly used for computer case screws |
| **RPM** | Revolutions Per Minute — measures fan speed |
| **Thermal Throttling** | CPU/GPU automatically slows down to prevent overheating damage |

---

## 8. Quiz — PSU Installation Order

**Match the step number to the correct action:**

| Step # | Action |
|---|---|
| **1** | A. Align the screw holes on the PSU with the mounts on the case |
| **2** | B. Screw the power supply into place |
| **3** | C. Open the computer case |

**✅ Answer Key:**

| Step | Action | Reasoning |
|---|---|---|
| **3 → C** | Open the case | You cannot do anything until the case is open |
| **1 → A** | Align screw holes | Position the PSU correctly before fastening |
| **2 → B** | Screw into place | Fasten only after alignment is confirmed |

> **Memory Tip:** Any hardware installation follows the same pattern:  
> **Open → Position → Fasten**

---

*Notes compiled from video lectures and AI-assisted review (Gemini). For study purposes only.*
