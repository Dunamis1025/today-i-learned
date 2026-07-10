# Computer Hardware: Adapter Cards, Media Readers & Power Connectors
## Study Notes Summary

---

## 1. Adapter Card Selection (2.1.5.3)

### Pre-Purchase Checklist
- **Compatibility** — Does the motherboard have an open, matching expansion slot?
- **Purpose** — What does the user need it for (gaming, networking, video capture)?
- **Future-proofing** — Buy slightly above current needs to avoid early upgrades

### Card Types & Key Specs

| Card Type | Key Specs to Check |
|---|---|
| **Graphics Card** | Slot type, VRAM, GPU, Max Resolution |
| **Sound Card** | Slot type, DSP, Port types, Signal-to-noise ratio |
| **Storage Controller** | Slot type, Connector qty, RAID type, Card RAM/processor |
| **I/O Card** | Slot type, Port type & quantity, Power requirements |
| **NIC** | Slot type, Speed, Wired/Wireless, Standards compatibility |
| **Capture Card** | Resolution, Frame rate, I/O ports, Format standards |

---

## 2. Installing Adapter Cards (2.1.5.4)

### Installation Order
1. Find empty expansion slot → remove metal slot cover
2. Align card to the slot
3. Press down gently until fully seated
4. Secure mounting bracket with a screw

### Critical Tips
- **Power cables** — High-end GPUs require separate **6-pin or 8-pin** connectors from the PSU (some need two)
- **Card length** — Measure internal case space before purchase; long cards may obstruct other components
- **Airflow** — Leave space around GPUs; they generate significant heat
- **Bracket trick** — Slide the bottom tab of the mounting bracket into the case slot *before* pushing the card into the motherboard

### Lab: Slot Compatibility Reference
| Card | Expansion Slot |
|---|---|
| Wired NIC | PCIe x1 |
| Wireless NIC | PCIe x1 |
| Video/GPU | PCIe x16 |

> **Safety:** Always wear an antistatic wrist strap and use an antistatic mat

---

## 3. Media Readers (2.1.6.1)

### Common Media Card Formats
| Format | Key Characteristic |
|---|---|
| **SD** | Standard size; up to 2 TB; cameras & laptops |
| **MicroSD** | Smallest SD variant; smartphones & tablets |
| **MiniSD** | Mid-size SD; older mobile phones |
| **CompactFlash** | Older but fast & high-capacity (up to 128 GB); video cameras |
| **Memory Stick** | Sony proprietary format; cameras, MP3 players, handhelds |
| **xD (Picture Card)** | Used in some older digital cameras |

### Media Reader Purchase Factors
- Supported card types (get a **multi-format reader** if needed)
- Internal vs. External
- Size & connector type

---

## 4. External Storage (2.1.6.2)

### When to Use What
| Use Case | Recommended Device |
|---|---|
| Small transfers (e.g., a presentation) | USB Flash Drive (Thumb Drive) |
| Large backups / bulk data transfer | External HDD or SSD |

### Purchase Factors
- **Port type** — USB-A, USB-C, eSATA, Thunderbolt
- **Storage capacity** — Match to data volume needs
- **Speed** — SSD is significantly faster than HDD
- **Portability** — Compact if mobile; size less critical for desk use
- **Power requirements** — Most modern drives are bus-powered via USB

---

## 5. Power Connector Installation (Video)

### Connector Types & Locations

| Connector | Pins | Purpose |
|---|---|---|
| Main motherboard power | **24-pin** | Powers entire motherboard |
| CPU auxiliary power | **4-pin / 8-pin** | Powers the processor |
| CPU fan | **4-pin** | Powers CPU cooling fan |
| Case fan | **3-pin** | Powers case airflow fan |
| SATA power | **15-pin** | Powers HDDs and SSDs |

### Installation Rules
- **Listen for the click** — 24-pin and CPU connectors lock with an audible click
- **Check the clip/latch** — Ensure the locking tab engages on larger connectors
- **L-shaped key** — SATA connectors are physically keyed; cannot be inserted upside down
- **Never force it** — If it resists, the orientation is wrong; flip and retry
- **Fan connectors** — Guided by notches; may not click loudly but should slide in smoothly

---

## Quick Reference: Key Concepts

```
Expansion Slots:   PCIe x1 (NIC) | PCIe x16 (GPU)
Power Connectors:  24-pin (Mobo) | 4/8-pin (CPU) | 15-pin SATA | 3/4-pin Fan
Media Cards:       SD > MiniSD > MicroSD | CompactFlash | Memory Stick | xD
External Storage:  Flash Drive (small) | External SSD/HDD (large)
```

---

*Source: Cisco IT Essentials — Chapter 2.1.5–2.1.6*
