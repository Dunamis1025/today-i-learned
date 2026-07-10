# IT Essentials – Study Notes

A summary of topics covered in this study session, focused on hardware fundamentals, BIOS/CMOS, RAID, and workplace safety procedures.

---

## 1. Electrical Units – Resistance

**Concept:** The unit used to measure resistance to current flow in a circuit is the **ohm (Ω)**.

- **Current** → measured in **amps** (rate of electron flow)
- **Voltage** → measured in **volts** (the "pressure" pushing current)
- **Power** → measured in **watts** (total energy used)
- **Resistance** → measured in **ohms** (opposition to current flow)

**Analogy:** Electricity is like water flowing through a pipe.
- Current = the water itself
- Voltage = water pressure
- Resistance (ohms) = how narrow/obstructed the pipe is

---

## 2. CMOS Battery – Low Charge Symptoms

**Concept:** A failing CMOS battery is most clearly indicated by **incorrect system time and date** after every reboot.

- The CMOS battery keeps BIOS settings (time, date, hardware config) alive while the PC is powered off — like a watch battery on the motherboard.
- When it dies, the motherboard "forgets" the time and resets it on every boot.

**Why other symptoms don't fit:**
- *POST beep codes* → usually point to RAM or GPU issues
- *Slow hard drive* → drive health issue, unrelated to CMOS
- *Boot failure* → too many possible causes (PSU, OS corruption, etc.) to be a definitive CMOS indicator

---

## 3. Audio/Video Editing Workstation – Key Component

**Concept:** The most important specialized component for an A/V editing workstation is a **dedicated/specialized video card (GPU)**.

- Video editing requires real-time rendering of large amounts of visual data.
- A powerful GPU offloads this heavy processing from the CPU, dramatically improving editing speed and responsiveness.

**Analogy:** CPU = the chef; GPU = high-efficiency kitchen appliances that let the chef work much faster.

**Why other options don't fit:**
- *Liquid cooling* → manages heat, doesn't boost rendering performance
- *TV tuner card* → for receiving TV signals only
- *High-speed wireless adapter* → affects internet speed, not local processing

---

## 4. Chemical Spill Procedure – Reference Document

**Concept:** For instructions on safely cleaning up and disposing of a spilled chemical (e.g., cleaning solution), the correct reference is the **Safety Data Sheet (SDS)**.

- SDS = a "manual" for each chemical product, covering safe handling, spill response, and disposal procedures.
- Legally required to be accessible wherever chemicals are used in a workplace.

**Why other options don't fit:**
- Hazmat teams, regulatory bodies, and insurance policies handle broader oversight or compliance — not immediate, product-specific cleanup steps. The SDS provides that directly.

---

## 5. BIOS Setup – Configurable Settings (Choose Two)

**Concept:** Two settings that can be modified in the BIOS setup program:

1. **Boot order** – determines which device (HDD, USB, optical drive, etc.) the system tries first when starting the OS.
2. **Enabling/disabling devices** – allows turning on/off onboard hardware components (e.g., integrated sound or network adapters) at the firmware level.

**Why other options don't fit:**
- *Swap file size, device drivers, drive partition size* → these are managed by the **operating system** (e.g., Windows) after boot, not by the BIOS.

---

## 6. RAID Levels – Fault Tolerance with Minimum Disks

**Scenario:** A network admin needs disk fault tolerance for a web server using the **minimum number of disks**.

**Answer: RAID 1 (Mirroring)**

- Data is written identically to two disks simultaneously.
- If one disk fails, the other still holds a complete copy → no data loss.
- Requires only **2 disks**, the minimum possible for fault tolerance.

**Analogy:** Keeping an identical backup copy of an important document in two separate folders — lose one, and you still have the other.

**Why other RAID levels don't fit:**
- **RAID 0** – improves performance via striping, but offers **no fault tolerance** (one failed disk = total data loss)
- **RAID 5 / RAID 6** – provide fault tolerance but require **3+ disks**, making them less efficient when the requirement is the *minimum* disk count

---

## Quick Reference Table

| Topic | Answer | Key Reason |
|---|---|---|
| Resistance unit | Ohms | Measures opposition to current flow |
| Low CMOS battery sign | Wrong time/date | CMOS loses power, can't retain clock settings |
| A/V workstation key part | Specialized video card (GPU) | Handles heavy real-time video rendering |
| Chemical spill instructions | Safety Data Sheet (SDS) | Product-specific handling/disposal info |
| BIOS-editable settings | Boot order + Enable/disable devices | Firmware-level, pre-OS settings |
| RAID for min disks + fault tolerance | RAID 1 (Mirroring) | Only 2 disks needed; full redundancy |

---

*Notes compiled from a ~30-minute study session on IT Essentials hardware/firmware fundamentals.*
