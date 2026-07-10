# Network Fundamentals – Study Notes (5.5.1.1)

## 1. Network Types

| Type | Description |
|------|-------------|
| PAN | Connects personal devices (keyboard, mouse, printer) over short distances; often uses Bluetooth |
| LAN | Local network within a building or campus |
| WLAN | Wireless version of LAN |
| WAN | Spans large geographic areas (countries/continents); used to connect branch offices to HQ |
| VPN | Secure virtual network over the internet |

**Internet Connection Methods:** DSL, fiber optics, satellite, mobile tethering, Ethernet over Power (uses existing electrical wiring)

---

## 2. TCP/IP Model

| Layer | Name | Role | Key Protocols |
|-------|------|------|---------------|
| 4 | Application | User-facing services | HTTP (port 80), DNS, DHCP |
| 3 | Transport | Reliable/fast delivery | TCP, UDP |
| 2 | Internet | IP-based routing | IP |
| 1 | Network Access | Physical transmission | Ethernet, Wi-Fi |

### TCP vs UDP

| | TCP | UDP |
|--|-----|-----|
| Connection | Connection-oriented | Connectionless |
| Reliability | Guaranteed delivery, ordered | No delivery guarantee |
| Speed | Slower | Faster |
| Use case | Web browsing, email | Streaming, gaming |

---

## 3. Wireless Technologies

### Wi-Fi Standards

| Standard | Frequency | Notes |
|----------|-----------|-------|
| 802.11b | 2.4GHz | Early standard |
| 802.11g | 2.4GHz | Faster than b |
| 802.11n | 2.4GHz / 5GHz | Dual-band |
| 802.11a | 5GHz | Less common |
| 802.11ac | 5GHz | High performance |

### Short-Range & Smart Home

- **Bluetooth / NFC** – short-range personal device communication
- **Zigbee** – smart home standard; requires a **coordinator** device to manage the network
- **Z-Wave** – another smart home wireless protocol

### Cellular Evolution

1G → 2G → 3G → 4G → **5G**

---

## 4. Network Hardware

| Device | Layer | How It Works |
|--------|-------|--------------|
| NIC | 1 | Connects a device to the network |
| Hub | 1 | Repeats signal to **all ports**; no segmentation; one collision domain |
| Repeater | 1 | Regenerates signal to extend distance |
| Switch | 2 | Forwards data using **MAC addresses**; each port = separate collision domain |
| Router | 3 | Routes data using **IP addresses** between different networks |

> **Key point:** A hub regenerates the signal without segmenting the network — it blindly forwards data to every connected port.

---

## 5. Network Security

| Technology | Type | Function |
|------------|------|----------|
| Firewall | Prevention | Blocks unauthorized traffic based on rules |
| IDS | Detection (passive) | Monitors traffic and alerts admins of suspicious activity |
| IPS | Prevention (active) | Detects and actively blocks threats in real time |
| UTM | All-in-one | Combines firewall, IDS, IPS, and more into a single appliance |

> **IDS = security camera** (watches and reports) | **IPS = security guard** (watches and acts)

---

## 6. Cabling

### Cable Types

**Copper Cables**

| Type | Details |
|------|---------|
| Coaxial | Copper/aluminum core with strong shielding; used in cable TV and satellite; harder to install than UTP |
| UTP (Unshielded Twisted-Pair) | Most common LAN cable; affordable and easy to install; vulnerable to EMI/RFI |
| STP (Shielded Twisted-Pair) | Foil-shielded pairs; blocks EMI/RFI; more expensive; must be properly grounded or it acts as an antenna |

Both UTP and STP use **RJ-45 connectors**.

**Fiber Optic**
- Transmits data as **light pulses** through glass or plastic strands
- Much faster and longer range than copper
- Immune to EMI/RFI

### Wiring Standards: T568A vs T568B

| Pin | T568A | T568B |
|-----|-------|-------|
| 1 | White/Green | White/Orange |
| 2 | Green | Orange |
| 3 | White/Orange | White/Green |
| 4 | Blue | Blue |
| 5 | White/Blue | White/Blue |
| 6 | Orange | Green |
| 7 | White/Brown | White/Brown |
| 8 | Brown | Brown |

| Cable Type | Wiring | Use Case |
|------------|--------|----------|
| Straight-through | Same standard both ends (A-A or B-B) | PC → Switch, Switch → Router |
| Crossover | T568A one end, T568B other | PC → PC, Switch → Switch |

> **T568B** is the most widely used standard in commercial/enterprise environments. No performance difference between the two — just stay consistent.

---

## 7. Key Port Numbers

| Protocol | Port |
|----------|------|
| HTTP | 80 |
| HTTPS | 443 |
| DNS | 53 |
| DHCP | 67/68 |

---

## 8. Quick-Reference: Important Protocols & Services

| Term | Definition |
|------|-----------|
| DHCP | Automatically assigns IP addresses to devices on a network |
| HTTP | Protocol for standard web browsing (port 80) |
| MAC Address | Hardware address used by switches (Layer 2) |
| IP Address | Logical address used by routers (Layer 3) |
| Ethernet over Power | Uses existing electrical wiring to carry network data |
