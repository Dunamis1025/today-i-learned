# Computer Hardware & Networking — Study Notes

---

## 1. Coaxial Cable

### Structure (Inside → Outside)
1. **Center conductor** — copper or copper-clad-steel; carries the signal
2. **Dielectric insulator** — non-conductive material surrounding the conductor
3. **Foil/braided shield** — blocks electromagnetic interference (EMI)
4. **PVC outer jacket** — physical protection

### Cable Types
| Type | Gauge | Shielding | Use Case |
|------|-------|-----------|----------|
| RG-6 | Heavy | High | Internet, Cable TV, Satellite TV |
| RG-59 | Thin | Low | Analog video, CCTV |

### Connectors
- **F-Type** — used with RG-6; screw-on connection (e.g., TV antenna wall port)
- **BNC** — used with RG-59; quarter-turn locking mechanism; used in professional audio/video equipment

---

## 2. SCSI & IDE (Legacy Internal Interfaces)

### SCSI (Small Computer Systems Interface)
- Connects multiple peripheral/storage devices using **daisy-chaining** (devices linked in series on a shared bus)
- **External (Centronics connector):** 36-pin or 50-pin; used for scanners and printers; secured with squeeze latches or bail locks
- **Internal:** 50-pin connector on a ribbon cable; used for internal hard drives

### IDE (Integrated Drive Electronics)
- Standard interface for connecting hard drives and optical drives to the motherboard
- Uses a **40-pin** ribbon cable (visually similar to internal SCSI)
- Typically 3 connectors per cable: **1 for motherboard** + **2 for drives**

> **Key difference:** SCSI supports more devices via daisy-chaining; IDE is limited to 2 drives per cable. Both are now replaced by **SATA**.

---

## 3. External vs Internal Computer Connections

### External Connections (accessible from outside the case)
- **USB** — connects keyboards, mice, external drives, etc.
- **DVI** — video output for monitors
- **Network (RJ-45)** — Ethernet/LAN port

### Internal Connections (inside the case only)
- **SATA** — connects motherboard to storage drives
- **IDE** — legacy version of SATA
- **Drive Activity LED** — front-panel indicator light; not a data connection

---

## 4. Monitor Characteristics

### Physical & Display Properties
| Term | Description |
|------|-------------|
| **Screen Size** | Diagonal measurement in inches (common: 19–24"; ultrawide: 30"+) |
| **Resolution** | Number of pixels (e.g., 1920×1080 = 1080p) |
| **Native Resolution** | The optimal resolution for a specific monitor (labeled "Recommended" in Windows) |
| **Native Mode** | When the GPU output exactly matches the monitor's native resolution |

### Connectivity
| Connector | Notes |
|-----------|-------|
| VGA / DVI | Older standards |
| **HDMI** | Carries audio + video; most common today |
| **DisplayPort** | Newest standard; supports highest resolutions and refresh rates |

> 💡 **More content on screen** → higher resolution. **Bigger elements** → larger screen size.

---

## 5. Monitor Technical Terms

### Image Quality
| Term | What It Means |
|------|--------------|
| **Pixel** | Smallest unit of a display; each pixel d
