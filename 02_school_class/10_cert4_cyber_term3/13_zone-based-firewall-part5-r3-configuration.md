# VU23218 - Assessment 2, Part 5: Zone-Based Firewall (ZFP) Configuration on R3

## Context

**Topology:**
- Server-PT "PC-A Server" (172.20.40.10/24) — connected via S1 — R1
- R1 — Se0/0/0 — 1.1.1.0/30 — Se0/0/0 — R2 (intermediate router)
- R2 — Se0/0/1 — 2.2.2.0/30 — Se0/0/1 — R3
- R3 — Gig0/1 — S3 — PC-C (192.168.50.0/24)

**Goal:** Configure and verify a Zone-Based Policy Firewall (ZFP) on **R3**, so that traffic initiated from the internal network (PC-C side) is permitted outbound, while traffic initiated from the external network (toward the Server) is blocked by default.

**Prerequisite issue solved:** The router (Cisco 2901, C2900-UNIVERSALK9-M image) initially rejected the `zone security` command (`Invalid input`). This was because the **Security (K9) technology package license** was not yet enabled. Fixed with:
```
license boot module c2900 technology-package securityk9
```
followed by a config save and `reload`. After reboot, `zone` and `zone-pair` commands became available.

---

## Step-by-step configuration on R3

### 1. Create the two security zones
```
zone security IN-ZONE
zone security OUT-ZONE
```
- **IN-ZONE** represents the internal network (PC-C side, connected via Gig0/1)
- **OUT-ZONE** represents everything reachable via the WAN interface (Se0/0/1) — including R2, R1, and ultimately the Server, even though the Server is not directly attached to R3

Key principle learned: zone membership is determined by **which network segment an interface leads to from R3's perspective**, not by which device is physically "outside." Anything reachable beyond an interface belongs to that interface's zone.

### 2. Create ACL 101 to classify internal traffic for inspection
```
access-list 101 permit ip 192.168.50.0 0.0.0.255 any
```
- This ACL does **not** itself permit/deny traffic at the interface level — instead, it classifies which traffic will later be selected for the ZFP `inspect` policy.
- 101 falls in the 100–199 range, confirming it as an **Extended ACL**.

### 3. Create a class-map and associate it with ACL 101
```
class-map type inspect match-all CMAP
 match access-group 101
```
- Groups all traffic matching ACL 101 under the name `CMAP`, so it can be referenced by name in the policy-map.

### 4. Create a policy-map with the inspect action
```
policy-map type inspect PMAP
 class type inspect CMAP
  inspect
```
- `inspect` enables **stateful inspection**: return traffic for sessions initiated from the internal zone is automatically permitted back through the firewall.
- Router noted: *"No specific protocol configured in class CMAP for inspection. All protocols will be inspected"* — expected, since ACL 101 matches all IP traffic (no protocol/port restriction was required).

### 5. Create the zone-pair and attach the policy
```
zone-pair security ZP-IN-OUT source IN-ZONE destination OUT-ZONE
 service-policy type inspect PMAP
```
- Defines a **directional** rule: traffic from IN-ZONE → OUT-ZONE is inspected/permitted per PMAP.
- No reverse zone-pair (OUT-ZONE → IN-ZONE) was created — by ZFP's default-deny behavior, any traffic direction without an explicit zone-pair is automatically blocked. This is what enforces "external traffic to internal is blocked."

### 6. Assign interfaces to their zones
```
interface gig0/1
 zone-member security IN-ZONE
interface se0/0/1
 zone-member security OUT-ZONE
```

---

## Verification

### Configuration verification (used `show run | section ...` due to some `show` subcommands — e.g. `show class-map type inspect`, `show policy-map type inspect zone-pair <name>` — not being supported by the Packet Tracer IOS simulation)

```
show run | section zone
```
```
zone security IN-ZONE
zone security OUT-ZONE
zone-pair security ZP-IN-OUT source IN-ZONE destination OUT-ZONE
 service-policy type inspect PMAP
 zone-member security IN-ZONE
 zone-member security OUT-ZONE
```

```
show access-lists 101
```
```
Extended IP access list 101
    permit ip 192.168.50.0 0.0.0.255 any
```

```
show run | section class-map
```
```
class-map type inspect match-all CMAP
 match access-group 101
```

```
show run | section policy-map
```
```
policy-map type inspect PMAP
 class type inspect CMAP
  inspect
```

```
show zone security
```
```
zone IN-ZONE  → Member Interfaces: GigabitEthernet0/1
zone OUT-ZONE → Member Interfaces: Serial0/0/1
```

```
show zone-pair security
```
```
Zone-pair name ZP-IN-OUT
    Source-Zone IN-ZONE   Destination-Zone OUT-ZONE
    service-policy PMAP
```

### Traffic verification

**PC-C (192.168.50.10) → PC-A Server (172.20.40.10):**
```
ping 172.20.40.10
```
Result: first ping timed out (expected — ARP resolution delay for first packet in a new conversation), followed by 3 successful replies. **Confirms internal → external traffic is permitted.**

**PC-A Server → PC-C (192.168.50.10):**
```
ping 192.168.50.10
```
Result: 4/4 packets lost (100% loss). **Confirms external → internal traffic is blocked**, since no zone-pair exists for the OUT-ZONE → IN-ZONE direction.

---

## Key Concepts Learned

- **Zone-Based Firewall building blocks and their purpose**, summarized by analogy:
  - **ACL 101** = the audition shortlist — defines which traffic gets selected for inspection.
  - **Class-map (CMAP)** = naming/grouping the shortlisted traffic under one label.
  - **Policy-map (PMAP)** = the contract defining what action (`inspect`) applies to that group.
  - **Zone-pair (ZP-IN-OUT)** = putting that contract into effect on an actual traffic path (source zone → destination zone).

- **Directional enforcement**: ZFP only permits traffic between zones where an explicit zone-pair with a policy exists. Any direction without a defined zone-pair is denied by default — this is what makes "permit internal→external, block external→internal" work without writing an explicit deny rule.

- **Licensing gotcha**: `zone security` requires the `securityk9` technology package to be enabled and the router reloaded before ZFP commands become available.

- **Packet Tracer IOS simulation limitations**: some real-IOS `show` command variants (e.g. `show class-map type inspect`, `show policy-map type inspect zone-pair <name>`) are not implemented in Packet Tracer. Equivalent information was retrieved instead via `show run | section <keyword>`, `show zone security`, and `show zone-pair security`.
