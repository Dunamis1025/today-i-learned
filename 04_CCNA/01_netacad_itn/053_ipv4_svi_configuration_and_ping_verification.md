# Networking Study Notes

## 1. IPv4 Address Structure

### What is it called?
The structure of an IPv4 address is called **Dotted-Decimal Format**.

### How does it work?
- An IPv4 address consists of **32 bits**, divided into **four groups of 8 bits (octets)**.
- Each octet is converted into a **decimal number ranging from 0 to 255**.
- The four numbers are separated by **periods (dots)**.

### Example
```
192.168.1.1
 ↑   ↑  ↑ ↑
 |   |  | └── 4th octet (8 bits → decimal)
 |   |  └──── 3rd octet
 |   └──────── 2nd octet
 └──────────── 1st octet
```

> **Key takeaway:** IPv4 = four decimal numbers (0–255) separated by periods.

---

## 2. Switch Virtual Interface (SVI)

### What is an SVI?
A **Switch Virtual Interface (SVI)** is a logical (software-based) interface on a network switch that has **no physical port** associated with it.

| Type | Description | Example |
|---|---|---|
| Physical Interface | Requires a physical cable | Ethernet port, Serial port |
| Virtual Interface (SVI) | Software-only, no physical port | Interface VLAN1 |

### Why is it needed?
Switches connect multiple computers, but to **remotely manage** a switch, the switch itself needs an IP address. The SVI (typically **Interface VLAN1**) serves as that management gateway.

---

## 3. Configuring the SVI — Lab Walkthrough

### Goal
Assign and verify IP addresses to Switch S1 and S2 via their SVI (Interface VLAN1).

### Key Commands

#### Check current interface status
```bash
Switch> enable
Switch# show ip interface brief
```
Look for `Interface VLAN1` in the output. Check two columns:
- **Status** — should be `up`
- **Protocol** — should be `up`

If either shows `administratively down` → the interface is shut down and must be activated.

#### Activate a shut-down interface (S1 fix)
```bash
Switch# configure terminal
Switch(config)# interface vlan1
Switch(config-if)# no shutdown
```
The `no shutdown` command **re-enables** a disabled interface.

#### Assign an IP address (S2 setup)
```bash
Switch(config)# interface vlan1
Switch(config-if)# ip address 192.168.1.3 255.255.255.0
Switch(config-if)# no shutdown
```

#### Verify the result
```bash
Switch# show ip interface brief
```
Confirm that `Interface VLAN1` shows:
- Correct IP address (e.g., `192.168.1.2` or `192.168.1.3`)
- Status: `up` / Protocol: `up`

### Summary of Lab Setup

| Device | Interface | IP Address | Action Taken |
|---|---|---|---|
| Switch S1 | VLAN1 | 192.168.1.2 | `no shutdown` (was admin down) |
| Switch S2 | VLAN1 | 192.168.1.3 | Assigned IP + `no shutdown` |

---

## 4. Testing Connectivity — Ping Command

### What is Ping?
`ping` sends **echo request packets** to a target IP address and waits for **echo replies**. It verifies whether two devices can communicate over a network.

```bash
ping 192.168.1.2
```

### Typical Output
```
Pinging 192.168.1.2 ...
Request timed out.       ← First attempt may fail (normal)
Reply from 192.168.1.2   ← Subsequent replies succeed
Reply from 192.168.1.2
Reply from 192.168.1.2
```

### Why does the first ping time out?
The first attempt often fails because devices need time to resolve each other's addresses via **ARP (Address Resolution Protocol)**. This is **normal behavior**.

### Bidirectional Testing
Always test connectivity **in both directions**:

```
PC-A → ping 192.168.1.3  (PC-A to S2)  ✅
PC-A → ping 192.168.1.11 (PC-A to PC-B) ✅
PC-B → ping 192.168.1.10 (PC-B to PC-A) ✅
```

### One-way failure = Firewall issue
If ping works in one direction but **not the other**, it typically indicates a **firewall** is blocking ICMP echo requests.

> **Note:** Windows Firewall blocks ICMP by default and may need to be temporarily disabled for network testing.

### Lab Connectivity Summary

| Source | Destination | IP Address | Result |
|---|---|---|---|
| PC-A | Switch S1 | 192.168.1.2 | ✅ Success |
| PC-A | Switch S2 | 192.168.1.3 | ✅ Success |
| PC-A | PC-B | 192.168.1.11 | ✅ Success |
| PC-B | PC-A | 192.168.1.10 | ✅ Success |

---

## Quick Reference — Command Cheatsheet

| Command | Purpose |
|---|---|
| `enable` | Enter Privileged EXEC mode |
| `configure terminal` | Enter Global Configuration mode |
| `interface vlan1` | Enter Interface Configuration mode for SVI |
| `ip address <IP> <mask>` | Assign an IP address to the interface |
| `no shutdown` | Activate (enable) a shut-down interface |
| `show ip interface brief` | View all interfaces, IPs, and their status |
| `ping <IP>` | Test network connectivity to a target IP |
