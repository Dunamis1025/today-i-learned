# Memory Types and Modules

## 1. ROM (Read-Only Memory)

- Read-only memory chip; data is written at the time of manufacture
- A ROM chip that cannot be erased or rewritten is now obsolete
- The term "ROM" is still used generically for any read-only memory chip type

---

## 2. PROM (Programmable Read-Only Memory)

- Information is written **after** manufacture (not at the factory)
- Manufactured **blank**, then programmed using a PROM programmer when needed
- Can only be programmed **once** — cannot be erased

| | ROM | PROM |
|---|---|---|
| Initial state | Pre-written | Blank |
| Written when | At manufacture | After manufacture |
| Erasable | ❌ | ❌ |

---

## 3. EPROM (Erasable Programmable Read-Only Memory)

- **Non-volatile** but can be erased by exposing it to strong **ultraviolet (UV) light**
- EPROMs have a **transparent quartz window** on top of the chip to allow UV exposure
- Constant erasing and reprogramming can eventually render the chip useless

| | ROM | PROM | EPROM |
|---|---|---|---|
| Initial state | Pre-written | Blank | Blank |
| Writable | Once (at manufacture) | Once | Multiple times ✅ |
| Erasable | ❌ | ❌ | ✅ (via UV light) |
| Non-volatile | ✅ | ✅ | ✅ |

---

## 4. RAM (Random Access Memory)

RAM is **volatile** — data is lost when power is off. It is used as main memory for active processes.

### 4.1 DRAM (Dynamic RAM)

- Older technology, popular until the mid-1990s
- Used for **main memory**
- Gradually discharges energy → must be **constantly refreshed** with pulses of electricity to maintain stored data

### 4.2 SRAM (Static RAM)

- Requires constant power to function, but does **not** need refreshing
- Often used for **cache memory**
- Uses **lower power** than DRAM
- **Much faster** than DRAM
- **More expensive** than DRAM

---

## 5. DRAM Generations

### 5.1 SDRAM (Synchronous Dynamic RAM)

- DRAM that operates **in synchronization** with the memory bus
- Can process **overlapping instructions in parallel** (e.g., read before a write completes)
- Higher transfer rates than standard DRAM

### 5.2 DDR SDRAM (Double Data Rate Synchronous Dynamic RAM)

- Transfers data **twice as fast** as SDRAM
- Supports **two writes and two reads** per CPU clock cycle
- Connector: **184 pins**, single notch
- Voltage: **2.5 V**
- Family: DDR2, DDR3, DDR4

### 5.3 DDR2 SDRAM

- Also transfers data twice as fast as SDRAM
- Runs at **higher clock speeds** than DDR (553 MHz vs. DDR at 200 MHz)
- Reduces noise and crosstalk between signal wires
- Connector: **240 pins**
- Voltage: **1.8 V**

### 5.4 DDR3 SDRAM

- Expands memory bandwidth by **doubling the clock rate** of DDR2
- Runs at up to **800 MHz**
- Consumes **less power** than DDR2
- Generates **less heat**
- Connector: **240 pins**
- Voltage: **1.5 V**

### 5.5 DDR4 SDRAM

- **Quadruples** DDR3 maximum storage capacity
- Runs at up to **1600 MHz**
- Connector: **288 pins**
- Voltage: **1.2 V**
- Supports advanced error correction: **ECC (Error-Correcting Code) memory**

### 5.6 DDR5

- More than **double the speed** of the fastest DDR4 modules
- **Quadruples** DDR4 maximum storage capacity
- Maximum module size: **128 GB**
- Connector: **288 pins** (different pattern from DDR4 — **not compatible**)
- Voltage: **1.1 V**

### 5.7 GDDR SDRAM (Graphics Double Data Rate SDRAM)

- "G" stands for **Graphics**
- RAM specifically designed for **video graphics**
- Used in conjunction with a dedicated **GPU**
- Family: GDDR, GDDR2, GDDR3, GDDR4, GDDR5
- Each generation improves performance and lowers power consumption
- Processes **massive amounts of data** but not necessarily at the fastest speeds

### DDR Generation Comparison

| Generation | Clock Speed | Voltage | Pins |
|---|---|---|---|
| SDRAM | — | — | 168 |
| DDR | 200 MHz | 2.5 V | 184 |
| DDR2 | 553 MHz | 1.8 V | 240 |
| DDR3 | up to 800 MHz | 1.5 V | 240 |
| DDR4 | up to 1600 MHz | 1.2 V | 288 |
| DDR5 | 2× DDR4 | 1.1 V | 288* |

> *DDR5 uses 288 pins but has a **different notch pattern** — incompatible with DDR4 slots.

---

## 6. Memory Modules

Early computers had RAM installed as individual chips (DIP chips) directly on the motherboard. These were hard to install and often came loose. Designers solved this by soldering chips onto a circuit board — creating a **memory module** — which plugs into a memory slot on the motherboard.

### 6.1 DIP (Dual Inline Package)

- An individual memory chip
- Has **dual rows of pins** on both sides used to attach directly to the motherboard
- Difficult to install; prone to becoming loose over time

### 6.2 SIMM (Single Inline Memory Module)

- A small circuit board that holds **several memory chips**
- **30-pin** or **72-pin** configurations
- Easier to install than individual DIP chips

### 6.3 DIMM (Dual Inline Memory Module)

- A circuit board that holds SDRAM, DDR, DDR2, DDR3, and DDR4 chips
- **Dual** rows of pins (one on each side) → more data per transfer than SIMM
- Different pin counts per generation:

| RAM Type | Pins |
|---|---|
| SDRAM DIMM | 168 |
| DDR DIMM | 184 |
| DDR2 / DDR3 DIMM | 240 |
| DDR4 DIMM | 288 |

> Different generations are **physically incompatible** — pin counts and notch positions differ.

### 6.4 SODIMM (Small Outline DIMM)

- A **smaller, more compact** version of DIMM
- Ideal for devices where space is limited: **laptops, printers**, etc.
- Pin configurations:
  - **32-bit transfers**: 72-pin, 100-pin
  - **64-bit transfers**: 144-pin, 200-pin, 204-pin, 260-pin

### Memory Module Evolution

```
DIP → SIMM → DIMM → SODIMM
(single chip) (single-sided board) (dual-sided board) (compact DIMM for laptops)
```
