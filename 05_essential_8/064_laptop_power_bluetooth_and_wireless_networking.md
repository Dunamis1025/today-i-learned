# Laptop Power Management, Bluetooth & Wireless Networking

> Study notes covering CompTIA A+ topics: power settings, Bluetooth, and wireless connectivity on laptops.

---

## 1. Power Management

### 1.1 Overview

- Advances in battery technology now allow laptops to run **10+ hours** on a single charge.
- **Power management** controls electricity flow to individual components.
- **ACPI (Advanced Configuration and Power Interface)** acts as a bridge between hardware and the OS, allowing the OS to control power states.

---

### 1.2 ACPI Power States

| State | Name | Description |
|-------|------|-------------|
| **S0** | Working | Computer is fully on; CPU is actively running. |
| **S1** | CPU Halt | CPU stops executing instructions, but CPU and RAM still receive power. Unused devices are powered down. |
| **S2** | CPU Off | CPU is powered off; RAM is still refreshed (lower power than S1). |
| **S3** | Sleep / Suspend | CPU off; RAM receives minimal power just to maintain its contents. |
| **S4** | Hibernate | CPU and RAM are both off. RAM contents are saved to a temporary file on the hard drive. |
| **S5** | Soft Off | Computer is completely off. All unsaved data is lost. |

> **Key distinction:** S3 (Sleep) keeps data in RAM. S4 (Hibernate) saves data to disk — uses the least power of any sleep state.

---

### 1.3 Managing ACPI in BIOS/UEFI

ACPI must be **enabled in BIOS/UEFI** for the OS to control power states.

**Steps to enable ACPI mode:**
1. Enter BIOS/UEFI setup (usually by pressing F2, DEL, or ESC during boot).
2. Navigate to **Power Management** settings.
3. Set ACPI mode to **Enabled**.
4. Save and exit.

**BIOS power settings also control:**
- System power states (sleep/wake behavior)
- Battery vs. AC performance profiles
- Thermal management (fan and temperature control)
- CPU and PCI bus power management
- **Wake on LAN (WOL)** — allows the computer to be powered on remotely via a network signal *(may require a physical cable between the NIC and motherboard)*

---

### 1.4 Windows Power Options

Access via: **Battery icon (right-click) → Power Options** or **Control Panel → Hardware and Sound → Power Options**

#### Power & Sleep Button Configuration
You can define what happens when you press the power button, sleep button, or close the lid — separately for **battery** and **plugged-in** modes.

| Option | Behavior |
|--------|----------|
| **Sleep** | Maintains session in RAM; low power usage |
| **Hibernate** | Saves session to disk; minimal power usage |
| **Fast Startup** | Hybrid of shutdown + hibernate; faster boot, slightly more power than full hibernate |
| **Shut Down** | Full power off; does not save session |

#### Power Plans
- **Balanced** (default): auto-adjusts performance based on activity
- Adjustable settings: screen brightness, display timeout, sleep timeout

#### Advanced Power Settings (`Change advanced power settings`)
Fine-tune power behavior per component:

- **Hard Disk:** Set idle timeout before the disk powers down
- **Wireless Adapter:** Balance between performance and power saving depending on power source
- **Battery Alerts:**
  - Set percentage thresholds for **Low** and **Critical** battery warnings
  - Configure automatic actions at critical level (e.g., auto-shutdown) to prevent data loss from sudden power failure

---

## 2. Bluetooth

### 2.1 Overview

- Standard: **IEEE 802.15.1**
- Supports: voice, music, video, and data transmission
- Uses **128-bit encryption** and **PIN-based pairing** for security

---

### 2.2 Bluetooth Classes (Power & Range)

| Class | Max Power | Typical Range |
|-------|-----------|---------------|
| **Class 1** | 100 mW | ~100 meters |
| **Class 2** | 2.5 mW | ~10 meters *(most common)* |
| **Class 3** | 1 mW | ~1 meter |

---

### 2.3 Bluetooth Security — Pairing

- First-time connection requires **pairing** using a PIN
- Subsequent connections happen automatically when devices are nearby and Bluetooth is on

---

### 2.4 Enabling Bluetooth on a Laptop

If Bluetooth isn't working, check:
1. **Physical switch** on the laptop's side or front panel
2. **Keyboard function key** (e.g., Fn + F5)
3. **BIOS/UEFI** — ensure Bluetooth is enabled
4. If no built-in Bluetooth: use a **USB Bluetooth adapter**

---

### 2.5 Connecting a Bluetooth Device (Windows 10)

**Access Bluetooth Settings via:**
- Action Center (bottom-right) → Bluetooth toggle / right-click → Settings
- Control Panel → Hardware and Sound → Add a device
- Settings → Devices → Bluetooth

**Steps to pair a device:**
1. Put the device into **pairing mode** (consult its manual — often hold power button until indicator light flashes)
2. In Windows: click **"Add Bluetooth or other device" → Bluetooth**
3. Select your device from the discovered list
4. Click **Done** once connected

Once paired, devices **reconnect automatically** when Bluetooth is on and they're in range. Disable Bluetooth via the Action Center to disconnect.

---

## 3. Wireless Networking

### 3.1 Wireless Adapter Types (Internal)

Laptops use one of three internal wireless adapter form factors:

| Type | Pins | Supported Standards | Notes |
|------|------|---------------------|-------|
| **Mini-PCI** | 124 | 802.11a/b/g | Older generation |
| **Mini-PCIe** | 54 | 802.11a/b/g/n/ac | Most common modern standard |
| **PCI Express Micro** | 54 | 802.11a/b/g/n/ac | Half the size of Mini-PCIe; used in Ultrabooks |

---

### 3.2 Cellular WAN & Tethering

- Some laptops have **built-in cellular WAN** (no extra hardware needed)
- Can upgrade via **Mini-PCIe** or **M.2** slots — requires a **SIM card** and possibly internal antennas

**Tethering vs. Hotspot:**

| Term | Meaning |
|------|---------|
| **Tethering** | Sharing a phone's mobile data with another device via USB, Bluetooth, or Wi-Fi |
| **Mobile Hotspot** | Phone acts as a Wi-Fi router, broadcasting a signal for multiple devices |

---

### 3.3 Connecting to a Wi-Fi Network (Windows)

**Access Network Settings via:**
- Taskbar → Network icon (bottom-right)
- Control Panel → Network and Internet → Connect to a network
- Right-click Start → Network Connections

**Steps to connect:**
1. Click the desired network from the available list
2. Decide whether to **connect automatically** (saves for future) or manually each time
3. Enter the **security key (password)**
4. When prompted about discoverability: select **No** on public/guest networks (security best practice)
5. Connection confirmed → ready to browse

---

## 4. ExpressCard (Laptop Expansion)

ExpressCard slots allow laptops to expand their hardware capabilities without opening the chassis.

**Common uses:** memory card readers, external storage, TV tuners, extra USB/FireWire ports, wireless NICs

### Types

| Type | Width | Common Uses |
|------|-------|-------------|
| **ExpressCard/54** | 54 mm | Smart card readers, compact flash readers, 1.8" disk drives |
| **ExpressCard/34** | 34 mm | FireWire, TV tuners, wireless NICs |

Both use a 75mm length, 5mm thickness, and support **PCI Express**, **USB 2.0**, or **USB 3.0** interfaces.

### Installation & Safe Removal

- **Install:** Push card into slot until fully seated
- **Remove (hot-swappable devices):** Click **"Safely Remove Hardware"** in the Windows system tray before ejecting to avoid data corruption
- **Non-hot-swappable devices:** Power off the computer before removal

---

## Quick Review — True / False

| Statement | Answer |
|-----------|--------|
| Bluetooth handles voice, music, video, and data | ✅ True |
| Class 1 Bluetooth range ≈ 100 meters | ✅ True |
| Tethering allows other devices to use a phone's internet | ✅ True |
| Wireless network settings are found under "System and Security" in Control Panel | ❌ False — they're under **Network and Internet** |
| Class 2 Bluetooth range ≈ 66 feet | ❌ False — it's ≈ **33 feet (10 meters)** |

---

*Topics: CompTIA A+ 220-1101 | Domain 1: Mobile Devices*
