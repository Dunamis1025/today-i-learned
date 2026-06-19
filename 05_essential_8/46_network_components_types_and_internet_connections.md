# Computer Networks — Fundamentals (Chapter 5 Notes)

Study notes covering network components, network types, and Internet connection technologies.

---

## 1. Why Networks Matter

Computer networks let people share resources and communicate, forming the foundation for services like email, the web, and online media. This section covers the principles, standards, and purposes of these networks.

**Topics covered in this chapter:**
- **Network Devices** — hubs, switches, access points, routers, firewalls
- **Connection Types** — DSL, cable, cellular, satellite
- **Communication Models** — the four layers of the TCP/IP model
- **Wireless Technology** — Wi-Fi (IEEE 802.11), RFID/NFC, Zigbee, Z-wave
- **Cabling** — twisted-pair, fiber-optic, coaxial cable
- A hands-on exercise: building and testing a straight-through UTP Ethernet cable

---

## 2. Core Network Components

Networks are made up of three categories of building blocks:

### Host Devices
End devices that users interact with directly (computers, smartphones). They sit at the **edge** of the network and run applications — web browsers, email clients — that access network services.

### Intermediary Devices
Devices that manage data flow *between* hosts:

| Device | Function |
|---|---|
| **Switch** | Connects multiple devices within a network |
| **Router** | Forwards traffic between different networks |
| **Wireless Router** | Connects wireless devices; often also functions as a switch for wired devices |
| **Access Point (AP)** | Extends Wi-Fi range by connecting to a wireless router |
| **Modem** | Connects a home/office to the Internet |

### Network Media
The physical or wireless channel data travels through. In diagrams, a **cloud icon** typically represents the Internet — the medium connecting separate networks.

---

## 3. Types of Networks (by Size/Purpose)

| Type | Full Name | Description |
|---|---|---|
| **PAN** | Personal Area Network | Connects nearby personal devices (phone, tablet, mouse), usually via Bluetooth |
| **LAN** | Local Area Network | Wired connection of devices in a small area (home, office, school) |
| **WLAN** | Wireless LAN | Like a LAN, but devices connect wirelessly via radio waves (Wi-Fi) |
| **WMN** | Wireless Mesh Network | Multiple APs combined to extend wireless coverage across a large home/building |
| **VLAN** | Virtual LAN | Logically segments one physical switch into multiple virtual networks, grouped by admin purpose rather than physical location |
| **MAN** | Metropolitan Area Network | Connects multiple buildings across a campus or city |
| **WAN** | Wide Area Network | Connects networks across large geographic distances; the Internet is the largest example |
| **VPN** | Virtual Private Network | Creates an encrypted tunnel over an insecure network (e.g., the Internet) for secure remote access — commonly used by teleworkers |

### VLAN Deep Dive
VLANs let a single physical switch behave like several independent ones:

- **Flexible grouping** — Users can be grouped by department/role regardless of physical location (e.g., IT staff on different floors share one VLAN).
- **Security & management** — Communication between VLANs is blocked by default, isolating sensitive traffic.
- **Traffic efficiency** — Segmenting limits broadcast traffic from flooding the whole network.
- **Inter-VLAN communication** requires a routing device (e.g., a router) to bridge VLANs.

---

## 4. Evolution of Internet Connection Technology

1. **Analog Telephone (Dial-up)** — 1990s; used standard voice phone lines + an analog modem; very slow.
2. **ISDN** (Integrated Services Digital Network) — used multiple channels over phone lines to carry voice, video, and data simultaneously; an early form of broadband.
3. **Broadband** — today's standard; uses different frequencies to send multiple signals over one medium simultaneously (e.g., TV + Internet on one cable, or voice call + browsing on one phone). Includes cable, DSL, satellite, and cellular.

---

## 5. Wired Connection Methods

### DSL vs. Cable
Both use a **modem** to connect to an ISP.

- **DSL** — uses copper telephone lines; "always-on" (no dial-up needed); voice and data signals use different frequencies, separated by filters to avoid interference; **VDSL** offers much higher speeds.
- **Cable** — uses coaxial cable (originally for cable TV), not telephone lines; connecting a router to the modem lets multiple devices share the connection.

### Fiber Optic
- Made of glass/plastic; transmits data as **light** → very high bandwidth.
- Backbone of the Internet; critical for large enterprises and data centers.
- Increasingly replacing older copper infrastructure.
- **FTTC** (Fiber to the Curb) — fiber runs to a neighborhood node, then copper/coax for the final stretch to the home.
- **FTTP** (Fiber to the Premises) — fiber runs directly into the building; an **ONT** (optical network terminal) converts the light signal into an electrical signal for use with standard Ethernet.
- Availability depends on geographic location and local ISPs.

---

## 6. Wireless Connection Methods

### Line-of-Sight Wireless Internet
Requires an unobstructed, direct path between a transmission tower and the user's receiver.

- **How it works**: a receiving antenna picks up RF signals directly from the provider's tower.
- **Frequency vs. range trade-off**:
  - Lower frequency (~900 MHz) → longer range, up to ~65 km (40 mi)
  - Higher frequency (~5.7 GHz) → shorter range, ~3 km (2 mi)
- **Limitations**: trees, tall buildings, and severe weather can block or weaken the signal — clear line of sight is essential.

### Satellite Internet
Used where cable/DSL aren't available (rural, remote, maritime areas).

- Uses a satellite dish for two-way communication with an orbiting satellite that relays data to the ISP.
- **Speed**: download ≥10 Mb/s typical; upload roughly 1/10th of download speed.
- **Latency**: high, since signals travel to space and back — problematic for gaming, VoIP, video calls.
- **LEO (Low Earth Orbit) satellite service**: newer approach using many satellites closer to Earth; speeds up to ~100 Mb/s with much lower latency (100–200 ms). The dish includes a motor to track moving satellites.

### Cellular Internet
- Coverage area is divided into **cells**, each served by a tower (base station).
- Connections hand off automatically between towers as the user moves, keeping service uninterrupted.
- Speeds have improved with each generation since 3G.
- In some regions/demographics, smartphones are the **primary** means of Internet access (e.g., per Pew Research, 20% of U.S. adults had no home broadband in 2018, rising to 28% among 18–29 year-olds, who relied on smartphones instead).

### Tethering & Mobile Hotspot
- **Tethering**: sharing a phone's cellular data connection with another device via Wi-Fi, Bluetooth, or USB cable.
- **Mobile Hotspot**: a specific form of tethering where the phone acts as a wireless AP, letting multiple nearby devices join its Wi-Fi and share the connection simultaneously.

---

## 7. Home / Small Office Network Setup

A typical setup combines several devices to get multiple devices online:

1. **ISP line → Modem**: converts the external signal into a digital signal local devices understand.
2. **Modem → Integrated Router**: provides Wi-Fi for wireless devices and wired ports for direct cable connections (PCs, consoles, etc.).
3. **Expansion**: adding switches or extra access points increases wired ports or extends wireless coverage when more devices need to connect.

Together, these devices function like a hub, letting every device in the home share the Internet connection and communicate with each other.
