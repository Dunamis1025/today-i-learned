# VU23218 – Session 10: Zone-Based Policy Firewalls (ZPF)

> **Unit:** VU23218 – Implement Network Security Infrastructure
> **Topic:** Module 10 – Zone-Based Policy Firewalls (Cisco IOS)
> **Date:** 2026-10-08
> **Lab:** Packet Tracer – Configure a ZPF (10.3.11)

---

## 1. Big Picture (TL;DR)

- **ZPF** = put interfaces into **security zones**, then apply **policies to traffic moving between zones** (not to individual interfaces).
- Policy is **directional**: *source zone → destination zone*.
- **Default between zones = DROP** unless a policy explicitly allows it.
- Three actions: **inspect**, **drop**, **pass**.
- Five configuration steps (order matters):
  1. Create the zones
  2. Identify traffic with a **class-map**
  3. Define an action with a **policy-map**
  4. Create a **zone pair** and attach the policy-map
  5. Assign **interfaces** to zones (do this **last**)

---

## 2. Classic Firewall vs. ZPF

| | Classic Firewall (CBAC) | Zone-Based Policy Firewall |
|---|---|---|
| Policy applied to | **Interface** | **Traffic between zones** |
| Depends on ACLs | Yes | **No** (ACLs can still be *referenced* by class-maps) |
| Default behaviour | Permissive per interface | **Deny unless explicitly permitted** |
| Policy language | Interface-bound inspection rules | **C3PL** (Cisco Common Classification Policy Language) |
| Readability / scalability | Harder | Easier to read, troubleshoot and scale |

**ZPF advantages**
- Not dependent on ACLs.
- Router is secure by default: *block unless explicitly allowed*.
- Policies are easy to read and troubleshoot with C3PL.
- One policy can handle many traffic classes.
- Interfaces (physical or virtual) can be grouped into zones.
- Policy applies to **one direction** of traffic between two zones.

---

## 3. Designing a ZPF (4 design steps)

1. **Determine the zones** – a zone is a boundary where traffic is subject to policy restrictions when crossing to another region.
2. **Establish policies between zones** – what the clients in the source zone may request from servers in the destination zone.
3. **Design the physical infrastructure** – how many devices between the most-secure and least-secure zones; need for redundancy.
4. **Identify subsets within zones and merge traffic requirements** – *out of scope for this course*.

### Zone naming

| Role | Common names |
|---|---|
| Trusted / LAN side | **Private = Inside = Internal = Trusted** |
| Untrusted / Internet side | **Public = Outside = External** |

- Zone names are **free to choose** but should be meaningful.
- Convention: **UPPERCASE** (e.g., `IN-ZONE`, `OUT-ZONE`) – stands out in `show running-config`. Convention, not a rule.
- Always follow the exact names given in an assessment/lab.

### Example topologies
- **LAN-to-Internet:** Inside zone ↔ firewall router ↔ Outside zone.
- **Redundant firewall design:** duplicate firewalls (and sometimes duplicate ISPs) for resilience; balance cost against the **value of the assets protected** (ROI mindset).
- **Complex design:** many zones (Inside, Administrator, E-Commerce, Perimeter/DMZ, VPN/remote workers, Outside), each with different policy. Related to network segmentation (subnets/VLANs).

---

## 4. ZPF Operation

### 4.1 Three actions

| Action | Meaning | ACL analogy |
|---|---|---|
| **inspect** | **Stateful** packet inspection. Router keeps session info for TCP/UDP and **automatically permits return traffic**. | — (ZPF-specific) |
| **drop** | Discards unwanted traffic. Optional `log` to record dropped packets. | `deny` |
| **pass** | Forwards traffic from one zone to another. **Stateless** – no connection tracking, so a return-direction policy is also required. | `permit` |

### 4.2 Stateful inspection explained

A stateful firewall remembers the **state of active connections** (source IP, source port, destination IP, destination port, protocol). When an inside host starts a connection, the firewall records it in a **state table**; the reply is recognised as belonging to that session and allowed back in. Unsolicited traffic from outside has no entry → dropped.

Example from `netstat` on a PC:
- Local address `10.129.2.149:44642` (source IP + **dynamic/ephemeral port** chosen by the OS)
- Foreign address `172.172.255.218:443` (destination IP + **well-known port**, HTTPS)
- State `ESTABLISHED`
- Many simultaneous connections use different source ports → **multiplexing**. Return traffic is only accepted for the exact matching port pair.

### 4.3 Rules for traffic to / from the self zone

- **Self zone** = the router itself (all IP addresses on router interfaces). Traffic originating at, or addressed to, the router.
- By default, traffic to/from the self zone is **allowed (pass)** unless a zone pair + policy exists.
- With a self-zone zone-pair and policy → `inspect`.
- `zone-member` on an interface does **not** protect the router itself unless a pair using the predefined `self` zone is configured.

### 4.4 Transit traffic default rules (summary)

| Source interface in zone? | Destination interface in zone? | Zone pair exists? | Policy exists? | Result |
|---|---|---|---|---|
| Yes | Yes | **No** | n/a | **Drop** (different zones, no pair) |
| Yes | Yes | Yes | **No** | **Drop** |
| Yes | Yes | Yes | Yes | **Inspect / pass / drop per policy** |
| Yes | **No** (not in any zone) | n/a | n/a | **Drop** |
| No | No | n/a | n/a | Normal routing (no ZPF involved) |

---

## 5. Configuring a ZPF

### 5.1 Configuration considerations
1. The router **never filters traffic between interfaces in the same zone**.
2. An interface **cannot belong to multiple zones** (create a new zone + pairs for unions).
3. ZPF can coexist with Classic Firewall but **not on the same interface** – remove `ip inspect` before applying `zone-member security`.
4. Traffic can **never flow between a zoned interface and a non-zoned interface**. Applying `zone-member` causes a **temporary interruption** until the other zone-member is configured → assign interfaces **last**.
5. **Default inter-zone policy = drop all** unless the service-policy on the zone pair allows it.
6. `zone-member` does **not** protect the router itself (traffic to/from the router) unless **self zone** pairs are configured.
7. Prerequisite: the router needs the **security technology package license** (`securityk9`).

### 5.2 Step 1 – Create zones

```
Router(config)# zone security zone-name
```
```
R3(config)# zone security IN-ZONE
R3(config-sec-zone)# exit
R3(config)# zone security OUT-ZONE
R3(config-sec-zone)# exit
```
Before creating, answer: *Which interfaces go in each zone? What is each zone called? What traffic is needed, and in which direction?*

### 5.3 Step 2 – Identify traffic with a class-map

```
Router(config)# class-map type inspect [match-any | match-all] class-map-name
Router(config-cmap)# match access-group {acl-number | name}
Router(config-cmap)# match protocol protocol-name
```
- **`match-any`** – packet needs to match **at least one** criterion (logical OR).
- **`match-all`** – packet must match **all** criteria (logical AND).
- A class-map can match an **ACL** (`match access-group`) or **protocols** (`match protocol http`).

```
R3(config)# access-list 101 permit ip 192.168.3.0 0.0.0.255 any
R3(config)# class-map type inspect match-all IN-NET-CLASS-MAP
R3(config-cmap)# match access-group 101
R3(config-cmap)# exit
```
- ACL numbers **100–199 = Extended ACL**; 1–99 = Standard ACL.

### 5.3a ACL refresher
**ACL = Access Control List.** Ordered list of `permit`/`deny` statements. Processed top-down; first match wins; **implicit `deny all`** at the end. Must be **applied** (e.g., to an interface with direction in/out) to have effect. In ZPF, ACLs are *referenced by class-maps* rather than applied to interfaces.

### 5.4 Step 3 – Define an action with a policy-map

```
Router(config)# policy-map type inspect policy-map-name
Router(config-pmap)# class type inspect class-map-name
Router(config-pmap-c)# {inspect | drop | pass}
```
```
R3(config)# policy-map type inspect IN-2-OUT-PMAP
R3(config-pmap)# class type inspect IN-NET-CLASS-MAP
R3(config-pmap-c)# inspect
%No specific protocol configured in class IN-NET-CLASS-MAP for inspection. All protocols will be inspected.
R3(config-pmap-c)# exit
R3(config-pmap)# exit
```
- The `%No specific protocol configured…` message is **informational**, not an error.
- Traffic not matched by any class falls into the automatic **`class class-default`**, whose default action is **drop**.

### 5.5 Step 4 – Zone pair + attach policy

```
Router(config)# zone-pair security zone-pair-name source source-zone destination destination-zone
Router(config-sec-zone-pair)# service-policy type inspect policy-map-name
```
```
R3(config)# zone-pair security IN-2-OUT-ZPAIR source IN-ZONE destination OUT-ZONE
R3(config-sec-zone-pair)# service-policy type inspect IN-2-OUT-PMAP
R3(config-sec-zone-pair)# exit
```
- A zone pair is **unidirectional**. No pair for OUT→IN means outside-initiated traffic is dropped by default.
- Naming tip: `IN-2-OUT` = "IN **to** OUT" (2 is shorthand for "to").

### 5.6 Step 5 – Assign interfaces to zones

```
Router(config-if)# zone-member security zone-name
```
```
R3(config)# interface g0/1
R3(config-if)# zone-member security IN-ZONE
R3(config-if)# exit
R3(config)# interface s0/0/1
R3(config-if)# zone-member security OUT-ZONE
R3(config-if)# exit
R3(config)# end
R3# copy running-config startup-config
Destination filename [startup-config]?      <-- just press Enter
```

### 5.7 Reading the whole config (show run)

```
R1# show run | begin class-map
```
Output order mirrors build order: **class-map → policy-map (with `class class-default` → `drop`) → zones → zone-pair (+ service-policy) → interface `zone-member`**.

---

## 6. Verifying a ZPF

| Command | Purpose |
|---|---|
| `show policy-map type inspect zone-pair sessions` | Shows **established sessions** – proof that ZPF is working. **Most important verification command.** |
| `show run \| begin class-map` | Shows class-map, policy-map, zone-pair and interface assignments |
| `show class-map type inspect` | Displays class-maps |
| `show policy-map type inspect` | Displays policy-maps |
| `show zone security` | Displays zones and their member interfaces |
| `show zone-pair security` | Displays zone pairs |
| `show version` | Check the **license** (look for `securityk9` in *Technology Package License Information*) |

Sample session entry:
```
Number of Established Sessions = 1
Session 2519191680 (192.168.3.3:1030)=>(192.168.1.3:80) tcp SIS_OPEN/TCP_ESTAB
```
- Left side = **source IP : ephemeral port**; right side = **destination IP : service port**.
- `class-default` showing dropped packets = evidence that unwanted traffic is being blocked.
- Sessions only exist **while the connection is alive** – run the `show` command immediately after generating traffic (SSH stays open; HTTP closes quickly, so click *Go* again and re-run).

### Well-known ports seen in the lab
| Service | Port |
|---|---|
| SSH | 22 |
| HTTP | 80 |
| HTTPS | 443 |

---

## 7. Licensing (security technology package)

- ZPF commands (`zone`, `zone-pair`) only appear if the IOS has the **security license**.
- Check with `show version` → *Technology Package License Information*; `securityk9` should be **Evaluation/Permanent**, not `disable`.
- Check whether the commands exist: in global config, type `?` and look for **`zone`** and **`zone-pair`**.
- Enable on a router lacking it (model-dependent module name):
  ```
  license boot module c2900 technology-package securityk9    ! 2900-series
  ```
  1900-series (e.g., 1941) uses the `c1900` module. Use `?` to discover the right name, accept the EULA, **save and reload**, then verify with `show version`.

---

## 8. Packet Tracer Lab – Configure a ZPF (10.3.11)

**Topology:** `PC-A (server) – S1 – R1 – R2 – R3 – S3 – PC-C`
Serial WAN links between routers; static routing and passwords pre-configured. The ZPF is configured **only on R3** (edge router). Inside = R3 LAN (G0/1, 192.168.3.0/24), Outside = serial side (S0/0/1).

| Device | Interface | IP address | Mask |
|---|---|---|---|
| R1 | G0/1 | 192.168.1.1 | 255.255.255.0 |
| R1 | S0/0/0 (DCE) | 10.1.1.1 | 255.255.255.252 |
| R2 | S0/0/0 | 10.1.1.2 | 255.255.255.252 |
| R2 | S0/0/1 (DCE) | 10.2.2.2 | 255.255.255.252 |
| R3 | G0/1 | 192.168.3.1 | 255.255.255.0 |
| R3 | S0/0/1 | 10.2.2.1 | 255.255.255.252 |
| PC-A | NIC | 192.168.1.3 | 255.255.255.0 |
| PC-C | NIC | 192.168.3.3 | 255.255.255.0 |

### Lab workflow
1. **Verify baseline connectivity** (before the firewall): PC-A → PC-C ping; PC-C → R2 SSH (`ssh -l Admin 10.2.2.2`); PC-C browser → `http://192.168.1.3`.
2. **Create zones:** `IN-ZONE`, `OUT-ZONE`.
3. **Class-map:** ACL 101 (permit IP from `192.168.3.0/24` to any) → `IN-NET-CLASS-MAP` (`match-all`, `match access-group 101`).
4. **Policy-map:** `IN-2-OUT-PMAP` → class `IN-NET-CLASS-MAP` → `inspect`.
5. **Zone pair:** `IN-2-OUT-ZPAIR` (source `IN-ZONE`, destination `OUT-ZONE`) + `service-policy type inspect IN-2-OUT-PMAP`.
6. **Assign interfaces:** `g0/1` → `IN-ZONE`; `s0/0/1` → `OUT-ZONE`.
7. **Save:** `copy running-config startup-config` (press **Enter** at the filename prompt – it is not a yes/no question).
8. **Test IN → OUT (should succeed):** ping PC-A, SSH to R2, HTTP to PC-A. While the session is active run `show policy-map type inspect zone-pair sessions` on R3 and record source/destination IP and port.
9. **Test OUT → IN (should fail):** ping PC-C from PC-A, and from R2.
10. **Check Results** in Packet Tracer → target **100%**.

### Observed results
| Test | Source | Destination |
|---|---|---|
| SSH | 192.168.3.3 : ephemeral (e.g., 1027) | 10.2.2.2 : **22** |
| HTTP | 192.168.3.3 : ephemeral (e.g., 1030) | 192.168.1.3 : **80** |
| Ping PC-A → PC-C | **Fails** (blocked by ZPF) | |
| Ping R2 → PC-C | **Fails** (blocked by ZPF) | |

### Lessons learned / gotchas
- **Console password vs. enable password** are different prompts: first `User Access Verification` (console), then `enable` (privileged).
- `ping` is **not valid in global config mode** – `end` to `R3#` first.
- Config mode shows `Invalid input` for exec commands → use `do show …` or `end`.
- `Translating "end"... domain server` appears when a mistyped command at `R3#` triggers DNS lookup – press Ctrl+C / wait.
- First ping often times out (ARP) – subsequent pings succeed.
- Use `?` and **Tab** completion to discover/complete commands.
- Always copy names **exactly** (case, hyphens) – Packet Tracer's *Check Results* is name-sensitive.
- Applying `zone-member` briefly interrupts traffic → do Step 5 last.

---

## 9. Command Cheat Sheet (copy-ready template)

```
! 1. Zones
zone security IN-ZONE
 exit
zone security OUT-ZONE
 exit

! 2. Class-map (via ACL)
access-list 101 permit ip <inside-network> <wildcard> any
class-map type inspect match-all <CLASS-MAP-NAME>
 match access-group 101
 exit

! 3. Policy-map
policy-map type inspect <POLICY-MAP-NAME>
 class type inspect <CLASS-MAP-NAME>
  inspect
  exit
 exit

! 4. Zone pair
zone-pair security <ZONE-PAIR-NAME> source IN-ZONE destination OUT-ZONE
 service-policy type inspect <POLICY-MAP-NAME>
 exit

! 5. Interfaces (LAST)
interface <inside-interface>
 zone-member security IN-ZONE
 exit
interface <outside-interface>
 zone-member security OUT-ZONE
 exit
end
copy running-config startup-config

! Verify
show policy-map type inspect zone-pair sessions
show run | begin class-map
show zone security
show zone-pair security
```

---

## 10. Glossary

| Term | Meaning |
|---|---|
| **ZPF** | Zone-Based Policy Firewall |
| **Zone** | Named security boundary; interfaces are members of exactly one zone |
| **Zone pair** | Directional pair (source zone → destination zone) to which a policy is attached |
| **Class-map** | Classifies traffic (by ACL or protocol) |
| **Policy-map** | Maps classes to actions (inspect/drop/pass) |
| **Service-policy** | Command that attaches a policy-map to a zone pair |
| **C3PL** | Cisco Common Classification Policy Language (class-map / policy-map / service-policy model) |
| **Self zone** | The router itself |
| **class-default** | Built-in catch-all class; default action **drop** |
| **Stateful inspection** | Tracks connection state and allows return traffic automatically |
| **Stateless (pass)** | Forwards without tracking state |
| **Multiplexing** | Many simultaneous connections distinguished by port numbers |
| **ACL 100–199** | Extended numbered ACL |

---

## 11. Self-Check Questions

1. What is the main advantage of ZPF over a classic firewall? *(Policies apply between zones; not ACL-dependent; deny by default.)*
2. Name the three ZPF actions and their ACL equivalents. *(inspect – none; drop ≈ deny; pass ≈ permit.)*
3. Why must interfaces be assigned to zones **last**? *(Zoned↔non-zoned traffic is blocked; assigning one side interrupts service until the policy is in place.)*
4. What happens to traffic with no matching class? *(Falls to class-default → drop.)*
5. Why is return traffic allowed for `inspect` but not for `pass`? *(inspect keeps a state table; pass is stateless.)*
6. What does `show policy-map type inspect zone-pair sessions` prove? *(Active, inspected sessions – i.e., ZPF is operating.)*
7. What is the self zone? *(The router itself; traffic to/from router interfaces.)*

---

## 12. Assessment 2 Link (study notes – keep answers in your own words)

- Part 5 of the Assessment 2 practical covers **configuring and verifying a ZPF** – same five steps as this lab with different names/IP ranges.
- The ACL is **numbered 101** (extended) in the assessment brief; match the network address given in the brief.
- Zone configuration is required on **one router only** (the edge router).
- Submit **both** the written document (knowledge questions + screenshots) **and** the Packet Tracer file (`.pkt`) – markers verify configuration from the file.
- Provide verification screenshots: successful inside→outside traffic, blocked outside→inside traffic, and the `show` outputs.
- Due date is in the Subject Outline (Session 17 / Saturday).
