# CompTIA A+ Study Notes — Hardware & Security Fundamentals

## 1. ESD Protection

**ESD (Electrostatic Discharge)** is the sudden flow of static electricity between objects — the same "zap" you feel touching a doorknob in dry weather. Even a tiny discharge can permanently destroy sensitive computer components.

### Tool: Antistatic Wrist Strap
- Worn around the wrist and clipped to a metal part of the PC case
- Safely drains static from your body to ground **before** it reaches components
- Eliminates the voltage difference between you and the hardware

### Why the Others Are Wrong

| Option | Why It's Wrong |
|---|---|
| UPS (Uninterruptible Power Supply) | Provides backup power during outages — unrelated to static |
| SPS (Standby Power System) | Similar to UPS; handles power loss, not ESD |
| Surge Suppressor | Protects against sudden voltage spikes (e.g., lightning) — not static discharge |

---

## 2. Fastest Memory Technology

### Answer: SRAM (Static RAM)

| Type | Speed | Cost | Use Case |
|---|---|---|---|
| **SRAM** | ⚡ Fastest | 💰 Very expensive | CPU Cache (L1/L2/L3) |
| DRAM | Slower | Cheap | Main system RAM |

- SRAM does **not** need to be constantly refreshed → much faster
- Too expensive to use as main memory → used only in small amounts inside the CPU as **cache memory**

### Why the Others Are Wrong

- **SODIMM** — A physical *form factor* (shape/size) of RAM used in laptops, not a speed classification
- **Dual / Quad Channel** — Widens the data highway between CPU and RAM (more bandwidth), but doesn't change the speed of the memory chips themselves

---

## 3. User Identity Verification on Laptops

### Answer: Biometric Identification Device

Verifies a user's identity using **unique physical characteristics**:
- Fingerprint scanner
- Facial recognition camera (e.g., Windows Hello)

Highly secure because biometric traits cannot be guessed or stolen like passwords.

### Why the Others Are Wrong

| Option | What It Actually Does |
|---|---|
| MIDI Device | Connects musical instruments to a computer |
| Digitizer | Converts pen/stylus strokes into digital input (for drawing) |
| Touch Screen | An input display you interact with by touch — not for authentication |

---

## 4. Active vs. Passive Cooling

### Active Cooling
Uses **electrical energy** to actively move heat away from components.

- ✅ **Example: Adding a case fan** — powered, moves air, forces heat out

### Passive Cooling
Absorbs and dissipates heat **without moving parts or electricity**.

- ✅ **Example: Heatsink alone** — metal fins absorb heat and release it into the air

### Why the Others Are Wrong

| Option | Why It's Wrong |
|---|---|
| Reduce CPU speed (Throttling / Underclocking) | Limits heat *generation*, but is not a cooling solution |
| Add a heatsink (alone) | Passive cooling — no power, no moving parts |
| Paint the computer case | Has no measurable effect on thermal performance |

---

## 5. Throttling vs. Underclocking

Both reduce CPU/GPU speed, but for different reasons and by different means.

| | Throttling | Underclocking |
|---|---|---|
| **Who decides** | System / OS (automatic) | User or manufacturer (manual) |
| **When** | Triggered by overheating or power limits | Set in advance |
| **Feel** | Sudden, unpredictable | Stable, intentional |
| **Goal** | Prevent damage | Save power / reduce heat / silence |
| **Analogy** | Emergency brake | Deciding to drive slowly from the start |

> **Key distinction:** Throttling is a *reactive* safety measure. Underclocking is a *proactive* design choice.

---

*Sources: CompTIA A+ exam prep materials, reviewed May 2026*
