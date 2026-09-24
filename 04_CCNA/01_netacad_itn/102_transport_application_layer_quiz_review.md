# Transport & Application Layer Quiz Review (Q1–32)

A consolidated review covering TCP/UDP fundamentals, transport layer responsibilities, the OSI vs TCP/IP model mapping, well-known application layer protocols, and port/window/sequence number calculations.

---

## 1. TCP vs UDP — Core Principle

| | TCP | UDP |
|---|---|---|
| Priority | **Reliability** | **Speed** |
| Connection | Connection-oriented (3-way handshake) | Connectionless ("just sends the datagrams") |
| Ordering | Sequence numbers → reassembles in correct order | No reordering — passes data through in the order received |
| Flow control | Yes (Window field) | None |
| Overhead | Higher | Low overhead |
| Error recovery | Detects (checksum) **and recovers** (retransmission) | Detects (checksum) only — no recovery; relies on the application layer if recovery is needed |
| Header fields | Source port, Destination port, **Sequence number, Acknowledgment number, Window, Flags (SYN/ACK/FIN)**, Checksum | Source port, Destination port, Length, **Checksum** (only 4 fields, ~8 bytes) |

**Rule of thumb:** Ask "Can this application tolerate some data loss in exchange for low delay?"
- Yes → UDP (video calls, live streaming, gaming, DNS, DHCP, TFTP, SNMP)
- No, must arrive perfectly → TCP (web pages, file transfer, email)

### Protocols that use TCP (need reliability)
**HTTP, FTP, SMTP** — anything where corrupted/missing data breaks the outcome (web pages, files, emails).

### Protocols that use UDP (need speed / can't wait for a connection)
**TFTP, SNMP, DHCP** — mnemonic: "**TSD** is UDP."
- TFTP: lightweight file transfer (the "Trivial" in the name hints at UDP)
- SNMP: short, periodic device status polling
- DHCP: happens *before* the client has an IP, so a TCP connection isn't even possible yet

### Why UDP is a good fit in two specific situations
1. Applications that **don't need to guarantee delivery** of the data.
2. Applications that **need a faster delivery mechanism** (no handshake, no ACK wait, no retransmission delay).

*Not* valid reasons to pick UDP: dynamic destination ports (irrelevant to the choice), or "overhead isn't an issue" (that's actually a reason TCP would be fine too — UDP is chosen specifically when overhead **is** a problem).

---

## 2. Checksum — What It Actually Is

A short numeric value in the header used purely to **detect** (not fix) corruption.

- **Sender**: runs a calculation over the segment/datagram's data → produces a checksum → sends it in the header.
- **Receiver**: re-runs the same calculation on the received data and compares it to the header's checksum.
  - Match → data is intact.
  - Mismatch → data was corrupted in transit → the segment/datagram is simply discarded.

**Both TCP and UDP include a checksum field.** The difference is what happens *after* a checksum failure:
- **TCP**: discards the bad segment, and its retransmission/ACK mechanism requests it again → self-recovering.
- **UDP**: discards the bad datagram and stops there — no retransmission request. Recovery (if needed at all) is left to the application layer running on top of UDP.

This is why "UDP relies on application layer protocols for error detection [recovery]" is considered a true characteristic of UDP, even though UDP itself does basic detection via checksum.

---

## 3. TCP Header Fields Unique to TCP (not in UDP)

UDP header = only **Source port, Destination port, Length, Checksum**.

TCP-only fields (because TCP needs to guarantee ordering, delivery, and pacing):
- **Sequence number** — labels each byte so segments can be **reassembled in the correct order** even if they arrive out of order.
- **Acknowledgment number** — tells the sender "I've received everything up through X; send me **X+1** next." (Different from sequence number: seq = "what byte is this," ack = "what I've confirmed receiving.")
- **Window** — used for **flow control**: tells the sender how much data the *receiver* can currently accept, so the sender doesn't overwhelm the receiver's buffer.
- **Flags** (SYN, ACK, FIN, etc.) — used to manage connection setup/teardown (e.g., the 3-way handshake).

### Window size calculation example
> TCP window size = 6,000 bytes, packet size = 1,500 bytes. After the server receives 2 packets, what byte does it acknowledge?

- Data actually received = 1,500 × 2 = 3,000 bytes.
- **ACK number = bytes received + 1** (ACK announces the *next expected byte*, not the count received).
- Answer: **3001**.
- Window size (6,000) is a red herring here — it only defines the *maximum* the receiver can accept before requiring an ACK; it is not the amount actually received.

### Sequence number recap
> What information does TCP use to reassemble and reorder received segments? → **Sequence numbers** (not acknowledgment numbers, not fragment numbers [that's an IP/network-layer concept], not port numbers).

---

## 4. Transport Layer — Core Responsibilities

Three of the six commonly-listed transport layer jobs are correct:
1. **Multiplexing** multiple communication streams from many users/apps over the same network.
2. **Identifying the applications and services** on client/server that should handle the data (via port numbers).
3. **Meeting the reliability requirements** of applications (choosing/enforcing TCP-style reliability or UDP-style speed).

Also correct (asked with slightly different wording in another question):
- **Providing the interface between apps and the network** (framed loosely) — *not* accepted as a correct answer in one specific question because it was too vague/general; the more precise transport-layer answers were "identifying the proper application for each stream" and "tracking individual communication between hosts."

**NOT transport layer responsibilities** (these belong to other layers):
- Formatting data for the destination device → **Presentation layer (OSI 6)**
- Error detection **of frames** (CRC) → **Data Link layer (OSI 2)**
- Frame delimiting → **Data Link layer (OSI 2)**
- Routing packets to the destination network → **Network layer (OSI 3)**

**Memory trick:** if the question says "frame," think Data Link (Layer 2). If it says "port" or "which application/stream," think Transport (Layer 4).

### Real-world scenario question
> Two browser windows open to two different sites — how does the transport layer know which page goes to which window?

Answer: each window gets a distinct **source port**, and the transport layer uses that to deliver the correct page to the correct window. (This is the *only* correct "transport layer function" among distractor scenarios describing Presentation-layer formatting/encoding, or Data-Link-layer MAC addressing.)

---

## 5. Port Numbers

- **Destination port** — identifies *which service* the data is going to (e.g., web server = 80).
- **Source port** — identifies *which session/program on the sender's machine* the data came from; lets the sender distinguish multiple simultaneous conversations to the same service (e.g., 3 browser tabs all hitting port 80, but each tab uses a different random source port).
- Port numbers exist for **both TCP and UDP** — UDP is not exempt from needing them.

### Well-known ports to memorize
| Port | Protocol |
|---|---|
| 20/21 | FTP |
| 25 | SMTP |
| 53 | DNS |
| 67 / 68 | DHCP (server / client) |
| 69 | TFTP |
| **80** | **HTTP** |
| 110 | POP3 |
| 443 | HTTPS |

---

## 6. Client/Server vs Peer-to-Peer (P2P)

| | Client/Server | Peer-to-Peer |
|---|---|---|
| Roles | **Fixed** — one device is always the server, others are always clients | **Fluid** — any device can act as client and server at the same time, depending on the moment |
| Dedicated server | Yes | **No dedicated server** |
| Resource location | Centralized | **Decentralized** (spread across peers) |
| User accounts | Often centrally managed | No central authority — each device manages its own |
| Data flow | N/A | Can be bidirectional/simultaneous (e.g., uploading and downloading in a torrent at once) |
| Scalability | Scales more predictably (add server capacity) | Actually scales *worse* as peers increase — no central coordination |

**What the two models have in common:** both involve devices that can act in **client and server roles** — Client/Server just fixes those roles permanently, while P2P lets the same device switch between them.

### Applications/protocols that allow a host to be client AND server simultaneously
✅ **P2P applications** (e.g., torrent clients) — not email apps or authentication services, which are strictly client/server.

### Named P2P protocol
- **WireShare, Bearshare, Shareaza** (file-sharing apps) all commonly use the **Gnutella** protocol.
- **eDonkey, eMule, BitTorrent, Bitcoin, LionShare** are all examples used in the **peer-to-peer** networking model (not "point-to-point" — that term refers to a 1:1 physical/logical link like PPP, a completely different concept from "peer-to-peer").

---

## 7. OSI 7-Layer Model vs TCP/IP 4-Layer Model

| OSI Layer | TCP/IP Layer | PDU | Core Function | Example Protocols | Related Device |
|---|---|---|---|---|---|
| 7. Application | ⎫ | Data | User-facing services | HTTP, FTP, SMTP, DNS, DHCP | – |
| 6. Presentation | ⎬ **Application** | Data | Formatting, **compression, encryption**, encoding | SSL/TLS, JPEG, ASCII | – |
| 5. Session | ⎭ | Data | Establishing/maintaining/ending a session (dialogue) between two hosts | NetBIOS, RPC | – |
| 4. Transport | Transport | **Segment** (TCP) / **Datagram** (UDP) | Ports, reliability vs speed, flow control, multiplexing | TCP, UDP | – |
| 3. Network | Internet | **Packet** | Logical (IP) addressing, routing | IP, ICMP | **Router** |
| 2. Data Link | Network Access | **Frame** | Physical (MAC) addressing, frame delimiting, CRC error detection | Ethernet, PPP | **Switch** |
| 1. Physical | ⎭ | **Bit** | Electrical signals, cabling, connectors | Cables | **Hub** |

### Key facts to memorize
1. **TCP/IP's single Application layer absorbs OSI's top 3 layers** (Application + Presentation + Session). This is the single most-tested mapping in this quiz set (appeared in Q19, Q21, Q29).
   - "Formatting/compressing/encrypting" → OSI Presentation → **TCP/IP Application**.
   - "Session establishment/management" → OSI Session → **TCP/IP Application**.
   - TCP/IP has **no separate "session" or "presentation" layer name** — if these appear as answer options in a TCP/IP-model question, they are traps (they don't exist as TCP/IP layers).
2. **Address types by layer:**
   - Logical address = **IP address** → Layer 3 (Network)
   - Physical address = **MAC address** → Layer 2 (Data Link)
   - Port number → Layer 4 (Transport)
3. **PDU (Protocol Data Unit) names change as headers are added going down the stack** (encapsulation):
   ```
   Data → Segment(TCP)/Datagram(UDP) → Packet → Frame → Bit
   ```
   Each layer wraps the data from the layer above with its own header (like nesting boxes). On the receiving end this unwraps in reverse (de-encapsulation).
4. **Device ↔ Layer inference works both ways:**
   - Router mentioned → Layer 3 (uses IP addresses to route)
   - Switch mentioned → Layer 2 (uses MAC addresses to forward frames)
   - Hub/cable mentioned → Layer 1 (raw electrical signal, no addressing concept)

---

## 8. Application Layer Protocols — What They Do

| Protocol | Purpose | Layer/Notes |
|---|---|---|
| **HTTP** | Web page transfer (GET = retrieve, POST = send/upload) | Application (TCP, port 80) |
| **FTP** | File transfer between client/server | Application (TCP) |
| **SMTP** | **Sending** email | Application (TCP, port 25) |
| **POP3 / POP** | **Receiving/retrieving** email from a mail server | Application (TCP, port 110) |
| **DNS** | Domain name → IP address resolution | Application (UDP typically, port 53) |
| **DHCP** | Automatic IP address assignment | Application (UDP, port 67/68) |
| **SSL/TLS** | Encrypts data (the "s" in https) | Presentation-layer function, absorbed into TCP/IP Application |
| **JPEG** | Image compression format | Presentation-layer function |
| **ASCII** | Character-to-binary encoding | Presentation-layer function |
| **NetBIOS** | Legacy Windows LAN name resolution/session establishment | Session-layer function |
| **RPC** | Remote Procedure Call — invoking a function on a remote host as if local | Session-layer function |
| **IP** | Addressing + routing | Network layer |
| **ICMP** | Network diagnostics (e.g., `ping`) | Network layer |
| **Ethernet** | Wired LAN standard | Data Link layer |
| **PPP** | Point-to-point (1:1) link protocol | Data Link layer |
| **ARP** | Resolves IP address → MAC address | Between Network/Data Link — **not** Application layer |
| **Gnutella** | P2P file-sharing protocol used by apps like WireShare/Bearshare/Shareaza | Application layer |
| **SMB (Server Message Block)** | Windows file/printer sharing; clients keep a **long-term/persistent connection** to the server for ongoing file operations (open/read/write/close), unlike FTP's separate control+data channel model | Application layer |

### Frequently tested groupings
- **TCP-using protocols:** HTTP, FTP, SMTP
- **UDP-using protocols:** TFTP, SNMP, DHCP
- **Web hosting service trio:** World Wide Web = **HTTP**, File Transfer = **FTP**, E-mail = **SMTP** (DNS/SNMP/DHCP are supporting infrastructure protocols, not "core application services" in this context)
- **Email-sending process protocols:** **SMTP** (send) + **POP** (receive) — note: in this particular question bank, the answer key accepts the option literally labeled "**POP**," not "**POP3**," even though POP3 is the technically precise name. When both appear as separate answer choices, check which one the grading key wants.
- **TCP/IP Application layer protocols (not Transport/Network/Data-Link):** FTP, HTTP, SNMP, SMTP, DHCP, DNS are Application; **TCP, UDP are Transport**; **ARP** sits between Network/Data-Link — none of the latter three belong in an "Application layer protocols" answer set.

---

## 9. DHCP Discover Message — Key Facts

When a client has no IP address yet, it **broadcasts** a DHCP Discover message to find a DHCP server:

- ✅ Comes **from a client** seeking an IP address (not from a server).
- ✅ **All hosts** on the network receive it, but **only a DHCP server replies**.
- ✅ **Destination IP = 255.255.255.255** (broadcast address).
- ❌ NOT: "only the DHCP server receives it" (everyone receives it; only the server responds).
- ❌ NOT: "source MAC = FF-FF-FF-FF-FF-FF" — that's the **destination** MAC (broadcast), not the source. The **source MAC is the client's real MAC address**.
- ❌ NOT: "comes from a server offering an IP" — that describes the *next* step, **DHCP Offer**, not Discover.

---

## 10. HTTP Methods

- **GET** — retrieves/requests data from the server (e.g., loading a page from a URL or clicking a link). Direction: server → client.
- **POST** — sends/uploads data to the server (e.g., submitting a form). Direction: client → server.
- Error info from server to client is handled by **HTTP status codes** (e.g., 404, 500), not by GET/POST themselves.
- Retrieving email via port 110 is **POP3**, unrelated to HTTP.

---

## 11. Quick-Reference Memory Rules

- **"TSD is UDP"** → TFTP, SNMP, DHCP use UDP.
- **"Port = Layer 4, IP = Layer 3, MAC = Layer 2"** for address types.
- **"TCP/IP Application = OSI's Application + Presentation + Session"** — no separate session/presentation layer exists in TCP/IP.
- **"ACK number = bytes received + 1"** (next expected byte, not total received).
- **Sequence number** → reassembly/ordering; **Acknowledgment number** → confirms receipt; don't confuse the two.
- **"CRC = Layer 2 error detection, Checksum = Layer 4 error detection, Routing = Layer 3."**
- **"Router → Layer 3 (IP); Switch → Layer 2 (MAC); Hub/cable → Layer 1 (signal)."**
- **"Point-to-point = a physical/logical 1:1 link (e.g., PPP); Peer-to-peer = a networking model where roles are fluid."** Easy to confuse by name only — different concepts entirely.
- Beware of absolute wording ("always," "never," "only") in answer choices — these are frequently traps that don't hold up against real exceptions (e.g., "UDP applications are always unreliable" is false because apps can implement their own reliability on top of UDP).
- Watch for **loosely-worded distractors** that sound plausible but describe the wrong layer entirely (e.g., "provides interface between applications and network" sounds like Transport but tested as too vague/incorrect versus more precise Transport-layer statements).

---

*Compiled from a 32-question review covering CCNA-style Transport Layer, Application Layer, TCP/UDP, OSI/TCP-IP model mapping, and client-server/P2P topics.*
