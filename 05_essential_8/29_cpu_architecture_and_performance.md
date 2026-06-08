# CPU Architecture & Performance — Study Notes

## 1. Instruction Set Architectures: RISC vs CISC

| Feature | RISC | CISC |
|---|---|---|
| Full Name | Reduced Instruction Set Computer | Complex Instruction Set Computer |
| Philosophy | Small, simple instructions executed very fast | Complex instructions that do more per command |
| Steps per task | More steps, but each is lightning fast | Fewer steps overall |
| Examples | ARM (smartphones, tablets) | Intel x86 (desktops, laptops) |
| Best for | Power-efficient, mobile devices | General-purpose computing |

**Key takeaway:** RISC breaks tasks into many tiny, fast steps. CISC handles complex operations in fewer, heavier steps.

---

## 2. CPU Performance Features

### Hyper-Threading *(Intel)*
- Allows a **single physical core** to handle **two threads simultaneously**
- The OS sees it as two logical processors
- Improves multitasking performance without adding physical cores

### HyperTransport *(AMD)*
- A **high-speed bus** connecting the CPU to the Northbridge chip
- Widens the data pathway, reducing bottlenecks between components

### Front Side Bus (FSB)
- The **data highway** between the CPU and the rest of the system
- Measured in **bits**; wider = more data transferred per cycle

### Clock Speed (MHz / GHz)
- Measures how many processing cycles occur **per second**
- MHz = millions of cycles/sec; GHz = billions of cycles/sec
- Higher clock speed generally means faster performance

---

## 3. Speed Control Techniques

### Overclocking
- Forces the CPU to run **faster than its rated specification**
- ⚠️ Risks: overheating, hardware damage, instability
- Not recommended without proper cooling

### CPU Throttling
- **Intentionally slows down** the CPU to conserve power or reduce heat
- Commonly triggered in laptops during battery-saving mode or thermal protection

---

## 4. Multicore Processors

A **multicore processor** places multiple processing cores on a single chip, enabling true parallel processing.

| Name | Cores |
|---|---|
| Single Core | 1 |
| Dual Core | 2 |
| Triple Core | 3 |
| Quad Core | 4 |
| Hexa-Core | 6 |
| Octa-Core | 8 |

**Benefits:**
- Handles multiple tasks simultaneously without slowdown
- More energy-efficient than using separate single-core CPUs
- Essential for video editing, gaming, and heavy multitasking

---

## 5. CPU Virtualization

- A hardware feature supported by both **Intel and AMD**
- Allows **one physical CPU** to act as **multiple independent virtual processors**
- Enables running multiple operating systems (e.g., Windows + Linux) side by side on **virtual machines (VMs)**
- Often requires manual activation in **BIOS settings**

---

## 6. GPU (Graphics Processing Unit)

| Type | Description |
|---|---|
| **Integrated GPU** | Built into the CPU chip; power-efficient, suitable for everyday tasks |
| **Dedicated GPU** | A separate card; high performance for gaming, 3D rendering, ML workloads |

---

## 7. Security: NX Bit (Execute Disable Bit)

- A CPU-level **security feature**
- Marks certain memory regions as **non-executable**
- Prevents malicious code (malware) from running in protected memory areas

---

## 8. Cooling Systems

Keeping CPU/GPU temperatures stable is critical for performance and longevity.

### Passive Cooling
| Component | Function |
|---|---|
| **Heat Sink** | Metal fins attached to CPU; spreads heat over a large surface area |
| **Thermal Compound** | Paste applied between CPU and heat sink to fill micro-gaps and improve heat transfer |

### Active Cooling
| Component | Function |
|---|---|
| **CPU Fan** | Mounted on top of heat sink; forces airflow to accelerate heat dissipation |
| **Case Fan** | Circulates air throughout the entire chassis |
| **GPU Fan** | Dedicated fan(s) on the graphics card for high-load cooling |

### Advanced Cooling
| Component | Function |
|---|---|
| **Water Cooling System** | Liquid circulates over a metal plate on the CPU/GPU, carries heat to a radiator; quieter and more efficient than air cooling |

---

## 9. Quick Reference: Term Matching

| Term | Definition |
|---|---|
| **CPU Virtualization** | One processor acts as multiple independent processors |
| **Throttling** | Runs below rated speed to save power or reduce heat |
| **Water Cooling** | Liquid-based cooling for high-heat CPUs/GPUs |
| **Overclocking** | Forces CPU beyond its rated speed specification |
| **Hyper-Threading** | Executes multiple code threads simultaneously on one core |
| **HyperTransport** | High-speed connection between CPU and Northbridge chip |

---

## 10. Cache Memory (Bonus)

- A **small, ultra-fast memory** built into or near the CPU
- Stores frequently used instructions and data for instant access
- Dramatically reduces the time the CPU spends waiting for data from RAM
- Organized in levels: **L1** (fastest, smallest) → **L2** → **L3** (slowest, largest)
