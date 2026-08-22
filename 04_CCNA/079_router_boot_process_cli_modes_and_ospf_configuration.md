# Networking Fundamentals — Study Notes

Consolidated notes from a study session covering Cisco router/switch fundamentals,
IPv4/IPv6 basics, ARP, OSPF, and CLI configuration modes. Combines concept
discussions with a 32-question review set.

---

## 1. Cisco Device Boot Process

When a router or switch powers on, it goes through three phases:

1. **Phase 1 — POST + Bootstrap:** The device performs a Power-On Self-Test (checks
   hardware for faults) and loads the **bootstrap program** from ROM.
2. **Phase 2 — Load IOS:** The bootstrap program locates and loads the **Cisco IOS**
   software (the actual operating system), typically from Flash memory.
3. **Phase 3 — Load Configuration:** Once IOS is running, the device loads the saved
   **startup configuration file** from NVRAM to restore its settings.

### What is a Bootstrap Program?
The word "bootstrap" comes from "pull yourself up by your bootstraps" — starting
something with no outside help. The bootstrap program is a small program stored in
ROM whose only job is to find and load the real operating system (IOS).

> **Analogy:** Like the ignition switch on a gas stove — it isn't the flame itself,
> but it's the small trigger that lights it. IOS is the flame; configurations are
> the food cooked on top of it.

### If the configuration file is missing
If NVRAM has no startup-config file when the router boots, the router has no
instructions to follow, so it automatically enters **setup mode**, prompting the
user to build a configuration from scratch.

---

## 2. CLI Configuration Modes

Cisco IOS uses a layered set of command modes. Moving "deeper" restricts what you're
configuring to a more specific target; moving back "up" widens the scope again.

| Mode | Prompt | Purpose |
|---|---|---|
| User EXEC | `Router>` | View-only; almost nothing can be changed |
| Privileged EXEC | `Router#` | View everything (`show ...`), save/reload |
| Global Configuration | `Router(config)#` | Settings that apply to the whole device |
| Interface Configuration | `Router(config-if)#` | Settings for one specific interface |
| Line Configuration | `Router(config-line)#` | Settings for console/VTY access lines |

**Mode transitions:**
- `enable` → User EXEC → Privileged EXEC
- `configure terminal` → Privileged EXEC → Global Config
- `interface gi0/0` or `line vty 0 4` → Global Config → a specific sub-mode
- `end` → jumps straight back to Privileged EXEC from any sub-mode

**Rule of thumb for matching a command to its mode:**
- Does it apply to *one specific port* (e.g. `ip address`)? → `(config-if)#`
- Does it apply to a *login/access line* (e.g. `login`, `password`, `transport input
  ssh`)? → `(config-line)#`
- Does it apply to the *whole device* (e.g. `hostname`, `service
  password-encryption`, `router ospf 10`)? → `(config)#`
- Is it a *save/verify/reload* action (e.g. `copy running-config startup-config`,
  `show ip route`)? → `#` (Privileged EXEC)
- Is it just `enable`? → typed at `>` (User EXEC)

### Example: interface configuration block
```
Floor(config)# interface gi0/1
Floor(config-if)# description Connects to the Registrar LAN
Floor(config-if)# ip address 192.168.235.234 255.255.255.0
Floor(config-if)# no shutdown
```
- `interface gi0/1` enters interface config mode for that port.
- `description ...` is just a human-readable label — has no effect on traffic.
- `ip address ...` assigns an IP address and subnet mask to the interface.
- `no shutdown` activates the interface (interfaces are administratively down by
  default).

Repeating this block for each interface (Gi0/0, S0/0/0, S0/0/1, etc.) configures the
whole router. `end` at the end exits all the way back to Privileged EXEC.

---

## 3. RAM vs. NVRAM

| | RAM (running-config) | NVRAM (startup-config) |
|---|---|---|
| Persists after reboot? | ❌ No | ✅ Yes |
| Holds | The configuration currently active/in use | The configuration loaded at boot |
| Command to save current state | `copy running-config startup-config` | — |

- `copy running-config startup-config` copies the live configuration into NVRAM so
  it survives a reboot. **Effect: the contents of NVRAM change.**
- **Two key functions of NVRAM:** (1) retains contents when power is removed, (2)
  stores the startup configuration file.

---

## 4. Interfaces, Loopback, and MAC Addresses

- A **physical interface** (e.g. `GigabitEthernet0/0`) is a real port with a cable,
  and it has its own unique **MAC address** burned in at the hardware level. A
  router doesn't have one single MAC address — each physical port has its own.
- A **Loopback interface** is a virtual, software-only interface with **no physical
  connection and no MAC address**. It's always "up" as long as the device is
  running, since there's no cable that can be unplugged.
- **Why use a Loopback?** To have a stable address that never goes down — commonly
  used as the **OSPF Router ID** or for reliable remote management, so that even if
  one physical port fails, the device is still reachable through any surviving port.
- Loopback traffic still physically arrives over a real port (cable) — the loopback
  address is simply the internal "destination" once inside the router, not a
  wireless or magic connection.
- Wi-Fi is unrelated to loopback: wireless NICs are real physical interfaces (using
  radio waves instead of cables) and do have their own MAC addresses. The Cisco ISR
  routers used in these labs have no wireless capability at all.

---

## 5. IPv4 Basics

### Connectionless
IP is a **connectionless** protocol — like dropping a letter in a mailbox without
first confirming the recipient is ready. Data is sent without establishing a prior
connection.

### The Protocol Field
A field in the IPv4 header that identifies **which upper-layer (Layer 4) protocol**
the packet is carrying (e.g. value 6 = TCP, 17 = UDP, 1 = ICMP). Like a label on a
shipping box saying what's inside, so the receiver knows how to process it.

### IPv6 Improvements over IPv4
- **Simplified header** → more efficient packet handling by routers.
- **Flow Label field** → tags packets belonging to the same real-time
  conversation (e.g. video/audio streaming) so routers keep them on the same path.
- **NAT is unnecessary** in IPv6 because the address space is so vast that every
  host can have its own public IPv6 address — no need to share/translate private
  addresses like in IPv4.

---

## 6. Routing Basics

### Two Primary Router Functions
1. **Path selection** — determining the best route to a destination.
2. **Packet forwarding** — actually sending packets out along the chosen path.

### Two Network Layer (OSI Layer 3) Services
1. Routing packets toward the destination.
2. Encapsulating PDUs received from the transport layer.

### Remote vs. Local Routes
- A **remote route** is a destination network reached via a **next-hop address**
  (i.e., through another router), because it isn't directly connected.

### Reading a Routing Table
Route codes seen with `show ip route`:
- `C` = directly Connected network
- `L` = Local (the router's own exact interface address)
- `O` = learned via **OSPF**
- `S` = Static route

Example line:
```
O    172.16.0.0/25 [110/2] via 10.1.1.2, 00:16:52, GigabitEthernet0/0/1
```
This means the router learned, via OSPF, that 172.16.0.0/25 is reachable by
forwarding through 10.1.1.2.

"**Variably subnetted**" simply means a major network block (e.g. a /16) contains
subnets using a different (variable) prefix length (e.g. /25) — it's an
informational header line, not an error.

### Default Gateway
The default gateway is the "exit door" a host uses to reach networks outside its own
local subnet. If configured incorrectly (or missing), the host can still talk to
devices on its own local network but **cannot reach any other network**.

**Practical rule:** the default gateway for hosts on a given LAN = the IP address of
the router interface that connects to that same LAN.

Example: for hosts on the "Registrar LAN," if the router's Gi0/1 interface
(described as "Connects to the Registrar LAN") has IP `192.168.235.234`, that address
is the correct default gateway for new hosts on that LAN.

---

## 7. Single-Area OSPFv2

### Concept
**OSPF (Open Shortest Path First)** is a link-state routing protocol. Each router:
1. Advertises the networks it's directly connected to.
2. Builds a full map of the network from everyone's advertisements.
3. Independently runs **Dijkstra's algorithm** to compute the shortest path to every
   known destination.

Each router calculates its own routes independently — there's no central controller.

### Dijkstra's Algorithm
An algorithm for finding the shortest path from one node to every other node in a
graph, based on the cost of each link. OSPF uses it to determine the lowest-cost path
to each destination network.

### Areas and the Backbone (Area 0)
- OSPF can divide a large network into **areas** to reduce the size of each router's
  link-state database and limit how far a change has to propagate.
- **Area 0** is mandatory and called the **backbone area** — all other areas must
  connect through it (analogy: the spine, with other areas as ribs).
- Between areas, only **summarized** route information crosses the boundary (via an
  Area Border Router) — not the full internal link-state detail.
- For **single-area OSPF**, everything is simply placed in Area 0.

### Wildcard Masks
Used in the `network` command to tell OSPF which interfaces to enable. Calculated by
subtracting the subnet mask from 255.255.255.255.

| Subnet | Subnet Mask | Wildcard Mask |
|---|---|---|
| /24 | 255.255.255.0 | 0.0.0.255 |
| /28 | 255.255.255.240 | 0.0.0.15 |
| /25 | 255.255.255.128 | 0.0.0.127 |
| /30 | 255.255.255.252 | 0.0.0.3 |

### Configuration Example (R1 – R2 lab)
Subnets: `192.168.10.0/24` (R1 LAN), `10.1.1.0/30` (R1–R2 link), `172.16.0.0/25` (R2
LAN).

**R1:**
```
enable
configure terminal
router ospf 10
network 192.168.10.0 0.0.0.255 area 0
network 10.1.1.0 0.0.0.3 area 0
```
**R2:**
```
enable
configure terminal
router ospf 10
network 172.16.0.0 0.0.0.127 area 0
network 10.1.1.0 0.0.0.3 area 0
```

- `router ospf 10` starts an independent OSPF process on that specific router — it
  must be configured separately on every router (process ID doesn't need to match
  between routers, though matching is best practice).
- `network ... area 0` doesn't set IP addresses — it just tells OSPF which
  already-configured interfaces to enable, and what area they belong to.

### Verification Steps
1. **Adjacency check** — look for:
   ```
   %OSPF-5-ADJCHG: Process 10, Nbr 192.168.10.1 on GigabitEthernet0/0/1 from LOADING to FULL
   ```
   `FULL` = the two routers have completely exchanged link-state info and are fully
   adjacent.
2. **`show ip route`** — confirm each router learned an `O` route to the other's
   subnet via the correct next hop.
3. **Ping test in both directions** (PC-A → PC-B and PC-B → PC-A) — rules out
   asymmetric routing issues. A single timed-out ping on the very first attempt after
   adjacency forms is normal (ARP resolution delay).

### Adjacency (word meaning)
"Adjacency" comes from "adjacent" (next to/neighboring). In OSPF, forming an
adjacency means two routers have gone beyond simply discovering each other
(**Neighbor** state) to **fully exchanging and synchronizing their link-state
databases** (**FULL** state).

---

## 8. ARP (Address Resolution Protocol)

- **Function:** ARP discovers the MAC address of a host on the local network when
  only its IP address is known.
- **ARP request destination address:** the broadcast address `FFFF.FFFF.FFFF` — asks
  the entire local network "who has this IP address?"
- **Why the NIC hands ARP data to the ARP process:** Ethernet frames carry a "type
  field" in their header. When a NIC sees the value `0x806`, it recognizes the frame
  as ARP and passes it to the ARP process.
- **`arp -d *` command:** clears the ARP cache on a PC — useful after network
  changes (e.g. a router being reconfigured) to remove stale address mappings.
- **ARP spoofing:** an attack where a device sends fake ARP messages to associate an
  IP address with the wrong (attacker's) MAC address, allowing traffic interception.
- **Two potential problems from ARP operation:**
  1. Attackers can manipulate MAC/IP mappings in ARP messages to intercept traffic.
  2. On large, low-bandwidth networks, frequent ARP broadcasts can cause
     communication delays.
- **IPv6 equivalent:** IPv6 doesn't use ARP. Instead, it uses **Neighbor
  Solicitation** and **Neighbor Advertisement** messages for address resolution.

---

## 9. Switching Behavior

A switch **floods** a frame out of every port except the one it arrived on when:
1. The destination MAC address is **unknown** to the switch (not in its MAC address
   table).
2. The frame's destination is the **broadcast address**.

Example: if PC1 sends a frame to PC3, but PC3 isn't yet in the switch's MAC address
table, the switch floods the frame out of every port except the one it received it
on.

---

## 10. ICMP (Internet Control Message Protocol)

- ICMP doesn't carry actual application data — it's a **messenger protocol** that
  reports network status.
- `ping` uses ICMP: it sends an **Echo Request** ("are you alive?") and expects an
  **Echo Reply** ("yes, I'm alive!") in return.
- Also reports problems such as **Destination Unreachable** and **Time Exceeded**
  (used by `traceroute`).
- In the IPv4 header's Protocol field, ICMP corresponds to value **1**.

### Loopback Test
Sending a signal to a device's own IP (e.g. `127.0.0.1`) to confirm that **the
TCP/IP stack on the device is working correctly** — it doesn't test the network,
just the local networking software.

---

## 11. Remote Access & Device Security

| Access Method | Description |
|---|---|
| Console | Direct physical cable connection; preferred **out-of-band** management method |
| AUX | Remote access via a dialup connection |
| Telnet | Remote access — **unencrypted / unsecure** |
| SSH | Remote access — **encrypted** |

### VTY Lines
**VTY = Virtual TeletYpe.** A virtual channel used for **remote** access to a device
(as opposed to the physical console port). By default, Cisco devices have 5 VTY
lines (`line vty 0 4`), allowing up to 5 simultaneous remote sessions.

```
Router(config)# line vty 0 4
Router(config-line)# transport input ssh
```
This restricts remote access to **SSH only**, blocking unencrypted methods like
Telnet. **Result: all communication between the device and remote users is
encrypted.**

### Securing the Console
Three commands used to secure console access:
```
line console 0
password cisco
login
```
- `line console 0` enters console line configuration mode.
- `password cisco` sets the password.
- `login` enables the password prompt at login.

### Testing a Banner Message
The fastest way to verify a banner is configured correctly: **exit privileged EXEC
mode and press Enter** — this re-triggers the login prompt sequence where the banner
displays.

### Banner / Hostname / Password Commands
| Action | Command | Mode |
|---|---|---|
| Display a message after accessing the router | `banner motd #` | `(config)#` |
| Configure a device name | `hostname CL1` | `(config)#` |
| Secure console access | `password class` | `(config-line)#` |

---

## Summary

This session covered the full path from powering on a Cisco device (POST →
bootstrap → IOS → startup-config) through CLI mode navigation, IPv4/IPv6
fundamentals, ARP and switch flooding behavior, ICMP, remote access security (VTY,
SSH, console), and a hands-on Single-Area OSPFv2 lab (R1–R2) — including wildcard
mask calculation, `network` command configuration, and verifying adjacency, routing
tables, and end-to-end connectivity via ping.
