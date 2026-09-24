# Router and Switch Configuration Lab — Summary Notes

Cisco Packet Tracer lab notes covering router interface configuration, IPv4/IPv6 addressing, default gateway configuration on switches, and the "Connect a Router to a LAN" activity.

---

## 1. Router Interface Configuration

Configuring a router interface means assigning a name, description, and IP address(es) to a physical port so it can communicate with other devices.

**Steps:**
1. **Select the interface** — specify the exact port to configure (e.g., `GigabitEthernet 0/0/0`).
2. **Add a description** — a human-readable note documenting where the connection leads (has no functional effect, purely for documentation).
3. **Assign addresses** — configure IPv4 and/or IPv6 addresses so devices can locate each other.
4. **Enable the interface** — router interfaces are disabled (shutdown) by default and must be explicitly activated with `no shutdown`.

**Example configuration:**
```
R1(config)# interface gigabitethernet 0/0/0
R1(config-if)# description Link to LAN
R1(config-if)# ip address 192.168.10.1 255.255.255.0
R1(config-if)# ipv6 address 2001:db8:acad:10::1/64
R1(config-if)# no shutdown
```

When successful, the system generates log messages confirming the interface has come up:
```
%LINK-3-UPDOWN: Interface GigabitEthernet0/0/0, changed state to up
%LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0/0, changed state to up
```

---

## 2. Verification Commands

| Command | Purpose |
|---|---|
| `show ip interface brief` | Quick summary of all interfaces: IP address and up/down status. Everything should show "up/up" if configured correctly. |
| `show ipv6 interface brief` | Same as above, but for IPv6 addresses and link status. |
| `show ip route` | Displays the IPv4 routing table (which networks the router knows how to reach). |
| `show ipv6 route` | Displays the IPv6 routing table. |
| `show interfaces [interface]` | Detailed statistics for a specific interface: hardware info, MAC address, bandwidth, errors, packet counters. |
| `show ip interface [interface]` | Detailed IPv4-specific settings for a given interface (ACLs, proxy ARP, redirects, etc.). |
| `show ipv6 interface [interface]` | Detailed IPv6-specific settings for a given interface (link-local address, joined multicast groups, ND settings). |

**Routing table route codes:**
- `C` = directly connected network
- `L` = local address (the router's own interface address)
- `O` = route learned dynamically via OSPF (from another router)
- `S` = static route (manually configured by an administrator)

---

## 3. Default Gateway Concept

- The **default gateway** is the router address that serves as the "exit door" to other networks.
- **Same-network communication**: devices on the same network communicate directly, without going through the router.
- **Cross-network communication**: devices on different networks send traffic through the default gateway (router), which forwards it toward the destination.

---

## 4. Configuring a Default Gateway on a Switch

- A Layer 2 switch does not need an IP address to forward traffic between devices on the same network.
- However, to allow an administrator to manage the switch remotely (e.g., via Telnet/SSH from a different network), the switch needs:
  - A management IP address (assigned to a Switch Virtual Interface, SVI — typically VLAN 1)
  - A **default gateway**, so its management traffic can exit the local network when responding to a remote administrator

**Configuration command:**
```
S1(config)# ip default-gateway 192.168.10.1
```
This points the switch toward the router's interface IP address on the same local network.

---

## 5. Hands-On Lab: "Connect a Router to a LAN"

### Topology / Addressing Table

| Device | Interface | IP Address | Subnet Mask | Default Gateway |
|---|---|---|---|---|
| R1 | G0/0 | 192.168.10.1 | 255.255.255.0 | N/A |
| R1 | G0/1 | 192.168.11.1 | 255.255.255.0 | N/A |
| R1 | S0/0/0 (DCE) | 209.165.200.225 | 255.255.255.252 | N/A |
| R2 | G0/0 | 10.1.1.1 | 255.255.255.0 | N/A |
| R2 | G0/1 | 10.1.2.1 | 255.255.255.0 | N/A |
| R2 | S0/0/0 | 209.165.200.226 | 255.255.255.252 | N/A |
| PC1 | NIC | 192.168.10.10 | 255.255.255.0 | 192.168.10.1 |
| PC2 | NIC | 192.168.11.10 | 255.255.255.0 | 192.168.11.1 |
| PC3 | NIC | 10.1.1.10 | 255.255.255.0 | 10.1.1.1 |
| PC4 | NIC | 10.1.2.10 | 255.255.255.0 | 10.1.2.1 |

Console password: `cisco` — Privileged EXEC password: `class`

### Part 1: Initial Router State Discovery

- `show interfaces` → full statistics for every interface on the router (long output; shows admin status, MAC address, bandwidth, error counters, etc.)
- `show ip interface brief` → condensed table of all interfaces with IP address and up/down status
- `show ip route` → showed only one connected route initially:
  ```
  C  209.165.200.224/30 is directly connected, Serial0/0/0
  ```
  Serial0/0/0 was the only interface already active (pre-configured); all Ethernet interfaces were `administratively down` (disabled, no IP assigned).
- A router that receives a packet for a destination not in its routing table simply **drops the packet** (unless a default route / "gateway of last resort" is configured, which was not the case here).

### Part 2: Configuring Router Interfaces

**R1 — GigabitEthernet0/0:**
```
R1(config)# interface gigabitethernet 0/0
R1(config-if)# ip address 192.168.10.1 255.255.255.0
R1(config-if)# no shutdown
R1(config-if)# description LAN connection to S1
```
Verified with: `ping 192.168.10.10` → 80% success rate (first packet timed out due to ARP resolution delay, which is normal/expected behavior).

**R1 — GigabitEthernet0/1:**
```
R1(config)# interface gigabitethernet 0/1
R1(config-if)# ip address 192.168.11.1 255.255.255.0
R1(config-if)# no shutdown
R1(config-if)# description LAN connection to S2
```

**R2 — GigabitEthernet0/0:**
```
R2(config)# interface gigabitethernet 0/0
R2(config-if)# ip address 10.1.1.1 255.255.255.0
R2(config-if)# no shutdown
R2(config-if)# description LAN connection to S3
```

**R2 — GigabitEthernet0/1:**
```
R2(config)# interface gigabitethernet 0/1
R2(config-if)# ip address 10.1.2.1 255.255.255.0
R2(config-if)# no shutdown
R2(config-if)# description LAN connection to S4
```

Result — `show ip interface brief` on both routers confirmed all Ethernet + Serial interfaces were `up/up`.

### Part 2, Step 3: Saving Configuration to NVRAM

Running-config lives in RAM and is lost on reboot. It must be copied to startup-config (NVRAM) to persist:
```
R1# copy running-config startup-config
R2# copy running-config startup-config
```
Both routers returned `[OK]`, confirming the save was successful.

### Part 3: Final Verification

**Routing table check on R1 (`show ip route`) after full configuration:**
```
O   10.1.1.0/24 [110/65] via 209.165.200.226, Serial0/0/0
O   10.1.1.0/24 [110/65] via 209.165.200.226, Serial0/0/0
O   10.1.2.0/24 [110/65] via 209.165.200.226, Serial0/0/0
C   192.168.10.0/24 is directly connected, GigabitEthernet0/0
C   192.168.11.0/24 is directly connected, GigabitEthernet0/1
C   209.165.200.224/30 is directly connected, Serial0/0/0
```

- **Connected (C) routes:** 3
- **OSPF (O) routes:** 2 — R1 automatically learned about R2's LANs (10.1.1.0/24 and 10.1.2.0/24) via the OSPF dynamic routing protocol running between R1 and R2 over the Serial link.
- **Total LANs + WANs in topology:** 5 (192.168.10.0, 192.168.11.0, 10.1.1.0, 10.1.2.0 = 4 LANs; 209.165.200.224/30 = 1 WAN)
- **C + O route count (3 + 2 = 5) matches the topology total (5)** → confirms the router has full knowledge of every network in the topology.

**What OSPF does:** instead of an administrator manually configuring static routes to every remote network on every router, OSPF lets routers automatically advertise their directly connected networks to their neighbors. Each router then calculates the best path to reach networks it isn't directly connected to. The `[110/65]` notation shown in the routing table means: `110` = OSPF's administrative distance (trustworthiness ranking of the route source), `65` = the calculated path cost (metric) — the lower this number, the better/shorter the path.

### End-to-End Connectivity Tests

| Test | Result |
|---|---|
| `ping 10.1.2.10` from PC1 (192.168.10.10) | 3/4 packets succeeded (75%) — first packet lost due to ARP delay |
| `ping 192.168.11.10` from R2 | 4/5 packets succeeded (80%), round-trip 8–12 ms |

Both tests succeeded, confirming full end-to-end connectivity across the entire topology — traffic correctly traversed from one LAN, through both routers via OSPF-learned routes, to a LAN on the opposite side of the network.

**Note:** Switches in this activity were left unconfigured, so pinging the switches themselves was not expected to work.

---

## 6. Key Takeaways

- Router interfaces are **disabled by default** and require `no shutdown` to activate.
- `description` commands are documentation-only and do not affect network function.
- `show ip interface brief` is the fastest way to confirm interface status and addressing.
- The first ping to a new destination often fails due to **ARP resolution delay** — this is expected, not a fault.
- **OSPF** eliminates the need for manual static routing between routers by automatically exchanging network reachability information.
- Configuration changes only persist after `copy running-config startup-config` saves them to NVRAM.
- A Layer 2 switch needs a default gateway configured (`ip default-gateway`) only for its own management traffic to reach devices outside its local network — it does not perform IP routing itself.
