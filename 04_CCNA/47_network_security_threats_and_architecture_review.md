# Network Fundamentals — Study Notes

> Cisco Networking Basics | Chapter Review Summary

---

## 1. Network Types by Geographic Scope

| Type | Full Name | Scope | Key Characteristic |
|------|-----------|-------|--------------------|
| **LAN** | Local Area Network | Small area (home, office, school) | Think: your home Wi-Fi router |
| **WAN** | Wide Area Network | Large area (cities, countries, continents) | Owned/managed by ISPs (e.g. telecoms) |
| **Intranet** | — | Organization-internal only | Only internal employees can access |
| **Extranet** | — | Organization + trusted outsiders | Secure access for partners/vendors |

### Quick Memory Trick
- **LAN** = Local = Living room
- **WAN** = Wide = World
- **Intranet** = Inside only
- **Extranet** = Extended to external partners

---

## 2. The Four Basic Characteristics of Network Architecture

### 2.1 Fault Tolerance
- The ability of a network to **continue operating even when a component fails**
- Achieved through **redundancy** — having multiple paths to a destination
- If one path goes down → traffic automatically reroutes through another
- **Example:** Multiple cables connecting buildings so one cut doesn't kill the network

### 2.2 Scalability
- The ability to **grow and expand** the network without replacing everything
- Achieved by following **accepted standards and protocols**
- Standardization ensures new devices from any manufacturer can join seamlessly
- **Example:** Adding 100 new computers to an office network without redesigning it

### 2.3 Quality of Service (QoS)
- A set of policies that **prioritize certain types of traffic** when the network is congested
- Voice and video calls are given higher priority (they break badly if delayed)
- Data downloads are given lower priority (a few seconds delay is acceptable)
- **Example:** During a busy network, your Zoom call stays clear while a file download slows down

### 2.4 Security
- Protects data and infrastructure from unauthorized access or attacks
- Built on three core principles — the **CIA Triad**:

| Principle | Meaning |
|-----------|---------|
| **Confidentiality** | Only authorized people can see the data |
| **Integrity** | Data is not tampered with during transmission |
| **Availability** | Data is accessible whenever it is needed |

---

## 3. Modern Network Trends

### BYOD (Bring Your Own Device)
- Policy allowing employees/students to use **personal devices** (phone, laptop, tablet) on a business or campus network
- Increases flexibility but also introduces security risks

### Cloud Computing
- Delivering IT resources (storage, software, servers) **over the internet**
- Deployment models:

| Type | Description |
|------|-------------|
| **Public** | Available to anyone (e.g. Google Drive, AWS) |
| **Private** | Exclusive to one organization |
| **Hybrid** | Mix of public + private |
| **Custom** | Tailored to specific needs |

### Video Communications
- Real-time face-to-face communication over the internet using cameras
- Best tool for meetings with people in different cities or countries
- **Examples:** Zoom, Microsoft Teams, Google Meet

### Powerline Networking
- Uses existing **electrical outlets/wiring** in a building to carry network data
- Useful where running new network cables is difficult
- Simply plug an adapter into a power socket → instant network connection

### Wireless Broadband
- Uses the same **cellular technology as smartphones** (4G/LTE, 5G) to provide internet access
- Used in areas where wired internet is unavailable

---

## 4. Network Security: Threats & Solutions

### Threats

| Threat | Description |
|--------|-------------|
| **Virus / Worm / Trojan Horse** | Malicious code that runs on user devices; steals data, corrupts files, causes malfunctions |
| **Denial of Service (DoS)** | Floods a system with fake requests until it slows down or crashes entirely |
| **Zero-Day / Zero-Hour Attack** | Attack that exploits a vulnerability on the **very first day** it is discovered — before any patch exists |

### Solutions

| Solution | Description |
|----------|-------------|
| **Firewall** | A security barrier that **blocks unauthorized access** to a network; filters incoming and outgoing traffic |
| **VPN (Virtual Private Network)** | Creates a **secure, encrypted tunnel** over the public internet; ideal for remote/work-from-home access |

---

## 5. Quick Concept Comparison Table

| Concept | Category | One-Line Summary |
|---------|----------|-----------------|
| LAN | Network Type | Small area network (home/office) |
| WAN | Network Type | Large area network (managed by ISPs) |
| Intranet | Network Type | Internal staff only |
| Extranet | Network Type | Internal + trusted external partners |
| Fault Tolerance | Architecture | Survives failures via redundancy |
| Scalability | Architecture | Grows easily thanks to standards |
| QoS | Architecture | Prioritizes important traffic (voice/video) |
| Security (CIA) | Architecture | Confidentiality + Integrity + Availability |
| BYOD | Trend | Personal devices on work/campus networks |
| Cloud Computing | Trend | IT resources delivered over the internet |
| Video Communications | Trend | Remote face-to-face meetings |
| Powerline | Connectivity | Network over electrical outlets |
| Wireless Broadband | Connectivity | Internet via cellular (4G/5G) |
| Virus/Worm/Trojan | Threat | Malicious code on devices |
| DoS | Threat | Overwhelm system until it crashes |
| Zero-Day | Threat | Attack on day vulnerability is discovered |
| Firewall | Defense | Blocks unauthorized network access |
| VPN | Defense | Secure encrypted tunnel for remote access |

---

## 6. Exam Tips

- **Redundancy → Fault Tolerance** (not Scalability)
- **Standards & Protocols → Scalability** (not Fault Tolerance)
- **CIA Triad → Security** (Confidentiality, Integrity, Availability)
- **Traffic priority during congestion → QoS**
- **Electrical outlet for networking → Powerline** (not Wi-Fi)
- **Cellular technology → Wireless Broadband** (not Powerline)
- **External partner access → Extranet** (not Intranet)
- **Personal device on work network → BYOD**
- **Crashes system with fake requests → DoS**
- **Day-zero vulnerability exploit → Zero-Day**
- **Blocks unauthorized access → Firewall** (not VPN)
- **Secure remote worker connection → VPN** (not Firewall)

---

*Last updated: 2026-06-01*
