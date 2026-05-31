# Networking Fundamentals — Study Notes

> Based on Cisco CCNA / Networking Essentials coursework

---

## Table of Contents

1. [Network Terminology: Hosts, Servers, and Intermediary Devices](#1-network-terminology)
2. [Intermediary Devices: Switches and Routers](#2-intermediary-devices)
3. [Physical Connection: NIC, Port, and Interface](#3-physical-connection)
4. [Transmission Media](#4-transmission-media)
5. [Network Topologies](#5-network-topologies)
6. [Cisco CLI: Command Hierarchy Navigation](#6-cisco-cli-navigation)
7. [Cable Types and Auto-MDIX](#7-cable-types-and-auto-mdix)

---

## 1. Network Terminology

### Hosts

- **Definition:** All computers and end-user devices that are directly connected to a network and participate in network communication.
- Hosts are the **source and destination** of all data on a network.
- Examples: PCs, laptops, smartphones, tablets, printers.

### Servers

- A **specialized type of host** that provides services (web pages, files, email, etc.) to other hosts.
- A server is still a host — it's just a host with a specific service role.

### Intermediary Devices

- Devices that **do not originate or consume data** themselves; instead, they connect end devices and manage traffic flow.
- Examples: **Switches**, **Routers**, Access Points, Firewalls.

| Category | Role | Examples |
|---|---|---|
| **Hosts** | Source / Destination of data | PC, Laptop, Smartphone |
| **Servers** | Specialized host providing services | Web server, File server |
| **Intermediary Devices** | Connect networks and direct traffic | Switch, Router |

> **Analogy:** On a highway, hosts are the cars carrying passengers (data). Intermediary devices are the road signs and traffic lights that guide them to the right destination.

---

## 2. Intermediary Devices

### Switches

- Connect multiple end devices **within the same local network (LAN)**.
- Forward data to the correct device based on **MAC addresses**.
- Operate at **Layer 2 (Data Link Layer)** of the OSI model.

### Routers

- Connect **different networks** together (e.g., your home LAN to the internet).
- Determine the **best path** for data to travel between networks.
- Operate at **Layer 3 (Network Layer)** of the OSI model and use **IP addresses**.

> **Summary:**
> - Switch = connects devices within **one** network
> - Router = connects **multiple** networks together

---

## 3. Physical Connection: NIC, Port, and Interface

### NIC (Network Interface Card)

- The **physical hardware component** (a card) installed in or attached to a host device.
- Provides the actual connection to the network — either via cable or wirelessly.
- Previously commonly called a **"LAN card."**
- Without a NIC, a computer cannot communicate with any network.

### Port

- The **physical jack/hole** on a NIC or networking device where a cable is plugged in.
- It is a component **of** the NIC, not a separate device.

### Interface

- A **broader, higher-level concept** used primarily on networking devices (like routers and switches).
- Combines the physical port with its **network configuration** (e.g., IP address, subnet mask).
- Interfaces are the **specialized ports on a networking device** that connect to individual networks.

| Term | What it means | Used for |
|---|---|---|
| **NIC** | The physical hardware card | End devices (hosts) |
| **Port** | The physical plug-in hole | Any device |
| **Interface** | Configured connection point | Networking devices (routers, switches) |

---

## 4. Transmission Media

The medium used to transmit data depends on the **type of signal** being sent.

### Copper Cable (e.g., UTP)

- Transmits data as **electrical pulses**.
- Common example: the standard Ethernet LAN cable (RJ-45 / UTP).
- Suitable for short-to-medium distances.

### Fiber-Optic Cable

- Transmits data as **pulses of light** through thin strands of glass or plastic.
- Extremely **high speed** and capable of transmitting over **very long distances**.
- Not affected by electromagnetic interference.

### Wireless

- Transmits data through the **air using radio waves** (electromagnetic signals).
- No cables required.
- Examples: Wi-Fi, LTE, 5G.

| Signal Type | Medium |
|---|---|
| Electrical pulses | Copper cable |
| Light pulses | Fiber-optic cable |
| Radio waves | Wireless |

---

## 5. Network Topologies

A **network topology** is a map or diagram of a network. There are two main types.

### Physical Topology

- Shows the **actual, real-world layout** of a network.
- Displays:
  - Where each physical device (switch, router, PC) is **located**
  - Which **cables** are connected to which ports
  - What **type of media** (copper, fiber, wireless) is used
- Used by network engineers and technicians for **installation and troubleshooting**.

### Logical Topology

- Shows **how data flows** through the network, regardless of physical location.
- Displays:
  - **IP addressing** schemes and subnets
  - The **logical path** data takes from source to destination
- Used for **planning and understanding data flow**.

| Topology Type | What it shows | Use case |
|---|---|---|
| **Physical** | Actual devices, cables, and locations | Installation, wiring, cabling |
| **Logical** | Data flow paths and IP addressing | Network design and troubleshooting logic |

> **Analogy:** Think of a house.
> - **Physical topology** = the blueprint showing where the pipes and electrical wires are installed in the walls.
> - **Logical topology** = the schematic showing how water or electricity flows from the main supply to each outlet.

---

## 6. Cisco CLI: Command Hierarchy Navigation

When configuring Cisco network devices (routers and switches), the CLI (Command-Line Interface) is organized in **hierarchical modes** — similar to folders on a computer.

### Key Navigation Commands

| Command / Key | Action |
|---|---|
| `exit` | Moves back **one level** in the hierarchy |
| `end` or **Ctrl-Z** | Immediately exits **all configuration modes** and returns to **Privileged EXEC mode** |
| **Ctrl-C** | **Aborts/cancels** the current command or running process |

### Mode Hierarchy (Simplified)

```
User EXEC Mode  (>)
  └── Privileged EXEC Mode  (#)
        └── Global Configuration Mode  (config)
              └── Sub-configuration Modes  (config-if, config-line, etc.)
```

### When to use each command

- **`exit`** — Use when you want to go back **one step at a time**.
  - Example: From `config-if` → `config` → `#`
- **`Ctrl-Z` / `end`** — Use when you want to **immediately jump back to the top** (`#`) from any depth.
  - Like pressing "Home" on a file browser instead of clicking "Back" repeatedly.
- **`Ctrl-C`** — Use when you want to **cancel** what you're currently typing or a running process. Does **not** navigate between modes.

> **Quick tip:** If you're deep in sub-configuration mode and want to get back fast, press **Ctrl-Z**.

---

## 7. Cable Types and Auto-MDIX

### Straight-Through vs. Crossover Cables

| Cable Type | Traditional Use |
|---|---|
| **Straight-through** | Connect different device types (PC → Switch, Switch → Router) |
| **Crossover** | Connect same device types (Switch → Switch, PC → PC) |

### Auto-Negotiation

Modern switches automatically negotiate the **best possible connection settings** with each other:

- **Speed:** Devices agree on the **highest speed both support** (e.g., if both support 1 Gbps, the link runs at 1 Gbps).
- **Duplex:** Automatically set to **full-duplex**, meaning data can be **sent and received simultaneously**.

### Auto-MDIX

- A modern feature that **automatically detects the cable type** and adjusts the port accordingly.
- This means you can connect two switches with a **straight-through cable** and it will work — no crossover cable needed.
- On new, unconfigured modern switches: **no manual configuration is required**.

### Summary: Two new switches connected with a straight-through cable

| Result | Reason |
|---|---|
| Link runs at the fastest speed both support | Auto-negotiation |
| Link operates in full-duplex mode | Auto-negotiation |
| Straight-through cable works fine | Auto-MDIX |

---

## Quick Reference Cheat Sheet

| Concept | Key Point |
|---|---|
| **Host** | Any end device that sends/receives data (PC, phone) |
| **Server** | A type of host that provides services |
| **Switch** | Connects devices in the same LAN |
| **Router** | Connects different networks |
| **NIC** | Hardware that connects a host to the network |
| **Port** | Physical hole/jack on a device |
| **Interface** | Configured connection point on a network device |
| **Copper cable** | Uses electrical signals |
| **Fiber-optic** | Uses light pulses; long distance, high speed |
| **Wireless** | Uses radio waves |
| **Physical topology** | Shows real devices, cables, and locations |
| **Logical topology** | Shows data flow and IP addressing |
| **Ctrl-Z / end** | Return immediately to Privileged EXEC mode |
| **exit** | Go back one level in CLI hierarchy |
| **Auto-MDIX** | Allows any cable type between modern switches |
| **Auto-negotiation** | Devices agree on best speed and duplex automatically |

---

*Last updated: June 2026*
