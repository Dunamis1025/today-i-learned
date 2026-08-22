# Packet Tracer Lab Notes: Use Ping and Traceroute to Test Network Connectivity

A troubleshooting exercise covering IPv4 and IPv6 connectivity across three routers (R1, R2, R3) connecting four PCs through a simulated WAN.

## Topology

```
PC1 (IPv4) --- S1 ---\                              /--- S3 --- PC3 (IPv4)
                       R1 === R2 === R3
PC2 (IPv6) --- S2 ---/                              \--- S4 --- PC4 (IPv6)
```

- R1 ↔ R2 and R2 ↔ R3 are serial WAN links.
- Each router's `G0/0` carries IPv6 to one PC-pair switch; `G0/1` carries IPv4 to the other.
- Routing between routers is handled by **EIGRP** (both `IP-EIGRP` for IPv4 and `IPv6-EIGRP` for IPv6).

## Addressing Table (reference)

| Device | Interface | IPv4 | Mask | IPv6 / Prefix | Link-local |
|---|---|---|---|---|---|
| R1 | G0/0 | — | — | 2001:db8:1:1::1/64 | — |
| R1 | G0/1 | 10.10.1.97 | /27 | — | — |
| R1 | S0/0/1 | 10.10.1.6 | /30 | 2001:db8:1:2::2/64 | fe80::1 |
| R2 | S0/0/0 | 10.10.1.5 | /30 | 2001:db8:1:2::1/64 | fe80::2 |
| R2 | S0/0/1 | 10.10.1.9 | /30 | 2001:db8:1:3::1/64 | fe80::2 |
| R3 | G0/0 | — | — | 2001:db8:1:4::1/64 | fe80::3 |
| R3 | G0/1 | 10.10.1.17 | /28 | — | — |
| R3 | S0/0/1 | 10.10.1.10 | /30 | 2001:db8:1:3::2/64 | fe80::3 |
| PC1 | NIC | 10.10.1.98 | /27, GW 10.10.1.97 | — | — |
| PC2 | NIC | — | — | 2001:db8:1:1::2/64, GW fe80::1 | — |
| PC3 | NIC | 10.10.1.18 | /28, GW 10.10.1.17 | — | — |
| PC4 | NIC | — | — | 2001:db8:1:4::2/64, GW fe80::3 | — |

---

## Part 1: IPv4 Connectivity (PC1 ↔ PC3)

### Symptom
`ping` from PC1 to PC3 fails immediately with:
```
Reply from 10.10.1.97: Destination host unreachable.
```
This differs from a plain timeout — it means the **default gateway itself** (R1) has no route to the destination and rejects the packet right away, rather than forwarding it and losing it downstream.

### Diagnosis process
1. **`tracert 10.10.1.18` from PC1** — every hop returned `10.10.1.97` (R1 itself), meaning the packet never left R1. R1 does not know how to reach PC3's subnet.
2. **`tracert 10.10.1.98` from PC3** — same pattern, stuck at `10.10.1.17` (R3 itself).
3. **`show ip route` on R1** — only showed directly connected networks (`C`/`L` routes): `10.10.1.4/30` and `10.10.1.96/27`. No route to R3's networks (`10.10.1.8/30`, `10.10.1.16/28`).
4. **`show ip route` on R3`** — mirror image: only its own directly connected networks, nothing for R1's side.
5. Both routers only know their *own* neighborhood — neither has learned any route via EIGRP (`D` codes), meaning EIGRP adjacency across the R1–R2–R3 chain isn't functioning.
6. **`show ip route` on R2`** — revealed the root cause: R2's `Serial0/0/0` interface was configured with **10.10.1.2/30** instead of the addressing table's **10.10.1.5/30**. This put R2 in a *different subnet* than R1 (10.10.1.4/30), so despite the physical link being `up/up`, R1 and R2 could never form an EIGRP neighbor relationship.

### Root cause
R2's `Serial0/0/0` IPv4 address was misconfigured (wrong subnet), breaking Layer 3 adjacency with R1 even though Layer 1/2 (`up/up`) looked fine.

### Fix
```
enable
configure terminal
interface serial0/0/0
ip address 10.10.1.5 255.255.255.252
exit
exit
```
Immediately triggered:
```
%DUAL-5-NBRCHANGE: IP-EIGRP 1: Neighbor 10.10.1.6 (Serial0/0/0) is up: new adjacency
```
EIGRP then automatically propagated routes in both directions — R1 learned `10.10.1.8/30` and `10.10.1.16/28` via R2; R3 learned `10.10.1.4/30` and `10.10.1.96/27` via R2. No changes were needed on R1 or R3 themselves.

### Verification
`ping` from PC1 to PC3 and PC3 to PC1: **4/4 packets received, 0% loss.**

---

## Part 2: IPv6 Connectivity (PC2 ↔ PC4)

### Symptom
`ping` from PC2 to PC4 (and reverse) fails with `Request timed out` on all four attempts.

### Diagnosis process
1. **`tracert 2001:DB8:1:4::2` from PC2** — successfully traced through:
   ```
   1  2001:DB8:1:1::1   (R1 G0/0)
   2  2001:DB8:1:2::1   (R2 S0/0/0)
   3  2001:DB8:1:3::2   (R3 S0/0/1)
   4  Request timed out
   ```
   This showed the packet reached **R3 successfully** — meaning IPv6-EIGRP routing between R1, R2, and R3 was working correctly (unlike Part 1). The failure happens *after* R3, on the R3–PC4 segment.
2. Checked PC4's `ipv6config /all`: its **Default Gateway was `FE80::2`**.
3. Checked R3 directly with `show ipv6 interface brief`: R3's actual link-local address is `FE80::3`, and its config matched the addressing table exactly (`2001:DB8:1:4::1`, `FE80::3`) — **R3 itself was correctly configured.**
4. This meant the discrepancy wasn't a router misconfiguration but a **PC-side misconfiguration**: PC4 was pointed at the wrong gateway address (R2's link-local, not R3's).
5. Opened PC4 → Desktop → IP Configuration: IPv6 was set to **Static**, with Default Gateway manually (and incorrectly) entered as `FE80::2`.

### Root cause
PC4's IPv6 configuration was static, and its Default Gateway field was manually set to `FE80::2` (R2's link-local address) instead of `FE80::3` (R3's, its actual first-hop router). PC4 could reach nothing off its local subnet because it was sending all outbound traffic toward a gateway address that wasn't its real neighbor.

### Fix
On PC4 → Desktop → IP Configuration → IPv6 Configuration → Default Gateway: changed `FE80::2` → `FE80::3`.

### Verification
`ping 2001:DB8:1:1::2` from PC4: **4/4 packets received, 0% loss, avg ~6ms.**

---

## Key Concepts Learned

### `show ip interface brief` / `show ipv6 interface brief`
Shows each interface's assigned address, Layer 1 status, and Layer 2 protocol status.
- **Status** = physical/electrical layer (cable connected, signal present).
- **Protocol** = whether the two connected devices are successfully exchanging Layer 2 keepalives/framing.
- `administratively down` = a human explicitly disabled the port with `shutdown`; not a fault. Re-enable with `no shutdown`.
- `up/up` on Status/Protocol but the neighboring device unreachable at Layer 3 = look at IP addressing, not the physical link.
- **Method** column: `manual` = IP was hand-configured; `unset` = no IP address configured at all.

### `show ip route` / route table codes
- **C (connected)**: the network directly attached to an interface, auto-derived from the interface's IP + mask.
- **L (local)**: the exact host address (`/32` for IPv4, `/128` for IPv6) of the interface itself.
- **D (EIGRP)**: a route learned dynamically from a neighboring router via EIGRP (named after EIGRP's underlying algorithm, DUAL — Diffusing Update ALgorithm).
- **S (static)**: a manually configured route (not used in this lab).
- A router only automatically knows routes to networks it's *directly* connected to. Routes to remote networks (reachable through another router) must come from a dynamic routing protocol (EIGRP/OSPF/etc.) or a static route — if neighbors aren't adjacent, those routes never populate.

### Subnetting refresher (IPv4 `/30` example)
- `255.255.255.252` = `/30` → 2 bits of host space → blocks of 4 addresses.
- Grouping the last octet into blocks of 4 (`0-3, 4-7, 8-11, ...`) lets you find which "neighborhood" a host address belongs to.
- Example: host `10.10.1.6` falls in the `4-7` block → network address `10.10.1.4/30`.
- Two routers on the same physical serial link must have addresses in the *same* block/subnet or they cannot form a Layer 3 adjacency, even if the physical link is `up/up`.

### IPv6 addressing
- **Physical (MAC) Address**: burned into the NIC at manufacture time, never changes.
- **Link-local address (`FE80::/10`)**: auto-generated from the MAC address; only valid for communication with directly-connected neighbors on the same link — never routed further. Used as the next-hop/gateway address in `show ipv6 route` and as default gateways for hosts.
- **Global IPv6 address**: the actual routable address used for end-to-end communication (e.g., `2001:DB8:1:1::2`).
- IPv6 subnets are conventionally sized `/64` regardless of how few hosts are on the link — address space is abundant, so subnetting for efficiency (like IPv4's `/30` WAN links) isn't necessary; using `/64` everywhere simplifies design and management.

### EIGRP vs. OSPF (both dynamic routing protocols — same job, different "brand")
- **OSPF** (Open Shortest Path First): an open, vendor-neutral standard; works across different manufacturers' equipment.
- **EIGRP** (Enhanced Interior Gateway Routing Protocol): a Cisco-proprietary protocol, historically limited to Cisco devices.
- Both automatically discover neighboring routers and exchange reachability information so that routers don't need every route manually configured — a router only needs to know "which direction to send it," not the entire path or the existence of every downstream router.
- Route code `D` (EIGRP) appears once two routers become EIGRP **neighbors** — signaled in the CLI by:
  ```
  %DUAL-5-NBRCHANGE: IP-EIGRP 1: Neighbor <ip> (<interface>) is up: new adjacency
  ```

### General troubleshooting methodology used
1. **Confirm the symptom** — `ping` fails (and note *how* it fails: instant "unreachable" vs. timeout, since that hints at where the failure occurs).
2. **Localize the failure point** — `tracert`/`traceroute` shows the last hop successfully reached, narrowing the search to "before X" vs. "after X."
3. **Inspect the suspect devices' configuration** — `show ip/ipv6 interface brief` (Layer 1/2 health) and `show ip/ipv6 route` (Layer 3 knowledge).
4. **Compare actual configuration against the documented design** (the addressing table) to spot discrepancies.
5. **Apply the minimal fix** at the actual point of misconfiguration — don't touch devices that are already correct.
6. **Re-verify** end-to-end with `ping` after the fix, and confirm the dynamic routing protocol re-converges automatically where applicable.

### Two different root-cause categories seen in this lab
| | Part 1 (IPv4) | Part 2 (IPv6) |
|---|---|---|
| Symptom | Ping fails, "destination unreachable" | Ping fails, timeout |
| Where the fault was | Router-to-router link (R2's interface IP in wrong subnet) | End-host gateway configuration (PC4's static default gateway) |
| How traceroute pointed to it | Never left the first router at all | Reached R3 successfully, died right after |
| Fix location | Router CLI (`ip address` command) | PC IP Configuration GUI (Default Gateway field) |

This illustrates that identical symptoms ("can't ping") can have very different root causes — the diagnostic process (traceroute → inspect configs → compare against documentation) is what actually reveals which layer/device is at fault, not the symptom alone.
