# VU23218 — Session 8: Firewall Technologies, STP Review & Packet Tracer 9.2.4

**Course:** 22603VIC – Certificate IV in Cyber Security
**Unit:** VU23218 – Implement network security infrastructure for an organisation
**Session:** 8
**Date:** 2026-09-10

---

## 1. STP (Spanning Tree Protocol) — Quick Review

Revisited from a previous session as a warm-up before firewall topics.

- **Purpose:** Prevents Layer 2 loops in redundant switched networks by blocking redundant paths while keeping one loop-free active topology.
- **Root Bridge election:** The switch with the lowest Bridge ID (Priority + MAC address) becomes the Root Bridge. All other switches calculate the shortest path back to it.
- **In-class quiz:** Given a triangle topology of `Switch0`, `Switch1`, `Switch2` inside the Public Network segment, the Root Bridge was **Switch1**.
- **Connection to today's lab:** When a link between two switches in this same triangle (`Switch0`–`Switch1`) is broken later in the Packet Tracer lab, STP is what detects the topology change and re-converges the network — this is the mechanism behind the ~30 second delay observed in Part 2 of the lab.

---

## 2. Firewall Technologies

Core theory covered before moving into the lab:

| Concept | Description |
|---|---|
| **Packet Filtering Firewall** | Inspects packets at Layer 3/4 (IP address, port, protocol) against static ACL-like rules. Stateless — does not track connection state. Fast but limited context. |
| **Stateful Firewall** | Tracks the state of active connections (TCP handshake, session table) and only allows return traffic that matches an established session. More secure than simple packet filtering. |
| **DMZ (Demilitarized Zone)** | A segregated network segment placed between the internal (trusted) network and the external (untrusted) network, typically hosting public-facing servers (web, DNS, mail) so that a compromise there doesn't directly expose the internal LAN. |
| **Layered Defense (Defense in Depth)** | Security is applied at multiple layers (perimeter firewall, internal segmentation, endpoint protection, monitoring) so that a single point of failure doesn't compromise the whole network. |

---

## 3. Packet Tracer Lab — 9.2.4 Identify Packet Flow

**Objective:** Observe how packets flow through a LAN and WAN topology, and how the flow path changes when the topology changes (e.g. a broken link).

### Topology overview
- **Public Network** (blue): `Router1`, `Router2` connected to `Switch0`, `Switch1`, `Switch2` (triangle) hosting `www.web.pka` and `Public DNS`
- **Home Network** (pink): `Switch` connecting `www.cisco.pka`, `Laptop0`, `PC1`
- **Remote/WAN network**: `Router1`–`Router4`–`Router2`–`Router3`–`Router5` mesh, connected via `West`/`East` routers
- **Local site** (orange): `Cable Modem0` → `Wireless Router0` → `PC0`, `Tablet0`

### Part 1: Verify Connectivity — ✅ Completed
- On `PC0`, opened Web Browser → `www.cisco.pka` → success (must use `.pka`, not `.com`)
- Repeated for `www.web.pka` → success
- Closed web browser

### Part 2: Remote LAN Network Topology
1. Switched to **Simulation mode** (`Shift + S`), used **Show All/None** to reset event list filters
2. **Edit Filters** → checked `DNS` (IPv4 tab) and `HTTP` (Misc tab)
3. On `PC0`, opened Web Browser → `www.web.pka` → Go
4. **Prediction question:** predicted the packet path for DNS resolution before capturing
5. Used **Capture/Forward** repeatedly until the page loaded, observing the actual DNS → HTTP packet path (used *View Previous Events* when the Buffer Full dialog appeared)
6. **Observation question:** recorded which path the HTTP packets actually traveled
7. Switched to **Real-time mode** (`Shift + R`)
8. Selected the **Delete (X)** tool and removed the link between **Switch0 and Switch1** in the Public Network to simulate a broken link
9. Waited ~**30 seconds** (STP re-convergence) — used Fast Forward to speed this up
10. Re-selected the **Arrow (Select)** tool to de-select Delete
11. Switched back to **Simulation mode**, opened the web browser on **Tablet0** (same Public Network segment as PC0's target) and navigated to `www.web.pka` again
12. **Observation question:** compared the new packet path against the original — with the direct Switch0–Switch1 link gone, traffic had to reroute through the remaining switch/path

### Part 3: WAN Network Topology
1. Remaining in Simulation mode, opened web browser on `PC0` → `www.cisco.pka` → Go
2. **Prediction question:** predicted the WAN packet path for DNS resolution
3. **Capture/Forward** until page loaded; recorded the actual HTTP path (View Previous Events on Buffer Full)
4. Switched to **Real-time mode**, removed the link between **Router4 and Router2**, simulating an inaccessible WAN path
   - Routers use **EIGRP** (Enhanced Interior Gateway Routing Protocol) to dynamically recalculate routes after the link loss
5. Switched back to Simulation mode, opened web browser on **Tablet0** → `www.cisco.pka` → observed the rerouted path
6. Switched back to Real-time mode
7. **PC1 → websites (tracert):**
   - Opened Command Prompt on `PC1`, ran `tracert www.web.pka`
   - Matched hop IP addresses to devices in the topology (hover over routers, or `router > CLI > show ip interface brief`)
   - **NAT note:** the private IP of `www.web.pka` (`192.168.2.254`) is translated to the public/routable IP `209.165.202.132`. In the tracert output, the first `209.165.202.132` hop is the `G0/1` interface of router `East`; the second occurrence is the web server's actual public IP.
8. Back in Simulation mode, opened the web browser on `PC1` → `www.web.pka` → Go → Capture/Forward
9. **Final comparison question:** compared the `tracert` hop results against the simulated HTTP packet path to confirm they matched

---

## 4. Key Takeaways

- Packet Tracer's **Simulation mode** lets you visually trace individual packets (DNS lookups, then HTTP requests) hop-by-hop, which makes abstract routing/switching concepts concrete.
- Breaking a link and switching to **Real-time mode** shows *convergence protocols in action* — STP for Layer 2 (LAN), EIGRP for Layer 3 (WAN) — both took a noticeable delay (~30s) to detect the failure and recalculate paths.
- **NAT** translates private IPs to public IPs at the network edge; this is visible directly in `tracert` output as a public IP appearing at the router's WAN-facing interface before the actual destination server.
- Firewall theory (packet filtering vs. stateful, DMZ, layered defense) connects directly to why organizations segment public-facing services (like `www.web.pka`) away from internal hosts — the Public Network segment in this lab is effectively acting like a DMZ.

---

## 5. Assessment Note

Instructor (Edsel Morales) mentioned that a completed version of this Packet Tracer activity can optionally be submitted to the **VU23220 "Class Activities" Brightspace dropbox** (afternoon class shell) for informal review/feedback, since he teaches both units. Not compulsory.
