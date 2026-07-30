# Session 2 – Routing and OSPF Fundamentals

**Course:** VU23218 – Implement Network Security Infrastructure
**Date:** 30 July 2026

---

## 1. Subnet Mask vs Wildcard Mask

- A **subnet mask** splits an IP address into a **network portion** and a **host portion**.
- A **wildcard mask** is the *inverse* of a subnet mask. It tells a router which bits of an address must match exactly (`0`) and which bits can be anything (`1`).

**Formula:**
```
255.255.255.255 − subnet mask = wildcard mask
```

**Wildcard mask reference table (used in today's lab):**

| Subnet (CIDR) | Subnet Mask       | Wildcard Mask   |
|---------------|-------------------|-----------------|
| /24           | 255.255.255.0     | 0.0.0.255       |
| /25           | 255.255.255.128   | 0.0.0.127       |
| /26           | 255.255.255.192   | 0.0.0.63        |
| /27           | 255.255.255.224   | 0.0.0.31        |
| /28           | 255.255.255.240   | 0.0.0.15        |
| /29           | 255.255.255.248   | 0.0.0.7         |
| /30           | 255.255.255.252   | 0.0.0.3         |

**CIDR notation** (e.g. `/24`, `/28`) = Classless Inter-Domain Routing. The number tells you how many leading bits (from the left) are `1`s in the subnet mask.

---

## 2. What is OSPF?

**OSPF (Open Shortest Path First)** is a dynamic, link-state routing protocol. Routers automatically share information about directly connected networks so they can calculate the shortest path to every other network in the topology — without an admin manually configuring every route (static routing).

- **Area 0 (Backbone Area):** In single-area OSPF, every router and interface belongs to Area 0. In multi-area OSPF, all other areas must connect back through Area 0.
- **Process ID:** A number (1–65535) chosen by the admin when enabling OSPF (`router ospf 10`). It is *locally significant* — it doesn't need to match between routers, but best practice is to keep it consistent.
- **`show ip route` output codes:**
  - `C` = directly connected network
  - `O` = network learned via OSPF (this is the proof OSPF is working — routers now know about networks they aren't directly connected to)

---

## 3. Router CLI Mode Structure

```
Router>                     ← User mode
     ↓ enable
Router#                     ← Privileged / Enable mode  (show commands only)
     ↓ config t
Router(config)#             ← Global configuration mode (hostname, no ip domain-lookup, etc.)
     ↓ router ospf 10
Router(config-router)#      ← Router (OSPF) configuration mode (network ... area 0 commands live here)
```

- `exit` → moves back one level at a time
- `end` → jumps straight back to Privileged mode (`#`) from any depth

---

## 4. Core OSPF Configuration Commands

```
Router(config)#no ip domain-lookup            ! optional: stops CLI from hanging on typos
Router(config)#router ospf 10                 ! enable OSPF, process ID 10
Router(config-router)#network 10.1.1.0 0.0.0.3 area 0
Router(config-router)#network 192.168.10.0 0.0.0.255 area 0
Router(config-router)#end
Router#show ip route                          ! confirm OSPF-learned routes (O) appear
Router#ping 172.16.0.10                        ! test end-to-end connectivity
Router#tracert 172.16.0.10                     ! trace the hop-by-hop path
```

**Command syntax breakdown:**
```
network [network-address] [wildcard-mask] area [area-id]
```
- `network-address` → the network to advertise (must match a directly connected network)
- `wildcard-mask` → calculated from the subnet mask (see table above)
- `area 0` → the OSPF area ID (0 for single-area OSPF)

---

## 5. Today's Lab Topology

```
PC-A(192.168.10.10) ── R1 ══════════ R2 ── PC-B(172.16.0.10)
     192.168.10.0/24        10.1.1.0/30        172.16.0.0/25
```

| Network            | Mask | Wildcard Mask  | Interface(s)                        |
|---------------------|------|----------------|--------------------------------------|
| 192.168.10.0/24     | /24  | 0.0.0.255      | R1 Gig0/0/0                          |
| 10.1.1.0/30         | /30  | 0.0.0.3        | R1 Gig0/0/1 ↔ R2 Gig0/0/1 (point-to-point link) |
| 172.16.0.0/25       | /25  | 0.0.0.127      | R2 Gig0/0/0                          |

**Why /30 for router-to-router links?** A point-to-point link only ever needs 2 usable host addresses (one per router), so /30 avoids wasting IP addresses compared to a larger subnet.

---

## 6. Verification Steps (used for the practical assessment)

1. `show ip route` on both routers **before** OSPF — confirms each router only knows its 2 directly connected networks (missing the 3rd, remote network).
2. Configure OSPF on R1 and R2 (commands above).
3. Watch for the automatic adjacency message:
   ```
   %OSPF-5-ADJCHG: Process 10, Nbr <neighbor-ip> from LOADING to FULL, Loading Done
   ```
   → confirms the two routers have become OSPF neighbors.
4. `show ip route` **after** OSPF — the 3rd network now appears with an `O` code.
5. From PC-A's command prompt:
   ```
   ping 172.16.0.10
   tracert 172.16.0.10
   ```
   - `ping` confirms 0% packet loss end-to-end.
   - `tracert` shows the exact hop path: `PC-A → R1 (192.168.10.1) → R2 (10.1.1.2) → PC-B (172.16.0.10)`.

---

## 7. Assessment Notes

- **Part 2** of the assessment covers this OSPF lab (Question 1: IP addressing + OSPF configuration with `show run` output; Question 2: verify connectivity with ping/traceroute screenshots).
- Screenshots for submission should include:
  - Router `show run` output (IP addresses + `router ospf [id]` + `network ... area 0` lines)
  - The topology diagram with subnet table
  - A visible notepad with **Name** and **Student ID**
  - PDU List window showing **Successful** ping results
  - Visible **date/time** (Windows taskbar clock) somewhere in the screenshot
- **Important distinction found later:** A *separate* "Question 2" exists elsewhere in the assessment document (likely an earlier/different Part) asking to **"configure two routers to communicate over a serial link"** — this is a more basic requirement (no OSPF, no R1/R2/R3 naming) and is satisfied by a simple two-router serial connection with matching subnet, DCE/DTE clocking, and a successful ping. This is *not* the same question as the OSPF-based Part 2 Question 2 above — worth confirming with the instructor if unsure which one is meant.

---

## Quick Reference Cheat Sheet

```
router ospf [process-id]
network [network-address] [wildcard-mask] area [area-id]
show ip route
ping [destination-ip]
tracert [destination-ip]
```

| Subnet | Wildcard Mask |
|--------|---------------|
| /24    | 0.0.0.255     |
| /25    | 0.0.0.127     |
| /30    | 0.0.0.3       |
