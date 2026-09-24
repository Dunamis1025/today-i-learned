# VLSM (Variable Length Subnet Mask) — Study Notes

## 1. Why VLSM Exists

Public IPv4 address space is depleted, so making the most of available
addresses is a priority. Traditional (fixed-length) subnetting divides a
network into equal-sized blocks. This is simple, but wasteful: a
point-to-point WAN link only needs 2 host addresses, yet a traditional
scheme might force it to use a block of 30 usable addresses, wasting 28
of them.

**VLSM** solves this by allowing each subnet to be sized exactly to its
own host requirement, as long as the resulting address ranges never
overlap. IPv6 has such a huge address space that this kind of
conservation generally isn't necessary.

## 2. Core Rules of VLSM

1. **Subnets do not need to be equal size** — as long as their address
   ranges don't overlap, small and large subnets can coexist.
2. **Work from largest to smallest.** Always satisfy the biggest host
   requirement first, then keep subdividing the remaining space for
   smaller requirements. Trying to do it in the opposite order usually
   causes overlaps or wasted space.
3. **No address waste** — each subnet is only as big as it needs to be,
   which conserves the limited public IPv4 pool and leaves extra room
   for future growth.

## 3. Block Size — The Fast Way to Calculate VLSM by Hand

**Block size = 256 − (last octet of the subnet mask)**

| Subnet mask | Last octet | Block size | Usable hosts |
|---|---|---|---|
| /24 (255.255.255.0)   | 0   | 256 | 254 |
| /25 (255.255.255.128) | 128 | 128 | 126 |
| /26 (255.255.255.192) | 192 | 64  | 62  |
| /27 (255.255.255.224) | 224 | 32  | 30  |
| /28 (255.255.255.240) | 240 | 16  | 14  |
| /29 (255.255.255.248) | 248 | 8   | 6   |
| /30 (255.255.255.252) | 252 | 4   | 2   |

**Step-by-step process:**

1. Convert each host requirement into the smallest mask that satisfies
   `2^n − 2 ≥ hosts needed` (n = number of host bits).
2. Sort all required subnets from **largest to smallest**.
3. Start the first (largest) subnet at the beginning of your address
   block (usually `.0`).
4. **Next subnet's starting address = previous subnet's starting address + previous subnet's block size.**
5. **Broadcast address of a subnet = that subnet's starting address + that subnet's own block size − 1.**
6. Continue until every requirement (including point-to-point WAN links,
   which almost always use /30, since they only ever need 2 hosts) has
   been assigned a non-overlapping block.

### Worked Example (from Packet Tracer practice)

Given network: `172.31.103.0/24`

Host requirements:
- User-1 LAN: 27 hosts
- User-2 LAN: 25 hosts
- User-3 LAN: 14 hosts
- User-4 LAN: 8 hosts
- WAN link (Remote-Site1 ↔ Remote-Site2): 2 hosts

| Order | Subnet | Hosts needed | Mask | Block size | Network/CIDR | First usable | Broadcast |
|---|---|---|---|---|---|---|---|
| 1 | User-1 LAN | 27 | /27 | 32 | 172.31.103.0/27   | .1  | .31 |
| 2 | User-2 LAN | 25 | /27 | 32 | 172.31.103.32/27  | .33 | .63 |
| 3 | User-3 LAN | 14 | /28 | 16 | 172.31.103.64/28  | .65 | .79 |
| 4 | User-4 LAN | 8  | /28 | 16 | 172.31.103.80/28  | .81 | .95 |
| 5 | WAN link   | 2  | /30 | 4  | 172.31.103.96/30  | .97 | .99 |

Note how each subnet's starting address is simply the previous
subnet's starting address plus its block size (e.g., User-3's `.64`
= User-1's block of 32 + User-2's block of 32).

### Device Address Assignment Convention

Within each LAN subnet:
- **First usable address** → router LAN interface (acts as the default
  gateway for that subnet).
- **Second usable address** → switch management (VLAN 1) interface.
- **Last usable address** → end-host PCs.

Example — User-4 LAN (`172.31.103.80/28`, usable range `.81`–`.94`):

| Device | IP | Mask | Default Gateway |
|---|---|---|---|
| Remote-Site2 G0/1 (gateway) | 172.31.103.81 | 255.255.255.240 | — |
| Sw4 (VLAN 1)                | 172.31.103.82 | 255.255.255.240 | 172.31.103.81 |
| User-4 (PC)                 | 172.31.103.94 | 255.255.255.240 | 172.31.103.81 |

## 4. Larger Worked Example (Cisco NetAcad video)

Given: `172.16.0.0/23` (512 total addresses), needing subnets for:
200, 100, 50, 25, 10 hosts, plus four point-to-point (2-host) links.

Check: required block sizes are 256, 128, 64, 32, 16, 4, 4, 4, 4 →
sum = 512, which exactly matches the available space.

Process (always split the *remaining* largest leftover block in half,
keep one half, subdivide the other):

| Step | Action | Resulting subnet | Size |
|---|---|---|---|
| 1 | Split /23 into two /24s | 172.16.0.0/24 | 256 |
| 2 | Keep 0.0/24, split 1.0/24 into two /25s | 172.16.1.0/25 | 128 |
| 3 | Keep 1.0/25, split 1.128/25 into two /26s | 172.16.1.128/26 | 64 |
| 4 | Keep 1.128/26, split 1.192/26 into two /27s | 172.16.1.192/27 | 32 |
| 5 | Keep 1.192/27, split 1.224/27 into two /28s | 172.16.1.224/28 | 16 |
| 6 | Split 1.240/28 into four /30s | 1.240, .244, .248, .252 /30 | 4 each |

Result: 9 non-overlapping subnets, each sized to fit real
requirements, with zero wasted addresses.

## 5. Planning Considerations Beyond the Math

- **Plan the whole addressing scheme before subnetting**: number of
  subnets, hosts per subnet, device types, and which addresses will be
  public vs. private.
- **DMZ / externally-facing segments**: need strict conservation and
  VLSM planning because public IPv4 addresses are scarce.
- **Internal (private) networks**: have much more headroom (millions of
  private addresses available), though very large organizations or ISPs
  can still exhaust them and may move to IPv6.
- **Static vs. dynamic addressing**:
  - End-user devices (phones, laptops) → DHCP (dynamic), easier to
    manage and reuse.
  - Servers/printers → static IP, since they must always be reachable
    at a predictable address. Public-facing servers need a public IP
    (often via NAT); internal servers use private IPs and are reached
    remotely via VPN.
  - Routers/firewalls → static IP on every interface, typically the
    first or last usable address in the subnet, serving as the default
    gateway.

## 6. What is a DMZ?

**DMZ = Demilitarized Zone.** A network segment placed between the
public internet and an internal/private LAN, used to host
externally-facing services (web, mail, DNS servers) so that even if
one of those servers is compromised, the attacker still can't directly
reach the internal network. Typically sits behind at least one
firewall (or between two firewalls / on a third firewall interface).

## 7. Today's Hands-On Practice (Packet Tracer)

Topology: two routers (Remote-Site1, Remote-Site2) connected by a WAN
link, each with two LANs (switch + PC), address block
`172.31.103.0/24`.

- Calculated the 5-subnet VLSM scheme shown in section 3 above.
- Configured Remote-Site1's three interfaces (`G0/0`, `G0/1`, `S0/0/0`)
  via CLI — all came up successfully.
- Remote-Site2 and most switches were locked by the activity's design
  (already pre-configured); only Sw3 and User-4 were editable.
- Configured Sw3's VLAN 1 interface and default gateway via CLI.
- Configured User-4's static IP (`172.31.103.94`, mask
  `255.255.255.240`, gateway `172.31.103.81`) via the PC's IP
  Configuration screen, and discussed why each of those three values
  is correct given the subnet it belongs to.
- Next steps: verify connectivity with `ping` between devices/routers
  once all editable devices are configured.
