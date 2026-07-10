# Laptop Hardware Maintenance – Study Notes

> Topics: Storage Drive, Optical Drive, Wireless Card, Speakers, CPU/Fan/Heatsink, Motherboard, Plastic Frame

---

## ⚠️ Universal Safety Rules (Apply to ALL procedures)

- Always **remove the power adapter** before working on any component.
- Always **remove the battery** before working on any component.
- Use **minimal force** — never yank or force components.
- Always **consult the laptop's manual** before disassembly; steps vary by model.
- Component replacement steps are **NOT the same for all laptops**.

---

## 1. Internal Storage Drive (HDD → SSD Upgrade)

### Key Concepts
- Laptop drives use the **2.5-inch form factor**
- Interface: **SATA connector**
- Types: **HDD** (platter-based) vs **SSD** (solid state — faster, no moving parts)

### Replacement Steps
1. Locate the **access panel** on the bottom of the laptop (marked with a disc icon).
2. Remove the panel screws and lift the cover.
3. Unscrew the **drive retention screw**.
4. Pull the **tab** to lift and slide the drive out of the SATA connector.
5. Transfer the **metal shield/bracket** from the old drive to the new one.
6. Slide the new drive into the SATA connector at the correct angle until it clicks.
7. Replace the retention screw and reattach the access panel.

### Lab Exercise: Drive Comparison
When researching replacement drives, document:
| Field | Details |
|---|---|
| Form Factor | e.g., 2.5-inch |
| Type | HDD or SSD |
| Capacity | GB |
| Port Type | e.g., SATA |
| Drive Speed | RPM (HDD) or read/write MB/s (SSD) |
| Manufacturer | Brand name |
| Retail Cost | Price |

> **Compatibility check is critical** — verify physical and technical compatibility before purchasing.

---

## 2. Optical Drive (CD/DVD Drive)

### Key Concepts
- Located on the **side** of the laptop
- Secured by a single screw (marked with a disc icon)
- Removal method **varies by laptop model**

### Replacement Steps
1. Remove the **retaining screw** on the side.
2. On some models, the drive doesn't slide straight out — press the **eject button firmly** to disconnect it from the internal connector.
3. Pull the drive out.
4. Slide the **new drive** in firmly until it locks.
5. Replace the retaining screw.

### Internal vs. External Optical Drive
- Compare options based on **price** and **data transfer speed**.
- External drives are an alternative if the laptop has no internal bay.

---

## 3. Wireless Network Card (Wi-Fi Card)

### Key Concepts
- Common form factor: **Mini PCIe** (not to be confused with Micro PCIe or Mini PCI)
- Has **antenna wires** connected (Main, Aux, MIMO — multiple in, multiple out)
- Wire count and labeling vary by model — **always document wire positions before removal**

### Replacement Steps
1. Remove the **access panel** screw and open the cover.
2. **Label or photograph** which antenna wire goes to which connector.
3. Gently pop off each **antenna wire** (use fingers or safe tweezers).
4. Remove the **two retention screws** holding the card.
5. The card springs up at ~**45 degrees** — pull it out by the edges.
6. Insert the **new card** (same form factor!) at 45 degrees, then press down to seat it.
7. Replace the two screws.
8. Reconnect the **antenna wires in the correct order**.
9. Replace panel, reinstall battery and power.
10. After booting, **install the correct drivers** for the new card.

---

## 4. Laptop Speakers

### Troubleshooting Before Replacing
Always check software first:
- Is audio **muted**?
- Is the **volume level** too low?

Only replace the speaker if software checks pass and there is still no sound.

### Replacement Steps
1. Follow the **manual** to disassemble internal components (the speaker may be deeply embedded).
2. Locate the **speaker connector** going to the system board.
3. Use a **flat tool or fingers** to lift the connector **straight up** — avoid bending pins.
4. Remove the old speaker and drop the new one in place.
5. Reconnect the connector and reassemble in reverse order.

---

## 5. CPU, Heatsink & Cooling Fan

### Key Concepts
- The **heatsink** draws heat away from the CPU; the **fan** blows air over the heatsink.
- **Thermal paste** bridges the gap between CPU and heatsink for efficient heat transfer.
- Heatsink screws are **numbered** — must be installed/removed in order for even pressure.
- Use a **torque screwdriver** if required by the manual.

### Replacement / Cleaning Steps

#### Disassembly
1. Unplug the **fan power cable** from the motherboard.
2. Remove the **fan retention screw**.
3. Loosen the **6 heatsink screws in numbered order** (e.g., 1 → 6).
4. Lift out the **fan** — clean with compressed air if dusty.
5. Lift out the **heatsink** — clean with compressed air.
6. Turn the **CPU locking screw** slightly to unlock.
7. Lift the **CPU** straight out of the socket.

#### Reassembly
1. Drop the **new (or cleaned) CPU** into the socket — do NOT press.
2. Turn the **locking screw** to lock the CPU in place.
3. Apply **thermal paste** (pea-sized dot) to the **center of the CPU**.
4. Place the **heatsink** directly on top.
5. Tighten heatsink screws in **numbered order** (1 → 6).
6. Reattach the **fan**, connect the fan power cable.
7. Tighten the fan retention screw.

> **Never install the heatsink before applying thermal paste.**

---

## 6. Motherboard (System Board)

### Key Concepts
- Laptop motherboards are **proprietary** — not standardized.
- Must order the exact board for your **specific laptop model and brand**.
- Replacing the motherboard requires removing **almost every other component first**.

### Replacement Steps
1. Disconnect **all cables** (HDD, Bluetooth, microphone, modem, etc.).
2. Remove all **motherboard retaining screws** (identified via manual).
3. Gently **pull back the plastic casing** while lifting the motherboard out.
4. Be careful of **side-mounted ports** (USB, audio jacks) catching on the frame.
5. Insert the **new motherboard**, reconnect all cables in reverse order.
6. Replace all screws and reassemble the laptop.

---

## 7. Plastic Frame & Component Covers

### Key Concepts
- The laptop exterior is made of **multiple plastic parts** covering different components.
- Common covers: HDD, RAM, Wireless LAN card, Bluetooth module, PC card slot.
- Hidden screws may be located **under rubber feet** — check the manual carefully.

### Disassembly Steps
1. Remove screws from **each component cover** and lift them off.
2. Disconnect internal cables (trackpad, microphone, etc.) before pulling the frame.
3. Remove all **remaining screws** from the frame (inside and outside).
4. Pry up the plastic frame at the **angle specified in the manual** (e.g., 45 degrees).
5. Lift off the frame — the system board and touchpad wiring will be exposed.

> **Always use a tool for leverage — never yank plastic frames by force.**

---

## 8. Knowledge Check – True or False

| Statement | Answer |
|---|---|
| Thermal paste is applied **after** installing the heatsink. | ❌ False — apply **before** |
| Remove both battery and power cable before replacing components. | ✅ True |
| Always consult the manual before removing components. | ✅ True |
| Component replacement steps are the same for all laptops. | ❌ False — steps vary by model |
| Laptop motherboards have a standard form factor. | ❌ False — they are proprietary |
| Laptop batteries and RAM modules are Customer-Replaceable Units (CRUs). | ✅ True |

---

## 9. Summary: Customer-Replaceable Units (CRUs)

Components users can typically replace themselves:
- **Battery**
- **RAM (Memory Module)**
- **Storage Drive (HDD/SSD)**
- **Optical Drive** (on many models)

Components requiring more expertise / full disassembly:
- Wireless Card
- CPU / Heatsink / Fan
- Speakers
- Motherboard
- Plastic Frame
