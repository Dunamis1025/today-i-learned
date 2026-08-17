# IPv4/IPv6 Addressing Quiz Review & Troubleshooting — Study Notes

Summary of a full practice-quiz review session (33 questions) covering IPv4 subnetting, private/reserved address ranges, IPv6 address types and autoconfiguration, and `tracert`/ICMP-based troubleshooting.

---

## 1. IPv4 Subnetting Fundamentals

### 1.1 Finding the Broadcast Address
For a network like `172.16.16.0/22`:
- `/22` = subnet mask `255.255.252.0`
- Block size in the 3rd octet = `256 - 252 = 4`
- Network range: `172.16.16.0` – `172.16.19.255`
- **Broadcast address = last address in the range = 172.16.19.255**

**General rule:** Broadcast address = the last address before the next subnet boundary (block size determines subnet boundaries).

### 1.2 Network vs. Host vs. Broadcast Address (Matching Drill)
Given an address + prefix, classify as Network / Host / Broadcast address:
- If the last portion falls exactly on a block-size boundary → **Network address**
- If it's the very last value before the next boundary → **Broadcast address**
- Anything strictly between → **Host address**

Example block sizes: `/25` → 128, `/24` → 256 (whole octet), `/28` → 16, `/27` → 32, `/26` → 64.

### 1.3 Usable Host Count
For a `/n` mask:
- Host bits = `32 - n`
- Total addresses = `2^(host bits)`
- **Usable hosts = 2^(host bits) − 2** (subtract network address and broadcast address)

Examples:
- `/26` → 6 host bits → 2^6 = 64 total → **62 usable**
- `/22` → 10 host bits → 2^10 = 1024 total → **1022 usable**

⚠️ Common trap: block size (the "magic number," e.g., 64 for `/26`) is **not** the same as usable host count. Block size = gap between subnets; usable hosts = total addresses in one subnet minus 2.

### 1.4 Finding a Subnet Mask from a Host Requirement
"Must accommodate N hosts" → find smallest host-bit count `h` such that `2^h − 2 ≥ N`.
- Example: 126 hosts → `2^7 − 2 = 126` → 7 host bits → `/25` → **255.255.255.128**

### 1.5 Creating Multiple Subnets from One Network
To create 4 subnets from `192.168.1.0/24`:
- Need `2^2 = 4` → borrow 2 bits → `/24` becomes **/26** (mask `255.255.255.192`)
- Block size = `256 − 192 = 64`
- Subnets: `.0`, `.64`, `.128`, `.192`
- **2nd usable subnet = 192.168.1.64, mask 255.255.255.192**

### 1.6 Matching Subnetwork ↔ Host Address (Practice Pattern)
Given several `/27` subnets (block size 32: `.0, .32, .64, .96...`), match each subnet to a host address that falls within its range (network address < host < broadcast address).

---

## 2. Private & Reserved IPv4 Address Ranges (RFC 1918 and others)

### 2.1 RFC 1918 Private Address Blocks — must memorize (3 blocks)
| Range | Class origin |
|---|---|
| **10.0.0.0/8** | entire Class A |
| **172.16.0.0/12** (172.16–172.31) | slice of Class B |
| **192.168.0.0/16** (192.168.0–192.168.255) | slice of Class C |

Mnemonic: A → 1 block, B → 16 blocks, C → 256 blocks (increasing granularity).

### 2.2 Addresses Often Confused with Private Ranges
| Range | Actual purpose |
|---|---|
| 169.254.0.0/16 | **Link-local / APIPA** — auto-assigned when DHCP fails; NOT private/routable, only works on the local segment |
| 100.64.0.0/14 | Carrier-Grade NAT (CGN), RFC 6598 — separate from RFC 1918 |
| 224.0.0.0–239.255.255.255 | **Multicast** range — not private unicast |
| 192.0.2.0/24 (and 198.51.100.0/24, 203.0.113.0/24) | **TEST-NET** — reserved for documentation/examples only |
| 240.0.0.0/4 | **Experimental** — reserved for future use, not used on the public Internet |
| 127.0.0.0/8 (e.g., 127.0.0.1) | **Loopback** — talks to itself, for local testing |

### 2.3 Why a Private IP "Won't Work" Across the Internet
Private (RFC 1918) addresses are not routable on the public Internet — routers drop packets with private source/destination addresses. Without VPN/NAT, two hosts using private addresses across the open Internet cannot reach each other directly.

---

## 3. IPv6 Addressing Fundamentals

### 3.1 Address Structure
- 128 bits total, written as 8 groups ("hextets") of 16 bits each, separated by `:`.
- **1 hex digit = 4 bits.** So: hex digits × 4 = bits.
  - `/64` → 64 ÷ 16 = first 4 hextets are the prefix
  - `/32` → 2 hextets
  - `/48` → 3 hextets

### 3.2 Finding the Prefix
For `2001:DB8:BC15:A:12AB::1/64` → the first 4 groups form the prefix:
**Prefix = 2001:DB8:BC15:A**

### 3.3 IPv6 Address Types by Prefix (memorize)
| Type | Prefix pattern | IPv4 rough equivalent |
|---|---|---|
| Link-local | **FE80::/10** | 169.254.x.x (APIPA) |
| Unique Local (ULA) | **FC00::/7** (includes FDFF::/7) | 192.168.x.x / private IP concept |
| Multicast | **FF00::/8** | 224.0.0.0–239.x.x.x |
| Loopback | **::1** | 127.0.0.1 |
| Global unicast | **2000::/3** | any public IP |

- **Link-local**: works only within the same physical link; cannot cross a router. Auto-generated on every interface.
- **Unique Local**: private-network equivalent, but usable across multiple links within an organization (unlike link-local).
- **Multicast**: delivered only to devices that have "joined" that multicast group — like a group chat, not everyone receives it.
- There is **no broadcast** in IPv6 — multicast replaces it entirely.

### 3.4 IPv6 Address Category Hierarchy
```
IPv6 Address
├── Unicast (1-to-1)
│    ├── Global unicast
│    ├── Link-local
│    ├── Unique local
│    └── Loopback
├── Multicast (1-to-group, "joined" members only)
└── Anycast (1-to-"nearest one" among a group sharing the same address)
```
- **"Two types of IPv6 unicast addresses" (a common exam question) = Link-local + Loopback.** Anycast and Multicast are *separate top-level categories*, not subtypes of unicast.

### 3.5 Special Multicast Addresses
| Address | Meaning |
|---|---|
| **FF02::1** | All-node multicast — every IPv6 device on the local link |
| **FF02::2** | All-router multicast |
| **FF02::1:FFxx:xxxx** | Solicited-node multicast — used by Neighbor Discovery to resolve a specific device's link-layer address (replaces IPv4 ARP), narrows the "audience" instead of broadcasting to everyone |

### 3.6 SLAAC (Stateless Address Autoconfiguration)
- Lets a host build its own global IPv6 address **without a DHCP server** and without any server tracking ("stateless" = no record kept of who has which address).
- Works via **ICMPv6 Router Advertisement (RA)** messages — the router periodically advertises the network prefix; the host uses it plus its own interface info to self-assign an address.
- **Protocol supporting SLAAC = ICMPv6** (not DHCPv6, not UDP, and "ARPv6" does not exist — ARP is replaced by ICMPv6 Neighbor Discovery Protocol in IPv6).
- **Stateless DHCPv6** ≠ what assigns the address; it only supplies extra info (e.g., DNS server) alongside SLAAC.
- **Stateful DHCPv6** = a server does assign and track addresses (opposite of stateless).

### 3.7 EUI-64
- Method for generating the 64-bit Interface ID from a device's **MAC address**.
- Process: split the 48-bit MAC in half → insert **FFFE** in the middle (48+16=64 bits) → flip the 7th bit (U/L bit) to mark global uniqueness.
- Answer to "what is used in EUI-64 to create the interface ID?" → **the MAC address of the interface.**

### 3.8 IPv6 Hierarchical Subnetting Example
Given `2001:DB8:1234:0000::/64`, if the company splits the 4th hextet ("0000", 16 bits) into Site / Sub-site / Subnet fields:
- Each hex digit = 4 bits.
- If Subnet field = 1 hex digit (4 bits) → max subnets per sub-site = **2^4 = 16**

### 3.9 IPv6 Subnetting from a Given Prefix (e.g., /48)
- Convention: the **last 64 bits are always reserved as the Interface ID** and are never subnetted.
- Formula: **subnetting bits available = 64 − (given prefix length)**
- Example: given `/48`, not touching the Interface ID → `64 − 48 = 16` subnetting bits → `2^16 = 65,536` possible subnets.

---

## 4. ICMP / Troubleshooting (Ping, Traceroute)

### 4.1 ICMP Destination Unreachable — Code Numbers (memorize)
| Code | Meaning |
|---|---|
| **0** | Network Unreachable — no path to the destination network at all |
| 1 | Host Unreachable — network reached, but the specific host wasn't found |
| 2 | Protocol Unreachable — destination can't process that protocol |
| 3 | Port Unreachable — nothing is listening on that port |

Lower code number = earlier/more fundamental failure stage.

### 4.2 ICMPv6 Time Exceeded
- Sent when a packet's **IPv6 Hop Limit** (IPv4 equivalent: TTL) is decremented to 0 and the packet must be dropped (prevents infinite routing loops).
- This is the exact mechanism `traceroute`/`tracert` exploits: it sends packets with increasing hop limits (1, 2, 3...) and records which router sends back a Time Exceeded message at each hop, building the path.

### 4.3 Default Source Address for `traceroute`
- By default, a router uses **the IP address of the outbound interface** (the interface the packet actually exits through) as the source address — not the lowest/highest configured IP, and not a loopback address.

### 4.4 Interpreting `tracert` Output for Troubleshooting
Given a `tracert` where Hop 1 succeeds (responds from the default gateway) but Hop 2 onward times out:
- The administrator should **begin troubleshooting at the last device that successfully responded** — i.e., the default gateway/router at Hop 1 — because that is the last confirmed-working point in the path. The failure could be at that router itself or in the link/device just beyond it, but investigation starts there, not further downstream.
- Rule of thumb: "the first device along the path on the same LAN as the sending host" (the default gateway) is where to start if it was the last hop to reply.

---

## 5. Quick-Reference Memorization Tables

**IPv4 special ranges:**
| Range | Purpose |
|---|---|
| 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 | Private (RFC 1918) |
| 169.254.0.0/16 | Link-local (APIPA) |
| 127.0.0.0/8 | Loopback |
| 224.0.0.0–239.255.255.255 | Multicast |
| 192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24 | TEST-NET (documentation) |
| 240.0.0.0/4 | Experimental/reserved |
| 100.64.0.0/14 | Carrier-Grade NAT |

**IPv6 special ranges:**
| Range | Purpose |
|---|---|
| 2000::/3 | Global unicast |
| FE80::/10 | Link-local |
| FC00::/7 | Unique local (ULA) |
| FF00::/8 | Multicast |
| ::1 | Loopback |

**Unicast / Multicast / Anycast / Broadcast — communication pattern analogy:**
| Type | Analogy |
|---|---|
| Unicast | 1:1 private chat |
| Multicast | Group chat (only joined members receive) |
| Anycast | Call routed to the *nearest* branch sharing one number |
| Broadcast | Mass announcement to everyone in range (not used in IPv6) |

---

## 6. Key Takeaways
- Most subnetting math (broadcast address, usable hosts, subnet mask from host count, creating N subnets) is **derivable from first principles** — no need to memorize individual answers, just the block-size method.
- Reserved/special address ranges (RFC 1918, APIPA, multicast, TEST-NET, IPv6 prefixes) are **RFC-defined constants that must be memorized**, though pairing IPv4 ↔ IPv6 equivalents (e.g., 169.254.x.x ↔ FE80::/10) makes memorization far easier.
- For `tracert`-based troubleshooting questions, the rule is: **start investigating at the last hop that successfully responded**, not the next hop that failed.
- SLAAC / EUI-64 / ICMPv6 concepts are tightly linked: SLAAC uses ICMPv6 Router Advertisements; EUI-64 (using the MAC address + FFFE) is one way the interface ID portion gets generated once the prefix is known.
