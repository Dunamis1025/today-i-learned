# 06. Memory: Single/Double-Sided, Multi-channel, Cache, and Error Checking

---

## 1.2.5.5 Single-Sided, Double-Sided, and Multi-channel

### Single-Sided vs Double-Sided

- **Single-sided**: RAM chips are on **only one side** of the module
- **Double-sided**: RAM chips are on **both sides** of the module

### Multi-channel Technology

Memory throughput can be increased through **multichannel technology**. The more channels, the more data can travel simultaneously.

| Type | Channels | Description |
|------|----------|-------------|
| Single Channel | 1 | All RAM slots addressed at the same time |
| Dual Channel | 2 | Adds a second channel to access a second module simultaneously |
| Triple Channel | 3 | Three modules can be accessed at the same time |
| Quad Channel | 4 | Adds another channel for even higher bandwidth |

> **Note:** To use triple and quad channel, the chipset architecture must support it. Memory slots must also be populated in the correct order.

---

## 1.2.5.6 Cache Memory

**Cache memory** uses **SRAM (Static RAM)** — the fastest type of memory — to store the most recently used data and instructions by the CPU. It provides faster access than retrieving data from the slower DRAM (main memory).

### Cache Levels

| Level | Location | Speed | Notes |
|-------|----------|-------|-------|
| **L1** | Inside the CPU | ⚡⚡⚡ Fastest | Each CPU model may have different amounts |
| **L2** | Inside the CPU (originally on motherboard) | ⚡⚡ Fast | Larger than L1, slightly slower |
| **L3** | High-end workstations & server CPUs | ⚡ Fast | Largest, shared among CPU cores |

### Access Order

```
CPU → L1 → L2 → L3 → Main RAM (DRAM)
      fastest              slowest
```

> A **cache hit** occurs when the CPU finds the data it needs in cache — the more cache hits, the faster the system runs.

---

## 1.2.5.7 Memory Errors

Memory errors occur when data is not stored correctly in the chips. Computers use different methods to detect and correct these errors.

### Error Checking Methods

| Method | Detects Errors | Corrects Errors | Common Use |
|--------|---------------|-----------------|------------|
| **Nonparity** | ❌ | ❌ | Home and business workstations |
| **Parity** | ✅ | ❌ | Some older systems |
| **ECC** | ✅ (multiple bits) | ✅ (single bit only) | Servers, financial/data analytics systems |

### Details

- **Nonparity**: Does not check for errors at all. The most common RAM for everyday use.
- **Parity**: Contains 8 bits for data + 1 **parity bit** for error checking. Can detect errors but cannot fix them.
- **ECC (Error Correction Code)**: Can detect multiple-bit errors and **correct single-bit errors**. Required in high-reliability environments like financial or data analytics servers.

> ⚠️ ECC can **detect** multiple bit errors, but can only **correct** single bit errors.

---

## 1.2.6 Check Your Understanding: Memory (Quiz Answers)

### Q1. Which statement describes EPROM?
**✅ Answer: Data can be erased using a strong ultraviolet light**

- EPROM = **Erasable Programmable Read-Only Memory**
- A transparent window on the chip allows UV light to erase stored data, after which it can be reprogrammed
- It is **non-volatile** (data persists without power) and **not** a type of RAM
- ❌ "Can only be programmed once" → that's **PROM**
- ❌ "Data programmed at manufacture" → that's **ROM**

---

### Q2. A user complains the computer is running very slowly. What solution would help speed it up?
**✅ Answer: Add more RAM**

- Insufficient RAM causes the system to use the hard drive as virtual memory, which is much slower
- More RAM = more programs can run simultaneously without slowdown
- ❌ ROM cannot be increased to improve speed
- ❌ L1 cache is fixed inside the CPU and cannot be swapped by the user
- ❌ ECC memory is for error correction, not performance

---

### Q3. Which RAM in the group provides the fastest performance?
**✅ Answer: SRAM**

Speed order (fastest → slowest):
```
SRAM > GDDR SDRAM > DDR4 SDRAM > DDR3 SDRAM > SDRAM
```

- SRAM does not need to be refreshed, making it extremely fast
- Used as **cache memory (L1, L2, L3)**
- Expensive and small capacity — not used as main memory

---

### Q4. True or False: Error Correction Code memory can correct multiple bit errors.
**✅ Answer: False**

- ECC can **detect** multiple bit errors ✅
- ECC can only **correct single bit errors** ✅
- ECC **cannot correct** multiple bit errors ❌

---

### Q5. Which memory module can support both 32-bit and 64-bit transfers of data?
**✅ Answer: SODIMM**

| Module | Bit Transfer | Notes |
|--------|-------------|-------|
| DIP | Limited | Very old chip format |
| SIMM | 32-bit only | Older module |
| DIMM | 64-bit | Standard desktop RAM |
| **SODIMM** | **32-bit + 64-bit** ✅ | Compact form for laptops and small PCs |
