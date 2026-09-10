# VU23218 — Deep Dive: Packet Tracer 9.2.4 (STP, EIGRP, NAT, tracert, ARP)

**Course:** 22603VIC – Certificate IV in Cyber Security
**Unit:** VU23218 – Implement network security infrastructure for an organisation
**Context:** Self-directed follow-up after Session 8, working independently through the full 9.2.4 "Identify Packet Flow" lab (Parts 1–3) with predictions, captures, and link-failure observations.
**Date:** 2026-09-10

This document goes deeper than the earlier Session 8 summary — it captures the actual predicted vs. observed packet paths, the underlying protocols involved, and several foundational networking concepts that came up while working through the lab.

---

## 1. Lab Topology Recap

- **Home Network (pink):** `www.cisco.pka`, `Switch`, `Laptop0`, `PC1`, connected via `West`
- **Local site (orange):** `PC0`, `Tablet0` → `Wireless Router0` → `Cable Modem0` → `Cloud0`
- **WAN mesh:** `Router1`, `Router2`, `Router3`, `Router4` (full mesh) + `Router5`
- **Public Network (blue):** `www.web.pka`, `Public DNS`, connected via `Switch0`, `Switch1`, `Switch2` (triangle) → `East`

---

## 2. Part 2 — Remote LAN Network Topology (Switch0/1/2 triangle)

### Predicted vs. observed path (before any link failure)

**DNS query/response (PC0 → Public DNS):**
```
PC0 → Wireless Router0 → Cable Modem0 → Cloud0 → Router5 → East → Switch0 → Switch1 → Public DNS
```

**HTTP request/response (PC0 → www.web.pka):**
```
PC0 → Wireless Router0 → Cable Modem0 → Cloud0 → Router5 → East → Switch0 → Switch1 → Switch2 → www.web.pka
```

**Why HTTP takes one extra hop than DNS:** the Switch0–Switch2 link showed an **orange dot** in Packet Tracer, meaning it was in **STP blocking state**. Since Switch1 is the Root Bridge, STP disables the redundant Switch0–Switch2 link to prevent a Layer 2 loop. Even though www.web.pka is physically attached to Switch2, traffic has to detour via Switch1 rather than taking the direct (but blocked) shortcut.

Both predicted paths were confirmed exactly by the Simulation mode Event List capture.

### Simulating a broken link (Switch0–Switch1) and observing STP re-convergence

Steps performed:
1. Real-time mode (`Shift+R`) → Delete tool → removed the Switch0–Switch1 link
2. Waited ~30 seconds for STP to detect the failure and re-converge
3. Observed the previously-blocked Switch0–Switch2 link visually change from **orange (blocking) → green triangles (forwarding)**
4. Back in Simulation mode, opened a browser on **Tablet0** and re-navigated to www.web.pka

**New HTTP path after the link failure:**
```
Tablet0 → Wireless Router0 → Router5 → East → Switch0 → Switch2 → www.web.pka
```

This is actually **one hop shorter** than the original path (no longer routes through Switch1) — a direct demonstration of STP automatically activating a previously-blocked backup path once the primary forwarding link goes down.

---

## 3. Part 3 — WAN Network Topology (Router mesh)

### Predicted vs. observed path (before any link failure)

**HTTP request/response (PC0 → www.cisco.pka):**
```
PC0 → Wireless Router0 → Cable Modem0 → Cloud0 → Router5 → Router2 → Router4 → West → Switch → www.cisco.pka
```
Confirmed exactly by capture — traffic used the direct Router2–Router4 mesh link.

### Simulating a broken WAN link (Router4–Router2) and observing EIGRP re-convergence

Unlike Part 2 (Layer 2, STP), this failure is at **Layer 3**, so routers running **EIGRP (Enhanced Interior Gateway Routing Protocol)** dynamically recalculate their routing tables instead.

Steps performed:
1. Real-time mode → Delete tool → removed the Router4–Router2 link
2. Switched back to Simulation mode, opened a browser on **Tablet0**, navigated to www.cisco.pka

**New HTTP path after the link failure:**
```
PC0 → Wireless Router0 → Cable Modem0 → Cloud0 → Router5 → Router2 → Router3 → Router4 → West → Switch → www.cisco.pka
```

EIGRP found an alternate route via **Router3** once the direct Router2–Router4 link was gone — the same conceptual behaviour as STP in Part 2 (dynamic rerouting around a failure), but operating at Layer 3 using routing tables rather than Layer 2 switch ports.

### PC1 → tracert and NAT verification

Ran `tracert www.web.pka` from PC1's command prompt:

```
Tracing route to 209.165.202.132 over a maximum of 30 hops:

  1   192.168.0.1
  2   209.165.200.225
  3   192.0.2.2
  4   192.0.2.18
  5   192.0.2.26
  6   209.165.202.132
  7   209.165.202.132
```

Matched each hop IP to router interfaces using `show ip interface brief` on each device:

| Hop | Device | Interface | IP Address |
|---|---|---|---|
| 1 | West | GigabitEthernet0/1 | 192.168.0.1 |
| 2 | Router4 | Serial0/1/1 | 209.165.200.225 |
| 3 | Router3 | Serial0/0/0 | 192.0.2.2 |
| 4 | Router2 | Serial0/0/1 | 192.0.2.18 |
| 5 | Router5 | Serial0/1/1 | 192.0.2.26 |
| 6 | East | GigabitEthernet0/1 | 209.165.202.132 |
| 7 | www.web.pka | NIC | 209.165.202.132 (public) / 192.168.2.254 (private) |

**NAT note:** the web server's private IP `192.168.2.254` is translated to the routable public IP `209.165.202.132`. Hop 6 (East's G0/1) and hop 7 (the server itself) both display this same public IP, which is why tracert shows it twice.

The router path in the tracert (West → Router4 → Router3 → Router2 → Router5 → East) matched the **already-rerouted** EIGRP path from the earlier WAN link failure test — confirming both routing tables were consistent.

### Comparing tracert vs. simulation results for HTTP (PC1 → www.web.pka)

Simulation Event List showed:
```
PC1 → Switch → West → Router4 → Router3 → Router2 → Router5 → East → Switch0 → Switch2 → www.web.pka
```

**Observation:** the router order matched tracert exactly. The simulation additionally revealed Layer 2 devices tracert doesn't report — the **Switch** between PC1 and West, and **Switch0/Switch2** between East and www.web.pka — because `tracert` only counts IP-routed (Layer 3) hops, not switches. This confirmed that the full physical path includes more devices than a Layer 3 traceroute alone shows.

---

## 4. Supporting Concepts Reviewed

### ARP (Address Resolution Protocol)
Before a device can build an Ethernet frame for the next hop, it needs that hop's **MAC address**, not just its IP. If the MAC isn't already cached, the device broadcasts an **ARP Request** ("who has this IP?"). Non-target devices on the segment receive and discard the broadcast frame — shown in Packet Tracer as a red X, which is normal broadcast behaviour, not an error. This happens freshly at each new subnet/segment along the path (e.g. observed at Wireless Router0 and again at the Router5–East boundary).

### Ethernet Frame (Layer 2)
The "envelope" used to deliver data within a single local network segment:
```
[Destination MAC] [Source MAC] [Type] [Data: IP packet] [FCS]
```
- Carries an IP packet as its payload
- Only valid for one hop/segment — a **new frame is built at every hop**, which is why ARP has to run again at each new segment

### FCS (Frame Check Sequence)
An error-checking value (CRC) appended to the end of an Ethernet frame. The sender computes it from the frame contents; the receiver recomputes it and compares. A mismatch means the frame was corrupted in transit and gets discarded — essentially a "tamper/damage seal" on the frame.

### DNS Query
A request asking a DNS server to resolve a human-readable domain name (e.g. `www.web.pka`) into the IP address actually needed for communication. DNS resolution always has to complete **before** the HTTP request can be sent, since the client needs the server's IP address first — this is why DNS events always preceded HTTP events in every capture throughout the lab.

---

## 5. Key Takeaways

- **STP (Layer 2)** and **EIGRP (Layer 3)** both perform the same conceptual job — detecting a link failure and rerouting traffic — but at different layers and using different mechanisms (blocked switch ports vs. recalculated routing tables).
- Both re-convergence events took a similar ~30 second window, visible directly in Packet Tracer via Fast Forward.
- `tracert` only reveals Layer 3 hops (routers); Packet Tracer's Simulation Event List shows the complete physical path including Layer 2 devices (switches, modems, cloud).
- NAT translates a private server IP to a public, routable IP at the network edge — visible directly in tracert output as the same public IP appearing at both the edge router's interface and the server's own address.
- Predicting a path *before* capturing it, then comparing prediction vs. observation, was a useful way to actually test understanding of switching/routing behaviour rather than just watching packets move.

---

## 6. Submission Note

Completed and submitted (`.docx` + `.pka`) via Brightspace's **Class Activities – Eddie's class** dropbox (VU23220 shell) for optional instructor feedback, since VU23218 (morning) and VU23220 (afternoon) are both taught by the same instructor, Edsel Morales.
