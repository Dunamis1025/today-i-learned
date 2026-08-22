# Packet Tracer Lab Notes: 13.3.1 - Use ICMP to Test and Correct Network Connectivity

A larger, more open-ended troubleshooting exercise across a 3-router topology (RTR-1, RTR-2, RTR-3) with mixed IPv4/IPv6 client subnets and a WAN-facing Corporate Server. Unlike the previous lab (13.2.7), the addressing table is provided complete from the start — the task is to compare it against live device configuration to find the discrepancies, with no scripted "test PC1 to PC3" instructions given.

## Topology

```
                    RTR-1 --- Corporate --- Corporate Server
                   /     \
        10.10.2.0/30    10.10.3.0/30
        2001:db8:2::/127  2001:db8:3::/127
                 /           \
             RTR-2           RTR-3
            /    \           /    \
   10.10.1.0/24  2001:db8:1::/64  10.10.5.0/24  2001:db8:5::/64
   (PC-1,LaptopA) (PC-2,PC-3)    (PC-4,Server1) (LaptopB,LaptopC)
```

- RTR-1 ↔ RTR-2 and RTR-1 ↔ RTR-3 are serial WAN links (dual-stack IPv4 + IPv6, /30 and /127 respectively).
- Routing is handled by **EIGRP** for both IPv4 (`IP-EIGRP`) and IPv6 (`IPv6-EIGRP`) — same protocol family as prior labs, just enabled for both stacks simultaneously.
- Five subnets total: two IPv4 client subnets, two IPv6 client subnets, plus the Corporate Server subnet (dual-stack).

## Key strategic decision: testing efficiency

Rather than pinging every host from every other host (an O(n²) approach), the efficient method used was:

1. Identify one **representative host per subnet** (since hosts sharing a subnet share the same gateway and same reachability characteristics).
2. From a single IPv4 representative (PC-1), ping one host in each *other* IPv4 subnet.
3. Separately, from a single IPv6 representative (PC-2), ping one host in each *other* IPv6 subnet.
4. IPv4 and IPv6 reachability must be tested **independently** — a working IPv4 path says nothing about the IPv6 path on the same physical links, since the two protocol stacks maintain entirely separate routing tables and neighbor relationships (as seen directly in this lab, where the IPv4 side was clean while the IPv6 side had a live fault).

This reduced the test surface from many dozens of ping pairs down to roughly 4 pings per protocol stack, which was enough to localize every fault found.

---

## Fault #1 (IPv4): PC-4 — wrong default gateway (typo)

### Symptom
From PC-1: `ping 10.10.5.10` (PC-4) → 100% loss (4/4 timeouts), while `ping 203.0.113.100` (Corporate Server, via RTR-1) succeeded normally.

### Diagnosis
- `tracert 10.10.5.10` from PC-1 showed successful hops through `10.10.1.1` (RTR-2) → `10.10.2.2` (RTR-1) → `10.10.3.2` (RTR-3's S0/1/0) → then timeout. The packet reached RTR-3 successfully; the fault was beyond it.
- `show ip interface brief` and `show ip route` on RTR-3 confirmed the router itself was fully correct: G0/0/0 had `10.10.5.1` exactly matching the addressing table, and `10.10.5.0/24` appeared as a `C` (connected) route.
- Since the router side was clean, the fault had to be on the PC-4 side.
- PC-4 → Desktop → IP Configuration revealed: IP `10.10.5.10` ✓, mask ✓, but **Default Gateway = `10.10.5.11`** — a one-digit typo; it should have been `10.10.5.1` (RTR-3's actual address).

### Fix
Corrected PC-4's Default Gateway field from `10.10.5.11` → `10.10.5.1`.

### Verification
`ping 10.10.5.10` from PC-1: 4/4 success, 0% loss.

---

## Fault #2 (IPv4): Server1 — misconfigured as DHCP instead of static

### Symptom
Opening Server1's IP Configuration showed:
```
DHCP: selected
DHCP failed. APIPA is being used.
IPv4 Address: 169.254.20.92
Subnet Mask: 255.255.0.0
Default Gateway: 0.0.0.0
```

### Explanation
- **DHCP** (Dynamic Host Configuration Protocol) automatically requests an IP configuration from a DHCP server, as opposed to **Static** configuration where the address is entered manually.
- This network has no DHCP server reachable to Server1, so the DHCP request failed.
- When a Windows-style host's DHCP request fails, it falls back to **APIPA** (Automatic Private IP Addressing) — self-assigning an address in the `169.254.0.0/16` block. This address is link-local only (usable only for communication with directly-attached neighbors) and cannot route off-subnet — hence Default Gateway showing `0.0.0.0`.
- Per the addressing table, Server1 should have been statically configured with `10.10.5.20 / 255.255.255.0`, gateway `10.10.5.1`.

### Fix
Switched IP Configuration from DHCP to **Static** and manually entered `10.10.5.20`, `255.255.255.0`, gateway `10.10.5.1`.

### Verification
`ping 10.10.5.20` from PC-1: 3/4 success (one initial timeout attributable to ARP resolution delay — normal on first contact after a config change), 0% loss confirmed on retest.

---

## Fault #3 (IPv6): RTR-3's G0/0/1 — wrong subnet number configured

### Symptom
From PC-2: `ping 2001:db8:5::10` (Laptop B) and `ping 2001:db8:5::20` (Laptop C) both failed instantly with:
```
Reply from 2001:DB8:1::1: Destination host unreachable.
```
(`2001:DB8:1::1` is PC-2's own default gateway, RTR-2's G0/0/1 — meaning RTR-2 itself rejected the packet immediately, having no route to the destination, rather than the packet timing out further downstream.)

Meanwhile `ping 2001:db8:acad::100` (Corporate Server, via RTR-1) succeeded — confirming the RTR-2 ↔ RTR-1 IPv6-EIGRP relationship was healthy, narrowing suspicion toward the RTR-1 ↔ RTR-3 ↔ Laptop B/C side.

### Diagnosis
- `show ipv6 interface brief` on RTR-2 showed all interfaces up/up with correct addressing — inconclusive on its own, since interface status doesn't reveal routing knowledge.
- `show ipv6 route` on RTR-2 revealed the actual issue: instead of a route to `2001:DB8:5::/64` (expected per addressing table), it had learned `2001:DB8:6::/64` via EIGRP — an off-by-one subnet number. RTR-2 wasn't at fault; it was faithfully relaying whatever it was told by an upstream neighbor.
- Checking RTR-3 (the router directly attached to Laptop B/C's subnet) confirmed the root cause: `show ipv6 interface brief` showed **GigabitEthernet0/0/1 = `2001:DB8:6::1`**, when the addressing table called for `2001:db8:5::1/64`. RTR-3 was legitimately, correctly advertising the wrong subnet — because its own interface had been configured with the wrong subnet number to begin with.

### Fix
On RTR-3:
```
enable
configure terminal
interface gigabitEthernet0/0/1
ipv6 address 2001:db8:5::1/64
no ipv6 address 2001:db8:6::1/64
exit
exit
```
Note: the old incorrect address was explicitly removed with `no ipv6 address ...`, since IPv6 interfaces can hold multiple addresses simultaneously — simply adding the correct one would have left the wrong one still active and still being advertised.

### Verification
- `show ipv6 route` on RTR-2 and RTR-1 both updated automatically (via EIGRP re-convergence) to show `2001:DB8:5::/64` in place of the old `2001:DB8:6::/64` entry.
- `ping 2001:db8:5::10` and `ping 2001:db8:5::20` from PC-2: both 4/4 success, 0% loss.

---

## Key Concepts Learned

### ICMP (Internet Control Message Protocol)
The protocol underlying both `ping` and `tracert`/`traceroute` — it's not a new tool, but the formal name for the status/error-reporting messages these tools have been generating all along (`Reply from...`, `Request timed out`, `Destination host unreachable`, etc.). Conceptually similar to a postal system's "undeliverable" return notice: it reports network-layer reachability problems back to the sender.
- `ping` = ICMP Echo Request / Echo Reply — "are you alive?"
- `traceroute` = relies on ICMP Time Exceeded (from transit routers) and Destination Unreachable/Echo Reply (from the final destination), incrementing TTL hop by hop to map the path.

### "Destination unreachable" vs. plain timeout — diagnostic value
- **Immediate "Destination host unreachable" from the *default gateway's own address*** = the first-hop router itself has no route to the target network and rejects the packet without forwarding it. Points to a routing-table gap at (or before) that router.
- **Plain "Request timed out" with no reply at all** = the packet may be traveling further but never getting a reply back, or is being silently dropped somewhere with no ICMP unreachable generated — a different failure mode requiring traceroute to localize.

### DHCP vs. Static, and APIPA
- **DHCP**: host requests an IP configuration automatically from a DHCP server.
- **Static**: IP configuration entered manually and fixed.
- **APIPA** (Automatic Private IP Addressing): the self-assigned fallback address (`169.254.0.0/16`) a Windows-style host uses when a DHCP request fails. It is link-local only, cannot be routed, and its presence (with Default Gateway `0.0.0.0`) is a strong diagnostic signal that DHCP failed rather than that the device was manually misconfigured.

### Reading `show ipv6 interface brief` vs. `show ipv6 route`
Reinforced from the IPv4 case in the prior lab: interface-brief commands only confirm Layer 1/2 status and the interface's own assigned address — they say nothing about whether the router has learned (or is correctly advertising) routes to other networks. Route-table inspection is required to confirm actual reachability knowledge, and comparing the *advertised* subnet against the *documented* subnet is what actually exposes a misconfigured interface upstream of a routing problem.

### EIGRP route table fields, revisited
- `D` code = route learned via EIGRP (named for the underlying DUAL — Diffusing Update ALgorithm — not simply "D for dynamic").
- `[90/2682112]` = `[Administrative Distance / Metric]`. AD (90 for EIGRP) reflects how trustworthy the *source* of the route is relative to other sources (lower = more trusted; directly connected = 0, static = 1, EIGRP = 90, OSPF = 110). Metric is EIGRP's internally computed path-quality score (bandwidth/delay-based); lower = better path. Only relevant for comparing between multiple candidate routes to the same destination — not something manually calculated in day-to-day troubleshooting.
- The trailing timestamp (e.g., `01:01:43`) shows how long ago the route was learned — a very recent timestamp (e.g., seconds) after a config fix is a strong positive signal that EIGRP just re-converged in response to that fix.
- `/30` subnet block-of-4 refresher: a `/30` mask leaves 2 host bits → 4 possible values per block (e.g., `.0, .1, .2, .3`), so identifying which 4-address block a given host IP falls into reveals its network address (e.g., host `.6` → network `.4/30`, covering `.4–.7`).

### General troubleshooting methodology (applied again, now with less guidance)
1. **Scale ping testing efficiently** — one representative host per subnet per protocol stack, rather than exhaustive pairwise testing.
2. **Traceroute to localize** — identify the last successfully-reached hop to bound where the fault lives (before vs. after a specific router).
3. **Interface-brief AND route-table, always as a pair** — interface status confirms Layer 1/2 health; the route table confirms Layer 3 knowledge. Neither alone is sufficient.
4. **Compare live config against the documented addressing table** — the actual mechanism that exposes typos, wrong subnet numbers, or wrong configuration modes (DHCP vs static).
5. **Fix at the exact point of divergence** — leave correctly-configured devices untouched; let the dynamic routing protocol (EIGRP) automatically propagate the correction network-wide once the true source of bad information is corrected.
6. **Re-verify end-to-end**, and tolerate a single initial ping timeout after a fresh config change as a normal ARP-resolution artifact rather than a sign of an unresolved fault.

### Three distinct root-cause categories found in this lab
| | Fault #1 | Fault #2 | Fault #3 |
|---|---|---|---|
| Layer | End-host config | End-host config mode | Router interface config |
| Nature | Typo in a manually-entered value | Wrong config mode entirely (DHCP vs static) | Wrong subnet number in a live, EIGRP-advertised address |
| Symptom | 100% ping loss to that one subnet | APIPA address, gateway `0.0.0.0` | Instant "unreachable" from local gateway; wrong subnet visible network-wide in route tables |
| How it was isolated | Traceroute reached the correct router; router config was clean → pointed to PC | Directly visible in IP Configuration dialog | Route table showed a *different* subnet number than documented; traced upstream to its origin router |

This lab reinforced that "the network is broken" can trace back to faults at any layer — end-host addressing, end-host configuration *mode*, or router interface configuration — and that the diagnostic sequence (ping → traceroute → interface/route inspection → compare against documentation) is what identifies which layer and which specific device is actually at fault, regardless of how similar the initial symptom looks across different faults.
