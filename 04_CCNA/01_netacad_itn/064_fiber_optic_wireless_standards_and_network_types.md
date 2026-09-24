# Network Fundamentals – Study Notes

> Topics: Fiber-Optic Cables, Wireless Standards, Network Types

---

## 1. Fiber-Optic Cable Types

### Multimode vs. Single-Mode

| Category | Multimode | Single-Mode |
|---|---|---|
| **Core Size** | Larger (wider path) | Smaller (narrow path) |
| **Light Source** | LED (economical) | Laser (high-precision, expensive) |
| **Distance** | Short (~500m – 2km) | Long (dozens to hundreds of km) |
| **Cost** | Lower | Higher |
| **Use Case** | Building interiors, campus networks | Inter-city, transcontinental links |

### Key Rules to Remember
- **Campus network** → **Multimode** (short distance, cost-effective)
- **500m data transfer** → **Multimode**
- **LED light source** → **Multimode**
- **Long-haul / backbone** → **Single-Mode**

---

## 2. Wireless Standards Comparison

| Standard | Range | Power Use | Best For |
|---|---|---|---|
| **Wi-Fi** | ~100m (indoors) | High | Home/office LAN, general internet |
| **Bluetooth** | 1–100m | Low-Medium | PAN – personal devices (earbuds, watch, phone) |
| **Zigbee** | ~10–100m (mesh) | Very Low | Industrial IoT, sensors, automation |
| **WiMAX** | Tens of km | High | Wide-area networks, city-scale coverage |

### Key Rules to Remember
- **PAN (Personal Area Network), 1–100m** → **Bluetooth**
- **Industrial / IoT environments** → **Zigbee** (low power + mesh networking)
- **City-wide coverage** → **WiMAX**
- **General LAN** → **Wi-Fi**

---

## 3. True/False Concepts – Common Exam Traps

### ❌ "Wireless is not suited for enterprise networks." → **FALSE**
Modern enterprise wireless:
- Provides **mobility** for employees using laptops, tablets, smartphones
- Offers **robust security** (enterprise-grade APs with advanced encryption and access control)
- Reduces **cabling costs** and enables flexible office layouts

### ❌ "Wireless LANs operate in full-duplex, so user count doesn't affect performance." → **FALSE**
- Wireless LAN is a **shared medium** – all devices share the same frequency/airwaves
- More users = more congestion = **slower speeds for everyone**
- Like a highway: more cars → more traffic jams
- Even Wi-Fi 6 (with near-full-duplex features) cannot eliminate performance degradation as users increase

---

## 4. Quick Concept Glossary

| Term | Meaning |
|---|---|
| **PAN** | Personal Area Network – devices within ~1–100m of a person |
| **LAN** | Local Area Network – building or campus scale |
| **WAN** | Wide Area Network – city, country, or global scale |
| **Mesh Network** | Devices relay signals to each other (used by Zigbee) |
| **Full-Duplex** | Simultaneous send and receive (not truly available in standard wireless LAN) |
| **Multimode Fiber** | Short-distance fiber using LED; wide core |
| **Single-Mode Fiber** | Long-distance fiber using laser; narrow core |

---

## 5. Memory Shortcuts

```
Short distance  → Multimode fiber
Long distance   → Single-mode fiber

Personal gadgets  → Bluetooth
Home/office Wi-Fi → Wi-Fi (802.11)
IoT / Sensors     → Zigbee
City-wide network → WiMAX

Wireless in enterprise? → YES (security + mobility)
More Wi-Fi users = slower? → YES (shared medium)
```

---

*Study session powered by Gemini + Claude · June 2026*
