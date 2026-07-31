# Single-Area OSPFv2 — Study Notes

Summary of concepts, commands, and verification steps covered while completing
**Packet Tracer Activity 2: OSPF Routing Protocol Practice** (R1–R2 topology).

## Topology

| Device | Interface | IP Address | Subnet |
|---|---|---|---|
| PC-A | Fa0 | 192.168.10.10/24 | LAN 1 |
| R1 | Gig0/0/0 | 192.168.10.1/24 | LAN 1 |
| R1 | Gig0/0/1 | 10.1.1.1/30 | WAN |
| R2 | Gig0/0/1 | 10.1.1.2/30 | WAN |
| R2 | Gig0/0/0 | 172.16.0.1/25 | LAN 2 |
| PC-B | Fa0 | 172.16.0.10/25 | LAN 2 |

Three subnets in total:

1. `192.168.10.0/24` → subnet mask `255.255.255.0` → wildcard mask `0.0.0.255`
2. `10.1.1.0/30` → subnet mask `255.255.255.252` → wildcard mask `0.0.0.3`
3. `172.16.0.0/25` → subnet mask `255.255.255.128` → wildcard mask `0.0.0.127`

## Key Concepts

### Interface
A physical or logical connection point on a router (e.g. `GigabitEthernet0/0/0`) through
which packets enter and leave. Each interface is assigned its own IP address.

### Loopback Interface
A **virtual, software-only interface** inside a router (no physical port). It is always
"up" as long as the router is running, since there's no cable to unplug. Commonly used
for a stable Router ID or management address.
> Word origin: "loop back" — a signal that is sent and returned to its own source, rather
> than going out to another physical destination.

### OSPF (Open Shortest Path First)
A **link-state routing protocol** where each router:
1. Advertises the networks it is directly connected to (link-state information).
2. Builds a complete map of the network from all routers' advertisements.
3. Runs **Dijkstra's algorithm** independently to calculate the shortest path to every
   destination network.

Each router calculates its own routes — no central authority tells it the path.

### Dijkstra's Algorithm
An algorithm (by Edsger Dijkstra) for finding the shortest path from one node to all
other nodes in a graph, given the "cost" of each link. OSPF uses this to compute the
best route to every known network based on cumulative link cost (related to bandwidth).

### Area 0 (Backbone Area)
- OSPF divides large networks into **areas** to limit the size of the link-state
  database each router must process, and to contain the scope of recalculation when a
  change occurs (fewer routers need to re-run Dijkstra).
- **Area 0 is mandatory** and is called the **backbone** — all other areas must connect
  through it (analogy: the spine, with other areas as ribs). Within one area, detailed
  link-state info is shared fully; between areas, only **summarized** route information
  crosses the boundary (via an Area Border Router), not the full internal detail.
- For **single-area OSPF** (as in this activity), everything is simply placed in Area 0.

### Wildcard Mask
The inverse of a subnet mask, used in the `network` command to tell OSPF which
interfaces to enable. Calculated by subtracting the subnet mask from
`255.255.255.255`.

Example:
```
255.255.255.255
-  255.255.255.0   (subnet mask for /24)
-----------------
   0.  0.  0.255   (wildcard mask)
```

## Configuration Commands

### R1
```
enable
configure terminal
router ospf 10
network 192.168.10.0 0.0.0.255 area 0
network 10.1.1.0 0.0.0.3 area 0
```

### R2
```
enable
configure terminal
router ospf 10
network 172.16.0.0 0.0.0.127 area 0
network 10.1.1.0 0.0.0.3 area 0
```

**Notes:**
- `router ospf 10` starts an independent OSPF process on *that* router — it must be
  configured separately on every router (the process ID does not need to match between
  routers, though it's best practice to keep it consistent).
- The `network ... area 0` command does not configure IP addresses; it simply tells
  OSPF which already-configured interfaces to enable for routing, and which area they
  belong to.

## Verification

### 1. OSPF Adjacency
Confirmed via the system message:
```
%OSPF-5-ADJCHG: Process 10, Nbr 192.168.10.1 on GigabitEthernet0/0/1 from LOADING to FULL
```
`FULL` = the two routers have completed exchanging link-state information and are fully
adjacent neighbors.

### 2. Routing Table (`show ip route`)
Route code meanings:
- `C` = Connected (directly attached network)
- `L` = Local (the router's own exact interface IP)
- `O` = **OSPF** — a route learned dynamically via OSPF (this is the key evidence that
  OSPF is working)

R1's table showed:
```
O    172.16.0.0/25 [110/2] via 10.1.1.2
```
R2's table showed:
```
O    192.168.10.0/24 [110/2] via 10.1.1.1
```
Each router learned the path to the *other* router's LAN automatically — proof that
Dijkstra's calculation succeeded on both sides.

`variably subnetted` simply means: "this major network (e.g. 172.16.0.0/16) contains
subnets of a different (variable) prefix length than its classful default" — an
informational header line, not an error.

### 3. Connectivity Test (ping)
- `PC-A > ping 172.16.0.10` — succeeded (one initial timeout due to ARP resolution,
  common and expected on the first ping after adjacency forms)
- `PC-B > ping 192.168.10.10` — succeeded, 0% loss

Both directions were tested to rule out asymmetric routing issues.

## Outcome
Single-Area OSPFv2 was successfully configured on R1 and R2. Both routers formed a
full OSPF adjacency, dynamically learned routes to each other's LAN, and full
bidirectional connectivity between PC-A and PC-B was confirmed via ping.
