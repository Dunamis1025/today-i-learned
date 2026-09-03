# Layer 2 Security Considerations (VU23218 - Module 14)

## Overview

Layer 2 is often called the **weakest link** in a network. Even if Layers 3–7 are protected with firewalls, VPNs, and IPS devices, a compromise at Layer 2 can undermine every layer above it, since all higher-layer traffic still has to pass through the switch.

Real-world note: ~85% of networking issues trace back to the **Physical layer** (Layer 1) — disconnected cables, wrong connectors, interference — before any Layer 2/3 misconfiguration is even considered.

---

## 1. Protocol Data Units (PDU) by Layer

| Layer | PDU Name |
|---|---|
| Application / Presentation / Session | Data |
| Transport | **Segment** (TCP) / **Datagram** (UDP) |
| Network | Packet |
| Data Link | Frame |
| Physical | Bits (electrical signal, not literally 0/1 — the receiver interprets analog signals as binary) |

---

## 2. Switch Fundamentals — MAC Address Table (CAM Table)

- A Layer 2 switch is **protocol-agnostic**: it doesn't care whether the frame carries an IPv4 packet, ARP message, or IPv6 ND packet. It forwards purely based on **MAC addresses**.
- The MAC Address Table is also called the **CAM Table (Content Addressable Memory)** — you search by content (MAC address) to find the location (port).

### Learning process
1. Every incoming frame's **source MAC address** is examined.
   - If not in the table → added along with the incoming port number.
   - If already in the table → the aging timer is refreshed.
2. Entries expire if no traffic is seen for the aging period (commonly cited as ~300 seconds / 5 minutes in documentation, though real default behavior can be shorter, e.g. ~30 seconds depending on platform).

### Forwarding process
1. The **destination MAC address** of the frame is checked against the table.
2. If found → forwarded **only** out that specific port.
3. If **not found** → the switch **floods** the frame out all ports except the one it came in on. This is called an **Unknown Unicast**.
   - This flooding is also why the **first ping in a sequence often fails/times out** — the sender doesn't yet know the destination's MAC address and must first resolve it via ARP.

### Switch vs. Hub
- **Hub**: forwards every frame out **all** ports (broadcast-like behavior).
- **Switch**: learns and forwards intelligently to the specific destination port — until it doesn't know the destination, at which point it temporarily behaves like a hub (flooding).

---

## 3. ARP (Address Resolution Protocol)

- Devices know **IP addresses** but need to resolve them to **MAC addresses** to build a Layer 2 frame.
- Process: a device broadcasts "Who has this IP? Tell me your MAC address," and the owner responds.
- Resolved mappings are stored in the **ARP cache**, checked with `arp -a`.
- This resolution delay is another reason the first packet in a new communication can be dropped.

**Security relevance**: ARP has no built-in authentication, making it vulnerable to **ARP spoofing/poisoning**, where an attacker falsely claims to own another device's IP address.

---

## 4. MAC Table Attacks

- **MAC Address Table Overflow (MAC Flooding)**: an attacker floods the switch with frames containing thousands of fake source MAC addresses, filling the CAM table to capacity.
- Once full, the switch can no longer learn new legitimate entries and **fails open** — it starts flooding all traffic out every port (like a hub), allowing the attacker to sniff traffic that shouldn't be visible to them.

---

## 5. Address Spoofing Attacks (MAC Spoofing)

- The attacker **changes their own host's MAC address** to match a legitimate target's MAC address.
- Since the switch trusts whatever source MAC address it sees, it **overwrites** the CAM table entry, redirecting traffic destined for the real host to the attacker instead.
- Can be combined with ARP spoofing for a **Man-in-the-Middle (MITM)** attack: the attacker intercepts traffic (e.g., destination port 80, capturing HTTP data) while transparently forwarding it to the real gateway/destination — so the victim notices no disruption.

---

## 6. Mitigation: Port Security

Port Security restricts which MAC address(es) are allowed to send traffic into a given switch port.

### Key configuration commands
```
interface range f0/1 - 2
 switchport mode access
 switchport port-security
 switchport port-security maximum 1
 switchport port-security mac-address sticky
 switchport port-security violation restrict
```

- `switchport port-security maximum 1` — limits the port to one learned/allowed MAC address.
- `switchport port-security mac-address sticky` — the switch **dynamically learns** the first MAC address seen on the port and **automatically writes it into the running-config** as if it were manually typed. Combines the convenience of dynamic learning with the permanence of static configuration.
- Unused ports should be explicitly shut down as a baseline defense:
```
interface range f0/3 - 24, g0/1 - 2
 shutdown
```

### Violation Modes

| Mode | Blocks unauthorized traffic? | Increments violation counter? | Sends syslog message? | Shuts down the port? |
|---|---|---|---|---|
| **Protect** | Yes | No | No | No |
| **Restrict** | Yes | Yes | Yes | No |
| **Shutdown** (default) | Yes | Yes | Yes | **Yes (err-disabled state)** |

- **Shutdown** mode puts the port into **err-disable state** — the port goes completely down, affecting even the legitimate device, until an administrator manually recovers it (`shutdown` / `no shutdown`).
- **Restrict** mode drops unauthorized traffic and logs/counts the violation, but keeps the port physically up (`Secure-up`), so the legitimate device on that port is unaffected.

### Port Security Aging
- **Absolute**: secure MAC addresses are deleted exactly after the configured time, regardless of activity.
- **Inactivity**: secure MAC addresses are deleted only if there is no traffic for the configured time period.

### Verification commands
```
show port-security
show port-security interface f0/2
show port-security address
show mac address-table
```

Key fields to check: `Violation Mode`, `Maximum MAC Addresses`, `Sticky MAC Addresses`, `Last Source Address:Vlan`, `Security Violation Count`.

### Lab Result Example
In the "Implement Port Security" lab:
- Fa0/1 and Fa0/2 were configured with sticky learning, max 1 MAC address, and violation mode `restrict`.
- A **Rogue Laptop** connected to Fa0/2 (originally learned as PC2's MAC address) could **not** ping PC1, because its MAC address did not match the sticky-learned entry.
- `show port-security interface f0/2` showed **Security Violation Count: 5** and the Rogue Laptop's real MAC address under `Last Source Address`.
- Meanwhile, PC2 (the original device) continued to work normally, since the port stayed up under restrict mode.

---

## 7. Mitigate DHCP Attacks

### Types
- **DHCP Starvation**: attacker floods the DHCP server with bogus DHCP requests to exhaust the pool of available IP addresses.
- **DHCP Spoofing**: attacker sets up a rogue DHCP server to hand out malicious configuration (e.g., pointing clients to a rogue default gateway or DNS server) — enabling further MITM attacks.

### Mitigation: DHCP Snooping
DHCP Snooping distinguishes **trusted** ports (where legitimate DHCP servers are connected, e.g. uplinks to the real server) from **untrusted** ports (all others, typically client-facing access ports).

```
ip dhcp snooping
interface <trusted-port>
 ip dhcp snooping trust
interface <untrusted-port>
 ip dhcp snooping limit rate <rate>
ip dhcp snooping vlan <vlan-id or range>
```

| Step | Command | Purpose |
|---|---|---|
| 1 | `ip dhcp snooping` | Globally enables DHCP snooping |
| 2 | `ip dhcp snooping trust` | Marks a port as trusted (legitimate DHCP server) |
| 3 | `ip dhcp snooping limit rate` | Rate-limits DHCP discovery messages on untrusted ports (mitigates starvation) |
| 4 | `ip dhcp snooping vlan` | Applies snooping to a specific VLAN or VLAN range |

DHCP Snooping also builds a **binding table** (IP-to-MAC mapping) that is later used by DAI and IP Source Guard.

---

## 8. Defense Pyramid (Cisco-recommended mitigation stack)

From foundational (bottom) to more advanced (top):

```
        IPSG (IP Source Guard)
             ↑
   DAI (Dynamic ARP Inspection)
             ↑
        DHCP Snooping
             ↑
        Port Security
```

| Technique | Mitigates |
|---|---|
| **Port Security** | MAC table overflow attacks, DHCP starvation |
| **DHCP Snooping** | DHCP starvation, rogue DHCP server (spoofing) attacks |
| **DAI (Dynamic ARP Inspection)** | ARP spoofing, ARP poisoning |
| **IPSG (IP Source Guard)** | MAC and IP address spoofing |

Note: Port Security is the easiest to enable but, according to Cisco recommendations, one of the hardest to properly implement across a real environment.

### General hardening principles
1. Use secure protocol variants instead of plaintext ones: **SSH** instead of Telnet, **HTTPS** instead of HTTP, **SCP/SFTP** instead of FTP.
2. Consider **Out-of-Band (OOB) management** — manage devices through a physically/logically separate path (e.g., console cable) so management access survives even if the in-band network is compromised or congested.
3. Use a **dedicated management VLAN** that carries only management traffic.
4. Use **ACLs** to filter unwanted access to management interfaces.

---

## 9. Spanning Tree Protocol (STP) — Introduction

*(Covered briefly; more detail to be added in the next session.)*

- Redundant switch links improve resilience but can create Layer 2 **loops**, causing broadcast storms and duplicate frame delivery.
- **STP** automatically detects loops and places redundant links into a **blocking** state, keeping only one active path between any two switches while keeping the backup path ready in case the primary fails.
- STP attacks (to be covered) involve manipulating STP messages (BPDUs) to trick the network into electing the attacker's switch as the **Root Bridge**, giving them a privileged position to intercept traffic.

---

## 10. Static vs. DHCP IP Assignment

- **DHCP** is used for most general-purpose end devices (workstations, laptops) — automating IP assignment at scale (imagine manually configuring 500 terminals).
- **Static IP addressing** is reserved for devices that act as **network reference points** and must always be reachable at a consistent address:
  - Router interfaces
  - VLAN management interfaces (SVI - Switch Virtual Interface)
  - Servers, printers, and other infrastructure devices

---

## Key Takeaways
- Layer 2 security is foundational — if it fails, all higher-layer security controls (firewalls, VPNs, IPS) can be bypassed.
- Switches learn and forward based purely on MAC addresses, which is both their strength (efficiency) and their weakness (exploitable via flooding/spoofing).
- Defense works best as layered controls: Port Security → DHCP Snooping → DAI → IP Source Guard, each building on the trust established by the layer below it.
- Practical mitigation is a mix of switch-level configuration (Port Security, DHCP Snooping) and broader hardening practices (secure protocols, OOB management, dedicated VLANs, unused port shutdown).
