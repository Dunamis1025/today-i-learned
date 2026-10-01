# Day 08: IPv4 Addressing (Part 2) — Host Count Calculations & Configuring IP Addresses on a Cisco Router

> Detailed English summary of Jeremy's IT Lab CCNA 200-301 video **"Free CCNA | IPv4 Addressing (Part 2)"** — based on the user's Gemini-generated Korean notes, expanded, translated, and gap-filled with additional explanations. Continues directly from `12_day07_ipv4_addressing_part1.md` (Day 07), applying the network/host/prefix concepts from Part 1 to worked examples across all three usable classes, then moving into actual Cisco IOS router interface configuration.

---

## 1. IPv4 Address Range & Usable Host Count — The General Formula

This section builds directly on Day 07's concepts (network portion, host portion, Network Address, Broadcast Address) by turning them into a **reusable formula** and applying it across Class A, B, and C.

### The Formula

```
Usable hosts = 2ⁿ − 2
```

Where **n = number of host bits** (the bits remaining *after* the prefix/network portion).

**Why subtract 2?** Because, as established in Day 07, every network reserves exactly two addresses that can never be assigned to an actual device:
- The **Network Address** (all host bits = 0) — sits at the very beginning of the range.
- The **Broadcast Address** (all host bits = 1) — sits at the very end of the range.

So out of the 2ⁿ total addresses a network's host bits can represent, exactly 2 are reserved, leaving 2ⁿ − 2 usable for real hosts.

> **Added clarification — "usable" vs. "total" addresses:** it's worth being precise about terminology here, since CCNA questions frequently test this distinction: **total addresses** in a network = 2ⁿ (includes the network and broadcast addresses); **usable host addresses** = 2ⁿ − 2 (excludes them). A question asking "how many addresses does this network contain?" wants 2ⁿ; a question asking "how many hosts can you actually assign?" wants 2ⁿ − 2. Mixing these up is one of the most common subnetting mistakes.

---

## 2. Worked Example 1: Class C Network (`192.168.1.0/24`)

| Item | Value |
|------|-------|
| Prefix | `/24` |
| Host bits (n) | 8 (the last octet) |
| Total addresses (2⁸) | 256 (0–255) |
| **Usable hosts (2⁸ − 2)** | **254** |
| Network Address | `192.168.1.0` (all host bits = 0) |
| First usable address | `192.168.1.1` (Network Address + 1) |
| Last usable address | `192.168.1.254` (Broadcast Address − 1) |
| Broadcast Address | `192.168.1.255` (all host bits = 1) |

> **Added clarification — the pattern of "Network Address + 1" and "Broadcast Address − 1":** this is a useful shortcut worth internalizing as its own rule: the **first usable host address is always exactly one number after the Network Address**, and the **last usable host address is always exactly one number before the Broadcast Address**. You never need to recompute the whole range from scratch — once you know the Network and Broadcast addresses, the usable range is everything strictly in between them.

---

## 3. Worked Example 2: Class B Network (`172.16.0.0/16`)

| Item | Value |
|------|-------|
| Prefix | `/16` |
| Host bits (n) | 16 (the last two octets) |
| Total addresses (2¹⁶) | 65,536 |
| **Usable hosts (2¹⁶ − 2)** | **65,534** |
| Network Address | `172.16.0.0` |
| First usable address | `172.16.0.1` |
| Last usable address | `172.16.255.254` |
| Broadcast Address | `172.16.255.255` |

> **Added clarification — why the last usable address looks like `...255.254` and not just `...0.254`:** because the host portion now spans **two full octets** (16 bits), "all host bits = 1" means *both* of those octets become `255`, and then subtracting 1 (for the usable range) only affects the very last bit — turning the final `255` into `254`. This is a common point of confusion: students sometimes expect the last usable address to look like `172.16.254.255`, but because binary counting fills the *rightmost* bit first, the "−1" always applies to the last octet, not the second-to-last one.

---

## 4. Worked Example 3: Class A Network (`10.0.0.0/8`)

| Item | Value |
|------|-------|
| Prefix | `/8` |
| Host bits (n) | 24 (the last three octets) |
| Total addresses (2²⁴) | 16,777,216 |
| **Usable hosts (2²⁴ − 2)** | **16,777,214** |
| Network Address | `10.0.0.0` |
| First usable address | `10.0.0.1` |
| Last usable address | `10.255.255.254` |
| Broadcast Address | `10.255.255.255` |

> **Added clarification — `10.0.0.0/8` is a private address range:** this particular example isn't a random choice — `10.0.0.0/8` is one of the three blocks reserved by RFC 1918 for **private (internal) networks**, alongside `172.16.0.0/12` and `192.168.0.0/16` (which is why the Class B and Class C examples above also happen to be private ranges). Private addresses aren't routable on the public internet and are what most home and corporate LANs actually use internally — this is background CCNA material will very likely expand on later (NAT, private vs. public addressing), but it's worth noting now since all three worked examples in this video happen to come from these reserved blocks.

---

## 5. Configuring an IP Address on a Cisco Router Interface (CLI)

### ① Checking Interface Status Before Configuration

```
Router> enable
Router# show ip interface brief
```
(Short form: `sh ip int br`)

This command gives a **one-line summary of every interface** on the router, showing:

| Column | Meaning |
|--------|---------|
| **IP Address** | The assigned IP (shows `unassigned` before configuration) |
| **Status** (Layer 1) | `up` if the cable is connected and the device on the other end is powered on; `administratively down` if an administrator has manually disabled it |
| **Protocol** (Layer 2) | Shows `up` only once Layer 1 is already `up` |

> **Added clarification — why Cisco router interfaces start out "administratively down" by default:** unlike switch ports (which are typically enabled out of the box), **router interfaces ship in a shutdown state by default** as a security/safety measure — an unconfigured interface with no IP address shouldn't be passing traffic, so Cisco defaults it to off until an administrator deliberately configures and enables it. This is different behavior from what was seen on switches in earlier labs (Day 04–06), where interfaces generally came up automatically once a cable was plugged in — router interfaces require the extra explicit `no shutdown` step covered below.

> **Added clarification — Layer 1 vs. Layer 2 status, and why Protocol depends on Status:** "Status" reflects the **physical** connection (is there electrical/optical signal present — is a cable plugged in, is the far end powered on?), while "Protocol" reflects whether the **data link layer** protocol running over that physical connection is functioning correctly. Protocol can never be `up` if Status is `down` — there's no point running a Layer 2 protocol over a connection that doesn't even have a working physical signal — but Status can be `up` while Protocol is still `down` in some troubleshooting scenarios (e.g., a Layer 2 encapsulation mismatch between two routers). This Layer 1/Layer 2 distinction mirrors exactly what was covered for switches in Day 05's SFD/synchronization discussion, just applied to a router's physical interfaces instead.

### ② Step-by-Step Interface Configuration

```
Router> enable
Router# configure terminal
Router(config)# interface gigabitethernet 0/0
Router(config-if)# ip address 10.255.255.255 255.0.0.0
Router(config-if)# no shutdown
```

| Step | Command | Short form | What it does |
|------|---------|------------|------------------|
| 1 | `enable` | `en` | Enter Privileged EXEC mode |
| 2 | `configure terminal` | `conf t` | Enter Global Configuration mode |
| 3 | `interface gigabitethernet 0/0` | `int g0/0` | Enter Interface Configuration mode for a specific interface |
| 4 | `ip address 10.255.255.255 255.0.0.0` | — | Assign an IP address and its subnet mask to this interface |
| 5 | `no shutdown` | `no shut` | **Activate** the interface (undo its default shutdown state) |

> **Added clarification — the CLI mode hierarchy this uses (connecting back to Day 04):** this sequence adds one more level on top of the mode hierarchy first introduced in Day 04's Basic Device Security lab (`Router>` → `Router#` → `Router(config)#`). **Interface Configuration mode** (`Router(config-if)#`) is a sub-mode *inside* Global Configuration mode, specific to whichever interface you just entered with the `interface` command — commands typed here (like `ip address` and `no shutdown`) apply only to that one interface, not the router as a whole.

> **Added clarification — why `no shutdown` is necessary:** as noted above, a router interface is shut down by default. Assigning an IP address with the `ip address` command does **not** automatically turn the interface on — you still need the separate `no shutdown` command to bring both Layer 1 and Layer 2 up. Forgetting this step is an extremely common beginner mistake in Packet Tracer labs: the IP address will show as configured in `show ip interface brief`, but the Status/Protocol columns will still read `administratively down / down` until `no shutdown` is entered, and the interface won't actually pass any traffic.

> **Added clarification — the subnet mask argument isn't optional:** note that the `ip address` command takes **two** arguments — the IP address itself, *and* the subnet mask (`255.0.0.0` in this example, matching the `/8` prefix used in Section 4's Class A worked example). Unlike some other networking contexts where a prefix length alone is enough, Cisco IOS's `ip address` command specifically requires the subnet mask written out in dotted-decimal form (not CIDR notation) — this is the same subnet mask notation covered in Day 07.

---

## 6. Useful Interface Verification Commands

| Command | What it shows |
|---------|-------------------|
| `show ip interface brief` | Quick summary table: interface name, IP address, Status, Protocol |
| `show interfaces <interface-name>` (e.g., `show interfaces gigabitethernet 0/0`) | **Detailed** Layer 1/Layer 2 information for one specific interface, including its **MAC address (BIA — Burned-In Address)** and configured IP address |
| `show interfaces description` | Shows each interface's status alongside any administrator-written **description** text |

### Adding a Description to an Interface

```
Router(config-if)# description # Connected to SW1 Gig0/1 #
```
(Short form: `desc`)

> **Added clarification — why interface descriptions matter in practice:** a `description` is purely a human-readable label — it has **zero effect on how the interface actually functions** (it doesn't change routing, doesn't appear in packets, and isn't required for the interface to work). Its entire purpose is **documentation for whoever manages the device later** — e.g., "Connected to SW1 Gig0/1" instantly tells the next administrator (or you, six months from now) what's plugged into that port without having to physically trace the cable. This becomes extremely valuable in real production networks with dozens or hundreds of interfaces, where it would otherwise be impossible to remember what's connected where. The notes' example used `#` characters as delimiters around the description text — this is just one administrator's style convention for visually marking where the description text starts and ends; any text can follow the `description` keyword.

> **Added clarification — BIA (Burned-In Address) callback to Day 05:** the notes mention that `show interfaces <name>` reveals an interface's **MAC address, labeled as "BIA."** This directly reuses the term introduced in Day 05 — BIA (Burned-In Address) is simply another name for a MAC address, emphasizing that it's permanently assigned at the hardware manufacturing stage. Seeing it labeled "BIA" in actual Cisco CLI output (rather than just "MAC address") is a good example of where that earlier terminology shows up in real device output you'll encounter in labs and on the exam.

---

## 7. Quick Summary

- The usable host formula **2ⁿ − 2** (n = host bits) applies uniformly across all three worked examples: Class C `/24` → 254 hosts; Class B `/16` → 65,534 hosts; Class A `/8` → 16,777,214 hosts.
- For any network, the **first usable address = Network Address + 1**, and the **last usable address = Broadcast Address − 1**.
- All three worked examples (`192.168.1.0/24`, `172.16.0.0/16`, `10.0.0.0/8`) happen to be private (RFC 1918) address ranges.
- Cisco router interfaces are **administratively down by default** and require an explicit `no shutdown` command to activate, in addition to being assigned an IP address and subnet mask via `ip address <IP> <subnet mask>`.
- **Status (Layer 1)** reflects the physical connection; **Protocol (Layer 2)** can only be up if Status is also up.
- `show ip interface brief`, `show interfaces <name>`, and `show interfaces description` are the three key verification commands, revealing IP/status info, detailed Layer 1/2 info plus the interface's MAC address (BIA), and administrator-written descriptions, respectively.

---

## 8. Command / Concept Cheat Sheet

| Command | Short form | Purpose |
|---------|-------------|---------|
| `enable` | `en` | Enter Privileged EXEC mode |
| `configure terminal` | `conf t` | Enter Global Configuration mode |
| `interface gigabitethernet 0/0` | `int g0/0` | Enter Interface Configuration mode for a specific interface |
| `ip address <IP> <subnet mask>` | — | Assign an IP address + subnet mask to the current interface |
| `no shutdown` | `no shut` | Activate an interface (undo default shutdown state) |
| `description <text>` | `desc` | Attach a human-readable label to an interface (no functional effect) |
| `show ip interface brief` | `sh ip int br` | Summary table of all interfaces: IP, Status, Protocol |
| `show interfaces <name>` | — | Detailed Layer 1/2 info for one interface, including its MAC address (BIA) |
| `show interfaces description` | — | Status + description text for all interfaces |
| Usable hosts formula | — | 2ⁿ − 2, where n = number of host bits |

---

## 9. Review Questions (for self-testing / Anki)

| Question | Answer |
|----------|--------|
| What is the formula for usable host addresses in a network? | 2ⁿ − 2, where n is the number of host bits |
| Why subtract 2 in the usable hosts formula? | The Network Address and Broadcast Address can't be assigned to hosts |
| How many usable hosts does a /24 network have? | 254 |
| How many usable hosts does a /16 network have? | 65,534 |
| How many usable hosts does a /8 network have? | 16,777,214 |
| What is the Network Address of 192.168.1.0/24? | 192.168.1.0 |
| What is the first usable host address in 192.168.1.0/24? | 192.168.1.1 |
| What is the last usable host address in 192.168.1.0/24? | 192.168.1.254 |
| What is the Broadcast Address of 192.168.1.0/24? | 192.168.1.255 |
| What is the relationship between the first usable address and the Network Address? | First usable = Network Address + 1 |
| What is the relationship between the last usable address and the Broadcast Address? | Last usable = Broadcast Address − 1 |
| What command shows a quick summary of all router interfaces (IP, Status, Protocol)? | show ip interface brief (sh ip int br) |
| What does "unassigned" mean in the IP Address column? | No IP address has been configured on that interface yet |
| What does "administratively down" mean in the Status column? | The interface has been manually shut down by an administrator (or is still in its default shutdown state) |
| Are Cisco router interfaces enabled or disabled by default? | Disabled (shut down) by default |
| What command activates a router interface? | no shutdown (no shut) |
| What command assigns an IP address to an interface, and what two values does it require? | ip address <IP address> <subnet mask> |
| Can the Protocol column show "up" if Status shows "down"? | No — Protocol can only be up if Status (Layer 1) is also up |
| What command shows detailed Layer 1/2 info and the MAC address for one specific interface? | show interfaces <interface-name> |
| What is a MAC address called in Cisco's show interfaces output? | BIA (Burned-In Address) |
| What command adds a human-readable label to an interface, and does it affect functionality? | description (desc) — no functional effect, purely documentation |
| What command shows every interface's status alongside its description text? | show interfaces description |

---

## My Study Log

- [x] Watched "IPv4 Addressing (Part 2)" video (Jeremy's IT Lab)
- [x] Had Gemini summarize the video content (Korean)
- [x] Had this summary translated, expanded, and gap-filled in English
- [ ] Reviewed Day 08 Anki flashcards
- [ ] Practiced the 2ⁿ − 2 formula with additional prefix lengths (e.g., /25, /26, /27)
- [ ] Packet Tracer lab: configure IP addresses on router interfaces and verify with show commands

### Notes / Confusing Points

- (add your own notes here)
