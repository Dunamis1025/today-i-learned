# 34. MAC Address Types & Hands-On Lab Walkthrough

## Overview

Today's study covered **Ethernet MAC Addresses** in depth — specifically the three types of MAC addresses used in Layer 2 communication (Unicast, Broadcast, and Multicast), followed by a practical lab using **Cisco Packet Tracer** to observe and analyze MAC addresses on a real switch and PC.

---

## Part 1: Theory — Three Types of Ethernet MAC Addresses

### 7.2.4 Unicast MAC Address

A **unicast MAC address** is a unique address used when a frame is sent from **one device to one specific destination device** (1-to-1 communication).

#### Key Characteristics
- The destination MAC address in the Ethernet frame header identifies a single device
- Both the destination IP address and the destination MAC address must be present in the frame
- **The source MAC address must always be a unicast address** (rule without exception)

#### How the MAC Address is Resolved
When a source device knows the destination IP address but not the MAC address, it uses one of the following protocols to discover it:

| Scenario | Protocol Used |
|----------|--------------|
| IPv4 destination | **ARP** (Address Resolution Protocol) |
| IPv6 destination | **ND** (Neighbor Discovery) |

#### Frame Structure (Unicast Example)
```
+------------------+------------------+-------------+-------------+-----------+---------+
|  Dest MAC        |  Source MAC      |  Source IP  |  Dest IP    | User Data | Trailer |
|  00-07-E9-42-AC-28 | 00-07-E9-63-CE-53 | 192.168.1.5 | 192.168.1.200 |         |         |
+------------------+------------------+-------------+-------------+-----------+---------+
```

---

### 7.2.5 Broadcast MAC Address

A **broadcast MAC address** is used when a frame must be received and processed by **every device on the Ethernet LAN** (1-to-all communication).

#### Key Characteristics
- Reserved destination MAC address: **`FF-FF-FF-FF-FF-FF`** (48 ones in binary)
- The Ethernet switch **floods** the frame out of all ports except the incoming port
- **Routers do NOT forward broadcast frames** — they are confined to the local network (broadcast domain)
- If the encapsulated data is an IPv4 broadcast packet, the destination IP address will also be a broadcast address (e.g., `192.168.1.255`)

#### Common Use Cases

| Protocol | Purpose |
|----------|---------|
| **DHCP** | A new device requests an IP address from a DHCP server |
| **ARP Request** | A device asks "Who has this IP address?" across the network |

> **Note:** Not all Ethernet broadcasts carry an IPv4 broadcast packet. For example, ARP Requests use Ethernet broadcast but do not use an IPv4 broadcast address.

---

### 7.2.6 Multicast MAC Address

A **multicast MAC address** is used when a frame is sent to a **specific group of devices** that have subscribed to a multicast group (1-to-many, but not all).

#### Key Characteristics
- Only devices that have **joined the multicast group** receive and process the frame
- **The source address must always be a unicast address** — multicast addresses can only be used as destinations
- By default, switches flood multicast frames like broadcasts — unless **multicast snooping** is configured
- Routers do not forward multicast frames unless specifically configured to do so

#### Reserved Multicast MAC Address Prefixes

| IP Version | MAC Address Prefix | IP Address Range |
|------------|--------------------|-----------------|
| IPv4 | `01-00-5E-xx-xx-xx` | `224.0.0.0` – `239.255.255.255` |
| IPv6 | `33-33-xx-xx-xx-xx` | Starts with `ff00::/8` |
| Other (STP, LLDP) | Various reserved addresses | N/A |

#### Common Use Cases
- **Routing protocols** — routers exchange topology information with each other
- **Video/audio streaming** — same content delivered efficiently to multiple subscribers

---

## Part 2: Comparison Table

| Feature | Unicast | Broadcast | Multicast |
|---------|---------|-----------|-----------|
| Recipients | 1 specific device | All devices on LAN | Subscribed group only |
| Dest MAC | Specific MAC | `FF-FF-FF-FF-FF-FF` | `01-00-5E-...` / `33-33-...` |
| Dest IP (IPv4) | Specific IP | `x.x.x.255` | `224.0.0.0`–`239.255.255.255` |
| Switch behavior | Forwards to specific port | Floods all ports | Floods all ports (unless snooping) |
| Router behavior | Forwards normally | ❌ Blocked | ❌ Blocked (unless configured) |
| Real-world analogy | Direct message (DM) | Building-wide announcement | Group chat |

---

## Part 3: Lab — View Network Device MAC Addresses (7.2.7)

### Lab Environment
- **Tool:** Cisco Packet Tracer
- **Devices:** 1x Cisco 2960 Switch (S1), 1x PC (PC-A)
- **Connection:** PC-A FastEthernet0 ↔ S1 FastEthernet0/6

### Addressing Table

| Device | Interface | IP Address | Subnet Mask |
|--------|-----------|------------|-------------|
| S1 | VLAN 1 | 192.168.1.2 | 255.255.255.0 |
| PC-A | NIC | 192.168.1.3 | 255.255.255.0 |

---

### Step 1: Configure PC-A

Set a static IP address on PC-A via Desktop → IP Configuration:
- IP Address: `192.168.1.3`
- Subnet Mask: `255.255.255.0`

---

### Step 2: Configure Switch S1 via CLI

```bash
Switch> enable
Switch# configure terminal

Switch(config)# hostname S1
S1(config)# no ip domain-lookup

S1(config)# interface vlan 1
S1(config-if)# ip address 192.168.1.2 255.255.255.0
S1(config-if)# no shutdown
S1(config-if)# end
```

#### Command Explanations

| Command | Purpose |
|---------|---------|
| `enable` | Enter privileged EXEC mode (admin mode) |
| `configure terminal` | Enter global configuration mode |
| `hostname S1` | Set the device hostname to S1 |
| `no ip domain-lookup` | Prevent the switch from doing DNS lookups on mistyped commands |
| `interface vlan 1` | Enter the configuration for VLAN 1 (the management interface) |
| `ip address 192.168.1.2 255.255.255.0` | Assign IP address to the switch |
| `no shutdown` | Bring the interface up (active) |
| `end` | Exit back to privileged EXEC mode |

---

### Step 3: Verify Connectivity

From PC-A Command Prompt:
```
ping 192.168.1.2
```

**Expected result:** 3 out of 4 packets succeed (first packet may fail due to ARP resolution delay — this is normal behavior).

---

### Step 4: View PC-A MAC Address

```
ipconfig /all
```

**Result from lab:**
```
Physical Address: 0001.6412.77E5
IPv4 Address:     192.168.1.3
Subnet Mask:      255.255.255.0
```

#### MAC Address Breakdown

| Part | Value | Meaning |
|------|-------|---------|
| OUI (first 3 bytes) | `00-01-64` | Manufacturer identifier (assigned by IEEE) |
| Serial (last 3 bytes) | `12-77-E5` | Unique device identifier assigned by manufacturer |

> In Packet Tracer, devices use simulated Cisco MAC addresses rather than real-world vendor OUIs.

---

### Step 5: View Switch S1 MAC Address

```
S1# show interfaces vlan 1
```

**Result from lab:**
```
Hardware is CPU Interface, address is 0001.632d.0cd1 (bia 0001.632d.0cd1)
Internet address is 192.168.1.2/24
```

#### MAC Address Breakdown

| Part | Value | Meaning |
|------|-------|---------|
| OUI (first 3 bytes) | `00-01-63` | Manufacturer identifier |
| Serial (last 3 bytes) | `2d-0c-d1` | Unique device identifier |

#### What is `bia`?

**bia = Burned-In Address** — the permanent MAC address physically embedded in the hardware at the time of manufacture.

- If the current MAC address **equals** the bia → the address has not been changed
- If they **differ** → the MAC address has been overridden in software (MAC spoofing)

---

### Step 6: View ARP Table on S1

```
S1# show arp
```

**Result from lab:**
```
Protocol  Address       Age (min)  Hardware Addr    Type   Interface
Internet  192.168.1.2   -          0001.632D.0CD1   ARPA   Vlan1
Internet  192.168.1.3   3          0001.6412.77E5   ARPA   Vlan1
```

#### Interpretation

| IP Address | MAC Address | Device |
|------------|-------------|--------|
| 192.168.1.2 | 0001.632D.0CD1 | S1 (switch itself) |
| 192.168.1.3 | 0001.6412.77E5 | PC-A |

The ARP table maps **Layer 3 (IP) addresses to Layer 2 (MAC) addresses**. The switch learned PC-A's MAC address dynamically when PC-A sent a ping.

---

### Step 7: View MAC Address Table on S1

```
S1# show mac address-table
```

**Result from lab:**
```
Vlan    Mac Address       Type      Ports
----    -----------       --------  -----
   1    0001.6412.77e5    DYNAMIC   Fa0/6
```

#### Interpretation

- The switch learned that **PC-A** (`0001.6412.77e5`) is reachable via **port Fa0/6**
- Type `DYNAMIC` means the switch learned this automatically by observing incoming frames
- `STATIC` entries (not shown here) are manually configured or reserved by the system (e.g., `ffff.ffff.ffff` for broadcast)

---

## Key Takeaways

1. **Every NIC has a unique MAC address** burned in by the manufacturer — it is a Layer 2 hardware identifier
2. **MAC addresses are 48 bits** (6 bytes), displayed in hexadecimal — the first 3 bytes are the OUI (manufacturer), and the last 3 bytes are the serial number
3. **Unicast** = 1-to-1, **Broadcast** = 1-to-all, **Multicast** = 1-to-group
4. **ARP** resolves IPv4 addresses to MAC addresses; **ND** does the same for IPv6
5. **Switches learn MAC addresses dynamically** by inspecting the source MAC of incoming frames and recording which port they came from — this is how they build the MAC address table
6. **Routers block both broadcast and multicast** by default — they do not forward these frame types to other networks
7. The **`bia` (Burned-In Address)** is the factory-assigned MAC address; if it matches the current address, the MAC has not been spoofed

---

## Commands Reference

| Command | Where | Purpose |
|---------|-------|---------|
| `ipconfig /all` | PC (Windows) | View IP config including MAC address |
| `ping <ip>` | PC (Windows) | Test Layer 3 connectivity |
| `show interfaces vlan 1` | Switch CLI | View switch VLAN interface details including MAC |
| `show arp` | Switch CLI | View ARP table (IP ↔ MAC mappings) |
| `show mac address-table` | Switch CLI | View MAC address table (MAC ↔ port mappings) |
