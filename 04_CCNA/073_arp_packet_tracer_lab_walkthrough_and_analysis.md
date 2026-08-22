# ARP (Address Resolution Protocol) — Study Notes

## 1. What is ARP?

**ARP (Address Resolution Protocol)** maps a known IPv4 address to its corresponding MAC (hardware) address on a local network. Devices communicate at Layer 2 using MAC addresses, but applications and users work with IP addresses — ARP bridges that gap.

### Two core functions of ARP
1. **Resolves IPv4 addresses to MAC addresses.**
2. **Maintains a table (ARP table / ARP cache) of IPv4-to-MAC address mappings**, stored temporarily in the device's **RAM**.

---

## 2. ARP Request (Broadcast)

When a device needs to send a packet but does not know the destination's MAC address:

1. It checks its local **ARP table** for the destination IP.
2. If no entry exists, it holds the outgoing packet and generates an **ARP request**.
3. The ARP request contains:
   - Sender's own IP and MAC address
   - **Target IP address** (known)
   - **Target MAC address** (unknown — this is what's being asked)
4. The ARP request is sent as a **broadcast** (destination MAC: `FFFF.FFFF.FFFF`), so every device on the local network must inspect it.
5. A **switch floods** the broadcast frame out of every port except the one it arrived on.
6. Every device receiving the broadcast compares the **target IP** in the request against its own IP:
   - If it doesn't match → the frame is silently ignored/dropped.
   - If it matches → that device must reply.
7. **Routers do not forward (flood) ARP broadcasts** to other interfaces — ARP requests stay within the local network segment.

---

## 3. ARP Reply (Unicast)

Only the device whose IP matches the target IP sends a reply:

1. The matching device builds an **ARP reply** containing its own IP and MAC address.
2. Unlike the request, the reply is sent as a **unicast** — directly to the original requester's MAC address (learned from the request).
3. The original sender:
   - Adds the new IP–MAC mapping to its ARP table.
   - Releases the packet that was on hold and now includes the resolved MAC address as the destination in the Ethernet header.
   - Forwards the frame to the destination.

If no device responds, the data is dropped (no communication is possible).

---

## 4. ARP and Remote (Cross-Network) Communication

When the destination IP is on a **different network** than the sender:

- The sender does **not** ARP for the remote host's IP — it ARPs for its **default gateway** (local router interface) instead.
- Logic: sender compares destination IP with its own network → if different network, look up (or ARP for) the **gateway's MAC address**.
- The IP packet's destination IP stays unchanged (the remote host), but the **Ethernet frame's destination MAC** is the **gateway's MAC**, since MAC addresses change hop-by-hop while IP addresses stay the same end-to-end.
- The first packet is queued until the gateway's MAC is resolved; subsequent packets use the cached entry immediately (no delay).

---

## 5. Switch MAC Address Table vs. ARP Table

| | MAC Address Table | ARP Table |
|---|---|---|
| Used by | Switches (Layer 2 devices) | Any IP-capable device (PCs, routers) |
| Maps | MAC address ↔ physical port | IP address ↔ MAC address |
| Purpose | Forward frames to the correct port only | Resolve IP to MAC for Layer 2 delivery |

- A switch dynamically learns which MAC addresses are reachable via which port by inspecting incoming frames.
- **Multiple MAC addresses can appear on a single port** if multiple devices are behind an intermediate device (e.g., an Access Point bridging several wireless hosts, or another switch) connected to that port.
- Routers with only routed interfaces (no switching function) show an **empty MAC address table**, since routing is a Layer 3 function, not Layer 2 switching.

---

## 6. Timing & Aging

- ARP table entries are **timestamped** and automatically **removed after a period of inactivity** to keep the cache current (Windows typically ages out entries in **15–45 seconds**).
- Entries can also be **manually cleared** (e.g., `arp -d` on Windows), forcing a fresh ARP request/reply cycle on the next communication attempt.
- **Static ARP entries** can be manually configured; these do **not** expire automatically and must be removed manually.
- **IPv6** uses an equivalent process called **ICMPv6 Neighbor Discovery (ND)**, with message types analogous to ARP request/reply.

---

## 7. Useful Commands

| Device | Command | Purpose |
|---|---|---|
| Windows PC | `arp -a` | View the ARP table |
| Windows PC | `arp -d` | Clear the ARP table |
| Cisco Router | `show ip arp` | View the router's ARP table |
| Cisco Switch/Router | `show mac-address-table` | View the MAC address table |

---

## 8. Security Consideration: ARP Spoofing / Poisoning

- Because ARP requests are broadcast and trust any reply, ARP is vulnerable to **ARP spoofing (ARP poisoning)**: an attacker sends forged ARP replies associating their own MAC address with another device's (often the gateway's) IP address, allowing them to **intercept or redirect traffic**.
- High traffic volume from many simultaneous ARP broadcasts (e.g., many devices powering on at once) can also cause temporary network slowdowns.
- Mitigation: enterprise switches use **Dynamic ARP Inspection (DAI)** to validate ARP packets against trusted bindings and block malicious replies.

---

## 9. Packet Tracer Lab — "Examine the ARP Table"

**Topology:**
```
Router0 --- Switch0 --- Access Point --- 10.10.10.2 / 10.10.10.3 (wireless)
Router0 === Router1 (serial link)
Router1 --- Switch1 --- 172.16.31.2 / 172.16.31.3 / 172.16.31.4
```

### Part 1 — Examine an ARP Request (local ping: 172.16.31.2 → 172.16.31.3)

1. Cleared ARP table (`arp -d`), then pinged in Simulation mode.
2. **ARP request** observed: Destination MAC = `FFFF.FFFF.FFFF` (broadcast) — **not** a known address in the addressing table, since the sender doesn't yet know the target's MAC.
3. **Switch1 flooded the frame to all other ports** (3 copies: to the two other PCs and to the router uplink), since it's a broadcast.
4. Only **172.16.31.3** (the intended target) processed and accepted the request; the other devices (172.16.31.4, Router1) received it but dropped it since it wasn't addressed to them.
5. **ARP reply**: Source/Destination MAC addresses reversed compared to the request, and the frame changed from broadcast to **unicast** (Src MAC = 172.16.31.3's MAC, Dest MAC = 172.16.31.2's MAC).
6. After the reply, the ICMP (ping) packet resumed and completed successfully — MAC addresses of source/destination frames correctly aligned with their IP addresses.
7. `arp -a` confirmed a new dynamic entry for **172.16.31.3**.
8. **Conclusion:** an end device issues an ARP request whenever it needs to communicate with an IP address for which it has **no current MAC mapping** in its ARP cache.

### Part 2 — Examine a Switch MAC Address Table

1. Generated more traffic: `ping 172.16.31.4` (from .2) and `ping 10.10.10.3` (from 10.10.10.2) — all **4/4 replies** received for each ping.
2. `show mac-address-table` on **Switch1**: each of the three wired PCs and the router uplink had a distinct MAC-to-port mapping, matching the addressing table exactly.
3. `show mac-address-table` on **Switch0**: two different MAC addresses (10.10.10.2 and 10.10.10.3) were mapped to the **same port (Fa0/2)**.
   - **Reason:** that port connects to an **Access Point**, which bridges multiple wireless clients onto a single physical switch port. The switch learns MAC addresses per frame, not per device, so all MACs arriving via that AP get associated with the one uplink port.

### Part 3 — ARP in Remote Communications (172.16.31.2 → 10.10.10.1)

1. Pinged **10.10.10.1** (a different subnet) from 172.16.31.2 — ping succeeded (4/4, TTL=254, indicating a router hop).
2. `arp -a` showed a **new entry for 172.16.31.1** (Router1's local interface / default gateway) — **not** for 10.10.10.1.
   - **Why:** ARP only operates within the local subnet. Since 10.10.10.1 is remote, the PC resolves the **default gateway's MAC address** instead, and hands the packet to the router for further routing.
3. Cleared ARP (`arp -d`) and repeated the ping in Simulation mode — again 2 PDUs appeared (ARP request + queued ICMP).
4. Opened the ARP request PDU at Switch1: **Target IP = 172.16.31.1** (the gateway), confirming the mechanism above.
5. On **Router1**:
   - `show mac-address-table` → **empty (0 entries)**, because Router1's interfaces are routed (Layer 3) interfaces, not switch ports doing Layer 2 MAC learning.
   - `show arp` → confirmed an entry for **172.16.31.2** (dynamic, aged ~3 min) and for 172.16.31.1 itself (permanent, no age, since it's the router's own interface).
6. **If the router has to respond to a fresh ARP request**, the **first ping reply is delayed** (extra round-trip for ARP resolution) compared to subsequent pings, which use the cached MAC and complete quickly.

---

## 10. Key Takeaways

- **ARP request = broadcast; ARP reply = unicast.**
- **Switches forward frames unchanged** (Layer 2) — inbound and outbound PDU contents at a switch are identical.
- **ARP only works within the local subnet.** For remote destinations, devices resolve the **default gateway's** MAC address, not the remote host's.
- **MAC address table (switch) ≠ ARP table (IP devices)** — different layers, different purposes.
- Missing ARP entries cause a one-time **delay** on first communication; cached entries make subsequent communication instant.
- ARP entries **expire automatically** after inactivity (this is what keeps the cache accurate and prevents stale mappings) — but can also be static or manually cleared.
- ARP's broadcast/trust-based nature makes it a target for **ARP spoofing**; **Dynamic ARP Inspection (DAI)** is a common defense.
