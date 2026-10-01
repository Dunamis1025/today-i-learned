# Day 09: Switch Interfaces — Status, Speed, and Duplex

> Continuing from Day 08 (router interface configuration), this session moves to **Cisco switch interfaces**: how they differ from router interfaces, how to check their status, and how speed/duplex settings (including autonegotiation and manual configuration) work. Source: personal lecture notes, summarized and expanded for CCNA 200-301 exam prep.

---

## 1. Switch Interfaces vs. Router Interfaces

Routers and switches are both "network devices with interfaces," but because they operate at **different OSI layers**, their interfaces behave very differently by default.

| Aspect | Router Interface | Switch Interface |
|---|---|---|
| **OSI Layer** | Layer 3 (Network layer) | Layer 2 (Data Link layer) |
| **IP address** | Assigned directly to the interface | **Not** assigned to a regular port (ports forward frames, not route packets) |
| **Default admin state** | `shutdown` (disabled) — must run `no shutdown` to bring it up | **Enabled** (`no shutdown` is the default) |
| **Primary job** | Route packets *between* different networks | Switch frames *within* the same network, based on MAC addresses |

### Why don't switch ports get an IP address?

A Layer 2 switch makes forwarding decisions using the **MAC address table**, not IP addresses — so an access/trunk port itself has no need for an IP. The one exception is the **SVI (Switched Virtual Interface)**, a *virtual* Layer 3 interface (e.g., `interface vlan 1`) that *can* be given an IP address purely so an administrator can remotely manage the switch (Telnet/SSH/ping to it). The SVI is not a physical port — it represents the switch's management presence on a VLAN.

### Why is the default state different?

- A **router** interface defaults to `shutdown` because routers are often deployed with only some interfaces actually cabled and used; leaving unused interfaces administratively down is a safer default.
- A **switch** port defaults to **up** (enabled) because switches are expected to have most or all of their many ports actively connected to end devices (PCs, APs, other switches) right out of the box — so Cisco's default assumes "plug and play."

---

## 2. Checking Switch Interface Status: `show interfaces status`

This is the single most useful command for getting a **one-line-per-port summary** of every interface on a switch.

```
Switch# show interfaces status
Switch# sh int status        (abbreviated form)
```

### Key columns in the output

| Column | Meaning |
|---|---|
| **Port** | Interface name/number, e.g. `Fa0/1` (FastEthernet 0/1), `Gi0/1` (GigabitEthernet 0/1) |
| **Status** | Connection state — see table below |
| **VLAN** | Which VLAN this access port currently belongs to (default: **VLAN 1**) |
| **Duplex** | `full` or `half` (transmission mode — see Section 3) |
| **Speed** | `10`, `100`, `1000`, `auto`, etc. (Mbps) |
| **Type** | Physical media/connector type, e.g. `10/100/1000BaseTX` |

### Status values explained

| Status | Meaning |
|---|---|
| **connected** | Port is up and a device is actively linked on the other end (normal, healthy state) |
| **notconnect** | Port is administratively enabled, but **no cable is plugged in** (or the far end is powered off) |
| **disabled** | Port has been manually shut down by an administrator (`shutdown` command) |

> **Note:** This is conceptually similar to the Status/Protocol (Layer 1/Layer 2) fields from `show ip interface brief` on a router — but `show interfaces status` is a **switch-specific** command that bundles connection state *and* speed/duplex/VLAN info into a single table, which `show ip interface brief` does not show.

---

## 3. Speed and Duplex

Making sure two connected devices agree on **how fast** to talk and **which direction(s)** they can talk at the same time is critical — a mismatch here is one of the most common causes of mysterious "slow network" problems in real networks (and a classic CCNA exam topic).

### ① Duplex modes

| Mode | Analogy | Behavior |
|---|---|---|
| **Half Duplex** | Walkie-talkie / CB radio | Can only send **or** receive at any given moment, never both at once. Used in old **hub**-based networks (shared collision domain). If two devices transmit simultaneously → **collision**, requiring retransmission (handled by CSMA/CD). |
| **Full Duplex** | Telephone call | Can send **and** receive **simultaneously**, over separate transmit/receive wire pairs. No collisions are possible. **Modern switch ports default to full duplex.** |

Half duplex is largely a legacy concept today (from the hub era), but CCNA still expects you to recognize it and know that a **duplex mismatch** (one side full, one side half) causes severe performance problems — not a hard failure, but a partially-working link full of errors.

### ② Autonegotiation

Autonegotiation is a process where two directly connected devices (e.g., a switch port and a PC's NIC) **exchange signals to advertise their supported speeds and duplex modes**, then automatically agree on the **best common setting** both sides support — highest mutual speed, and full duplex if both support it.

- This happens automatically and is the default behavior on modern Cisco switch ports (`speed auto` / `duplex auto`).
- It's the recommended setting in almost all real-world situations, because it removes the risk of manual misconfiguration.

### ③ Manual configuration (CLI)

Sometimes an administrator needs to **force** a specific speed or duplex — e.g., connecting to an old device with broken autonegotiation, or satisfying a strict documented standard.

```
Switch(config)# interface fastethernet 0/1
Switch(config-if)# speed 100
Switch(config-if)# duplex full
```

- `speed 100` — locks the port to 100 Mbps (disables autonegotiating speed).
- `duplex full` — locks the port to full duplex (disables autonegotiating duplex).

> **⚠️ Duplex Mismatch Warning:** If one side of a link is forced to `full` and the other side is left on `auto` (which can sometimes fall back to `half` when the other side isn't negotiating) or is forced to `half`, you get a **duplex mismatch**. The link does **not** go down — it keeps working, but very badly: you'll see **late collisions, CRC errors, and FCS errors** piling up on `show interfaces`, with effective throughput dropping drastically (a switch-to-PC link that should run at 100 Mbps full might perform worse than old 10 Mbps Ethernet). This is a classic real-world and CCNA troubleshooting scenario: **"the link is up, but performance is terrible" → check for a duplex mismatch.**
>
> **Best practice:** Configure both ends the same way — either **both auto**, or **both manually fixed to the identical speed and duplex**. Never mix "one side auto, one side forced," since a port forced to one side alone cannot fully negotiate with an autonegotiating partner.

---

## 4. Configuring Multiple Interfaces at Once: `interface range`

Typing into each port individually is tedious when you need to apply the *same* configuration to many ports (e.g., all ports going to user workstations). The `interface range` command lets you select a **contiguous block of ports** and configure them all simultaneously.

```
Switch(config)# interface range fastethernet 0/1 - 4
Switch(config-if-range)# description To Workstations
Switch(config-if-range)# shutdown
```

- `interface range fastethernet 0/1 - 4` — selects ports Fa0/1 through Fa0/4 together.
- The prompt changes to `(config-if-range)#` to show you're in **range mode**, applying to all selected ports at once.
- Any command entered here (`description`, `shutdown`, `speed`, `duplex`, `switchport mode access`, etc.) is applied identically to **every port in the range**.

> **Syntax notes:**
> - Spaces around the hyphen (`0/1 - 4`) are required.
> - You can also select a comma-separated, non-contiguous list, e.g. `interface range fastethernet 0/1 - 4 , 0/8`.
> - This is purely a **configuration shortcut** — it does not create a new logical interface; it's still configuring the individual physical ports, just in bulk.

---

## 5. Useful Switch Management Commands — Summary Table

| Command | Purpose |
|---|---|
| `show interfaces status` | Quick, one-line-per-port summary: connection status, VLAN, duplex, speed, port type |
| `show ip interface brief` | On a switch, mainly useful for checking the **SVI's** IP/status (e.g., VLAN 1 management interface), since regular access/trunk ports don't carry IP addresses |
| `show interfaces <port>` | **Detailed** statistics for one specific port: traffic counters, error counts (collisions, CRC errors, runts, giants), and Layer 1/2 status — the command to reach for when actively troubleshooting a single problem port |

---

## 6. Quick Summary

- Switches are Layer 2 devices: regular ports don't get IP addresses (only the management SVI does), and ports are **enabled by default** (unlike router interfaces, which default to `shutdown`).
- `show interfaces status` is the key command for a fleet-wide view of port state, VLAN, speed, and duplex.
- **Full duplex** (simultaneous send/receive, no collisions) is the modern default; **half duplex** (one direction at a time, hub-era, collision-prone) is largely legacy.
- **Autonegotiation** lets two connected devices automatically agree on the best mutual speed/duplex; manual `speed`/`duplex` commands override this when needed.
- A **duplex mismatch** doesn't kill the link — it causes severe performance degradation and errors, making it a classic subtle troubleshooting trap.
- `interface range` lets you configure many ports at once instead of repeating commands port-by-port.
- For deep troubleshooting on a single port, `show interfaces <port>` gives the full error/statistics picture that `show interfaces status` summarizes.

---

## 7. Review Questions (for Anki)

| Question | Answer |
|---|---|
| Why don't regular switch ports get an IP address? | Switches operate at Layer 2 and forward frames using MAC addresses, not IP; only the SVI (a virtual Layer 3 interface) gets an IP, for management purposes |
| What is the default administrative state of a switch port? | Enabled (up) — opposite of a router interface, which defaults to `shutdown` |
| What command shows a one-line summary of status, VLAN, duplex, and speed for every switch port? | `show interfaces status` |
| In `show interfaces status`, what does `notconnect` mean? | The port is enabled, but no cable/device is detected on the other end |
| In `show interfaces status`, what does `disabled` mean? | The port has been manually shut down by an administrator |
| What is half duplex, and what's the walkie-talkie analogy? | Can only send or receive at one time, not both — like a walkie-talkie; used in old hub networks, prone to collisions |
| What is full duplex, and what's the telephone analogy? | Can send and receive simultaneously — like a phone call; no collisions; the modern default on switch ports |
| What does autonegotiation do? | Lets two connected devices exchange their supported speed/duplex capabilities and automatically agree on the best common setting |
| What commands manually force speed and duplex on an interface? | `speed <value>` and `duplex full	half` entered in interface configuration mode |
| What happens if one side of a link is forced full duplex and the other is half duplex? | A duplex mismatch — the link stays up but suffers severe performance loss and errors (not a clean failure) |
| What command lets you configure several contiguous ports at once? | `interface range <type> <start> - <end>` |
| Which command gives detailed traffic and error statistics for a single switch port? | `show interfaces <port>` |
| On a switch, what does `show ip interface brief` mainly show? | The IP/status of the management SVI (e.g., VLAN 1), since regular ports don't have IP addresses |

---

## My Study Log

- [x] Watched Day 09 lecture video (switch interfaces)
- [x] Compared switch interfaces vs. router interfaces (Layer, IP assignment, default state)
- [x] Learned `show interfaces status` and its key fields
- [x] Studied half vs. full duplex and autonegotiation
- [x] Learned manual `speed`/`duplex` configuration and duplex mismatch risk
- [x] Learned `interface range` for bulk port configuration
- [ ] Packet Tracer lab for this topic (if available)
- [ ] Reviewed Day 09 Anki flashcards

### Notes / Confusing Points

- (add your own notes here)
