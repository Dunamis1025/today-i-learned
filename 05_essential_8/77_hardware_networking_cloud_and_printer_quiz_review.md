# CompTIA A+ Study Notes

## Q1 — ESD (Electrostatic Discharge)
**Scenario:** Walking across carpet then touching a keyboard connected to a tower PC.

Static electricity builds up through friction (e.g., walking on carpet). Touching a device connected to a PC lets the charge travel through the cable into sensitive components like the motherboard, potentially destroying them. Always use an anti-static wrist strap when handling hardware.

---

## Q2 — ACPI (Advanced Configuration and Power Interface)
**Answer:** ACPI

Acts as the bridge between laptop hardware and the OS. It enables power management features like sleep modes, wake events, and battery optimization. Technicians use it to configure performance-based power schemes.

---

## Q3 — Virtualization & Disaster Recovery
**Answer:** Hardware does not have to be identical.

Virtual machines are stored as files (not tied to specific hardware). In a disaster, those VM files can be restored to any compatible host server — no need for identical replacement equipment. This enables fast, flexible recovery.

---

## Q4 — Shared Printer Security Risks
**Answer:** Document viewing in the print queue / Cached files

- **Print queue exposure:** Unauthorized users may see documents waiting to be printed.
- **Cached files:** Printers store recent print jobs in memory/storage. If not cleared, sensitive data can be retrieved later.

---

## Q5 — LAN (Local Area Network)
**Answer:** LAN

Covers a single building or campus. Connects devices within the same organization for file sharing, printing, and internet access. Fast and private compared to wide-area networks.

---

## Q6 — File & Printer Sharing Protocol (Windows)
**Answer:** SMB (Server Message Block)

The standard Windows protocol for sharing files, printers, and resources across a network. It's what makes "shared folders" and "shared printers" work in a Windows environment.

---

## Q7 — Windows Virtual Desktop
**Answer:** Windows Virtual Desktop

Allows creating multiple independent workspaces on one physical machine. Users can group apps by task (e.g., design tools on Desktop 1, browser on Desktop 2) and switch between them without cluttering a single screen.

---

## Q8 — APIPA Address (169.254.x.x)
**Answer:** Unreachable DHCP server

When a computer can't reach the DHCP server (usually the router) to get an IP address, Windows auto-assigns a 169.254.x.x address (APIPA). This address can't communicate with the internet — it signals a failed DHCP connection.

---

## Q9 — DDR SDRAM
**Answer:** Transfers data twice per clock cycle (vs. once for SDRAM)

DDR = Double Data Rate. Regular SDRAM sends data once per clock cycle. DDR sends data on both the rising and falling edge, doubling the throughput without increasing clock speed.

---

## Q10 — Cleaning Computer Components
**Answer:** Hold compressed air cans upright while spraying

Tilting or inverting a compressed air can releases cold liquid propellant, which can thermally shock and damage components. Also:
- Don't force fans to spin too fast (damages motor)
- Don't use window cleaner on LCD screens (strips anti-glare coating)

---

## Q11 — VA (Vertical Alignment) LCD
**Answer:** Vertical Alignment (VA)

VA panels align liquid crystals vertically to block backlight more effectively, producing deeper blacks and a much higher contrast ratio than TN or IPS panels. Best for media consumption and dark-scene content.

---

## Q12 — UDP vs TCP
**Answer:** UDP is preferred when delivery guarantee isn't needed / when speed is critical

- **TCP** = reliable, confirms every packet received ("registered mail")
- **UDP** = fast, no confirmation ("regular mail")

UDP is ideal for real-time gaming, video calls, and live streaming where speed > perfect delivery.

---

## Q13 — Enterprise Hypervisors for Data Centers
**Answer:** VMware ESX/ESXi / Microsoft Hyper-V 2012

- **Type 1 (bare-metal) hypervisors** run directly on hardware — designed for data center workloads with high performance, security, and availability.
- VMware ESXi and Hyper-V are enterprise-grade Type 1.
- VirtualBox / VMware Fusion are Type 2 (run on top of an OS) — suitable for personal/test use only.

---

## Q14 — Testing on Multiple OS (Windows 10 & 11)
**Answer:** Dual boot / Client-side virtualization

- **Dual boot:** Install two OSes on one machine; choose which to load at startup.
- **Client-side virtualization:** Run a virtual machine (e.g., Windows 11) inside the current OS using software like Hyper-V or VirtualBox.

Both methods allow multi-OS testing without extra hardware.

---

## Q15 — UTM (Unified Threat Management)
**Answer:** UTM

A single security appliance that combines: firewall, VPN, IDS/IPS, and DoS/DDoS protection. Simplifies management by consolidating multiple security functions into one device.

---

## Q16 — "RAID Not Found" After Power Outage
**Answer:** The external RAID controller is not receiving power

RAID controllers manage disk arrays. If the external controller loses power (or wasn't properly restored after an outage), the server can't detect the disk group and throws a "RAID not found" error.

---

## Q17 — Cloud Service for App Development & Deployment
**Answer:** PaaS (Platform as a Service)

PaaS provides a pre-configured platform (servers, storage, networking) so developers can focus on writing and collaborating on code — not managing infrastructure. Ideal for web app development teams.

---

## Q18 — Paper Jams in Humid Environment
**Answer:** Too much humidity

Paper absorbs moisture in damp environments, causing sheets to stick together or lose rigidity. This leads to misfeeding and frequent paper jams. Store paper in a dry area and check environmental conditions before installing printers.

---

## Q19 — Slow Printing of Graphics/Photos
**Answer:** Upgrade the printer's RAM

Printing high-resolution images requires processing large data sets. Insufficient RAM causes the printer to slow down significantly. More RAM = faster processing of complex print jobs.

---

## Q20 — Touchscreen Not Responding / Inaccurate
**Answer:** The digitizer is faulty

The digitizer sits over the display and converts touch input into digital signals. A damaged or failing digitizer causes unresponsive or inaccurate touch behavior. Replacing the digitizer resolves the issue.

---

## Q21 — BIOS Hardware Failure Indication
**Answer:** The computer emits a pattern of beeps (beep codes)

During POST (Power-On Self-Test), the BIOS checks hardware before the display is ready. If a critical failure is found, it signals the problem via beep codes from the internal speaker. The pattern (number/length of beeps) identifies which component is failing.

---

## Q22 — IPv6 Host Identifier
**Answer:** `0607:1234:aa10:ba01`

IPv6 address: `2001:0DB8:75a3:0214:0607:1234:aa10:ba01 /64`

- `/64` means the first 64 bits = network portion (first 4 segments)
- Last 64 bits = host identifier / interface ID (last 4 segments)
- Host ID: `0607:1234:aa10:ba01`

---

## Q23 — Inkjet vs Laser Printer Differences
**Answer:** Output dryness / Initial purchase cost

| Feature | Laser | Inkjet |
|---|---|---|
| Output | Dry immediately (toner fused by heat) | May be wet (liquid ink) |
| Upfront cost | More expensive | Less expensive |

---

## Q24 — ATX Motherboard Replacement
**Answer:** CPU may need to be replaced

Different motherboards use different CPU socket types. If the new ATX motherboard has a different socket, the existing CPU may be incompatible and must be replaced.

---

## Q25 — Laser Printer Maintenance Kit Contents
**Answer:** Pickup rollers / Transfer rollers / Fuser assembly

| Component | Function |
|---|---|
| Pickup rollers | Pull paper from tray; wear causes feed failures |
| Transfer rollers | Move toner from drum to paper; wear causes faded prints |
| Fuser assembly | Uses heat to bond toner to paper; failure causes smearing/flaking |

---

## Q26 — Cleaning Inside a Computer
**Answer:** Dust

Fans draw in air continuously, accumulating dust on components. Dust blocks airflow, traps heat, and can cause electrical shorts. Regular cleaning improves airflow, lowers temperatures, and extends hardware lifespan.
