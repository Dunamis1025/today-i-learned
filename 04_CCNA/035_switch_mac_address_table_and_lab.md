# Network Switching & MAC Address Table - Study Notes

## Overview

This document summarizes the concepts and hands-on lab work completed in **Cisco Networking Academy - Chapter 7**, focusing on how Layer 2 switches forward Ethernet frames using MAC address tables.

---

## 1. How a Switch Forwards Frames

### Core Concept
A Layer 2 switch delivers Ethernet frames to host devices based on **MAC addresses**, not IP addresses. The switch maintains a **MAC Address Table** (also called CAM table) that maps MAC addresses to physical ports.

### Frame Forwarding Logic

| Situation | Switch Action |
|---|---|
| Destination MAC **found** in table | Forward frame to that specific port only (**Unicast**) |
| Destination MAC **not found** in table | Flood frame out **all ports** except the incoming port |
| Source MAC **not found** in table | **Add** source MAC + port to the table |
| Source MAC **already in** table | Refresh the **5-minute timer** |

### MAC Address Table Entry Lifecycle
1. Switch receives a frame
2. Checks **source MAC** → adds to table if unknown, refreshes timer if known
3. Checks **destination MAC** → forwards or floods accordingly
4. Entries expire after **5 minutes** of inactivity

---

## 2. Unicast vs Flooding

### Unicast (Known Destination)
- Destination MAC exists in the MAC table
- Frame is sent to **one specific port only**
- Efficient — other devices never see the frame

### Flooding (Unknown Destination)
- Destination MAC does **not** exist in the MAC table
- Frame is sent to **all ports except the incoming port**
- Other devices receive the frame but drop it if the destination MAC doesn't match their own

---

## 3. Packet Forwarding Scenario (Internet-bound Packet)

### PC-A → Internet (via Router)

```
PC-A → S1 → S2 → Router → Internet
```

**Outbound Frame:**
- Source MAC: PC-A
- Destination MAC: Router (00-0D)

| Step | Device | Action |
|---|---|---|
| 1 | S1 | Source MAC already in table → refresh timer. Destination MAC unknown → **flood all ports** |
| 2 | PC-B | Destination MAC doesn't match → **drop frame** |
| 3 | S2 | Source MAC already in table → refresh timer. Destination MAC unknown → **flood all ports** |
| 4 | PC-C | Destination MAC doesn't match → **drop frame** |
| 5 | Router | Destination MAC matches → **accept frame** |

**Return Frame (Router → PC-A):**
- Source MAC: Router (00-0D)
- Destination MAC: PC-A

| Step | Device | Action |
|---|---|---|
| 1 | S2 | Source MAC (Router) not in table → **add it**. Destination MAC (PC-A) found → **forward to port** |
| 2 | S1 | Source MAC (Router) not in table → **add it**. Destination MAC (PC-A) found → **forward out Port 1** |
| 3 | PC-A | Destination MAC matches → **accept frame** |

---

## 4. Lab 7.3.7 - View the Switch MAC Address Table

### Network Topology

```
PC-A ---[Fa0/6]--- S1 ---[Fa0/1]---[Fa0/1]--- S2 ---[Fa0/18]--- PC-B
```

### Addressing Table

| Device | Interface | IP Address | Subnet Mask |
|---|---|---|---|
| S1 | VLAN 1 | 192.168.1.11 | 255.255.255.0 |
| S2 | VLAN 1 | 192.168.1.12 | 255.255.255.0 |
| PC-A | NIC | 192.168.1.1 | 255.255.255.0 |
| PC-B | NIC | 192.168.1.2 | 255.255.255.0 |

### Device MAC Addresses (recorded during lab)

| Device | MAC Address |
|---|---|
| PC-A | 0001.4315.0741 |
| PC-B | 00D0.97AA.61DC |
| S1 F0/1 (bia) | 0001.c966.7301 |
| S2 F0/1 (bia) | 00d0.ba4b.3801 |

---

## 5. Key Commands Used

### On PC (Command Prompt)
```bash
ipconfig /all           # Show NIC MAC address and IP configuration
arp -a                  # Show ARP cache (IP ↔ MAC mappings learned by PC)
ping <ip-address>       # Test connectivity to a device
```

### On Switch (Cisco IOS CLI)
```bash
enable                              # Enter privileged EXEC mode
configure terminal                  # Enter global configuration mode
hostname S1                         # Set switch hostname

interface vlan 1                    # Enter VLAN 1 management interface
ip address 192.168.1.11 255.255.255.0  # Assign IP to switch
no shutdown                         # Activate the interface

show interface F0/1                 # View interface details including bia MAC address
show mac address-table              # View the MAC address table
clear mac address-table dynamic     # Clear all dynamically learned MAC entries
```

---

## 6. Lab Results & Observations

### Before ping (S2 MAC Table)
```
Vlan    Mac Address       Type      Ports
----    -----------       ----      -----
1       0001.c966.7301   DYNAMIC   Fa0/1
```
Only S1's MAC was known — no communication had occurred yet.

### After ping from PC-B to all devices (S2 MAC Table)
```
Vlan    Mac Address       Type      Ports
----    -----------       ----      -----
1       0001.4315.0741   DYNAMIC   Fa0/1
1       0001.c966.7301   DYNAMIC   Fa0/1
1       0060.2fa1.13c8   DYNAMIC   Fa0/1
1       00d0.97aa.61dc   DYNAMIC   Fa0/18
```

**Key observations:**
- PC-A and S1 both appear on **Fa0/1** because PC-A is behind S1 from S2's perspective
- PC-B appears on **Fa0/18** — its direct connection port
- The switch learned all MAC addresses **automatically** through communication

### PC-B ARP Cache (after ping)
```
Internet Address    Physical Address    Type
192.168.1.1         0001.4315.0741     dynamic   ← PC-A
192.168.1.11        0060.2fa1.13c8     dynamic   ← S1
192.168.1.12        00e0.f972.adde     dynamic   ← S2
```
Before ping: `No ARP Entries Found`
After ping: All 3 devices mapped automatically

---

## 7. Concept Comparison

### Switch MAC Table vs PC ARP Cache

| | Switch MAC Table | PC ARP Cache |
|---|---|---|
| **Stores** | MAC ↔ Port | IP ↔ MAC |
| **Purpose** | Know which port to send a frame out | Know which MAC to use for a given IP |
| **Populated by** | Inspecting source MAC of incoming frames | ARP request/reply process |
| **Command to view** | `show mac address-table` | `arp -a` |
| **Cleared by** | `clear mac address-table dynamic` | `arp -d` |

### Both PC and Switch Learn Dynamically
- Neither needs manual configuration for basic communication
- Both tables are built **automatically** as network traffic flows
- This is why the first ping sometimes has 1 packet loss — the devices are still learning

---

## 8. Why `interface vlan 1` for Switch IP?

Switches are Layer 2 devices and don't inherently have IP addresses. To assign a management IP:
- `interface vlan 1` creates a **virtual management interface (SVI)**
- This allows network admins to remotely manage the switch via SSH/Telnet
- Without this, you can only manage the switch via direct console cable

```
Switch(config)# interface vlan 1
Switch(config-if)# ip address 192.168.1.11 255.255.255.0
Switch(config-if)# no shutdown
```

---

## 9. Reflection — Challenges on Larger Networks

On small networks (2–4 devices), MAC learning is fast and simple. On larger networks:

- **MAC table overflow**: Switches have limited table size. An attacker can flood fake MACs to fill the table, causing the switch to flood all traffic (**MAC flooding attack**)
- **Broadcast storms**: Excessive flooding can degrade network performance significantly
- **Security concerns**: Flooded frames are visible to all devices on the segment
- **Scalability**: These issues are why **VLANs**, **routing**, and **network segmentation** are essential in enterprise networks

---

## 10. Summary

```
Communication Flow:
─────────────────────────────────────────────────────
1. PC wants to send data → checks ARP cache for MAC
2. If MAC unknown → sends ARP broadcast to find it
3. Frame arrives at switch → switch checks MAC table
4. If destination MAC known → forward to specific port
5. If destination MAC unknown → flood all ports
6. Switch learns source MAC automatically on every frame
─────────────────────────────────────────────────────
```

> **Core Takeaway**: Switches make networks efficient by learning which device is on which port, so traffic is only sent where it needs to go — not everywhere.
