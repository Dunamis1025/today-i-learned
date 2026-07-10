# Computer Assembly Study Notes

## 1. RAM Installation

### What is RAM?
RAM (Random Access Memory) is a temporary memory module that plugs directly into the motherboard. It stores data that the CPU is actively using, so more/faster RAM = better performance.

### Step-by-Step Installation Order
| Step | Label | Action |
|------|-------|--------|
| 1 | C | **Open the RAM slot levers** — Push the plastic clips at both ends of the slot outward to open the slot |
| 2 | B | **Orient the RAM stick** — Align the notch on the RAM with the key in the slot (it only fits one way) |
| 3 | D | **Lower the RAM into the slot** — Gently place it in; it is not locked yet |
| 4 | A | **Press down firmly** — Push both ends down until you hear a click and the levers snap back up |

> **Key point:** The notch alignment (Step 2) is critical — RAM is keyed so it cannot be inserted backwards.

---

## 2. Motherboard Installation

### What are Standoffs?
Standoffs are small **metal pillars** screwed into the computer case **before** the motherboard is placed. They:
- Elevate the motherboard off the metal case floor
- Prevent **short circuits** (direct metal-to-metal contact = electrical damage)
- Provide threaded holes for the motherboard screws

> Some cases have **built-in standoffs**; others require manual installation.

### Step-by-Step Installation Order
| Step | Label | Action |
|------|-------|--------|
| 1 | B | **Align the motherboard direction** — I/O ports must face the rear of the case |
| 2 | E | **Locate the standoff positions** — Temporarily place the board to identify which screw holes to use |
| 3 | F | **Install standoffs** — Screw them into the confirmed locations |
| 4 | D | **Install the I/O plate** — Snap the metal shield into the rear opening of the case |
| 5 | A | **Lower the motherboard into place** — Align I/O ports with the I/O plate cutouts |
| 6 | C | **Screw in the motherboard** — Tighten screws into the standoffs one by one |

### Critical Tips
- ⚠️ **Do not overtighten screws** — Excessive force can crack the motherboard PCB
- ⚠️ **Check the I/O plate orientation** — Installing it upside down means the board won't fit
- The I/O plate snaps in; press each corner and edge until you hear it click

---

## 3. Motherboard Selection Criteria

### 1. Compatibility (Most Important)
Before buying a motherboard, verify:
- **CPU socket type** — Must physically match your CPU (e.g., AM5, LGA1700). Wrong socket = cannot install.
- **RAM type & speed** — DDR4 vs DDR5, and supported frequencies
- **GPU / expansion cards** — PCIe slot version and quantity
- **Power supply connectors** — PSU must have the right 24-pin ATX and CPU power connectors

### 2. Form Factor (Physical Size)
The motherboard must physically fit inside your case:

| Form Factor | Size | Common Use |
|-------------|------|------------|
| ATX | Full size | Desktop builds, most features |
| Micro-ATX | Smaller | Budget/compact builds |
| Mini-ITX | Very small | Small form factor (SFF) builds |

> Screw hole positions also vary by form factor — mismatched standoffs won't align.

### 3. Expansion Slots
| Slot Type | Description |
|-----------|-------------|
| **PCIe (modern)** | High-speed serial connection; used for GPUs, NVMe cards, etc. |
| **PCI (legacy)** | Older parallel bus; mostly obsolete |

Check the number of PCIe slots if you plan to add a GPU, capture card, or NVMe expansion later.

### 4. The Bus System
The **bus** is the internal data highway connecting all components.

| Bus Type | Function |
|----------|----------|
| **Data Bus** | Carries actual data between components |
| **Address Bus** | Carries the memory address (tells data *where* to go) |

- **Bus width:** 64-bit buses transfer more data per cycle than 32-bit buses → faster performance
- **Clock speed:** Measured in **MHz** or **GHz** — higher = faster data transfer rate

### 5. Clock Speed
- Determines how many data transfer cycles occur per second
- Higher MHz/GHz = more operations per second = better throughput
- Applies to both the CPU-to-RAM path and internal chip communication

---

## Key Vocabulary

| Term | Meaning |
|------|---------|
| **Standoff** | Metal spacer pillar between motherboard and case; prevents short circuits |
| **I/O Plate** | Metal shield covering the rear port area; filters dust and aligns ports |
| **PCIe** | High-speed expansion slot for GPUs and other add-in cards |
| **Bus** | Internal data pathway connecting CPU, RAM, and other components |
| **Form Factor** | Physical size standard for motherboards (ATX, Micro-ATX, Mini-ITX) |
| **Socket** | CPU mounting interface; must match between CPU and motherboard |
| **Call it a day** | Expression meaning "to stop work for now" (used in the video transcript) |
| **Snug** | Tight/secure fit — e.g., screws should be snug but not overtightened |
