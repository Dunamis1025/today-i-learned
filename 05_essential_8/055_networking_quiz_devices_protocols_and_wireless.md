# Networking Devices, Protocols & Connectivity — Study Notes

## 1. Internet Connection Types

| Type | Key Feature |
|------|------------|
| **Line of Sight Wireless** | Always-on service; transmits radio signals from a tower directly to a receiver at a home/business; requires a clear, unobstructed path between transmitter and receiver |
| **Fiber (Fiber-optic)** | Fastest available connection; transmits data as pulses of light through glass/plastic strands; immune to EMI/RFI; least signal degradation over long distances |
| **DSL** | Uses the existing telephone network to connect to an ISP; requires a **DSL modem** to convert telephone signals into digital data |
| **LEO Satellite** | Low Earth Orbit; operates at ~550km altitude; supports ~100 Mbps with much lower latency (~20ms) than traditional GEO satellites (~600ms) |

---

## 2. Network Devices & Their Functions

| Device | Function |
|--------|----------|
| **Switch** | Forwards data based on the **destination MAC address** in the frame; sends data only to the specific port of the target device (more efficient than a hub) |
| **Patch Panel** | Termination point for cable runs; keeps cables organized and safely out of walkways |
| **Proxy Server** | Acts as an intermediary between users and the internet; caches frequently accessed web pages on the internal network to speed up access and reduce bandwidth |
| **Syslog Server** | Centralized repository for log messages from network devices (routers, switches, firewalls); used for troubleshooting, auditing, and monitoring network health |
| **Cloud-based Network Controller** | Allows administrators to remotely manage many network devices through a single dashboard interface |
| **UTM (Unified Threat Management)** | All-in-one security appliance (e.g., Cisco ASA 5505-X); combines stateful firewall + IDS/IPS into one device |

---

## 3. Firewall & Security

### Stateful Firewall
- Monitors **both incoming and outgoing** traffic
- Remembers the **state** of active connections — tracks whether a packet belongs to an already-permitted session
- Much smarter than stateless packet filtering

### IDS / IPS (Intrusion Detection / Prevention System)
- Actively scans network traffic for malicious patterns
- IDS = detects and alerts; IPS = detects and **blocks**

### UTM Device
- Combines stateful firewall + IDS/IPS into a single appliance
- Example: **Cisco ASA 5505-X**

---

## 4. Protocols & Port Numbers

| Protocol | Port | Purpose |
|----------|------|---------|
| **SMTP** | 25 | Sending emails |
| **POP** | 110 | Receiving emails (downloads to device) |
| **IMAP** | 143 | Receiving/managing emails (stays on server) |
| **HTTPS** | 443 | Secure web browsing |
| **SMB/CIFS** | 445 | File sharing |
| **SLP** | 427 | Service Location Protocol |

> **Rule**: Port numbers tell the server which application the data is intended for — like apartment numbers in a building.

---

## 5. Power over Ethernet (PoE)

- **Standard**: IEEE **802.3af**
- Delivers **both data and electrical power** over a single Ethernet cable
- Eliminates the need for separate power outlets

### Devices commonly powered by PoE
- **IP phones** (VoIP desk phones)
- **Wireless access points** (ceiling/wall-mounted)

### Devices NOT powered by PoE
- Routers, core switches, modular switches (too high power draw — use dedicated AC power)

---

## 6. Cabling & Interference

### UTP vs STP

| Feature | UTP | STP |
|---------|-----|-----|
| Shielding | None | Metallic foil/braid around wires |
| EMI resistance | Lower | Higher |
| RFI resistance | Lower | Higher |
| Cost | Cheaper | More expensive |

### Fiber Optic in High-EMI Environments
- Uses **light**, not electrical signals → **completely immune to EMI and RFI**
- Recommended for environments like airplane engine assembly plants where heavy machinery generates strong electromagnetic interference

---

## 7. Wireless Technologies

| Technology | Use Case | Range / Notes |
|------------|----------|---------------|
| **Bluetooth** | PAN (Personal Area Network) — headphones, smartwatch, keyboard | Short range; piconet supports up to **7 slave devices** simultaneously (3-bit addressing: 2³ = 8 addresses, 1 reserved for master) |
| **Z-Wave** | Smart home automation | Open standard; supports up to **232 devices** per network |
| **Wi-Fi (802.11n/ac)** | LAN wireless networking | Broader range; higher bandwidth |

### Why Bluetooth supports exactly 7 devices
- Uses a **3-bit Active Member Address (AMA)**
- 2³ = 8 possible addresses → 1 reserved for the master → **7 remaining for slave devices**
- Chosen for minimal overhead and low power consumption on small battery-powered devices

---

## 8. Network Scope

| Type | Coverage | Example |
|------|----------|---------|
| **PAN** | Personal area (~10m) | Bluetooth devices |
| **LAN** | Home / office building | Wi-Fi, Ethernet |
| **WAN** | Cities, countries, continents | The internet |

> **WAN characteristic**: Connects multiple networks that are **geographically separated**.

---

## 9. Port Numbers & Application Sessions

- Each application running on a PC is assigned a unique **source port number**
- When data returns from the internet, the OS uses port numbers to deliver it to the correct application
- **IP address** = building address (identifies the PC)
- **Port number** = room/apartment number (identifies the specific application)

---

## 10. Wiring Standards Recap

| Standard | Swapped Pairs |
|----------|--------------|
| T568A vs T568B | **Green and orange** pairs swap positions; blue and brown remain the same |
