# Day 09 Anki Review: CLI Modes, Interface Settings, Duplex, Error Counters & Layer Concepts

> Follow-up to `14_day09_switch_interfaces_speed_duplex.md`. This note consolidates everything worked through in the Anki-style review sessions after Day 09: Cisco IOS CLI modes and security commands, console port settings, speed/duplex/autonegotiation in depth, CSMA/CD and collision domains, `show` command output (status fields and error counters), Ethernet frame field recap, TCP/IP layer concepts, device/cabling basics, and an IPv4 host-count refresher. A keyword cheat sheet and a full Anki table are at the end.

---

## 1. Cisco IOS CLI Modes and Prompts

The prompt tells you which mode you are in. Memorize the prompt, and you know the privilege level.

| Mode | Prompt | How to enter | What you can do |
|---|---|---|---|
| **User EXEC** | `Router>` | Default on login | Basic monitoring (limited `show`, `ping`) |
| **Privileged EXEC** | `Router#` | `enable` | All `show` commands, save config, enter config mode |
| **Global configuration** | `Router(config)#` | `configure terminal` | Change device-wide configuration |
| **Interface configuration** | `Router(config-if)#` | `interface <type> <number>` | Configure one specific interface |
| **Line configuration** | `Router(config-line)#` | `line console 0`, `line vty 0 4` | Configure console/VTY access |

### Moving between modes

| Command | Effect |
|---|---|
| `enable` | User EXEC `>` to Privileged EXEC `#` |
| `configure terminal` | Privileged EXEC to Global config |
| `exit` | Back **one** level (e.g., `(config-if)#` to `(config)#`) |
| `end` or `Ctrl+Z` | Straight back to Privileged EXEC `#` from any config mode |
| `disable` | Privileged EXEC `#` back to User EXEC `>` |

**Memory hooks**
- The symbol changes from `>` to `#` only once. `(config)#` is just `#` with a `(config)` tag showing that you are in configuration mode.
- Think of a building: `>` is a visitor pass (lobby), `#` is a staff pass (`enable`), `(config)#` is the management-office key (`configure terminal`).
- The text inside the parentheses names the sub-mode: `if` = interface, `line` = console/VTY line.

### The two configuration files

| File | Stored in | Behavior |
|---|---|---|
| **running-config** | RAM (volatile) | The active configuration; every command you type changes it immediately; **lost on reboot or power loss** |
| **startup-config** | NVRAM (non-volatile) | Loaded at boot; survives power loss |

Save the running configuration permanently:

```
Switch# copy running-config startup-config
Switch# copy run start          (abbreviated)
```

Analogy: running-config is a Word document you are editing; startup-config is the version you saved to disk. Forget to save, and a reboot throws the edits away.

---

## 2. Device Security Commands

```
Router(config)# enable password <password>
Router(config)# enable secret <password>
Router(config)# service password-encryption
```

In `enable password <password>`, the second word "password" is a **placeholder for the value you choose**, not a keyword: `enable password cisco123`.

| Command | What it does | Encrypted? |
|---|---|---|
| `enable password <pw>` | Sets the password for entering Privileged EXEC mode | **No** (stored as plain text in the config) |
| `enable secret <pw>` | Sets the same password, but hashed | **Yes** (much stronger) |
| `service password-encryption` | Turns on a global feature that obscures **all plain-text passwords** in the config (current and future) | Weak (Type 7) |

### Key points
- Read `service password-encryption` literally: "enable the password-encryption service."
- It covers **current and future** plain-text passwords (console, VTY, `enable password`, etc.).
- Type 7 is **reversible** with common tools; it only hides passwords from casual over-the-shoulder viewing. For real protection use `enable secret`.
- If both `enable password` and `enable secret` are configured, **`enable secret` takes precedence**.
- `no service password-encryption` stops *future* obscuring but does **not** decrypt passwords already obscured.

Exam wording trick: "**un**encrypted password" means `enable password`; "encrypted" means `enable secret`; "encrypt current and future passwords" means `service password-encryption`.

**Quick lab (Packet Tracer)**
```
Router> enable
Router# configure terminal
Router(config)# enable password cisco123
Router(config)# end
Router# show running-config         <- shows "enable password cisco123" in plain text
Router# configure terminal
Router(config)# service password-encryption
Router(config)# end
Router# show running-config         <- now shows "enable password 7 0822..." (obscured)
```

---

## 3. Console Port Default Settings

| Setting | Default |
|---|---|
| **Speed (baud rate)** | **9600** |
| Data bits | 8 |
| Parity | None |
| Stop bits | 1 |
| Flow control | None |

Shorthand: **9600-8-N-1**. The same values go into the terminal program (e.g., PuTTY, Serial mode) when connecting with a console cable.

### Terminology
- **Baud rate**: how many times per second the signal changes ("symbols per second"). On a simple serial link where each signal change carries one bit, baud is effectively equal to bits per second, so "9600 baud" is roughly "9600 bits per second". Named after Emile Baudot (telegraph engineer).
- **Parity**: one extra check bit appended to the data so the receiver can detect a single flipped bit (even/odd/none). Default is none.
- **Stop bit**: a bit that marks the **end of one character** so the receiver knows where one byte ends and the next begins (like a period at the end of a sentence).
- **PuTTY**: not an acronym. A free terminal program supporting SSH, Telnet, and serial (console) connections.
- **Symptom of mismatched baud rates**: garbled, unreadable characters on the terminal.

---

## 4. Interface Configuration Commands (Recap and Additions)

All of these are entered in `(config-if)#` mode, after selecting an interface.

| Goal | Command |
|---|---|
| Add a note describing the interface | `description <text>` (e.g., `description To SW1`) |
| Set speed to 100 Mbps | `speed 100` (options: `10`, `100`, `1000`, `auto`) |
| Set full duplex | `duplex full` (options: `full`, `half`, `auto`) |
| Shut down / enable | `shutdown` / `no shutdown` |

Notes:
- `description` has **no effect on traffic**. It documents what the port connects to and shows up in `show interfaces description`.
- Reading `speed 100`: "speed" is the command word, "100" is the value in Mbps (the unit is implied). It is entered in interface mode because speed is a **per-port** property.
- `speed 100` replaces autonegotiated speed with a fixed 100 Mbps. `duplex full` does the same for duplex.
- A `##` that sometimes appears around text such as `## To SW1 ##` in copied notes is a **markdown formatting artifact**, not IOS syntax. Type the plain text only.

---

## 5. Speed, Duplex and Autonegotiation (Deep Dive)

### Duplex = can you send and receive at the same time?

| Mode | Behavior | Analogy |
|---|---|---|
| **Half duplex** | One direction at a time; uses CSMA/CD; collisions possible | Walkie-talkie |
| **Full duplex** | Send and receive simultaneously on separate wire pairs; **no collisions** | Telephone call |

### Defaults: both are `auto`
- Default speed setting = **auto**
- Default duplex setting = **auto**

### Setting versus result (a common confusion)

| Term | Meaning |
|---|---|
| **Setting** | What is configured: `auto` (default), or a fixed value |
| **Result** | What was actually agreed with the neighbor, e.g., 100 Mbps full duplex |

`show interfaces status` makes the difference visible:

```
Port    Status      Vlan  Duplex   Speed  Type
Fa0/1   connected   1     a-full   a-100  10/100BaseTX    <- auto-negotiated result
Fa0/2   connected   1     full     100    10/100BaseTX    <- manually fixed
```

The **`a-` prefix** means "this value came from autonegotiation."
So "switch ports run full duplex by default" means "auto usually negotiates to full", not "the configured default is full".

### What is being negotiated?
When two devices connect, they exchange short signals over the cable advertising the speed/duplex combinations each supports, then pick the **best combination both support**. Rough preference order, best first: 1000 full, 1000 half, 100 full, 100 half, 10 full, 10 half.

### Why manual settings are risky
When speed and duplex are **both** fixed manually, the port stops sending negotiation signals. If the neighbor is still set to `auto`:
1. The auto side cannot learn the fixed side's duplex from negotiation.
2. It can usually still **detect the speed** from the electrical signal.
3. It **cannot detect duplex**, so (for 10/100 links, per the standard) it falls back to **half duplex**, the lowest common denominator that works with any partner.
4. The fixed side runs full duplex. The two ends now disagree: a **duplex mismatch**.

### Duplex mismatch
- Link stays **up** (both `Status` and `Protocol` show up), which is what makes it hard to diagnose.
- The **half-duplex side** treats normal incoming traffic as collisions (CSMA/CD) and keeps stopping/retrying.
- The **full-duplex side** ignores collision logic and keeps transmitting, so frames arrive damaged.
- Symptoms: **late collisions** (on the half side), **CRC/FCS errors** (on the full side), runts, retransmissions, and **dramatically slow throughput** while the link looks healthy.
- Best practice: **both ends auto**, or **both ends manually set to identical values**. The most common cause is "one side fixed, other side auto."

---

## 6. CSMA/CD and Collision Domains

### CSMA/CD = Carrier Sense Multiple Access with Collision Detection

| Part | Meaning |
|---|---|
| **Carrier Sense** | Listen first: is the wire idle? |
| **Multiple Access** | Many devices share the same medium |
| **Collision Detection** | If two devices transmit at once, detect the collision, stop, wait a random time, retransmit |

Flow: listen, transmit if idle, watch for a collision while sending, on collision stop and back off randomly, then try again.

- Ethernet devices use CSMA/CD to detect and handle collisions on **half-duplex** interfaces.
- **Full duplex does not use CSMA/CD** (no shared medium, so no collisions).

### Collision domain
- **Domain** here means "a scope/zone in which something applies" (not an internet domain name).
- A **collision domain** is the group of devices whose simultaneous transmissions can collide.

| Device | Collision domains |
|---|---|
| **Hub** | **One** for the whole hub: it repeats every signal out of every other port, so all connected devices share one wire logically |
| **Switch** | **One per port**: frames go only where needed, and full duplex removes collisions altogether |

Analogy: a hub is everyone talking in one room (overlapping voices ruin it); a switch is a private phone booth per person.

---

## 7. `show ip interface brief`: Status vs Protocol

| Field | OSI layer | What it tells you |
|---|---|---|
| **Status** | **Layer 1** (Physical) | Is the interface physically up (cable connected, signal detected) or administratively disabled? |
| **Protocol** | **Layer 2** (Data Link) | Is the Layer 2 protocol working (frames can be exchanged)? |

| Status | Protocol | Meaning |
|---|---|---|
| up | up | Fully working |
| down | down | Layer 1 problem: no cable, far end off, etc. |
| up | down | Layer 1 fine, Layer 2 problem: e.g., encapsulation mismatch, missing keepalives |
| administratively down | down | Interface was shut down with the `shutdown` command |

Memory hook: **S**tatus = layer **1** (physical connection), **P**rotocol = layer **2** (how they talk).
On a **switch**, `show interfaces status` is the dedicated summary command (`connected`, `notconnect`, `disabled`, plus VLAN/duplex/speed/type). On a switch, `show ip interface brief` mostly matters for the management SVI.

---

## 8. `show interfaces` Error Counters

| Counter | What it counts |
|---|---|
| **runts** | Frames **smaller** than the minimum size (**64 bytes**) |
| **giants** | Frames **larger** than the maximum size (**1518 bytes**) |
| **CRC** | Frames that **failed the FCS/CRC check** (corrupted in transit) |
| **frame** | Frames with an **incorrect/illegal format** (CRC failure together with a non-integer number of bytes) |
| **input errors** | **Total** of the various error counters for frames the device received |

Notes:
- "Input" means traffic **received** by this interface.
- The 64-byte minimum and 1518-byte maximum are measured from **Destination MAC through FCS**; the Preamble and SFD are not counted.
- Collisions and duplex mismatches commonly raise runts, CRC errors and late collisions.
- Detail view for one port: `show interfaces <port>`.

Memory hook: **smaller = runts** (runt of the litter), **larger = giants**, **failed check = CRC**, **bad format = frame**, **total = input errors**.

---

## 9. Ethernet Frame Recap: Preamble, SFD, FCS, CRC

| Field | Size | Pattern / purpose |
|---|---|---|
| **Preamble** | 7 bytes | Each byte is **`10101010`**; lets the receiver synchronize its clock to the sender |
| **SFD** (Start Frame Delimiter) | 1 byte | **`10101011`**; marks "the real frame starts now" |
| Destination MAC / Source MAC | 6 bytes each | Hardware addresses |
| Type/Length | 2 bytes | Identifies payload type or length |
| **FCS** (Frame Check Sequence) | 4 bytes (trailer) | Error-detection value |

- SFD is identical to a Preamble byte except the **last bit is 1**, so the receiver sees two 1s in a row and knows the pattern ended. Analogy: Preamble is "ready, ready, ready" and SFD is "go!"
- **CRC (Cyclic Redundancy Check)** is the **algorithm** that computes the value placed in the **FCS field**. FCS is the field; CRC is the method.
- How it works (conceptually): the sender computes a value from the frame and appends it; the receiver recomputes it and compares. A mismatch means the frame was damaged.
- Ethernet detects errors but **does not correct** them: a bad frame is **discarded**. Recovery (if needed) is the job of higher layers such as TCP.

---

## 10. TCP/IP 5-Layer Model and Layer Interactions

| Layer | Name | Key words |
|---|---|---|
| 5 | Application | HTTP, DNS, user-facing services |
| 4 | **Transport** | **Port numbers**, TCP/UDP; end-to-end communication between **application processes** |
| 3 | **Network** (a.k.a. **Internet** layer in TCP/IP) | **IP addresses, routers**; end-to-end delivery between **hosts across networks** |
| 2 | Data Link | MAC addresses, switches, frames |
| 1 | Physical | Cables, signals, bits |

Hook: **port means Layer 4; IP address and router mean Layer 3.**
(IP address picks the right **device**; port number picks the right **program** on that device. Like building address versus apartment number.)

### Layer interaction terms
| Term | Definition |
|---|---|
| **Adjacent-layer interaction** | A layer interacting with the layers **directly above and below it on the same device** ("adjacent" = next to) |
| **Same-layer interaction** | A layer interacting (logically) with the **equivalent layer on another device** (e.g., my Transport layer to the server's Transport layer) |

"a.k.a." = "also known as".

---

## 11. Devices, Firewalls and Cabling

- **Cisco ISR** = **Integrated Services Router**: a router that integrates several functions (routing, switching modules, security, VPN, voice) in one box; typical for branch offices. Answer to "what kind of device is an ISR?" is **router**.
- **Host-based firewall**: a **software** application running on an individual host (like a PC) that filters traffic entering and leaving that host (e.g., Windows Defender Firewall). Contrast with a network-based firewall at the network boundary.

### UTP cable types
| Cable | Wiring | Typical use |
|---|---|---|
| **Straight-through** | Each pin connects to the **same** pin on the other end (1 to 1, 2 to 2, ...) | Different device types: PC to switch, router to switch |
| **Crossover** | Pairs are swapped (pins 1,2 to 3,6) | Like devices: switch to switch, PC to PC, router to router (modern devices often auto-detect with Auto-MDIX) |

Question wording: "connects a pin pair on one end to **the same pair** on the other end" means **straight-through**.

---

## 12. IPv4 Addressing Refresher

### Hosts per network
Formula: **usable hosts = 2^n - 2**, where **n = number of host bits**. The "-2" removes the **network address** (all host bits 0) and the **broadcast address** (all host bits 1).

| Class | Host bits | Calculation | Usable hosts |
|---|---|---|---|
| **A** | 24 | 2^24 - 2 | **16,777,214** |
| B | 16 | 2^16 - 2 | 65,534 |
| C | 8 | 2^8 - 2 | 254 |

### Class D and E
| Class | Range (first octet) | Purpose |
|---|---|---|
| D | 224 to 239 | **Multicast** group addresses |
| E | 240 to 255 | **Experimental/reserved** |

- Neither is split into network and host parts, so **no default prefix length** applies to them.
- IPv4 has only 32 bits, so the largest prefix is **/32**; something like `/40` cannot exist.

---

## 13. Question-Pattern Cheat Sheet (Keyword to Answer)

Many Anki questions follow a template: read the question stem, then match a **keyword** in the clue.

| Clue keyword | Answer |
|---|---|
| port numbers, application processes | Transport layer (Layer 4) |
| IP addresses, routers, across networks | Network/Internet layer (Layer 3) |
| layer and those above/below on same device | adjacent-layer interaction |
| layer and the equivalent layer on another device | same-layer interaction |
| two configuration files | running-config, startup-config |
| unencrypted privileged EXEC password | `enable password` |
| encrypt current and future passwords | `service password-encryption` |
| `Router(config)#` | Global configuration mode |
| Layer 1 status field | Status |
| Layer 2 status field | Protocol |
| default speed / default duplex | auto |
| detect/prevent collisions on half duplex | CSMA/CD |
| same collision domain (hub) | collision |
| smaller than 64 bytes | runts |
| larger than max size | giants |
| failed CRC check | CRC |
| illegal format | frame |
| total of error counters | input errors |
| Cisco ISR | Router |
| same pin to same pin | straight-through cable |
| console baud rate | 9600 |
| one byte of Ethernet preamble | `10101010` |
| SFD | Start Frame Delimiter (`10101011`) |
| FCS algorithm | CRC (Cyclic Redundancy Check) |

**Reading tip:** do not try to translate the whole sentence word by word. Find the skeleton ("What/Which ...?") first, then use the one or two keywords in the clue.

---

## 14. Review Questions (for Anki)

| Question | Answer |
|---|---|
| Which TCP/IP layer provides end-to-end communication between application processes using port numbers? | Transport layer (Layer 4) |
| Which TCP/IP layer provides end-to-end communication between hosts across networks using IP addresses and routers? | Network / Internet layer (Layer 3) |
| What is interaction between a layer and those above and below it called? | Adjacent-layer interaction |
| What is interaction between a layer and the equivalent layer on another device called? | Same-layer interaction |
| What two configuration files are kept on a Cisco device? | running-config (RAM) and startup-config (NVRAM) |
| Which command saves the running configuration permanently? | `copy running-config startup-config` |
| What prompt indicates User EXEC mode? Privileged EXEC? Global config? | `Router>`; `Router#`; `Router(config)#` |
| Command to enter Privileged EXEC from User EXEC? | `enable` |
| Command to enter Global configuration from Privileged EXEC? | `configure terminal` |
| Difference between `exit` and `end`? | `exit` goes back one level; `end` (or Ctrl+Z) returns to Privileged EXEC |
| Configure an unencrypted password for Privileged EXEC mode? | `enable password <password>` |
| Which command stores the Privileged EXEC password in hashed form? | `enable secret <password>` |
| Encrypt current and future passwords on the device? | `service password-encryption` |
| Does `no service password-encryption` decrypt passwords already encrypted? | No |
| Default Cisco console port baud rate? | 9600 |
| Default console settings (shorthand)? | 9600-8-N-1, no flow control |
| What does a stop bit do? | Marks the end of a transmitted character/byte |
| What is parity? | An extra bit used for simple error detection; default is none |
| What does PuTTY stand for? | Nothing: it is a name, not an acronym (a free terminal/SSH/serial client) |
| What is a baud rate? | Signal changes per second (about bits per second on a simple serial link) |
| Command to add a description to an interface? | `description <text>` |
| Command to set interface speed to 100 Mbps? | `speed 100` |
| Command to set interface to full duplex? | `duplex full` |
| Default speed setting of an interface? | auto |
| Default duplex setting of an interface? | auto |
| What does an `a-` prefix (e.g., `a-full`, `a-100`) mean in `show interfaces status`? | The value was determined by autonegotiation |
| What is half duplex? Full duplex? | One direction at a time (walkie-talkie); both directions simultaneously (telephone) |
| What is a duplex mismatch? | The two ends of a link use different duplex modes; link stays up but throughput collapses and errors rise |
| Most common cause of a duplex mismatch? | One side manually fixed, the other side left on auto |
| Why does an auto side fall back to half duplex when the neighbor is fixed? | It can sense speed but not duplex without negotiation signals, so it picks half (works with any partner) |
| What does CSMA/CD stand for? | Carrier Sense Multiple Access with Collision Detection |
| What do Ethernet devices use to detect and prevent collisions on half-duplex interfaces? | CSMA/CD |
| Does full duplex use CSMA/CD? | No |
| All devices connected to an Ethernet hub are in the same ___ domain. | Collision |
| How many collision domains does a hub have? A switch? | One for the whole hub; one per switch port |
| What does the Status field of `show ip interface brief` show? | Layer 1 status |
| What does the Protocol field show? | Layer 2 status |
| What does `up/down` (Status/Protocol) indicate? | Layer 1 is fine but Layer 2 has a problem |
| What does `administratively down` mean? | Interface was disabled with `shutdown` |
| Which error counter counts frames smaller than 64 bytes? | runts |
| Which counter counts frames larger than the maximum size? | giants |
| Which counter counts frames failing the CRC check? | CRC |
| Which counter counts frames with an incorrect/illegal format? | frame |
| Which counter is the total of the various input error counters? | input errors |
| What is the bit pattern of one byte in the Ethernet Preamble? | `10101010` |
| What does SFD stand for? | Start Frame Delimiter |
| What kind of algorithm does the Ethernet FCS use? | CRC (Cyclic Redundancy Check) |
| What is the relationship between FCS and CRC? | FCS is the field; CRC is the algorithm that computes its value |
| What does ISR stand for? | Integrated Services Router |
| What kind of network device is a Cisco ISR? | Router |
| What is a host-based firewall? | A software firewall on an individual host that filters traffic entering/exiting that host |
| Which cable connects each pin to the same pin on the other end? | Straight-through |
| Usable hosts per Class A network? | 2^24 - 2 = 16,777,214 |
| Formula for usable hosts given n host bits? | 2^n - 2 |
| Why subtract 2 in the host formula? | Network address (all host bits 0) and broadcast address (all host bits 1) are unusable |
| What are Class D and Class E addresses for? | D = multicast (224-239); E = experimental (240-255) |
| What does "i.e." mean? "e.g."? | "that is" (restates); "for example" (gives an example) |

---

## My Study Log

- [x] Reviewed Cisco IOS CLI modes and prompts
- [x] Learned running-config vs startup-config and `copy run start`
- [x] Learned `enable password`, `enable secret`, `service password-encryption`
- [x] Learned console default settings (9600-8-N-1) and the terms baud/parity/stop bit
- [x] Deep-dived autonegotiation, `a-` prefix, duplex fallback and duplex mismatch
- [x] Learned CSMA/CD and collision domains (hub vs switch)
- [x] Learned Status (L1) vs Protocol (L2) in `show ip interface brief`
- [x] Learned `show interfaces` error counters (runts, giants, CRC, frame, input errors)
- [x] Recapped Preamble/SFD/FCS/CRC and the TCP/IP 5-layer model, adjacent vs same-layer interaction
- [x] Reviewed ISR, host-based firewall, straight-through vs crossover cables
- [x] Reviewed IPv4 host formula (2^n - 2) and Class D/E
- [ ] Packet Tracer lab: set speed/duplex on two switches, then create and observe a duplex mismatch
- [ ] Packet Tracer lab: `enable password` vs `enable secret` vs `service password-encryption`
- [ ] Re-do the Anki cards for Day 09 until no card is missed twice in a row

### Notes / Confusing Points

- Setting vs result: default is `auto`, the negotiated result is usually full duplex.
- `Status` = Layer 1, `Protocol` = Layer 2 (S before P, 1 before 2).
- "port" points to Layer 4; "IP address / router" points to Layer 3.
- (add your own notes here)
