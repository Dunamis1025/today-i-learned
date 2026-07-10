# IT Essentials & Networking — Study Notes (Q20–Q50)

---

## Hardware

### Internal Storage
- **SATA** is the standard connector for internal hard drives and SSDs to the motherboard.
- USB, Thunderbolt, and eSATA are for **external** devices.

### Motherboard & Chipset
- **Northbridge** handles high-speed components: **RAM** and **Video Card**.
- **Southbridge** handles slower peripherals: USB, NIC, FireWire.

### CPU Upgrade Compatibility
- When upgrading a CPU, always verify compatibility with:
  1. **Motherboard** — socket type must match.
  2. **Power Supply** — must support the new CPU's power draw.

### RAM
- **DDR3** is a type of RAM (memory module) installed into the motherboard.

### BIOS / Firmware
- **EEPROM** (Electrically Erasable Programmable Read-Only Memory) is the solid-state technology that allows BIOS to be **flashed (updated)**.
- ROM = read-only, cannot be updated. SODIMM/SDRAM = volatile system memory, not firmware.

### Power Supply
- A **faulty power supply** is the most likely cause of a computer randomly rebooting — it fails to deliver consistent power.

### UPS (Uninterruptible Power Supply)
- Contains an internal battery; instantly switches to battery power during an outage.
- Gives time to **save data and safely shut down**.
- Also **conditions power quality** — critical for 24/7 mission-critical equipment.
- **Surge suppressor** only protects against voltage spikes — no battery, no backup.
- **APC** is a brand (manufacturer) of UPS devices, not a separate technology.

### Memory Card Reader
- Reads data from flash memory cards (SD, CF, etc.) used in cameras and mobile devices.

### KVM Switch
- Stands for **Keyboard, Video, Mouse**.
- Allows one set of keyboard/mouse/monitor to control **multiple computers**.
- Connectors: green (keyboard), purple (mouse), blue (monitor/VGA).

### MAC Address
- A MAC address is **48 bits** (6 bytes), represented as 12 hexadecimal digits.
- It is a globally unique hardware identifier for every network interface.

---

## Troubleshooting

### Random Reboots
- Most likely cause: **power supply** failure.

### Clicking Noise from Computer
- A loud **clicking sound** from a hard drive is a sign of mechanical failure (head/platter damage).
- **Immediate action**: inspect and back up data before total drive failure.

### Laptop Keyboard Key Not Responding
- First solution: **clean with compressed air** to remove debris trapped under keys.

### Wireless Network Not Showing on Laptop
- Quickest fix: press the **function key (Fn + F-key)** — it toggles the wireless NIC on/off.
- Look for an antenna or Wi-Fi icon on the key.

### Troubleshooting Process — Step 1
- Asking customers questions to gather symptoms = **"Identify the Problem"** step.

### Laser Printer Cleaning
- Use a **HEPA-capable vacuum** to safely remove excess toner particles.
- Regular vacuums allow fine toner particles to pass through; wet cloths can smear toner.

---

## Printers

### Shared Printer (Windows 10)
- To allow other Windows 10 computers to automatically download the correct driver, the person sharing must click the **"Additional Drivers"** button in printer properties.

### Default Printer
- When printing without manually selecting a printer, Windows sends the job to the **default printer**.

---

## Networking

### TCP/IP Model — 4 Layers
| Layer | Role |
|---|---|
| **Application** | User-facing apps (browser, email) |
| **Transport** | End-to-end delivery (TCP/UDP) |
| **Internet** | Logical addressing & routing (IP) |
| **Network Access** | Physical transmission (cables, Wi-Fi) |

### Intermediary vs. End Devices
- **Intermediary devices** (relay/forward traffic): **Switch**, **Modem**, Router
- **End devices** (source/destination): Computer, Printer, IP Phone

### DHCP
- Automatically assigns IP addresses to devices on a network.
- Eliminates the need to manually configure each workstation — ideal as a network grows.

### OLT vs. ONT (Fiber Networks)
| Device | Location | Role |
|---|---|---|
| **OLT** (Optical Line Terminal) | ISP's central office | "Parent" — manages traffic for the whole neighborhood |
| **ONT** (Optical Network Terminal) | Customer's premises | "Child" — converts optical signal for home/office use |

### SDN (Software-Defined Networking)
- The **SDN controller** sits in the middle and controls:
  - **Application layer** (top — defines what the network should do)
  - **Infrastructure layer** (bottom — physical hardware that carries traffic)

### NFC (Near Field Communication)
- Short-range wireless technology for **contactless "tap and pay"** payments.

---

## IPv6

### Compression Rules
1. **Drop leading zeros** in each 16-bit block: `0db8` → `db8`, `0100` → `100`
2. **Replace one contiguous run of all-zero blocks** with `::` (used only once)

**Example — Compress:**
`2001:0db8:cafe:0100:0f0d:0000:0000:00AA/96` → `2001:db8:cafe:100:f0d::AA/96`

**Example — Decompress:**
`2001:420:59:0:1::a/64` → `2001:0420:0059:0000:0001:0000:0000:000a`
- Restore all blocks to 4 digits with leading zeros.
- Replace `::` with enough `0000` blocks to total 8 groups.

---

## Cloud Models

| Model | Description |
|---|---|
| **Public** | Delivered over the internet to anyone |
| **Private** | Exclusive to a single organization |
| **Community** | Shared by organizations with common functional needs |
| **Hybrid** | Combination of two or more cloud types |

---

## Virtualization

### Hypervisor
- Software that enables **PC virtualization** — partitions one physical machine so multiple virtual operating systems run simultaneously.

### Use Case
- Run **legacy applications** incompatible with the current OS by running an older OS inside a virtual environment.

---

## Mobile Devices

### Battery Replacement Indicators
Replace a mobile battery when:
- Battery **overheats** during use
- Battery is **leaking** (physical failure, safety risk)

> Screen issues or brightness problems are typically software/display issues, not battery-related.

---

## Laptop Maintenance

### Before Cleaning a Laptop
1. **Disconnect from the electrical outlet**
2. **Remove all installed batteries**

Safety first — ensure no electricity is flowing before handling internal components.
