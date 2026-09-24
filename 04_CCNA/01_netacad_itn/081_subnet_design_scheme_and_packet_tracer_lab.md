# IPv4 Addressing & Subnetting — Study Notes

Summary of concepts covered across a Networking Academy course review and a hands-on Packet Tracer lab.

---

## 1. Communication Types

- **Unicast** — one-to-one communication between a single source and a single destination device.
- **Broadcast** — one-to-all communication; a message is sent to every device on the network simultaneously. Useful but can degrade performance if excessive.
- **Multicast** — one-to-many (selective) communication; only devices that have subscribed to a specific group receive the data.

---

## 2. Public vs. Private IP Addresses

- **Public IP** — globally unique, routable on the internet.
- **Private IP** — used only inside a local network (home, office); not routable on the public internet.
- **NAT (Network Address Translation)** — because public IPv4 addresses are limited, a router translates private IPs to a public IP so internal devices can reach the internet.

### RFC 1918 Private Address Blocks

| Network Address / Prefix | Private Range |
|---|---|
| 10.0.0.0/8 | 10.0.0.0 – 10.255.255.255 |
| 172.16.0.0/12 | 172.16.0.0 – 172.31.255.255 |
| 192.168.0.0/16 | 192.168.0.0 – 192.168.255.255 |

**Common trap:** not every address starting with 172 or 192 is private — it must fall specifically in **172.16–172.31** or **192.168.x.x**. For example, 192.0.3.15 is **public** because the second octet is 0, not 168.

---

## 3. Special-Use & Legacy Addressing

- **Special-use addresses**: loopback (device testing itself), link-local (temporary self-assigned addressing when no DHCP is available).
- **Legacy classful addressing**: old system dividing addresses into fixed Classes A/B/C by network size — abandoned due to address waste.
- **Address governance**: IANA (global authority) allocates address blocks to 5 Regional Internet Registries (RIRs), which distribute to ISPs/organizations.

---

## 4. Broadcast Domains & Segmentation

- A **broadcast domain** is the set of devices that receive a broadcast message.
- **Routers block broadcasts** by default — they don't forward them to other networks, which is how broadcast domains get segmented.
- **Problem with large broadcast domains**: too many devices → excessive broadcast traffic → both individual devices and the overall network slow down.
- **Solution**: split large networks into smaller **subnets**.

---

## 5. Subnetting Fundamentals

### Why subnet?
- Reduces broadcast traffic and improves performance
- Enables security policies (which subnets can/can't talk to each other)
- Limits the blast radius of misconfigurations, hardware issues, or malicious traffic

### How subnetting works (binary logic)
- A subnet mask splits an IP address into **network bits (1s)** and **host bits (0s)**.
- Devices/routers use a **logical AND** between the IP address and subnet mask to determine the network address.
  - Example: `192.168.1.10 AND 255.255.255.0 = 192.168.1.0` (the network address)
- **Subnetting** = borrowing bits from the host portion and converting them to network (subnet) bits, done left-to-right.

### Prefix ↔ Subnet Mask Conversion
A prefix like `/26` means 26 of the 32 total bits are network bits (1s). Convert octet by octet:
- 3 full octets of 1s → 255.255.255
- 4th octet: remaining bits set to 1 (26 − 24 = 2 bits) → `11000000` = 192
- Result: **255.255.255.192**

### Effect of Borrowing Bits (from a /24 base)

| Prefix | Bits Borrowed | Subnet Mask | # Subnets (2ⁿ) | Host Bits | # Usable Hosts (2ʰ − 2) |
|---|---|---|---|---|---|
| /25 | 1 | 255.255.255.128 | 2 | 7 | 126 |
| /26 | 2 | 255.255.255.192 | 4 | 6 | 62 |
| /27 | 3 | 255.255.255.224 | 8 | 5 | 30 |
| /28 | 4 | 255.255.255.240 | 16 | 4 | 14 |
| /29 | 5 | 255.255.255.248 | 32 | 3 | 6 |
| /30 | 6 | 255.255.255.252 | 64 | 2 | 2 |

**Rule:** each additional borrowed bit **doubles** the number of subnets and **halves** the number of usable hosts per subnet (minus 2 for network + broadcast addresses). Practically, LANs rarely go beyond /30 or usable host addresses become too scarce.

### The "Magic Number" Trick
The magic number = the place value of the **last borrowed (rightmost "1") bit** in the subnet mask. It tells you the increment between subnet addresses.

- /25 → last bit in the 128's place → subnets increase by 128 (0, 128)
- /26 → last bit in the 64's place → subnets increase by 64 (0, 64, 128, 192)
- /27 → magic number 32 → subnets go 0, 32, 64, 96, 128, 160, 192, 224
- /28 → magic number 16 → subnets go 0, 16, 32, 48, 64...
- /29 → magic number 8
- /30 → magic number 4

This also works in other octets — e.g., subnetting `172.16.0.0/16` down to `/23` borrows bits into the 3rd octet, giving a magic number of 2 there (subnets: 172.16.0.0, 172.16.2.0, 172.16.4.0...) while gaining far more host bits than a same-prefix subnet in the last octet would.

### Anatomy of Each Subnet
- **Network address** = first address in the subnet (all host bits = 0) — not assignable to a device
- **Broadcast address** = last address in the subnet (all host bits = 1) — not assignable to a device
- **Usable host range** = everything in between
- Formula: broadcast address = (next subnet's start address) − 1

---

## 6. Applied Example — Packet Tracer Lab: "Subnet an IPv4 Network"

**Scenario:** Subnet `192.168.0.0/24` for a customer network with:
- LAN-A: minimum 50 hosts
- LAN-B: minimum 40 hosts
- 2 additional subnets reserved for future growth
- No VLSM — all subnets must use the same mask

### Step 1 — Determine requirements
- Largest subnet needed: **50 hosts**
- Minimum subnets needed: **4** (LAN-A + LAN-B + 2 future)

### Step 2 — Choose the mask
Cross-referencing the borrow-bit table:
- Only /25 (126 hosts) and /26 (62 hosts) satisfy the ≥50-host requirement
- Only /26 satisfies the ≥4-subnets requirement (4 subnets exactly)
- **Chosen mask: /26 → 255.255.255.192**

### Step 3 — Derive the subnets (magic number = 64)
| Subnet | Assignment |
|---|---|
| 192.168.0.0/26 | LAN-A |
| 192.168.0.64/26 | LAN-B |
| 192.168.0.128/26 | Reserved (future) |
| 192.168.0.192/26 | Reserved (future) |

### Step 4 — Assign host addresses within each subnet
Convention: router gets the **first** usable host address, switch gets the **second**, end-device (PC) gets the **last** usable host address.

**LAN-A (192.168.0.0/26, usable range .1–.62):**
| Device | Interface | IP Address | Subnet Mask | Default Gateway |
|---|---|---|---|---|
| CustomerRouter | G0/0 | 192.168.0.1 | 255.255.255.192 | N/A |
| LAN-A Switch | VLAN1 | 192.168.0.2 | 255.255.255.192 | 192.168.0.1 |
| PC-A | NIC | 192.168.0.62 | 255.255.255.192 | 192.168.0.1 |

**LAN-B (192.168.0.64/26, usable range .65–.126):**
| Device | Interface | IP Address | Subnet Mask | Default Gateway |
|---|---|---|---|---|
| CustomerRouter | G0/1 | 192.168.0.65 | 255.255.255.192 | N/A |
| LAN-B Switch | VLAN1 | 192.168.0.66 | 255.255.255.192 | 192.168.0.65 |
| PC-B | NIC | 192.168.0.126 | 255.255.255.192 | 192.168.0.65 |

### Step 5 — Device configuration (Cisco IOS CLI)

**Router:**
```
enable
configure terminal
hostname CustomerRouter
enable secret Class123
line console 0
 password Cisco123
 login
exit
interface g0/0
 ip address 192.168.0.1 255.255.255.192
 no shutdown
exit
interface g0/1
 ip address 192.168.0.65 255.255.255.192
 no shutdown
exit
```
Save configuration (must be run from privileged EXEC mode, i.e. `Router#`, not `Router(config)#`):
```
copy running-config startup-config
```
(Press Enter at the "Destination filename" prompt to accept the default.)

**Switches (management IP on VLAN1):**
```
enable
configure terminal
interface vlan 1
 ip address 192.168.0.2 255.255.255.192
 no shutdown
exit
ip default-gateway 192.168.0.1
```
(LAN-B switch uses 192.168.0.66 / gateway 192.168.0.65)

**PCs:** configured via Desktop → IP Configuration (static IP, mask, gateway) as listed in the table above.

### Step 6 — Verification (ping tests)
- PC-A → default gateway (192.168.0.1): success
- PC-B → default gateway (192.168.0.65): success
- PC-A → PC-B (cross-subnet, routed through CustomerRouter): success

All connectivity tests passed, confirming the subnetting scheme and device configuration were correct.

---

## 7. Key Takeaways / Common Pitfalls

- Not all `172.x` or `192.x` addresses are private — only 172.16–31 and 192.168.x.x qualify.
- **Network address ≠ usable host address**, and neither is the **broadcast address** — both ends of a subnet are reserved.
- The magic number (place value of the last borrowed bit) is a fast way to find subnet boundaries without full binary conversion.
- CLI mode matters: commands like `copy running-config startup-config` only work in privileged EXEC mode (`#`), not global config mode (`(config)#`) — use `exit` to step back up.
- Convention in addressing schemes: infrastructure devices (routers/switches) get addresses from the low end of the usable range; end-user devices are often placed toward the high end.
