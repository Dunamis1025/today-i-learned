# CompTIA A+ Study Notes — Chapter 3.3: Hardware & Displays

---

## 3.3.1.1 — Motherboard Upgrade: Key Considerations

### Why Upgrade?
- User requirements have changed
- Newer software demands higher hardware specs
- Newer hardware offers enhanced performance

### Compatibility Checklist (Domino Effect)
| Component | What to Check |
|-----------|--------------|
| **CPU** | Must fit the new motherboard's socket type |
| **RAM** | Must match the new board's memory standard (e.g., DDR4, DDR5) |
| **Case** | New board must physically fit inside the existing case |
| **Power Supply** | Must supply sufficient wattage for the new board |

### Safety Tips
- Always work on an **antistatic mat** and wear an **antistatic wrist strap**
- When reusing the CPU, **clean off old thermal compound** and re-apply fresh compound before reinstallation

---

## 3.3.1.2 — Motherboard Replacement: Step-by-Step

### Procedure

1. **Record Connections** — Photograph or note all cable and component positions before disassembly
2. **Disassemble** — Disconnect all cables; remove expansion cards and store them on antistatic surfaces
3. **Remove Old Motherboard** — Unscrew carefully; distinguish between metallic and non-metallic standoffs to avoid reuse mistakes
4. **Prepare New Motherboard** — Identify connector locations; replace the rear **I/O shield** with the one supplied for the new board
5. **Secure** — Mount the new board using correct screws; **never force screws** (wrong screws can strip threads or generate metal shavings that cause short circuits)
6. **Reconnect** — Attach power connectors, case buttons, and cooler cables (refer to the motherboard manual)
7. **Reinstall Expansion Cards** — Re-seat GPU and other cards
8. **Final Check** — Verify no loose parts or unconnected cables before powering on

> **Key Tip:** Keep all screws organized during disassembly — losing or mixing them is the most common mistake.

---

## 3.3.1.3 — CPU Upgrade

### Compatibility Requirements
- New CPU must fit the **existing socket** on the motherboard
- Must be supported by the **motherboard chipset**
- Power supply must be able to handle the CPU's TDP (power draw)

### Heat Management
- Faster CPUs generate more heat → may require a **new/better heat sink and fan assembly**
- **Thermal compound** must be applied between the CPU and heat sink for proper heat transfer
- Monitor CPU temperature via **BIOS** or third-party software after installation

### Case Airflow (Fan Placement)
| Position | Role | Location |
|----------|------|----------|
| **Intake** | Draws cool air in | Near the bottom of the case |
| **Exhaust** | Pushes hot air out | Near the top of the case |

> **Avoid** placing two fans directly opposing each other — it disrupts airflow and reduces cooling efficiency.

---

## 3.3.4.4 — Multiple Monitors

### Why Use Multiple Monitors?
- Expands desktop workspace across physical screens
- Enables multitasking (e.g., reference material on one screen, active work on another)
- Significantly improves productivity

### Setup (Windows)
1. Connect monitors via **HDMI**, **DisplayPort**, or other supported cables
2. Right-click the desktop → **Display settings**
3. Configure:
   - **Monitor arrangement** (drag to match physical layout)
   - **Resolution** per monitor
   - **Primary display** selection

---

## 3.3.4.5 — Monitor Terminology

| Term | Definition |
|------|------------|
| **Native Resolution** | The resolution the monitor is built for; shown as *(Recommended)* in Windows |
| **Aspect Ratio** | Width-to-height ratio of the screen; 4:3 (older) vs. 16:9 (modern standard) |
| **Dot Pitch** | Physical distance between pixels; smaller = sharper image |
| **Contrast Ratio** | Range between brightest white and darkest black; higher is better (e.g., 4,500:1 > 1,000:1) |
| **Screen Size** | Diagonal measurement of the display area, in inches |
| **Resolution** | Total pixel count; e.g., 1920 × 1080 (width × height) |
| **Pixel** | The smallest unit of a display image; more pixels = more detail |

---

## Quick Reference: Key Concepts

```
Motherboard upgrade  →  check CPU socket, RAM type, case fit, PSU wattage
CPU upgrade          →  check socket, chipset support, thermal solution
Thermal compound     →  ALWAYS apply between CPU and heat sink
Antistatic precautions → ALWAYS use mat + wrist strap when handling components
Multiple monitors    →  connect via cable → Display Settings → arrange & configure
Native resolution    →  always use the (Recommended) setting for best image quality
```

---

*Notes compiled from Cisco/CompTIA A+ curriculum — Chapter 3.3*
