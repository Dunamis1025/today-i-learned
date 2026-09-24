# Networking Fundamentals – Study Notes

---

## 1. Routing – Path Determination in Networks

**Question:** Which device determines the path that messages take through internetworks?

**Answer:** **Router**

### Key Concepts
- The internet functions like a massive road map with thousands of interconnected paths.
- A **router** reads this map and directs data along the most efficient route to its destination.
- It operates by examining destination addresses and consulting routing tables to forward packets hop-by-hop.

### Why the Other Options Are Wrong
| Device | Role |
|---|---|
| **Firewall** | Security guard — blocks unauthorized access |
| **Web Server** | Warehouse — stores and serves website content |
| **DSL Modem** | Bridge — connects your home network to the ISP |

---

## 2. Cisco IOS – Command Mode Hierarchy

**Question:** An admin tries to configure a switch but gets an error. What is the problem?

**Answer:** The administrator must **first enter Privileged EXEC Mode** before issuing configuration commands.

### Mode Hierarchy
```
Switch>          ← User EXEC Mode       (read-only, very limited)
Switch#          ← Privileged EXEC Mode (enter with: enable)
Switch(config)#  ← Global Config Mode   (enter with: configure terminal / conf t)
```

### Rule
You **cannot** jump from User EXEC Mode (`>`) directly to Global Config Mode. You must step through each level.

```bash
Switch> enable
Switch# configure terminal
Switch(config)# ...
```

---

## 3. Finding the SVI IP Address on a Cisco Switch

**Question:** How do you find the IP address of Switch0's SVI (Switch Virtual Interface)?

**Answer:** Use `show running-config` and look for `interface Vlan1`.

### Steps
```bash
# Step 1: Enter Privileged EXEC Mode
Switch> enable

# Step 2: Display running configuration
Switch# show running-config
```

### What to Look For
```
interface Vlan1
 ip address 192.168.x.x 255.255.255.0
 no shutdown
```

> **What is an SVI?**  
> Switches forward traffic but don't natively have IP addresses. An SVI (Switch Virtual Interface) is a virtual interface assigned an IP address so that administrators can manage the switch remotely. It is typically configured on **VLAN 1**.

---

## 4. Network Types – SOHO Network

**Question:** What term describes a network used by people working from home or a small remote office?

**Answer:** **SOHO Network**

### Acronym Breakdown
| Letters | Meaning |
|---|---|
| **SO** | Small Office |
| **HO** | Home Office |

A SOHO network is a small-scale setup (e.g., home router connecting a PC, printer, and smartphone) typical of home-based workers or micro-businesses.

### Why the Other Options Are Wrong
| Term | Meaning |
|---|---|
| **Converged Network** | Carries voice, video, and data over a single infrastructure |
| **BYOD** | Policy allowing employees to use personal devices for work |
| **QoS (Quality of Service)** | Technology that prioritizes traffic to guarantee performance |

---

## 5. OSI Model – Encapsulation and PDU Data Addition

**Question:** At which OSI layer is data added to a PDU during the encapsulation process?

**Answer:** **Application Layer** (Layer 7)

### Encapsulation Analogy
Think of it like shipping a package:
- The **item inside** = the actual data (created at the Application Layer)
- Each layer below **wraps the package** by adding a header

### PDU by Layer
| OSI Layer | PDU Name | What Gets Added |
|---|---|---|
| **Application** | Data | **Original data is created here** |
| Transport | Segment | Source/destination port numbers |
| Network | Packet | Source/destination IP addresses |
| Data Link | Frame | MAC addresses |
| Physical | Bits | Binary signal |

> **Key Insight:** Lower layers (Transport, Network, etc.) do **not** create the data — they only add headers to wrap the data that already exists from the Application Layer.

---

## Summary Table

| Topic | Key Answer | Command / Note |
|---|---|---|
| Path determination device | Router | — |
| Cisco config error cause | Wrong mode (User EXEC) | Use `enable` first |
| Find SVI IP address | `show running-config` | Look for `interface Vlan1` |
| Home/small office network | SOHO Network | Small Office / Home Office |
| Where data is added in PDU | Application Layer | Top of the OSI model |
