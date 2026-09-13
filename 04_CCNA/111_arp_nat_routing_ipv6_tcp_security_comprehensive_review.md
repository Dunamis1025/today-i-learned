# CCNA Comprehensive Review: ARP, NAT, Routing, IPv6, TCP, and Security

Covers CCNA: Introduction to Networks course final exam prep (Q18–55) plus surrounding concepts.

## Router behavior on receiving a Layer 2 frame

When a router receives a frame off the wire, its first action is to **de-encapsulate** it — strip the Layer 2 header to expose the packet. The full sequence:
1. De-encapsulate the incoming frame
2. Determine the best path (routing decision)
3. Re-encapsulate into a new frame for the outgoing interface
4. Forward onto the medium

## Default gateway misconfiguration

If the default gateway is misconfigured **on the host** (not the router):
- Local communication still works — same-subnet traffic goes through the switch, no gateway needed.
- Remote communication fails — the host sends packets to the wrong gateway address, so they never reach the actual router.
- Incoming replies can't be routed back out, since the return path also depends on the (wrong) gateway.

Contrast with other misconfigurations:
- Wrong IP/subnet mask → even local communication fails.
- Wrong gateway → local works, remote fails.
- Wrong DNS → communication works, but domain names don't resolve (IP access still works).

## IPv4 header fields

- **Destination IPv4 address**: the only field that can hold unicast, multicast, *or* broadcast — because it's the receiver's address. Source address must always be unicast (only one device can send).
- **Protocol**: identifies what's encapsulated. TCP = 6, UDP = 17, ICMP = 1.
- **Header checksum**: detects corruption in the header during transmission.
- **TTL**: decrements by 1 per router hop; discarded at 0 to prevent infinite looping.

## NAT (Network Address Translation)

- IPv4 has only ~4.3 billion addresses — far fewer than the number of devices worldwide.
- Private IP ranges (192.168.x.x, 10.x.x.x, 172.16–31.x.x) can't be routed directly on the internet.
- The router translates private → public IP when traffic leaves the LAN.
- Multiple devices sharing one public IP are distinguished by **port number** — this specific mechanism is called **PAT (Port Address Translation)** / NAT overload.
  - Example: 192.168.1.10:5000 → 203.0.113.5:40001; 192.168.1.11:5000 → 203.0.113.5:40002
- **IPv6 doesn't need NAT** — the address space is so large that every device can get its own public IPv6 address directly, eliminating the need for private-to-public translation.

## Routing table entry types

- **Directly-connected route**: network attached directly to a router interface. No next hop needed.
- **Local route**: the router's own interface address, shown as a /32 host route (all 32 bits pinned = exactly one address). No next hop needed.
- **Remote route**: reached via another router. Requires a **next hop address** — the IP of the next router in the path.

Key rule: only remote routes have a next hop; directly-connected and local routes don't.

## MAC address table / switch flooding behavior

When a switch receives a frame:
- If the **destination MAC** is in the MAC address table → forward out that port only (unicast forwarding).
- If the destination MAC is **not** in the table → **flood** to every port except the one the frame arrived on.

Important: whether *other* MAC addresses happen to already be in the table is irrelevant — flooding is decided purely by whether the *destination* of this specific frame is known. The switch also learns the *source* MAC of every incoming frame and records which port it came in on, regardless of what it does with that frame.

## ARP request/reply for a remote destination

When PC1 needs to reach PC3 on a different subnet:
1. PC1 recognizes (from subnet mask math) that PC3 is remote.
2. PC1 sends an ARP request as a **broadcast**, asking for its **default gateway's** MAC — not PC3's.
3. The broadcast reaches all devices via the switch; only the device whose IP matches (the router) responds.
4. The router replies with its own interface MAC as a **unicast**.
5. PC1 sends the actual data packet to the router using that MAC as the destination.
6. The router will separately ARP for PC3's real MAC — a later step, out of scope for this exchange.

Destination MAC address used in an ARP request frame: **FFFF.FFFF.FFFF** (Layer 2 broadcast, all 48 bits = 1). This differs from `255.255.255.255` (Layer 3 broadcast).

## MAC address notation

- MAC = 48 bits total (6 bytes).
- Cisco notation: 4 hex digits × 3 groups (FFFF.FFFF.FFFF) — 16 bits per group.
- Standard notation: 2 hex digits × 6 groups (FF:FF:FF:FF:FF:FF) — 8 bits per group.
- 1 hex digit = 4 bits (2⁴ = 16 possible values, matching hex's 16 symbols).
- 48 bits was chosen by IEEE — gives ~281 trillion addresses, judged sufficient without going to 64 bits.

## Subnetting — block size / magic number

For a given prefix, host bits = 32 − prefix. Block size = 2^(host bits).

Example: /29 → 3 host bits → block size 8.
- Subnet boundaries: 0–7, 8–15, 16–23...
- First address in each block = network address.
- Last address in each block = broadcast address.
- Everything in between = assignable unicast addresses.

`192.168.1.15/29` → falls in block 8–15 → last address → **broadcast address**.

## IPv6 special addresses

| Address | Meaning | IPv4 equivalent |
|---|---|---|
| `::1` (or `0:0:0:0:0:0:0:1`) | Loopback | 127.0.0.1 |
| `::` (all zeros) | Unspecified | 0.0.0.0 |
| `fe80::/10` | Link-local | 169.254.x.x (but always present/normal in IPv6, unlike IPv4's error-state APIPA) |
| `2000::/3` | Global unicast | Public IPv4 address |
| `ff00::/8` | Multicast | 224.0.0.0–239.255.255.255 |

IPv6 compression rules:
1. Leading zeros in each group can be dropped (`0220` → `220`).
2. One contiguous run of all-zero groups can be collapsed to `::` — only once per address.

## Reading a workstation's IPv6 routing table (`netstat -r`)

- `/64` entries represent the **network itself** (a range), not a specific host.
- `/128` entries represent exactly **one host address**.
- To identify which `/128` link-local address belongs to the local workstation (vs. a remote peer), compare the interface identifier (the latter portion of the address) against the workstation's known global unicast address — matching suffixes indicate the same interface.

`netstat -r` shows the routing table; `ipconfig`/`ifconfig` shows the assigned interface addresses — different purposes.

## TCP window size

- Defines the amount of data the sender can transmit **before requiring an acknowledgment** — this is TCP's flow control mechanism.
- Prevents overwhelming the receiver's buffer when sender/receiver processing speeds differ.
- **Not the same as bandwidth**: bandwidth is a property of the physical link (how much data the cable/wireless can carry per second — an infrastructure limit); window size is a property of the receiver's buffer capacity (a software/host limit).
- Random numbers in the 3-way handshake refer to sequence numbers, not window size.

## Well-known port numbers

| Service | Port |
|---|---|
| FTP (data/control) | 20 / 21 |
| SSH | 22 |
| Telnet | 23 |
| SMTP | 25 |
| DNS | 53 |
| DHCP (server/client) | 67 / 68 |
| TFTP | 69 |
| HTTP | 80 |
| HTTPS | 443 |

Port groups:
- **Well-known**: 0–1023
- **Registered**: 1024–49151
- **Private/dynamic (ephemeral)**: 49152–65535

## DNS-related commands

- `nslookup <domain>` — manually queries a DNS server to resolve a hostname.
- `ipconfig /displaydns` — shows the local **cached** DNS records (doesn't query the server).
- `tracert` — traces the path (hops) to a destination; unrelated to DNS.

## POP3 vs IMAP

- **POP3**: downloads email to the local client and deletes it from the server. Good for single-device mail management.
- **IMAP**: keeps mail on the server and syncs across devices. Standard for modern multi-device email.
- SMTP sends mail; Telnet/SSH provide remote access (unencrypted/encrypted respectively).

## Firewall types and OSI layers

- **Packet-filtering firewall**: evaluates each packet independently using Layer 3 (IP) and Layer 4 (port) info only. No memory of connection state. Filters up to the **transport layer**.
- **Stateful firewall**: tracks connection state/session, so it can recognize replies to established connections. Filters up to the **session layer**.
- Application-layer inspection (Layer 7) requires a next-generation firewall (NGFW) — beyond either of the above.

## Security concepts

- **DoS (Denial of Service)**: overwhelming a target (e.g., a firewall) with traffic until the service becomes unavailable to legitimate users. Keyword: "flooded with traffic."
- **Access attack**: unauthorized attempt to break into a system or data.
- **Trojan horse**: malware disguised as legitimate software.
- **Reconnaissance**: information-gathering phase before an attack (scanning for vulnerabilities).
- `login block-for X attempts Y within Z`: defends against **brute-force** password-guessing attacks by locking out login attempts after repeated failures in a short window.
- Malware defense: keep software updated (patches known vulnerabilities) + use antivirus software (detects/blocks malicious files in real time). Deleting unused software reduces attack surface but doesn't actively detect/block malware.

## Network models

- **Client-server (client-based)**: a dedicated server provides services; clients connect to request them. Example: Google Drive.
- **Peer-to-peer**: no dedicated server — each device (peer) can act as both server and client. Example: two students directly sharing a folder between their own computers.

## Redundancy planning

For internet-connection redundancy specifically (not server or LAN redundancy):
- Adding a second web server → redundancy for the *server*, not the connection.
- Adding a second NIC → redundancy *inside* the server, still single point of failure if same ISP/line.
- Adding switch-to-edge-router links → redundancy *inside* the LAN, not the external connection.
- **Adding a second ISP connection via a cheaper line (e.g., DSL)** → true internet-connection redundancy, and cost-effective since the backup doesn't need to match the primary leased line's cost.

Terminology:
- **Leased line**: a dedicated, non-shared connection to an ISP — stable, secure, always-on, but expensive.
- **Edge router**: the router at the boundary between the internal LAN and the external internet — the "gateway" for the whole organization.
- **DSL**: uses existing copper telephone lines to carry internet signal; ADSL (asymmetric DSL) has faster download than upload speed — the technology behind Korea's early broadband rollout.
