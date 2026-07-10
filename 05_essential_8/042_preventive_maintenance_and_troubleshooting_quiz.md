# TIL: PC Preventive Maintenance & Troubleshooting (Chapter 4)

## Overview

Preventive maintenance is the proactive management of computer hardware and software to extend equipment lifespan, reduce failures, minimize downtime, and cut repair costs. Without a plan, organizations face **increased downtime** and **increased repair costs** — the two most significant consequences of neglect.

---

## Why Preventive Maintenance Matters

- Protects equipment against **future problems** before they escalate
- Reduces the frequency of unexpected hardware failures
- Extends the operational lifespan of components
- Lowers total cost of ownership for IT infrastructure

> **Most important reason:** Preventive maintenance helps protect computer equipment against future problems by catching issues early — before they become costly failures.

---

## Hardware Maintenance: What to Clean & Check

### Cleaning Guidelines
- Use **compressed air** to remove dust from inside the computer case
  - It safely blows dust out of hard-to-reach areas without touching sensitive parts
  - **Never use** damp cloths or regular dusters on internal components
- When blowing out a CPU fan, **hold the fan blades still** to prevent it from spinning
  - A fan spinning too fast from air pressure can act like a generator and create electrical current that damages components
- **Never invert** a compressed air can — liquid propellant can spray out and cause damage

### Components to Inspect Regularly
| Component | What to Check |
|---|---|
| CPU fan & heat sink | Dust buildup, fan spinning freely |
| RAM modules | Dust, secure seating in slots |
| Storage drives | Cable connections (see below) |
| Adapter cards (GPU, etc.) | Dust, secure in PCIe slots |
| Cables & power connectors | Loose or damaged connections |
| Keyboard & mouse | External cleaning |

### Hard Drive Maintenance
- **Check that cables are firmly connected** — this is the only safe external maintenance task
- **Never open** a hard drive — it is a precision-sealed component; even microscopic dust causes permanent damage
- Do not use compressed air inside the drive, and do not clean read/write heads with a cotton swab

### Environmental Controls
- Keep air vents **unobstructed** for proper airflow
- Maintain appropriate **room temperature and humidity**
- Extreme temperatures are the most damaging environmental factor for laptops

---

## Software Maintenance Schedule

Maintain a regular schedule for:
- Updating **security software** and **virus definition files**
- Removing **unnecessary or unused programs**
- Running **disk defragmentation** on HDDs
- Applying **OS patches and security updates**

---

## The 6-Step Troubleshooting Process

| Step | Action |
|---|---|
| 1 | **Identify the problem** — gather information from the user |
| 2 | **Establish a theory of probable causes** — hypothesize before acting |
| 3 | **Test the theory** — determine the most likely cause |
| 4 | **Establish a plan of action** — outline steps to resolve the issue |
| 5 | **Verify full system functionality** — confirm the fix worked |
| 6 | **Document findings, actions, and outcomes** — critical for future reference |

> **Key insight:** Step 2 is often skipped in haste — always form a hypothesis before jumping to solutions. Step 6 (documentation) is what prevents repeating the same mistakes in the future.

---

## Hardware Troubleshooting: Common Scenarios & Answers

### Q: Computer sometimes doesn't turn on
**Likely cause:** Failing **power supply unit (PSU)**
- PSU gradually loses ability to deliver stable power
- Distinguish from: POST errors (hardware component issue), blinking cursor (OS/software issue), loose power cord (physical connection issue)

### Q: Computer clock keeps losing time
**Likely cause:** **CMOS battery** is loose or dead
- The CMOS battery on the motherboard keeps BIOS settings (including date/time) alive when the PC is off
- When it fails, the system clock resets every time the machine loses power

### Q: Large files take longer to open than usual
**First action:** **Back up user data immediately**
- When hard disk failure is suspected, data safety is the top priority
- Do not replace the drive or run disk cleanup before securing the data — both actions can accelerate failure

### Q: Laptop used in extreme cold (-25°C to 27°C)
**Biggest risk:** **Temperature**
- Extreme cold degrades lithium-ion battery performance significantly
- Temperature swings cause condensation inside the device, leading to short circuits
- Cold makes components brittle and affects lubricants in fans and drive motors
- (Humidity at 40% and wind at 72 km/h are less immediately damaging)

---

## Key Takeaways

1. **Compressed air** is the go-to tool for internal hardware cleaning — nothing else is safe for delicate components.
2. **Hard drives are sealed units** — never open them for any maintenance reason.
3. **Cable checks** are the safest and most impactful routine hardware task.
4. **CMOS battery failure** = system clock issues.
5. **PSU failure** = intermittent or complete failure to power on.
6. **Data backup comes first** whenever hardware failure is suspected.
7. **Documentation** at the end of every troubleshooting session prevents repeat work.
8. **Temperature** is the most critical environmental threat to computing hardware.

---

*Source: Cisco IT Essentials — Chapter 4: Preventive Maintenance and Troubleshooting*
