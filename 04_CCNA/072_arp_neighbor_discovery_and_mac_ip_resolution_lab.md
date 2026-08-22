# ARP, MAC/IP Addressing, and Packet Tracer Lab Notes

## 1. Why This Matters

Every device on a network needs a way to find other devices before it can exchange data.
Two types of addresses make this possible:

- **IP address** — identifies the *final destination*, regardless of how many networks the packet crosses.
- **MAC address** — identifies the *next physical device* the frame must reach along the path (hop-by-hop).

Manually configuring MAC-to-IP mappings on every device would be slow and error-prone, so this resolution happens automatically:

- **ARP (Address Resolution Protocol)** — used in **IPv4** to map a known IP address to a MAC address.
- **ICMPv6 Neighbor Discovery (ND)** — performs the equivalent role in **IPv6**.

## 2. How Address Resolution Works

### Same local network (LAN)
The sending device can talk to the destination directly. It looks up (or ARPs for) the **destination device's own MAC address** and uses that as the frame's destination MAC.

### Remote network (different subnet)
The destination IP is out of reach directly, so the frame is instead addressed to the **local default gateway (router) interface's MAC address**. The router:
1. Strips off the incoming Ethernet frame.
2. Examines the destination IP address to choose the best route.
3. Re-encapsulates the packet in a **new frame** with new source/destination MAC addresses appropriate for the next link.
4. Decrements the IP **TTL** by 1.

This means:

| Layer | Behavior across multiple hops |
|---|---|
| IP address (source/destination) | Stays the same end-to-end |
| MAC address | Changes at every hop/router boundary |
| TTL | Decreases by 1 at every router |

### ARP in action
The very first time a device needs to reach an IP it doesn't have a MAC address for, it broadcasts an **ARP Request** ("who has this IP?") and receives a unicast **ARP Reply**. This mapping is cached, so only the *first* packet in a conversation is delayed — this is why a first ping to a new destination can show "Request timed out" while subsequent pings succeed immediately.

## 3. Lab: Packet Tracer – Identify MAC and IP Addresses

**Goal:** Trace how MAC and IP address fields in a PDU (ping/ICMP packet) change (or don't) as it crosses different network devices, using Simulation mode.

### Part 1 — Local network communication (172.16.31.5 → 172.16.31.2)

| At Device | Dest. MAC | Src MAC | Src IPv4 | Dest IPv4 |
|---|---|---|---|---|
| 172.16.31.5 | 000C.85CC.1DA7 | 00D0.D311.C788 | 172.16.31.5 | 172.16.31.2 |
| Switch1 | 000C.85CC.1DA7 | 00D0.D311.C788 | 172.16.31.5 | 172.16.31.2 |
| Hub | 000C.85CC.1DA7 | 00D0.D311.C788 | 172.16.31.5 | 172.16.31.2 |
| 172.16.31.2 (received) | 000C.85CC.1DA7 | 00D0.D311.C788 | 172.16.31.5 | 172.16.31.2 |

**Observations:**
- Switch and Hub pass the frame through **unchanged** — neither modifies MAC or IP fields.
- The Hub broadcasts the signal out **every connected port** (172.16.31.2, .3, .4). Only 172.16.31.2 accepts it; the others reject it (shown as a red "X" in the simulation) because the destination MAC doesn't match their own.
- On the ping **reply (pong)** from 172.16.31.2, the ICMP type changes from `0x08` (Echo Request) to `0x00` (Echo Reply), and the source/destination IP addresses **swap**.

### Part 2 — Remote network communication (172.16.31.5 → 10.10.10.2)

| At Device | Dest. MAC | Src MAC | Src IPv4 | Dest IPv4 |
|---|---|---|---|---|
| 172.16.31.5 | 00D0.BA8E.741A | 00D0.D311.C788 | 172.16.31.5 | 10.10.10.2 |
| Switch1 | 00D0.BA8E.741A | 00D0.D311.C788 | 172.16.31.5 | 10.10.10.2 |
| Router (inbound) | 00D0.BA8E.741A | 00D0.D311.C788 | 172.16.31.5 | 10.10.10.2 |
| Router (outbound) | 0060.2F84.4AB6 | 00D0.588C.2401 | 172.16.31.5 | 10.10.10.2 |
| Switch0 | 0060.2F84.4AB6 | 00D0.588C.2401 | 172.16.31.5 | 10.10.10.2 |
| Access Point | 0060.2F84.4AB6 | 00D0.588C.2401 | 172.16.31.5 | 10.10.10.2 |
| 10.10.10.2 (received) | 0060.2F84.4AB6 | 00D0.588C.2401 | 172.16.31.5 | 10.10.10.2 |

**Key finding — Router behavior:**

| Field | Inbound (172 side) | Outbound (10 side) | Changed? |
|---|---|---|---|
| Dest MAC | 00D0.BA8E.741A | 0060.2F84.4AB6 | ✅ |
| Src MAC | 00D0.D311.C788 | 00D0.588C.2401 | ✅ |
| Src IP | 172.16.31.5 | 172.16.31.5 | ❌ (unchanged) |
| Dest IP | 10.10.10.2 | 10.10.10.2 | ❌ (unchanged) |
| TTL | 128 | 127 | ✅ (decremented) |

- The router is the **exact point where MAC addresses suddenly change** between the 172 network and the 10 network — because it de-encapsulates and re-encapsulates the packet for the outgoing interface.
- IP addresses never change across the entire path — this is what makes IP a true end-to-end (logical) addressing scheme, while MAC is only hop-to-hop (physical) addressing.
- Switch0 and Access Point (Layer 2 devices, wired and wireless) again pass everything through unmodified, same as Switch1/Hub in Part 1.
- Because MAC-to-IP mapping wasn't cached yet, the **first ping to 10.10.10.2 timed out** (ARP resolution delay); subsequent pings succeeded immediately once the ARP cache was populated.

## 4. Reflection Question Highlights

| # | Question | Answer |
|---|---|---|
| 3–4 | Does the Hub lose/alter MAC or IP info? | No — Hub is a Layer 1 device; it has no concept of addresses at all, it just repeats the electrical signal to every port. |
| 5–6 | Does the Access Point alter anything? | No — it's a Layer 2 device; frames pass through unchanged. |
| 7 | Highest OSI layer used by Hub/AP | Hub: Layer 1 (Physical). Access Point: Layer 2 (Data Link). |
| 8, 12 | Red "X" rejections | Occur at Hub and Switch ports where the frame's destination MAC doesn't match the receiving device — the frame is discarded, not forwarded further. |
| 13 | Where do MAC addresses suddenly change between the 10 and 172 networks? | At the **Router** — it replaces the Ethernet frame each time it forwards between interfaces. |
| 16–17 | Do IP addresses ever change/swap? | Source/Destination IP never change during forward transit, but they **swap** on the ping reply (pong), since the replying device becomes the new source. |
| 19 | Why does each router port need a different IP network? | Each interface sits on a distinct broadcast domain/subnet; unique networks per port are required for correct routing decisions. |
| 20 | If IPv6 were used instead | ARP would be replaced by ICMPv6 Neighbor Discovery (Neighbor Solicitation/Advertisement messages) to resolve MAC addresses instead of IPv4 ARP broadcasts. |

## 5. One-Line Takeaways

- **IP = where the packet is ultimately going. MAC = who gets it next.**
- **Switches, hubs, and access points (Layer 1/2)** never touch MAC or IP addresses — they just forward or repeat.
- **Routers (Layer 3)** are the only devices that rewrite MAC addresses and decrement TTL, while leaving the IP addresses untouched.
- **ARP (IPv4) / ND (IPv6)** exist purely to answer one question: *"I know your IP — what's your MAC?"*
