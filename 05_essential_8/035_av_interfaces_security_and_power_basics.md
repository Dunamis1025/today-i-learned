# IT Essentials Study Notes — Hardware & Power Concepts (Q6–Q10)

A summary of key concepts covering interfaces, security features, display hardware safety, BIOS, and AC power conditions.

## 1. HDMI (High-Definition Multimedia Interface)

**Definition:** A digital interface originally designed for HDTVs, now the standard connector for audio/video on computers and consumer electronics.

**Key points:**
- Combines video and audio transmission into a **single cable**, unlike older standards.
- Originally developed for HDTVs; now widely used to connect PCs, laptops, monitors, projectors, and gaming consoles.
- Supports high-definition video and high-quality digital audio simultaneously.

**Comparison with other interfaces:**
- **VGA / DVI** — primarily video-only, generally no audio support.
- **USB** — designed for general data transfer, not primarily A/V.
- **FireWire** — historically used for connecting video capture/camcorder equipment.

---

## 2. LoJack (Anti-Theft Technology)

**Definition:** A security and tracking service embedded in computer hardware to protect devices in case of theft.

**Core functions (remote, via internet connection):**
- **Locate** — find the geographic location of a stolen device.
- **Lock** — prevent unauthorized use of the system.
- **Delete/Wipe** — remotely erase sensitive personal data.

**Why it's notable:**
- Embedded at the **firmware level (BIOS/UEFI)**, meaning it can persist even if the thief:
  - Replaces the hard drive
  - Reinstalls the operating system
- This makes it extremely resilient compared to software-only tracking solutions.

---

## 3. CRT Monitor Disposal Hazards

**Definition:** CRT (Cathode Ray Tube) monitors pose serious safety risks during disposal/repair due to stored electrical energy.

**Main hazard: Potential residual high voltage**
- Even after a CRT monitor is powered off and unplugged, internal **capacitors** can retain extremely high voltage (potentially tens of thousands of volts) for an extended period.
- Technicians who open or disassemble the unit without proper discharge procedures risk **severe or fatal electric shock**.

**Additional note:**
- CRT monitors also contain hazardous materials (e.g., lead), but the most immediate physical danger during handling/disposal is the **residual high-voltage charge**, not the toxic materials.

---

## 4. BIOS (Basic Input/Output System)

**Definition:** Low-level firmware that initializes and tests hardware before the operating system loads.

**Key function: Performs a check on all internal components (POST – Power-On Self-Test)**
- Activates the moment the power button is pressed, **before the OS starts**.
- Verifies that critical hardware is present and functioning correctly:
  - RAM
  - Keyboard
  - Storage devices (HDD/SSD)
  - Other internal components
- If a problem is detected, the system emits **beep codes** to signal specific hardware errors.

**Summary:** BIOS ensures the hardware is in a working state and ready for the operating system to boot.

---

## 5. AC Power Fluctuations — Brownout vs. Sag vs. Surge/Spike

**Definition:** Different terms describe abnormal AC voltage conditions, classified by direction (high/low) and duration (short/prolonged).

| Condition | Voltage Direction | Duration | Description |
|---|---|---|---|
| **Brownout** | Decrease | Prolonged | A sustained drop in voltage; power isn't cut, but equipment may run weakly, flicker, or behave erratically. |
| **Sag** | Decrease | Momentary/short | A brief, short-term dip in voltage. |
| **Surge / Spike** | Increase | Momentary/short | A sudden, brief increase in voltage; can damage sensitive electronic components. |

**Key answer for Q10:** A **prolonged reduction in AC voltage level** = **Brownout**.

**Related context:**
- AC power feeds devices, but internal computer components run on **DC power**, requiring conversion via a power supply.
- **Capacitors** within power supplies and devices are **notoriously prone to failure** when subjected to repeated voltage fluctuations or prolonged exposure to heat.
- A **UPS (Uninterruptible Power Supply)** can help mitigate brownouts, sags, and surges by providing stable backup power and voltage regulation.

---

## Vocabulary Reference

| Term | Meaning |
|---|---|
| **Checksum** | A value used to verify data integrity (detects corruption/tampering). |
| **UPS** | Uninterruptible Power Supply — provides backup power during outages/fluctuations. |
| **Fluctuation** | An irregular rise and fall in a value (e.g., voltage, price). |
| **Notoriously** | Known widely for a negative trait (e.g., "notoriously prone to failure"). |
| **Capacitor** | An electronic component that stores and releases electrical energy. |
| **Prone to** | Having a tendency toward (usually something negative). |
| **AC Power** | Alternating Current — the type of electricity supplied to outlets. |
| **Prolonged** | Lasting for an extended/longer-than-expected period. |
