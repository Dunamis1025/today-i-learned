# VU23218 AT2 Part 6 – SPAN, Sniffer, IDS vs IPS (+ ZBF / ACL review)

**Date:** 2026-09-06
**Unit:** VU23218 Implement network security infrastructure for an organisation (22603VIC Cert IV Cyber Security)
**Task:** Assessment Task 2, Section B, Part 6 – Configure SPAN and Monitor Traffic Using a Sniffer
**Tool:** Cisco Packet Tracer

---

## 1. Topology recap

```
PC-A Server (172.20.40.10) --Fa0/6-- S1 --Fa0/5-- R1 G0/1 (172.20.40.1)
Sniffer0 ------------------Fa0/7-- S1
R1 Se0/0/0 --1.1.1.0/30-- R2 --2.2.2.0/30-- R3 G0/1 (192.168.50.1) -- S3 -- PC-C (192.168.50.10)
```

| Subnet | Mask | Wildcard |
|---|---|---|
| LAN1 172.20.40.0/24 | 255.255.255.0 | 0.0.0.255 |
| WAN1 1.1.1.0/30 | 255.255.255.252 | 0.0.0.3 |
| WAN2 2.2.2.0/30 | 255.255.255.252 | 0.0.0.3 |
| LAN2 192.168.50.0/24 | 255.255.255.0 | 0.0.0.255 |

- OSPF process 50, area 0 on R1/R2/R3
- Hostnames include student ID (R1-100705670 etc.). Today S1 was renamed `S1-100705670` for consistency.
- S1 F0/5 is the **router-facing port** – the only exit from LAN1. Every packet between LAN1 and the rest of the network passes through it, which is why it was chosen as the SPAN source.

---

## 2. Review before starting – ZBF and ACL concepts

### 2.1 ZBF (Zone-Based Firewall) – what Part 5 was

A ZBF groups router interfaces into **zones** and controls traffic **between zones**. By default nothing can pass between zones until a zone-pair with a policy is created.

Four building blocks (audition-show analogy used in class):

| Step | Command | Role | Analogy |
|---|---|---|---|
| 1 | `access-list 101 permit ip 192.168.50.0 0.0.0.255 any` | *Who?* – identify traffic | audition list |
| 2 | `class-map type inspect match-all CMAP` + `match access-group 101` | *Name the group* | group name |
| 3 | `policy-map type inspect PMAP` → `class type inspect CMAP` → `inspect` | *What to do with the group* | mission |
| 4 | `zone-pair security ZP-IN-OUT source IN-ZONE destination OUT-ZONE` + `service-policy type inspect PMAP` | *Where it applies* – actually activates it | putting them on stage |

Then interfaces are assigned: `interface g0/1` → `zone-member security IN-ZONE`, `interface s0/0/1` → `zone-member security OUT-ZONE`.

**Zone-pair** = opening a one-way road from zone A to zone B and attaching a policy to that road. Only `ZP-IN-OUT` exists, so OUT → IN has no road at all → blocked.

### 2.2 What `inspect` really does (stateful)

Problem: the only road is IN → OUT, but a ping reply from the Server travels OUT → IN. Without help, replies would be dropped and every ping would fail.

`inspect` makes the router keep a **session table** (a notebook): "192.168.50.10 sent a ping to 172.20.40.10 – let the reply back in." When the reply arrives it is matched to the notebook entry and allowed. Traffic that starts from the outside has no entry, so it is dropped.

Analogy: a club guest orders food delivery; the bouncer writes it down and lets the delivery in. A delivery nobody ordered is turned away.

Result observed in Part 5: PC-C → Server ping succeeded; Server → PC-C ping failed 100 %.

### 2.3 ACL vs ZBF

| | ACL (Part 4) | ZBF (Part 5) |
|---|---|---|
| Scope | one interface, one direction | groups of interfaces (zones) |
| Memory | **stateless** – checks each packet against the list only | **stateful** – remembers outgoing sessions |
| Return traffic | not recognised; needs a separate rule the other way | allowed automatically by `inspect` |
| Cost | very cheap | uses CPU/RAM for the session table |
| Availability | routers and switches, no licence | routers only, needs `securityk9` |

Why ACLs are still worth learning even though ZBF is "smarter":
1. ZBF **uses** an ACL inside the class-map – no ACL, no ZBF.
2. ACLs are a general-purpose **selector** used everywhere: VPN (which traffic to encrypt), NAT, VTY restriction, QoS, route filtering.
3. Simple one-way rules (e.g. block HTTP) are cheaper with an ACL.
4. Switches and unlicensed devices only have ACLs.

Analogy: ACL = hammer, ZBF = power drill. The drill is stronger but you don't use it for every nail, and you must understand drill bits (ACLs) to use it.

### 2.4 ACL syntax breakdown

```
access-list 150 deny tcp 192.168.50.0 0.0.0.255 host 172.20.40.10 eq 80
```
- `deny` – action for matching packets
- `tcp` – protocol
- `192.168.50.0 0.0.0.255` – source network + wildcard
- `host 172.20.40.10` – single destination host
- `eq 80` – destination port **equal** to 80 (HTTP)

Port operators: `eq` (equal), `neq` (not equal), `gt` (greater than), `lt` (less than), `range a b`. In practice `eq` is almost always used. The operator after the destination address refers to the **destination** port; client source ports are random so they are rarely specified.

An ACL is a **selector / sieve**: it picks out packets that match the four conditions (src, dst, protocol, port). What happens to them (permit/deny on an interface, inspect in ZBF, encrypt in VPN) is decided by whatever *uses* the ACL. In a ZBF class-map, `permit` means "this traffic belongs to the class", not "allow it".

### 2.5 Wildcard mask

Inverse of the subnet mask. Bit `0` = must match exactly, bit `255` (all ones) = don't care.
- `192.168.50.0 0.0.0.255` → 192.168.50.0 – 192.168.50.255
- Quick calc: `255 – subnet mask octet` for each octet (255.255.255.252 → 0.0.0.3)

Why Cisco uses it: it is more flexible than a subnet mask. A wildcard can mix 0 and 255 in any position, e.g. `10.0.0.1 0.255.255.0` matches "host .1 in every 10.x.x.0 subnet", which a contiguous subnet mask can never express. ACLs are selectors, so that flexibility is useful. Used in ACLs and OSPF `network` statements.

### 2.6 securityk9 licence

Cisco 2900 routers ship with all features on the box but **locked by licence package**. `ipbase` (routing) is open; firewall/VPN/IPS features need `securityk9` (k9 = includes crypto). Symptom without it: `zone security` returns `% Invalid input` – the command is not wrong, the feature is hidden.

Fix (Packet Tracer):
```
license boot module c2900 technology-package securityk9
end
copy run start
reload
```
Also required later for VPN work on R1/R3.

---

## 3. Part 6 concepts

### 3.1 Sniffer

A packet-capture device – Packet Tracer's version of Wireshark. It shows every frame that arrives on its port.

Problem: a switch forwards frames using its **MAC address table** – each frame goes only to the port where the destination MAC lives. A Sniffer on F0/7 is never the destination of Server/R1 traffic, so nothing is sent to F0/7. (It's not that the switch "doesn't know" F0/7; F0/7 is simply not the receiver.)

### 3.2 SPAN (Switched Port Analyzer)

SPAN tells the switch: *"copy everything passing through the source port and send the copy to the destination port."*

- **Source port** – the port being watched (F0/5, router-facing)
- **Destination port** – where copies go (F0/7, Sniffer)
- The **original** frames are still forwarded normally → zero impact on communication
- Local SPAN = source and destination on the same switch

Analogy: a CCTV camera at the club entrance (F0/5) streaming to the security-room monitor (F0/7).

### 3.3 IDS vs IPS

| | IDS – Intrusion **Detection** System | IPS – Intrusion **Prevention** System |
|---|---|---|
| Placement | **out-of-band** – receives a copy (via SPAN) | **inline** – sits in the traffic path |
| Action | alert + log only | block immediately |
| Network impact | none (passive) | adds latency; device failure or a false positive can break legitimate traffic |
| Response | passive | active |

The SPAN + Sniffer setup in this lab is exactly the **IDS** deployment model: it only ever sees a copy.

---

## 4. Part 6 procedure (as performed)

### Step 1 – Add and connect the Sniffer
- End Devices → **Sniffer** → place inside LAN1 near S1
- Copper Straight-Through: Sniffer **Ethernet0** ↔ S1 **FastEthernet0/7**
- Note: this PT version names the Sniffer ports `Ethernet0 / Ethernet1`, not `Port0`.
- Wait for link lights to turn green.

### Step 2 – Configure the Sniffer (GUI tab)
- Service: **On** (on by default – STP/CDP/OSPF frames were already piling up)
- Incoming Packets: Port0
- **Show All/None** → clears all filters → **Edit Filters** → tick **ICMP** only
- **Clear** the capture list before generating test traffic

### Step 3 – SPAN on S1
```
enable
configure terminal
hostname S1-100705670
monitor session 1 source interface fastEthernet 0/5
monitor session 1 destination interface fastEthernet 0/7
end
```

### Step 4 – Verify
```
S1-100705670# show monitor session 1
Session 1
---------
Type              : Local Session
Description       : -
Source Ports      :
    Both          : Fa0/5
Destination Ports : Fa0/7
    Encapsulation : Native
          Ingress : Disabled

S1-100705670# show running-config | include monitor
monitor session 1 source interface Fa0/5
monitor session 1 destination interface Fa0/7
```
`Both` = ingress **and** egress traffic on F0/5 is mirrored.

### Step 5 – Generate ICMP and confirm capture
Test 1 – PC-C → Server: `ping 172.20.40.10` → 3/4 replies (first timeout = ARP), Sniffer captured **6 ICMP** (3 req + 3 reply), detail showed `PRO:0x01`, `SRC IP: 172.20.40.10`.

Test 2 (Appendix B method) – PC-A → R1: `ping 172.20.40.1` → 4/4 replies, Sniffer captured **8 ICMP** (4 + 4), detail showed `SRC IP: 172.20.40.1`, `TTL:255` (router-originated).

Both tests prove the copy of F0/5 traffic reaches F0/7.

### Step 6 – Save
```
copy running-config startup-config
```
+ Ctrl+S in Packet Tracer.

---

## 5. Written explanation submitted

**Purpose of SPAN**
A switch forwards frames based on its MAC address table, sending each frame only to the port where the destination device is connected. A monitoring device connected to a different port is not the destination, so it cannot see that traffic. SPAN solves this by copying the traffic passing through a source port and sending the copy to a destination port, where a Sniffer or IDS can analyse it. The original traffic is still forwarded normally, so SPAN does not affect network communication. In this activity, S1 was configured with F0/5 (the port connected to R1) as the source port and F0/7 (connected to the Sniffer) as the destination port. When PC-C (192.168.50.10) pinged the Server (172.20.40.10), both the ICMP requests and replies were captured by the Sniffer, which confirmed that the SPAN session was working correctly.

**IDS vs IPS**
IDS (Intrusion Detection System) analyses a copy of the traffic out-of-band. When it detects suspicious activity, it generates an alert and logs the event, but it does not block the traffic itself. IPS (Intrusion Prevention System), on the other hand, sits inline in the traffic path, so it can block suspicious traffic immediately as it is detected. Because of this, IDS does not affect network performance but is passive, while IPS can actively block threats but may add delay, and a device failure or a false positive can interrupt legitimate communication. The SPAN + Sniffer setup in this activity only inspects a copy of the traffic, so it works in the same way as an IDS.

---

## 6. Evidence mapping (Question ↔ screenshot)

| Question | Screenshot content |
|---|---|
| Q1 | 1-A: Sniffer GUI (Service On, ICMP filter) with Fa0/7 link visible; 1-B: S1 CLI with `monitor session` commands + `show monitor session 1` |
| Q2 | PC-C ping + Sniffer ICMP capture; PC-A → R1 ping + Sniffer capture (8 ICMP) |
| Q3 | `show monitor session 1` (reuse 1-B), `show running-config \| include monitor`, `copy run start`, Sniffer capture (reuse) |
| Written | Notepad screenshot of the explanation text + typed into the document |

Screenshot format (all parts): full window (title bar + Physical/Config/CLI tabs visible), Notepad with name + student ID, Windows clock visible.

---

## 7. Packet Tracer / environment gotchas

- **Dark mode hides labels.** With Windows dark mode, PT's *Default* colour scheme made "Service On/Off" text invisible. Fix: Options → Preferences → Interface → Color Scheme → **Classic** (no "Light" option), then restart PT. Save the .pkt first.
- Sniffer ports are `Ethernet0/1`; Service is on by default.
- Show All/None must be clicked **before** Edit Filters, otherwise all protocols stay ticked.
- Unsupported show commands in PT (from Part 5): `show class-map type inspect`, `show policy-map type inspect zone-pair` → use `show run | section class-map` / `policy-map` / `zone` instead.

## 8. Why the evidence rules are so strict

A .pkt file alone proves nothing (easy to copy). Full-window screenshots with hostname-embedded student ID + Notepad + clock prove *who* did the work, *when*, and *on which device*. VET qualifications (Cert IV) are audited, so assessors must keep verifiable evidence. It also mirrors real-world change-management practice: every config change is documented with command output and a timestamp.

---

## Quick self-test
1. What is a zone-pair? → A one-way road between two zones with a policy attached; nothing passes between zones without one.
2. Why does the ping reply get through a one-way ZBF? → `inspect` records the outgoing session and allows matching return traffic (stateful).
3. What does `eq 80` mean? → destination port equals 80 (HTTP).
4. Wildcard for /30? → 0.0.0.3.
5. Why can't the Sniffer see traffic without SPAN? → the switch only forwards frames to the destination MAC's port.
6. One key IDS/IPS difference? → IDS is out-of-band and only alerts; IPS is inline and blocks.
