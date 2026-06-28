# Printer & Mobile Device Study Notes
> IT Essentials — Printers, Mobile Devices & Troubleshooting

---

## 1. Printer Types & Core Mechanisms

### Laser Printer
- Uses **toner** (powder) applied to a drum via static electricity, then fused to paper using **heat** from the **fuser unit** (hot rollers).
- Key imaging steps: **Processing → Charging → Exposing → Developing → Transferring → Fusing → Cleaning**
  - **Developing**: Toner powder is attracted to the electrostatic "latent image" on the drum, making it visible.

### Inkjet Printer
- **Thermal inkjet nozzles**: Rapid heat generates a **steam bubble** inside the ink chamber, which expands and ejects ink onto paper.
- Relies entirely on **ink cartridges** — if empty, no output is produced at all.
- **Color mismatch** between screen and print → Fix: **Calibrate the printer**.

### Dot Matrix (Impact) Printer
- Uses pins to strike an **ink ribbon** against paper.
- Best for: **continuous-feed paper** and **multi-part carbonless forms** (e.g., 3-part invoices), because the impact force transfers through multiple layers.
- Faded/light print causes: **worn-out ribbon** or **damaged ribbon**.

### Thermal Printer
- Uses a **heating element (thermal head)** that touches heat-sensitive paper directly.
- Maintenance: Clean the heating element regularly with **isopropyl alcohol** to remove residue and extend printer life.

---

## 2. Printer Configuration Options

| Setting | Description |
|---|---|
| **Grayscale printing** | Prints using only black ink in varying shades |
| **Print layout** | Sets format: normal, banner, booklet, or poster |
| **Paper orientation** | Portrait (vertical) or landscape (horizontal) |
| **Collate** | Prints multi-page documents in complete sets (1-2-3, 1-2-3) |
| **Duplex** | Prints on both sides of the paper |

---

## 3. Printer Connectivity

| Method | Details |
|---|---|
| **USB** | Direct 1-to-1 connection between printer and one computer |
| **Ethernet** | Connects printer directly to a network (router/switch) for shared access |
| **Wi-Fi (IEEE 802.11)** | Most common wireless network printing method |
| **Bluetooth** | Short-range direct wireless connection between printer and device |

### Wireless Modes
- **Infrastructure**: Connects through a wireless access point (router) — standard for home/office.
- **Ad hoc**: Direct peer-to-peer connection without a router.

---

## 4. Print Server

### Hardware Print Server
- A dedicated device that manages print jobs independently.
- **Advantage**: Does not slow down client computers because it offloads all processing.

### Functions of a Print Server
1. **Queues print jobs** until the printer is ready.
2. **Provides shared print resources** to all connected client computers.

### Sharing a Locally Attached Printer (Disadvantages)
- Printer becomes **unavailable** when the host computer is rebooted or shut down.
- The host computer **may slow down** when processing other users' print jobs.

---

## 5. Printer Drivers

- Software that **converts a document** into a language the printer can understand — acts as a translator between the OS and the printer.
- **Installation order matters**: Some printers require the driver to be installed *before* connecting the hardware, to prevent the OS from loading an incorrect generic driver.
- **"Access Denied" during installation** → The user account lacks **administrative privileges**.
- **Additional Drivers button** (Printer Properties → Sharing tab): Stores drivers for other operating systems, so network clients can auto-download the correct driver.

---

## 6. Print Spooler

- A background software service that holds print jobs in a **queue** before sending them to the printer.
- **Error fix**: **Restart the print spooler** — clears frozen/corrupted jobs and restores printing.

---

## 7. Troubleshooting Common Printer Problems

| Problem | Cause(s) | Solution |
|---|---|---|
| **No output at all** (inkjet) | Empty ink cartridge | Replace cartridge |
| **No output, blank LCD** | Printer not powered on | Check power cable and power button |
| **Faded/light print** (laser) | Low toner cartridge; incompatible paper | Replace toner; use correct paper |
| **Faded/light print** (impact) | Worn or damaged ribbon | Replace ribbon |
| **Vertical lines/streaks** | Toner unevenly distributed | Remove cartridge and gently shake to redistribute toner |
| **Wrong colors** (inkjet) | Printer out of calibration | Calibrate the printer |
| **Paper jams** | High humidity; wrong paper type | Store paper properly; use correct paper |
| **Slow computer during printing** | Printer lacks sufficient RAM to buffer large images | Upgrade printer memory |

### Troubleshooting Step — After Applying a Fix
- Restarting the printer and printing a test page = **Verifying the solution and system functionality**.

---

## 8. Preventive Maintenance

- **Reset page counters** (if available) after each maintenance cycle to accurately track when parts next need service.
- Do **not** replace toner on a fixed schedule — replace based on actual depletion.
- Cleaning inkjet heads only after failure is **repair**, not **prevention**.

---

## 9. Mobile Devices

### Bluetooth
- Short-range wireless technology for device-to-device connections.
- To connect a Bluetooth headset to a smartphone:
  1. **Turn on Bluetooth** on the phone.
  2. **Pair the devices** — put the headset in pairing/discovery mode, then select it on the phone.

### NFC (Near Field Communication)
- Enables **tap-to-pay** and other close-proximity data transfer (within ~10 cm).
- Used in contactless payment terminals at retail stores.

### Swollen Battery Causes
- **Defective battery** (manufacturing fault)
- **Overcharging** (charging beyond capacity)
- **Incompatible charger** (incorrect voltage/current)

### Apps Won't Open
- If apps were installed on an **external SD card** and the card is removed, those apps cannot be launched.

### Touchscreen Laptops
- Require a **digitizer** — a hardware layer over the display that converts touch/pen input into digital signals.

---

## 10. Quick Reference — "Which printer for the job?"

| Requirement | Best Printer |
|---|---|
| Multi-part carbonless forms + continuous feed | **Dot matrix** |
| High-quality photo printing | **Inkjet** |
| High-volume office documents | **Laser** |
| Receipts / heat-sensitive labels | **Thermal** |
