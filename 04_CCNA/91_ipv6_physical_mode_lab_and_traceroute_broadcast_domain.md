# Packet Tracer — Configure IPv6 Addresses on Network Devices (Physical Mode)

Study notes from working through the Cisco Networking Academy Packet Tracer
Physical Mode (PTPM) lab: cabling a router/switch/PC topology by hand and
configuring IPv6 addressing end-to-end.

## Topology

```
PC-A --F0/6--> S1 --F0/5--> G0/0/1 R1 G0/0/0 --> PC-B
```

| Device | Interface | IPv6 Address        | Prefix | Default Gateway |
|--------|-----------|----------------------|--------|------------------|
| R1     | G0/0/0    | 2001:db8:acad:a::1   | /64    | N/A              |
| R1     | G0/0/1    | 2001:db8:acad:1::1   | /64    | N/A              |
| S1     | VLAN 1    | 2001:db8:acad:1::b   | /64    | N/A (fe80::1)    |
| PC-A   | NIC       | 2001:db8:acad:1::3   | /64    | fe80::1          |
| PC-B   | NIC       | 2001:db8:acad:a::3   | /64    | fe80::1          |

## 1. Physical Mode basics

Unlike Logical Mode, Physical Mode (PTPM) requires **real cabling** before any
CLI is accessible:

- **Ethernet cables** (green, "Copper Straight-Through") connect end devices
  to switch ports and switch-to-router ports per the topology.
- **Console cable** (light blue, RJ45 ↔ RS232) is what actually opens a
  device's CLI. Without one plugged in, clicking a router/switch shows no
  terminal.
- The console cable can be run from **any PC** (doesn't have to be one that's
  part of the data topology) — it's purely a management link, separate from
  the Ethernet data path. Configuring R1 from PC-B's terminal is perfectly
  valid even though PC-B's Ethernet link goes to R1's data interface, not a
  console-dedicated device.
- On the router/switch model used here, the console port is on the **rear**
  panel, not the front — worth checking if a cable "won't unplug" from the
  front view.
- Only one console cable can usefully drive one device at a time; move it
  between R1 and S1 as needed.

## 2. Basic device setup (both R1 and S1)

```
enable
configure terminal
hostname <name>
no ip domain-lookup
enable secret class
line console 0
 password cisco
 login
exit
line vty 0 4        (0 15 on switches — more VTY lines available)
 password cisco
 login
exit
service password-encryption
banner motd # Unauthorized access is prohibited #
```

- `line console 0` = settings for the physical console port.
- `line vty 0 4` = settings for **remote** access (Telnet/SSH) — a separate,
  unrelated configuration mode from interface config. Easy to conflate with
  `ipv6 enable` etc. because both blocks end in `exit`, but one is line
  config and the other is interface config.

## 3. IPv6 addressing on R1

```
interface g0/0/0
 ipv6 address 2001:db8:acad:a::1/64
 ipv6 enable
 no shutdown
exit

interface g0/0/1
 ipv6 address 2001:db8:acad:1::1/64
 ipv6 enable
 no shutdown
exit
```

- `ipv6 enable` explicitly turns on IPv6 processing / generates a link-local
  address on the interface. (Note: assigning a global `ipv6 address` already
  implicitly enables IPv6 on the interface, but it's fine — and common
  practice — to state it explicitly too.)

### Manually setting link-local addresses

```
interface g0/0/0
 ipv6 address fe80::1 link-local
exit
interface g0/0/1
 ipv6 address fe80::1 link-local
exit
```

**Why the same `fe80::1` can be reused on both interfaces:** link-local
addresses are never routed beyond their own link (broadcast domain). Since
G0/0/0 and G0/0/1 sit on two entirely separate networks, `fe80::1` on one has
no way to collide with `fe80::1` on the other.

## 4. Multicast groups on an interface

`show ipv6 interface g0/0/0` lists "Joined group address(es)":

- `FF02::1` — all-IPv6-nodes on the link
- `FF02::1:FF00:1` — solicited-node multicast address (used by Neighbor
  Discovery), derived from the last 24 bits of the interface's address
- `FF02::2` — all-routers group, which only appears **after**
  `ipv6 unicast-routing` is enabled on the router

## 5. Enabling IPv6 routing + SLAAC

```
ipv6 unicast-routing
```

This makes R1 act as an IPv6 router and start periodically sending **Router
Advertisement (RA)** messages on its interfaces (visible via
`ND router advertisements are sent every 200 seconds`).

**SLAAC (Stateless Address Autoconfiguration):** instead of a DHCP-style
server explicitly assigning each host an address ("stateful"), the router
only advertises the network **prefix** via RA. Each host then builds its own
global unicast address by combining that prefix with an interface ID it
generates itself (traditionally from its MAC address), and adopts the RA
sender's link-local address as its default gateway. No server needs to track
who has which address — hence "stateless."

Verified via `ipconfig` on PC-B before/after enabling routing:
- **Before**: only a link-local address, no global unicast address, no
  default gateway.
- **After**: PC-B automatically received a global address using R1's
  advertised prefix (`2001:db8:acad:a::/64`) plus its own MAC-derived
  interface ID, and set `fe80::1` as its default gateway — all without any
  static configuration on PC-B.

## 6. Switch (S1) IPv6 management address

```
interface vlan 1
 ipv6 address 2001:db8:acad:1::b/64
 ipv6 address fe80::1 link-local
 no shutdown
exit
```

**What is a VLAN / why put an IP here?** A switch is a Layer 2 device — it
doesn't need per-port IP addresses to forward frames. But it still needs a
single management IP for things like remote login and `show` commands. That
address is attached not to a physical port but to **VLAN 1's virtual
interface (SVI)** — VLAN 1 being the default VLAN that all switch ports
belong to unless configured otherwise. The SVI only comes `up/up` once at
least one physical port belonging to that VLAN is itself `up/up`.

## 7. PC static IPv6 configuration

Set via Desktop → IP Configuration → IPv6 Configuration → Static, per the
addressing table (PC-A: `2001:db8:acad:1::3/64`, gateway `fe80::1`; PC-B:
`2001:db8:acad:a::3/64`, gateway `fe80::1`).

## 8. Verifying end-to-end connectivity

```
ping fe80::1                        (from PC-A/PC-B to R1's link-local)
tracert 2001:db8:acad:a::3          (PC-A -> PC-B)
ping 2001:db8:acad:1::3             (PC-B -> PC-A)
```

All four checks succeeded (0% packet loss).

### `tracert` vs `ping`

- `ping`: only reports whether the destination is reachable and round-trip
  time.
- `tracert`/`traceroute`: reveals each **hop** (router) along the path by
  sending packets with increasing TTL/Hop Limit values — each router along
  the way decrements TTL by 1, and when it hits 0 that router responds,
  revealing itself as one hop.

Result: `PC-A -> R1 (2001:DB8:ACAD:1::1) -> PC-B` — exactly 2 hops, proving
IPv6 was routing correctly through R1.

**Why the switch (S1) never shows up as a hop:** TTL/Hop Limit is
decremented only by Layer 3 devices (routers) that process the IP header. A
switch operates at Layer 2 and forwards frames based on MAC addresses alone
— it never inspects or modifies the IP header, so it's invisible to
traceroute; it appears as if the cable simply runs straight through it.

**Why the layers are split this way (design rationale):**
1. A switch's job is purely to move frames within *one* network — it has no
   need to understand IP at all.
2. Skipping IP-header processing keeps switching fast and cheap; interpreting
   IP headers per-frame the way a router does would add significant
   overhead.
3. TTL exists specifically to prevent packets from looping forever across
   **routed** paths between separate networks. Within a single switched
   network (one broadcast domain), that kind of multi-path routing loop
   can't occur, so there's no need for a TTL mechanism at that layer.

### Broadcast domain, explained

A **broadcast** is a message sent to every device on a network at once (e.g.
ARP asking "who has this IP?"). A **broadcast domain** is the full set of
devices that broadcast reaches.

- Switches forward broadcasts out every connected port, so everything wired
  to the same switch (possibly across multiple switches) is **one**
  broadcast domain.
- Routers do **not** forward broadcasts from one attached network to
  another — each side of a router is a **separate** broadcast domain.

In this lab: PC-A and S1 share one broadcast domain (`2001:db8:acad:1::/64`);
crossing R1 into PC-B's network (`2001:db8:acad:a::/64`) is a different
broadcast domain. This is also why, within a single broadcast domain,
multi-path loops (and thus TTL-based loop protection) aren't a design
concern — only routers, which sit at domain boundaries, need to manage that.

("Domain" here just means "the range/area a given rule or behavior applies
to" — the same generic sense used in "collision domain," "web domain," or
"domain of a function" in math.)

## 9. Gotcha: unsaved configuration is lost on power-cycle

Packet Tracer only keeps configuration in `running-config` (memory) until
explicitly saved. Powering a device off/on (which happened mid-lab here)
wipes any unsaved config back to defaults (hostname `Router`, interfaces
`shutdown`, no addresses). Confirmed via `show running-config` showing a
fully reset device.

**Lesson: always save after finishing configuration on a device:**

```
copy running-config startup-config
```

(Equivalent shorthand: `write memory` / `wr`.) This should be done
immediately after each device's config is complete, not deferred to the end
of the lab.

## 10. Reflection Questions

**Q1: Why can the same link-local address `fe80::1` be assigned to both
Ethernet interfaces on R1?**

Link-local addresses are scoped to their own link and are never routed. Since
G0/0/0 and G0/0/1 belong to two independent links/networks, the same
`fe80::1` on each has no way to conflict — comparable to two different
buildings each having a "1st floor" with no ambiguity.

**Q2: Subnet ID of `2001:db8:acad::aaaa:1234/64` when the global routing
prefix is a /48?**

Expanding the address into 16-bit blocks:
`2001 : 0db8 : acad : 0000 : 0000 : aaaa : 1234`

- First 48 bits (3 blocks) = Global Routing Prefix = `2001:0db8:acad`
- Next 16 bits (4th block) = Subnet ID = **`0000`**
- Remaining 64 bits = Interface ID

**Subnet ID = 0**
