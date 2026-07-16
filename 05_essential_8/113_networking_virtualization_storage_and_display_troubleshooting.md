# IT Fundamentals Study Notes (Q32–Q80)

A study summary covering networking, hardware, printers, displays, storage, and troubleshooting concepts (CompTIA-style review).

---

## Networking

**Proxy server** — Caches frequently visited web content for faster local access and hides internal IP addresses from external sites, adding a layer of security.

**Private IP addressing** — Devices on small office/home networks typically use private IPs internally; a router translates these to a single public IP via NAT, improving security and conserving public addresses.

**Hub vs. Switch** — A hub broadcasts incoming data to *all* ports regardless of destination, making it inefficient and less secure. A switch sends data only to the intended device.

**Access Point (AP)** — Bridges a wired network to wireless devices using radio waves (Wi-Fi), letting laptops/phones connect without cables.

**Mobile data connections** — Tablets/smartphones connect to networks via **cellular** (4G/LTE/5G, carrier-based, wide-area) or **Wi-Fi** (local router-based).

**APIPA** — If no DHCP server is reachable, a computer self-assigns an address in the `169.254.x.x` range, allowing local network communication without internet access.

**RDP port** — Remote Desktop Protocol uses **port 3389**; this must be open on the remote PC's firewall.

**802.11n** — Supports both 2.4 GHz and 5 GHz bands (dual-band), giving faster 5 GHz throughput while staying backward-compatible with older 2.4 GHz devices.

**QoS & traffic engineering (VoIP)** — Prioritizes voice packets over other traffic, reducing **latency** (delay) and **jitter** (inconsistent packet timing) for clear calls.

**Duplicate IP address** — Causes "document failed to print" errors on printer restart; the printer can't reconnect if another device already holds its IP.

**Printer not appearing on network** — First fix: **manually add the printer's IP address** rather than replacing hardware.

**Thin client vs. thick client (remote office)** — Key deciding factor: **internet bandwidth between main and remote office**. Thin clients rely on constant server communication (need high bandwidth); thick clients process locally and tolerate weaker connections.

---

## Virtualization

**Hypervisor installation requirement** — Needs **virtualization software**; the hypervisor itself is the software that lets one physical machine run multiple OSes simultaneously.

**Virtual desktop networking** — Requires a **virtual NIC** (software-based network card) so the virtual machine can communicate with the network.

**Virtualization workstation build** — Needs **multicore processors** (handle multiple VMs' processing) and **maximum RAM** (memory for each VM). Graphics cards/monitors/cooling are not core requirements.

---

## Storage / RAID

**RAID 0** — Stripes data across drives for speed and easy capacity expansion, but has **no redundancy** — one drive failure loses all data.

**RAID 5** — Combines striping with parity (recovery data) across ≥3 drives. Balances cost, capacity, and fault tolerance — good when budget is limited but some data protection is needed.

**ECC memory** — "Error Correction Code" RAM automatically detects/fixes memory bit errors. Best choice for database workstations where data integrity is critical.

**Second hard drive not visible** — Check **File Explorer** first, then **Disk Management** to see if Windows physically detects the drive.

**Loud clicking noise from a computer** — Classic symptom of **hard drive** mechanical failure (read/write head malfunction); back up data immediately.

**Unexpected reboots during use** — Likely caused by a failing **power supply** (unstable voltage) or a faulty **motherboard** (overheating/damage).

---

## Displays

**HDMI** — Single cable carrying both digital video and audio; standard for TVs, consoles, and computers.

**Native resolution** — Matches the LCD's actual physical pixel count 1:1; fixes oversized/blurry icons and images caused by non-native resolution settings.

**OLED** — Self-lit pixels turn off completely for true black, using less power and requiring no backlight — resulting in a thinner, lighter, more energy-efficient display than LCD/LED.

**Inverter** — Powers the LCD backlight. A failing inverter causes a **dull, pale, or dim screen**, and can also cause **flickering**. Requires professional replacement (deep inside the display housing).

**Screen refresh rate mismatch** — Another cause of laptop screen flickering, alongside inverter failure.

**External display not showing laptop screen** — Check: (1) **video cable firmly connected**, (2) **laptop is actually sending signal to the external device** (via Fn key / display mode toggle).

---

## Laptops

**Function keys (Fn)** — Dual-purpose keys on laptops; combined with the Fn key they control hardware settings (brightness, volume, Wi-Fi toggle) to save keyboard space.

**Inverter replacement** — Requires a professional technician (deep disassembly), unlike hard drive/battery/RAM which are user-replaceable.

**Docking station vs. port replicator** — A docking station additionally provides: **extra optical drive**, **PCI cards**, **additional hard drive** — true internal expansion, unlike a port replicator which only extends basic ports.

**Intermittent Wi-Fi disconnects (802.11n card)** — First step: **move the laptop to a new location** to rule out interference/obstacles before hardware/software fixes.

---

## Desktop Hardware

**Front panel connections** — Must connect to motherboard headers: **drive activity light**, **USB connectors**, **PC power button**.

**PCIe graphics card power (100W draw)** — Supplied by both the **motherboard's PCIe slot (~75W max)** and a **separate PCIe power connector from the PSU** for the remainder.

**CPU overheating** — Causes frequent lockups with no error message, recurring immediately after restart since the CPU has no time to cool down.

**CAD workstation build** — Needs **SSD** (fast file access), **specialized graphics card** (3D rendering), and **maximum RAM** (large design files).

---

## Printers

**Fuser assembly & pickup rollers** — Common field-replaceable parts in laser printer maintenance kits. Fuser bonds toner to paper via heat/pressure; pickup rollers feed paper (wear causes jams).

**Vertical lines on every page** — Check the **toner cartridge** first (often contains the imaging drum/developer roller causing the defect).

**Laser printer imaging process order** — Charging → **Exposing** (laser creates latent image) → Developing (toner applied) → Transferring → Fusing.

**Impact printer** — Uses a fabric ribbon struck by pins; faded print means the **ribbon** needs replacing (unlike laser/inkjet/thermal, which don't use ribbons).

**Inkjet color problems after cartridge swap** — Fix: **perform a printer head cleaning** to clear clogged nozzles (air bubbles/dried ink).

**Blank printer control panel** — Two causes: **printer not powered on**, or **screen contrast set too low**.

---

## Mobile / Peripherals

**Smartwatch** — Can make/receive phone calls directly, unlike GPS devices, VR headsets, or e-readers.

**GPS app not working** — First step: **ensure Location setting is enabled** before assuming hardware failure.

**USB 3.0 device running at ~450 Mb/s instead of 5 Gb/s** — Likely plugged into a **USB 2.0 port** (max ~480 Mb/s), which throttles the device to the slower standard.

---

## Servers & Protocols

**FTP server** — Uses two connections: a **control channel** (commands/replies) and a **data channel** (actual file transfer), enabling reliable large file transfers.

**Email decryption error** — Fix: **install an appropriate (digital) certificate** to unlock/read encrypted email content.

---

## Troubleshooting Methodology

**"I suspect a failed service pack caused this"** — This step is **Establish a theory of probable cause**, following user interview and preceding theory testing.
