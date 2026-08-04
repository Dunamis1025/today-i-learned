# Lab: Design and Implement a VLSM Addressing Scheme

Cisco Networking Academy (CCNA) lab — VLSM subnetting design and router configuration, completed in Cisco Packet Tracer (Physical Mode).

## Overview

**Base network:** `192.168.33.128/25`

**Topology:**
```
S1 --F0/5---G0/0/1--> BR1 --G0/0/0---G0/0/0--> BR2 --G0/0/1---F0/5--> S2
```

**Host requirements:**

| Subnet Description | Hosts Needed |
|---|---|
| BR1 LAN | 40 |
| BR2 LAN | 25 |
| BR2 IoT LAN (future) | 5 |
| BR2 CCTV LAN (future) | 4 |
| BR2 HVAC C2LAN (future) | 4 |
| BR1-BR2 Link | 2 |

The goal of VLSM (Variable Length Subnet Mask) is to subnet a single address block into differently-sized subnets — largest requirement first — to minimize wasted address space, unlike FLSM where every subnet is forced to the same size.

## Part 1 & 2 — VLSM Subnet Design

Subnets were allocated from largest to smallest, each carved out of the remaining address space in order.

| Subnet Description | Hosts Needed | Network Address / CIDR | First Host Address | Broadcast Address |
|---|---|---|---|---|
| BR1 LAN | 40 | 192.168.33.128/26 | 192.168.33.129 | 192.168.33.191 |
| BR2 LAN | 25 | 192.168.33.192/27 | 192.168.33.193 | 192.168.33.223 |
| BR2 IoT LAN | 5 | 192.168.33.224/29 | 192.168.33.225 | 192.168.33.231 |
| BR2 CCTV LAN | 4 | 192.168.33.232/29 | 192.168.33.233 | 192.168.33.239 |
| BR2 HVAC C2LAN | 4 | 192.168.33.240/29 | 192.168.33.241 | 192.168.33.247 |
| BR1-BR2 Link | 2 | 192.168.33.248/30 | 192.168.33.249 | 192.168.33.251 |

Verified: each subnet's broadcast address is immediately followed by the next subnet's network address, with zero wasted addresses across the full /25 block.

### Interface Address Table

The first host address in each LAN subnet is assigned to the router's Ethernet interface. BR1 is assigned the first host address on the BR1-BR2 link.

| Device | Interface | IP Address | Subnet Mask | Description |
|---|---|---|---|---|
| BR1 | G0/0/0 | 192.168.33.249 | 255.255.255.252 (/30) | BR1-BR2 Link |
| BR1 | G0/0/1 | 192.168.33.129 | 255.255.255.192 (/26) | 40 Host LAN |
| BR2 | G0/0/0 | 192.168.33.250 | 255.255.255.252 (/30) | BR1-BR2 Link |
| BR2 | G0/0/1 | 192.168.33.193 | 255.255.255.224 (/27) | 25 Host LAN |

## Part 3 — Cabling and Configuration (Physical Mode)

### Physical Setup

1. Dragged S1, BR1, BR2, S2 from the shelf into the rack.
2. Connected S1–BR1, BR1–BR2, and BR2–S2 with Copper Straight-Through cables (Gigabit interfaces support Auto-MDIX, so Straight-Through works between routers as well as router-to-switch). Packet Tracer's "Automatic" cable tool is the safest option when unsure which cable type to use.
3. Confirmed all links showed green connection dots (link up).
4. Connected PC1 to BR1's console port and PC2 to BR2's console port using blue Console (rollover) cables, so each router could be configured independently via its own PC terminal.
5. Powered on both routers — router configuration was inaccessible via CLI until this was done.

### Accessing the CLI (Console, not Command Prompt)

- On each PC: **Desktop → Terminal** (not Command Prompt) opens a console session to the attached router.
- Default terminal port settings (9600 bps, 8 data bits, no parity, 1 stop bit, no flow control) are correct out of the box — no changes needed.
- On first boot, IOS asks: `Would you like to enter the initial configuration dialog? [yes/no]` → answered **no** to configure manually via CLI instead of the setup wizard.

### IOS Mode Hierarchy (key troubleshooting lesson)

| Prompt | Mode | Entered via | Notes |
|---|---|---|---|
| `Router>` | User EXEC | (default after login) | View-only |
| `Router#` | Privileged EXEC | `enable` | System-level commands |
| `Router(config)#` | Global Configuration | `configure terminal` (from `#`) | hostname, interfaces, etc. |
| `Router(config-if)#` | Interface Configuration | `interface g0/0/0` (from `(config)#`) | IP address, no shutdown, etc. |

Common errors encountered and resolved:
- `interface g0/0/0` typed as `interface 0/0/0` (missing `g`) → `% Invalid input detected`.
- `interface`/`configure terminal` attempted from the wrong mode (e.g., from `Router>` or after already exiting back to `#`) → `% Invalid input detected`. Fixed by re-entering `configure terminal` first.

### Configuration Commands Applied (BR1 and BR2)

```
enable
configure terminal
hostname BR1                     ! (or BR2)
no ip domain-lookup
enable secret class
line console 0
 password cisco
 login
exit
line vty 0 4
 password cisco
 login
exit
service password-encryption
banner motd #Unauthorized access is strictly prohibited#

interface g0/0/0
 description Link to BR2         ! (or "Link to BR1" on BR2)
 ip address <link-ip> 255.255.255.252
 no shutdown
exit

interface g0/0/1
 description <LAN description>
 ip address <lan-ip> <lan-mask>
 no shutdown
exit

end
copy running-config startup-config
```

### Command Explanations

| Command | Purpose |
|---|---|
| `no ip domain-lookup` | Prevents the router from trying to DNS-resolve mistyped commands as hostnames (avoids long hangs on typos). |
| `enable secret class` | Sets the (strongly encrypted) password required to enter Privileged EXEC mode via `enable`. |
| `line console 0` | Configuration mode for the physical console port — the connection used to access the CLI in this lab. `password cisco` + `login` requires a password (`cisco`) at first console login, *before* reaching the `Router>` prompt. |
| `line vty 0 4` | Configuration mode for the 5 virtual terminal lines (0–4) used for remote Telnet/SSH access. Same password logic as console, but for remote connections. |
| `service password-encryption` | Encrypts plaintext passwords stored in the config (e.g., console/vty passwords). `enable secret` is already strongly hashed regardless. |
| `banner motd #...#` | Sets a "Message of the Day" banner shown to anyone connecting to the device. **MOTD = Message Of The Day.** |
| `copy running-config startup-config` | Saves the active (RAM-only) running configuration to NVRAM (`startup-config`), so it persists across reboots. Functionally identical to the legacy `write memory` (`wr`) command — `copy run start` is the modern, standardized form Cisco documentation/curricula now favor, since the `copy` verb generalizes to other destinations (e.g., TFTP) whereas `write` does not. |

### Connectivity Test

Ping tests performed from within each router's CLI (not from the PC's Command Prompt — the PCs are only console-connected, not network-connected, so pinging from PC Command Prompt fails with 100% loss).

- **BR2 → BR1** (`ping 192.168.33.249`): 80% success (4/5). First packet timed out due to the initial ARP resolution delay (normal behavior); Correctional.
- **BR1 → BR2** (`ping 192.168.33.250`): 100% success (5/5).

Both results confirm the BR1–BR2 link is correctly configured and operational.

> **Note:** Pings to the GigabitEthernet LAN interfaces on the *other* router are expected to fail at this stage — no routing protocol has been configured yet, so neither router has a route to the other's LAN subnet. This is outside the scope of this lab, which focuses on VLSM design and interface configuration only.

## Reflection Question

**Q: Can you think of a shortcut for calculating the network addresses of consecutive /30 subnets?**

A: A `/30` mask (255.255.255.252) yields a block size of 4 addresses (256 − 252 = 4). Therefore consecutive `/30` network addresses always increment by 4 in the last octet (e.g., `.248`, `.252`, `.256→` rolls to the next octet, etc.). Once the first `/30` network address is known, subsequent ones can be listed by simply adding 4 repeatedly, without recalculating the subnet mask each time.

## Summary of Completed Work

- [x] Determined host/subnet requirements from the topology
- [x] Designed the full VLSM addressing scheme (largest-to-smallest allocation)
- [x] Verified no wasted address space across the six subnets
- [x] Completed the device interface address table
- [x] Physically racked and cabled S1, BR1, BR2, S2 in Packet Tracer Physical Mode
- [x] Console-connected PC1 → BR1 and PC2 → BR2
- [x] Configured hostname, passwords, banner, and encryption on both routers
- [x] Assigned and activated (`no shutdown`) all router interfaces with calculated IPs
- [x] Saved configurations to NVRAM on both routers
- [x] Verified bidirectional connectivity across the BR1–BR2 link
- [x] Answered the reflection question on consecutive /30 subnet shortcuts
