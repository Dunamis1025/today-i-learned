# Computer Hardware Troubleshooting — Study Notes

## 1. Storage Device Issues

### Storage Device Not Recognized
- **Causes:** Loose power/data cables, incorrect jumper settings, device failure, incorrect BIOS settings
- **Solutions:** Secure all cables, check/reset jumpers, replace the device if faulty, reset storage settings in BIOS

> **What is a Jumper?**
> A jumper is a small physical connector on a motherboard or hard drive. A tiny plastic cap is placed over metal pins to bridge or disconnect them, physically changing the hardware's configuration. On older IDE drives, jumpers set the device role as **Master** (primary) or **Slave** (secondary). Modern SATA drives do not require jumper settings.

### External Drive Not Recognized
- **Causes:** Poor connection, disabled ports in BIOS, faulty drive
- **Solutions:** Re-insert the drive, enable external ports in BIOS, replace the drive if faulty

### Memory Card Not Recognized
- **Causes:** Unsupported card type, incorrect connection, improper BIOS configuration, faulty reader
- **Solutions:** Use a compatible card, check physical connection of the reader, reconfigure BIOS settings, replace the reader

---

## 2. Optical Drive (CD/DVD) Issues

### Disc Not Recognized
- **Causes:** Disc inserted upside down, multiple discs inserted, damaged disc, wrong file format, faulty drive
- **Solutions:** Re-insert disc correctly, ensure only one disc is present, try a different disc, replace the optical drive

### Disc Won't Eject
- **Causes:** Jammed drive, software lock, hardware failure
- **Solutions:** Insert a pin into the emergency eject hole next to the eject button, reboot to clear software locks, replace the drive if faulty

---

## 3. USB Issues

### Slow USB Data Transfer
- **Causes:** Motherboard does not support USB 3.0, incorrect BIOS port speed settings
- **Solutions:** Upgrade to a USB 3.0-capable motherboard or install an expansion card, set port speed to "high speed" in BIOS

---

## 4. Motherboard Issues

### Computer Won't Start (Fans Spin, No Beeps)
- **Causes:** POST (Power-On Self-Test) failure, faulty cabling, improperly seated or damaged CPU
- **Solutions:** Reseat the CPU, check all internal cables, inspect the motherboard for damage

### System Boots to Wrong Device
- **Causes:** Media left in a removable drive, incorrect boot order in BIOS
- **Solutions:** Remove unnecessary media, correct the boot order in BIOS settings

### Clock Resets or BIOS Settings Lost
- **Causes:** CMOS battery is loose or dead
- **Solutions:** Reseat the CMOS battery; replace it if the problem persists

### No Video After Installing a New GPU
- **Causes:** Monitor still connected to motherboard, onboard video not disabled in BIOS, auxiliary power not connected
- **Solutions:** Connect monitor to the new GPU, disable onboard video in BIOS, connect PCIe power cable to the GPU

### Sound Card / NIC Not Working
- **Causes:** Onboard audio or LAN still enabled in BIOS conflicting with new card
- **Solutions:** Disable onboard audio/LAN in BIOS, reseat the card in a different expansion slot, replace the card if faulty

### Hard Drive Activity LED Not Lighting Up
- **Causes:** LED cable loose, disconnected, or plugged in with wrong polarity
- **Solutions:** Reconnect the LED cable to the correct motherboard header, check +/- orientation

### BIOS Update Failure
- **Causes:** Interrupted or failed BIOS flash
- **Solutions:** Contact the motherboard manufacturer for a replacement BIOS chip; if the board has two BIOS chips, switch to the backup chip

### CPU Not Recognized Correctly
- **Causes:** Outdated BIOS firmware
- **Solutions:** Update BIOS to the latest version, reconfigure CPU settings in the BIOS advanced menu

### Damaged Motherboard Capacitors
- **Causes:** Heat, power surges, or voltage spikes
- **Symptoms:** Capacitors appear **distended**, **swollen**, **bulging** (top puffed outward like a dome), or are **leaking residue**
- **Solution:** The motherboard must be replaced — there is no repair option

> **What does "bulging" mean?**
> A healthy capacitor has a flat top. A bulging capacitor has its top pushed outward into a dome shape due to internal pressure buildup — similar to a bloated food can. It is a clear sign of physical damage.

---

## 5. Power Supply Unit (PSU) Issues

### Computer Won't Turn On
- **Causes:** Unplugged cord, faulty power cord, PSU switch off, incorrect voltage setting, loose internal power connector, failed PSU
- **Solutions:**
  1. Confirm the power cord is plugged into a working outlet
  2. Replace the power cord if faulty
  3. Check the PSU switch on the back of the case is set to ON
  4. Verify voltage selector is set correctly
  5. Reseat the front panel power button connector on the motherboard
  6. Replace the PSU if all else fails

### Computer Reboots, Shuts Down Unexpectedly, or Smells of Burning
- **Causes:** PSU is failing
- **Signs:** Unexpected reboots or shutdowns, smell of burning electronics, visible smoke
- **Solution:** Stop using the computer immediately and replace the PSU

---

## 6. Display / Monitor Issues

### No Image on Screen
- **Causes:** Loose video cable, wrong input source selected, monitor not powered on, brightness too low
- **Solutions:** Reseat the video cable, select the correct input source (HDMI/DisplayPort), power on the monitor, adjust brightness

### Blurry or Distorted Image / Incorrect Colors
- **Causes:** Damaged or bent video cable
- **Solutions:** Replace the video cable

### Low Resolution / Small Text
- **Causes:** Incorrect resolution setting, outdated or missing graphics driver
- **Solutions:** Set resolution to the monitor's native recommended resolution in Display Settings, update the graphics driver

### Screen Flickering
- **Causes:** Cable too long, electromagnetic interference from nearby devices (e.g., speakers)
- **Solutions:** Use a shorter cable, move interfering devices away from the monitor

---

## 7. CPU, RAM & Performance Issues

### Computer Won't Boot or Locks Up (Overheating)
- **Causes:** CPU overheating
- **Solutions:** Reinstall CPU with fresh thermal paste, replace the CPU fan, add case fans for better airflow

### Unexpected Reboots / System Errors
- **Causes:** Front-side bus, CPU multiplier, or CPU voltage set too high (overclocking instability)
- **Solutions:** Lower overclocking settings or reset BIOS to factory defaults

### CPU Won't Install
- **Causes:** Wrong CPU socket type
- **Solution:** Replace with a CPU that matches the motherboard's socket

### Dual-Core CPU Shows Only One Core Graph
- **Causes:** BIOS does not recognize the new CPU
- **Solution:** Update BIOS firmware

### RAM Not Recognized
- **Causes:** Faulty RAM, wrong RAM type, mismatched sticks, RAM not fully seated
- **Solutions:** Replace or reseat the RAM, ensure the RAM type is compatible with the motherboard

### Slow Performance After Windows Upgrade
- **Causes:** Insufficient RAM, GPU with insufficient VRAM
- **Solutions:** Install additional RAM, upgrade to a GPU with more video memory

---

## Quick Reference — First Steps for Any Issue

| Symptom | First Thing to Try |
|---|---|
| Device not recognized | Reseat cables / reconnect the device |
| No display | Check cable connection and input source |
| System won't boot | Check power connections and BIOS settings |
| Slow performance | Check RAM, drivers, and BIOS settings |
| Unexpected shutdowns | Check PSU and CPU temperatures |
| Physical damage visible | Replace the damaged component |
