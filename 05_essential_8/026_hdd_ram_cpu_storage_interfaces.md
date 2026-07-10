# IT Hardware Study Notes
> CompTIA A+ / IT Fundamentals — Key Hardware Concepts

---

## 1. HDD Form Factors (Physical Size Standards)

**Question type:** *A technician needs to order a replacement internal SATA HDD — which form factors should they choose from?*

| Form Factor | Size | Primary Use |
|---|---|---|
| **2.5 inch** (6.35 cm) | Small | Laptops, compact desktops |
| **3.5 inch** (8.89 cm) | Standard | Full-size desktop PCs |

**Key concept:** A *form factor* refers to the physical size and shape of a hardware component. Internal drives must physically fit into the drive bay of the computer case, so choosing the correct size is essential.

> ✅ For desktop replacement: **2.5" or 3.5"** are the two valid SATA HDD form factors.

---

## 2. CPU Package Types (How the CPU Connects to the Motherboard)

**Question type:** *A technician is upgrading a processor in a computer that is a couple of years old — which two package types could be used?*

| Package | Full Name | How it Works |
|---|---|---|
| **PGA** | Pin Grid Array | Pins are on the **CPU**; they insert into holes in the motherboard socket |
| **LGA** | Land Grid Array | Pins are on the **motherboard socket**; CPU has flat contact pads ("lands") |

> ✅ Modern CPUs use **PGA** or **LGA**.

**Why other options are wrong:**
- **PCIe** — An expansion slot standard for GPUs and add-in cards, not a CPU package
- **GDDR** — Graphics card memory (VRAM), not a CPU type
- **ISA** — An obsolete bus architecture from early PCs; no longer used

---

## 3. RAM Module Types (Memory Form Factors)

**Question type:** *A student wants to add memory to a tower computer to speed it up — which module type should they look for?*

| Module | Full Name | Used In |
|---|---|---|
| **DIMM** | Dual In-line Memory Module | Desktop / tower PCs ✅ |
| **SODIMM** | Small Outline DIMM | Laptops, mini PCs |
| **SIMM** | Single In-line Memory Module | Obsolete (pre-DIMM era) |
| **DIP** | Dual In-line Package | Very early computers; obsolete |

> ✅ Upgrading a **desktop tower** → choose **DIMM**  
> ✅ Upgrading a **laptop** → choose **SODIMM**

---

## 4. Storage Interfaces (How Drives Connect to the Motherboard)

**Question type:** *A customer is replacing a motherboard and buying a new mechanical HDD — which storage interface should the salesperson recommend?*

| Interface | Status | Notes |
|---|---|---|
| **SATA** | ✅ Current standard | Fast, simple cable, used in all modern PCs |
| **EIDE / IDE** | ❌ Legacy | Wide ribbon cable; obsolete |
| **RAID 5** | ❌ Not an interface | A *data redundancy technique*, not a physical connector |

> ✅ For any modern mechanical hard drive: recommend **SATA**.

**Key distinction:** RAID is a *storage configuration method* (combining multiple drives for speed/redundancy), not a physical interface standard.

---

## 5. Bonus Concept: Why is it Called a "Bus"?

The word **bus** in computing shares the same origin as the public transport vehicle.

- **Etymology:** Both derive from Latin *omnibus* — meaning **"for all"**
- In 19th-century France, public horse-drawn carriages were called *omnibuses* ("for all people"), later shortened to *bus*

**Analogy:**

| Public Bus | Computer Bus |
|---|---|
| Shared transport for all passengers | Shared communication channel for all components |
| Stops at multiple destinations | Connects CPU, RAM, I/O devices via a common path |
| Carries passengers to their stop | Carries data signals to their target component |

> Think of a computer bus as the **data highway** inside your machine — all components share the road.

---

## Quick Reference Summary

| Topic | Key Answer |
|---|---|
| HDD form factors (SATA) | **2.5"** (laptop) and **3.5"** (desktop) |
| CPU packages (modern) | **PGA** (pins on CPU) and **LGA** (pins on motherboard) |
| RAM for desktop tower | **DIMM** |
| RAM for laptop | **SODIMM** |
| Storage interface (modern HDD) | **SATA** |
| RAID 5 | A data redundancy *technique*, not an interface |
