# Network Security & IoT - Study Notes
> Cisco Essentials 8 | Chapter 6.1

---

## 1. UPnP (Universal Plug and Play)

UPnP allows devices to automatically discover and connect to a network without manual configuration.

**Why it's dangerous:**
- No authentication process — every device is trusted by default
- Attackers can exploit this to intercept traffic or exfiltrate sensitive data
- Most routers have UPnP **enabled by default**

**What to do:**
- Access your router settings and **disable UPnP**
- Use an online vulnerability profiling tool to check if your router is exposed

---

## 2. DMZ (Demilitarized Zone)

A DMZ is a separate network segment that sits between the public internet and the internal private network.

**Purpose:**
- Hosts servers that need to be publicly accessible (e.g., web servers, email servers)
- If a DMZ server is compromised, the internal network remains protected

**How it works on a router:**
- All incoming internet traffic is forwarded directly to one designated device
- That device is **fully exposed** to the internet — no longer protected by the router's firewall
- Must have **firewall software installed on the device itself**

**Key tradeoff:** Easy external access vs. high security risk

---

## 3. Port Forwarding & Port Triggering

### Port Forwarding
Allows specific external traffic to reach a designated internal device by opening a specific port.

- Example: All traffic on **port 80 (HTTP)** → forwarded to internal server at `10.10.10.50`
- The port stays **permanently open**
- More targeted than DMZ — only the necessary port is exposed

### Port Triggering
A dynamic, temporary version of port forwarding.

- The router **watches for outgoing traffic** on a trigger port
- When detected, it automatically opens the required incoming port
- Once the session ends, the port is **automatically closed**
- More secure than standard port forwarding

| Feature | DMZ | Port Forwarding | Port Triggering |
|---|---|---|---|
| Ports opened | All | Specific (permanent) | Specific (temporary) |
| Security risk | High | Medium | Low |
| Use case | Full server exposure | Web/game servers | Gaming sessions |

---

## 4. MAC Address Filtering

Controls which devices can connect to the network using their unique hardware identifier (MAC address).

**Two modes:**
- **Whitelist** — only listed MAC addresses are allowed
- **Blacklist** — listed MAC addresses are blocked

**How to find a MAC address:**
- Windows: `ipconfig /all` → look for "Physical Address"
- iPhone/Android: Settings → About → Wi-Fi Address

**Limitations:**
- One device can have multiple MAC addresses (wired vs. wireless interfaces)
- Must be manually updated when adding new devices
- MAC addresses can be spoofed by determined attackers
- Best used **alongside** other security measures, not as the sole defense

---

## 5. Whitelisting & Blacklisting

Controls network access based on IP addresses or websites.

| | Whitelist | Blacklist |
|---|---|---|
| Logic | Allow only approved items | Block specific items |
| Best for | Restricting users to safe content | Blocking known bad sites |
| Management | Strict but secure | Flexible but reactive |

**Limitation:** Both require **manual updates** and can be difficult to maintain at scale. Consider dedicated parental control or content filtering software for easier management.

---

## 6. IoT (Internet of Things)

IoT refers to the connection of everyday physical objects to the internet, enabling them to communicate and be controlled remotely.

**Common home IoT devices:**
- Smart thermostats
- Lighting systems
- Security cameras
- Smart locks
- Voice-enabled assistants (e.g., Amazon Echo, Google Home)

**How they work:**
- Connected to your home network
- Monitored and controlled via a single interface (usually a smartphone app)

**Security concern:**
- IoT devices expand the **attack surface** of your network
- Many IoT devices have weak default security settings
- Each connected device is a potential entry point for attackers

---

## 7. Packet Tracer Lab — Configure Firewall Settings (Summary)

### Topology
```
Server0 ──┐
           WRS1 ── Telco Cloud ── DNSsrv
PC0 ──────┘                  └── Remote PC
Laptop0 (wireless)
Laptop1 (wireless)
```

### What was configured:

**Step 1 — Router Access**
- Accessed WRS1 at `192.168.0.1` from PC0
- Credentials: `admin` / `admin`
- SSID: `aCompany` | Passphrase: `aCompWiFi`

**Step 2 — Wireless Client Setup**
- Connected Laptop0 and Laptop1 to WRS1
- Laptop0: IP `192.168.0.102` | MAC `0001.9794.EB38`
- Laptop1: IP `192.168.0.104` | MAC `000B.BE43.CEE3`

**Step 3 — MAC Filtering**
- Enabled MAC filtering on WRS1
- Registered only Laptop0's MAC (`00:01:97:94:EB:38`)
- Result: Laptop0 maintained connection; **Laptop1 was disconnected** (blocked at association level)

**Step 4 — Connectivity Test**
- Laptop0 successfully pinged Remote PC at `209.165.201.29`
- Remote PC could NOT access `www.acompany.com` → WRS1 didn't know which internal device to forward to

**Step 5 — DMZ**
- Enabled DMZ on WRS1, pointed to `192.168.0.20` (Server0)
- Remote PC successfully loaded `www.acompany.com`
- DMZ then **disabled** after verification

**Step 6 — Single Port Forwarding**
- Configured HTTP (port 80) → `192.168.0.20` (Server0)
- Remote PC successfully loaded `www.acompany.com` without DMZ
- More secure: only port 80 exposed, all other ports remain closed

### Key Takeaway
> DMZ opens **all ports** to a device. Single Port Forwarding opens **only what's needed**. Always prefer port forwarding over DMZ for better security.

---

## Quick Reference — Security Features Comparison

| Feature | What it controls | Security level |
|---|---|---|
| UPnP | Auto device discovery | ❌ Very low — disable it |
| DMZ | All traffic → one device | ⚠️ Low — use carefully |
| Port Forwarding | Specific port → one device | ✅ Medium |
| Port Triggering | Temporary port → one device | ✅ Medium-High |
| MAC Filtering | Device hardware ID | ✅ Basic — use with others |
| Whitelist/Blacklist | IP addresses / websites | ✅ Good with upkeep |
