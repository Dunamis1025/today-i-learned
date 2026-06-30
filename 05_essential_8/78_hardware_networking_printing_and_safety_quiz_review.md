# CompTIA A+ Study Notes — Questions 27–50

---

## Q27 — Environmental Hazard for Laptops in a Furniture Factory
**Answer: Dust**

The fans in a laptop continuously pull air in, drawing airborne wood particles inside. Accumulated dust clogs vents and coats components, causing overheating. Combined with high humidity (70%), dust becomes sticky and can corrode circuits or cause short circuits. The temperature (27°C) is within normal operating range, but dust is the primary physical threat.

---

## Q28 — True Statement About Laptops vs Desktops
**Answer: Most internal laptop components cannot be used in desktops**

Laptops use miniaturized, proprietary components designed for portability and low power. These differ in physical form factor and electrical specs from standardized desktop parts. Laptop CPUs, RAM, and GPUs are not compatible with desktop motherboards. Also: laptop motherboards are chassis-specific (no standard form factor like ATX), and laptops do require dedicated cooling systems.

---

## Q29 — Purpose of a Safety Data Sheet (SDS)
**Answer: To specify procedures for handling potentially hazardous materials**

An SDS provides guidelines for safe handling, storage, and disposal of hazardous substances. It includes health risk information, emergency response procedures, and protection protocols for workers.

---

## Q30 — BIOS Security Features
**Answer: Drive Encryption, Passwords, TPM**

| Feature | Function |
|---|---|
| Drive Encryption | Encrypts hard drive data so unauthorized users can't read it |
| Passwords | Requires authentication to access BIOS or boot the system |
| TPM (Trusted Platform Module) | Hardware chip that stores encryption keys and validates system integrity |

---

## Q31 — Safety Hazards When Working with Laser Printers
**Answer: High Voltage and Hot Components**

- **High Voltage**: Internal high-voltage power supply creates static for printing; residual charge remains even after unplugging — risk of electric shock.
- **Hot Components**: The fuser unit melts toner onto paper at extremely high temperatures; touching it right after printing can cause severe burns.

---

## Q32 — Collate Print Order
**Answer: 1, 2, 3, 1, 2, 3**

- **Collated**: Prints one complete set at a time → `1, 2, 3 | 1, 2, 3`
- **Uncollated**: Prints all copies of each page → `1, 1, 2, 2, 3, 3`

---

## Q33 — Customer-Replaceable Laptop Components
**Answer: Battery and RAM**

- **Battery**: Designed as a consumable; often removable without tools.
- **RAM**: Accessible via a dedicated panel on the laptop's underside.
- Other parts (display, integrated card reader, mini-PCIe modules) require significant disassembly — not suitable for customer-level replacement.

---

## Q34 — Motherboard Section for Installing a Video Card
**Answer: Section D (PCIe slots)**

- Section D = PCIe expansion slots → for video/graphics cards
- Section C = RAM slots
- Section A = Main power connector
- Section B = Rear I/O ports

---

## Q35 — Component Connected via SATA Cable
**Answer: Optical Drive**

SATA cables connect storage devices (HDD, SSD, optical drives) to the motherboard for data transfer.
- Video card → PCIe slot
- Power supply → dedicated power cables
- Network card → PCIe slot or onboard

---

## Q36 — Best Use Case for Wi-Fi Calling on a Corporate Device
**Answer: When in an area with poor cellular coverage**

Wi-Fi Calling routes voice and text over a Wi-Fi network instead of cellular. Most useful in basements, large buildings, or remote areas with weak cell signal.

---

## Q37 — Power Supply Set to 230V Plugged into 110V Outlet
**Answer: The PC will not turn on**

The power supply needs input voltage within its configured range. 110V is too low to trigger startup when set to 230V. (Note: the reverse — 110V setting in a 230V outlet — causes immediate hardware damage or failure.)

---

## Q38 — Motherboard Connector for Installing an Internal HDD
**Answer: SATA**

SATA is the standard data interface for HDDs and SSDs. Other connectors:
- PCI → expansion cards
- ATX → main power supply
- PWR_SW → case power button

---

## Q39 — Required IPv4 Values for Basic Network Connectivity
**Answer: IP Address, Subnet Mask, Default Gateway**

| Value | Purpose |
|---|---|
| IP Address | Unique identifier for the device on the network |
| Subnet Mask | Defines which part of the IP is the network vs. host |
| Default Gateway | Router address used to reach external networks |

---

## Q40 — Two Types of Wired High-Speed Internet
**Answer: Cable and DSL**

- **Cable**: Uses coaxial TV cables for high-speed internet.
- **DSL**: Uses existing telephone lines; allows simultaneous voice and data.
- Dial-up = not high-speed; Cellular & Satellite = wireless.

---

## Q41 — RAID Level Using Both Mirroring and Striping
**Answer: RAID 10**

| Technique | Effect |
|---|---|
| Striping | Splits data across drives → faster performance |
| Mirroring | Duplicates data across drives → redundancy/protection |
| RAID 10 | Combines both → speed + reliability |

---

## Q42 — Proper Way to Dispose of Old RAM
**Answer: Recycle following local regulations**

Electronic components may contain hazardous materials (heavy metals). Improper disposal (landfill, incineration) pollutes the environment. Always use authorized e-waste recycling facilities per local laws.

---

## Q43 — Components That Can Cause Random Reboots
**Answer: CPU and Power Supply**

- **CPU**: Overheating triggers automatic shutdown/reboot to prevent damage.
- **Power Supply**: Unstable or insufficient power delivery causes unexpected reboots or crashes.

---

## Q44 — Port 389 = Which Protocol?
**Answer: LDAP (Lightweight Directory Access Protocol)**

LDAP manages and queries directory information (user accounts, devices, org data) over a network. Default port: **389**.

---

## Q45 — Compressing an IPv6 Address
**Original**: `fe80:09ea:0000:2200:0000:0000:0fe0:0290`

**Rules:**
1. Remove leading zeros in each group: `09ea → 9ea`, `0fe0 → fe0`, `0290 → 290`
2. Replace longest consecutive all-zero groups with `::` (used only once)

**Result**: `fe80:9ea:0:2200::fe0:290`

---

## Q46 — ACPI Power State: CPU & RAM Off, RAM Saved to Disk
**Answer: S4 (Hibernate)**

S4 saves the entire RAM contents to the hard drive before fully powering off. On restart, data is loaded back from disk, restoring the previous session.

| State | Description |
|---|---|
| S1–S3 | Sleep states (RAM still powered) |
| S4 | Hibernate (RAM saved to disk, full power off) |
| S5 | Full shutdown |

---

## Q47 — Paper Not Feeding into Printer — Two Possible Causes
**Answer: Paper size mismatch and wrinkled paper**

- **Size Mismatch**: Printer settings don't match the paper loaded in the tray → printer detects error and stops feeding.
- **Wrinkled Paper**: Damaged paper prevents pickup rollers from gripping sheets properly.

---

## Q48 — D: Drive Not Visible — How to Check if OS Recognizes It
**Answer: Use Disk Management (Control Panel)**

Disk Management is the standard Windows tool to view drive status, initialize disks, create partitions, and assign drive letters. If the hardware is physically connected, it will appear here even without a drive letter.

---

## Q49 — App Not Responding on Laptop
**Answer: The app needs to be restarted**

When an app freezes, the first step is to close and relaunch it to clear memory conflicts or temporary errors. This is the most probable and simplest cause before investigating hardware or OS issues.

---

## Q50 — Printed Documents Show Garbled/Unknown Characters
**Answer: Re-install the printer driver**

The printer driver translates computer data into printer-readable language. If corrupted or misconfigured, the printer outputs garbage text. Re-installing the driver restores correct communication.

---

*Study session: Q27–50 | Topics: Hardware, Networking, Printing, Safety, Storage, Power Management*
