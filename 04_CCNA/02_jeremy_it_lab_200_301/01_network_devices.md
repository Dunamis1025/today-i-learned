# Day 01 - Network Devices

> **Course:** Jeremy's IT Lab - Free CCNA 200-301 Complete Course
> **Topic:** Network fundamentals and the three core devices (switch, router, firewall)
> **Note:** Review material that overlaps with Cisco NetAcad ITN

---

## 1. What Is a Network?

- A **computer network** is a digital telecommunications system that lets multiple devices (**nodes**) **share resources** such as data, files, printers, and an internet connection.
- The purpose of a network: **communication and resource sharing** between devices.

### Key Terms

| Term | Meaning |
|------|---------|
| **Node** | Any device connected to a network (router, switch, firewall, server, client, etc.) |
| **End host / Endpoint** | A device that is the **source or destination** of traffic (PC, smartphone, server) |
| **Intermediary device** | A device that **forwards** traffic between end hosts (switch, router, firewall) |

> **Note:** "Node" is the broadest term. End hosts/endpoints are the subset of nodes that originate or receive traffic. Switches and routers are nodes, but they are not normally called end hosts.

---

## 2. Client and Server

### Definitions

- **Client**: a device that **requests and uses** services provided by a server.
- **Server**: a device that **provides functions or services** to clients.

### Examples

| Scenario | Client | Server |
|----------|--------|--------|
| Watching a YouTube video | My smartphone / PC | The server sending the video data |
| Receiving a video from a friend via AirDrop | My phone (receiving) | My friend's phone (sending) |

### Key Takeaways

- Client and server are **roles, not device types**.
- The same device can act as a **client in one situation and a server in another**.
- The only question that matters: **who is requesting, and who is providing?**

---

## 3. The Three Core Network Devices

### 1) Switch

**In one line:** connects devices **within the same LAN**.

- **LAN (Local Area Network)**: a network in a small area such as one office, one floor, or one home.
- Role: connects and forwards data between end hosts on the same LAN (PCs, printers, servers).
- Characteristics:
  - Has **many ports/interfaces** (typically 24 or more).
  - Used to tie together the devices on an office floor or in a home.
  - **Cannot connect separate LANs or send data to the internet.**

### 2) Router

**In one line:** connects **different networks (LANs)** to each other.

- Role: connects networks together and forwards data across the internet (WAN).
- Characteristics:
  - Has **fewer interfaces** than a switch.
  - Essential for communication between distant networks.
    - Example: **New York office LAN <-> Tokyo office LAN**
  - Also the gateway a LAN uses to reach the internet.

### 3) Firewall

**In one line:** **allows or blocks traffic** based on predefined security rules.

- Role: monitors traffic **entering and leaving** the network and **blocks** anything that violates the rules.
- Types:

| Type | Description |
|------|-------------|
| **Network-based firewall** | A **dedicated hardware device** at the network edge that protects the whole internal network from external attacks |
| **NGFW (Next-Generation Firewall)** | A traditional firewall **plus** advanced filtering such as **IPS (Intrusion Prevention System)** |
| **Host-based firewall** | **Software running on an individual PC or server**, adding a per-device layer of protection |

> Common exam distinction: **host-based = software on the device; network-based = dedicated appliance at the network edge.**

---

## 4. Device Comparison

| | Switch | Router | Firewall |
|---|--------|--------|----------|
| Core role | Connects devices in the **same LAN** | Connects **different LANs**, provides internet access | **Monitors and blocks** traffic |
| Scope | Inside a local network | Between networks | Network edge or an individual host |
| Port count | Many (24+) | Few | - |
| Cannot do | Connect LANs, reach the internet | - | - |
| Example | PCs on one office floor | New York <-> Tokyo | Blocking outside attacks, protecting a PC |

---

## 5. Example Topology

```
[PC1]--\                                    /--[PC3]
[PC2]----[Switch A]--[Router A]==Internet==[Router B]--[Switch B]----[PC4]
[Printer]-/          (New York LAN)                    (Tokyo LAN)
```

- Traffic **within** a LAN is handled by the **switch**.
- Traffic **leaving** a LAN is handled by the **router**.
- A **firewall** at the network edge blocks external threats, and each PC can also run a **host-based firewall**.

---

## 6. Review Questions

| Question | Answer |
|----------|--------|
| Which device connects 30 PCs together? | **Switch** |
| Which device connects two different networks (LANs)? | **Router** |
| What role does my phone play when streaming a video? | **Client** |
| Which has more ports, a switch or a router? | **Switch** |
| Which device cannot send data to the internet by itself? | **Switch** (a router is required) |
| Which firewall adds IPS and other advanced filtering? | **NGFW** |
| Which firewall runs on an individual PC? | **Host-based firewall** |

---

## 7. Summary

- **Switch** = connects devices inside a LAN
- **Router** = connects LANs to each other (and to the internet)
- **Firewall** = permits or denies traffic according to rules
- **Client / Server** = roles (requester vs. provider), not device types

---

## 8. Study Log

- [x] Watched the video
- [x] Reviewed Anki cards
- [ ] Packet Tracer lab (none for this day)

### Notes / Confusing Points

- (add your own notes here)
