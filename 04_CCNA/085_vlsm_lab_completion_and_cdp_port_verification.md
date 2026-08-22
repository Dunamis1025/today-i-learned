# Packet Tracer Lab: Design and Implement a VLSM Addressing Scheme

## 1. Overview

This lab is part of the Cisco Networking Academy (CCNA) curriculum. Given a
single network address and a set of host requirements, the goal is to:

1. Design a VLSM (Variable Length Subnet Mask) addressing scheme.
2. Configure the design on routers, switches, and PCs inside Packet Tracer.
3. Verify end-to-end connectivity with `ping`.

Deliverable: a filled-in worksheet (Host Requirements table, Subnet Design
table, Addressing Table) plus a working, pingable topology.

## 2. Topology

```
        W2-87 --- WS-2                         172.16.67.0/24 (given network)
                    |
                  (G0/1)
                    |
E2-47 --- ES-2 -- (G0/1)East(G0/0)-- ES-1 --- E1-22
                    |
                (Serial WAN, DCE/DTE)
                    |
                  West
                 (G0/0)    (G0/1)
                    |          |
                  WS-1       WS-2
                    |          |
                 W1-201      W2-87
```

- Two routers: **East** and **West**, connected via a serial WAN link
  (point-to-point).
- Each router has two LAN interfaces (G0/0, G0/1), each connected to a
  switch, each switch connected to one PC.
- Host requirements (from the topology labels):
  - E2-47 (behind ES-2, East router): **23 hosts**
  - E1-22 (behind ES-1, East router): **19 hosts**
  - W1-201 (behind WS-1, West router): **11 hosts**
  - W2-87 (behind WS-2, West router): **7 hosts**
  - WAN link between East and West: **2 hosts** (point-to-point, always 2)
- Given network: **172.16.67.0/24**

## 3. Key VLSM Design Rules

- Subnets must be **contiguous** — no wasted/unused address space between
  them.
- Assign subnets **from largest host requirement to smallest**.
- Use the **most efficient (smallest) subnet** for the router-to-router
  point-to-point WAN link (a /30, giving exactly 2 usable addresses).
- Address assignment convention used in this lab:
  - **First usable address** → router LAN interface (or one side of the WAN
    link)
  - **Last usable address** → the other side of the WAN link
  - **Second usable address** → switch VLAN 1 management interface
  - **Last usable address** → PC (host) NIC

## 4. How Many Host Bits Are Needed?

Formula: smallest `n` such that `2^n - 2 >= required hosts`.

| Required Hosts | Host Bits (n) | Usable Hosts (2^n - 2) | Mask   | CIDR |
|-----------------|---------------|-------------------------|--------|------|
| 23               | 5             | 30                       | 255.255.255.224 | /27 |
| 19               | 5             | 30                       | 255.255.255.224 | /27 |
| 11               | 4             | 14                       | 255.255.255.240 | /28 |
| 7                | 4             | 14                       | 255.255.255.240 | /28 |
| 2 (WAN)          | 2             | 2                        | 255.255.255.252 | /30 |

## 5. Subnet Allocation (Largest → Smallest, Contiguous)

Starting from 172.16.67.0/24, subnets are carved out in descending order of
size:

| Subnet Description | Hosts Needed | Network/CIDR       | First Usable Host | Broadcast Address |
|---------------------|--------------|----------------------|---------------------|----------------------|
| East G0/1 (E2-47)   | 23           | 172.16.67.0/27       | 172.16.67.1          | 172.16.67.31         |
| East G0/0 (E1-22)   | 19           | 172.16.67.32/27      | 172.16.67.33         | 172.16.67.63         |
| West G0/0 (W1-201)  | 11           | 172.16.67.64/28      | 172.16.67.65         | 172.16.67.79         |
| West G0/1 (W2-87)   | 7            | 172.16.67.80/28      | 172.16.67.81         | 172.16.67.95         |
| WAN (East–West)     | 2            | 172.16.67.96/30      | 172.16.67.97         | 172.16.67.99         |

Note: the two /27s (32 addresses each) come first, then the two /28s (16
addresses each), then the /30 (4 addresses) — each new subnet starts exactly
where the previous one's broadcast address ends, so there is zero wasted
space.

## 6. Final Addressing Table

| Device  | Interface | IP Address    | Subnet Mask       | Default Gateway |
|---------|-----------|----------------|--------------------|------------------|
| East    | G0/0      | 172.16.67.33   | 255.255.255.224    | N/A              |
| East    | G0/1      | 172.16.67.1    | 255.255.255.224    | N/A              |
| East    | S0/0/0    | 172.16.67.97   | 255.255.255.252    | N/A              |
| West    | G0/0      | 172.16.67.65   | 255.255.255.240    | N/A              |
| West    | G0/1      | 172.16.67.81   | 255.255.255.240    | N/A              |
| West    | S0/0/0    | 172.16.67.98   | 255.255.255.252    | N/A              |
| ES-1    | VLAN 1    | 172.16.67.34   | 255.255.255.224    | 172.16.67.33     |
| ES-2    | VLAN 1    | 172.16.67.2    | 255.255.255.224    | 172.16.67.1      |
| WS-1    | VLAN 1    | 172.16.67.66   | 255.255.255.240    | 172.16.67.65     |
| WS-2    | VLAN 1    | 172.16.67.82   | 255.255.255.240    | 172.16.67.81     |
| E1-22   | NIC       | 172.16.67.62   | 255.255.255.224    | 172.16.67.33     |
| E2-47   | NIC       | 172.16.67.30   | 255.255.255.224    | 172.16.67.1      |
| W1-201  | NIC       | 172.16.67.78   | 255.255.255.240    | 172.16.67.65     |
| W2-87   | NIC       | 172.16.67.94   | 255.255.255.240    | 172.16.67.81     |

Important: which physical interface (G0/0 vs G0/1) maps to which subnet was
**not visible from the logical topology diagram alone** — it had to be
confirmed on the actual devices (see Section 7). The initial assumption
(G0/0 = larger LAN) turned out to be backwards for the East router once
verified.

## 7. Discovering the Real Interface Mapping (CDP)

A topology diagram doesn't show which physical port connects where unless
port labels are explicitly enabled. Two ways to find this out in Packet
Tracer:

### a) Enable port labels permanently
`Options → Preferences → Interface tab → check "Always Show Port Labels in
Logical Workspace"`. This shows interface names on every link at all times.

### b) Use CDP (Cisco Discovery Protocol) from the CLI
CDP only reports neighbors on interfaces that are **up**, so the interfaces
must be enabled first:

```
enable
configure terminal
interface gigabitEthernet0/0
 no shutdown
interface gigabitEthernet0/1
 no shutdown
end
show cdp neighbors
```

Result on **East**:
```
Device ID   Local Intrfce   Port ID
ES-1        Gig 0/0         Gig 0/1
ES-2        Gig 0/1         Gig 0/1
```
→ East G0/0 goes to ES-1 (19 hosts), East G0/1 goes to ES-2 (23 hosts).

Result on **West**:
```
Device ID   Local Intrfce   Port ID
WS-1        Gig 0/0         Gig 0/1
WS-2        Gig 0/1         Gig 0/1
```
→ West G0/0 goes to WS-1 (11 hosts), West G0/1 goes to WS-2 (7 hosts).

Other useful verification commands:
- `show ip interface brief` — quick view of IP address, admin/line protocol
  status per interface.
- `show controllers serial0/0/0` — identifies whether a serial interface is
  DCE (needs `clock rate`) or DTE.

## 8. Configuration Commands Used

### Router (example: East)
```
enable
configure terminal
interface gigabitEthernet0/0
 ip address 172.16.67.33 255.255.255.224
 no shutdown
exit
interface gigabitEthernet0/1
 ip address 172.16.67.1 255.255.255.224
 no shutdown
exit
interface serial0/0/0
 ip address 172.16.67.97 255.255.255.252
 no shutdown
exit
end
write memory
```
(West router configured the same way with its own values.)

Note: the DCE side of a serial link needs a `clock rate` command (e.g.
`clock rate 64000`) for the link to come fully up; check with
`show controllers serial0/0/0`.

### Switch (example: ES-1)
```
enable
configure terminal
interface vlan1
 ip address 172.16.67.34 255.255.255.224
 no shutdown
exit
end
write memory
```

### PC
Set via Desktop tab → IP Configuration (IP address, subnet mask, default
gateway) — not via CLI.

## 9. Verification

- `ping` between every pair of PCs across all four LANs succeeded.
- Because East and West are directly connected via the WAN link and each
  router only has two directly-connected LAN subnets plus the WAN subnet,
  no dynamic routing protocol or static routes were required beyond the
  directly connected networks — connectivity worked purely from correct
  VLSM addressing and interfaces being up.

## 10. Manual Calculation Walkthrough (Magic Number Method)

This section documents the step-by-step manual/binary process used to
derive the subnets by hand, before shortcutting to the `2^n - 2` formula.
Working through it this way makes the borrowing-bits logic and the
"where do subnets touch" boundary checks much more intuitive.

### a) Starting point

Given network: **172.16.67.0/24**, mask in binary:

```
11111111 . 11111111 . 11111111 . 00000000 = 255.255.255.0
```

Bit place values for the last octet:
```
128  64  32  16  8  4  2  1
2^7  2^6 2^5 2^4 2^3 2^2 2^1 2^0
```

### b) Borrowing bits to reach /27

To carve 172.16.67.0/24 down to **/27**, 3 bits are borrowed from the host
portion:

```
11111111 . 11111111 . 11111111 . 11100000 = 255.255.255.224
```

- 3 bits borrowed → `2^3 = 8` subnets created.
- Remaining host bits = 5 → usable hosts = `2^5 - 2 = 32 - 2 = 30`.
- 30 hosts + network address + broadcast address = 32 addresses per subnet
  block (the "magic number" — the block size / increment between subnet
  starts).

### c) Listing all eight /27 blocks (increment of 32)

```
172.16.67.0/27
172.16.67.32/27
172.16.67.64/27
172.16.67.96/27
172.16.67.128/27
172.16.67.160/27
172.16.67.192/27
172.16.67.224/27
```

Only the first two blocks (0/27 and 32/27) are actually needed — for the
23-host and 19-host LANs (30 usable addresses each, plenty of headroom).
The remaining six /27 blocks are **not wasted** — they get folded back and
re-subnetted into smaller pieces for the 11-host, 7-host, and WAN
requirements ("반으로 잘랐다가 다시 쪼갬" — split in half, then subdivide
again).

### d) Re-subnetting 172.16.67.64/27 into two /28s

Borrowing 1 more bit (4 bits total from the /24):

```
11111111 . 11111111 . 11111111 . 11110000 = 255.255.255.240
```

- 4 bits borrowed → magic number (block size) = `2^4 = 16`.
- Usable hosts = `2^4 - 2 = 14` — enough for the 11-host and 7-host LANs.

```
172.16.67.64/28   (uses the first half of the old .64/27 block)
172.16.67.80/28   (uses the second half of the old .64/27 block)
```

### e) Re-subnetting 172.16.67.96/27 into eight /30s (for the WAN link)

Since only 2 addresses are needed for the point-to-point WAN link, keep
borrowing bits until the block is just big enough:

```
11111111 . 11111111 . 11111111 . 11111100 = 255.255.255.252
```

- 6 bits borrowed from the /24 (2 host bits remain) → magic number = `2^2 = 4`.
- Usable hosts = `2^2 - 2 = 2` — exactly what the WAN link needs.

Listing out the /30 candidates inside the old .96/27 block (increment of 4):
```
172.16.67.96/30, 100/30, 104/30, 108/30, 112/30, 116/30, 120/30, 124/30
```
The first one, **172.16.67.96/30**, is selected for the WAN link; the rest
are unused headroom (allowed, since the design only required one WAN
subnet).

### f) Final subnet table (network ~ broadcast, with hosts needed)

| Block Size | Network/CIDR       | ~ | Broadcast Address    | Hosts Needed |
|------------|----------------------|---|------------------------|---------------|
| 32         | 172.16.67.0/27       | ~ | 172.16.67.31/27        | 23            |
| 32         | 172.16.67.32/27      | ~ | 172.16.67.63/27        | 19            |
| 14         | 172.16.67.64/28      | ~ | 172.16.67.79/28        | 11            |
| 14         | 172.16.67.80/28      | ~ | 172.16.67.95/28        | 7             |
| 4          | 172.16.67.96/30      | ~ | 172.16.67.99/30        | 2 (WAN)       |

This matches the final Subnet Design table in Section 5 exactly.

### g) Assignment convention recap (from the notes)

```
Router  = 1st usable address in the subnet
Switch  = 2nd usable address in the subnet
PC      = last usable address in the subnet
WAN     = East gets 1st usable (.97), West gets last usable (.98)
```

### h) Quick binary reference used throughout (last octet)

```
128  64  32  16  8  4  2  1
2^7  2^6 2^5 2^4 2^3 2^2 2^1 2^0
```
Mask value cheat sheet derived from this row:
- Borrow 1 bit → .128 (2 subnets, 126 hosts each)
- Borrow 2 bits → .192 (4 subnets, 62 hosts each)
- Borrow 3 bits → .224 (8 subnets, 30 hosts each)  ← used for /27
- Borrow 4 bits → .240 (16 subnets, 14 hosts each) ← used for /28
- Borrow 5 bits → .248 (32 subnets, 6 hosts each)
- Borrow 6 bits → .252 (64 subnets, 2 hosts each)  ← used for /30 (WAN)

## 11. Key Takeaways

- VLSM lets you size each subnet to actual host needs instead of using one
  fixed mask everywhere, avoiding wasted address space.
- Always subnet from **largest to smallest** requirement to keep the
  allocation contiguous.
- Point-to-point WAN links only ever need 2 usable addresses → always use
  a /30.
- A logical topology diagram does **not** reveal port-to-port mapping by
  itself; use CDP (`show cdp neighbors`) or enable port labels in Packet
  Tracer preferences to confirm real connections before assigning IPs.
- `show ip interface brief` and `show cdp neighbors` are the two fastest
  CLI commands for sanity-checking a lab mid-configuration.
