# Packet Tracer - Basic Device Configuration: Study Notes

## Scenario

A router connects two LANs (Room-145 and Room-146). The task is to configure a router and one switch using Cisco IOS, assign IPv4 and IPv6 addressing to all devices, and verify full end-to-end connectivity with ping.

## Topology

- **Router (Floor14)**
  - G0/0 → Room-145 network: `10.10.10.0/24`, IPv6 `2001:DB8:ACAD:100::/64`
  - G0/1 → Room-146 network: `10.10.11.0/24`, IPv6 `2001:DB8:ACAD:200::/64`
- **Room-145 switch** — locked/inaccessible in this topology; connects Manager-A and Reception-A
- **Room-146 switch** — accessible; connects Manager-B and Reception-B

## Core Concepts Learned

### `show running-config`
Displays the device's currently active configuration held in RAM. This is different from `startup-config`, which is the configuration saved in NVRAM and loaded on reboot. Changes made in a session only persist after `copy running-config startup-config`.

### Interfaces and `shutdown` / `no shutdown`
An interface is a physical port on the device. `shutdown` administratively disables a port even if a cable is physically connected — no traffic will pass. `no shutdown` re-enables it. Configuring an IP address on a shut-down interface has no effect until it is enabled.

### IPv6 Link-Local vs. Global Unicast Addresses
- **Link-local (`FE80::/10`)**: Auto-generated when IPv6 is enabled on an interface. Only usable for communication within the same local network segment; never routable beyond it.
- **Global unicast (e.g., `2001:DB8:ACAD:100::1/64`)**: Must be manually configured. This is the actual routable address used for end-to-end communication across networks.

### Console and VTY Lines
- **`line console 0`**: Configures the physical console port — used when directly connecting a cable/terminal to the device (e.g., for initial setup).
- **`line vty 0 4` / `line vty 5 15`**: Configure virtual terminal lines used for remote access (Telnet/SSH) over the network. "VTY" stands for **Virtual TeleType**, a term inherited from old physical terminal hardware, now referring to a software-emulated remote session.
- Cisco IOS ships with 5 default VTY lines (`0–4`) for historical/backward-compatibility reasons; newer IOS versions allow extending up to 16 total (`5–15` added on top) rather than renumbering the original range, to avoid breaking existing scripts and admin habits.
- Both console and VTY lines need `password` + `login` configured, or login attempts will fail even if the lines are otherwise reachable.

### Cisco Syslog Message Format
Format: `%FACILITY-SEVERITY-MNEMONIC: message`
- FACILITY: subsystem (e.g., `LINK`, `LINEPROTO`)
- SEVERITY: 0 (Emergency, most severe) to 7 (Debugging, least severe); based on the standard syslog severity scale
- Level 5 = "Notification" — a normal state change worth logging, not necessarily a fault (e.g., an interface transitioning from down to up)
- `LINEPROTO` messages commonly appear at severity 5; `LINK` messages (e.g., `LINK-3-UPDOWN`) can appear at severity 3 depending on the event

### Switch VLAN 1 (Management Interface)
Switches are Layer 2 devices — physical ports don't get individual IP addresses. To allow remote management (ping, Telnet/SSH access to the switch itself), a virtual VLAN 1 interface is assigned an IP address. This is unrelated to how actual host traffic passes through the physical ports, which continue to work at Layer 2 regardless of VLAN 1's IP.

### `ip default-gateway` (switch) vs. routing (router)
Since a switch has no routing table, `ip default-gateway` tells it where to send traffic destined for outside its own subnet — analogous conceptually to a host's default gateway.

## Router Configuration Steps (Floor14)

```
Router>enable
Router#configure terminal
Router(config)#hostname Floor14
Floor14(config)#enable secret class

Floor14(config)#line console 0
Floor14(config-line)#password cisco
Floor14(config-line)#login
Floor14(config-line)#exit

Floor14(config)#line vty 0 4
Floor14(config-line)#password cisco
Floor14(config-line)#login
Floor14(config-line)#exit

Floor14(config)#line vty 5 15
Floor14(config-line)#password cisco
Floor14(config-line)#login
Floor14(config-line)#exit

Floor14(config)#service password-encryption
Floor14(config)#banner motd #Unauthorized access is prohibited#

Floor14(config)#interface g0/0
Floor14(config-if)#description Link to Room-145
Floor14(config-if)#ip address 10.10.10.1 255.255.255.0
Floor14(config-if)#ipv6 address 2001:DB8:ACAD:100::1/64
Floor14(config-if)#no shutdown
Floor14(config-if)#exit

Floor14(config)#interface g0/1
Floor14(config-if)#description Link to Room-146
Floor14(config-if)#ip address 10.10.11.1 255.255.255.0
Floor14(config-if)#ipv6 address 2001:DB8:ACAD:200::1/64
Floor14(config-if)#no shutdown
Floor14(config-if)#exit

Floor14(config)#exit
Floor14#copy running-config startup-config
```

Note: `ipv6 unicast-routing` was already enabled by default in this lab's starting configuration.

## Switch Configuration Steps (Room-146)

```
Switch>enable
Switch#configure terminal
Switch(config)#hostname Room-146
Room-146(config)#enable secret class

Room-146(config)#line console 0
Room-146(config-line)#password cisco
Room-146(config-line)#login
Room-146(config-line)#exit

Room-146(config)#line vty 0 4
Room-146(config-line)#password cisco
Room-146(config-line)#login
Room-146(config-line)#exit

Room-146(config)#line vty 5 15
Room-146(config-line)#password cisco
Room-146(config-line)#login
Room-146(config-line)#exit

Room-146(config)#service password-encryption
Room-146(config)#banner motd #Unauthorized access is prohibited#

Room-146(config)#interface vlan 1
Room-146(config-if)#description Management Interface
Room-146(config-if)#ip address 10.10.11.100 255.255.255.0
Room-146(config-if)#no shutdown
Room-146(config-if)#exit
Room-146(config)#ip default-gateway 10.10.11.1

Room-146#copy running-config startup-config
```

Verified via `show ip interface brief` that VLAN1 reached `up/up` status.

## PC Addressing Table (final, verified)

| Device | IPv4 | Gateway | IPv6 | IPv6 Gateway |
|---|---|---|---|---|
| Manager-A | 10.10.10.101/24 | 10.10.10.1 | 2001:DB8:ACAD:100::50/64 | FE80::2 |
| Reception-A | 10.10.10.102/24 | 10.10.10.1 | 2001:DB8:ACAD:100::60/64 | FE80::2 |
| Manager-B | 10.10.11.101/24 | 10.10.11.1 | 2001:DB8:ACAD:200::50/64 | FE80::3 |
| Reception-B | 10.10.11.102/24 | 10.10.11.1 | 2001:DB8:ACAD:200::60/64 | FE80::3 |

Some hosts were pre-filled; others (Reception-A, Manager-B) needed manual entry. One misconfiguration was caught and fixed: Reception-B initially had its IPv4 address entered as `10.10.10.102` (duplicating Reception-A's address, causing an IP conflict) instead of the correct `10.10.11.102`.

## Connectivity Verification

Pinged across both subnets, in both IPv4 and IPv6, from multiple source hosts:
- Manager-A → local gateway, remote gateway, Manager-B (IPv4 and IPv6): all successful
- Reception-A → Room-145 switch, Room-146 switch, Reception-B (IPv4 and IPv6): all successful

**Note on first-ping timeouts:** A single dropped packet on the first ping attempt to a new destination (e.g., "1 lost, 25% loss") is normal and does not indicate a fault. It happens because the sending host must first resolve the destination's MAC address via ARP before the first packet can be delivered; once the ARP entry is cached, subsequent pings succeed immediately. Re-running the ping confirms 0% loss.

## Remaining Wrap-Up Steps
- Confirm `copy running-config startup-config` returned `[OK]` on the switch.
- Use Packet Tracer's "Check Results" button to confirm the completion percentage/score.

---

# Supplement: IPv6 Addressing Concepts (from Gemini session)

## Static (Global) IPv6 Address Configuration

Manually assigning a full, routable IPv6 address to a router interface. The administrator logs into the router, selects a specific interface, and explicitly specifies its address ("this interface's address is this"). The command syntax is similar to IPv4 static addressing, but the address format is longer and follows IPv6 notation. Each interface needs a unique address assigned by hand, and the interface must be enabled for the router to use it to communicate with other devices.

## Link-Local IPv6 Address Configuration

Manually assigning a recognizable, easy-to-remember internal address (typically starting with `FE80`) used for basic communication with nearby devices on the same local segment. Rather than relying on the automatically-generated link-local address, the administrator sets a custom, identifiable one on each interface, making it easier to tell at a glance which interface or device is being referenced during troubleshooting or management.
