# CCNA Study Notes — Router/Switch Basics, Subnetting, and Packet Tracer Labs

## 1. Cisco Router & Switch Hardware Overview

Classroom lab equipment varies, but the NetAcad curriculum centers on the **Cisco 4000 Series routers** and **Cisco 2960 Series switches**.

Key hardware concepts:
- **Integrated ports**: Built-in ports on the router (e.g., Gigabit Ethernet 0/0/0, 0/0/1) that don't require add-on hardware.
- **Expansion slots**: Routers support modular expansion cards to add more connection types.
  - **NIM** (Network Interface Module) slots — used for serial cable connections.
  - **WIC / EHWIC** (Enhanced High-Speed WAN Interface Card) slots — also used for serial WAN connections, found on 1900/2900 series routers.
- **SFP (Small Form-Factor Pluggable)**: A module slot that accepts fiber transceivers for fiber-optic connections.
- **Shared ports**: Some Gigabit Ethernet ports share a single logical interface with an SFP slot — only one (copper or fiber) can be active at a time.

Different router models (4000, 2900, 1900 series) vary in port count and expansion slot type, but the same core concepts apply across all of them.

---

## 2. Subnetting Fundamentals

### Why Subnetting Works: Binary ANDing
A device determines its network address by converting its **IP address** and **subnet mask** to binary and performing a logical **AND** operation.
- Rule: `1 AND 1 = 1`, everything else = `0`.
- Example: `192.168.1.10` ANDed with `255.255.255.0` → network address `192.168.1.0`.

### Classless Subnetting
Beyond the standard classful masks (`/8`, `/16`, `/24`), subnet masks can be any length (e.g., `/25`, `/18`, `/12`) by **borrowing bits** from the host portion of the address, moving left to right.

### Worked Example: Borrowing 1 Bit
Starting network: `192.168.1.0/24`

Borrow 1 bit from the host portion → new mask `/25` (`255.255.255.128`):
- **Subnet bits**: 1 → creates 2^1 = **2 subnetworks**
- **Host bits**: 7 remaining → 2^7 = 128 addresses per subnet, minus 2 (network + broadcast) = **126 usable hosts per subnet**

Resulting subnets:
| Subnet | Range | Network Address | Broadcast Address |
|---|---|---|---|
| Subnet 1 | .0 – .127 | 192.168.1.0 | 192.168.1.127 |
| Subnet 2 | .128 – .255 | 192.168.1.128 | 192.168.1.255 |

**Verification via ANDing:**
- Host `192.168.1.68` AND `/25` mask → network `192.168.1.0` (falls in Subnet 1)
- Host `192.168.1.138` AND `/25` mask → network `192.168.1.128` (falls in Subnet 2)

### Key Rule
- The **first address** in any subnet = the **network address** (identifies the subnet, not assignable to a host).
- The **last address** in any subnet = the **broadcast address** (used to send to all hosts on that subnet, not assignable to a host).

---

## 3. Default Gateway Concept

A device needs three things to communicate across networks: an **IP address**, a **subnet mask**, and a **default gateway**.

- The default gateway is the **IP address of the router interface attached to the local network** — it's the "exit door" a device uses to reach any network other than its own.
- If a device's gateway is missing, wrong, or on the wrong subnet, it can talk to devices on its own local network but **not** to anything beyond it.

---

## 4. Packet Tracer Lab: Troubleshoot Default Gateway Issues

**Goal**: Practice a structured troubleshooting method — verify documentation, isolate problems, test, implement fixes, re-verify, and document.

**Troubleshooting method**:
1. Verify documentation and test to isolate problems.
2. Determine a solution.
3. Implement the solution.
4. Re-test to confirm the fix worked.
5. Document the outcome.

**Workflow**:
- Complete the addressing table (fill in missing default gateways for switches/PCs).
- Test **local connectivity first** (same subnet) before testing **remote connectivity** (across the router) — local issues must be resolved first, or remote tests are meaningless.
- Fix one issue at a time and re-verify before moving to the next, to avoid masking additional problems.

**Common issue types found in this type of lab**: wrong IP address on a host, wrong/missing default gateway, gateway typo (e.g., missing an octet).

---

## 5. Packet Tracer Lab: Build a Switch and Router Network (Physical Mode)

**Goal**: End-to-end review lab — physically cable a topology, configure it from scratch, and verify both IPv4 and IPv6 connectivity.

### Part 1 — Set Up the Topology
- Move router, switch, and PCs from the **Shelf** to the **Rack/Table**.
- Cable devices according to the addressing table.
- Power everything on.

### Part 2 — Configure Devices
**On PCs**: assign static IPv4 address, subnet mask, and default gateway (plus IPv6 where applicable).

**On the router**:
- Set hostname.
- `enable secret` — encrypted privileged EXEC password.
- Console and VTY (remote) line passwords, with `login` enabled.
- `service password-encryption` — encrypts all plaintext passwords in the config.
- `banner motd` — warning banner shown at login.
- Configure and activate (`no shutdown`) both interfaces with IPv4 and IPv6 addresses.
- Add interface `description` for documentation.
- `ipv6 unicast-routing` — enables the router to actually route IPv6 traffic.
- Save config: `copy running-config startup-config`.
- Set the clock.

**On the switch**:
- Hostname, VLAN 1 interface IP (activated with `no shutdown`), default gateway, save config.

### Part 3 — Verify Connectivity & Display Info
- Ping between all devices (PC ↔ PC, PC ↔ router, switch ↔ router) for both IPv4 and IPv6.
- `show ip route` / `show ipv6 route` — view the routing table. Directly connected networks show a `C` code.
- `show interface <int>` — detailed interface status, MAC address, IP info.
- `show ip interface brief` / `show ipv6 interface brief` — quick summary of all interfaces and their up/down status.

---

## 6. Router Startup & Security — Q&A Reference

**Q: Why does a router boot into setup mode?**
A: Because there's no configuration file in NVRAM — the router auto-launches setup mode to help build a basic config from scratch.

**Q: Command to encrypt all passwords in the router config?**
A: `service password-encryption` — encrypts any plaintext passwords immediately upon entry.

**Q: Most secure way to protect privileged EXEC access with password `trustknow1`?**
A: `enable secret trustknow1` — uses strong hashing, unlike `enable password` which is weak/plaintext.

**Q: Result of `hostname portsmouth` on a router?**
A: The prompt immediately updates to `portsmouth(config)#`.

**Q: Commands to require a login with password `cisco` for out-of-band (console) access?**
A:
```
Router(config)# line console 0
Router(config-line)# password cisco
Router(config-line)# login
```
Out-of-band management means managing the device via a direct console cable, separate from the network itself.

**Q: Command to see all interfaces, their IPv4 addresses, and status at a glance?**
A: `show ip interface brief`

**Q: Which CLI mode grants access to all device commands (config, management, troubleshooting)?**
A: **Privileged EXEC mode**

**Q: Purpose of the startup configuration file?**
A: Holds the commands the router loads and applies automatically every time it boots.

**Q: What characterizes a host's default gateway?**
A: The IP address of the router interface on the *same network* as the host — the exit point to other networks.

**Q: Purpose of `banner motd`?**
A: Displays a message (e.g., legal warning) to anyone logging into the device.

**Q: Which configuration mode do you need to be in to use the `login` command?**
A: Any **line configuration mode** (console, VTY, or AUX line).

**Q: What is stored in a Cisco router's NVRAM?**
A: The **startup configuration** — NVRAM is non-volatile, so it retains this file even when powered off.

**Q: True statement about `service password-encryption`?**
A: As soon as it's entered, all currently configured plaintext passwords are immediately encrypted.

---

## 7. Personal Lab Session Notes (Hands-On Practice Log)

### Lab A — Troubleshoot Default Gateway Issues
Topology: R1 (two subnets: 192.168.10.0/24 and 192.168.11.0/24), S1, S2, PC1–PC4.

**Issues found and fixed:**
| Device | Problem | Fix |
|---|---|---|
| PC1 | IP address was `192.168.11.10` (wrong subnet) | Corrected to `192.168.10.10` |
| PC4 | Default gateway was `192.168.1.1` (typo, missing an octet) | Corrected to `192.168.11.1` |
| S1, S2 | VLAN 1 IP/gateway not configured (Config tab locked — required CLI) | Configured via CLI: `interface vlan 1` → `ip address` → `no shutdown` → `ip default-gateway` |

All local and remote pings succeeded afterward, including from the switches themselves.

### Lab B — Basic Device Configuration (Floor14 / Room-145 / Room-146)
Topology: Router **Floor14** (2 interfaces, dual-stack IPv4/IPv6), Switch **Room-145** (inaccessible by design), Switch **Room-146** (to be configured), 4 PCs (Manager-A, Reception-A, Manager-B, Reception-B).

**Configuration performed:**
- Floor14: hostname, `enable secret class`, console/VTY passwords (`cisco`), `service password-encryption`, MOTD banner, both interfaces configured with IPv4 + IPv6 + descriptions, `ipv6 unicast-routing`, saved config.
- Room-146: hostname, same password/banner setup, VLAN 1 IPv4 address + `no shutdown`, `ip default-gateway`, interface descriptions, saved config.
- PCs: completed missing IPv4 gateways and IPv6 addresses/gateways per the addressing table.

**Issue found and fixed:**
- **Reception-B** had an incorrect IPv4 address (`10.10.10.102`), which duplicated Reception-A's address and put it on the wrong subnet relative to its own gateway. Corrected to `10.10.11.102`.

**Result:** All IPv4 and IPv6 pings succeeded between every device; Packet Tracer's Check Results reported **100% completion**.

---

*Compiled from CCNA NetAcad course material, Packet Tracer lab instructions, and hands-on lab session notes.*
