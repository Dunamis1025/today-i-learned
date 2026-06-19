# IT Hardware Troubleshooting — Study Notes

A summary of computer hardware troubleshooting and components, covering storage, memory, cabling, and peripheral-sharing devices.

## Storage & Drives

**New drive not detected in BIOS**
Two things to check first:
- Data and power cables are properly connected (the drive needs power and a signal path to the motherboard).
- The drive's port is enabled in BIOS (a connected drive still won't show up if its controller/port is disabled in firmware settings).

**Drive type for a magnetic, fast, tower-compatible RAID setup → 3.5" 15K drive**
- *Magnetic*: a traditional HDD using spinning magnetic platters (vs. SSD/NVMe, which are flash-based/electronic).
- *Fast*: "15K" = 15,000 RPM, much faster than standard consumer HDDs (5,400–7,200 RPM).
- *Tower-compatible*: 3.5" is the standard form factor for desktop tower drive bays.

**Storage that connects directly to PCIe and is highly reliable → NVMe M.2**
- NVMe is a protocol built to talk directly to the high-speed PCIe bus, skipping the slower interfaces older drives use.
- M.2 is just the physical form factor (a small stick-shaped module).
- No moving parts + direct PCIe connection = faster performance and higher reliability than HDD/SATA SSD.

**Best components for a graphic design / programming / gaming build → dedicated GPU + SSD**
- *Dedicated GPU*: offloads heavy visual computation from the CPU, needed for gaming and design work.
- *SSD*: flash storage with near-instant data access, drastically cutting boot and load times vs. mechanical drives.

## Memory (RAM)

**Key feature of SDRAM → requires constant power to function**
SDRAM is volatile memory — it stores data in capacitors that lose charge over time, so it must be continuously powered and refreshed. Power loss = data loss.

**Motherboard with 2 black slots + 2 blue slots → dual-channel memory**
Color-coding marks dual-channel architecture. Installing matching RAM pairs into same-colored slots lets the system access both modules simultaneously, doubling the data bandwidth between RAM and CPU.

**DDR generations — pin count & voltage:**

| Type | Pins | Power | Notable feature |
|------|------|-------|------------------|
| DDR SDRAM | 184 | — | 2 reads/writes per CPU clock cycle |
| DDR2 SDRAM | 240 | 1.8V | — |
| DDR3 SDRAM | 240 | 1.5V | — |
| DDR4 SDRAM | 288 | — | Advanced error correction (ECC) support |

Each generation: more pins (prevents incompatible insertion), lower voltage (less heat/power use), added reliability features.

## Hardware Failure Diagnosis

**Random reboots → check for distended (bulging) capacitors → on the motherboard**
Capacitors are small cylindrical components that stabilize power delivery on the motherboard. Age or overheating can cause them to bulge or leak — a visible, classic sign of motherboard failure causing instability/reboots.

**Blotches/artifacts on screen during gaming — two likely causes:**
- *GPU overheating*: intense gaming load generates heat; if cooling fails, the GPU can malfunction and produce visual glitches.
- *Loose video cable*: a poorly seated or damaged HDMI/DisplayPort cable interrupts the signal, causing distorted images.

## Cabling

**RG-6 coaxial cable — main use: replacing cable TV wiring**
Designed for high-frequency signals (cable TV, satellite, broadband). Thicker center conductor + stronger shielding than older standards = longer-distance signal transmission with minimal loss/interference.

**Straight-through cable — why choose it: to connect a device to a wired network**
The standard Ethernet/patch cable for LAN connections (e.g., PC to switch/router/wall jack). Wiring maps pin-to-pin (pin 1 → pin 1), letting different device types communicate correctly.

## Client/Peripheral Devices

**Thin client setup step not needed for thick clients → connect the computer to the application server**
Thin clients have minimal local processing/storage and rely on a central server to run software, so connecting to that server is essential. Thick clients have their own local resources and can run software independently.

**Configuring LoJack on a laptop → enable it in BIOS**
LoJack is anti-theft software (tracking/remote wipe) built into the firmware level so it can survive even a wiped or replaced hard drive — it must be turned on in BIOS/UEFI, below the OS level.

**KVM switch — best description: lets one keyboard/mouse/monitor set control multiple computers**
KVM = Keyboard, Video, Mouse. It acts as a hub so a single set of peripherals can control several PCs, switching between them via button or shortcut — useful for server rooms or multi-PC desks.
