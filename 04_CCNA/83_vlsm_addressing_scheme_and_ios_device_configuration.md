# IPv4 Subnetting Notes

A study summary covering IPv4 addressing fundamentals and a full worked subnetting exercise (Cisco Packet Tracer scenario).

## 1. Public vs. Private IP Addresses

- **Public IP addresses** are internet-facing and reachable from outside — used for things like web servers that outside users need to reach.
- **Private IP addresses** are used freely only within an internal network (a company or home) and are not directly reachable from the internet.
- Inside an organization, most internal devices (that don't need external access) are assigned private IPs generously, while only a limited number of public IPs are used for external-facing resources.
- Private IP space can be subdivided into smaller blocks to match the size of each internal network, avoiding wasted addresses.

## 2. The Inverse Relationship: Networks vs. Hosts per Network

When subnetting a network, **the number of possible networks and the number of hosts per network are inversely related**:

- Splitting a network into **more, smaller subnets** → **fewer** usable host addresses per subnet.
- Needing **more hosts** in a subnet → **fewer** subnets can be created from the same address block.

This happens because the total number of address bits in an octet (or address block) is fixed. Borrowing bits from the host portion to create more network/subnet distinctions directly shrinks the number of bits left to number hosts.

**Example:** For a base 24-bit network (24 network bits, 8 host bits):

| Subnet bits borrowed | Number of subnets | Hosts per subnet |
|---|---|---|
| 0 | 1 | 254 |
| 1 | 2 | 126 |
| 2 | 4 | 62 |
| 3 | 8 | 30 |

As subnet count goes up, hosts per subnet goes down — a direct trade-off.

## 3. Prefix Length and Subnet Mask Calculation

### Example: /25

- Starting from a /24 (24 network bits, 8 host bits), borrowing **1 bit** from the host portion gives a **/25** prefix.
- The last octet in binary becomes `10000000` → decimal **128**.
- Resulting subnet mask: **255.255.255.128**.
- Number of subnets created: borrowing 1 bit → 2¹ = **2 subnets**.
- Addresses per subnet: 256 ÷ 2 = **128 addresses**.
- Usable hosts per subnet: 128 − 2 (network address + broadcast address) = **126 hosts**.

### Example: /22 (host portion size)

- IPv4 addresses are 32 bits total. A **/22** prefix means the first 22 bits are the network portion.
- Remaining bits = 32 − 22 = **10 bits** → this is the **host portion**.
- These 10 host bits are what distinguish individual devices within that network.

### General rule

- **Subnets created** = 2^(number of borrowed bits)
- **Usable hosts per subnet** = 2^(remaining host bits) − 2
  - Minus 2 accounts for:
    - The **network address** (all host bits = 0) — identifies the subnet itself, not assignable to a device.
    - The **broadcast address** (all host bits = 1) — used to send to all devices on that subnet, not assignable to a device.

## 4. Variable-Length Subnetting (VLSM) — Matching Subnet Size to Need

Not every subnet in a network has to be the same size. A common real-world design is a **headquarters + multiple branch offices**, each needing a different number of hosts:

- HQ: 40 devices
- Branch 1: 25 devices
- Branch 2: 30 devices
- Branch 3: 10 devices
- Branch 4: 15 devices

Rather than using one fixed subnet size for everyone (which would waste addresses on smaller sites), each site is assigned a subnet sized just large enough for its needs (e.g., `172.16.0.0/26` for one site, a different prefix for another). This is called **VLSM (Variable Length Subnet Masking)** — dividing the same address block into differently-sized pieces, so addresses aren't wasted.

There is no single fixed rule for how to split a network — administrators design the split based on:
- Organization size
- Number of devices needed per department/site
- Room for future growth

## 5. Worked Example — Packet Tracer Subnetting Scenario

**Given:** Network `192.168.100.0/24`. Topology: R1 and R2, each with 2 LANs (4 LANs total, 25 hosts required each) plus a serial WAN link between R1 and R2.

### Step 1: Determine subnets needed

- 4 LANs + 1 WAN link (R1↔R2) = **5 subnets needed**.
  - Note: the serial (WAN) link between two routers is also a network and needs its own subnet — even though it only connects two routers (no PCs/switches), each end needs an IP address.

### Step 2: Bits to borrow

- Need 2ⁿ ≥ 5 → n = 3 (2³ = 8 ≥ 5). **Borrow 3 bits.**

### Step 3: Subnets created & hosts per subnet

- Subnets created: 2³ = **8**
- Host bits remaining: 8 − 3 = 5
- Usable hosts per subnet: 2⁵ − 2 = **30** (meets the 25-host requirement)

### Step 4: New subnet mask

- Last octet borrowed bits: `111` (3 bits) + `00000` (5 host bits) = `11100000`
- Decimal: 128 + 64 + 32 = **224**
- New subnet mask: **255.255.255.224** (/27)

### Step 5: Subnet table (first 5 subnets used)

| Subnet | Subnet Address | First Usable Host | Last Usable Host | Broadcast Address |
|---|---|---|---|---|
| 0 | 192.168.100.0 | 192.168.100.1 | 192.168.100.30 | 192.168.100.31 |
| 1 | 192.168.100.32 | 192.168.100.33 | 192.168.100.62 | 192.168.100.63 |
| 2 | 192.168.100.64 | 192.168.100.65 | 192.168.100.94 | 192.168.100.95 |
| 3 | 192.168.100.96 | 192.168.100.97 | 192.168.100.126 | 192.168.100.127 |
| 4 | 192.168.100.128 | 192.168.100.129 | 192.168.100.158 | 192.168.100.159 |

(Subnets 5–7 exist mathematically — 160, 192, 224 — but aren't needed for this topology. 256+ is out of range since one octet only goes 0–255.)

### Step 6: Subnet assignment

- Subnet 0 → R1 G0/0 LAN (PC1/S1)
- Subnet 1 → R1 G0/1 LAN (PC2/S2)
- Subnet 2 → R2 G0/0 LAN (PC3/S3)
- Subnet 3 → R2 G0/1 LAN (PC4/S4)
- Subnet 4 → R1↔R2 WAN link

### Step 7: Addressing rules and final table

- **Routers**: first usable address in each connected subnet (R1 also gets the first usable on the WAN link; **R2 gets the last usable on the WAN link**).
- **Switches**: second usable address in their LAN subnet + default gateway = that LAN's router IP.
- **PCs**: last usable address in their LAN subnet + default gateway = that LAN's router IP.

| Device | Interface | IP Address | Subnet Mask | Default Gateway |
|---|---|---|---|---|
| R1 | G0/0 | 192.168.100.1 | 255.255.255.224 | — |
| R1 | G0/1 | 192.168.100.33 | 255.255.255.224 | — |
| R1 | S0/0/0 | 192.168.100.129 | 255.255.255.224 | — |
| R2 | G0/0 | 192.168.100.65 | 255.255.255.224 | — |
| R2 | G0/1 | 192.168.100.97 | 255.255.255.224 | — |
| R2 | S0/0/0 | 192.168.100.158 | 255.255.255.224 | — |
| S1 | VLAN 1 | 192.168.100.2 | 255.255.255.224 | 192.168.100.1 |
| S2 | VLAN 1 | 192.168.100.34 | 255.255.255.224 | 192.168.100.33 |
| S3 | VLAN 1 | 192.168.100.66 | 255.255.255.224 | 192.168.100.65 |
| S4 | VLAN 1 | 192.168.100.98 | 255.255.255.224 | 192.168.100.97 |
| PC1 | NIC | 192.168.100.30 | 255.255.255.224 | 192.168.100.1 |
| PC2 | NIC | 192.168.100.62 | 255.255.255.224 | 192.168.100.33 |
| PC3 | NIC | 192.168.100.94 | 255.255.255.224 | 192.168.100.65 |
| PC4 | NIC | 192.168.100.126 | 255.255.255.224 | 192.168.100.97 |

> **Key gotcha caught during the exercise:** Subnet 2's second usable address had to be `.66` for S3, not `.65` — because `.65` was already assigned to R2's G0/0 interface. Every device in the same subnet must have a unique IP.

## 6. Configuring the Devices in Cisco IOS (Packet Tracer CLI)

### Router interface configuration (e.g., R1)

```
R1>enable
R1#configure terminal
R1(config)#interface gigabitEthernet 0/0
R1(config-if)#ip address 192.168.100.1 255.255.255.224
R1(config-if)#no shutdown
R1(config-if)#exit
R1(config)#interface gigabitEthernet 0/1
R1(config-if)#ip address 192.168.100.33 255.255.255.224
R1(config-if)#no shutdown
R1(config-if)#exit
R1(config)#exit
R1#copy running-config startup-config
```

- `configure terminal` → enters global configuration mode.
- `interface <name>` → enters interface configuration mode for a specific port.
- `ip address <ip> <mask>` → assigns the IP and subnet mask.
- `no shutdown` → activates the interface (router interfaces are administratively down by default).
- `copy running-config startup-config` → saves the config so it survives a reboot.

### Switch configuration (e.g., S3)

Switches use a **VLAN 1 interface** for their management IP, plus a separately configured default gateway:

```
Switch>enable
Switch#configure terminal
Switch(config)#interface vlan 1
Switch(config-if)#ip address 192.168.100.66 255.255.255.224
Switch(config-if)#no shutdown
Switch(config-if)#exit
Switch(config)#ip default-gateway 192.168.100.65
```

Note: `ip default-gateway` is set in **global config mode**, not interface mode.

### PC configuration (GUI, not CLI)

Via **Desktop → IP Configuration**, select **Static** and enter:
- IPv4 Address: e.g., `192.168.100.126`
- Subnet Mask: `255.255.255.224`
- Default Gateway: e.g., `192.168.100.97`

## 7. Verifying Connectivity

Per the exercise instructions, connectivity can only be verified from R1, S3, and PC4 (the devices that were manually configured), but every IP address in the addressing table should be pingable from them:

```
ping 192.168.100.1
ping 192.168.100.33
ping 192.168.100.129
... (etc. for every device in the table)
```

Successful replies (`Reply from ...`) confirm the addressing scheme, interface configuration, and routing (EIGRP, pre-configured) are all working correctly end-to-end.

## 8. Quick Reference: Powers of 2

Useful for calculating subnet/host counts:

```
2^1  = 2
2^2  = 4
2^3  = 8
2^4  = 16
2^5  = 32
2^6  = 64
2^7  = 128
2^8  = 256
```

Sum of all bit values in an octet (1+2+4+...+128) = 255, which is why a single octet's maximum decimal value is 255 (0–255 = 256 total values).
