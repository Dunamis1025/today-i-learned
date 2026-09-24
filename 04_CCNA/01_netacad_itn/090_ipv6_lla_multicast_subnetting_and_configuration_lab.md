# IPv6 Study Notes — Link-Local Addresses, Multicast, Subnetting & Configuration

Study session covering CCNA-style material (sections 12.6–12.8), including hands-on Packet Tracer configuration.

---

## 1. Dynamic Link-Local Addresses (LLA)

- Every IPv6-enabled device **must** have a Link-Local Address (LLA) to communicate, in addition to any Global Unicast Address (GUA) it may have.
- LLAs always use the reserved prefix **`fe80::/10`**.
- The remaining 64 bits (Interface ID) can be generated dynamically in two ways:
  - **EUI-64 process** — derived from the device's 48-bit MAC address, expanded to 64 bits by inserting `FFFE` in the middle and flipping the 7th bit (U/L bit).
  - **Randomly generated 64-bit number** — no relation to the MAC address.
- LLAs can also be **configured statically** by an administrator for readability.

### On Windows
- Windows typically generates LLAs (and SLAAC-based GUAs) using the **same interface ID** — either EUI-64 or a random number — so the last 64 bits of the GUA and the LLA match.
- Verified via `ipconfig`.

### On Cisco Routers
- Cisco IOS routers automatically create an LLA whenever a GUA is assigned to an interface.
- By default, Cisco uses **EUI-64** based on the interface's MAC address.
- Serial interfaces have no MAC address of their own, so the router **borrows the MAC address of the first available Ethernet interface** — this is valid because LLAs only need to be unique on the local link, not globally.
- Because EUI-64-derived LLAs are long and hard to remember, administrators often configure LLAs statically (e.g., `fe80::1`) for easier recognition.

---

## 2. Verifying IPv6 Configuration

### `show ipv6 interface brief`
- Displays each interface's Layer 1/2 status (`[up/up]`, etc.) and its IPv6 addresses.
- Each active interface shows **two addresses**: the LLA (`fe80::...`) and the configured GUA.
- Useful for a quick check that addressing matches the design/addressing table.

### `show ipv6 route`
- Displays the IPv6 routing table (IPv6 only, not IPv4).
- Route codes:
  - **C** = directly connected network (added automatically when an interface with a GUA is `up/up`)
  - **L** = local route — the specific `/128` address of the router's own interface, used for efficient processing of packets destined to the router itself. (LLAs are *not* listed in the routing table since they aren't routable beyond the local link.)

### `ping`
- Works the same as IPv4 `ping`, just with an IPv6 destination address.
- When pinging an **LLA** from a router, IOS prompts for the **exit interface**, since the same LLA prefix could technically exist on multiple links.

---

## 3. Well-Known & Solicited-Node Multicast Addresses

- IPv6 multicast addresses always start with **`ff00::/8`**.
- Multicast addresses can only be a **destination**, never a source address.

### Well-known multicast groups
- **`ff02::1`** — All-nodes multicast group. Every IPv6-enabled device on the link joins automatically. Functions like an IPv4 broadcast. Routers send Router Advertisement (RA) messages here.
- **`ff02::2`** — All-routers multicast group. Only devices with `ipv6 unicast-routing` enabled (i.e., acting as routers) join this group.

### Solicited-Node multicast
- Used to efficiently target a specific device (e.g., for Duplicate Address Detection / Neighbor Discovery) without flooding every device on the link.
- Maps to a **special Ethernet multicast MAC address**, so a receiving NIC can filter the frame **at the hardware level** just by checking the destination MAC — without passing it up to the IPv6 process — saving CPU overhead for devices that aren't the target.

---

## 4. IPv6 Subnetting

- Unlike IPv4 (where subnetting requires borrowing bits from the host portion), IPv6 was **designed with subnetting in mind** — the GUA has a dedicated **Subnet ID** field between the Global Routing Prefix and the Interface ID.

### Structure (example: 16-bit Subnet ID)
```
Global Routing Prefix (48 bits) | Subnet ID (16 bits) | Interface ID (64 bits)
```
- `/48` prefix + 16-bit Subnet ID → `/64` per subnet.
- 16-bit Subnet ID → up to **65,536 subnets**.
- 64-bit Interface ID → ~18 quintillion hosts per subnet — address conservation is a non-issue.

### Creating subnets
- No binary math needed — just **increment the subnet ID in hexadecimal**:
  `2001:db8:acad:0000::/64` → `0001` → `0002` → ... → `ffff`

### Allocation example
- A topology needing 5 networks (e.g., 4 LANs + 1 router-to-router serial link) simply uses subnets `0001` through `0005` out of the 65,536 available, from block `2001:db8:acad::/48`.
- **Key IPv6-specific point:** even a point-to-point serial link (only 2 hosts needed) gets a full `/64`, same as a LAN — unlike IPv4 where such links are usually given a tiny `/30`. This "wastes" address space by IPv4 standards, but it's a non-issue given IPv6's enormous address space, and keeps addressing consistent and simple.

---

## 5. Hands-On: Packet Tracer — Configure IPv6 Addressing

Topology: Router **R1** connects two LANs (Sales/Billing/Accounting and Design/Engineering/CAD) and an ISP link via a serial interface.

### Part 1 — Router configuration
```
Router> enable
Router# configure terminal
Router(config)# ipv6 unicast-routing
```
- `ipv6 unicast-routing` is required for the router to **forward** IPv6 packets between interfaces (without it, the router can only talk to directly connected networks, not route between them).

For each interface (G0/0, G0/1, S0/0/0):
```
R1(config)# interface gigabitEthernet 0/0
R1(config-if)# ipv6 address 2001:db8:1:1::1/64
R1(config-if)# ipv6 address fe80::1 link-local
R1(config-if)# no shutdown
```
- Repeated for G0/1 (`2001:db8:1:2::1/64`) and S0/0/0 (`2001:db8:1:a001::2/64`), all using the same static LLA `fe80::1` for easy recognition.
- Verified with `show ipv6 interface brief` (all interfaces `up/up`, addresses matching the addressing table).
- Saved configuration: `copy running-config startup-config`.

### Part 2 & 3 — Servers and Clients
- Configured static IPv6 addresses + `/64` prefix on Accounting, CAD, Sales, Billing, Design, and Engineering.
- All devices used **`fe80::1`** (the router's LLA) as their **default gateway** — reinforcing that in IPv6, the default gateway is typically the router's link-local address, not a GUA.

### Part 4 — Testing & Verification
- Opened web pages from Sales to Accounting (same subnet) and to CAD (different subnet, routed through R1) — both succeeded, confirming inter-VLAN/inter-subnet routing worked.
- Pinged the ISP (`2001:db8:1:a001::1`) from Engineering — 100% success, confirming end-to-end routing across all three subnets.

**Result:** Full IPv6 connectivity across three subnets via R1, validating both the addressing scheme and `ipv6 unicast-routing`.

---

## 6. Lab: Identify IPv6 Addresses (own PC)

Ran `ipconfig /all` on a personal Windows machine and identified real-world IPv6 address types on the active Wi-Fi adapter:

| Address type | Example prefix | Meaning |
|---|---|---|
| GUA (Global Unicast) | `2401:d005:...` | Real public IPv6 address assigned by the ISP |
| ULA (Unique-Local) | `fdee:ba45:...` (starts with `fd`) | Private-use IPv6 address, similar role to IPv4's `192.168.x.x` |
| LLA (Link-Local) | `fe80::...` | Local-link-only address, present on the PC and used as the router's address in Default Gateway |

- Noticed multiple **Temporary IPv6 Addresses** (marked Preferred/Deprecated) — this is Windows' **privacy extension** feature, which periodically generates new randomized interface IDs instead of a fixed EUI-64 address, to prevent long-term device tracking.
- Default Gateway was shown as an LLA (`fe80::...`), confirming that router communication over IPv6 uses link-local addressing by design.

---

## Quick Reference: Address Type Prefixes

| Prefix | Type |
|---|---|
| `2000::/3` (e.g., `2001:...`) | Global Unicast Address (GUA) |
| `fc00::/7` (`fc00`/`fd00`) | Unique-Local Address (ULA) |
| `fe80::/10` | Link-Local Address (LLA) |
| `ff00::/8` | Multicast |
| `::1` | Loopback |
