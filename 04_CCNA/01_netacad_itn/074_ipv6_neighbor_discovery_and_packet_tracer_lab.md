# IPv6 Neighbor Discovery (ND) — Study Notes

## 1. Overview

IPv6 Neighbor Discovery (ND), implemented via NDP (Neighbor Discovery Protocol), is
the IPv6 equivalent of ARP in IPv4. It resolves a known IPv6 address into the
corresponding MAC (Layer 2) address so a device can actually deliver a frame on
the local link.

## 2. The Five Core ICMPv6 ND Message Types

| Type # | Name | Abbreviation | Purpose |
|---|---|---|---|
| 133 | Router Solicitation | RS | Host asks "is there a router here?" |
| 134 | Router Advertisement | RA | Router announces itself / network config |
| 135 | Neighbor Solicitation | NS | "Who has this IPv6 address? Send me your MAC." |
| 136 | Neighbor Advertisement | NA | Reply containing the requester's MAC address |
| — | Redirect | — | Informs a host of a better next-hop |

- **Solicitation** = a request message ("to ask for").
- **Advertisement** = a response/announcement message ("to broadcast/inform").

## 3. Key IPv4 ARP vs IPv6 ND Comparison

| | ARP (IPv4) | ND (IPv6) |
|---|---|---|
| Request delivery | Broadcast (all devices) | Multicast (solicited-node group only) |
| Where irrelevant frames get dropped | Software/OS layer (NIC passes it up first) | Hardware/NIC layer (dropped immediately) |
| Overhead on unrelated hosts | Some (must inspect before discarding) | Minimal (filtered by hardware) |

**Core reason ND is more efficient:** ARP broadcasts must be handed up to software
on every host to check relevance. ND uses a **solicited-node multicast address**
derived from the target's IPv6 address, mapped to a special Ethernet multicast
MAC (`33:33:xx:xx:xx:xx`). Only NICs that have registered that multicast MAC
(because it matches one of their own IPv6 addresses) accept the frame — everyone
else discards it in hardware, without ever notifying the OS.

## 4. Broadcast vs Multicast vs Unicast

| Type | Recipients | Analogy |
|---|---|---|
| Unicast | One specific device | Direct message |
| Broadcast | Every device on the network | Announcement to a whole building |
| Multicast | Only devices in a specific group | Message to a group chat |

- ARP = broadcast (whole building hears it).
- ND = multicast (only the relevant "group," effectively narrowing to almost one device).
- "Node" = any individual device connected to the network. "Solicited-node multicast"
  = a multicast address built specifically to target one particular node.

## 5. Address Resolution Process — Same Network (Local)

1. Host A wants to send to Host C on the *same* network. It knows C's IPv6
   address but not C's MAC.
2. Host A checks its **neighbor cache** (a.k.a. neighbor table — same concept as
   an ARP table: maps IPv6 ↔ MAC). No entry found.
3. The IPv6 packet is placed **on hold**.
4. Host A builds an ICMPv6 **Neighbor Solicitation (Type 135)**:
   - Target IPv6 address = Host C's address.
   - Destination = solicited-node multicast address (e.g., `FF02::1:FFxx:xxxx`).
   - Destination MAC = corresponding multicast MAC (`33:33:...`).
5. The switch **floods** this multicast frame out all ports except the incoming one
   (switches can't selectively forward multicast without extra features like IGMP
   snooping).
6. Every NIC that receives it checks the destination MAC in hardware:
   - Uninvolved hosts/routers: MAC doesn't match anything they've registered → **discarded in hardware**, never reaches the OS.
   - Host C: the multicast MAC matches its own solicited-node multicast MAC → accepted, passed up to IPv6/ICMPv6 processing.
7. Host C sees the Target Address in the NS matches its own global unicast
   address → it is the target.
8. Host C adds Host A's IPv6+MAC to its own neighbor cache, then replies with a
   **Neighbor Advertisement (Type 136)** sent as a **unicast** frame directly to
   Host A (includes Host C's MAC in the Link-Layer Address option).
9. Host A receives the NA, adds Host C's IPv6+MAC to its neighbor cache, releases
   the held packet, and forwards it — now using direct unicast MAC addressing.
10. **Once learned, the entry is cached.** A second ping to the same destination
    produces **no NDP events at all** — only ICMPv6 echo request/reply, because the
    MAC is already known.

### Local network — condensed sequence
```
PCA1 (no MAC for PCA2) 
  → NS (multicast) → Switch floods → PCA2 accepts / RTA/others ignore in hardware
  → PCA2 caches PCA1's info, replies with NA (unicast)
  → PCA1 caches PCA2's MAC → sends original Echo Request directly (unicast)
  → PCA2 replies Echo Reply (Type 129)
```

## 6. Address Resolution Process — Different Network (Remote)

When the destination is on a **different** network, the host cannot resolve the
destination's MAC directly — instead it resolves the **default gateway's** MAC,
because the packet must first be forwarded there.

1. Host A determines the destination is off-link. It does **not** solicit for the
   destination's MAC; it solicits for the **default gateway's link-local address**
   (e.g., `FE80::1`).
   - Note: this NS uses the source's **link-local** IPv6 address, not its global
     unicast address — link-local addresses are used for on-link/gateway
     interactions.
2. Gateway (router) replies with its MAC via NA.
3. Host A now sends the original packet to the **router's MAC address** (not the
   destination host's MAC) — the destination IP in the packet stays the same,
   but the Layer 2 destination is the router.
4. The router receives the packet, and if it does not yet know the MAC address of
   the destination on the far network's interface, it performs **its own** ND
   process on that interface (NS/NA exchange with the destination host).
5. Once the router learns the destination's MAC, it forwards the frame to the
   destination host, again using unicast Layer 2 addressing but with the
   router's own MAC as the source.
6. The reply path works symmetrically: the destination host also doesn't know
   the original sender's MAC (different network), so it sends its reply frame
   to the **router's MAC**, not the original sender's MAC — the router relays it
   back.
7. Because two independent ND exchanges occur (Host↔Router, Router↔Destination),
   remote communication generates noticeably **more ND events** than local
   communication.
8. As with local communication, once both legs are cached (host→router MAC,
   router→destination MAC), a repeated ping generates **no additional NDP
   events** — this is why TTL is 1 lower for the remote ping (127 instead of
   128) — the packet passed through one router hop.

### Remote network — condensed sequence
```
PCA1 (dest = PCB1, different subnet)
  → NS (targeting gateway's link-local addr, via multicast)
  → RTA replies with NA (its MAC)
  → PCA1 sends Echo Request to RTA's MAC (dest IP still = PCB1)
  → RTA doesn't know PCB1's MAC → RTA does its own NS/NA exchange on the PCB1-side LAN
  → RTA forwards Echo Request to PCB1
  → PCB1 replies, sending back to RTA's MAC (not PCA1's), since PCB1 also
    doesn't know PCA1 directly
  → RTA relays reply back to PCA1
```

## 7. Reflection Answers

**When is ND required?**
Whenever a device knows a destination's IPv6 address but does not have a cached
MAC address for it (or for the relevant next-hop, e.g., the default gateway).

**How does a router limit ND traffic on the network?**
The solicited-node multicast address used in NS messages is scoped as
**link-local**, so routers do **not forward** these ND packets to other networks —
ND traffic stays confined to the local link, never propagating network-wide.

**How does IPv6 minimize the impact of ND on hosts?**
By using multicast (mapped to a specific Ethernet multicast MAC based on part of
the target's IPv6 address) instead of broadcast. Uninvolved NICs can reject
irrelevant frames in **hardware**, without ever escalating to the OS/software
layer — unlike ARP broadcasts, which every host's software must inspect.

**How does the ND process differ for local vs. remote destinations?**
- **Local:** the host directly resolves the destination host's MAC address via
  one NS/NA exchange.
- **Remote:** the host resolves the **default gateway's** MAC address instead
  (packet is sent to the router regardless of final destination). The router
  then independently resolves the actual destination's MAC on its own
  interface. This means remote communication involves two separate ND
  exchanges instead of one, producing more ND events overall.

## 8. Packet Tracer Lab Notes (Cisco Netacad – IPv6 Neighbor Discovery)

**Topology:** RTA (router) connects two LANs — PCA1/PCA2 on `2001:db8:acad:1::/64`,
PCB1 on `2001:db8:acad:2::/64`. All hosts use `fe80::1` (RTA) as default gateway.

**Part 1 (local — PCA1 → PCA2):**
- `show ipv6 neighbors` / `clear ipv6 neighbors` on RTA to reset the cache before
  capturing.
- `ping –n 1 2001:db8:acad:1::b` from PCA1's command prompt (`-n` = number of
  echo requests to send).
- Simulation mode + Edit Filters (ICMPv6, NDP) to isolate relevant events —
  around 12 relevant events appear near time 0.000–0.008s. (Later events, e.g.
  at ~9.8s, 39s, etc., are unrelated background Router Advertisement traffic
  the router sends periodically, and can be ignored.)
- Confirmed: first ICMPv6 event has no Layer 2 info (MAC unknown yet) →
  Echo Request Type 128 held → NS (Type 135) sent via multicast → switch
  floods it → target host accepts (multicast MAC match), others ignore in
  hardware → NA (Type 136) sent back unicast with the responder's MAC in the
  Link-Layer Address option → original Echo Request (128) now sent with full
  L2 info → Echo Reply (Type 129) returned.
- Repeating the same ping produced **zero NDP events** — proof the neighbor
  cache was reused instead of re-resolving.

**Part 2 (remote — PCA1 → PCB1):**
- Same reset procedure, then `ping –n 1 2001:db8:acad:2::a`.
- Significantly more captured events due to the two-hop discovery process
  described in Section 6 above.
- First NS from PCA1 used its **link-local** source address (not global
  unicast) — because it's targeting the on-link gateway, not a remote host.
- Destination MAC used by PCA1 for the actual Echo Request was **RTA's MAC**,
  not PCB1's.
- RTA's outbound frame (before its own ND) lacked destination L2 info,
  because RTA itself needed to resolve PCB1's MAC on its other interface.
- PCB1's reply frames were also addressed to **RTA's MAC** (not PCA1's
  directly) — since PCB1 doesn't have PCA1's MAC and must relay through the
  gateway too.
- Ping TTL was 127 (vs. 128 for the local case) — one less due to the router
  hop.
- Repeating the ping produced no NDP events (cache reused on both legs).
- `show ipv6 neighbors` on RTA afterward listed cached entries for devices
  it had directly resolved (its connected LAN hosts) — but not an automatic
  entry for hosts it never directly solicited (e.g., PCA2 unless pinged from
  the router itself).

## 9. Terminology Quick Reference

- **Neighbor cache / neighbor table**: per-device table mapping IPv6 ↔ MAC
  addresses (IPv6 analog of an ARP table). Local to each host/router, not the
  switch.
- **Solicited-node multicast address**: special multicast IPv6 address derived
  from the low-order bits of a target's IPv6 address, used so only that
  target (or a very small set of nodes) responds to an NS.
- **Link-local address (`FE80::/10`)**: address scope used for on-link
  communication (e.g., host-to-gateway ND), not routable beyond the local link.
- **TTL (Time To Live)**: decremented by each router hop; used here to confirm
  whether a router was traversed.
