# Access Control Lists (ACLs) — Standard, Extended, and Wildcard Masking

**Course:** 22603VIC – Certificate IV in Cyber Security
**Unit:** VU23218 – Implement Network Security Infrastructure for an Organisation
**Module:** 8 – Access Control Lists
**Date:** 2026-08-20

---

## 1. What is an ACL?

An **Access Control List (ACL)** is a series of IOS commands that filter packets based on information found in the packet header.

### Common uses of ACLs
- Limit network traffic to increase network performance (e.g. block video traffic)
- Provide traffic flow control (e.g. restrict routing updates to a known source)
- Provide a basic level of security for network access (e.g. restrict access to HR network)
- Filter traffic based on traffic type (e.g. permit email, deny Telnet)
- Screen hosts to permit or deny access to network services (e.g. restrict FTP/HTTP by user group)
- Provide priority to certain classes of traffic (used with QoS)

**Important limitation:** ACLs only provide a *basic* level of security. They work well alongside firewalls, IPS, and DMZ architecture, but are not a replacement for them.

### Packet Filtering — where it happens (OSI model)
- **Layer 3 (Network)** — filters based on **source/destination IP address**
- **Layer 4 (Transport)** — filters based on **port number** (TCP/UDP)

Cisco routers support both Standard and Extended ACLs to filter at these layers.

---

## 2. Numbered vs Named ACLs

### Numbered ACLs
| Range | Type |
|---|---|
| 1–99 | Standard IP access list |
| 100–199 | Extended IP access list |
| 1300–1999 | Standard IP access list (expanded range) |
| 2000–2699 | Extended IP access list (expanded range) |

The expanded ranges exist because the original 1–99 / 100–199 ranges eventually weren't enough for large networks with many ACLs.

### Named ACLs
- Preferred method — names are alphanumeric, **case sensitive**, and must be unique. Capitalising is recommended (e.g. `BLOCK-HTTP`, `NO-ACCESS`).
- Created with:
  ```
  Router(config)# ip access-list standard access-list-name
  Router(config)# ip access-list extended access-list-name
  ```
- Entering this command changes the prompt to a dedicated ACL configuration mode:
  - Standard named ACL → `Router(config-std-nacl)#`
  - Extended named ACL → `Router(config-ext-nacl)#`
- Inside this mode you can use `?` to see all available ACE options (`deny`, `permit`, `remark`, `no`, `exit`, sequence numbers, etc.)

### Key command-syntax distinction
- **Numbered ACL** → command starts with `access-list`
- **Named ACL** → command starts with `ip access-list`

---

## 3. Wildcard Masking

### Concept
A wildcard mask works like a subnet mask (uses ANDing to identify which bits to match) but the meaning of 1s and 0s is **reversed**:

| | Subnet Mask | Wildcard Mask |
|---|---|---|
| binary **1** | = match | = **ignore** |
| binary **0** | = not a match | = **must match** |

### Shortcut calculation formula
```
Wildcard Mask = 255.255.255.255 − Subnet Mask
```

### Worked examples
| Prefix | Subnet Mask | Wildcard Mask |
|---|---|---|
| /24 | 255.255.255.0 | 0.0.0.255 |
| /28 | 255.255.255.240 | 0.0.0.15 |
| /16 | 255.255.0.0 | 0.0.255.255 |

### Wildcard mask types / use cases
| Purpose | Wildcard Mask | Result |
|---|---|---|
| Match a single host | **0.0.0.0** | Every octet must match exactly — targets exactly one IP |
| Match an entire /24 subnet | **0.0.0.255** | Last octet ignored — all 254 hosts in that subnet |
| Match a range of subnets | e.g. **0.0.15.255** | Lower 4 bits of the 3rd octet ignored → covers subnets **192.168.16.0/24 through 192.168.31.0/24** (16 consecutive subnets in one rule) |
| Match all hosts | **255.255.255.255** | Every bit ignored — matches any address |

**Why the range trick works:** `15` in binary is `00001111`. The four `1` bits mean "don't care" for the lower 4 bits of that octet, so any value 0000–1111 (0–15) is accepted there. Combined with a fixed upper nibble (e.g. `0001` = 16 in binary), the matching addresses span 16 (`00010000`) through 31 (`00011111`) — a block of 16 consecutive subnets covered by a single ACE.

### Shortcut keywords
| Keyword | Replaces | Meaning |
|---|---|---|
| **host** | `0.0.0.0` | Match exactly one host address |
| **any** | `0.0.0.0 255.255.255.255` | Match any/all source addresses |

Example — these two commands are equivalent:
```
access-list 10 permit 192.168.10.10 0.0.0.0
access-list 10 permit host 192.168.10.10
```

---

## 4. ACE (Access Control Entries) and Sequence Numbers

- An **access list** is the whole rule set; each individual line inside it is an **ACE (Access Control Entry)**.
- The router processes ACEs **top to bottom, in order**. As soon as a packet matches an ACE, the router executes that action (permit/deny) and **stops** — it does not check further ACEs below it.
- ACEs are automatically assigned **sequence numbers** in increments of 10 (10, 20, 30…) — this deliberately leaves gaps so a new rule can later be inserted *between* existing entries without renumbering everything (same principle as old-style BASIC line numbers, e.g. `10 PRINT`, `20 INPUT`).
- This means **rule order matters**: more specific rules should generally go before broader ones (like `permit any`), otherwise the broad rule may catch traffic before the specific rule ever gets a chance to run.

### Example ACL and how the router evaluates it
```
Standard IP access list 5
    10 permit 192.168.1.0 0.0.0.255
    20 deny host 192.168.2.10
```
- Packet from 192.168.1.x → matches line 10 → **permitted**
- Packet from host 192.168.2.10 → doesn't match line 10 → checks line 20 → matches → **denied**
- Router does this evaluation extremely fast.

---

## 5. Standard ACL Syntax (Numbered)

```
Router(config)# access-list access-list-number {deny | permit | remark text} source [source-wildcard]
```

| Parameter | Description |
|---|---|
| access-list-number | 1–99 or 1300–1999 |
| deny / permit | action if condition matched |
| remark text | optional documentation comment, max 100 characters |
| source | source network/host to filter; use `any` for all networks, `host ip-address` for a single host, or plain IP (assumes /32 if `source-wildcard` omitted — defaults to 0.0.0.0) |
| source-wildcard | optional 32-bit wildcard mask |
| log | optional — generates a log message for the first matched packet of that ACE; useful for troubleshooting/security monitoring |

### Example
```
Router(config)# access-list 5 permit 192.168.1.0 0.0.0.255
```

---

## 6. Applying an ACL to an Interface

Creating an ACL does nothing on its own — it must be applied to a specific interface **in a specific direction** to actually affect traffic.

```
Router(config-if)# ip access-group {access-list-number | access-list-name} {in | out}
```

| Direction | Meaning |
|---|---|
| **in** | Filters traffic **entering** the router on that interface, before it is routed |
| **out** | Filters traffic **exiting** the router on that interface, after it has been routed |

**Direction is one of the most common places to make a mistake** — getting it backwards means the ACL filters the wrong traffic flow entirely, even if the ACL itself is written correctly.

### Guideline for choosing direction
- If the network attached to one specific inbound interface is the *only* source of traffic that needs filtering → apply **inbound**.
- If the same filter needs to apply to traffic arriving from *multiple* inbound interfaces before it leaves through one common outbound interface → apply **outbound** (more efficient — one ACL instead of several).

---

## 7. Removing an ACL

```
Router(config)# no access-list access-list-number
```
- Removing an ACL with `no access-list [number]` deletes **the entire ACL** (all its ACEs) — it does not selectively remove a single ACE.
- **Important:** Removing the ACL itself does **not** automatically remove the reference to it on the interface. The `ip access-group` command that applies the ACL must be removed separately.

### Correct removal sequence
```
Router(config)# interface s0/0/0
Router(config-if)# no ip access-group 11 out
Router(config)# no access-list 11
```

---

## 8. Verification / Troubleshooting Commands

| Command | Purpose |
|---|---|
| `show access-lists` | Shows all configured ACLs, their ACEs, and match counters (`N match(es)`) — counter increases each time a packet hits that ACE |
| `show access-lists [number \| name]` | Filter output to one specific ACL |
| `show run \| include interface\|access` | Filters `show running-config` output to only lines containing "interface" or "access" (the `\|` pipe symbol creates an OR condition) — quick way to find *which interface* and *which direction* an ACL is applied to, without scrolling through the entire config |

### Hands-on troubleshooting example (Packet Tracer 8.1.5 – ACL Demonstration)
**Topology:**
```
PC1 — S1 — R1 — R2 — R3 — S5 — PC4 / DNS Server
192.168.10.0/24 (PC1 side) — 192.168.11.0/24 — 192.168.30.0/24 — 192.168.31.0/24 (DNS server side)
```

**Symptom:** PC1 (on 192.168.10.0/24) could ping same-side hosts but got `Destination host unreachable` when pinging PC4 (192.168.30.12) and the DNS Server (192.168.31.12) — 100% packet loss both times.

**Diagnosis steps:**
1. Confirmed OSPF routing itself was healthy (`%OSPF-5-ADJCHG ... FULL`) — the problem wasn't a routing issue.
2. Ran `show access-lists` on R1:
   ```
   Standard IP access list 11
       10 deny 192.168.10.0 0.0.0.255 (9 match(es))
       20 permit any
   ```
   Found that ACL 11 explicitly denies all traffic originating from 192.168.10.0/24, including ICMP (ping) echoes. Match count increased with each failed ping attempt.
3. Ran `show run | include interface|access` to confirm where the ACL was applied:
   ```
   interface Serial0/0/0
    ip access-group 11 out
   access-list 11 deny 192.168.10.0 0.0.0.255
   access-list 11 permit any
   ```
   Confirmed it was applied **outbound** on Serial0/0/0 (the link toward R2/R3).
4. **Root cause:** Any traffic from PC1's subnet trying to leave R1 via Serial0/0/0 is blocked by ACE #10 before ACE #20 (`permit any`) is ever reached.
5. **Fix (removal sequence):**
   ```
   R1(config)# interface s0/0/0
   R1(config-if)# no ip access-group 11 out
   R1(config)# no access-list 11
   ```
6. Re-tested pings from PC1 to PC4 and the DNS server — expected to succeed once the ACL is removed.

---

## 9. Extended ACLs (Introduced — will be covered in more depth next week)

### Key difference from Standard ACLs
| | Standard ACL | Extended ACL |
|---|---|---|
| Filters on | Source IP address only | Source IP **and** destination IP, protocol, and port |
| Precision | Coarse | Fine-grained |

### Numbered range
100–199 or 2000–2699 (expanded)

### Full syntax
```
Router(config)# access-list access-list-number {deny | permit | remark text} protocol
  source source-wildcard [operator {port}]
  destination destination-wildcard [operator {port}]
  [established] [log]
```
Not all keywords/parameters need to be used every time — only what's relevant to the rule.

### Parameter table
| Parameter | Description |
|---|---|
| access-list-number | 100–199 or 2000–2699 |
| deny / permit | action |
| remark text | optional comment, max 100 chars |
| protocol | name or number of protocol; common keywords: `ip`, `tcp`, `udp`, `icmp`. `ip` matches all IP protocols |
| source | source network/host — `any`, `host ip-address`, or a plain IP |
| source-wildcard | optional 32-bit wildcard mask on the source |
| destination | destination network/host |
| destination-wildcard | optional 32-bit wildcard mask on the destination |

### Applying an extended ACL to an interface
Uses the exact same command as Standard ACLs:
```
Router(config-if)# ip access-group {access-list-number | access-list-name} {in | out}
```

### Port keyword options
Selecting a protocol determines which port options are available:
- `tcp` → TCP-related port options
- `udp` → UDP-specific port options
- `icmp` → ICMP-related message-type options

Ports can be specified by **name** (more readable, shows ACE intent clearly) or by **number**. Not every common port has a name option available in IOS — e.g. **SSH (22)** and **HTTPS (443)** have no name keyword and must be entered as numbers.

### Common named ports (from CLI `?` output)
| Name | Port |
|---|---|
| ftp | 21 |
| telnet | 23 |
| smtp | 25 |
| domain (DNS) | 53 |
| pop3 | 110 |
| www (HTTP) | 80 |

### Port comparison operators
| Operator | Meaning |
|---|---|
| eq | equal to a given port |
| gt | greater than a given port |
| lt | less than a given port |
| neq | not equal to a given port |
| range | a range of port numbers |

### Example — two equivalent ACEs (name vs number)
```
R1(config)# access-list 100 permit tcp any any eq www
R1(config)# access-list 100 permit tcp any any eq 80
```
Both produce exactly the same result — `www` is just the readable alias for port 80.

### Example — a port with no name alias (must use number)
```
R1(config)# access-list 100 permit tcp any any eq 443    ! HTTPS — no keyword available
```

### `established` keyword (introduced, to be expanded later in the Firewalls topic)
- Matches only **return traffic** for a connection that originated from inside the network — i.e. TCP traffic with the ACK or RST flag set.
- Concept illustrated with an example: a host sends a request from local port 12772 to a remote server at 203.123.75.6 on port 443; the reply traffic comes back addressed to port 12772 on the originating host. Because this is recognised as part of an already-established connection, it is automatically permitted.
- This tracking mechanism is referred to as a **state table** — will be discussed in more detail when covering firewalls.

### Common mistakes to watch out for when configuring ACLs
1. **Wildcard mask miscalculation** — can accidentally block/permit the wrong range of addresses.
2. **Wrong direction (`in` vs `out`)** — filters the wrong traffic flow entirely.
3. **Applied to the wrong interface** — the ACL has no effect on the traffic it was meant to filter.

**Recommended practice for complex ACLs:**
1. Write out the specifics of the policy in a text editor first.
2. Add the IOS configuration commands to accomplish those tasks.
3. Include remarks to document the ACL.
4. Copy and paste the commands onto the device (reduces typos and syntax errors).
5. Always thoroughly test the ACL to confirm it applies the desired policy correctly.

---

## Quick Command Reference

```
! Standard numbered ACL
access-list 10 permit 192.168.3.0 0.0.0.255
access-list 10 permit host 192.168.10.10        ! host keyword = 0.0.0.0 wildcard
access-list 11 permit any                        ! any keyword = match all

! Standard named ACL
ip access-list standard BLOCK-HTTP
 permit 192.168.1.0 0.0.0.255
 deny host 192.168.2.10

! Apply ACL to an interface
interface Serial0/0/0
 ip access-group 11 out

! Remove an ACL cleanly
interface Serial0/0/0
 no ip access-group 11 out
!
no access-list 11

! Verify
show access-lists
show access-lists 11
show run | include interface|access

! Extended numbered ACL example
access-list 100 permit tcp any any eq www
access-list 100 permit tcp any any eq 80
access-list 100 permit tcp any any eq 443
```

## Key Takeaways
- ACLs filter packets top-to-bottom by sequence number; first match wins, then processing stops.
- Wildcard mask = 255.255.255.255 − subnet mask; `0` = must match, `1` = ignore (opposite of subnet mask logic).
- `host` and `any` are shorthand for the two extreme wildcard masks (0.0.0.0 and 255.255.255.255/0.0.0.0-255.255.255.255).
- An ACL only affects traffic once applied to an interface with `ip access-group [number] [in|out]` — getting the direction wrong is one of the most common configuration mistakes.
- Standard ACLs filter on source IP only; Extended ACLs add destination IP, protocol, and port for much more granular control.
- `show access-lists` and `show run | include` are the two go-to commands for diagnosing why traffic is being unexpectedly blocked or allowed.
