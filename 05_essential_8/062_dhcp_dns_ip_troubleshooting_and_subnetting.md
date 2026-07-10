# Networking Study Notes

## IP Addressing

### APIPA (Automatic Private IP Addressing)
- Address range: `169.254.x.x`
- Self-assigned when a device **cannot reach a DHCP server**
- Devices with APIPA can only communicate with other APIPA devices on the same local segment
- Cannot reach the internet or any external network
- **Fix:** Restart the DHCP server so devices can obtain a valid address

### DHCP (Dynamic Host Configuration Protocol)
- Automatically assigns IP addresses to devices on a network
- Eliminates manual (static) configuration
- When a device moves floors/locations and can't get an IP, check if it's **statically configured** — static IPs don't auto-request from DHCP
- Useful commands (Windows):
  - `ipconfig /release` — drops the current IP address
  - `ipconfig /renew` — requests a new IP from the DHCP server

### Static IP Conflicts
- An **IP address conflict** occurs when two devices share the same IP
- Common cause: a static IP on one device overlaps with a DHCP-assigned address
- **Fix:** Change the static IP to one outside the DHCP pool

### Subnet Mask & CIDR Notation
- A subnet mask defines how many bits represent the **network portion** of an IP address
- Binary conversion determines the prefix length:

| Subnet Mask   | Binary                                      | CIDR |
|---------------|---------------------------------------------|------|
| 255.0.0.0     | 11111111.00000000.00000000.00000000         | /8   |
| 255.255.0.0   | 11111111.11111111.00000000.00000000         | /16  |
| 255.255.255.0 | 11111111.11111111.11111111.00000000         | /24  |

- Example: IP `192.168.150.16` with mask `255.255.0.0` → **16 bits** for network address

### IPv6 Host Identifier
- IPv6 addresses are 128 bits, divided into 8 segments of 16 bits each
- With a `/64` prefix: first 4 segments = **network**, last 4 segments = **host identifier**
- Example: `2001:0db8:cafe:4500:1000:00d8:0058:00ab/64`
  - Network: `2001:0db8:cafe:4500`
  - Host ID: `1000:00d8:0058:00ab`

---

## DNS (Domain Name System)
- Translates human-readable hostnames (e.g., `www.google.com`) into IP addresses
- **Symptom of DNS failure:** can ping an IP address but not the hostname
- Network connectivity is fine; the name-to-IP translation is broken

### Domain Name Resolution Failure
- If a domain times out but the IP address works → **DNS resolution failed**
- The DNS record may not point to the correct IP yet (e.g., newly registered domain)

---

## HTTP vs HTTPS
- `http://` — unencrypted connection
- `https://` — encrypted connection using **SSL/TLS** (port 443)
- To access secure content, explicitly use `https://` in the URL

---

## Network Troubleshooting

### Loopback Test
- Pinging the loopback address (`127.0.0.1`) tests if the **network card itself** is working
- Successful loopback + failed gateway = physical or external issue (not the NIC)

### Faulty Network Cable
- Indicators: switch port LED is off **and** NIC LED is off
- Loopback ping succeeds (NIC is fine), but no physical link detected
- Most likely cause: **bad or disconnected cable**

### Key CLI Commands

| Command          | Purpose                                      |
|------------------|----------------------------------------------|
| `ping`           | Tests connectivity to a host                 |
| `ipconfig /release` | Releases the current IP address           |
| `ipconfig /renew`   | Requests a new IP from DHCP               |
| `tracert`        | Traces the route packets take to a destination |

---

## Network Protocols & Services

### DHCP vs APIPA vs ICMP vs SMTP vs FTP
| Protocol | Role |
|----------|------|
| DHCP     | Auto-assigns IP addresses |
| APIPA    | Self-assigns fallback IPs when DHCP is unreachable |
| ICMP     | Used for diagnostics (ping, tracert) |
| SMTP     | Sends email |
| FTP      | Transfers files |

### NetBIOS
- Legacy Windows network protocol, required only on systems **older than Windows 2000**
- No modern security features; considered **obsolete and insecure**
- Should be disabled on modern systems

### DSL (Digital Subscriber Line)
- Provides high-speed internet over existing **telephone (copper) lines**
- Separates voice and data using different frequency bands — both can be used simultaneously

---

## Network Hardware

### Wireless Router
- Required to create a home wireless (Wi-Fi) network
- Distributes the internet connection wirelessly to multiple devices simultaneously

### Network Switch — MAC Address Table
- A switch maps each **physical port** to the **MAC address** of the connected device
- Administrators use the MAC address table (CAM table) to identify which device is on which port

---

## Network Security

### Preventing Unauthorized Device Access (Temporary Measures)
Two effective temporary steps when network changes create vulnerability:
1. **Disable DHCP** — stops unauthorized devices from auto-obtaining an IP
2. **Assign static IPs to authorized devices** — ensures only known devices can communicate

### Port Triggering
- A dynamic firewall feature on routers
- When an internal device sends traffic **out** through the **trigger port** (e.g., port 25), the router temporarily opens the **open port** (e.g., port 113) for **inbound** traffic back to that device
- More secure than port forwarding because the port only opens when triggered

---

## Loopback Tool — Serial Communication
- A **loopback plug** is used to test serial (or other) communication ports
- It loops the outgoing signal back into the receiving pins of the same port
- Confirms whether the port or cable can successfully send and receive data

---

## Quick Reference: Common IP Issues

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `169.254.x.x` address | DHCP server unreachable | Restart DHCP server |
| Moved PC can't connect | Static IP configured | Switch to automatic (DHCP) |
| IP address conflict | Static IP overlaps DHCP pool | Change the static IP |
| Can ping IP, not hostname | DNS failure | Check/restart DNS server |
| Domain times out, IP works | DNS resolution failed | Check DNS records |
| NIC LED off, switch port off | Faulty cable | Replace/reseat network cable |
| Need new IP from DHCP | Stale/incorrect IP | Run `ipconfig /renew` |
