# PC Hardware Troubleshooting Guide

A comprehensive reference for diagnosing and resolving common computer hardware issues.

---

## 1. Display Problems & Solutions

| Problem | Solution |
|---|---|
| **No image (power is on)** | Check/replace video cable; use `Fn` key combo to switch to external display (laptops) |
| **Flickering screen** | Adjust refresh rate; replace the inverter component |
| **Dim image** | Calibrate LCD backlight per repair manual |
| **Dead pixels / missing color** | Contact the manufacturer |
| **Artifacts (flashing lines/patterns)** | Check display connections; clean dust from internals; replace GPU |
| **Incorrect color patterns** | Check display connections; inspect/replace GPU |
| **Distorted image** | Restore factory display settings; check internal connections; inspect/replace GPU |
| **Ghost image (burn-in)** | Power off and unplug for a few hours; use degauss feature; replace display if unresolved |
| **Distorted geometry** | Update/reinstall GPU driver in Safe Mode; correct geometry via display settings |
| **Oversized images/icons** | Update/reinstall GPU driver in Safe Mode; adjust resolution in display settings |
| **Misaligned multiple monitors** | Use display control panel to identify and realign monitors; update GPU driver in Safe Mode |
| **VGA mode (low resolution)** | Reboot normally (may be in Safe Mode); update/reinstall GPU driver in Safe Mode |

---

## 2. General Hardware Problems & Solutions

| Problem | Solution |
|---|---|
| **RAID not found / stops working** | Check power to RAID controller; reconfigure BIOS; install correct drivers; replace RAID controller |
| **Slow performance** | Add more RAM; clean or add cooling fans to prevent overheating |
| **External drive not recognized** | Install correct drivers; attach external power or remove other USB devices (insufficient USB power) |
| **Won't boot after BIOS update** | Restore firmware from onboard backup; use second BIOS chip; contact manufacturer |
| **Random reboots / lockups / BSOD** | Test RAM modules; reset motherboard to factory defaults; lower FSB/CPU multiplier/voltage |
| **Slower after CPU upgrade** | Update BIOS firmware to support the new multi-core CPU |
| **"Cannot read from source disk" error** | Replace the failing disk |
| **Won't power on** | Check power cable and power strip; inspect PSU and motherboard power connectors |
| **System freeze / Blue Screen** | Check for overheating; reseat RAM; update GPU driver; remove non-essential peripherals |
| **"Disk not found" on boot** | Check SATA/data cable connection between HDD and motherboard; verify boot order in BIOS |
| **Beep codes on boot** | Refer to motherboard manual to decode beep pattern (RAM failure, GPU error, etc.) |
| **OS won't load** | Boot into Safe Mode; remove recently installed drivers/programs; use Windows recovery to restore system files |

---

## 3. Diagnostic Tools

### Multimeter
- Insert **black probe → COM jack**, **red probe → + jack**
- Used to measure electrical properties (e.g., battery voltage)
- Handle with care — sensitive equipment; avoid drops and beware of high voltage

### Power Supply Tester
Connectors testable: `20/24-pin motherboard`, `Molex`, `PCI-E`, `SATA`, `Berg`, `P4/P8`

**Test procedure:**
1. Turn off PSU
2. Plug in the connector to test
3. Switch PSU on
4. Check if LEDs illuminate

**Expected LEDs (if PSU is healthy):** `+12V` · `-12V` · `+5V` · `-5V` · `+3.3V` · `PG`

> If LEDs don't light up, verify all connections. If still failing, consult an instructor or replace the PSU.

---

## 4. Technician Reference Tools & Documentation

| Tool | Purpose |
|---|---|
| **Notes** | Avoid repeating steps; track what to do next during a repair session |
| **Journal** | Record problem descriptions, attempted solutions, steps taken, config changes, and replaced parts |
| **History of Repairs** | Track past work on a specific machine (dates, parts replaced, customer info) |
| **Troubleshooting Guides / Manuals** | Quick reference for known issues and manufacturer-specific procedures |
| **Online Forums & Chat Sites** | Community Q&A for specific technical issues |
| **Manufacturer FAQs** | Official answers to common product-specific problems |
| **Internet Search Engines** | Broad search for hardware-specific solutions |
| **Technical Websites & News Groups** | In-depth articles, alerts, and OS-specific discussions (Windows, macOS, Linux) |
