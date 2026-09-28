# Day 03: OSI Model / TCP-IP Model, Packet Tracer Lab & Intro to CLI

> Notes for Day 03 of Jeremy's IT Lab CCNA 200-301 course, covering the **OSI Model / TCP-IP Model** lecture, the accompanying **OSI Model Day 3 Packet Tracer Lab**, and the follow-up **Intro to the CLI** video (terminal emulators, PuTTY, console cabling, and basic IOS password commands). Also incorporates concepts drilled during today's Anki review session for Day 03 cards.

---

## 1. The 5-Layer TCP/IP Model (Jeremy's Version)

CCNA material typically references two competing layer models: the 7-layer **OSI model** (theoretical/academic) and the 4-layer **TCP/IP model** (traditional, practical). Jeremy teaches a **5-layer hybrid** that splits the traditional TCP/IP model's "Network Access" layer into two separate layers for clarity.

| # | 5-Layer Model (Jeremy) | 4-Layer TCP/IP (traditional) | 7-Layer OSI |
|---|--------------------------|-------------------------------|--------------|
| 5 | Application | Application | Application (7), Presentation (6), Session (5) |
| 4 | Transport | Transport | Transport (4) |
| 3 | Network | Internet | Network (3) |
| 2 | Data Link | Network Access | Data Link (2) |
| 1 | Physical | (part of Network Access) | Physical (1) |

**Key rule:** the 5-layer model simply splits "Network Access" into **Data Link** + **Physical**, and renames "Internet" to **Network**. The OSI model's top three layers (Session, Presentation, Application) are all folded into a single **Application** layer in both the 4-layer and 5-layer TCP/IP models — this is why Application layer is called "Layer 5" in the TCP/IP model but "Layer 7" in OSI (same functional layer, different numbering scheme).

### Layer Responsibilities

| Layer | Responsibility | Example Protocols |
|-------|-----------------|--------------------|
| **Application** | Protocols for communication *between applications* — creating and interpreting data | HTTP, HTTPS, FTP, DNS, DHCP |
| **Transport** | *End-to-end* delivery between application **processes**, using **port numbers** to identify the correct program on a host | TCP, UDP |
| **Network** | Logical addressing and routing across the entire path from source to destination network | IP |
| **Data Link** | *Hop-to-hop* delivery within a local network segment, using **MAC addresses** and switches | Ethernet, STP |
| **Physical** | Raw bit transmission over the physical medium (cables, signals) | Ethernet cabling standards (see Day 02 notes) |

### Clarifying "End-to-End" vs. "Hop-to-Hop"

These two terms describe *different scopes of delivery*, and are easy to conflate with the unrelated concept of "hop count" used in routing metrics (e.g., traceroute/TTL, which counts only **router** traversals).

- **End-to-end (Transport layer)**: concerned only with the two endpoints — the sending application process and the receiving application process — regardless of how many devices the data passes through in between.
- **Hop-to-hop (Data Link layer)**: concerned only with delivery across **one single link** between two directly connected devices (PC↔switch, switch↔switch, switch↔router, router↔router — *each* such link is one "hop" in this context). Each hop uses a different pair of source/destination MAC addresses, since Layer 2 addressing only has meaning on that one local link.

This is a different sense of "hop" than the routing/TTL concept, where only router traversals count and switches are transparent.

---

## 2. PDUs (Protocol Data Units) and Encapsulation

Each layer's data unit has its own name:

| Layer | PDU Name |
|-------|----------|
| Application | Data |
| Transport | **Segment** |
| Network | **Packet** (L3PDU) |
| Data Link | **Frame** (L2PDU) |
| Physical | Bits |

**Encapsulation**: as data descends from Layer 5 to Layer 1, each layer wraps the entire unit received from the layer above inside its own header (and, for Data Link, a trailer too) — like nested boxes.

```
[Layer 5] Data
    ↓ wrapped by Transport header
[Layer 4] Segment = [Transport Header][Data]
    ↓ wrapped by Network header
[Layer 3] Packet = [Network Header][Segment]
    ↓ wrapped by Data Link header/trailer
[Layer 2] Frame = [Data Link Header][Packet][Data Link Trailer]
```

**Rule:** the *payload* of any given layer's PDU is always the complete PDU of the layer immediately above it.
- The payload of a **Frame** (L2PDU) is a **Packet** (L3PDU).
- The payload of a **Packet** (L3PDU) is a **Segment** (L4PDU).
- The payload of a **Segment** is **Data** (Application layer).

---

## 3. Adjacent-Layer vs. Same-Layer Interaction

- **Adjacent-layer interaction**: the *real*, literal interaction between a layer and the layer directly above/below it, *within the same device*. Data is only ever physically handed from one layer to its immediate neighbor (e.g., Transport hands its segment down to Network — never directly to Data Link).
- **Same-layer interaction**: a *conceptual/logical* framing where a layer on one device is treated as if it communicates directly with the matching layer on another device (e.g., "my PC's Transport layer talking to the server's Transport layer"), even though the data physically travels down through all layers, across the physical medium, and back up through all layers on the receiving side. Only Layer 1 (Physical) is where data actually crosses between devices.

**Analogy:** like two diplomats speaking through interpreters over a phone line. The diplomats seem to talk "directly" to each other (same-layer interaction), and the interpreters also seem to talk to each other directly — but the only physical connection is the phone line itself (Physical layer). Every other "conversation" is a logical abstraction built on top of that one real physical link.

---

## 4. Networking Terminology Recap

| Term | Meaning |
|------|---------|
| **IETF** (Internet Engineering Task Force) | The organization that develops and publishes internet protocol standards (distinct from IEEE, which governs physical/cabling standards like 802.3 covered in Day 02) |
| **RFC** (Request for Comments) | The name IETF uses for its official standards documents — a historical name retained from the early ARPANET era when these were informal proposal documents inviting feedback |
| **Cisco ASA** | Stands for **Adaptive Security Appliance** — Cisco's branded hardware firewall product line. "ASA" is the product name; "Firewall" is the general category/function it belongs to |

---

## 5. OSI Model — Packet Tracer Lab (Day 3)

### Network Topology

| Device | Role |
|--------|------|
| R1, R2 | Routers |
| Switch 1, Switch 2 | Switches |
| Server 1 | Server, IP `192.168.1.100` |
| PC 1 | Client PC |

**Interface naming conventions:**
- **G** (GigabitEthernet) = 1 Gbps interfaces (also abbreviated GI, GIG)
- **F** (FastEthernet) = 100 Mbps interfaces (also abbreviated FA)

**IP addressing:**

| Network | Devices |
|---------|---------|
| `192.168.1.0/24` | Server 1 (`.100`), PC 1, Switch 1, Switch 2, R1's G0/0 (`.1`) |
| `10.0.0.0/24` | R1's G0/1 (`.1`) ↔ R2's G0/0 (`.2`) — the inter-router link |

### Using Packet Tracer's Simulation Mode

Simulation Mode lets you step through traffic on the network and inspect each packet's OSI layer breakdown as it's sent and received by each device — a hands-on way to see encapsulation and the different layers in action.

#### Example A: Layer 2 protocol — STP (Spanning Tree Protocol)

- **Source device:** Switch 2
- STP operates at **Layer 2 (Data Link)**.
- Inspecting the PDU shows:
  - **Layer 2 header**: IEEE 802.3 Ethernet header information
  - **Encapsulation**: the device wraps the STP PDU into an Ethernet **Frame**
  - **Layer 1**: shows the physical port/interface the frame is transmitted out of

#### Example B: Layer 3 protocol — OSPF (Open Shortest Path First)

- **Source device:** Router 1 (R1)
- OSPF operates at **Layer 3 (Network)** and is used to find the best path between different networks.
- Inspecting the PDU shows:
  - **Layer 3 header** contains the **source IP address** and **destination IP address** (IP addressing is Layer 3 information)
  - The PDU also carries the underlying **Layer 2 and Layer 1** information (every higher-layer PDU is still encapsulated down through the lower layers to actually be transmitted)

#### Example C: Layer 7 protocol — DHCP (Dynamic Host Configuration Protocol)

- **Source device:** PC 1
- DHCP is used to automatically obtain an IP address and operates at **Layer 7 (Application)**.

**Commands used on PC 1 (Command Prompt):**

| Command | Effect |
|---------|--------|
| `ipconfig` | Displays the PC's current IP address |
| `ipconfig /release` | Releases (gives up) the current IP address |
| `ipconfig /renew` | Requests a new IP address — this is what generates DHCP traffic to observe |

**Key observation from the DHCP PDU inspection:**

Looking at the DHCP message's OSI layer breakdown, information appears for **Layers 7, 4, 3, 2, and 1** — but **Layers 5 and 6 show nothing**. This directly demonstrates why the TCP/IP model (used in real networks) collapses OSI's Session (5), Presentation (6), and Application (7) layers into a single **Application layer**: real protocols like DHCP don't have distinct Layer 5/6 behavior to observe, because that separation is a theoretical OSI construct, not how real-world stacks are implemented.

- **Layer 4**: the DHCP PDU is encapsulated into a **UDP segment** (DHCP uses UDP, not TCP, at the Transport layer).

---

## 6. Intro to the CLI

### Terminal Emulators

A **terminal emulator** is software that lets a modern computer connect to and control another device (router, switch, server) via command-line input — reproducing the function of old physical hardware terminals (hence "terminal emulator": software *emulating* a hardware terminal). Since Cisco devices are configured entirely via CLI (no GUI), a terminal emulator is required to interact with them.

**PuTTY** is the terminal emulator demonstrated in this course (free, available from putty.org or the Microsoft Store — both are legitimate, distributed by the same original author, Simon Tatham).

### PuTTY Connection Types

| Connection Type | When Used |
|------------------|-----------|
| **Serial** | Direct physical console cable connection — used for initial device configuration, before any network/IP connectivity exists |
| **SSH** | Remote access over an existing network connection, encrypted (secure) |
| **Telnet** | Remote access over a network connection, *unencrypted* — largely deprecated for security reasons |

**Note:** modern laptops typically lack physical serial (COM) ports, so attempting a Serial connection without the correct hardware (or a USB-to-serial adapter) will produce an error like `Unable to open connection to COM1` — this is expected behavior, not a misconfiguration, when no physical serial port/device is present.

### Console Connection: Rollover Cable, not Crossover

**Question:** What kind of cable connects to a Cisco device via the RJ45 console port?
**Answer: Rollover cable** (not Crossover)

**Key clarification:** RJ45 describes only the **physical connector shape** (an 8-pin plug) — it does not specify the internal wiring. Different cable types (Straight-through, Crossover, Rollover) can all use RJ45 connectors on their ends.

| Cable Type | Wiring Pattern | Purpose |
|------------|------------------|---------|
| Straight-through | Pin 1→1, 2→2, ... (no change) | PC ↔ Switch (Ethernet data) |
| Crossover | Select pins swapped (e.g., 1↔3, 2↔6) | PC↔PC, Switch↔Switch (Ethernet data) |
| **Rollover** | **All 8 pins fully reversed** (1↔8, 2↔7, 3↔6, ... — pin order is "rolled over") | PC ↔ Router/Switch **console port** (management access, not Ethernet data traffic) |

The console port is used for out-of-band management (serial communication), which is a fundamentally different purpose from Ethernet data transmission — hence the different (Rollover) wiring, despite sharing the same RJ45 connector shape as Ethernet cables.

### Baud Rate: Why Console Connections Use Speed 9600

**"Speed" in PuTTY's Serial settings = baud rate** — the number of bits transmitted per second over the serial link. Both ends of a serial connection must be configured to the *same* baud rate to communicate correctly (a mismatch causes garbled/unreadable output).

- **Cisco console ports default to 9600 baud** — this is an industry-standard default worth memorizing directly: *"Cisco console port default speed = 9600."*

---

## 7. IOS Command: `service password-encryption`

This command controls whether passwords stored in a Cisco device's configuration file are stored as encrypted text or plain (readable) text.

### If `service password-encryption` is enabled:

| Password Type | Effect |
|-----------------|--------|
| Currently configured passwords | **Will be encrypted** (immediately, retroactively) |
| Future passwords | **Will be encrypted** as they're configured |
| `enable secret` | **Not affected** |

### If `service password-encryption` is disabled:

| Password Type | Effect |
|-----------------|--------|
| Currently configured (already-encrypted) passwords | **Will NOT be decrypted** — they stay encrypted; disabling doesn't reverse existing encryption |
| Future passwords | **Will NOT be encrypted** — new passwords are stored in plain text going forward |
| `enable secret` | **Not affected** |

### Why `enable secret` is always unaffected

- **`enable password`** (legacy command) — plaintext by default, and *is* affected by `service password-encryption` (toggled on/off).
- **`enable secret`** (modern, more secure command) — is **always strongly encrypted/hashed automatically** the moment it's configured, completely independent of whether `service password-encryption` is on or off. It never depends on this global setting.

**Memory rule:** *"`enable secret` is always encrypted regardless of settings; other passwords (like `enable password`) depend on whether `service password-encryption` is toggled on."*

---

## 8. Quick Summary

- Jeremy's 5-layer model splits the 4-layer TCP/IP model's "Network Access" into Data Link + Physical; Application layer is "Layer 5" here but "Layer 7" in OSI (same layer, different numbering).
- Transport layer provides end-to-end delivery via port numbers; Data Link layer provides hop-to-hop delivery via MAC addresses within a local segment — these are different scopes of delivery, distinct from routing "hop count" (which only counts routers).
- PDU names by layer: Data → Segment → Packet → Frame → Bits. Encapsulation wraps each layer's PDU inside the layer below's header.
- Adjacent-layer interaction is real, physical, within-device data handoff between neighboring layers; same-layer interaction is a logical/conceptual framing of communication between matching layers on different devices.
- IETF publishes internet standards as RFCs; Cisco ASA is a branded firewall product (Adaptive Security Appliance).
- In the Packet Tracer lab, STP (L2), OSPF (L3), and DHCP (L7) traffic were inspected via Simulation Mode; the DHCP inspection showed no Layer 5/6 data, illustrating why TCP/IP collapses these into one Application layer.
- Terminal emulators (e.g., PuTTY) let a computer control a Cisco device via CLI, using Serial (console), SSH, or Telnet connections.
- Console ports use a **Rollover cable** (all 8 pins reversed) with RJ45 connectors — not a Crossover cable; RJ45 only describes connector shape, not wiring scheme.
- Cisco console ports default to a baud rate (Speed) of **9600**.
- `service password-encryption` toggles encryption for legacy passwords (`enable password`, line passwords, etc.) but never affects `enable secret`, which is always encrypted by default.

---

## 9. Review Questions

| Question | Answer |
|----------|--------|
| In the 5-layer TCP/IP model, which layer handles communication between applications, creating/interpreting data? | Layer 5 (Application) — a.k.a. Layer 7 in OSI |
| Which layer provides end-to-end communication using port numbers? | Layer 4 (Transport) |
| Which layer provides hop-to-hop delivery within a local network using MAC addresses and switches? | Layer 2 (Data Link) |
| What is the payload of a Frame (L2PDU)? | A Packet (L3PDU) |
| What is interaction between a layer and its immediate neighbors called? | Adjacent-layer interaction |
| What documents does the IETF publish standards in? | RFCs (Requests for Comments) |
| What kind of network device is a Cisco ASA? | Firewall (Adaptive Security Appliance) |
| In the Packet Tracer lab, what layer does STP operate at? | Layer 2 (Data Link) |
| What layer does OSPF operate at, and what does its header contain? | Layer 3 (Network); source & destination IP addresses |
| What layer does DHCP operate at, and why do Layers 5/6 show no data when inspecting it? | Layer 7 (Application); because TCP/IP model merges OSI Layers 5/6/7 into one Application layer |
| What kind of cable connects to a Cisco device via the RJ45 console port? | Rollover cable (not Crossover) |
| What is the default baud rate (Speed) for a Cisco console connection? | 9600 |
| If `service password-encryption` is enabled, what happens to the `enable secret`? | Nothing — it's unaffected (always encrypted regardless) |
| If `service password-encryption` is disabled, are already-encrypted passwords decrypted? | No — they remain encrypted; only future passwords are affected |

---

## My Study Log

- [x] Watched OSI Model / TCP-IP Model lecture (Day 03)
- [x] Completed OSI Model Day 3 Packet Tracer Lab (STP, OSPF, DHCP traffic inspection)
- [x] Watched Intro to the CLI video (PuTTY, terminal emulators, console cabling)
- [x] Reviewed Day 03 Anki flashcards
- [ ] Hands-on PuTTY Serial practice (blocked — no physical COM port on laptop; conceptual understanding confirmed instead)

### Notes / Confusing Points

- (add your own notes here)
