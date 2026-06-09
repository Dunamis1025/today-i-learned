# Network Security: Flat vs. Segmented Network Architecture
> Security Impossible – Cyber Range Lab Notes  
> GNS3 Web UI Practical | Date: 2025-06-09

---

## Overview

This lab covers the analysis of a vulnerable **flat network**, identifying its security risks, and redesigning it into a **segmented, firewall-protected architecture** using GNS3.

---

## Phase 1: Auditing the Flat Network

### What is a Flat Network?
A flat network is one where **all devices share the same subnet** (e.g., `10.10.10.0/24`) with no internal barriers between them.

### Topology Observed
```
Internet
    |
Core-Router
    |
  Switch (single)
  / | \ \ \ \
C1 C2 C3 Web DNS File
```

### Inventory
| Type | Devices |
|------|---------|
| End-user Clients | Client-1, Client-2, Client-3 |
| Servers | WebServer, DNSServer, FileServer |
| Networking | 1× Flat-Switch, 1× Core-Router |

### Security Risks Identified

| Risk | Description |
|------|-------------|
| **Unrestricted Lateral Movement** | A single compromised client can freely reach all other devices — no internal barriers exist |
| **Critical Services Exposed** | FileServer and DNSServer share the same broadcast domain as clients — easy targets for sniffing/spoofing |
| **Expanded Attack Surface** | If the WebServer is compromised from the internet, attacker gains direct, unshielded access to all internal hosts |
| **No Visibility or Control** | No firewall chokepoint to monitor, log, or block malicious traffic |

---

## Phase 2: Redesigning the Secure Network

### Design Goals
- Divide the network into **logical security zones**
- Place **firewall chokepoints** between zones
- Apply **least-privilege access** — only allow what is explicitly needed

### New Topology
```
Internet
    |
Core-Router
    |
Firewall-1 (External/DMZ Firewall)
   /        \
Switch-3    Firewall-2 (Internal Firewall)
(DMZ)        /         \
  |        Switch-1   Switch-2
Web  DNS  (LAN-1)     (LAN-2)
           / | \          |
         C1  C2  C3    FileServer
```

### Zone Definitions

| Zone | Switch | Devices | Trust Level |
|------|--------|---------|-------------|
| **DMZ** | Switch-3 | WebServer, DNSServer | Low — internet-facing |
| **LAN-1** (User Zone) | Switch-1 | Client-1, Client-2, Client-3 | Medium |
| **LAN-2** (Internal Server Zone) | Switch-2 | FileServer | High — no direct internet access |

### Devices Used

| Device | Count | Role |
|--------|-------|------|
| Ubuntu Machine | 6 | 3× Clients + WebServer + DNSServer + FileServer |
| Router | 1 | Core-Router (internet gateway) |
| Open vSwitch (OVS) | 3 | Switch-1, Switch-2, Switch-3 |
| OPNsense Firewall | 2 | Firewall-1 (External), Firewall-2 (Internal) |

### Firewall Placement & Purpose

**Firewall-1 (External)**
- Sits between: `Core-Router ↔ Switch-3 (DMZ)`
- Purpose: All traffic entering the Web/DNS servers from the internet must pass inspection first

**Firewall-2 (Internal)**
- Sits between: `Firewall-1 ↔ Switch-1 (LAN-1) ↔ Switch-2 (LAN-2)`
- Purpose: Prevents lateral movement — even if a client is infected, malware cannot reach the FileServer

---

## Key Concepts

### Lateral Movement
When an attacker compromises one machine and moves sideways to other machines within the same network. Flat networks make this trivially easy.

### DMZ (Demilitarized Zone)
A network segment that sits between the public internet and the internal network. Public-facing servers (Web, DNS) live here — accessible from outside but isolated from sensitive internal resources.

### Defense in Depth
Layering multiple security controls so that if one fails, others still protect the system.
```
Internet → Firewall-1 → DMZ → Firewall-2 → Internal Zones
```

### Deny All / Allow by Exception
Firewalls default to blocking everything. Administrators must explicitly create **Allow rules** only for necessary traffic (e.g., allow HTTP/HTTPS to WebServer on port 80/443, DNS on port 53).

### Trust Zones
| Zone | Trust Level |
|------|-------------|
| Internet | Zero Trust |
| DMZ (Web/DNS) | Low Trust |
| LAN-1 (Clients) | Medium Trust |
| LAN-2 (FileServer) | High Trust |

---

## Traffic Flow: Before vs. After

### Before (Flat Network)
```
Client-1 → Switch → FileServer   ✅ Direct, no inspection
```

### After (Segmented Network)
```
Client-1 → Switch-1 → Firewall-2 → Switch-2 → FileServer
                           ↑
                     Must pass firewall rules
```

---

## Quiz Answers Summary

| Q | Answer |
|---|--------|
| Biggest risk of shared subnet | All devices in same broadcast domain → unrestricted L2 communication |
| Term for moving C1 → FileServer attack | **Lateral Movement** |
| Why WebServer = expanded attack surface | Compromised WebServer gives attacker unshielded path to all internal clients |
| Role of OPNsense | Security chokepoints — monitor, log, and block inter-zone traffic |
| Where to place Web/DNS servers | **DMZ** |
| Why Firewall-2 between Switch-1 and Switch-2 | Stops malware on client machines from spreading to FileServer |
| New path from Client-1 to FileServer | Client-1 → Switch-1 → Firewall-2 → Switch-2 → FileServer |
| Who decides DMZ → LAN packet flow | **OPNsense Firewall** |
| Why FileServer is in LAN-2, not DMZ | FileServer does not need to be publicly accessible |
| How to enable WebServer under Deny All policy | Add explicit Allow rule for HTTP/HTTPS traffic to WebServer |

---

## Real-World Applications

- **Financial institutions**: Separate employee Wi-Fi from payment processing systems using the same zone model
- **Healthcare**: Patient record servers (EMR) isolated from public-facing appointment portals (HIPAA compliance)
- **Cloud (AWS/Azure)**: VPCs and subnets implement these same zone boundaries virtually

---

## Next Steps

- [ ] Configure actual firewall rules in OPNsense CLI
- [ ] Study VLANs — how zones are enforced at the physical switch level
- [ ] Research High Availability — what happens if a firewall goes down?
- [ ] Explore Zero Trust Architecture (ZTA) — what if even LAN-1 clients are untrusted?
- [ ] Practice port-level rule mapping (HTTP=80, HTTPS=443, DNS=53, SSH=22)
