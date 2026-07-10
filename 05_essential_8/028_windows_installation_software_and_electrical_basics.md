# IT Fundamentals Study Notes

## 1. Windows 10 Installation

### Overview
A clean installation of Windows 10 involves wiping the target drive and setting up the OS from scratch using bootable installation media (USB or DVD).

### Step-by-Step Process

#### Phase 1 — Preparation & Boot
- Insert the bootable USB/DVD and power on the computer
- Press any key when prompted to boot from the installation media
- Click **"Install Now"** to begin setup

#### Phase 2 — Configuration
- Enter the **product key** and accept the license agreement
- Select **"Custom: Install Windows only"** to perform a clean install
- Choose the target drive/partition for installation

> ⚠️ **Warning:** This process **erases all data** on the selected drive. Back up important files before proceeding.

#### Phase 3 — Automated Installation
- Windows copies files and **reboots automatically several times**
- Do **not** press any key during restarts — let it boot from the hard drive

#### Phase 4 — Personalization
- Select region and keyboard layout
- Create a **local (offline) account** (skip Microsoft account sign-in)
- Set a username and password
- Configure privacy settings (Cortana, diagnostics, etc.)
- Installation complete — Windows desktop appears

---

## 2. Installing & Uninstalling Software (Windows)

### Installing Software
1. Log in with an **administrator account**
2. Locate and run the installer file (`.exe`)
3. Accept the license agreement
4. Keep **default settings** for installation path and Start Menu folder
5. Click **"Install"**, then **"Finish"**
6. Provide credentials if prompted on first launch

### Uninstalling Software
1. Open **Control Panel → Programs and Features**
2. Right-click the target program → select **"Uninstall"**
3. Confirm with **"Yes"** when prompted
4. Click **"OK"** once removal is confirmed
5. Verify the program no longer appears in the list

---

## 3. Electrical Fundamentals for IT Technicians

### The Four Basic Electrical Units

| Unit | Variable | Measured In | Description |
|------|----------|-------------|-------------|
| Voltage | V | Volts (V) | The "pressure" that pushes electrical charge through a circuit |
| Current | I | Amperes (A) | The rate of flow of electrical charge |
| Resistance | R | Ohms (Ω) | Opposition to the flow of current |
| Power | P | Watts (W) | Total energy consumed or produced |

> 💡 **Why is Current `I` and not `C`?**  
> The symbol `I` comes from the French term **"Intensité de courant"** (intensity of current), used by French scientists like Ampère in the 18th–19th century. The letter `C` was already taken by **Capacitance**.

### Key Formulas

#### Ohm's Law
```
V = I × R
I = V / R
R = V / I
```

#### Power Formulas
```
P = V × I
P = V² / R
P = I² × R
```

### Analogy: Water in a Pipe
| Electricity | Water |
|-------------|-------|
| Voltage | Water pressure |
| Current | Flow rate |
| Resistance | Pipe size |
| Power | Total work the water can do |

---

## 4. Power Supply Unit (PSU) — Voltage Settings

### Voltage Selector Switch
- Older PSUs have a **manual red switch** on the back
- Must be set to match the country's electrical standard:
  - 🇰🇷 Korea / 🇪🇺 Europe → **220V**
  - 🇺🇸 USA / 🇯🇵 Japan → **110V / 115V**
- Modern PSUs **auto-detect** voltage — no manual switch needed
- Setting the wrong voltage can **damage the PSU and components**

> 🚨 **NEVER open a PSU.**  
> Internal **capacitors** retain dangerous electrical charges long after the power is off. Risk of severe electric shock.

---

## 5. Ohm's Law Practice Problems

### Given Formulas
- `V = I × R`
- `P = V × I`
- `P = V² / R`
- `I = P / V`
- `V = P / I`

### Worked Examples

#### Problem E — Find Current (I)
- **Given:** V = 12V, P = 60W
- **Formula:** `I = P / V`
- **Calculation:** `I = 60 / 12 = 5A`
- **Answer: 5A** ✅

#### Problem F — Find Power (P)
- **Given:** V = 3.3V, R = 0.25Ω
- **Formula:** `P = V² / R`
- **Calculation:** `P = 3.3² / 0.25 = 10.89 / 0.25 = 43.56W`
- **Answer: 43.56W** ✅

#### Problem G — Find Voltage (V)
- **Given:** P = 120W, I = 24A
- **Formula:** `V = P / I`
- **Calculation:** `V = 120 / 24 = 5V`
- **Answer: 5V** ✅
