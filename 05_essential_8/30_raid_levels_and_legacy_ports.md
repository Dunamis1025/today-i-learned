# Study Notes: RAID & Computer Ports

> **Date:** 2026-06-09
> **Topics:** RAID Levels, Video Ports, Legacy Ports

---

## 1. RAID (Redundant Array of Independent Disks)

A technology that **groups multiple hard drives together** to work as a single unit — improving speed, safety, or both.

### Core Concepts

| Concept | Description |
|---|---|
| **Striping** | Splits data across multiple drives → faster read/write |
| **Mirroring** | Duplicates data on two drives → redundancy |
| **Parity** | Stores math-based checksum data → allows recovery if one drive fails |
| **Double Parity** | Two sets of parity data → survives up to two simultaneous drive failures |

### RAID Levels

| RAID Level | Method | Speed | Safety | Storage Efficiency |
|---|---|---|---|---|
| **RAID 0** | Striping only | ⚡ Fastest | ❌ None (one failure = total loss) | 100% |
| **RAID 1** | Mirroring only | Normal | ✅ High | 50% |
| **RAID 5** | Striping + Parity | Fast | ✅ Good (survives 1 failure) | ~67–94% |
| **RAID 6** | Striping + Double Parity | Moderate | ✅✅ Very High (survives 2 failures) | ~50–88% |
| **RAID 10** | Mirroring + Striping | ⚡ Fast | ✅✅ Very High | 50% |

### Quick Selection Guide

- **Personal use** → RAID 1 or RAID 5
- **Enterprise / mission-critical** → RAID 10
- **Max speed, no redundancy needed** → RAID 0

---

## 2. Video / Graphics Ports

Ports that connect your computer to a display. Evolution: **Analog → Digital → High-speed Digital**

| Port | Type | Key Feature |
|---|---|---|
| **VGA** | Analog | 15-pin, blue connector; legacy/outdated |
| **DVI** | Digital | Early LCD standard; digital signal |
| **HDMI** | Digital | Carries **both video and audio**; most common today |
| **DisplayPort (DP)** | Digital | High-performance; preferred for gaming & high-res monitors |

---

## 3. Legacy Ports

Older connectors that were **device-specific** before USB became the universal standard.

| Port | Pins | Purpose | Status |
|---|---|---|---|
| **Serial** | 9 or 25-pin (DB-9/DB-25) | Printers, modems, mice; now used for network device console config | Legacy |
| **Parallel** | 25-pin receptacle | Printers ("printer port"); sends multiple bits at once | Legacy |
| **Game Port** | 15-pin | Joystick / game controllers; later merged into sound cards | Obsolete |
| **PS/2** | 6-pin | Keyboard (purple) & Mouse (green) dedicated ports | Legacy |
| **Audio (3.5mm)** | — | Pink = Mic in, Green = Speaker/headphone out, Blue = Line in | Still used |

---

## Summary

```
Legacy Era                         Modern Era
─────────────────────────────────────────────
Every device → own port      →    USB (universal)
VGA (analog)                 →    HDMI / DisplayPort (digital)
Single HDD (vulnerable)      →    RAID (redundant, fast)
```

> **Key takeaway:** Hardware has evolved from specialized, fragmented connections toward universal, high-speed, and fault-tolerant systems.
