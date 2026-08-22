# Routing Tables, Default Gateways, and Static vs. Dynamic Routing

Study notes on how hosts and routers decide where to send data.

---

## 1. How a Host Decides Where to Send Data

When a device sends data, it must first determine whether the destination is on the same network or a remote one. Destinations fall into three categories:

1. **Loopback (self)** — the device is sending data to itself (e.g., `127.0.0.1` for IPv4, `::1` for IPv6), commonly used to test the device's own network configuration.
2. **Same network (local)** — the destination device is on the same LAN, so data is delivered **directly**, with no router involved.
3. **Remote network** — the destination is on a different network, so the data must be sent to an intermediary device (a router).

---

## 2. Default Gateway

The **default gateway** is the network device — typically a router — that allows communication between different networks.

- Devices on the same local network can talk to each other directly.
- To reach anything **outside** the local network, traffic must pass through the default gateway.
- Without a configured default gateway, a device cannot communicate with outside networks at all.
- The host learns the gateway's IP address either manually or via DHCP, and routes all outbound (external) traffic to that address.

## 3. Host Routing Table

Every host keeps its own **routing table** — a list of where to send data.

- On Windows, view it with **`route print`** or **`netstat -r`** (both produce the same output).
- It shows the networks the host is directly connected to, and where the default route (gateway) points for everything else.

---

## 4. Router Routing Table

When a router receives a packet, it checks the **destination IP address** and looks for the **most specific matching entry** in its routing table to decide where to forward the packet.

A router's routing table contains three types of entries:

| Entry Type | Description |
|---|---|
| **Directly connected networks** | Networks physically attached to one of the router's interfaces |
| **Remote networks** | Networks learned either manually (static routes) or automatically via dynamic routing protocols |
| **Default route** | A fallback path used when no more specific route matches — also called the **"gateway of last resort"** |

On a Cisco IOS router, the command **`show ip route`** displays this table.

### Route Source Codes (in `show ip route` output)

| Code | Meaning |
|---|---|
| **L** | Local — the router interface's own IP address |
| **C** | Connected — a network directly attached to the router (created automatically when the interface is active) |
| **S** | Static — manually configured by an administrator (a default static route shows as **S\***, using the `0.0.0.0` network address) |
| **O** | OSPF — a remote network learned dynamically via the OSPF protocol |
| **D** | EIGRP — a remote network learned dynamically via the EIGRP protocol |

Each routing table entry may also show:
- **Administrative distance** — a trustworthiness rating comparing routes from different sources
- **Metric** — a value (e.g., hop count, bandwidth) used to determine the best path
- **Next-hop address** — the IP of the next router along the path
- **Exit interface** — which local interface to send the packet out through

---

## 5. Static vs. Dynamic Routing

### Static Routing
- Routes are **manually configured** by an administrator, specifying both the destination network and the next-hop router's IP address.
- Does **not** update automatically if the network topology changes — the administrator must manually reconfigure it.
- Best suited for **small networks** with simple, non-redundant topologies.

### Dynamic Routing
- Routers **exchange information with each other** and automatically learn/update paths.
- If the topology changes, routers detect it and recalculate new paths on their own — far less administrative overhead.
- Common protocols: **OSPF** and **EIGRP**.
- In practice, static and dynamic routing are often **used together** in the same network.

---

## 6. Dynamic Routing Protocols

### OSPF (Open Shortest Path First)
- A dynamic routing protocol where routers exchange information to build a map of the network and calculate the shortest path to each destination automatically.
- Chooses paths based primarily on link speed/bandwidth.

### EIGRP (Enhanced Interior Gateway Routing Protocol)
- A Cisco-developed dynamic routing protocol, similar in purpose to OSPF.
- Uses a **composite metric** — bandwidth, delay, reliability, and load combined — rather than a single factor.
- Internally uses an algorithm called **DUAL (Diffusing Update Algorithm)**:
  - Each router pre-calculates not only the best path (**successor**) but also a backup path (**feasible successor**).
  - If the primary path fails, the router switches to the backup **immediately**, without needing to recalculate from scratch.
  - Only if no backup path exists does the router "diffuse" queries to neighboring routers asking for a new path.
  - This gives EIGRP very fast convergence (adaptation to network changes) compared to protocols that must recalculate from scratch.

---

## 7. IPv4/IPv6 Header Recap (Layer 3 Basics)

- The network layer (OSI Layer 3) enables data exchange across networks using IPv4/IPv6.
- IP is **connectionless** and provides **"best-effort" delivery** — it doesn't guarantee delivery.
- **Encapsulation at Layer 3** adds source and destination **IP addresses** to the data.
- The **MTU (Maximum Transmission Unit)** value — passed up from the data link layer — tells the network layer the maximum size of data that can be sent at once.
- IPv4 uses a **32-bit address space**; the destination address field stays constant throughout a packet's journey, while fields like **TTL** decrease at each hop.
- IPv6's **Hop Limit** field serves the same purpose as IPv4's TTL — it decreases by 1 at each router hop, and the packet is dropped when it reaches zero.
- IPv6 was created to solve IPv4's **address depletion** problem by offering a vastly larger address space, along with a simpler header for more efficient packet handling.

---

## 8. Quiz Q&A Summary

1. **Host forwarding decisions** — Local hosts can reach each other directly without a router.
2. **Default gateway** — The default gateway address is the IP address of the router on the local network.
3. **View routing table on Windows** — `netstat -r` and `route print` (identical output).
4. **Cisco command to view routing table** — `show ip route`.
5. **Code "O" in routing table** — Route learned dynamically via OSPF.
6. **Gateway of last resort** — The default route.
7. **Static route characteristic** — Must be configured manually by an administrator.
8. **Static + dynamic routing together?** — True; commonly used in combination.
9. **Encapsulation at Layer 3 adds** — Source and destination IP addresses.
10. **How network layer uses MTU** — MTU (from the data link layer) tells the network layer the max data size it can send at once.
11. **IPv4 characteristic** — Uses a 32-bit address space.
12. **Info router uses to forward a packet** — The packet's destination IP address, checked against the routing table.
13. **Packet delivery within the same LAN** — Sent directly to the destination host, no gateway needed.
14. **Ping loopback interface** — `127.0.0.1` (IPv4 loopback address).
15. **Detecting/retransmitting missing data when lower layer is connectionless** — Upper-layer connection-oriented protocols track received data and request retransmission of missing parts.
16. **Why IPv6 was created** — To solve IPv4 address depletion by providing a much larger address space.
17. **Field routers use to forward packets** — The destination IP address.
18. **IPv4 field that stays constant during transmission** — The destination address (unlike TTL, which decreases per hop).
19. **IPv6 field used to detect expired packets** — Hop Limit (decrements by 1 per hop; packet dropped at 0).
