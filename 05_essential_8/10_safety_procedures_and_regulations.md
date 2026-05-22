# Cisco Networking Academy — Lab: Safety Study Notes

> **Course**: IT Essentials / CompTIA A+ Prep  
> **Topic**: Computer Hardware Safety Procedures  
> **Source**: Cisco Networking Academy Lab - Safety (2022)

---

## Overview

This lab covers essential safety procedures when building or servicing computer hardware. A safe workspace must be **clean, organized, and properly lit**.

---

## Part 1: Personal Safety

Prevents cuts, burns, electrical shock, and eye damage.

**Key Precautions:**
- Remove watches and jewelry; secure loose clothing
- Keep food and drinks out of the workspace
- Wear safety goggles and an air filtration mask when needed
- Bend knees (not the back) when lifting heavy objects
- Inspect tools before use — clean, repair, or replace as needed

**Additional Precautions (Q&A):**
- Wear an **anti-static (ESD) wrist strap** to protect components from static discharge
- Watch out for **sharp metal edges** inside PC cases — consider gloves
- Maintain **adequate lighting** to avoid losing small parts
- Keep the workspace **organized** to prevent tripping or dropping equipment

---

## Part 2: Electrical Safety

Prevents electrical fires, injuries, and fatalities.

### Printer Safety
- Allow hot components (e.g., the **fuser unit**) to cool down before handling
- Be cautious of toner dust — work in a ventilated area

### Power Supply Unit (PSU) Safety
- **Never open or repair a PSU yourself**
- Internal **capacitors** store high-voltage charge even after unplugging
  > 💡 *Capacitor* = an electrical component that temporarily stores energy, like a small battery. It can remain charged long after power is removed — making it dangerous.

### Equipment Grounding
- **Purpose**: Provides a low-resistance path for stray current to flow safely to the ground instead of through a person
- **PCs & Printers**: Use a **3-prong grounded plug** in a properly grounded wall outlet
- **Large Metal Racks**: Connect to the building's main earthing system using a **grounding/bonding cable**

> 📝 *Note: Some countries require Portable Appliance Testing (PAT) to verify equipment safety.*

---

## Part 3: Fire Safety

### Fire Response Procedures
- Never fight a fire that is out of control
- Always have a planned **fire escape route** before starting work
- Evacuate quickly and **contact emergency services**
- Watch for burning smells from electronics — a sign of overheating or short circuit

### P-A-S-S Fire Extinguisher Technique

| Letter | Action | Description |
|--------|--------|-------------|
| **P** | Pull | Pull the safety pin |
| **A** | Aim | Aim at the **base** of the fire, not the flames |
| **S** | Squeeze | Squeeze the handle firmly |
| **S** | Sweep | Sweep side to side until fire is out |

### Fire Extinguisher Types (Australia Standard)

| Color | Type | Use Case |
|-------|------|----------|
| 🔴 Red | Water | Paper, wood — ❌ NOT for electrical fires |
| ⚪ White | Dry Powder (ABE) | Most fires including electrical — most **versatile** |
| ⚫ Black | CO₂ | Electrical equipment — leaves no residue |
| 🔵 Blue | Foam | Grease/liquid fires (e.g., kitchen) |

> 💡 *Versatile* = capable of doing many different things; suitable for multiple situations.

---

## Part 4: Government Regulations Compliance

### Health & Safety (Australia)
- **Agency**: SafeWork Australia
- **Website**: [safeworkaustralia.gov.au](https://www.safeworkaustralia.gov.au)
- **Key electrical safety rules**:
  - Inspect all electrical equipment regularly (Test & Tag program)
  - Remove damaged cords/plugs from service immediately
  - Never perform electrical work with wet hands
  - Use **Residual Current Devices (RCDs)** / safety switches

### Building Codes (Australia)
- **Standard**: National Construction Code (NCC)
- Covers: fire escape routes, extinguisher placement, wiring standards, fire-resistant barriers

### Environmental Regulations (E-Waste)
- **Problem**: A company replaced 50 laptops — how to dispose properly?
- **Solution**: Use a certified **E-waste recycling facility** (check local council)
- **Process at facility**:
  1. Data sanitization (physical drive destruction or secure wipe)
  2. Disassembly into components
  3. Recovery and recycling of plastics, metals, and rare materials

---

## Reflection: Most Important Safety Rule?

> **Power off and discharge residual electricity before touching any component.**

No matter how experienced you are, working on live equipment risks electric shock and permanent component damage. Safety always comes before speed or convenience.

---

## Bonus: Computer Disassembly Order (from video lab)

A proper disassembly sequence minimizes risk of damage:

1. **Power down** → unplug → hold power button to drain residual charge
2. Disconnect all peripherals (monitor, keyboard, mouse, network)
3. Open case side panel
4. Remove **HDD/SSD** (SATA power → SATA data → screws)
5. Remove **Optical Drive** (cables → screws → slide out front)
6. Disconnect **PSU cables** from motherboard (24-pin + 4-pin CPU)
7. Remove **GPU / adapter cards** (bracket screw → release locking lever → lift)
8. Unplug **front panel connectors** (USB, audio, power/reset buttons)
9. Remove **RAM** (press locking tabs on both sides → lift out)
10. Place all components on **anti-static mat**

### Key Tips
- Always **look for a locking lever or clip** before pulling — never use brute force
- Label or group screws by location for easy reassembly
- Never open or disassemble the **PSU** — capacitors inside remain dangerous

---

*Study notes compiled with the help of Gemini & Claude AI assistants.*
